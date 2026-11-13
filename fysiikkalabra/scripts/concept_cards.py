"""Käsitetakomo concept cards inside Ruukkilabra (teacher 2026-11-03: "kortit tulevat luvun luo, ei päinvastoin").

  python scripts/concept_cards.py check      validates the card data (also run by the build and CI)
  python scripts/concept_cards.py stats      cards per module and chapter, and the bold terms that link to a card

The data: one JSON file per module, `kortit/<module>.json` (Finnish, also used by the fi-easy pages) and
`kortit/en/<module>.json` (English; a module without one has no card sections in English). The build publishes
them unchanged as `site/kortit/<module>.json` and `site/kortit/en/<module>.json`; Käsitetakomo (`site/kasitteet.html`)
reads those files and the lesson, module and Sovella pages carry the same cards from the build, so both read one
source. A file:
  {"moduuli": "FY4", "nimi": "...", "kesken": true (optional), "aiheet": [{"id", "nimi"}],
   "kortit": [{"id", "moduuli", "luku", "aihe", "kasite", "maaritelma", "kaava"?, "kaava_puhe"?, "kuva"?}]}
`id` is permanent (a student's review deck in the browser, `ruukkilabra:kortit`, is keyed by it); `luku` is the
chapter id the card belongs to (null: the card is only in Käsitetakomo); `aihe` the permanent topic id of
Käsitetakomo's topic menu; `kasite` and `maaritelma` the two faces (inline maths as `$...$`); `kaava` display LaTeX
without dollars and `kaava_puhe` how it reads aloud (screen readers, aria-label).

Where the cards appear (one component, templates/kortit.js; never before the Teoriatiivistelmä):
  - a lesson: in Teoriatiivistelmä every bold term that names a card (mark_terms), and the first plain mention of
    each of the chapter's other cards (mark_first, 2026-11-13), opens a popover, and after the
    Tiivistelmä list a row of chips "Tämän luvun käsitteet (n)"; as the last part of Esimerkit "Kertaa luvun
    käsitteet" with the chapter's cards (lesson_section; without JavaScript a definition list), no stage of its own
    in the step navigation (teacher 2026-11-05);
  - a module page: "Kertauspakkasi" (module_section), the cards a student marked "Kertaa myöhemmin";
  - Sovella itsenäisesti: "Varmista käsitteet ennen tehtäviä" (practice_section), only the deck's cards, shown only
    when the deck has some;
  - site/kasitteet.html (app_page_body): topic choice and combining, the student's own deck (?moduuli=FY4&pakka=oma),
    one chapter (&luku=fy4-4). The old addresses ../kasitetakomo.html and ../kasitekortit.html redirect there.
"""
import functools, html as _h, json, pathlib, re, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from courses import ROOT

SRC = ROOT / "kortit"
APP = "kasitteet.html"
ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
FIELDS = ("id", "moduuli", "luku", "aihe", "kasite", "maaritelma")
OPTIONAL = ("kaava", "kaava_puhe", "kuva")
SHOWN = 8          # a lesson's card row shows at most this many; the rest are a link away (teacher 2026-11-03)
UNICODE_MATH = re.compile(r"[₀-₉ₐ-ₜ⁰-⁹⁻⁺²³ΔΣρηαγμλωφπθτν≈·×−]")   # maths written in Unicode instead of LaTeX


def esc(s): return _h.escape(str(s), quote=True)


def data_lang(lang):
    """The card language of a page language: fi-easy pages use the Finnish cards."""
    return "en" if lang == "en" else "fi"


def src_file(code, dl):
    return SRC / (f"{code.lower()}.json" if dl == "fi" else f"{dl}/{code.lower()}.json")


@functools.lru_cache(maxsize=None)
def module(code, dl="fi"):
    f = src_file(code, dl)
    return json.loads(f.read_text(encoding="utf-8")) if f.is_file() else None


def modules(dl="fi"):
    """Every module with a card file, in curriculum order."""
    import courses
    return [c for c in courses.codes() if module(c, dl)]


def cards_of(code, lang):
    m = module(code, data_lang(lang))
    return [] if not m or m.get("kesken") else m["kortit"]


