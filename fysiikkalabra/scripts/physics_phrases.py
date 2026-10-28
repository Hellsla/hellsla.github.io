"""High-precision warnings for physics claims the FY1–FY3 accuracy audit found taught as fact (docs/physics-guardrails.md).

  python scripts/physics_phrases.py [<folder or file> ...]   warn about the sentences that state one (default: every
                                                             Finnish lesson, exercise set and Sovella itsenäisesti)

A rule is a claim pattern plus the words that make the sentence right (a qualifier): "puoli asteikkoväliä" is right in
"lukeman epävarmuutta voidaan arvioida puoleksi asteikkovälistä", wrong as "virhearvio on puoli asteikkoväliä". A match
is a warning for the science reviewer, never proof: the sentence is printed so a human sees it in context. What is not
taught as fact is skipped: a wrong multiple-choice option (a choice without "correct": true), the misconception a
sentence names in order to refute it ("virhekäsitys", "luulee", "ei pidä paikkaansa", "väärin", a quotation), and
a claim inside a stated model ("ideaalikaasun mallissa"). lint_lesson.py prints them as warnings for each lesson;
test_physics_phrases.py (CI) proves every rule on right and wrong example sentences and that no current Finnish text
states a known wrong claim, so a corrected error cannot come back unnoticed."""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
I = re.I

# (id, claim pattern, qualifier that makes the sentence right or None, message)
RULES = [
    ("scale-half", re.compile(r"(?:virhe-?arvio|epävarmuus|virhe)\w* (?:on|ei voi olla)\b[^.;]{0,40}\b(?:puoli|puolet|puolikas)\w* (?:pienimmästä |pienintä )?asteikkov", I),
     re.compile(r"lukem\w* epävarmuu|yksinkertai|esimerki|arvioi(?:da|daan)? (?:esimerkiksi )?puolek", I),
     "half the smallest division estimates the READING uncertainty in a simple case, not the measurement's uncertainty"),
    ("scale-max", re.compile(r"ei voi olla (?:yhtä )?(?:asteikkoväliä|asteikkovälin|puolta asteikkoväliä) (?:suurempi|isompi)", I), None,
     "an uncertainty can exceed a scale division (reaction time, parallax, an unclear edge)"),
    ("uncertainty-max", re.compile(r"(?:mittaus)?epävarmuus\w* (?:kertoo|ilmoittaa|on)[^.;]{0,50}\b(?:enintään|korkeintaan|suurimma\w*) (?:poike|virhe|mahdolli)", I),
     re.compile(r"ei (?:yleensä )?tarkoita|valmista\w* ilmoitta|virheraj", I),
     "a measurement uncertainty is an estimate, not a guaranteed maximum deviation (an instrument's stated error limit is a different thing)"),
    ("never-on-line", re.compile(r"\b(?:eivät|ei) (?:koskaan|ikinä) (?:osu|ole|kulje|sijaitse)[^.;]{0,40}\bsuora", I), None,
     "points scatter around a fitted line, but nothing forbids one lying exactly on it: 'yleensä'"),
    ("outlier-drop", re.compile(r"poikkea\w*[^.;]{0,90}\b(?:jätetään pois|jättää (?:sen )?pois|poistetaan|hylätään)", I),
     re.compile(r"\bsyy|perustel|vain jos|vain,? jos|ei poisteta|ei saa|pelkästään|kirja|dokumentoi|ei pidä", I),
     "a deviant result is checked and the measurement repeated if needed; it is dropped only for a found, documented cause"),
    ("half-range-mean", re.compile(r"keskiarvon (?:epävarmuus|virhe)\w*[^.;]{0,60}(?:vaihteluvälin puol|puolet vaihteluvälistä|puolikas)|(?:vaihteluvälin puol\w*|puolet vaihteluvälistä)[^.;]{0,60}keskiarvon (?:epävarmuus|virhe)", I),
     re.compile(r"yksinkertai|arvio|likim|tässä (?:tehtävässä|harjoituksessa|kurssissa)", I),
     "half the range is a simple estimate of the scatter adopted for the exercise, not the uncertainty of the mean"),
    ("efficiency-below-100", re.compile(r"hyötysuhde\w* (?:on |jää )?(?:aina|kaikissa laitteissa|jokaisessa laitteessa) (?:alle|pienempi kuin) \$?100", I),
     re.compile(r"lämpövoimako|kiertoprosess|lämpökonee", I),
     "efficiency is at most 100 %; it is often below 100 % in real devices (a cyclic heat engine always below)"),
    ("phase-bonds", re.compile(r"(?:kemialli\w*|molekyyli\w*n sisäi\w*|molekyylien) sido\w* (?:katkea|purka|purkautu|hajoa|rikkou)|(?:sulamise|höyrystymise|kiehumise)\w*[^.;]{0,40}\bsido\w* (?:katkea|purka|purkautu|hajoa)", I),
     re.compile(r"välis|keskinäi|vety\w*sido|ei katkea|eivät katkea|ei hajoa|eivät hajoa|pysyvät ehj", I),
     "melting and boiling change the interactions BETWEEN molecules; the chemical bonds inside a molecule do not break"),
    ("phase-energy", re.compile(r"\bolomuodon muutos (?:vaatii|tarvitsee) (?:aina )?energiaa", I), None,
     "freezing and condensation release energy; say which changes need energy"),
    ("heat-stored", re.compile(r"\b(?:kappale\w*|aine\w*|vede\w*|vesi|kivi\w*)\b[^.;]{0,30}\b(?:sisältää|varastoi|on varastoitunut\w*) (?:paljon |enemmän |vähemmän )?lämpö(?:ä|energiaa)\b|lämpö(?:ä)? varastoituu", I),
     re.compile(r"sisäenergi", I),
     "heat is energy in transfer; what a body has is internal energy"),
    ("friction-creates", re.compile(r"kitka\w* (?:synnyttää|tuottaa|luo|valmistaa) (?:uutta )?(?:energiaa|lämpöenergiaa)", I),
     re.compile(r"muunta|muuttu|sisäenergia", I),
     "friction converts mechanical energy into internal energy; it creates no energy"),
    ("all-fuels-co2", re.compile(r"(?:kaikki(?:en)?|jokai\w*) polttoaine\w*[^.;]{0,60}(?:hiilidioksid|CO_?\{?2|CO₂)", I),
     re.compile(r"hiiltä sisältäv|fossiili|vety|paitsi", I),
     "only carbon-containing fuels give CO₂ when their carbon burns (hydrogen gives water)"),
    ("absolute-zero-stop", re.compile(r"(?:absoluuttise\w* nollapistee\w*|0\\?,?\s?\\?,?\\text\{K\}|nollassa kelvinissä)[^.;]{0,80}(?:liike|hiukkas\w*|värähtel\w*)[^.;]{0,40}(?:pysähty|lakka|loppu|seis)", I),
     re.compile(r"lähes|ei kokonaan|ei täysin|vähimmä|kvantti|pienimmill|\bei (?:kokonaan )?(?:lakkaa|pysähdy|lopu)", I),
     "at absolute zero the particles' energy is at its minimum, not all motion stops"),
    ("heat-direction", re.compile(r"lämpö\w* (?:siirtyy|virtaa|kulkee) aina lämpimämmä\w*[^.;]{0,40}kylmempä", I),
     re.compile(r"netto|säteil\w*[^.;]*molem|itsestään|johtu|kulje\w*", I),
     "net transfer is from warm to cold; radiation leaves both bodies (say 'nettomääräisesti' or name conduction)"),
    ("dive-exhale", re.compile(r"hengitettävä (?:koko (?:ajan|nousun ajan) )?ulos|on puhallettava (?:koko ajan )?ulos|puhalla\w* (?:koko ajan )?ulos (?:noust|koko nousun)", I), None,
     "the diving rule is: never hold your breath while ascending, breathe normally"),
]

