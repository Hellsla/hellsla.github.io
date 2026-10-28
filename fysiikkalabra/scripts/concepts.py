"""Cross-chapter consistency of recurring physics concepts (docs/physics-guardrails.md, teacher 2026-10-28).

  python scripts/concepts.py list                        the concepts and how many passages each has, per chapter
  python scripts/concepts.py packet <concept> [--lang fi]  review-concepts/<concept>.md: every passage about it
  python scripts/concepts.py changed [<ref>]             the concepts a change since <ref> (default origin/main) touches

Lessons are reviewed one by one, so two chapters can explain one idea in contradicting ways. A concept is a short list
of Finnish word stems; a passage is a sentence of a lesson, an exercise set, an exit ticket or a Sovella task that
contains one, with its chapter title, file and place (a wrong option is marked as a distractor). The packet carries
only those sentences and the concept's guardrail section, no figures or whole pages, so one science reviewer compares a
concept across FY1–FY3 in one small run (prompt: `Read review-concepts/packet-<concept>.md and follow it.`) and
reports contradictions as `file — passage — fix`. `changed` names the concepts whose passages a pull request edits, so a
concept-wide correction is reviewed once, not lesson by lesson. Nothing here is maintained by hand but the stems."""
import json, pathlib, re, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import physics_phrases as P

ROOT = P.ROOT
OUT = ROOT / "review-concepts"

# concept: (guardrail section heading, stems); a stem matches a word's start, case-insensitively
CONCEPTS = {
    "uncertainty": ("Measurement and data", ["epävarmuu", "virhearvi", "virhe-arvi", "mittausvirhe", "satunnaisvirhe", "systemaattinen virhe",
                                             "karkea virhe", "vaihteluväli", "hajont", "resoluutio", "asteikkoväli", "poikkeav"]),
    "fit": ("Measurement and data", ["sovit", "kulmakerroi", "ääriviiv", "jyrkin", "loivin", "ekstrapol", "origon kautta", "pisteiden kautta",
                                     "pisteet eivät"]),
    "internal-energy": ("Energy, heat and efficiency", ["sisäenergi", "lämpöenergi", "lämpönä", "lämpö siirtyy", "kitka", "lämmöksi"]),
    "temperature": ("Particles, temperature and changes of state", ["keskimääräi\\w* liike-energi", "lämpötila kertoo", "lämpötila kuvaa",
                                                                    "absoluuttise\\w* nollapistee", "hiukkasten liike", "värähtel"]),
    "phase-change": ("Particles, temperature and changes of state", ["sulami", "sulaa", "höyrysty", "kiehu", "jäätym", "tiivisty", "sidos",
                                                                     "vuorovaikutusenergi", "olomuodon muutos", "ominaissulamis", "ominaishöyrysty"]),
    "efficiency": ("Energy, heat and efficiency", ["hyötysuhte", "lämpökerroi", "lämpövoimako", "yhteistuotan", "carnot", "hukkalämp"]),
    "heat-transfer": ("Energy, heat and efficiency", ["johtumi", "kulkeutumi", "lämpösäteil", "säteilee", "säteily", "nettomää", "lämpimämmä"]),
    "gas": ("State a law's conditions where it is used", ["ideaalikaasu", "boylen", "kaasun paine", "tilanyhtäl", "harva\\w* kaasu", "nesteyty"]),
    "fuel": ("Energy, heat and efficiency", ["lämpöarvo", "ravintoarvo", "ravinno\\w* energi", "hiilidioksid", "palami", "polttoaine"]),
}


def pattern(concept):
    return re.compile(r"\b(?:" + "|".join(CONCEPTS[concept][1]) + ")", re.I)


def title(folder):
    m = folder / "meta.json"
    if m.exists(): return json.loads(m.read_text()).get("title", folder.name)
    return f"{folder.parent.name} Sovella itsenäisesti"


def where(path):
    """Readable places of a JSON file's strings: activity id and field, so a reviewer can find the sentence."""
    def walk(o, place, wrong=False):
        if isinstance(o, str): yield place, o, wrong
        elif isinstance(o, dict):
            here = o.get("id", place) if isinstance(o.get("id"), str) else place
            distractor = "text" in o and "feedback" in o and not o.get("correct")
            for k, v in o.items(): yield from walk(v, f"{here}.{k}", wrong or (distractor and k == "text"))
        elif isinstance(o, list):
            for i, v in enumerate(o): yield from walk(v, f"{place}[{i}]", wrong)
    return walk(json.loads(path.read_text()), path.name)