def chapter_cards(code, lid, lang):
    return [c for c in cards_of(code, lang) if c["luku"] == lid]


def has_chapters(code, lang):
    return any(c["luku"] for c in cards_of(code, lang))


def norm(s):
    s = re.sub(r"<[^>]+>|\$[^$]*\$", "", _h.unescape(s))
    return re.sub(r"\s+", " ", s).strip().lower()


def match(term, cards):
    """The card a bold term names: the concept exactly (case aside), or the concept with a Finnish ending
    ("kokonaisvoimaa", "rajanopeudeksi": the concept's stem plus at most five letters, one word). Longer concepts first."""
    t = norm(term)
    if not t: return None
    for c in sorted(cards, key=lambda c: -len(c["kasite"])):
        k = norm(c["kasite"])
        if t == k: return c
        stem = k[:-1] if len(k) > 5 else k
        if len(k) > 4 and t.startswith(stem) and len(t) - len(k) <= 5 and " " not in t[len(stem):] and "-" not in t[len(stem):]: return c
    return None


def mark_terms(stage_html, code, lang):
    """Bold terms of the Teoriatiivistelmä stage that name a card of the module get data-kortti (kortit.js turns them
    into popover buttons; without JavaScript they stay plain bold)."""
    cards = cards_of(code, lang)
    if not cards: return stage_html
    by_len = sorted(cards, key=lambda c: -len(c["kasite"]))
    def one(m):
        t = norm(m.group(1))   # the old rule first, then the Finnish endings of mark_first ("tehoksi" → Teho)
        c = match(m.group(1), cards) or next((c for c in by_len if (rx := term_rx(c["kasite"], lang)) and rx.fullmatch(t)), None)
        return f'<strong class="kc-mark" data-kortti="{c["id"]}">{m.group(1)}</strong>' if c else m.group(0)
    return re.sub(r"<strong>((?:(?!</?strong>).)+?)</strong>", one, stage_html, flags=re.S)


# The chapter's own concepts in plain text (teacher 2026-11-13, "kaikki": FY1 had underlined terms, most chapters had
# none because their Teoria has no bold term naming a card). After mark_terms, the first occurrence of each of the
# chapter's cards that no bold term marked becomes a plain-weight mark of its own: text only, never in a heading, a
# link, a button, a figure, a formula, a bold term or the chips, and only inside the theory text (div.act-theory).
# A build-side mark, so no lesson text changes and no review goes stale.
_FI_CASE = ("", "n", "a", "ä", "ta", "tä", "na", "nä", "ksi", "ssa", "ssä", "sta", "stä", "lla", "llä", "lta", "ltä", "lle",
            "an", "en", "in", "on", "un", "yn", "än", "ön", "hin", "seen", "t", "ja", "jä", "ia", "iä", "ien", "jen", "ihin",
            "issa", "issä", "ista", "istä", "illa", "illä", "ille", "iksi", "ina", "inä", "it", "ita", "itä", "iden", "itten",
            "ineen", "jensa", "nsa", "nsä")
_FI_CLITIC = ("", "kin", "kaan", "kään", "han", "hän")
_FI_END = "(?:" + "|".join(sorted({c + k for c in _FI_CASE for k in _FI_CLITIC if c + k}, key=len, reverse=True)) + ")?"
_WEAK = (("mp", "mm"), ("nt", "nn"), ("nk", "ng"), ("lt", "ll"), ("rt", "rr"), ("kk", "k"), ("pp", "p"), ("tt", "t"), ("ht", "hd"))
_WORD = "A-Za-z0-9ÅÄÖåäöÉéÜü-"


