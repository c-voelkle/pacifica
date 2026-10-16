import os
import re
import time
import json
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel
from google import genai
from google.genai import types

load_dotenv()
console = Console()

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
    http_options=types.HttpOptions(timeout=300_000)
)

MODEL_ID = "gemini-4-argon"
BEATS_FILE = Path("beats.json")
BIBLE_FILE = Path("bible.md")
SKILL_FILE = Path("skills/archival_voices.md")
INJECTOR_FILE = Path("inject_archives.py")
PROGRESS_FILE = Path("archival_discovery_progress.json")

SEED_KEYS = ["FUSETSUGAKI", "HYORYUKI", "HAWAIIAN_MELE", "NUPEPA_LETTER", "CLIOMETRIC_DATASET"]

class BespokeVoice(BaseModel):
    voice_key: str
    voice_title: str
    originating_beats_and_stage: str
    sierpinski_vertex_alignment: str
    historical_context_and_medium: str
    voice_register_and_linguistic_quirks: str
    sample_attribution_line: str
    recommended_word_length: str
    chapter_or_scene_placement_ideas: str

class StageDiscovery(BaseModel):
    era_title: str
    beat_range: str
    newly_invented_voices: list[BespokeVoice]

def sync_outputs(seed_skill: str, completed_eras: dict, discovered_keys: list[str]):
    """Writes current progress immediately to skills/archival_voices.md and inject_archives.py."""
    all_eras_md = ["## DISCOVERED BESPOKE VOICES BY NARRATIVE ERA (GENERATED FROM BEATS.JSON)\n"]
    for era_key in sorted(completed_eras.keys(), key=lambda x: int(x)):
        all_eras_md.append(completed_eras[era_key]["markdown"])

    full_skill = seed_skill + "\n\n---\n\n" + "\n\n".join(all_eras_md) + "\n"
    SKILL_FILE.write_text(full_skill, encoding="utf-8")

    if INJECTOR_FILE.exists():
        inj_code = INJECTOR_FILE.read_text(encoding="utf-8")
        keys_formatted = "VOICE_KEYS = [\n" + "\n".join(f'    "{k}",' for k in discovered_keys) + "\n]"
        inj_code = re.sub(r'VOICE_KEYS\s*=\s*\[.*?\]', keys_formatted, inj_code, flags=re.DOTALL)
        INJECTOR_FILE.write_text(inj_code, encoding="utf-8")

