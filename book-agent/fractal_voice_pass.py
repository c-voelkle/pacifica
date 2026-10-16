import os
import re
import sys
import shutil
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
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
VOICES_TEXT = Path("skills/voices.md").read_text(encoding="utf-8", errors="replace")
FRACTAL_TEXT = Path("skills/sierpinski_structure.md").read_text(encoding="utf-8", errors="replace")
STYLE_TEXT = Path("skills/literary_style_skill.md").read_text(encoding="utf-8", errors="replace")

VERTEX_NAMES = {
    1: "V1: The Ledger (Technocracy & Strategy)",
    2: "V2: The Crucible (Tactile World & Sea)",
    3: "V3: The Covenant (Love, Brotherhood & Shadow)",
}

VOICE_MAP = {
    1: "VOICE A: THE GEOMETER (Order / Ledger / Statecraft)",
    2: "VOICE B: THE ALKALI & SALT REGISTER (Tactile World & Friction)",
    3: "VOICE C: THE COVENANT & THE SHADOW (Love, Loyalty & Obsession)",
}

def split_chapters(raw_text: str) -> list[tuple[str, str]]:
    normalized = re.sub(r'(?m)^(#{1,3}\s+.+)$', r'\n\n\1\n\n', raw_text)
    blocks = [b.strip() for b in re.split(r'\n\s*\n', normalized) if b.strip()]
    chapters, cur_header, cur_paras = [], "# Chapter 1", []
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

def compute_sierpinski_coordinate(ch_idx_zero: int, total_chapters: int) -> tuple[int, int, int]:
    progress = ch_idx_zero / max(1, total_chapters)
    macro = min(3, int(progress * 3) + 1)
    meso_progress = (progress * 3) % 1.0
    meso = min(3, int(meso_progress * 3) + 1)
    micro = (ch_idx_zero % 3) + 1
    return (macro, meso, micro)

def show_sierpinski_map():
    chapters = split_chapters(MANUSCRIPT_FILE.read_text(encoding="utf-8", errors="replace"))
    table = Table(title="Sierpinski Gasket Architecture & Voice Matrix")
    table.add_column("Ch #", style="cyan", justify="right")
    table.add_column("Title", style="white")
    table.add_column("Coord", style="bold yellow", justify="center")
    table.add_column("Macro (Act)", style="dim")
    table.add_column("Meso (Movement)", style="dim")
    table.add_column("Micro (Chapter Voice)", style="green")

    for i, (header, body) in enumerate(chapters):
        m1, m2, m3 = compute_sierpinski_coordinate(i, len(chapters))
        clean_title = re.sub(r'^#{1,3}\s+', '', header)
        table.add_row(
            str(i + 1),
            clean_title[:38],
            f"[{m1}.{m2}.{m3}]",
            VERTEX_NAMES[m1].split("(")[0].strip(),
            VERTEX_NAMES[m2].split("(")[0].strip(),
            VOICE_MAP[m3].split("(")[0].strip()
        )
    console.print(table)

