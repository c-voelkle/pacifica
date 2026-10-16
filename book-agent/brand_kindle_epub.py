import re
import uuid
import html
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BOOK_TITLE     = "The Grand Confederation of Pacifica"
BOOK_SUBTITLE  = ""
BOOK_AUTHOR    = "Curtis Völkle"
AUTHOR_SORT    = "Völkle, Curtis"
PUBLISHER      = "Pacifica Press"
PUBLICATION_DT = "2026-10-14"
LANGUAGE       = "en"
SUBJECTS       = ["Historical Fiction", "Alternate History", "19th Century"]
DESCRIPTION    = (
    "In the fractured wake of American secession, Protector Elias Thorne "
    "forges a sovereign Pacific republic from the forts of Arizona to the "
    "iron grades of the Sierra Nevada and the treaty ports of the Far East."
)

EPUB_PATH = Path("pacifica.epub")
COVER_PATH = Path("cover.jpg")

if Path("manuscript_chaptered.md").exists():
    MANUSCRIPT_PATH = Path("manuscript_chaptered.md")
elif Path("manuscript_polished.md").exists():
    MANUSCRIPT_PATH = Path("manuscript_polished.md")
else:
    MANUSCRIPT_PATH = Path("manuscript.md")

def prepare_cover_image():
    source_img = None
    if Path("cover.png").exists():
        source_img = Path("cover.png")
    else:
        candidates = list(Path(".").glob("ChatGPT-Bild*09_57_53.png")) + list(Path("$env:USERPROFILE/Downloads").glob("ChatGPT-Bild*09_57_53.png"))
        if candidates:
            source_img = candidates[0]

    if not source_img and COVER_PATH.exists():
        print(f"Using existing cover.jpg: {COVER_PATH.resolve()}")
        return

    if source_img:
        print(f"Processing cover image from {source_img.resolve()}...")
        img = Image.open(source_img).convert("RGBA")
        
        target_w, target_h = 1600, 2560
        img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        
        # Create a gradient overlay for the bottom 30% to ensure text readability
        overlay = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
        draw_overlay = ImageDraw.Draw(overlay)
        
        gradient_height = 700
        start_y = target_h - gradient_height
        for y in range(gradient_height):
            # Smooth fade from transparent to dark navy/black
            alpha = int(220 * (y / gradient_height) ** 1.5)
            draw_overlay.line([(0, start_y + y), (target_w, start_y + y)], fill=(10, 14, 22, alpha))
            
        img = Image.alpha_composite(img, overlay).convert("RGB")
        draw = ImageDraw.Draw(img)
        
        # Load serif font for author name
        font = None
        for font_name in ["georgia.ttf", "times.ttf", "palabi.ttf", "arial.ttf"]:
            try:
                font = ImageFont.truetype(font_name, 64)
                break
            except Exception:
                continue
        if not font:
            font = ImageFont.load_default()

        author_text = BOOK_AUTHOR.upper()
        bbox = draw.textbbox((0, 0), author_text, font=font)
        tw = bbox[2] - bbox[0]
        tx = (target_w - tw) / 2
        ty = target_h - 160

        # Crisp shadow and high-contrast cream text
        draw.text((tx + 3, ty + 3), author_text, font=font, fill=(0, 0, 0))
        draw.text((tx, ty), author_text, font=font, fill=(242, 236, 222))

        img.save(COVER_PATH, "JPEG", quality=95)
        print(f"Cover enhanced with gradient banner and author name: {COVER_PATH.resolve()}")
    else:
        raise FileNotFoundError("Could not locate cover image PNG in folder or Downloads.")

def format_inline_markdown(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escaped)
    escaped = re.sub(r'\*(.+?)\*', r'<em>\1</em>', escaped)
    return escaped

def parse_into_chapters(raw_text: str) -> list[tuple[str, list[str]]]:
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
        if not has_explicit_headers and current_words >= 6500:
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

def build_kindle_epub(chapters: list[tuple[str, list[str]]]):
    prepare_cover_image()
    book_uuid = str(uuid.uuid4())
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    css = """
    body { font-family: Georgia, "Bookerly", serif; line-height: 1.6; margin: 4%; color: #111; }
    .cover-page { margin: 0; padding: 0; text-align: center; }
    .cover-page img { max-width: 100%; max-height: 100%; object-fit: contain; }
    .title-page { text-align: center; margin-top: 22%; page-break-after: always; }
    .title-page h1 { font-size: 2.2em; font-weight: normal; letter-spacing: 0.08em; margin-bottom: 0.3em; }
    .title-page h2 { font-size: 1.1em; font-weight: normal; font-style: italic; color: #444; margin-top: 0; margin-bottom: 2.5em; }
    .title-page .author { font-size: 1.3em; letter-spacing: 0.06em; margin-top: 2em; }
    .title-page .publisher { font-size: 0.85em; letter-spacing: 0.12em; margin-top: 6em; color: #666; }
    h1.chapter-title { text-align: center; font-size: 1.4em; font-weight: normal; letter-spacing: 0.06em; margin-top: 2.5em; margin-bottom: 2em; page-break-before: always; }
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
        zf.write(COVER_PATH, "OEBPS/cover.jpg")

        cover_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
  <title>Cover</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body class="cover-page" epub:type="cover">
  <div><img src="cover.jpg" alt="{html.escape(BOOK_TITLE)} Cover"/></div>
</body>
</html>"""
        zf.writestr("OEBPS/cover.xhtml", cover_xhtml)

        subtitle_html = f"<h2>{html.escape(BOOK_SUBTITLE)}</h2>" if BOOK_SUBTITLE else ""
        title_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
  <title>{html.escape(BOOK_TITLE)}</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
  <div class="title-page" epub:type="titlepage">
    <h1>{html.escape(BOOK_TITLE)}</h1>
    {subtitle_html}
    <p class="first author">{html.escape(BOOK_AUTHOR)}</p>
    <p class="first publisher">{html.escape(PUBLISHER)}</p>
  </div>