def passages(concept, lang="fi"):
    """(chapter, file, place, sentence, distractor) of every sentence about a concept."""
    pat, out = pattern(concept), []
    for folder in sorted(p for p in (ROOT / "content" / lang).glob("*/*") if p.is_dir()):
        for n in P.FILES:
            f = folder / n
            if not f.exists(): continue
            rel = str(f.relative_to(ROOT))
            if n.endswith(".json"):
                for place, text, wrong in where(f):
                    for _, s in P.sentences(text):
                        if pat.search(s): out.append((title(folder), rel, place, " ".join(s.split()), wrong))
            else:
                for line, s in P.sentences(f.read_text()):
                    if pat.search(s) and not s.lstrip().startswith(("<", "|")): out.append((title(folder), rel, f"line {line}", " ".join(s.split()), False))
    return out


def guardrail(heading):
    text = (ROOT / "docs/physics-guardrails.md").read_text()
    m = re.search(rf"^## {re.escape(heading)}.*?(?=^## |\Z)", text, re.M | re.S)
    return m.group(0).strip() if m else ""


def packet(concept, lang="fi"):
    rows = passages(concept, lang)
    OUT.mkdir(exist_ok=True)
    body = [f"# Concept review: {concept} ({lang})\n",
            "You are the science reviewer (`.claude/agents/science-reviewer.md`) for ONE concept across all chapters. Below are "
            "every sentence of the course material that mentions it, grouped by chapter, and the guardrail that applies. Find "
            "**contradictions between chapters** (one chapter says what another denies), claims that break the guardrail, and "
            "conditions stated in one place but dropped in another. A sentence marked *distractor* is a wrong option on purpose: "
            "judge only that its feedback (listed separately) is right. Do not judge style. Open a source file only when a "
            "sentence cannot be judged without its context.\n",
            "Write `review-concepts/report-" + concept + ".md`: `## Contradictions` and `## Guardrail breaks`, each item "
            "`file (place) — passage — fix (exact Finnish)`, at most 15 items, then `## Consistent` (one line per chapter "
            "checked). Under 500 words.\n", "## Guardrail\n", guardrail(CONCEPTS[concept][0]), "\n## Passages\n"]
    chap = None
    for t, f, place, s, wrong in rows:
        if t != chap: body.append(f"\n### {t}\n"); chap = t
        body.append(f"- `{f}` ({place}){' *distractor*' if wrong else ''}: {s}")
    path = OUT / f"packet-{concept}.md"
    path.write_text("\n".join(body) + "\n")
    return path, len(rows)


def changed(ref="origin/main"):
    diff = subprocess.run(["git", "diff", "-U0", ref, "--", "content/fi", ":(exclude,glob)**/review/**"], cwd=ROOT, capture_output=True, text=True).stdout
    lines = [l[1:] for l in diff.splitlines() if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    return {c: n for c in CONCEPTS if (n := sum(1 for l in lines if pattern(c).search(l)))}


if __name__ == "__main__":
    a = sys.argv[1:]
    lang = a[a.index("--lang") + 1] if "--lang" in a else "fi"
    if a[:1] == ["list"]:
        for c in CONCEPTS:
            rows = passages(c, lang); per = {}
            for r in rows: per[r[0]] = per.get(r[0], 0) + 1
            print(f"{c}: {len(rows)} passages in {len(per)} chapters")
    elif a[:1] == ["packet"] and len(a) >= 2 and a[1] in CONCEPTS:
        path, n = packet(a[1], lang)
        print(f"{path.relative_to(ROOT)}: {n} passages, {len(path.read_text()) // 1000} kB")
    elif a[:1] == ["changed"]:
        for c, n in changed(a[1] if len(a) > 1 and not a[1].startswith("--") else "origin/main").items():
            print(f"{c}: {n} changed line(s) -> python scripts/concepts.py packet {c}")
    else: sys.exit(__doc__ + "\nconcepts: " + ", ".join(CONCEPTS))
