"""Tables never scroll sideways (teacher 2026-11-08: "en halua että taulukkoja täytyy scrollata").

The cells of a table wrap their words at every width (site.css). A long Finnish word in a header ("satunnaisvirhe",
"vaihteluvälin") does not break by itself, because browsers hyphenate Finnish unevenly (Chromium has no Finnish
dictionary), so the build puts soft hyphens (U+00AD, shown only at a line break) at the syllable boundaries of every
long word in a table cell of a Finnish page; a heading written as one formula of words ($\\text{...}$) gets its
words out of the formula, since a formula never wraps. Other formulas ($...$) and tags are left alone. check_layout.py fails a page
whose table is wider than its box.

Usage: python scripts/tablefit.py "satunnaisvirhe"   (prints the word with its breaks marked)"""
import re, sys

SHY = "\u00ad"
VOWELS = set("aeiouyäöåAEIOUYÄÖÅ")
MIN_WORD = 9                                       # shorter words fit a phone's narrowest column as they are
CELL = re.compile(r"(<(?:t[hd]|caption)\b[^>]*>)(.*?)(<\\?/(?:t[hd]|caption)>)", re.S)   # <\/td>: a cell inside a script's JSON string (a simulation's table text) ends there, not at the page's next real </td>
SKIP = re.compile(r"(<[^>]*>|\$\$.*?\$\$|\$[^$]*\$|\\\(.*?\\\)|&[#\w]+;)", re.S)   # tags, formulas, entities
WORD = re.compile(r"[A-Za-zÅÄÖåäö]{%d,}" % MIN_WORD)


def hyphenate_fi(word):
    """Finnish syllable rule: a break before a consonant that is followed by a vowel (sa-tun-nais-vir-he, spekt-ri);
    at least two letters stay on each side."""
    out = []
    for i, ch in enumerate(word):
        if 2 <= i <= len(word) - 2 and ch not in VOWELS and word[i + 1] in VOWELS and word[i - 1].isalpha():
            out.append(SHY)
        out.append(ch)
    return "".join(out)


HOIST = re.compile(r"\$\\text\{([^{}$\\]* [^{}$\\]*)\}(?:\\[ ,;]|\s)*(\([^$]*\))?\$")


def _hoist(m):
    r"""A heading set as one formula of words, "$\text{etäisyys kasvaimesta}\ (\text{cm})$", cannot wrap: its words
    go out of the formula and only the unit stays maths, "etäisyys kasvaimesta $(\text{cm})$"."""
    return m.group(1) + (f" ${m.group(2)}$" if m.group(2) else "")


def _cell(text, finnish):
    text = HOIST.sub(_hoist, text)
    if not finnish: return text
    parts = SKIP.split(text)
    return "".join(p if i % 2 else WORD.sub(lambda m: hyphenate_fi(m.group(0)), p) for i, p in enumerate(parts))


def fit(html, finnish):
    """Every table cell and caption of a built page: headings of words out of their formula, and on a Finnish page
    soft hyphens in the long words. Running it again changes nothing."""
    return CELL.sub(lambda m: m.group(1) + _cell(m.group(2).replace(SHY, ""), finnish) + m.group(3), html)


CARD_TITLE = re.compile(r'(<div class="ch-box">(?:(?!</li>).)*?(?:<a href="[^"]*">|<span class="ch-title">))(.*?)(</a>|</span>)', re.S)
CARD_WORD = re.compile(r"[A-Za-zÅÄÖåäö]{14,}")     # a card's title column holds about 14 letters: a shorter word goes whole to the next line


PARTS = re.compile(r"(?<=[a-zåäö]{3})(?=(?:energia|asteikko|aalto|aallo|aika|uuni|ääni|aktiivi|ulottei))")


def hyphenate_card(word):
    """hyphenate_fi with the joints of a compound whose later part begins with a vowel: the syllable rule alone never
    breaks before a vowel, so it would give "potentiaa-lienergia" and "puoliintumi-saika". The parts listed are the
    ones the card titles have; a part not listed is simply not broken at its joint."""
    return SHY.join(hyphenate_fi(part) for part in PARTS.split(word))


def cards(html, finnish):
    """The title of every chapter, unit and investigation card (cardgrid.py) on a Finnish page: soft hyphens in its
    very long words, so that "Liukukitkakertoimen" breaks at a syllable with a hyphen and not in the middle of one
    without (UI audit 2026-11-10, finding 16; site.css asks for hyphens:auto, which Chromium has no Finnish
    dictionary for). Running it again changes nothing."""
    if not finnish: return html
    def one(m):
        parts = SKIP.split(m.group(2).replace(SHY, ""))
        return m.group(1) + "".join(p if i % 2 else CARD_WORD.sub(lambda w: hyphenate_card(w.group(0)), p) for i, p in enumerate(parts)) + m.group(3)
    return CARD_TITLE.sub(one, html)


if __name__ == "__main__":
    for w in sys.argv[1:]: print(hyphenate_fi(w).replace(SHY, "-"))
