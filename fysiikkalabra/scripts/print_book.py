"""Print a whole course as one A5 book (teacher 2026-11-03): the theory and worked examples of every chapter exactly as
the site shows them, no tasks or interactive parts; a QR code at the start of each chapter leads to its page on the
web (simulation, tasks and model solutions).

    python scripts/print_book.py FY1 [--lang fi|en|fi-easy] [--out print]

Writes two PDFs:
  <out>/<C>-<lang>-A5.pdf          the book page by page (for reading on a screen or an A5 printer)
  <out>/<C>-<lang>-A4-tulostus.pdf two A5 pages on each A4 sheet in cut-and-stack order: print double-sided
                                    (flip on the short edge), cut the stack in half, put the left half on top of the
                                    right half and bind the left edge (staples or comb binding).
Reads the committed site/ pages, so build the site first. Needs playwright, segno, pypdf and reportlab."""
import argparse, html, io, json, pathlib, re, sys

import segno
from pypdf import PdfReader, PdfWriter, PageObject, Transformation
from playwright.sync_api import sync_playwright
from reportlab.pdfgen import canvas

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _browser import launch  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
BASE_URL = "https://ruukkilab.fi/"
MM = 72 / 25.4
A5 = (148 * MM, 210 * MM)

TEXT = {
    "fi": {"qr": "Simulaatio, tehtävät ja malliratkaisut verkossa", "toc": "Sisällys",
           "course_qr": "Kurssi verkossa", "note": "Teoria ja esimerkit verkkomateriaalista Ruukkilabra"},
    "fi-easy": {"qr": "Simulaatio, tehtävät ja ratkaisut verkossa", "toc": "Sisällys",
                "course_qr": "Kurssi verkossa", "note": "Teoria ja esimerkit verkkomateriaalista Ruukkilabra"},
    "en": {"qr": "Simulation, tasks and model solutions online", "toc": "Contents",
           "course_qr": "The course online", "note": "Theory and worked examples from Ruukkilabra"},
}

# The book keeps the opening (title, question, picture, goals), the theory and the worked examples. Everything a
# student answers or operates on the web is left out: predictions, the investigation, the simulation, tasks, the
# check, the exercises, hints and model solutions, the optional boxes that hold a task, navigation and buttons.
BOOK_CSS = """
@page{size:A5;margin:13mm 14mm 15mm 14mm}
html,body{background:#fff!important}
main{font-size:10pt!important;line-height:1.42!important}main *{font-size:inherit}
main h1{font-size:17pt!important;line-height:1.2!important}main h2{font-size:13pt!important}main h3{font-size:11pt!important}
#ennusta,#tutki,#sim,#tarkista,#exercises,nav,.chapter-nav,details.sim-box,details.fold,details.hint,details.answer,
details.solution,.solution,.pad,.pad-open,button,.stage-no,.skip-link,
.activity:not(.act-theory):not(.act-hook),details.opt:has(.activity:not(.act-theory):not(.act-hook)),
a[href*="kasitetakomo"],a[href*="takomo"],#credits,.unit-credits{display:none!important}
/* the photo credits list at the end of a chapter is left out: every photo's caption names its author and licence */
/* a table prints flat: no scroll-cue shadows at its edges (they printed as grey bands), nothing hidden by scrolling */
table{background:#fff!important;overflow:visible!important}
/* a box never splits over two pages (a box taller than a page still breaks, there is no other way) */
blockquote,.katex-display,.notice,table,.eq-chain,.example-task,.intro-aside,.kc,details.opt,.worked .step,.fig,.fig-row,
figure,.book-qr{break-inside:avoid}
.intro-row{flex-direction:column!important}svg{max-width:100%;height:auto}img{max-width:100%}
.book-qr{display:flex;gap:4mm;align-items:center;margin:0 0 5mm;padding:2.5mm 3mm;border:1px solid #bbb;border-radius:2mm;break-inside:avoid}
.book-qr svg{width:21mm;height:21mm;flex:none}.book-qr p{margin:0;font-size:8.5pt!important;line-height:1.35}
.book-qr .u{font-family:monospace;word-break:break-all}
"""


