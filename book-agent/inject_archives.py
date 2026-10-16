import os
import re
import sys
import json
import shutil
from datetime import datetime
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
BIBLE_TEXT = Path("bible.md").read_text(encoding="utf-8", errors="replace") if Path("bible.md").exists() else ""
ARCHIVAL_SKILL = Path("skills/archival_voices.md").read_text(encoding="utf-8", errors="replace")
STYLE_SKILL = Path("skills/literary_style_skill.md").read_text(encoding="utf-8", errors="replace")

VOICE_KEYS = [
    "FUSETSUGAKI",
    "HYORYUKI",
    "HAWAIIAN_MELE",
    "NUPEPA_LETTER",
    "CLIOMETRIC_DATASET",
    "ASSAY_CIPHER_LEDGER",
    "CORRIDO_DE_CONTRABANDO",
    "RIVER_PILOT_SOUNDING_BOOK",
    "DEAD_LETTER_CARTRIDGE_CONFESSION",
    "MARE_ISLAND_GUTTA_CABLE_TAPE",
    "CREOLE_YUKON_FUR_TALLY_BARK",
    "TAGALOG_ANTING_ANTING_LIBRITO",
    "YOKOHAMA_KAWARABAN_WOODBLOCK",
    "DIOMED_CAISSON_DECOMPRESSION_LOG",
    "QIAOXIANG_BONE_REPATRIATION_MANIFEST",
    "SYDNEY_BUSH_BALLAD_BROADSHEET",
    "SYNCRETIC_EXAMINATION_EIGHT_LEGGED_ESSAY",
    "CULEBRA_DUPPY_CALYPSO_CHALK",
    "AERO_HYDROGEN_BAROGRAPH_LOG",
    "CHEFU_HEMI_PHRENOLOGICAL_CASEBOOK",
    "IMPERIAL_SUCCESSION_KOSEKI_DOSSIER",
    "GHAZIPUR_ABKARI_OPIUM_TARIFF_CHALLAN",
    "THALASSIA_KAHUNA_ARCHITECTURAL_SPECIFICATION",
    "GENEVA_LAZARETTO_FUMIGATION_DOSSIER",
    "KHYBER_STEAM_TANK_BOILER_LANDAY",
    "NEWCASTLE_JACQUARD_MILL_TAPE",
    "MAITREYA_MARX_SUTRA_TALISMAN",
    "NIPKOW_PHOSPHOR_KAUAI_ELEGY",
    "THALASSIA_EVACUATION_CRATE_INVENTORY",
]

class EpigraphPlan(BaseModel):
    chosen_voice_key: str
    historical_rationale: str
    formatted_markdown_blockquote: str

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

def ensure_blockquote(text: str) -> str:
    lines = [l.strip() for l in text.strip().splitlines() if l.strip()]
    out = []
    for l in lines:
        if not l.startswith(">"):
            out.append(f"> {l}")
        else:
            out.append(l)
    return "\n".join(out)