def discover_voices_from_beats(beats_per_era: int = 30):
    if not BEATS_FILE.exists():
        raise FileNotFoundError("beats.json not found.")

    beats = json.loads(BEATS_FILE.read_text(encoding="utf-8", errors="replace"))
    bible = BIBLE_FILE.read_text(encoding="utf-8", errors="replace") if BIBLE_FILE.exists() else ""
    seed_skill = SKILL_FILE.read_text(encoding="utf-8", errors="replace").split("## DISCOVERED")[0].rstrip()

    # Load existing progress if resuming after a timeout
    if PROGRESS_FILE.exists():
        state = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        completed_eras = state.get("completed_eras", {})
        discovered_keys = state.get("discovered_keys", list(SEED_KEYS))
        console.print(f"[yellow]Resuming from checkpoint: {len(completed_eras)} era(s) already saved.[/yellow]")
    else:
        completed_eras = {}
        discovered_keys = list(SEED_KEYS)

    for start_idx in range(0, len(beats), beats_per_era):
        era_id = str(start_idx)
        era_beats = beats[start_idx:start_idx + beats_per_era]
        first_id = era_beats[0].get("beat_id", start_idx + 1)
        last_id = era_beats[-1].get("beat_id", start_idx + len(era_beats))

        if era_id in completed_eras:
            console.print(f"[dim]Skipping Beats {first_id}..{last_id} (already saved in checkpoint).[/dim]")
            continue

        beats_text = "\n".join(
            f"Beat {b.get('beat_id')} (Ch {b.get('chapter', '?')} - {b.get('location', '')}): {b.get('action', '')}"
            for b in era_beats
        )

        console.print(f"\n[bold cyan]Mining Beats {first_id}..{last_id} for unique cultural, technical & human archival voices...[/bold cyan]")

        prompt = f"""You are the Literary Worldbuilding Architect for 'The Grand Confederation of Pacifica'.
Below are our 5 Core Exemplar Voices (`FUSETSUGAKI`, `HYORYUKI`, `HAWAIIAN_MELE`, `NUPEPA_LETTER`, `CLIOMETRIC_DATASET`), the World Bible, and Beats {first_id} through {last_id} of the novel.

[WORLD BIBLE]
{bible}

[EXISTING VOICE KEYS (DO NOT DUPLICATE THESE)]
{", ".join(discovered_keys)}

[BEATS {first_id} TO {last_id}]
{beats_text}

[TASK]
Analyze the specific events, geographies, subcultures, technologies, treaties, and human/romantic tragedies occurring in Beats {first_id}–{last_id}.
Invent **3 to 4 brand-new, hyper-specific archival document voices** uniquely tailored to this stage of the narrative—with the same level of cultural specificity, local flavor, and structural brilliance as the *Hawaiian Mele layered with kaona* or the *Kuroshio castaway fisherman's journal*.

CRITICAL DESIGN CRITERIA FOR NEW VOICES:
1. **No Generic Templates:** Do not invent bland categories like "Newspaper Article" or "Military Report". Invent hyper-specific historical artifacts organic to these exact beats.
2. **Sierpinski Triadic Balance Across the 3–4 Voices:**
   - At least one voice must embody **Vertex 1 (The Ledger: technocracy, engineering, cryptography, finance, or future cliometrics)**.
   - At least one voice must embody **Vertex 2 (The Crucible: bottom-up vernacular, foreign/indigenous local eyes, sensory friction, labor, or sea)**.
   - At least one voice must embody **Vertex 3 (The Covenant & Its Shadows: pure tragic love, brotherhood in arms, filial piety, jealousy, obsession, or intimate relics left behind)**.
3. Give each voice a crisp UPPER_SNAKE_CASE `voice_key`.
"""

        resp = None
        for attempt in range(1, 7):
            try:
                resp = client.models.generate_content(
                    model=MODEL_ID,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                        response_schema=StageDiscovery,
                        temperature=0.7,
                    ),
                )
                break
            except Exception as e:
                wait_s = 15 * attempt
                console.print(f"[bold yellow]Attempt {attempt}/6 warning ({e}). Retrying in {wait_s}s...[/bold yellow]")
                time.sleep(wait_s)

        if resp is None:
            raise RuntimeError(f"Failed on Beats {first_id}..{last_id} after 6 attempts. Run script again to resume!")

        stage_data = StageDiscovery.model_validate_json(resp.text)
        era_md_lines = [f"### Era: {stage_data.era_title} (Beats {first_id}–{last_id})\n"]

        for v in stage_data.newly_invented_voices:
            clean_key = re.sub(r'[^A-Z0-9_]', '_', v.voice_key.upper()).strip('_')
            if clean_key not in discovered_keys:
                discovered_keys.append(clean_key)

            console.print(Panel(
                f"[bold yellow]{v.voice_title}[/bold yellow] ({v.sierpinski_vertex_alignment})\n"
                f"[cyan]Beats/Stage:[/cyan] {v.originating_beats_and_stage}\n"
                f"[white]{v.historical_context_and_medium}[/white]\n"
                f"[dim]Register:[/dim] {v.voice_register_and_linguistic_quirks}\n"
                f"[green]Placement Idea:[/green] {v.chapter_or_scene_placement_ideas}",
                title=f"NEW VOICE: {clean_key}"
            ))

            era_md_lines.append(f"""#### `{clean_key}` — {v.voice_title}
- **Originating Stage:** {v.originating_beats_and_stage}
- **Sierpiński Alignment:** {v.sierpinski_vertex_alignment}
- **Historical Context & Medium:** {v.historical_context_and_medium}
- **Voice, Register & Linguistic Quirks:** {v.voice_register_and_linguistic_quirks}
- **Sample Attribution:** `> — *{v.sample_attribution_line}*`
- **Recommended Length:** {v.recommended_word_length}
- **Best Narrative Placement:** {v.chapter_or_scene_placement_ideas}
""")

        completed_eras[era_id] = {
            "era_title": stage_data.era_title,
            "markdown": "\n".join(era_md_lines)
        }

        # Save checkpoint & update skill files immediately after every single era!
        PROGRESS_FILE.write_text(json.dumps({
            "completed_eras": completed_eras,
            "discovered_keys": discovered_keys
        }, indent=2), encoding="utf-8")
        sync_outputs(seed_skill, completed_eras, discovered_keys)
        console.print(f"[green]Checkpoint saved for Beats {first_id}..{last_id} ({len(discovered_keys)} total voices in repository).[/green]")

    console.print(f"\n[bold green]All eras complete! Saved {len(discovered_keys)} bespoke voices to {SKILL_FILE} and {INJECTOR_FILE.name}![/bold green]")

if __name__ == "__main__":
    discover_voices_from_beats(beats_per_era=30)
