import os
import re
import sys
import shutil
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
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
WORKBENCH_FILE = Path("workbench_chapter.md")
BIBLE_TEXT = Path("bible.md").read_text(encoding="utf-8", errors="replace") if Path("bible.md").exists() else ""
SKILL_TEXT = Path("skills/literary_style_skill.md").read_text(encoding="utf-8", errors="replace") if Path("skills/literary_style_skill.md").exists() else ""

def split_chapters(raw_text: str) -> list[tuple[str, str]]:
    normalized = re.sub(r'(?m)^(#{1,3}\s+.+)$', r'\n\n\1\n\n', raw_text)
    blocks = [b.strip() for b in re.split(r'\n\s*\n', normalized) if b.strip()]
    chapters = []
    cur_header = "# Chapter 1"
    cur_paras = []
    for b in blocks:
        if re.match(r'^#{1,3}\s+', b):
            if cur_paras:
                chapters.append((cur_header, "\n\n".join(cur_paras)))
                cur_paras = []
            cur_header = b
        else:
            cur_paras.append(b)
    if cur_paras:
        chapters.append((cur_header, "\n\n".join(cur_paras)))
    return chapters

def checkout_chapter(ch_num: int):
    chapters = split_chapters(MANUSCRIPT_FILE.read_text(encoding="utf-8", errors="replace"))
    if ch_num < 1 or ch_num > len(chapters):
        raise ValueError(f"Chapter {ch_num} out of range (1..{len(chapters)}).")
    
    header, body = chapters[ch_num - 1]
    template = f"""<!-- CHAPTER_INDEX: {ch_num} -->
[DIRECTOR'S NOTES FOR THIS CHAPTER]
- Pacing / Expansion: (e.g., Expand this chapter by ~1,000 words. Slow down the opening scene and establish the physical setting and economic stakes before the dialogue starts.)
- Character / Subtext: (e.g., Give Elias more pushback from his subordinates; make the dialogue sharper and less agreeable.)
- My Custom Additions: (Any lines or paragraphs you write directly into the text below will be preserved and woven into the rewrite.)
[/DIRECTOR'S NOTES]

{header}

{body}
"""
    WORKBENCH_FILE.write_text(template, encoding="utf-8")
    console.print(f"[bold green]Checked out Chapter {ch_num} ({header}) to {WORKBENCH_FILE.name} ({len(body.split()):,} words).[/bold green]")
    console.print("[cyan]1. Open workbench_chapter.md, fill in [DIRECTOR'S NOTES], and make any direct edits to the prose.[/cyan]")
    console.print("[cyan]2. Then run: python rework_chapter.py --apply[/cyan]")