def generate_epigraph_for_chapter(ch_num: int, header: str, body: str, prev_voices: list[str], forced_voice: str | None = None, custom_hint: str = "") -> EpigraphPlan:
    words = body.split()
    chapter_excerpt = " ".join(words[:900]) + "\n...\n" + " ".join(words[-600:])
    avoid_list = ", ".join(prev_voices[-2:]) if prev_voices else "None"

    voice_instruction = (
        f"You MUST use the archival voice `{forced_voice}`."
        if forced_voice
        else f"Select the most resonant voice from {VOICE_KEYS}. Do NOT repeat the immediately preceding voices ({avoid_list}). Balance Primary Sources (Edo Fusetsugaki, Castaway Hyoryuki, Hawaiian Mele with Kaona, Nupepa letters, Ciphers) with Secondary Sources (21st-century Cliometric Datasets, Revisionist Biographies)."
    )

    prompt = f"""You are the Archival Worldbuilding Editor for the historical novel 'The Grand Confederation of Pacifica'.

[WORLD & CHARACTER BIBLE]
{BIBLE_TEXT}

[ARCHIVAL VOICE REPOSITORY]
{ARCHIVAL_SKILL}

[STYLE RULES]
{STYLE_SKILL}

[TARGET CHAPTER {ch_num}: {header}]
{chapter_excerpt}

[EDITORIAL INSTRUCTION]
{voice_instruction}
{f"Specific Author Direction: {custom_hint}" if custom_hint else ""}

Write a rich, period-authentic archival epigraph or document excerpt to stand at the opening of {header}.
RULES:
1. It must illuminate the broader geopolitical, cultural, maritime, economic, or human/tragic context of this chapter (e.g., Kingdom of Hawaii agreements, Edo Bakufu intelligence, castaway sailors, local perception of the Protector, or modern econometric/historical analysis looking back at the human cost).
2. Make the voice 100% distinct from the novel's narrative prose. Include authentic period terminology, dates, archive catalogue numbers, or scholar notes where appropriate.
3. Format `formatted_markdown_blockquote` with `> ` at the start of every line, ending with `> — *[Full Source Attribution, Date, and Archive/Publication]*`.
"""

    resp = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=EpigraphPlan,
            temperature=0.65,
        ),
    )
    plan = EpigraphPlan.model_validate_json(resp.text)
    plan.formatted_markdown_blockquote = ensure_blockquote(plan.formatted_markdown_blockquote)
    return plan

def inject_chapter_epigraphs(target_spec: str, forced_voice: str | None = None, custom_hint: str = "", dry_run: bool = False):
    raw_text = MANUSCRIPT_FILE.read_text(encoding="utf-8", errors="replace")
    chapters = split_chapters(raw_text)

    if target_spec.lower() == "all":
        targets = list(range(1, len(chapters) + 1))
    elif "-" in target_spec:
        s, e = target_spec.split("-", 1)
        targets = list(range(int(s), int(e) + 1))
    else:
        targets = [int(target_spec)]

    prev_voices = []
    modified = False

    if not dry_run:
        backup = Path(f"manuscript_backup_archives_{datetime.now().strftime('%H%M%S')}.md")
        shutil.copy2(MANUSCRIPT_FILE, backup)
        console.print(f"[dim]Backed up manuscript to {backup.name}[/dim]")

    for ch_num in targets:
        if ch_num < 1 or ch_num > len(chapters):
            continue
        header, body = chapters[ch_num - 1]
        paras = [p.strip() for p in re.split(r'\n\s*\n', body) if p.strip()]

        console.print(f"\n[bold blue]Composing Archival Epigraph for Chapter {ch_num} ({header})...[/bold blue]")
        plan = generate_epigraph_for_chapter(ch_num, header, body, prev_voices, forced_voice, custom_hint)
        prev_voices.append(plan.chosen_voice_key)

        console.print(Panel(
            f"[bold yellow]Voice:[/bold yellow] {plan.chosen_voice_key}\n"
            f"[bold cyan]Rationale:[/bold cyan] {plan.historical_rationale}\n\n"
            f"[green]{plan.formatted_markdown_blockquote}[/green]",
            title=f"Chapter {ch_num}: {header}"
        ))

        if not dry_run:
            # Replace existing top epigraph if present, otherwise prepend
            if paras and paras[0].lstrip().startswith(">"):
                paras[0] = plan.formatted_markdown_blockquote
            else:
                paras.insert(0, plan.formatted_markdown_blockquote)
            chapters[ch_num - 1] = (header, "\n\n".join(paras))
            modified = True

    if modified and not dry_run:
        MANUSCRIPT_FILE.write_text("\n\n".join(f"{h}\n\n{b}" for h, b in chapters) + "\n", encoding="utf-8")
        console.print(f"\n[bold green]Successfully injected archival epigraph(s) into {MANUSCRIPT_FILE.name}![/bold green]")

