"""A course unit's translation through the pipeline (teacher 2026-11-04, FY9 in en and fi-easy; scripts/units.py).
Usage: python scripts/test_unit_i18n.py

In a temporary copy of the project, fy9-koe's en version is removed and made again with translate_kit.py (extract,
then apply with the Finnish texts as the "translation"); then the language check, the unit check, the build (an
unreviewed translation is not published, the course pages link the Finnish unit), the hash of its own, and the
build with stand-in PASS reports and FY9 in content/en/local-courses.json: the page at site/en/fy9-koe.html, the
language links between the versions, the course page and the YO-sekoitin. FY14's units build as the committed site.
The real project is not touched."""
import hashlib, json, os, pathlib, re, shutil, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent
UNIT = "fy9-koe"
failures = []


def expect(name, cond, detail=""):
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"  -> {str(detail)[:600]}"))
    if not cond: failures.append(name)


def snapshot():
    files = [SRC / "local-courses.json"] + sorted((SRC / "content").rglob("*")) + sorted((SRC / "lessons").rglob("*")) + sorted((SRC / "site").glob("*.html"))
    return hashlib.sha256(b"".join(p.as_posix().encode() + p.read_bytes() for p in files if p.is_file() and "/review/" not in p.as_posix())).hexdigest()
REAL = snapshot()

T = pathlib.Path(tempfile.mkdtemp(prefix="fysiikkalabra-unit-i18n-"))
for f in ("curriculum.json", "competencies.json", "glossary.json", "local-courses.json", "CLAUDE.md", "NOTES.md"): shutil.copy(SRC / f, T / f)
for d in ("scripts", "templates", "content", "lessons", "lang", "assets", "tests", "kortit", "tips", "news"):
    if (SRC / d).is_dir(): shutil.copytree(SRC / d, T / d, ignore=shutil.ignore_patterns("__pycache__", "packet-*", "shots*"))
(T / "docs").mkdir(exist_ok=True); shutil.copy(SRC / "docs/visual-baseline.tsv", T / "docs")
# The copy starts from the state before FY9 was translated: only this unit has an en version, and FY9 is not yet in
# content/en/local-courses.json (the test adds it); the fi-easy versions wait for their course the same way.
for lang in ("en", "fi-easy"):
    for u in (T / "content" / lang / "units").glob("fy9-*"):
        if lang == "en" and u.name != UNIT: shutil.rmtree(u)
    lcp = T / "content" / lang / "local-courses.json"
    if lcp.is_file():
        lc0 = json.loads(lcp.read_text()); lc0.pop("FY9", None); lcp.write_text(json.dumps(lc0, ensure_ascii=False, indent=2))
ENV = {**os.environ, "FYSIIKKALABRA_ROOT": str(T)}
EN = T / "content/en/units" / UNIT; KIT = T / "kit"


def run(script, *args):
    r = subprocess.run([sys.executable, str(T / "scripts" / script), *map(str, args)], capture_output=True, text=True, cwd=T, env=ENV, timeout=1800)
    return r.returncode, r.stdout + r.stderr


fi_hash = run("units.py", "hash", UNIT)[1].strip()
code, out = run("translate_kit.py", "extract", UNIT, "en", KIT)   # from the committed translation, then made again from the kit alone
k = KIT / "en" / UNIT
expect("extract writes the unit's kit", code == 0 and all((k / n).is_file() for n in ("strings.json", "figures.json", "unit.md", "teacher.md", "sovella/solutions.md"))
       and not (k / "key_concepts.json").exists() and "Given" in (k / "sovella/solutions.md").read_text(), out)
