"""Grammar of a lesson's learning goals (`learn` in inquiry.json), which the page shows as the end of one sentence:
"Tällä tunnilla opit | laskemaan …" and "In this lesson, you will learn to | calculate …" (teacher 2026-10-29).

So a Finnish (fi, fi-easy) goal starts with a lowercase verb in the third infinitive illative (-maan/-mään), and a
skill joined with "ja", "sekä" or "tai" takes the same form ("laskemaan … ja selittämään …"); an English goal starts
with a lowercase bare verb ("calculate …", "explain …"). A short second sentence may follow in Selkeä suomi.
Module goals ("Opiskelija osaa …"), Pohjatiedot and rubrics have their own grammar and are never checked here.

`check(goals, lang)` returns (errors, warnings): an error is a form that is certainly wrong under the heading
("Osaat laskea …", "You can …", a capital letter, a first word that is no -maan/-mään verb); a warning is a likely
break of the parallel form that a person should look at. No grammar parser: a small list of common verbs.

  python scripts/objectives.py            every lesson's goals in every language"""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

FINNISH = ("fi", "fi-easy")
# second-person or other finite forms that cannot follow "Tällä tunnilla opit"
FI_FINITE = re.compile(r"\b(?:sinä|osaat|opit|osaa|tunnistat|erotat|tiedät|ymmärrät|tutkit|tulkitset|selität|lasket|"
                       r"vertailet|arvioit|perustelet|sovellat|käytät|määrität|luet|päättelet|kuvaat|muunnat|ratkaiset)\b", re.I)
# a first-infinitive verb after a conjunction ("laskemaan … ja selittää …") breaks the parallel -maan/-mään form
FI_FIRST_INF = re.compile(r"\b(?:ja|sekä|tai)\s+(?:laskea|selittää|vertailla|tunnistaa|arvioida|perustella|soveltaa|tutkia|"
                          r"erottaa|lukea|päätellä|määrittää|kertoa|liittää|käyttää|tulkita|valita|kuvata|ilmoittaa|"
                          r"muuntaa|ratkaista|esittää|sovittaa|nimetä|kirjoittaa|korjata|raportoida|todentaa)\b", re.I)
EN_BAD_START = re.compile(r"^(?:you\b|i\b|to\b|can\b|be able\b|learn\b|students?\b)", re.I)
EN_BREAK = re.compile(r"\b(?:and|or)\s+(?:you\s+)?can\b|\band\s+to\s+[a-z]", re.I)


def first_sentence(text):
    """The text up to the first full stop that ends a sentence (not one inside $…$)."""
    plain = re.sub(r"\$[^$]*\$", lambda m: "x" * len(m.group(0)), text)
    m = re.search(r"[.!?](?:\s|$)", plain)
    return text[:m.start()] if m else text


def check(goals, lang):
    errs, warns = [], []
    for i, g in enumerate(goals or []):
        if not isinstance(g, str) or not g.strip(): continue
        s = g.strip(); first = re.match(r"[^\s,:;]+", s).group(0)
        if s[0].isupper(): errs.append(f"learn[{i}]: starts with a capital: the goal completes the heading's sentence, so it starts in lowercase (\"{first.lower()} …\")")
        if lang in FINNISH:
            head = first_sentence(s)
            if FI_FINITE.match(s): errs.append(f"learn[{i}]: \"{first} …\" does not follow \"Tällä tunnilla opit\"; write the verb as -maan/-mään (\"laskemaan …\", \"selittämään …\")")
            elif not re.fullmatch(r"[a-zåäö-]+m[aä]{2}n", first.lower()): errs.append(f"learn[{i}]: the first word \"{first}\" is no -maan/-mään verb; \"Tällä tunnilla opit\" continues with one (\"laskemaan …\")")
            else:
                if FI_FINITE.search(head): warns.append(f"learn[{i}]: a finite verb (\"{FI_FINITE.search(head).group(0)}\") inside the goal; keep the skills parallel (\"laskemaan … ja selittämään …\")")
                later = s[len(head):]
                if re.search(r"(?:^|[.!?]\s+)(?:Opit|Osaat|Sinä)\b", later): warns.append(f"learn[{i}]: a later sentence starts \"Opit …\"/\"Osaat …\" and repeats the heading; join the skills in one clause (\"… ja selittämään …\")")
                if FI_FIRST_INF.search(head): warns.append(f"learn[{i}]: \"{FI_FIRST_INF.search(head).group(0)}\" breaks the parallel form; write -maan/-mään (\"… ja selittämään …\")")
        elif lang == "en":
            if EN_BAD_START.match(s): errs.append(f"learn[{i}]: \"{first} …\" does not follow \"In this lesson, you will learn to\"; start with the verb (\"calculate …\", \"explain …\")")
            elif re.match(r"[A-Za-z]+s\b", first) and first.lower() not in ("discuss", "assess", "express", "process", "access", "address", "focus", "analyse", "analyze", "use", "compare"):
                warns.append(f"learn[{i}]: \"{first}\" looks like a third-person verb; the goal continues \"you will learn to …\" with a bare verb")
            if EN_BREAK.search(s): warns.append(f"learn[{i}]: \"{EN_BREAK.search(s).group(0)}\" breaks the parallel form; join bare verbs (\"calculate … and explain …\")")
    return errs, warns


if __name__ == "__main__":
    import courses
    bad = 0
    for lang in sorted(p.name for p in (courses.ROOT / "content").iterdir() if p.is_dir() and not p.name.startswith("_")):
        for f in sorted((courses.ROOT / "content" / lang).glob("*/*/inquiry.json")):
            e, w = check(json.loads(f.read_text()).get("learn"), lang)
            for m in e: print(f"ERROR {f.relative_to(courses.ROOT)}: {m}"); bad += 1
            for m in w: print(f"WARNING {f.relative_to(courses.ROOT)}: {m}")
    print(f"{bad} error(s)"); sys.exit(1 if bad else 0)
