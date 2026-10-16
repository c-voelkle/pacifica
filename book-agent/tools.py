import re
import json
import subprocess
from pathlib import Path

MANUSCRIPT_PATH = Path("manuscript.md")
BEATS_PATH = Path("beats.json")

def get_full_manuscript_parts(seam_word_count: int = 500) -> tuple[str, str]:
    """Splits the full manuscript on disk into the true locked body and the 500-word seam."""
    if not MANUSCRIPT_PATH.exists():
        return "", ""
    text = MANUSCRIPT_PATH.read_text(encoding="utf-8").strip()
    if not text:
        return "", ""
    
    matches = list(re.finditer(r'\S+', text))
    if len(matches) <= seam_word_count:
        return "", text
    
    split_char_idx = matches[-seam_word_count].start()
    para_break = text.rfind("\n\n", 0, split_char_idx)
    if para_break != -1 and (split_char_idx - para_break) < 600:
        split_char_idx = para_break
        
    locked_body = text[:split_char_idx].rstrip()
    malleable_seam = text[split_char_idx:].lstrip()
    return locked_body, malleable_seam

def get_manuscript_and_seam(seam_word_count: int = 500, max_context_words: int = 35000) -> tuple[str, str]:
    """Returns a rolling window of the last max_context_words of locked prose + the 500-word seam for the prompt."""
    locked_body, malleable_seam = get_full_manuscript_parts(seam_word_count)
    if not locked_body:
        return "", malleable_seam
        
    matches = list(re.finditer(r'\S+', locked_body))
    if len(matches) > max_context_words:
        trim_idx = matches[-max_context_words].start()
        para_break = locked_body.find("\n\n", trim_idx)
        if para_break != -1 and (para_break - trim_idx) < 600:
            trim_idx = para_break
        locked_body = "... [EARLIER CHAPTERS OMITTED FROM RAW BUFFER - SEE COMPLETED BEATS LOG] ...\n\n" + locked_body[trim_idx:].lstrip()
        
    return locked_body, malleable_seam

def commit_sliding_seam_pass(
    rewritten_seam_and_new_prose: str,
    completed_beat_ids: list[int],
    paused_mid_scene_note: str
) -> str:
    # Always splice against the FULL manuscript on disk so zero words are ever lost!
    full_locked_body, _ = get_full_manuscript_parts(500)
    
    if full_locked_body:
        updated_manuscript = f"{full_locked_body}\n\n{rewritten_seam_and_new_prose.strip()}\n"
    else:
        updated_manuscript = f"{rewritten_seam_and_new_prose.strip()}\n"
        
    MANUSCRIPT_PATH.write_text(updated_manuscript, encoding="utf-8")
    
    beats = json.loads(BEATS_PATH.read_text(encoding="utf-8"))
    for b in beats:
        if b["beat_id"] in completed_beat_ids:
            b["status"] = "completed"
    BEATS_PATH.write_text(json.dumps(beats, indent=2), encoding="utf-8")
    
    subprocess.run(["git", "add", "manuscript.md", "beats.json"], check=False)
    subprocess.run(
        ["git", "commit", "-m", f"Beats {completed_beat_ids} | Seam: {paused_mid_scene_note}"],
        check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    
    total_words = len(updated_manuscript.split())
    return f"SUCCESS: Seam spliced. Manuscript is now {total_words} words."