def qr_svg(url):
    buf = io.BytesIO()
    segno.make(url, error="m").save(buf, kind="svg", scale=4, border=1, xmldecl=False, svgns=True)
    return buf.getvalue().decode()


def chapters(course, lang):
    cur = json.loads((ROOT / "curriculum.json").read_text(encoding="utf-8"))
    sub = SITE if lang == "fi" else SITE / lang
    out = []
    for les in cur[course]["lessons"]:
        f = sub / f"{les['id']}.html"
        if f.exists():
            out.append((les["id"], f))
    if not out:
        sys.exit(f"no built pages for {course} in {sub}")
    return out, sub


def page_url(lang, name):
    return BASE_URL + ("" if lang == "fi" else lang + "/") + name


def render_chapter(page, f, url, label):
    page.goto(f.as_uri(), wait_until="networkidle")
    page.evaluate("() => window.dispatchEvent(new Event('beforeprint'))")
    # the title as HTML: a formula in it stays KaTeX (rule 1); the MathML copy is dropped so it is not printed twice
    title = page.evaluate("() => { const h = document.querySelector('main h1'); if (!h) return document.title; "
                          "const c = h.cloneNode(true); c.querySelectorAll('.katex-mathml').forEach((m) => m.remove()); "
                          "return c.innerHTML.trim(); }")
    page.add_style_tag(content=BOOK_CSS)
    box = (f'<div class="book-qr">{qr_svg(url)}<p>{html.escape(label)}:<br>'
           f'<span class="u">{html.escape(url.replace("https://", ""))}</span></p></div>')
    page.evaluate("(b) => { const h = document.querySelector('main h1'); "
                  "const q = h.closest('.intro-head')?.querySelector('blockquote') || h; q.insertAdjacentHTML('afterend', b); }", box)
    return title, page.pdf(format="A5", print_background=True, prefer_css_page_size=True)


FONTS = SITE / "vendor/fonts"
BRAND = SITE / "brand"
SITE_HOME = "https://ruukkilab.fi/"
# the covers in the site's colours, kept light for a school printer (teacher 2026-11-07): cream paper with the
# Ruukkilabra wordmark (its subtitle is part of the logo), the course in forest green over a thin green and copper
# rule, the school's logo in black; the back cover has the site's address with a QR code. Covers have no margins.
FRONT_CSS = """
@font-face{font-family:"Fraunces";font-weight:100 900;src:url(%(fraunces)s) format("woff2")}
@font-face{font-family:"Plus Jakarta Sans";font-weight:200 800;src:url(%(jakarta)s) format("woff2")}
@page{size:A5;margin:16mm 15mm}@page cover{margin:0}
html,body{margin:0}body{font-family:"Plus Jakarta Sans",Arial,sans-serif;color:#14171e;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.cover{page:cover;box-sizing:border-box;width:148mm;height:209.5mm;display:flex;flex-direction:column;background:#f7f3ec;
  padding:22mm 16mm 16mm;overflow:hidden}
.logo{display:block;width:92mm;height:auto}
.rule{height:1.6mm;margin:30mm 0 9mm;background:linear-gradient(to right,#1a4b2e 0 72%%,#d76a10 72%% 100%%);width:40mm}
.code{font:700 40pt/1 "Fraunces",Georgia,serif;color:#1a4b2e}
h1{font:600 20pt/1.22 "Fraunces",Georgia,serif;margin:4mm 0 0;max-width:112mm;color:#14532d}
.foot{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between;gap:6mm}
.school{width:54mm;height:auto}
.back{break-before:page;justify-content:space-between;align-items:center;text-align:center}
.back .symbol{width:30mm;height:auto;margin-top:10mm}
.back .note{font-size:9pt;color:#474c5b;margin:6mm 0 0;max-width:90mm;line-height:1.45}
.qr{display:flex;flex-direction:column;align-items:center;gap:3mm;font:700 14pt "Plus Jakarta Sans",sans-serif;color:#1a4b2e}
.qr svg{width:30mm;height:30mm}
.blank{break-before:page;height:1mm}
h2{font:700 15pt "Fraunces",Georgia,serif;color:#14532d;margin:0 0 6mm;break-before:page}
ol{list-style:none;padding:0;margin:0;font-size:10pt}
li{display:flex;gap:2mm;margin:0 0 2.6mm;line-height:1.3}li .n{flex:none;width:7mm;color:#14532d;font-weight:700}
li .t{flex:1}li .p{flex:none;width:8mm;text-align:right}""" % {
    "fraunces": (FONTS / "fraunces-latin-wght-normal.woff2").as_uri(),
    "jakarta": (FONTS / "plus-jakarta-sans-latin-wght-normal.woff2").as_uri()}