def _fi_stems(w):
    """The stems a Finnish word takes before a case ending, as regex alternatives (the word itself first)."""
    out = [w]
    if w.endswith("nen"): out += [w[:-3] + "se", w[:-3] + "s"]
    if re.search(r"[aeiouyäö](us|ys)$", w): out += [w[:-1] + "de", w[:-1] + "tt"]   # nopeus → nopeuden, nopeutta
    elif w.endswith("s") and len(w) > 4: out += [w[:-1] + "kse", w[:-1] + "ks"]
    if w.endswith("de"): out.append(w[:-2] + "tee")
    elif w.endswith("ke"): out.append(w[:-2] + "kkee")
    elif w.endswith("e"): out.append(w + "e")
    if w[-1:] in "aäoöuyi" and len(w) > 4: out.append(w[:-1])          # the plural: voim-ia, teho-ja
    if w[-1:] in "aäoöuyie":                                           # the weak grade before a closed syllable
        for a, b in _WEAK:
            i = w.rfind(a, max(0, len(w) - 4))
            if i > 0: out.append(w[:i] + b + w[i + len(a):]); break
        else:
            if w.endswith("ki"): out.append(w[:-2] + "i")              # laki → lain
    return out


def _word_rx(w, lang, last):
    w = w.lower()
    if lang == "en":
        return re.escape(w) + ("(?:s|es)?" if last else "") if not w.endswith("y") or not last else re.escape(w[:-1]) + "(?:y|ies)"
    return "(?:" + "|".join(re.escape(s) for s in dict.fromkeys(_fi_stems(w))) + ")" + _FI_END


def term_rx(kasite, lang):
    if "$" in kasite or "\\(" in kasite: return None          # a name with a formula ($\\beta^-$-hajoaminen) stays a card only
    words = norm(kasite).split(" ")
    if not words or not words[0] or words[0].startswith("-"): return None
    body = r"\s+".join(_word_rx(w, lang, i == len(words) - 1) for i, w in enumerate(words))
    return re.compile(rf"(?<![{_WORD}]){body}(?![{_WORD}])", re.I)


_SKIP = {"h1", "h2", "h3", "h4", "h5", "h6", "a", "button", "summary", "strong", "b", "code", "pre", "script", "style",
         "svg", "figure", "label", "select", "option", "textarea", "math", "sup", "sub"}
_VOID = {"br", "img", "input", "hr", "meta", "source", "wbr", "col", "area", "embed", "link", "track", "param"}
# English: a term that only modifies the noun after it is not the concept on its own ("wind power plants" is not Power;
# teacher 2026-11-13: underline power where it first stands by itself)
_EN_COMPOUND = re.compile(r"\s+(?:plants?|stations?|grids?|lines?|supply|supplies|cables?|outlets?|sockets?)\b", re.I)
_MATH = re.compile(r"\$\$.*?\$\$|\$[^$]*\$|\\\(.*?\\\)|\\\[.*?\\\]", re.S)


def mark_first(stage_html, code, lid, lang):
    cards = [c for c in chapter_cards(code, lid, lang) if f'data-kortti="{c["id"]}"' not in stage_html]
    if not cards: return stage_html
    parts = re.split(r"(<[^>]+>)", stage_html)
    stack, ok = [], []          # stack of (tag, skips, theory); ok: indices of text parts a mark may go into
    for i, p in enumerate(parts):
        if p.startswith("<"):
            m = re.match(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)([^>]*)>", p)
            if not m: continue
            close, tag, rest = m.group(1), m.group(2).lower(), m.group(3)
            if close:
                while stack:
                    if stack.pop()[0] == tag: break
            elif tag not in _VOID and not rest.rstrip().endswith("/"):
                cls = re.search(r'class="([^"]*)"', rest)
                cls = cls.group(1).split() if cls else []
                skip = tag in _SKIP or any(k.startswith("kc-") or k in ("fig", "fig-tex", "fig-hero") for k in cls)
                stack.append((tag, skip, "act-theory" in cls))
        elif p.strip() and stack and any(t for _, _, t in stack) and not any(s for _, s, _ in stack):
            ok.append(i)
    taken = {}                  # part index → list of (start, end, card)
    for c in sorted(cards, key=lambda c: -len(c["kasite"])):
        rx = term_rx(c["kasite"], lang)
        if not rx: continue
        for i in ok:
            text = parts[i]
            maths = [m.span() for m in _MATH.finditer(text)]
            hit = next((m for m in rx.finditer(text)
                        if not any(a < m.end() and m.start() < b for a, b in maths)
                        and not (lang == "en" and _EN_COMPOUND.match(text, m.end()))
                        and not any(a < m.end() and m.start() < b for a, b, _ in taken.get(i, []))), None)
            if hit: taken.setdefault(i, []).append((hit.start(), hit.end(), c)); break
    for i, spans in taken.items():
        t = parts[i]
        for a, b, c in sorted(spans, key=lambda s: -s[0]):
            t = t[:a] + f'<span class="kc-mark kc-plain" data-kortti="{c["id"]}">{t[a:b]}</span>' + t[b:]
        parts[i] = t
    return "".join(parts)


