import os
import re
import sys
import shutil
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel
from rich.console import Console
from google import genai
from google.genai import types

load_dotenv()
console = Console()

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
    http_options=types.HttpOptions(timeout=300_000)
)

MODEL_ID = "gemini-4-argon"
MANUSCRIPT_FILE = Path("manuscript_chaptered.md")
BIBLE_TEXT = Path("bible.md").read_text(encoding="utf-8", errors="replace") if Path("bible.md").exists() else ""
SKILL_TEXT = Path("skills/literary_style_skill.md").read_text(encoding="utf-8", errors="replace") if Path("skills/literary_style_skill.md").exists() else ""

class InsertionTarget(BaseModel):
    paragraph_id: int
    chapter_context: str
    specific_instruction: str

class ThreadPlan(BaseModel):
    targets: list[InsertionTarget]

def weave_narrative_thread(thread_description: str, max_spots: int = 6):
    raw_text = MANUSCRIPT_FILE.read_text(encoding="utf-8", errors="replace")
    paras = [p.strip() for p in re.split(r'\n\s*\n', raw_text) if p.strip()]

    # Build lightweight paragraph digest for the planner
    digest_lines = []
    cur_ch = "Chapter 1"
    for idx, p in enumerate(paras):
        if p.startswith("#"):
            cur_ch = p.lstrip("# ").strip()
            digest_lines.append(f"[P{idx}] === {cur_ch} ===")
        elif len(p.split()) > 15:
            words = p.split()
            digest_lines.append(f"[P{idx} | {cur_ch}] {' '.join(words[:12])} ... {' '.join(words[-6:])}")

    plan_prompt = f"""You are a developmental editor weaving a new narrative thread across a finished historical novel.

[NARRATIVE THREAD TO WEAVE ACROSS THE NOVEL]
{thread_description}

[MANUSCRIPT PARAGRAPH INDEX]
{chr(10).join(digest_lines)}

[TASK]
Select up to {max_spots} specific paragraph IDs across the novel where this thread can be naturally woven into the existing scene (either by expanding the paragraph or adding a short exchange/detail) so the thread develops organically over time.
Never select a `# Chapter` heading or `***` line.
"""

    console.print(f"[bold blue]Scanning full manuscript to find the {max_spots} best insertion points for your thread...[/bold blue]")
    plan_resp = client.models.generate_content(
        model=MODEL_ID,
        contents=plan_prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ThreadPlan,
            temperature=0.2,
        ),
    )
    plan = ThreadPlan.model_validate_json(plan_resp.text)

    for i, t in enumerate(plan.targets, 1):
        console.print(f"  [cyan]{i}. [P{t.paragraph_id} - {t.chapter_context}]:[/cyan] {t.specific_instruction}")

    # Inject [[WEAVE: ...]] directives into those exact paragraphs so coauthor_pass.py can execute or preview them!
    modified_paras = list(paras)
    for t in plan.targets:
        pid = max(0, min(len(modified_paras) - 1, t.paragraph_id))
        modified_paras[pid] = f"{modified_paras[pid]}\n\n[[WEAVE THREAD: {t.specific_instruction}]]"

    MANUSCRIPT_FILE.write_text("\n\n".join(modified_paras) + "\n", encoding="utf-8")
    console.print(f"\n[bold green]Planted {len(plan.targets)} [[WEAVE THREAD: ...]] markers into {MANUSCRIPT_FILE.name}![/bold green]")
    console.print("[yellow]Run `python coauthor_pass.py --dry-run` to inspect them (or edit the markers yourself), then run `python coauthor_pass.py` to execute them all![/yellow]")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        console.print('Usage: python weave_thread.py "Describe the recurring motif, subplot, or worldbuilding context you want woven across the novel"')
    else:
        weave_narrative_thread(sys.argv[1])
