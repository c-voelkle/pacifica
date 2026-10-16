import os
import re
import json
import time
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from google import genai
from google.genai import types

load_dotenv()
console = Console()

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
    http_options=types.HttpOptions(timeout=180_000)
)

MODEL_ID = "gemini-4-argon"
SKILL_TEXT = Path("skills/literary_style_skill.md").read_text(encoding="utf-8", errors="replace")
PROGRESS_FILE = Path("polish_progress.json")
OUTPUT_FILE = Path("manuscript_polished.md")

EDITOR_SYSTEM_PROMPT = f"""You are a master literary line editor working on a historical novel.
Rewrite the provided [DRAFT PASSAGE TO LINE-EDIT] to eliminate AI-generated prose tells while applying the literary craft rules below.

{SKILL_TEXT}

CRITICAL EXECUTION RULES:
1. Preserve 100% of plot actions, historical details, character names, dialogue meaning, and scene transitions.
2. NEVER summarize, abridge, or skip paragraphs. Your output word count must remain between 85% and 100% of the input passage word count.
3. Do NOT borrow nouns or imagery from the style guide examples. Use only the world and objects present in the draft passage.
4. Seamlessly match the tone and flow of the [PREVIOUS POLISHED CONTEXT] if provided, but output ONLY the rewritten version of [DRAFT PASSAGE TO LINE-EDIT].
"""

def chunk_manuscript_by_paragraphs(text: str, target_words: int = 2000) -> list[str]:
    paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    chunks, current_chunk, current_words = [], [], 0
    for p in paras:
        w = len(p.split())
        if current_words + w > target_words and current_chunk:
            chunks.append("\n\n".join(current_chunk))
            current_chunk, current_words = [p], w
        else:
            current_chunk.append(p)
            current_words += w
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))
    return chunks

def polish_manuscript():
    raw_text = Path("manuscript.md").read_text(encoding="utf-8", errors="replace")
    chunks = chunk_manuscript_by_paragraphs(raw_text, target_words=2000)
    
    completed_idx = -1
    prev_tail = ""
    if PROGRESS_FILE.exists() and OUTPUT_FILE.exists():
        state = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        completed_idx = state.get("last_completed_chunk", -1)
        existing_out = OUTPUT_FILE.read_text(encoding="utf-8", errors="replace")
        prev_tail = " ".join(existing_out.split()[-250:])
    elif OUTPUT_FILE.exists():
        OUTPUT_FILE.unlink()

    console.print(f"[bold cyan]Total chunks to line-edit: {len(chunks)} (Starting at chunk {completed_idx + 2}/{len(chunks)})[/bold cyan]")

    for idx, chunk in enumerate(chunks):
        if idx <= completed_idx:
            continue

        orig_words = len(chunk.split())
        console.print(f"[bold blue]Polishing Chunk {idx + 1}/{len(chunks)} ({orig_words} words)...[/bold blue]")

        prompt = f"""[PREVIOUS POLISHED CONTEXT (READ-ONLY FOR FLOW - DO NOT REPEAT)]
{prev_tail if prev_tail else "(Start of Manuscript)"}

[DRAFT PASSAGE TO LINE-EDIT]
{chunk}"""

        for attempt in range(1, 6):
            try:
                resp = client.models.generate_content(
                    model=MODEL_ID,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=EDITOR_SYSTEM_PROMPT,
                        temperature=0.45,
                        max_output_tokens=16384,
                    ),
                )
                edited_text = (resp.text or "").strip()
                new_words = len(edited_text.split())

                if new_words < int(orig_words * 0.72):
                    raise ValueError(f"Output too short ({new_words}/{orig_words} words) - possible truncation.")

                with OUTPUT_FILE.open("a", encoding="utf-8") as f:
                    f.write(edited_text + "\n\n")

                prev_tail = " ".join(edited_text.split()[-250:])
                PROGRESS_FILE.write_text(json.dumps({"last_completed_chunk": idx}), encoding="utf-8")
                
                ratio = round((new_words / orig_words) * 100, 1)
                console.print(f"[green]Chunk {idx + 1}/{len(chunks)} complete: {orig_words} -> {new_words} words ({ratio}%)[/green]")
                break
            except Exception as e:
                wait_s = min(15 * attempt, 60)
                console.print(f"[yellow]Attempt {attempt} warning ({e}). Retrying in {wait_s}s...[/yellow]")
                time.sleep(wait_s)
        else:
            raise RuntimeError(f"Failed to polish chunk {idx + 1} after 5 attempts.")

    console.print("[bold green]All chunks polished! Saved to manuscript_polished.md[/bold green]")

if __name__ == "__main__":
    polish_manuscript()