def strings(T):
    """The interface texts kortit.js needs (lang "cards.ui"; a key missing in a language falls back to Finnish)."""
    import i18n
    ui = dict(i18n.T("fi")("cards.ui"))
    try: ui.update(T("cards.ui"))
    except KeyError: pass
    return ui


def data_block(T, lang, cards, extra=None, app=None):
    """The cards a page's component works on, as one JSON element (never shown, never read by KaTeX)."""
    d = {"lang": data_lang(lang), "app": app, "strings": strings(T), "cards": cards}
    if extra: d.update(extra)
    return '<script type="application/json" class="kc-data">' + json.dumps(d, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def static_card(c):
    """One card as a definition-list entry: what a reader sees without JavaScript."""
    f = f'<span class="kc-formula">$${c["kaava"]}$$</span>' if c.get("kaava") else ""
    return f'<div class="kc-item" data-id="{c["id"]}"><dt>{esc(c["kasite"])}</dt><dd>{esc(c["maaritelma"])}{f}</dd></div>'


def app_href(code, **q):
    return APP + f"?moduuli={code}" + "".join(f"&amp;{k}={v}" for k, v in q.items())


def chips(code, lid, T, lang):
    """The place of the chips row after the Tiivistelmä list (kortit.js fills it), or "" when the chapter has no cards."""
    return f'<div class="kc-chips" data-luku="{lid}" hidden></div>' if chapter_cards(code, lid, lang) else ""


def lesson_section(code, lid, T, lang, titles):
    """The last part of the Esimerkit stage (teacher 2026-11-05: the cards are practice, no stage of their own in the
    navigation; inquiry.render puts it there), or "" when the chapter has no cards in this language. Closed until
    opened (teacher 2026-11-06: "oletuksena kiinni"); the Käsitteet link of the navigation opens it (lesson.js)."""
    cards = chapter_cards(code, lid, lang)
    if not cards: return ""
    return (f'<details class="opt kc-fold"><summary>{T("cards.lesson_title")}</summary>'
            f'<div class="activity act-concepts kc-section" id="kertaa-kasitteet" data-moduuli="{code}" data-luku="{lid}">'
            f'<p class="kc-intro">{T("cards.lesson_lead")}</p>'
            f'<dl class="kc-dl">{"".join(static_card(c) for c in cards)}</dl>'
            f'<p class="kc-more"><a href="{app_href(code)}">{T("cards.module_all")}</a></p>'
            + data_block(T, lang, cards_of(code, lang), {"luku": lid, "moduuli": code, "chapters": titles}, APP)
            + '<script src="kortit.js"></script></div></details>')


def lesson_nav(T):
    return f'<a href="#kertaa-kasitteet" class="toc-sub toc-concepts"><span class="toc-label">{T("cards.nav")}</span></a>'


def module_section(code, T, lang, titles, svg=""):
    """The module page's "Kertauspakkasi" tile (teacher 2026-11-03; a tile since 2026-11-10), or "" when the module has
    no cards in this language. It links to the module's cards; kortit.js turns its count into the deck's and its link
    into "?pakka=oma" when the student has marked cards to review."""
    cards = cards_of(code, lang)
    if not cards: return ""
    import cardgrid
    slim = [{"id": c["id"], "luku": c["luku"]} for c in cards]
    tile = cardgrid.card(T.count("cards.tile_cards", len(cards)), T("cards.deck_title"), app_href(code), svg=svg,
                         cls=" me-tile kc-deck", attrs=f' data-moduuli="{code}"')
    return tile[:-len("</li>")] + data_block(T, lang, slim, {"moduuli": code, "chapters": titles}, APP) + '<script src="kortit.js"></script></li>'


def practice_section(code, T, lang):
    """Sovella itsenäisesti: the deck's cards of the module above the tasks; hidden until kortit.js finds some."""
    cards = cards_of(code, lang)
    if not cards: return ""
    return (f'<section class="kc-practice" data-moduuli="{code}" hidden aria-labelledby="h-kc-practice"><h2 id="h-kc-practice">{T("cards.practice_title")}</h2>'
            f'<p class="kc-intro">{T("cards.practice_lead")}</p><div class="kc-row"></div>'
            + data_block(T, lang, cards, {"moduuli": code}, APP) + '<script src="kortit.js"></script></section>')


def app_page_body(T, lang, names, chapters):
    """site/kasitteet.html: the app's screens (kortit.js) and, for a reader without JavaScript, every card as a list."""
    dl = data_lang(lang)
    files = {c: (f"kortit/{c.lower()}.json" if dl == "fi" else f"kortit/en/{c.lower()}.json") for c in modules(dl)}
    static = ""
    for c in modules(dl):
        m = module(c, dl)
        if m.get("kesken"): continue
        # each module a closed box (teacher 2026-11-04, UI fix 5): the list without JavaScript stays short on a phone
        static += f'<details class="kc-static-module"><summary><h2>{c} · {esc(m["nimi"])}</h2></summary>'
        for a in m["aiheet"]:
            cs = [k for k in m["kortit"] if k["aihe"] == a["id"]]
            if cs: static += f'<h3>{esc(a["nimi"])}</h3><dl class="kc-dl">{"".join(static_card(k) for k in cs)}</dl>'
        static += "</details>"
    return (f'<header class="kc-app-head"><h1>{T("cards.app_title")}</h1><p class="lead">{T("cards.app_lead")}</p></header>'
            f'<div class="kc-app" data-files=\'{esc(json.dumps(files))}\' hidden></div>'
            f'<div class="kc-static">{static}</div>'
            + data_block(T, lang, [], {"names": names, "chapters": chapters}, APP) + '<script src="kortit.js"></script>')


def publish(site):
    """The data files into site/kortit/ (and their pictures), as the pages and Käsitetakomo read them."""
    out = site / "kortit"
    for f in sorted(SRC.rglob("*")):
        if f.is_file() and f.suffix in (".json", ".svg", ".png", ".webp"):
            (out / f.relative_to(SRC)).parent.mkdir(parents=True, exist_ok=True); shutil.copy(f, out / f.relative_to(SRC))
    return [str((pathlib.Path("kortit") / f.relative_to(SRC))) for f in sorted(SRC.rglob("*.json"))]


def errors():
    """Every problem in the card files: [] when all is well."""
    import courses
    errs, seen = [], {}
    for dl in ("fi", "en"):
        for f in sorted((SRC if dl == "fi" else SRC / dl).glob("*.json")):
            name = f"kortit/{'' if dl == 'fi' else dl + '/'}{f.name}"
            try: m = json.loads(f.read_text(encoding="utf-8"))
            except ValueError as e: errs.append(f"{name}: not JSON ({e})"); continue
            code = m.get("moduuli")
            if code not in courses.codes() or f.stem != str(code).lower(): errs.append(f"{name}: moduuli {code!r} is not a module named by the file"); continue
            slots = [l["id"] for l in courses.curriculum()[code].get("lessons", [])]
            topics = {a["id"] for a in m.get("aiheet", [])}
            for a in m.get("aiheet", []):
                if not ID.fullmatch(a.get("id", "")): errs.append(f"{name}: topic id {a.get('id')!r} is not lowercase-with-hyphens")
            for i, c in enumerate(m.get("kortit", [])):
                p = f"{name} card {c.get('id', i)}"
                miss = [k for k in FIELDS if k not in c]
                if miss: errs.append(f"{p}: missing {', '.join(miss)}"); continue
                if set(c) - set(FIELDS) - set(OPTIONAL): errs.append(f"{p}: unknown fields {sorted(set(c) - set(FIELDS) - set(OPTIONAL))}")
                if not ID.fullmatch(c["id"]) or not c["id"].startswith(code.lower() + "-"): errs.append(f"{p}: id must be lowercase-with-hyphens and start with {code.lower()}-")
                if (dl, c["id"]) in seen: errs.append(f"{p}: id used twice")
                seen[(dl, c["id"])] = 1
                if c["moduuli"] != code: errs.append(f"{p}: moduuli {c['moduuli']} in {code}'s file")
                if c["luku"] is not None and c["luku"] not in slots: errs.append(f"{p}: luku {c['luku']!r} is not a chapter of {code} (curriculum.json)")
                if c["aihe"] not in topics: errs.append(f"{p}: aihe {c['aihe']!r} is not a topic of the file")
                if not c["kasite"].strip() or not c["maaritelma"].strip(): errs.append(f"{p}: empty kasite or maaritelma")
                for k in ("kasite", "maaritelma"):
                    if c[k].count("$") % 2: errs.append(f"{p}: unbalanced $ in {k}")
                    if not m.get("kesken") and UNICODE_MATH.search(re.sub(r"\$[^$]*\$", "", c[k])):
                        errs.append(f"{p}: maths in Unicode in {k}; write it in LaTeX ($...$ or kaava): {c[k]!r}")
                if "kaava" in c and ("$" in c["kaava"] or not c["kaava"].strip()): errs.append(f"{p}: kaava is display LaTeX without $")
                if c.get("kaava") and not c.get("kaava_puhe"): errs.append(f"{p}: kaava without kaava_puhe")
                if c.get("kuva") and not (ROOT / c["kuva"].replace("kortit/", "kortit/", 1)).is_file(): errs.append(f"{p}: picture {c['kuva']} not found")
                if "\\vec" in c.get("kaava", "") + c["maaritelma"] or "\\mathbf" in c.get("kaava", "") + c["maaritelma"]: errs.append(f"{p}: vectors are \\overline (teacher 2026-10-29)")
                if re.search(r"\\[,;:!]\^", c.get("kaava", "") + c["maaritelma"]): errs.append(f"{p}: a superscript needs a base after a space, write \\,{{}}^\\circ (KaTeX cannot parse \\,^)")
    for f in sorted((SRC / "en").glob("*.json")) if (SRC / "en").is_dir() else []:
        fi = module(f.stem.upper(), "fi")
        en = json.loads(f.read_text(encoding="utf-8"))
        if not fi: errs.append(f"kortit/en/{f.name}: no Finnish file"); continue
        a, b = {c["id"]: c for c in fi["kortit"]}, {c["id"]: c for c in en["kortit"]}
        for cid in b:
            if cid not in a: errs.append(f"kortit/en/{f.name}: card {cid} is not in the Finnish file")
            elif (a[cid]["luku"], a[cid]["aihe"]) != (b[cid]["luku"], b[cid]["aihe"]): errs.append(f"kortit/en/{f.name}: card {cid} has another luku or aihe than in Finnish")
    return errs


def stats():
    import courses
    for code in modules():
        cs = cards_of(code, "fi")
        by = {}
        for c in cs: by.setdefault(c["luku"], []).append(c["kasite"])
        print(f"{code}: {len(cs)} cards, {sum(1 for c in cs if c['luku'])} in chapters; en: {len(cards_of(code, 'en'))}")
        for lid in [l["id"] for l in courses.curriculum()[code]["lessons"]] + [None]:
            if lid in by: print(f"  {lid}: {', '.join(by[lid])}")


if __name__ == "__main__":
    if sys.argv[1:] == ["check"]:
        errs = errors()
        print("\n".join(errs) or f"concept cards: {sum(len(cards_of(c, 'fi')) for c in modules())} cards in {len(modules())} modules, "
              f"{sum(len(cards_of(c, 'en')) for c in modules('en'))} in English")
        sys.exit(1 if errs else 0)
    if sys.argv[1:] == ["stats"]: stats(); sys.exit(0)
    sys.exit(__doc__)