# a sentence that names a claim in order to refute it, or a stated model's claim, is not a claim taught as fact
REFUTES = re.compile(r"virhekäsity|luule|luullaan|ajattele\w* (?:usein|helposti)|ei pidä paikkaansa|ei ole totta|\bväärin\b|virheellinen väite|«|»|“|”", I)


def sentences(text):
    """The sentences of a text with the line each starts on; inline SVG is blanked (its labels are LaTeX symbols)."""
    text = re.sub(r"<svg\b.*?</svg>", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    line, out = 1, []
    for part in re.split(r"(?<=[.!?])\s+|\n\s*\n", text):
        out.append((line, part)); line += part.count("\n") + 1
    return out


def taught(obj, wrong=False):
    """(text, is_taught) for every string of a JSON file: a wrong option's own text is a distractor, not teaching."""
    if isinstance(obj, str): yield obj, not wrong
    elif isinstance(obj, dict):
        distractor = "text" in obj and "feedback" in obj and not obj.get("correct")
        for k, v in obj.items(): yield from taught(v, wrong or (distractor and k == "text"))
    elif isinstance(obj, list):
        for v in obj: yield from taught(v, wrong)


def problems_in(name, text):
    """(file, line, rule id, message, sentence) for every flagged sentence of one file's text."""
    if name.endswith(".json"):
        try: units = [(1, s) for t, ok in taught(json.loads(text)) if ok for _, s in sentences(t)]
        except json.JSONDecodeError: units = sentences(text)
    else: units = sentences(text)
    out = []
    for line, s in units:
        if REFUTES.search(s): continue
        for rid, pat, ok, msg in RULES:
            if pat.search(s) and not (ok and ok.search(s)):
                out.append((name, line, rid, msg, " ".join(s.split())[:160]))
    return out


FILES = ("lesson.md", "inquiry.json", "exit-ticket.json", "exercises/exercises.json", "exercises/solutions.md",
         "tasks.json", "solutions.md")


def problems(folder):
    folder = pathlib.Path(folder); out = []
    for n in FILES:
        p = folder / n
        if p.exists(): out += problems_in(n, p.read_text())
    return out


def finnish_units():
    return sorted(p for p in (ROOT / "content/fi").glob("*/*") if p.is_dir())


if __name__ == "__main__":
    paths = [pathlib.Path(a).resolve() for a in sys.argv[1:]] or finnish_units()
    n = 0
    for p in paths:
        for f, line, rid, msg, s in (problems(p) if p.is_dir() else problems_in(p.name, p.read_text())):
            n += 1; print(f"WARN  {p.relative_to(ROOT) if p.is_relative_to(ROOT) else p}/{f}:{line} [{rid}] {msg}\n      «{s}»")
    print(f"{n} sentence(s) to check (docs/physics-guardrails.md)")
    sys.exit(1 if n else 0)