def apply_inline_archive_tags(dry_run: bool = False):
    """Scans manuscript_chaptered.md for [[ARCHIVE: ...]] tags and replaces them with rich primary/secondary documents."""
    raw_text = MANUSCRIPT_FILE.read_text(encoding="utf-8", errors="replace")
    paras = [p.strip() for p in re.split(r'\n\s*\n', raw_text) if p.strip()]

    tag_indices = [i for i, p in enumerate(paras) if re.search(r'\[\[ARCHIVE:(.+?)\]\]', p, flags=re.DOTALL)]
    if not tag_indices:
        console.print("[yellow]No [[ARCHIVE: ...]] tags found in manuscript_chaptered.md.[/yellow]")
        return

    if not dry_run:
        backup = Path(f"manuscript_backup_interludes_{datetime.now().strftime('%H%M%S')}.md")
        shutil.copy2(MANUSCRIPT_FILE, backup)

    for idx in tag_indices:
        match = re.search(r'\[\[ARCHIVE:(.+?)\]\]', paras[idx], flags=re.DOTALL)
        directive = match.group(1).strip()
        before_ctx = "\n\n".join(paras[max(0, idx - 4):idx])
        after_ctx = "\n\n".join(paras[idx + 1:min(len(paras), idx + 5)])

        console.print(f"\n[bold blue]Generating Archival Interlude at P{idx}: {directive}[/bold blue]")
        prompt = f"""You are the Archival Worldbuilding Editor for 'The Grand Confederation of Pacifica'.

[WORLD & CHARACTER BIBLE]
{BIBLE_TEXT}

[ARCHIVAL VOICE REPOSITORY]
{ARCHIVAL_SKILL}

[SURROUNDING NARRATIVE CONTEXT (BEFORE)]
{before_ctx}

[AUTHOR'S ARCHIVAL DIRECTIVE]
{directive}

[SURROUNDING NARRATIVE CONTEXT (AFTER)]
{after_ctx}

Compose the requested archival document or interlude (120 to 350 words unless specified otherwise).
Format every line of `formatted_markdown_blockquote` as a Markdown blockquote (`> `), ending with `> — *[Source Attribution, Date, Archive]*`.
"""
        resp = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=EpigraphPlan,
                temperature=0.65,
            ),
        )
        plan = EpigraphPlan.model_validate_json(resp.text)
        block = ensure_blockquote(plan.formatted_markdown_blockquote)

        console.print(Panel(f"[bold yellow]{plan.chosen_voice_key}[/bold yellow]\n\n[green]{block}[/green]", title=f"Interlude @ P{idx}"))

        if not dry_run:
            # Replace the [[ARCHIVE: ...]] tag with the formatted blockquote
            paras[idx] = re.sub(r'\[\[ARCHIVE:.+?\]\]', block, paras[idx], flags=re.DOTALL)

    if not dry_run:
        MANUSCRIPT_FILE.write_text("\n\n".join(paras) + "\n", encoding="utf-8")
        console.print(f"\n[bold green]Applied {len(tag_indices)} archival interlude(s) to {MANUSCRIPT_FILE.name}![/bold green]")

if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--dry-run"]

    if not args:
        console.print("""[bold cyan]Archival & Epigraph Injector Usage:[/bold cyan]
  1. Generate epigraphs for specific chapters (auto-selects best voice):
     python inject_archives.py --epigraphs 1-3 --dry-run
     python inject_archives.py --epigraphs 1-3
     python inject_archives.py --epigraphs all

  2. Generate an epigraph for a single chapter with a specific voice & hint:
     python inject_archives.py --chapter 2 --voice NUPEPA_LETTER --hint "How Honolulu dockworkers viewed the Protector's gunboats"

  3. Execute inline [[ARCHIVE: ...]] interlude tags placed anywhere in manuscript_chaptered.md:
     python inject_archives.py --apply-tags""")
    elif args[0] == "--epigraphs" and len(args) >= 2:
        inject_chapter_epigraphs(args[1], dry_run=dry)
    elif args[0] == "--chapter" and len(args) >= 2:
        ch = args[1]
        v = args[args.index("--voice") + 1] if "--voice" in args else None
        h = args[args.index("--hint") + 1] if "--hint" in args else ""
        inject_chapter_epigraphs(ch, forced_voice=v, custom_hint=h, dry_run=dry)
    elif args[0] == "--apply-tags":
        apply_inline_archive_tags(dry_run=dry)
