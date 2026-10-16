import os
import re
import html
import statistics
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
    http_options=types.HttpOptions(timeout=180_000)
)

MODEL_ID = "gemini-3-flash-preview"
SKILL_TEXT = Path("skills/literary_style_skill.md").read_text(encoding="utf-8", errors="replace")

def extract_sample(word_offset: int = 15000, sample_words: int = 1100) -> str:
    """Grabs a ~1,100-word clean paragraph slice from manuscript.md."""
    raw = Path("manuscript.md").read_text(encoding="utf-8", errors="replace")
    paras = [p.strip() for p in re.split(r'\n\s*\n', raw) if p.strip()]
    
    collected = []
    running_total = 0
    sample_total = 0
    for p in paras:
        w = len(p.split())
        running_total += w
        if running_total >= word_offset:
            collected.append(p)
            sample_total += w
            if sample_total >= sample_words:
                break
    return "\n\n".join(collected)

def count_tells(text: str) -> dict:
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if len(s.split()) > 1]
    lengths = [len(s.split()) for s in sentences]
    
    ing_tails = len(re.findall(r',\s+[a-z]+ing\b', text))
    em_dashes = text.count("\u2014") + text.count("\u2013") + text.count(" -- ")
    not_but = len(re.findall(r"\bnot\b[^.!?]{1,50}\bbut\b|\bwasn't\b[^.!?]{1,40}\bit was\b", text, re.I))
    filters = len(re.findall(r'\b(saw|heard|felt|noticed|realized|seemed to|appeared to|began to|started to)\b', text, re.I))
    
    return {
        "words": len(text.split()),
        "sentence_sd": round(statistics.pstdev(lengths), 1) if len(lengths) > 1 else 0,
        "ing_tails": ing_tails,
        "em_dashes": em_dashes,
        "not_x_but_y": not_but,
        "filter_verbs": filters,
    }

def run_ab_test():
    original = extract_sample(word_offset=15000, sample_words=1100)
    print(f"Extracted {len(original.split())}-word sample from manuscript.md. Running style rewrite via {MODEL_ID}...")

    system_prompt = f"""You are a master literary line editor.
Rewrite the provided novel passage to eliminate every AI-generated prose tell while applying the craft rules below.

{SKILL_TEXT}

STRICT EXECUTION RULES:
1. Preserve 100% of plot actions, character names, setting details, and dialogue meaning.
2. Keep the passage length close to the original (do not summarize scenes into synopsis).
3. Output ONLY the rewritten prose in plain paragraphs separated by blank lines.
"""

    resp = client.models.generate_content(
        model=MODEL_ID,
        contents=f"[ORIGINAL DRAFT PASSAGE]\n\n{original}",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.45,
            max_output_tokens=8192,
        ),
    )
    rewritten = resp.text.strip()

    orig_stats = count_tells(original)
    new_stats = count_tells(rewritten)

    print("\n================ A/B DIAGNOSTIC ================")
    print(f"Metric                     | BEFORE (Raw) | AFTER (Styled)")
    print(f"---------------------------|--------------|---------------")
    print(f"Total Words                | {orig_stats['words']:<12} | {new_stats['words']:<12}")
    print(f"Sentence Length Rhythm SD  | {orig_stats['sentence_sd']:<12} | {new_stats['sentence_sd']:<12} (Higher = more varied rhythm)")
    print(f"Participial ', -ing' tails | {orig_stats['ing_tails']:<12} | {new_stats['ing_tails']:<12}")
    print(f"Em-dashes                  | {orig_stats['em_dashes']:<12} | {new_stats['em_dashes']:<12}")
    print(f"'Not X, but Y' contrasts   | {orig_stats['not_x_but_y']:<12} | {new_stats['not_x_but_y']:<12}")
    print(f"Filter/Throat-clear verbs  | {orig_stats['filter_verbs']:<12} | {new_stats['filter_verbs']:<12}")
    print("================================================\n")

    orig_paras = [f"<p>{html.escape(p)}</p>" for p in re.split(r'\n\s*\n', original) if p.strip()]
    new_paras = [f"<p>{html.escape(p)}</p>" for p in re.split(r'\n\s*\n', rewritten) if p.strip()]

    html_out = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>A/B Prose Style Comparison</title>
<style>
  body {{ font-family: Georgia, serif; background: #f4f4f0; color: #1a1a1a; margin: 0; padding: 24px; }}
  h1 {{ font-family: system-ui, sans-serif; text-align: center; font-size: 20px; margin-bottom: 8px; }}
  .stats {{ font-family: monospace; background: #222; color: #0f0; padding: 14px 20px; border-radius: 8px; max-width: 900px; margin: 0 auto 24px auto; font-size: 13px; white-space: pre; }}
  .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 28px; max-width: 1400px; margin: 0 auto; }}
  .col {{ background: #fff; padding: 28px 34px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); line-height: 1.65; font-size: 16px; }}
  .col h2 {{ font-family: system-ui, sans-serif; font-size: 15px; text-transform: uppercase; letter-spacing: 0.08em; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-top: 0; }}
  .before h2 {{ color: #b91c1c; }}
  .after h2 {{ color: #15803d; }}
  p {{ margin: 0 0 1.1em 0; text-align: justify; }}
</style>
</head>
<body>
  <h1>A/B Style Test: Raw Draft vs. Literary Anti-Slop Skill</h1>
  <div class="stats">BEFORE -> Words: {orig_stats['words']} | ', -ing' tails: {orig_stats['ing_tails']} | Em-dashes: {orig_stats['em_dashes']} | Filter verbs: {orig_stats['filter_verbs']} | Rhythm SD: {orig_stats['sentence_sd']}
AFTER  -> Words: {new_stats['words']} | ', -ing' tails: {new_stats['ing_tails']} | Em-dashes: {new_stats['em_dashes']} | Filter verbs: {new_stats['filter_verbs']} | Rhythm SD: {new_stats['sentence_sd']}</div>
  <div class="grid">
    <div class="col before">
      <h2>Before (Original Draft Excerpt)</h2>
      {chr(10).join(orig_paras)}
    </div>
    <div class="col after">
      <h2>After (Strunk + Anti-Slop Skill Applied)</h2>
      {chr(10).join(new_paras)}
    </div>
  </div>
</body>
</html>"""

    Path("ab_comparison.html").write_text(html_out, encoding="utf-8")
    print("Saved side-by-side view to ab_comparison.html!")

if __name__ == "__main__":
    run_ab_test()