code, out = run("translate_kit.py", "extract", UNIT, "fi-easy", KIT)
expect("an S2 kit has key_concepts.json", code == 0 and json.loads((KIT / "fi-easy" / UNIT / "key_concepts.json").read_text())["key_concepts"], out)
shutil.rmtree(EN)
code, out = run("translate_kit.py", "apply", UNIT, "en", KIT)
expect("apply writes content/en/units/ and its checks pass", code == 0 and "checks pass" in out and (EN / "unit.json").is_file() and (EN / "sovella/tasks.json").is_file(), out[-600:])
expect("the en figures use a decimal point", "{,}" not in "".join(re.findall(r"<svg\b.*?</svg>", (EN / "unit.md").read_text(), re.S)))
code, out = run("check_i18n.py")
expect("check_i18n checks the unit translation", code == 0 and "en: 0 error(s)" in out and UNIT not in out.split("en: not translated yet")[-1].split("\n")[0], out[-800:])
code, out = run("units.py", "check")
expect("units.py check accepts a translation language of the course", code == 0, out[-600:])
tj = json.loads((EN / "inquiry.json").read_text()); a = next(x for x in tj["activities"] if "answer" in x and isinstance(x["answer"], (int, float)))
a["answer"] += 1; (EN / "inquiry.json").write_text(json.dumps(tj, ensure_ascii=False))
code, out = run("check_i18n.py")
expect("a translation that changes an answer is an error", code == 1 and "inquiry.json" in out, out[-600:])
a["answer"] -= 1; (EN / "inquiry.json").write_text(json.dumps(tj, ensure_ascii=False))

sys.path.insert(0, str(T / "scripts")); os.environ["FYSIIKKALABRA_ROOT"] = str(T)
import units
h_en = units.content_hash(UNIT, "en")
expect("the translation has a hash of its own; the source's is unchanged", h_en and h_en != fi_hash and run("units.py", "hash", UNIT)[1].strip() == fi_hash, (h_en, fi_hash))
code, out = run("build.py")
expect("an unreviewed translation is not published", code == 0 and not (T / f"site/en/{UNIT}.html").exists() and f'href="en/{UNIT}.html"' not in (T / f"site/{UNIT}.html").read_text(), out[-600:])   # the language menu may link the en course page's note
fy14 = [u for c in json.loads((SRC / "local-courses.json").read_text())["FY14"]["chapters"] for u in c["units"] if (SRC / f"site/en/{u['id']}.html").is_file()]
expect("FY14's units build as the committed site", fy14 and all((T / f"site/en/{u['id']}.html").read_text() == (SRC / f"site/en/{u['id']}.html").read_text() for u in fy14), [u["id"] for u in fy14])

for role in ("science", "pedagogy", "visual"):
    (EN / "review").mkdir(exist_ok=True); (EN / f"review/{role}.md").write_text(f"VERDICT: PASS\nCONTENT-HASH: {h_en}\n\n## Blocking\nnone\n")
code, out = run("build.py")
expect("a reviewed translation waits for its course in content/en/local-courses.json", code == 0 and not (T / f"site/en/{UNIT}.html").exists() and "waits for FY9" in out, out[-600:])
lc = json.loads((T / "content/en/local-courses.json").read_text())
lc["FY9"] = {"title": "Exam preparation", "subtitle": "Revision.", "school": "Kiviruukki upper secondary school", "description": "A test entry."}
(T / "content/en/local-courses.json").write_text(json.dumps(lc, ensure_ascii=False, indent=2))
code, out = run("build.py")
page = (T / f"site/en/{UNIT}.html").read_text() if (T / f"site/en/{UNIT}.html").exists() else ""
fi_page = (T / f"site/{UNIT}.html").read_text()
expect("a reviewed translation is published at site/en/", code == 0 and '<html lang="en"' in page, out[-600:])
expect("the unit's versions link to each other", f'href="en/{UNIT}.html" hreflang="en"' in fi_page and f'href="../{UNIT}.html" hreflang="fi"' in page
       and 'hreflang="fi-easy"' not in fi_page, re.findall(r'<a class="lang"[^>]*>[^<]*</a>', fi_page + page))
course = (T / "site/en/FY9.html").read_text()
other = next(u["id"] for c in json.loads((T / "local-courses.json").read_text())["FY9"]["chapters"] for u in c["units"] if u["id"] != UNIT and (T / f"site/{u['id']}.html").is_file())
expect("the en course page links the en unit, the Finnish one for a unit not translated, with its note",
       f'href="{UNIT}.html"' in course and f'href="../{other}.html"' in course and f'id="unavailable-{other}"' in course and f'id="unavailable-{UNIT}"' not in course)
mix = T / "site/en/yo-sekoitin.html"
expect("the en YO-sekoitin lists the published unit's tasks only", not mix.exists() or (f"{UNIT}-s1" in mix.read_text() and f"{other}-s1" not in mix.read_text()))

shutil.rmtree(T, ignore_errors=True)
expect("the real project is untouched", snapshot() == REAL)
print("all unit translation tests passed" if not failures else f"{len(failures)} failure(s): {', '.join(failures)}")
sys.exit(1 if failures else 0)