def _doc(lang, body):
    return (f'<!doctype html><html lang="{lang[:2]}"><meta charset="utf-8">'
            f'<link rel="stylesheet" href="{(SITE / "vendor/katex/katex.min.css").as_uri()}"><style>{FRONT_CSS}</style>'
            f'<body>{body}</body></html>')


def front_html(course, lang, course_title, toc, toc_start):
    t = TEXT[lang]
    logo = BRAND / ("ruukkilabra-logo-en.svg" if lang == "en" else "ruukkilabra-logo-fi.svg")
    rows = "".join(f'<li><span class="n">{i}</span><span class="t">{title}</span>'
                   f'<span class="p">{p}</span></li>' for i, (title, p) in enumerate(toc, 1))
    return _doc(lang, f'<div class="cover"><img class="logo" src="{logo.as_uri()}" alt="Ruukkilabra">'
                      f'<div class="rule"></div><div class="code">{course}</div><h1>{html.escape(course_title)}</h1>'
                      f'<div class="foot"><img class="school" src="{(BRAND / "kiviruukin-lukio-rivi-musta.svg").as_uri()}" '
                      f'alt="Kiviruukin lukio"></div></div>'
                      f'<div class="blank"></div><h2>{t["toc"]}</h2><ol>{rows}</ol>')


def back_html(lang):
    t = TEXT[lang]
    return _doc(lang, f'<div class="cover back"><div><img class="symbol" src="{(BRAND / "ruukkilabra-symboli.svg").as_uri()}" '
                      f'alt=""><p class="note">{t["note"]}</p></div>'
                      f'<div class="qr">{qr_svg(SITE_HOME)}ruukkilab.fi</div>'
                      f'<img class="school" src="{(BRAND / "kiviruukin-lukio-rivi-musta.svg").as_uri()}" alt="Kiviruukin lukio">'
                      f'</div>')


def number_pages(reader, skip, stop):
    """Stamps the page number at the foot of the pages from index `skip` up to `stop`."""
    out = PdfWriter()
    for i, pg in enumerate(reader.pages):
        if skip <= i < stop:
            buf = io.BytesIO()
            w, h = float(pg.mediabox.width), float(pg.mediabox.height)
            c = canvas.Canvas(buf, pagesize=(w, h))
            c.setFont("Helvetica", 8)
            c.setFillGray(.35)
            c.drawCentredString(w / 2, 7 * MM, str(i + 1))
            c.save()
            pg.merge_page(PdfReader(buf).pages[0])
        out.add_page(pg)
    return out


