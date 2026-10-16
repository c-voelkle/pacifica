import os
import json
import time
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from google import genai
from google.genai import types
from pydantic import BaseModel
from tools import get_manuscript_and_seam, commit_sliding_seam_pass

load_dotenv()
console = Console()

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
    http_options=types.HttpOptions(timeout=180_000)
)

WRITER_MODEL_ID = "gemini-4-argon"
AUDIT_MODEL_ID = "gemini-3-flash-preview"

class ContinuityAudit(BaseModel):
    overused_phrases_to_ban: list[str]
    unresolved_continuity_errors: list[str]
    pacing_directive_for_next_pass: str

class WritingPassOutput(BaseModel):
    rewritten_seam_and_new_prose: str
    completed_beat_ids: list[int]
    paused_mid_scene_note: str

SYSTEM_INSTRUCTION = """You are an autonomous long-form literary novelist engine.
You are writing a single, unbroken novel.

CRITICAL RULES OF THE SLIDING SEAM:
1. You will be given the Story Bible, the log of completed beats, the recent manuscript window ([LOCKED MANUSCRIPT]), and the [MALLEABLE 500-WORD SEAM].
2. Your `rewritten_seam_and_new_prose` MUST begin by seamlessly rewriting and polishing the [MALLEABLE 500-WORD SEAM] so there is zero tonal or structural break, then continuing directly into the assigned pending beats.
3. NEVER end your generation at the end of a chapter or at a neat emotional resolution.
4. Unless you are executing the final beat of the entire book, you MUST stop your prose in the middle of an active scene, dialogue exchange, or physical action in the last assigned beat.
5. Never summarize time ("Over the next few days..."). Render every beat in immediate sensory prose.
"""

def generate_with_retry(model_id: str, prompt: str, config: types.GenerateContentConfig, max_attempts: int = 8):
    for attempt in range(1, max_attempts + 1):
        try:
            return client.models.generate_content(
                model=model_id,
                contents=prompt,
                config=config,
            )
        except Exception as e:
            wait_sec = min(15 * attempt, 60)
            console.print(f"[yellow]Timeout or transient error ({type(e).__name__}: {str(e)[:80]}). Retrying in {wait_sec}s ({attempt}/{max_attempts})...[/yellow]")
            time.sleep(wait_sec)
    raise RuntimeError("Max retries exceeded.")

def run_continuity_audit(bible: str, recent_manuscript: str) -> ContinuityAudit:
    console.print("[bold yellow]Running fast Continuity & Lexical Audit (12k window via Flash)...[/bold yellow]")
    audit_excerpt = " ".join(recent_manuscript.split()[-12000:])
    prompt = f"""
    [STORY BIBLE]
    {bible}

    [RECENT MANUSCRIPT EXCERPT (LAST 12,000 WORDS)]
    {audit_excerpt}

    Identify any metaphors, verbs, or physical tics repeated too often in this recent excerpt, any continuity drift against the Bible, and provide a 1-sentence pacing directive for the next writing pass.
    """
    try:
        response = generate_with_retry(
            model_id=AUDIT_MODEL_ID,
            prompt=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ContinuityAudit,
                temperature=0.2,
                max_output_tokens=2048,
            ),
            max_attempts=3
        )
        return ContinuityAudit.model_validate_json(response.text)
    except Exception as e:
        console.print(f"[yellow]Audit skipped due to error ({e}); continuing writing pass...[/yellow]")
        return ContinuityAudit(
            overused_phrases_to_ban=[],
            unresolved_continuity_errors=[],
            pacing_directive_for_next_pass="Keep scene momentum sharp and concrete."
        )

def run_book_pipeline(beats_per_pass: int = 3):
    bible = Path("bible.md").read_text(encoding="utf-8")
    dynamic_bans: list[str] = []
    pacing_note = "Maintain tight, tactile pacing and keep scene momentum moving forward."
    pass_counter = 0

    while True:
        beats = json.loads(Path("beats.json").read_text(encoding="utf-8"))
        completed_beats = [
            f"Beat {b['beat_id']} (Ch.{b['chapter']}): {b['action']}"
            for b in beats if b["status"] == "completed"
        ]
        pending_beats = [b for b in beats if b["status"] == "pending"]
        
        if not pending_beats:
            console.print("[bold green]All beats completed! Full manuscript is ready in manuscript.md.[/bold green]")
            break

        current_batch = pending_beats[:beats_per_pass]
        is_final_batch = len(pending_beats) <= beats_per_pass
        locked_body, seam = get_manuscript_and_seam(seam_word_count=500, max_context_words=35000)

        if pass_counter > 0 and pass_counter % 3 == 0:
            audit = run_continuity_audit(bible, locked_body + "\n\n" + seam)
            dynamic_bans.extend(audit.overused_phrases_to_ban)
            dynamic_bans = list(set(dynamic_bans))[-25:]
            pacing_note = audit.pacing_directive_for_next_pass
            console.print(f"[cyan]Audit updated bans:[/cyan] {dynamic_bans}")

        prompt = f"""[STORY BIBLE - STATIC PREFIX]
{bible}

[COMPLETED STORY SO FAR - BEAT LOG]
{chr(10).join(completed_beats[-60:]) if completed_beats else "(None yet)"}

[LOCKED MANUSCRIPT WINDOW (RECENT 35,000 WORDS) - DO NOT ALTER]
{locked_body if locked_body else "(Start of Book)"}

[MALLEABLE 500-WORD SEAM - REWRITE AND CONTINUE FROM HERE]
{seam if seam else "(No seam yet - begin Beat 1 directly)"}

[ACTIVE NEGATIVE CONSTRAINTS - BANNED PHRASES/TICS]
{json.dumps(dynamic_bans)}

[EDITORIAL PACING DIRECTIVE]
{pacing_note}

[CURRENT ASSIGNED BEATS TO EXECUTE]
{json.dumps(current_batch, indent=2)}

[EXECUTION INSTRUCTION]
Write approximately {sum(b['target_words'] for b in current_batch)} words total (including the 500-word rewritten seam) covering Beats {[b['beat_id'] for b in current_batch]}.
{"This is the final batch of the book; bring the narrative to its ultimate conclusion." if is_final_batch else "STOP MID-SCENE inside the final beat of this batch while characters are actively speaking or moving."}
Return the JSON output with your rewritten seam + new prose.
"""

        console.print(f"[bold blue]Executing Pass #{pass_counter + 1} for Beats {[b['beat_id'] for b in current_batch]}...[/bold blue]")

        response = generate_with_retry(
            model_id=WRITER_MODEL_ID,
            prompt=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                response_mime_type="application/json",
                response_schema=WritingPassOutput,
                temperature=0.85,
                max_output_tokens=16384,
            ),
        )

        pass_data = WritingPassOutput.model_validate_json(response.text)
        status_msg = commit_sliding_seam_pass(
            rewritten_seam_and_new_prose=pass_data.rewritten_seam_and_new_prose,
            completed_beat_ids=pass_data.completed_beat_ids,
            paused_mid_scene_note=pass_data.paused_mid_scene_note,
        )
        console.print(f"[green]{status_msg}[/green]")

        usage = response.usage_metadata
        cached_tokens = getattr(usage, "cached_content_token_count", 0) or 0
        console.print(
            f"[dim]Pass complete | Input tokens: {usage.prompt_token_count} "
            f"(Cached: {cached_tokens}) | Output tokens: {usage.candidates_token_count}[/dim]"
        )
        pass_counter += 1

if __name__ == "__main__":
    run_book_pipeline(beats_per_pass=3)
