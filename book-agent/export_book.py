import re
import uuid
import html
import zipfile
from datetime import datetime, timezone
from pathlib import Path

if Path("manuscript_chaptered.md").exists():
    MANUSCRIPT_PATH = Path("manuscript_chaptered.md")
elif Path("manuscript_polished.md").exists():
    MANUSCRIPT_PATH = Path("manuscript_polished.md")
else:
    MANUSCRIPT_PATH = Path("manuscript.md")

BIBLE_PATH = Path("bible.md")
EPUB_PATH = Path("book.epub")
PRINT_HTML_PATH = Path("book_print.html")

def detect_title() -> str:
    if BIBLE_PATH.exists():
        first_line = BIBLE_PATH.read_text(encoding="utf-8", errors="replace").splitlines()[0].strip()
        cleaned = re.sub(r'^[#*:\s]+', '', first_line).strip()
        if cleaned and len(cleaned) < 80:
            return cleaned
    return "Pacifica"

BOOK_TITLE = detect_title()
BOOK_AUTHOR = "Curtis Völkle"
WORDS_PER_AUTO_CHAPTER = 6500

def format_inline_markdown(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escaped)
    escaped = re.sub(r'\*(.+?)\*', r'<em>\1</em>', escaped)
    return escaped

def parse_into_chapters(raw_text: str) -> list[tuple[str, list[str]]]:
    # Ensure any markdown header '# ...' is cleanly separated by blank lines even if edited without extra newlines
    normalized = re.sub(r'(?m)^(#{1,3}\s+.+)$', r'\n\n\1\n\n', raw_text)
    blocks = [b.strip() for b in re.split(r'\n\s*\n', normalized) if b.strip()]
    has_explicit_headers = any(re.match(r'^#{1,3}\s+', b) for b in blocks)

    chapters: list[tuple[str, list[str]]] = []
    current_title = "Chapter 1"
    current_paras: list[str] = []
    current_words = 0
    chapter_num = 1

    for block in blocks:
        header_match = re.match(r'^#{1,3}\s+(.+)$', block)
        if header_match:
            if current_paras:
                chapters.append((current_title, current_paras))
                current_paras = []
                current_words = 0
            current_title = header_match.group(1).strip()
            chapter_num += 1
            continue

        if block in ("***", "---", "* * *"):
            current_paras.append("__SCENE_BREAK__")
            continue

        block_words = len(block.split())
        if not has_explicit_headers and current_words >= WORDS_PER_AUTO_CHAPTER:
            chapters.append((f"Chapter {chapter_num}", current_paras))
            chapter_num += 1
            current_title = f"Chapter {chapter_num}"
            current_paras = []
            current_words = 0

        current_paras.append(block)
        current_words += block_words

    if current_paras:
        chapters.append((current_title, current_paras))

    return chapters

def build_epub(chapters: list[tuple[str, list[str]]]):
    book_uuid = str(uuid.uuid4())
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    css = """
    body { font-family: Georgia, "Times New Roman", serif; line-height: 1.6; margin: 5%; color: #111; }
    h1 { text-align: center; font-weight: normal; letter-spacing: 0.08em; margin-top: 2.5em; margin-bottom: 2em; page-break-before: always; }
    p { margin: 0; text-indent: 1.5em; text-align: justify; }
    p.first { text-indent: 0; }
    blockquote.archival { margin: 1.5em 6% 1.8em 6%; padding: 0.6em 1em; border-left: 2px solid #888; font-size: 0.92em; line-height: 1.5; }
    blockquote.archival p { text-indent: 0; margin-bottom: 0.5em; text-align: left; }
    blockquote.archival p.attribution { text-align: right; font-style: italic; margin-top: 0.6em; color: #333; }
    hr.scenebreak { border: none; text-align: center; margin: 1.5em 0; }
    blockquote.archival { margin: 1.5em 6% 1.8em 6%; padding: 0.6em 1em; border-left: 2px solid #888; font-size: 0.92em; line-height: 1.5; }
    blockquote.archival p { text-indent: 0; margin-bottom: 0.5em; text-align: left; }
    blockquote.archival p.attribution { text-align: right; font-style: italic; margin-top: 0.6em; color: #333; }
    hr.scenebreak::after { content: "* * *"; letter-spacing: 0.3em; }
    """

    with zipfile.ZipFile(EPUB_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        zf.writestr("META-INF/container.xml", """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>""")
        zf.writestr("OEBPS/style.css", css.strip())

        manifest_items = [
            '<item id="style" href="style.css" media-type="text/css"/>',
            '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>'
        ]
        spine_items = []
        nav_links = []

        for idx, (title, paras) in enumerate(chapters, start=1):
            fname = f"chapter_{idx:03d}.xhtml"
            item_id = f"ch{idx:03d}"
            manifest_items.append(f'<item id="{item_id}" href="{fname}" media-type="application/xhtml+xml"/>')
            spine_items.append(f'<itemref idref="{item_id}"/>')
            nav_links.append(f'<li><a href="{fname}">{html.escape(title)}</a></li>')

            body_lines = [f"<h1>{html.escape(title)}</h1>"]
            is_first_para = True
            for p in paras:
                if p == "__SCENE_BREAK__":
                    body_lines.append('<hr class="scenebreak"/>')
                    is_first_para = True
                elif p.lstrip().startswith(">"):
                    q_lines = [line.lstrip("> ").strip() for line in p.splitlines() if line.lstrip("> ").strip()]
                    q_html = []
                    for ql in q_lines:
                        if ql.startswith("—") or ql.startswith("--"):
                            q_html.append(f'<p class="attribution">{format_inline_markdown(ql)}</p>')
                        else:
                            q_html.append(f'<p>{format_inline_markdown(ql)}</p>')
                    body_lines.append('<blockquote class="archival">' + "".join(q_html) + '</blockquote>')
                    is_first_para = True
                else:
                    cls = ' class="first"' if is_first_para else ""
                    body_lines.append(f"<p{cls}>{format_inline_markdown(p)}</p>")
                    is_first_para = False

            chapter_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
{chr(10).join(body_lines)}
</body>
</html>"""
            zf.writestr(f"OEBPS/{fname}", chapter_xhtml)

        nav_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>Table of Contents</title><link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>Contents</h1>
    <ol>
      {chr(10).join(nav_links)}
    </ol>
  </nav>
</body>
</html>"""
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml)

        content_opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookId">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">urn:uuid:{book_uuid}</dc:identifier>
    <dc:title>{html.escape(BOOK_TITLE)}</dc:title>
    <dc:creator>{html.escape(BOOK_AUTHOR)}</dc:creator>
    <dc:language>en</dc:language>
    <meta property="dcterms:modified">{now_iso}</meta>
  </metadata>
  <manifest>
    {chr(10).join(manifest_items)}
  </manifest>
  <spine>
    {chr(10).join(spine_items)}
  </spine>