def modulate_chapter(ch_num: int, custom_voice_override: int | None = None):
    chapters = split_chapters(MANUSCRIPT_FILE.read_text(encoding="utf-8", errors="replace"))
    if ch_num < 1 or ch_num > len(chapters):
        raise ValueError(f"Chapter {ch_num} out of range (1..{len(chapters)}).")

    m1, m2, m3 = compute_sierpinski_coordinate(ch_num - 1, len(chapters))
    if custom_voice_override in (1, 2, 3):
        m3 = custom_voice_override

    header, body = chapters[ch_num - 1]
    coord_str = f"[{m1}.{m2}.{m3}]"
    dominant_voice = VOICE_MAP[m3]

    console.print(f"[bold cyan]Modulating {header} -> Sierpinski Coord {coord_str} | {dominant_voice}[/bold cyan]")

    system_prompt = f"""You are a master literary stylist executing a Sierpinski Fractal & Voice Modulation pass on a chapter.

[SIERPINSKI FRACTAL ARCHITECTURE FOR THIS CHAPTER]
- Chapter Coordinate: {coord_str}
- Macro Act Gravity (Digit 1): {VERTEX_NAMES[m1]}
- Meso Movement Tension (Digit 2): {VERTEX_NAMES[m2]}
- Micro Chapter Trajectory & Dominant Voice (Digit 3): {VERTEX_NAMES[m3]} -> Use **{dominant_voice}**

{FRACTAL_TEXT}

{VOICES_TEXT}

{STYLE_TEXT}

CRITICAL EXECUTION RULES:
1. Modulate the prose syntax, focalization lens, and metaphor domain to embody **{dominant_voice}** while honoring the `{coord_str}` fractal intersection.
2. Ensure every scene inside this chapter exhibits self-similar triadic progression (Setup/Ledger -> Friction -> Covenant/Synthesis around an unspoken Central Void).
3. Preserve 100% of plot continuity, character names, and key events (and any `> ` archival epigraphs), keeping word count between 95% and 115% of the input text.
4. Output ONLY the finished prose of the chapter body (no `# Chapter` header or meta-commentary).
"""

    paras = [p.strip() for p in re.split(r'\n\s*\n', body) if p.strip()]
    # Preserve top archival epigraph untouched if present
    epigraph_block = ""
    if paras and paras[0].lstrip().startswith(">"):
        epigraph_block = paras.pop(0)

    chunks, cur_chunk, cur_words = [], [], 0
    for p in paras:
        w = len(p.split())
        if cur_words + w > 2200 and cur_chunk:
            chunks.append("\n\n".join(cur_chunk))
            cur_chunk, cur_words = [p], w
        else:
            cur_chunk.append(p)
            cur_words += w
    if cur_chunk:
        chunks.append("\n\n".join(cur_chunk))

    reworked_chunks = []
    prev_tail = " ".join(chapters[ch_num - 2][1].split()[-250:]) if ch_num > 1 else "(Start of Book)"

    for idx, ch_part in enumerate(chunks, 1):
        console.print(f"[blue]  -> Modulating section {idx}/{len(chunks)} ({len(ch_part.split())} words) in {dominant_voice.split(':')[1].split('(')[0].strip()}...[/blue]")
        prompt = f"""[PRECEDING FLOW CONTEXT (DO NOT REPEAT)]
{prev_tail}

[CHAPTER SECTION {idx}/{len(chunks)} TO MODULATE INTO {coord_str} / {dominant_voice}]
{ch_part}"""

        resp = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.55,
                max_output_tokens=16384,
            ),
        )
        out_text = (resp.text or "").strip()
        reworked_chunks.append(out_text)
        prev_tail = " ".join(out_text.split()[-250:])

    final_body = (f"{epigraph_block}\n\n" if epigraph_block else "") + "\n\n".join(reworked_chunks)
    backup = Path(f"manuscript_backup_fractal_ch{ch_num}_{datetime.now().strftime('%H%M%S')}.md")
    shutil.copy2(MANUSCRIPT_FILE, backup)

    chapters[ch_num - 1] = (header, final_body)
    MANUSCRIPT_FILE.write_text("\n\n".join(f"{h}\n\n{b}" for h, b in chapters) + "\n", encoding="utf-8")
    console.print(f"[bold green]Chapter {ch_num} modulated to {coord_str} ({len(body.split()):,} -> {len(final_body.split()):,} words)! Backup: {backup.name}[/bold green]")

if __name__ == "__main__":
    if len(sys.argv) == 1 or "--map" in sys.argv:
        show_sierpinski_map()
    elif len(sys.argv) >= 2 and sys.argv[1].isdigit():
        ch = int(sys.argv[1])
        override = int(sys.argv[2]) if len(sys.argv) >= 3 and sys.argv[2] in ("1", "2", "3") else None
        modulate_chapter(ch, override)
