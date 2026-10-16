import os
import re
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
MANUSCRIPT_FILE = Path("manuscript_chaptered.md")
OUTPUT_JSON = Path("character_bible.json")

class CharacterProfile(BaseModel):
    name: str
    role_or_significance: str
    social_and_cultural_background: str
    sierpinski_vertex_affinity: str  # V1 (Ledger), V2 (Crucible/Earth), or V3 (Covenant/Shadow)
    syntax_and_rhythm: str
    metaphor_domain: str
    speech_quirks_or_dialect: str
    emotional_deflection_or_tell: str

class ExtractedCharacters(BaseModel):
    characters: list[CharacterProfile]

def split_chapters(raw_text: str) -> list[str]:
    normalized = re.sub(r'(?m)^(#{1,3}\s+.+)$', r'\n\n\1\n\n', raw_text)
    blocks = [b.strip() for b in re.split(r'\n\s*\n', normalized) if b.strip()]
    chapters, cur_lines = [], []
    for b in blocks:
        if re.match(r'^#{1,3}\s+', b) and cur_lines:
            chapters.append("\n\n".join(cur_lines))
            cur_lines = [b]
        else:
            cur_lines.append(b)
    if cur_lines:
        chapters.append("\n\n".join(cur_lines))
    return chapters

def mine_all_chapters():
    if not MANUSCRIPT_FILE.exists():
        raise FileNotFoundError(f"{MANUSCRIPT_FILE} not found.")

    raw_text = MANUSCRIPT_FILE.read_text(encoding="utf-8", errors="replace")
    chapter_blocks = split_chapters(raw_text)

    console.print(f"[bold cyan]Found {len(chapter_blocks)} chapters in manuscript. Mining every chapter for characters...[/bold cyan]")

    all_characters = {}

    # Process chapters in sliding groups of 5 to ensure exhaustive extraction without token limits
    group_size = 5
    for i in range(0, len(chapter_blocks), group_size):
        chunk_chapters = chapter_blocks[i:i + group_size]
        chunk_text = "\n\n---\n\n".join(chunk_chapters)
        ch_range = f"Chapters {i+1} to {min(i+group_size, len(chapter_blocks))}"

        console.print(f"[blue]  -> Extracting characters from {ch_range}...[/blue]")

        prompt = f"""You are the Master Character & Voice Architect for 'The Grand Confederation of Pacifica'.
Extract EVERY character appearing in these specific manuscript chapters—including major principals, recurring figures, and all minor/fleeting individuals (guards, captains, clerks, local merchants, foreign attachés, family members).

[MANUSCRIPT CHUNK ({ch_range})]
{chunk_text}

[TASK]
Return a comprehensive JSON list of all characters found in this chunk, complete with psychological and linguistic profiles.
Ensure strict Sierpinski Triadic balance:
- **Vertex 1 Characters:** Think in terms of logistics, ledgers, statecraft, command.
- **Vertex 2 Characters:** Think in terms of physical survival, vernacular, weather, tactile friction.
- **Vertex 3 Characters:** Driven by deep private devotion, brotherhood, filial piety, or obsessive shadow registers (jealousy, fanaticism).
"""

        resp = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ExtractedCharacters,
                temperature=0.3,
            ),
        )

        data = ExtractedCharacters.model_validate_json(resp.text)
        for c in data.characters:
            # Merge/deduplicate by name
            key = c.name.strip().title()
            if key not in all_characters:
                all_characters[key] = c

    final_list = list(all_characters.values())
    output_data = ExtractedCharacters(characters=final_list)
    OUTPUT_JSON.write_text(json.dumps(output_data.model_dump(), indent=2), encoding="utf-8")

    console.print(f"\n[bold green]Successfully extracted and profiled {len(final_list)} unique characters across all chapters! Saved to {OUTPUT_JSON.name}[/bold green]")
    for c in final_list[:15]: # Show first 15 in terminal
        console.print(Panel(
            f"[bold yellow]Role:[/bold yellow] {c.role_or_significance} | [cyan]Vertex:[/cyan] {c.sierpinski_vertex_affinity}\n"
            f"[white]Syntax & Rhythm:[/white] {c.syntax_and_rhythm}\n"
            f"[green]Speech Quirks:[/green] {c.speech_quirks_or_dialect}",
            title=c.name
        ))

if __name__ == "__main__":
    mine_all_chapters()