def apply_workbench():
    wb_text = WORKBENCH_FILE.read_text(encoding="utf-8", errors="replace")
    m_idx = re.search(r'<!--\s*CHAPTER_INDEX:\s*(\d+)\s*-->', wb_text)
    m_notes = re.search(r'\[DIRECTOR\'S NOTES FOR THIS CHAPTER\](.*?)\[/DIRECTOR\'S NOTES\]', wb_text, flags=re.DOTALL)
    if not m_idx or not m_notes:
        raise ValueError("workbench_chapter.md is missing CHAPTER_INDEX or [DIRECTOR'S NOTES] tags.")

    ch_num = int(m_idx.group(1))
    notes = m_notes.group(1).strip()
    chapter_content = wb_text.split("[/DIRECTOR'S NOTES]", 1)[1].strip()

    chapters = split_chapters(MANUSCRIPT_FILE.read_text(encoding="utf-8", errors="replace"))
    orig_header, _ = chapters[ch_num - 1]

    # Extract header and body from workbench
    lines = chapter_content.splitlines()
    new_header = lines[0].strip() if lines and lines[0].strip().startswith("#") else orig_header
    draft_body = "\n".join(lines[1:]).strip() if lines and lines[0].strip().startswith("#") else chapter_content

    prev_tail = " ".join(chapters[ch_num - 2][1].split()[-350:]) if ch_num > 1 else "(Start of Book)"
    next_head = " ".join(chapters[ch_num][1].split()[:350]) if ch_num < len(chapters) else "(End of Book)"

    console.print(f"[bold blue]Re-architecting Chapter {ch_num} ({new_header}) via {MODEL_ID}...[/bold blue]")

    system_prompt = f"""You are a master historical novelist executing a full chapter 'Director's Cut' rework.

[WORLD & CHARACTER BIBLE]
{BIBLE_TEXT}

[LITERARY STYLE & ANTI-SLOP SKILL]
{SKILL_TEXT}

CRITICAL RULES:
1. Fulfill every instruction in [DIRECTOR'S NOTES] thoroughly. If the notes ask for more depth, scene context, or slower pacing, expand the chapter substantially with concrete physical, logistical, and political detail.
2. Preserve any custom lines, edits, or `[KEEP: ...]` passages the human author wrote inside the draft chapter.
3. Maintain strict continuity with [END OF PREVIOUS CHAPTER] and ensure the end of this chapter sets up [START OF NEXT CHAPTER] seamlessly.
4. Output ONLY the finished prose of the chapter body (do not include the '# Chapter' heading or commentary).
"""

    prompt = f"""[END OF PREVIOUS CHAPTER (READ-ONLY CONTINUITY)]
{prev_tail}

[DIRECTOR'S NOTES]
{notes}

[CURRENT CHAPTER DRAFT (INCLUDING HUMAN EDITS)]
{draft_body}

[START OF NEXT CHAPTER (READ-ONLY CONTINUITY)]
{next_head}"""

    # If the chapter is very long (>3500 words), split into two halves so output tokens never cap out
    paras = [p.strip() for p in re.split(r'\n\s*\n', draft_body) if p.strip()]
    mid = len(paras) // 2
    halves = ["\n\n".join(paras[:mid]), "\n\n".join(paras[mid:])] if len(draft_body.split()) > 3200 else [draft_body]

    reworked_parts = []
    for idx, part in enumerate(halves, 1):
        console.print(f"[cyan]Processing Part {idx}/{len(halves)} ({len(part.split()):,} words)...[/cyan]")
        part_prompt = f"""[END OF PREVIOUS CONTEXT]
{prev_tail if idx == 1 else " ".join(reworked_parts[-1].split()[-350:])}

[DIRECTOR'S NOTES FOR CHAPTER]
{notes}

[CHAPTER PART {idx} OF {len(halves)} TO REWORK]
{part}

[FOLLOWING CONTEXT]
{halves[1][:1200] if idx == 1 and len(halves) > 1 else next_head}"""

        resp = client.models.generate_content(
            model=MODEL_ID,
            contents=part_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.6,
                max_output_tokens=16384,
            ),
        )
        reworked_parts.append((resp.text or "").strip())

    final_body = "\n\n".join(reworked_parts)
    old_w = len(draft_body.split())
    new_w = len(final_body.split())

    backup = Path(f"manuscript_backup_ch{ch_num}_{datetime.now().strftime('%H%M%S')}.md")
    shutil.copy2(MANUSCRIPT_FILE, backup)

    chapters[ch_num - 1] = (new_header, final_body)
    full_out = "\n\n".join(f"{h}\n\n{b}" for h, b in chapters) + "\n"
    MANUSCRIPT_FILE.write_text(full_out, encoding="utf-8")

    console.print(f"[bold green]Chapter {ch_num} reworked: {old_w:,} -> {new_w:,} words! (Backup saved to {backup.name})[/bold green]")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        checkout_chapter(int(sys.argv[1]))
    elif "--apply" in sys.argv:
        apply_workbench()
    else:
        console.print("Usage:\n  python rework_chapter.py 2        # Checks out Chapter 2 into workbench_chapter.md\n  python rework_chapter.py --apply  # Rebuilds Chapter 2 from your Director's Notes & edits")
