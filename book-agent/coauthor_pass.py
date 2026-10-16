import os
import re
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
BIBLE_FILE = Path("bible.md")
SKILL_FILE = Path("skills/literary_style_skill.md")

BIBLE_TEXT = BIBLE_FILE.read_text(encoding="utf-8", errors="replace") if BIBLE_FILE.exists() else ""
SKILL_TEXT = SKILL_FILE.read_text(encoding="utf-8", errors="replace") if SKILL_FILE.exists() else ""

SYSTEM_PROMPT = f"""You are a master historical novelist co-writing a novel with the lead human author.
The human author has written edits and placed inline editorial directives inside double brackets `[[...]]` within the manuscript excerpt.

[WORLD & CHARACTER BIBLE]
{BIBLE_TEXT}

[LITERARY STYLE & ANTI-SLOP RULES]
{SKILL_TEXT}

CRITICAL CO-AUTHORING RULES:
1. Execute every `[[...]]` directive in the [TARGET BLOCK TO REWORK / EXPAND] with rich, concrete historical detail, sensory grounding, and period-authentic dialogue.
2. If the human author included specific lines of dialogue, phrases, or rough draft sentences inside or adjacent to the `[[...]]` tag, preserve and weave their exact words naturally into the scene.
3. Remove the `[[...]]` bracket tags from the final output.
4. Ensure seamless narrative, tonal, and syntactic continuity with both [PRECEDING CONTEXT] and [FOLLOWING CONTEXT]. Do NOT repeat text from the preceding or following context blocks.
5. Output ONLY the finished replacement prose for the Target Block in plain Markdown paragraphs.
"""

def has_directive(text: str) -> bool:
    return bool(re.search(r'\[\[.+?\]\]', text, flags=re.DOTALL))

def run_coauthor_pass(dry_run: bool = False):
    if not MANUSCRIPT_FILE.exists():
        raise FileNotFoundError(f"{MANUSCRIPT_FILE} not found.")

    raw_text = MANUSCRIPT_FILE.read_text(encoding="utf-8", errors="replace")
    paras = [p.strip() for p in re.split(r'\n\s*\n', raw_text) if p.strip()]

    # Find indices of all paragraphs containing [[...]]
    directive_indices = [i for i, p in enumerate(paras) if has_directive(p)]
    if not directive_indices:
        console.print("[yellow]No [[...]] directives found in manuscript_chaptered.md. Add [[EXPAND: ...]] or [[REWRITE: ...]] tags first![/yellow]")
        return

    # Group nearby directive paragraphs (within 3 paragraphs of each other) into single surgical windows
    windows: list[tuple[int, int]] = []
    for idx in directive_indices:
        start = max(0, idx - 1)
        end = min(len(paras) - 1, idx + 1)
        # Never swallow a '# Chapter' header into a rewrite target unless the directive is on the header itself
        if start < idx and paras[start].startswith("#"):
            start = idx
        if end > idx and paras[end].startswith("#"):
            end = idx

        if windows and start <= windows[-1][1] + 2:
            windows[-1] = (windows[-1][0], max(windows[-1][1], end))
        else:
            windows.append((start, end))

    console.print(f"[bold cyan]Found {len(directive_indices)} inline directive(s) grouped into {len(windows)} surgical co-authoring window(s).[/bold cyan]")

    if dry_run:
        for w_idx, (s, e) in enumerate(windows, 1):
            snippet = "\n---\n".join(paras[s:e+1])
            console.print(f"\n[bold yellow]Window {w_idx} (Paragraphs {s}..{e}):[/bold yellow]\n{snippet}")
        return

    # Create timestamped backup before modifying manuscript_chaptered.md
    backup_path = Path(f"manuscript_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
    shutil.copy2(MANUSCRIPT_FILE, backup_path)
    console.print(f"[dim]Backed up current manuscript to {backup_path.name}[/dim]")

    new_paras = []
    cursor = 0

    for w_idx, (s, e) in enumerate(windows, 1):
        # Append untouched paragraphs before this window
        new_paras.extend(paras[cursor:s])

        # Gather ~800 words of preceding context and ~500 words of following context
        before_slice = "\n\n".join(paras[max(0, s - 8):s])
        target_slice = "\n\n".join(paras[s:e + 1])
        after_slice = "\n\n".join(paras[e + 1:min(len(paras), e + 6)])

        console.print(f"\n[bold blue]Executing Co-Author Window {w_idx}/{len(windows)} (Paras {s}..{e})...[/bold blue]")
        console.print(f"[dim]{target_slice}[/dim]")

        prompt = f"""[PRECEDING CONTEXT (READ-ONLY FOR CONTINUITY - DO NOT REPEAT)]
{before_slice if before_slice else "(Start of Chapter)"}

[TARGET BLOCK TO REWORK / EXPAND (EXECUTE ALL [[...]] DIRECTIVES HERE)]
{target_slice}

[FOLLOWING CONTEXT (READ-ONLY FOR CONTINUITY - DO NOT REPEAT)]
{after_slice if after_slice else "(End of Chapter)"}"""

        resp = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.6,
                max_output_tokens=8192,
            ),
        )

        replacement = (resp.text or "").strip()
        replacement_paras = [p.strip() for p in re.split(r'\n\s*\n', replacement) if p.strip()]
        
        old_w = len(target_slice.split())
        new_w = len(replacement.split())
        console.print(f"[green]Window {w_idx} complete: {old_w} words -> {new_w} words.[/green]")

        new_paras.extend(replacement_paras)
        cursor = e + 1

    # Append remaining untouched paragraphs
    new_paras.extend(paras[cursor:])

    MANUSCRIPT_FILE.write_text("\n\n".join(new_paras) + "\n", encoding="utf-8")
    console.print(f"\n[bold green]All {len(windows)} co-authoring directives applied to {MANUSCRIPT_FILE.name}![/bold green]")

if __name__ == "__main__":
    import sys
    run_coauthor_pass(dry_run="--dry-run" in sys.argv)