def cut_and_stack(src):
    """Two A5 pages on each A4 landscape sheet. With N pages (padded to a multiple of 4) the left halves of the stack
    hold pages 1..N/2 and the right halves N/2+1..N, so after one cut the left half goes on top of the right half."""
    pages = list(src.pages)
    w, h = float(pages[0].mediabox.width), float(pages[0].mediabox.height)
    n = -(-len(pages) // 4) * 4
    pages += [PageObject.create_blank_page(width=w, height=h) for _ in range(n - len(pages))]
    half = n // 2
    out = PdfWriter()
    for i in range(n // 4):
        for left, right in ((2 * i, half + 2 * i), (half + 2 * i + 1, 2 * i + 1)):   # front, back (short-edge flip)
            s = PageObject.create_blank_page(width=2 * w, height=h)
            s.merge_transformed_page(pages[left], Transformation())
            s.merge_transformed_page(pages[right], Transformation().translate(w, 0))
            out.add_page(s)
    return out, n


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("course")
    ap.add_argument("--lang", default="fi", choices=sorted(TEXT))
    ap.add_argument("--out", default=str(ROOT / "print"))
    a = ap.parse_args()
    course = a.course.upper()
    chs, sub = chapters(course, a.lang)
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    label = TEXT[a.lang]["qr"]
    with sync_playwright() as pw:
        b = launch(pw)
        page = b.new_page()
        rendered = []
        for cid, f in chs:
            title, pdf = render_chapter(page, f, page_url(a.lang, f.name), label)
            rendered.append((title, PdfReader(io.BytesIO(pdf))))
            print(f"{cid}: {len(rendered[-1][1].pages)} pages", file=sys.stderr)
        index = sub / f"{course}.html"
        course_title = course
        if index.exists():
            page.goto(index.as_uri())
            course_title = page.evaluate("() => document.querySelector('main h1')?.textContent.trim() || ''") or course
            course_title = re.sub(rf"^{course}\s*[:·–-]?\s*", "", course_title)
        # cover, blank back, contents: render once to count the contents pages, then with the real page numbers
        front_n = 0
        for _ in range(2):
            p, toc = front_n + 1, []
            for title, r in rendered:
                toc.append((title, p))
                p += len(r.pages)
            front_file = out / f".{course}-{a.lang}-front.html"   # a file, so the page may load KaTeX's file:// CSS
            front_file.write_text(front_html(course, a.lang, course_title, toc, front_n), encoding="utf-8")
            page.goto(front_file.as_uri(), wait_until="networkidle")
            front_file.unlink()
            front = PdfReader(io.BytesIO(page.pdf(format="A5", prefer_css_page_size=True)))
            if len(front.pages) == front_n:
                break
            front_n = len(front.pages)
        back_file = out / f".{course}-{a.lang}-back.html"
        back_file.write_text(back_html(a.lang), encoding="utf-8")
        page.goto(back_file.as_uri(), wait_until="networkidle")
        back_file.unlink()
        back = PdfReader(io.BytesIO(page.pdf(format="A5", prefer_css_page_size=True)))
        b.close()
    book = PdfWriter()
    for r in [front] + [r for _, r in rendered]:
        for pg in r.pages:
            book.add_page(pg)
    content = len(book.pages)
    # blank pages before the back cover, so the back cover is the last page of a folded booklet (pages = 4k)
    w, h = float(book.pages[0].mediabox.width), float(book.pages[0].mediabox.height)
    for _ in range(-(content + 1) % 4):
        book.add_blank_page(width=w, height=h)
    book.add_page(back.pages[0])
    buf = io.BytesIO()
    book.write(buf)
    numbered = number_pages(PdfReader(buf), skip=2, stop=content)
    a5 = out / f"{course}-{a.lang}-A5.pdf"
    with open(a5, "wb") as fh:
        numbered.write(fh)
    sheets, n = cut_and_stack(PdfReader(a5))
    a4 = out / f"{course}-{a.lang}-A4-tulostus.pdf"
    with open(a4, "wb") as fh:
        sheets.write(fh)
    print(f"{a5}: {len(PdfReader(a5).pages)} A5 pages; {a4}: {n // 4} A4 sheets, double-sided")


if __name__ == "__main__":
    main()
