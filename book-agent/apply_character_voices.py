import os
import re
import sys
import json
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
BIBLE_JSON = Path("character_bible.json")
STYLE_FILE = Path("skills/literary_style_skill.md")

STYLE_TEXT = STYLE_FILE.read_text(encoding="utf-8", errors="replace") if STYLE_FILE.exists() else ""

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

def apply_polyphony_to_chapter(ch_num: int):
    if not BIBLE_JSON.exists():
        raise FileNotFoundError("character_bible.json not found. Run mine_characters.py first!")

    char_profiles = BIBLE_JSON.read_text(encoding="utf-8", errors="replace")
    chapters = split_chapters(MANUSCRIPT_FILE.read_text(encoding="utf-8", errors="replace"))
    
    if ch_num < 1 or ch_num > len(chapters):
        raise ValueError(f"Chapter {ch_num} out of range (1..{len(chapters)}).")

    header, body = chapters[ch_num - 1]
    console.print(f"[bold cyan]Applying Polyphonic Character Voices to {header}...[/bold cyan]")

    system_prompt = f"""You are a master literary editor enforcing strict polyphonic character voice architecture.

[MASTER CHARACTER BIBLE & VOICE PROFILES]
{char_profiles}

[LITERARY STYLE & ANTI-SLOP RULES]
{STYLE_TEXT}

CRITICAL EXECUTION RULES:
1. **Strict Polyphony & Zero Ventriloquism:** Examine every line of dialogue and interior focalization in this chapter. Every character (whether Elias, Kaiulani, Caleb, or any minor/fleeting figure) must speak and perceive through their exact profile in the Character Bible (syntax, rhythm, metaphor domain, speech quirks).
2. **Micro-Level Dialogue Audit:** If a minor character or principal speaks in standard authorial prose, rewrite their lines to reflect their specific background and dialect.
3. **Preserve Plot & Continuity:** Keep 100% of plot events, character names, and any `> ` archival epigraphs. Keep word count between 95% and 110% of the input text.
4. Output ONLY the finished prose of the chapter body (no `# Chapter` header or meta-commentary).
"""

    paras = [p.strip() for p in re.split(r'\n\s*\n', body) if p.strip()]
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
        console.print(f"[blue]  -> Polyphonic audit on section {idx}/{len(chunks)} ({len(ch_part.split())} words)...[/blue]")
        prompt = f"""[PRECEDING FLOW CONTEXT (DO NOT REPEAT)]
{prev_tail}

[CHAPTER SECTION {idx}/{len(chunks)} TO AUDIT & REWRITE FOR UNIQUE CHARACTER VOICES]
{ch_part}"""

        resp = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.5,
                max_output_tokens=16384,
            ),
        )
        out_text = (resp.text or "").strip()
        reworked_chunks.append(out_text)
        prev_tail = " ".join(out_text.split()[-250:])

    final_body = (f"{epigraph_block}\n\n" if epigraph_block else "") + "\n\n".join(reworked_chunks)
    backup = Path(f"manuscript_backup_polyphony_ch{ch_num}_{datetime.now().strftime('%H%M%S')}.md")
    shutil.copy2(MANUSCRIPT_FILE, backup)

    chapters[ch_num - 1] = (header, final_body)
    MANUSCRIPT_FILE.write_text("\n\n".join(f"{h}\n\n{b}" for h, b in chapters) + "\n", encoding="utf-8")
    console.print(f"[bold green]Polyphonic character voice pass complete for {header}! Backup saved to {backup.name}[/bold green]")

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        apply_polyphony_to_chapter(int(sys.argv[1]))
    else:
        console.print("Usage: python apply_character_voices.py 2  # Runs polyphonic character pass on Chapter 2")
