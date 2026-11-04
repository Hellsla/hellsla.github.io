"""Chapter cards (teacher 2026-11-03 "Ruukkikortit", extended to the school's own courses 2026-11-04): one card per
chapter with its opening illustration, "Luku n", its title and its opening question, the cards grouped under section
labels in one continuous grid (a section's label above its first card). One markup for every course page, so
site.css styles them all alike:

  module pages FY1–FY8     build.py chapter_cards: lessons under the module's themes
  local course units       local_courses.page_body: FY9, FY14 units under the course's chapters
  investigation bank       investigations.bank: FY10 investigations under their topics (the filter moves a topic's label to its first card shown)

  <ol class="lessons ch-cards"><li class="live ch-card"><h3 class="ch-theme">Section</h3><div class="ch-box">…</div></li>
    <li class="soon ch-card"><div class="ch-box">…</div></li></ol>
  a local course chapter's label: <div class="ch-label"><h3 class="ch-theme">…</h3><p class="ch-theme-q">question</p></div>
"""
import re

HERO = re.compile(r'<svg\b[^>]*data-fig="hero".*?</svg>', re.S)


def hero(text):
    """The opening illustration (<svg data-fig="hero">) of a page or a source text, made decorative for a card: the
    title and the question beside it say what it shows, so its role, description, class and style go."""
    m = HERO.search(text or "")
    if not m: return ""
    head, rest = m.group(0).split(">", 1)
    svg = re.sub(r'\s(?:role|aria-label|aria-labelledby|class|style)="[^"]*"', "", head) + ">" + rest
    svg = svg.replace("<svg", '<svg aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMid slice"', 1)
    return re.sub(r"<title\b.*?</title>|<desc\b.*?</desc>", "", svg, flags=re.S)


def md_question(text):
    """The opening question of a source text (`> **Miksi** …` / `> **Why** …`) as card HTML: bold dropped, *emphasis*
    kept as <em>, inline HTML (a <span lang>) and $maths$ as written."""
    m = re.search(r"^> (\*\*.+)$", text or "", re.M)
    if not m: return ""
    q = m.group(1).replace("**", "")
    return re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", q).strip()


def label(heading, lead="", attrs=""):
    """A section's label, carried by its first card (one continuous grid, teacher 2026-11-04): the heading, and for a
    local course chapter its question under it."""
    h = f'<h3 class="ch-theme"{attrs}>{heading}</h3>'
    return f'<div class="ch-label">{h}<p class="ch-theme-q"{attrs}>{lead}</p></div>' if lead else h


def card(num, title, href=None, why="", svg="", tags="", cls="", attrs="", lab=""):
    """One card. num and title are HTML; href None = a chapter still coming (a dashed card without a link or picture).
    cls adds classes after "live ch-card"; attrs (a leading space) adds attributes to the <li> (filter data); lab is
    the label (label()) of a section that starts at this card."""
    num = f'<span class="l-num">{num}</span>'
    if href is None:
        return (f'<li class="soon ch-card{cls}"{attrs}>{lab}<div class="ch-box">{num}<span class="ch-title">{title}</span>'
                + (f'<p class="ch-tags">{tags}</p>' if tags else "") + "</div></li>")
    return (f'<li class="live ch-card{cls}"{attrs}>{lab}<div class="ch-box">{num}<a href="{href}">{title}</a>'
            + (f'<p class="ch-why">{why}</p>' if why else "") + (f'<p class="ch-tags">{tags}</p>' if tags else "")
            + (f'<div class="ch-img">{svg}</div>' if svg else "") + "</div></li>")


def grid(items, attrs=""):
    """The cards in one continuous grid: a section's label sits above its first card, so a short section leaves no hole."""
    return f'<ol class="lessons ch-cards"{attrs}>{items}</ol>' if items else ""