</package>"""
        zf.writestr("OEBPS/content.opf", content_opf)

def build_print_html(chapters: list[tuple[str, list[str]]]):
    sections = []
    for title, paras in chapters:
        lines = [f"<section class='chapter'><h1>{html.escape(title)}</h1>"]
        is_first = True
        for p in paras:
            if p == "__SCENE_BREAK__":
                lines.append('<div class="scenebreak">* * *</div>')
                is_first = True
            else:
                cls = ' class="first"' if is_first else ""
                lines.append(f"<p{cls}>{format_inline_markdown(p)}</p>")
                is_first = False
        lines.append("</section>")
        sections.append("\n".join(lines))

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{html.escape(BOOK_TITLE)}</title>
<style>
  @page {{ size: 6in 9in; margin: 0.85in 0.75in 0.9in 0.75in; }}
  body {{ font-family: Georgia, "Palatino Linotype", serif; font-size: 11pt; line-height: 1.55; color: #111; max-width: 42em; margin: 2em auto; padding: 0 1em; }}
  .title-page {{ text-align: center; page-break-after: always; padding-top: 35%; margin-bottom: 4em; }}
  .title-page h1 {{ font-size: 28pt; font-weight: normal; letter-spacing: 0.08em; margin-bottom: 0.5em; }}
  .title-page h2 {{ font-size: 14pt; font-weight: normal; color: #444; }}
  section.chapter {{ page-break-before: always; margin-top: 3em; }}
  section.chapter h1 {{ font-size: 16pt; font-weight: normal; text-align: center; letter-spacing: 0.08em; margin: 2.5em 0 2em 0; }}
  p {{ margin: 0; text-indent: 1.5em; text-align: justify; hyphens: auto; }}
  p.first {{ text-indent: 0; }}
  .scenebreak {{ text-align: center; margin: 1.5em 0; letter-spacing: 0.3em; }}
</style>
</head>
<body>
  <div class="title-page">
    <h1>{html.escape(BOOK_TITLE)}</h1>
    <h2>{html.escape(BOOK_AUTHOR)}</h2>
  </div>
  {chr(10).join(sections)}
</body>
</html>"""
    PRINT_HTML_PATH.write_text(html_doc, encoding="utf-8")

if __name__ == "__main__":
    raw = MANUSCRIPT_PATH.read_text(encoding="utf-8", errors="replace")
    total_words = len(raw.split())
    chapters = parse_into_chapters(raw)
    build_epub(chapters)
    build_print_html(chapters)
    print(f"\n==========================================")
    print(f"SOURCE FILE:       {MANUSCRIPT_PATH.name}")
    print(f"FINAL NOVEL STATS: {total_words:,} words (~{total_words // 275:,} pages)")
    print(f"Detected {len(chapters)} chapters:")
    for i, (t, p_list) in enumerate(chapters, 1):
        w_count = sum(len(p.split()) for p in p_list if p != "__SCENE_BREAK__")
        print(f"  [{i:02d}] {t} ({w_count:,} words)")
    print(f" -> E-Reader EPUB:  {EPUB_PATH.resolve()}")
    print(f" -> Print/PDF HTML: {PRINT_HTML_PATH.resolve()}")
    print(f"==========================================\n")