</body>
</html>"""
        zf.writestr("OEBPS/titlepage.xhtml", title_xhtml)

        manifest_items = [
            '<item id="style" href="style.css" media-type="text/css"/>',
            '<item id="cover-image" href="cover.jpg" media-type="image/jpeg" properties="cover-image"/>',
            '<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>',
            '<item id="titlepage" href="titlepage.xhtml" media-type="application/xhtml+xml"/>',
            '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
            '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>'
        ]
        spine_items = [
            '<itemref idref="cover" linear="no"/>',
            '<itemref idref="titlepage"/>',
            '<itemref idref="nav"/>'
        ]
        nav_links = ['<li><a href="titlepage.xhtml">Title Page</a></li>']
        ncx_navpoints = []

        for idx, (title, paras) in enumerate(chapters, start=1):
            fname = f"chapter_{idx:03d}.xhtml"
            item_id = f"ch{idx:03d}"
            manifest_items.append(f'<item id="{item_id}" href="{fname}" media-type="application/xhtml+xml"/>')
            spine_items.append(f'<itemref idref="{item_id}"/>')
            nav_links.append(f'<li><a href="{fname}">{html.escape(title)}</a></li>')
            ncx_navpoints.append(f"""    <navPoint id="navPoint-{idx}" playOrder="{idx}">
      <navLabel><text>{html.escape(title)}</text></navLabel>
      <content src="{fname}"/>
    </navPoint>""")

            body_lines = [f'<h1 class="chapter-title">{html.escape(title)}</h1>']
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

        first_ch_href = "chapter_001.xhtml" if chapters else "titlepage.xhtml"
        nav_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>Table of Contents</title><link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
  <nav epub:type="toc" id="toc">
    <h1 class="chapter-title">Contents</h1>
    <ol>
      {chr(10).join(nav_links)}
    </ol>
  </nav>
  <nav epub:type="landmarks" hidden="hidden">
    <ol>
      <li><a epub:type="cover" href="cover.xhtml">Cover</a></li>
      <li><a epub:type="toc" href="nav.xhtml">Table of Contents</a></li>
      <li><a epub:type="bodymatter" href="{first_ch_href}">Start of Book</a></li>
    </ol>
  </nav>
</body>
</html>"""
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml)

        toc_ncx = f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="urn:uuid:{book_uuid}"/>
    <meta name="dtb:depth" content="1"/>
  </head>
  <docTitle><text>{html.escape(BOOK_TITLE)}</text></docTitle>
  <navMap>
{chr(10).join(ncx_navpoints)}
  </navMap>
</ncx>"""
        zf.writestr("OEBPS/toc.ncx", toc_ncx)

        subjects_xml = "\n    ".join(f"<dc:subject>{html.escape(s)}</dc:subject>" for s in SUBJECTS)

        content_opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookId">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:identifier id="BookId">urn:uuid:{book_uuid}</dc:identifier>
    <dc:title>{html.escape(BOOK_TITLE)}</dc:title>
    <dc:creator id="creator">{html.escape(BOOK_AUTHOR)}</dc:creator>
    <meta refines="#creator" property="role" scheme="marc:relators">aut</meta>
    <meta refines="#creator" property="file-as">{html.escape(AUTHOR_SORT)}</meta>
    <dc:publisher>{html.escape(PUBLISHER)}</dc:publisher>
    <dc:language>{html.escape(LANGUAGE)}</dc:language>
    <dc:date>{html.escape(PUBLICATION_DT)}</dc:date>
    <dc:description>{html.escape(DESCRIPTION)}</dc:description>
    {subjects_xml}
    <meta property="dcterms:modified">{now_iso}</meta>
    <meta name="cover" content="cover-image"/>
  </metadata>
  <manifest>
    {chr(10).join(manifest_items)}
  </manifest>
  <spine toc="ncx">
    {chr(10).join(spine_items)}
  </spine>
  <guide>
    <reference type="cover" title="Cover" href="cover.xhtml"/>
    <reference type="toc" title="Table of Contents" href="nav.xhtml"/>
    <reference type="text" title="Start" href="{first_ch_href}"/>
  </guide>
</package>"""
        zf.writestr("OEBPS/content.opf", content_opf)

if __name__ == "__main__":
    raw = MANUSCRIPT_PATH.read_text(encoding="utf-8", errors="replace")
    chapters = parse_into_chapters(raw)
    build_kindle_epub(chapters)
    print(f"\n==========================================")
    print(f"KINDLE-READY EPUB BUILT: {EPUB_PATH.resolve()}")
    print(f" -> Title:     {BOOK_TITLE}")
    print(f" -> Author:    {BOOK_AUTHOR} (Sorts as: {AUTHOR_SORT})")
    print(f" -> Cover:     {COVER_PATH.resolve()} (Gradient Vignette + Author Added)")
    print(f" -> Chapters:  {len(chapters)}")
    print(f"==========================================\n")
