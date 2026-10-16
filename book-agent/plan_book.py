import os
import json
import time
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from google import genai
from google.genai import types
from google.genai import errors
from pydantic import BaseModel

load_dotenv()
console = Console()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
MODEL_ID = "gemini-3-flash-preview"

class Beat(BaseModel):
    beat_id: int
    chapter: int
    pov: str
    location: str
    action: str
    subtext: str
    target_words: int
    status: str = "pending"

class BookBlueprint(BaseModel):
    story_bible_markdown: str
    beats: list[Beat]

def generate_blueprint(total_beats: int = 180, words_per_beat: int = 600):
    concept = Path("concept.txt").read_text(encoding="utf-8")
    console.print(f"[bold cyan]Generating Story Bible and {total_beats}-beat blueprint (~{total_beats * words_per_beat:,} words target)...[/bold cyan]")
    console.print("[dim]This generates ~20,000 tokens of structured JSON and takes about 60-90 seconds...[/dim]")
    
    prompt = f"""
    Based on the following book concept, create:
    1. A comprehensive Story Bible in Markdown (character voice profiles, world rules, sensory palette, themes, and stylistic negative constraints).
    2. A chronological sequence of exactly {total_beats} granular scene beats (`beat_id` 1 to {total_beats}) organized across logical chapters (roughly 20 to 30 chapters).
       - Each beat must represent a distinct scene, micro-escalation, or dramatic shift (never summarize weeks/months; keep scenes immediate and tactile).
       - Set `target_words` to {words_per_beat} per beat and `status` to "pending".

    [BOOK CONCEPT]
    {concept}
    """
    
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=BookBlueprint,
        temperature=0.7,
        max_output_tokens=65536,
    )

    for attempt in range(1, 6):
        try:
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=prompt,
                config=config,
            )
            break
        except (errors.ServerError, errors.ClientError) as e:
            if "503" in str(e) or "429" in str(e) or "UNAVAILABLE" in str(e):
                wait_sec = 10 * attempt
                console.print(f"[yellow]Server busy (503/429). Waiting {wait_sec}s before retry {attempt}/5...[/yellow]")
                time.sleep(wait_sec)
            else:
                raise
    
    blueprint = BookBlueprint.model_validate_json(response.text)
    Path("bible.md").write_text(blueprint.story_bible_markdown, encoding="utf-8")
    
    beats_data = [b.model_dump() for b in blueprint.beats]
    for idx, b in enumerate(beats_data, start=1):
        b["beat_id"] = idx
        b["status"] = "pending"
        
    Path("beats.json").write_text(json.dumps(beats_data, indent=2), encoding="utf-8")
    Path("manuscript.md").write_text("", encoding="utf-8")
    console.print(f"[bold green]SUCCESS! Saved bible.md and {len(beats_data)} beats to beats.json![/bold green]")

if __name__ == "__main__":
    generate_blueprint(total_beats=180, words_per_beat=600)
