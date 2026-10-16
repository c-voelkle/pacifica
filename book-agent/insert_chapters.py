import os
import re
import json
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from google import genai
from google.genai import types
from pydantic import BaseModel

load_dotenv()
console = Console()

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
    http_options=types.HttpOptions(timeout=300_000)
)

MODEL_ID = "gemini-4-argon"
SOURCE_FILE = Path("manuscript_polished.md") if Path("manuscript_polished.md").exists() else Path("manuscript.md")
OUTPUT_FILE = Path("manuscript_chaptered.md")
BEATS_FILE = Path("beats.json")

class ChapterBreak(BaseModel):
    chapter_number: int
    chapter_title: str
    start_paragraph_id: int
    inflection_reason: str

class ChapterMap(BaseModel):
    chapters: list[ChapterBreak]

def build_paragraph_digest(paras: list[str]) -> str:
    """Creates a compact index of all paragraphs with cumulative word counts and scene breaks."""
    digest_lines = []
    cum_words = 0
    for idx, p in enumerate(paras):
        w = len(p.split())
        cum_words += w
        if p in ("***", "---", "* * *"):
            digest_lines.append(f"[P{idx} | Words: {cum_words}] === EXISTING SCENE BREAK (***) ===")
        else:
            words = p.split()
            if len(words) <= 24:
                snippet = p
            else:
                snippet = " ".join(words[:14]) + " ... " + " ".join(words[-8:])
            digest_lines.append(f"[P{idx} | Words: {cum_words}] {snippet}")
    return "\n".join(digest_lines)

def map_chapters():
    raw_text = SOURCE_FILE.read_text(encoding="utf-8", errors="replace")
    # Strip any old auto-headers if present
    paras = [p.strip() for p in re.split(r'\n\s*\n', raw_text) if p.strip() and not re.match(r'^#{1,2}\s+', p.strip())]
    total_words = sum(len(p.split()) for p in paras)

    console.print(f"[bold cyan]Loaded {SOURCE_FILE.name}: {len(paras)} paragraphs ({total_words:,} words).[/bold cyan]")

    beats_summary = ""
    if BEATS_FILE.exists():
        beats = json.loads(BEATS_FILE.read_text(encoding="utf-8", errors="replace"))
        ch_groups = {}
        for b in beats:
            ch_groups.setdefault(b.get("chapter", 1), []).append(f"Beat {b['beat_id']}: {b['action']}")
        beats_summary = "\n".join(
            f"Planned Chapter {ch}: " + " | ".join(actions)
            for ch, actions in sorted(ch_groups.items())
        )

    digest = build_paragraph_digest(paras)
    target_chapters = max(20, min(36, round(total_words / 5800)))

    prompt = f"""You are the structural editor for a {total_words:,}-word historical novel.
Below is the original beat outline and the complete Paragraph Index ([P0] through [P{len(paras)-1}]) of the finished manuscript.

[ORIGINAL CHAPTER & BEAT OUTLINE]
{beats_summary}

[MANUSCRIPT PARAGRAPH INDEX]
{digest}

[TASK]
Divide this manuscript into approximately {target_chapters} chapters (aiming for 4,000 to 8,000 words per chapter, though dramatic inflection points always take priority over exact word count).

CRITICAL RULES FOR CHAPTER PLACEMENT:
1. Chapter 1 MUST start at `start_paragraph_id: 0`.
2. Every subsequent chapter MUST start at a genuine narrative inflection point:
   - Immediately after an existing `***` scene break (choose the paragraph right AFTER the `***` break), OR
   - At a major shift in location, POV character, or time ("By the third night...", "Three hundred miles west...", etc.), OR
   - Immediately following a high-impact dramatic resolution or cliffhanger line.
3. NEVER place a chapter break in the middle of an ongoing dialogue exchange or continuous physical action.
4. Give each chapter an evocative, period-authentic literary title (e.g., "The Drumhead at Tucson", "Iron on the Grade", "The Hankow Inspectorate"). Do NOT include "Chapter X:" inside `chapter_title`—only the title itself.
"""

    console.print(f"[bold blue]Analyzing full narrative arc via {MODEL_ID} to pinpoint ~{target_chapters} chapter inflection points...[/bold blue]")

    resp = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ChapterMap,
            temperature=0.2,
            max_output_tokens=8192,
        ),
    )

    chapter_map = ChapterMap.model_validate_json(resp.text)
    breaks = sorted(chapter_map.chapters, key=lambda x: x.start_paragraph_id)
    if not breaks or breaks[0].start_paragraph_id != 0:
        breaks.insert(0, ChapterBreak(chapter_number=1, chapter_title="Prologue", start_paragraph_id=0, inflection_reason="Start of book"))

    # Map start_paragraph_id -> header string
    break_lookup = {}
    for idx, brk in enumerate(breaks, start=1):
        pid = max(0, min(len(paras) - 1, brk.start_paragraph_id))
        # If the model pointed directly at a '***' line, advance 1 paragraph so header appears after the break
        if paras[pid] in ("***", "---", "* * *") and pid + 1 < len(paras):
            pid += 1
        break_lookup[pid] = (idx, brk.chapter_title, brk.inflection_reason)

    output_blocks = []
    for idx, p in enumerate(paras):
        if idx in break_lookup:
            ch_num, ch_title, reason = break_lookup[idx]
            # Remove redundant scene break right before a new chapter header
            if output_blocks and output_blocks[-1] in ("***", "---", "* * *"):
                output_blocks.pop()
            header = f"# Chapter {ch_num}: {ch_title}"
            output_blocks.append(header)
            console.print(f"[green]{header}[/green] [dim](@ P{idx}: {reason})[/dim]")
        output_blocks.append(p)

    OUTPUT_FILE.write_text("\n\n".join(output_blocks) + "\n", encoding="utf-8")
    console.print(f"\n[bold green]Successfully injected {len(break_lookup)} narrative chapter breaks into {OUTPUT_FILE.name}![/bold green]")

if __name__ == "__main__":
    map_chapters()
