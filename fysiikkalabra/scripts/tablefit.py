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
CELL = re.compile(r"(<(?:t[hd]|caption)\b[^>]*>)(.*?)(</(?:t[hd]|caption)>)", re.S)
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


if __name__ == "__main__":
    for w in sys.argv[1:]: print(hyphenate_fi(w).replace(SHY, "-"))
