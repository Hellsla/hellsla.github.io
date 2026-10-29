"""Tests for a second language (README "Languages"). Usage: python scripts/test_i18n.py
Copies the project into a temporary folder, adds a language "en" made only of lang/en.json and content/en/ (one lesson,
its Finnish texts as the "translation"), and checks the language check, the review hash of the translation, the build
into site/en/ and the links between the languages. The real project is not touched."""
import hashlib, json, os, pathlib, re, shutil, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent
LESSON = "fy3-3"
failures = []


def expect(name, cond, detail=""):
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"  -> {str(detail)[:600]}"))
    if not cond: failures.append(name)


def snapshot():
    files = sorted((SRC / "content").rglob("*")) + sorted((SRC / "lessons").rglob("*")) + sorted((SRC / "lang").rglob("*")) + sorted((SRC / "site").rglob("*.html"))
    return hashlib.sha256(b"".join(p.as_posix().encode() + p.read_bytes() for p in files if p.is_file() and "/review/" not in p.as_posix())).hexdigest()
REAL = snapshot()

T = pathlib.Path(tempfile.mkdtemp(prefix="fysiikkalabra-i18n-"))
for f in ("curriculum.json", "competencies.json", "glossary.json", "CLAUDE.md", "NOTES.md"): shutil.copy(SRC / f, T / f)
for d in ("scripts", "templates", "content", "lessons", "lang", "assets", "tests"): shutil.copytree(SRC / d, T / d, ignore=shutil.ignore_patterns("__pycache__", "packet-*", "shots*"))
for p in [*(T / "lang").glob("*.json"), *(T / "content").iterdir()]:     # Finnish only: the test adds its own "en"
    if p.stem not in ("fi", "_gold"): shutil.rmtree(p) if p.is_dir() else p.unlink()
ENV = {**os.environ, "FYSIIKKALABRA_ROOT": str(T)}


def run(script, *args):
    r = subprocess.run([sys.executable, str(T / "scripts" / script), *map(str, args)], capture_output=True, text=True, cwd=T, env=ENV, timeout=900)
    return r.returncode, r.stdout + r.stderr


fi_hash = run("reviews.py", "hash", LESSON)[1].strip()
code, out = run("check_i18n.py")
expect("one language: nothing to compare", code == 0 and "fi only" in out, out)
code, out = run("build.py")
fi_page = (T / "site" / f"{LESSON}.html").read_text()
site_page = re.sub(r'<a class="lang" [^>]*>[^<]*</a>', "", (SRC / "site" / f"{LESSON}.html").read_text())  # the real site has languages
expect("one language: the build is the committed site, without language links", code == 0 and fi_page == site_page and 'class="lang"' not in fi_page, out[-400:])

# a second language: lang/en.json and content/en/, nothing else
en = json.loads((T / "lang/fi.json").read_text())
en["format"].update(html_lang="en", og_locale="en_GB", decimal=".", language_name="English")
en["site"]["name"] = "Physics Lab"; en["lesson"]["check"] = "Check"
(T / "lang/en.json").write_text(json.dumps(en, ensure_ascii=False, indent=2) + "\n")
fi_dir = T / "content/fi/FY3" / LESSON; en_dir = T / "content/en/FY3" / LESSON
shutil.copytree(fi_dir, en_dir, ignore=shutil.ignore_patterns("review"))
code, out = run("check_i18n.py")
expect("a language without courses.json or figure texts is incomplete", code == 1 and "courses.json: no title for FY3" in out and "figures.json has no translation" in out and "not translated yet" in out, out)

cur = json.loads((T / "curriculum.json").read_text())
(T / "content/en/courses.json").write_text(json.dumps({c: {"title": m["title"] + " (en)", "tavoitteet": m.get("tavoitteet", []),
    "lessons": {l["id"]: l["title"] for l in m.get("lessons", [])}} for c, m in cur.items() if not c.startswith("_")}, ensure_ascii=False, indent=1))
sys.path.insert(0, str(T / "scripts")); os.environ["FYSIIKKALABRA_ROOT"] = str(T)
import importlib.util, figlib
spec = importlib.util.spec_from_file_location("figs", T / "lessons/FY3" / LESSON / "figures.py"); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
figlib.set_language({"_": "_"}, "."); [fn() for fn in mod.FIGURES.values()]
(en_dir / "figures.json").write_text(json.dumps({t: t for t in figlib.MISSING}, ensure_ascii=False, indent=1))
code, out = run("figures.py", LESSON, "--lang", "en")
en_md = (en_dir / "lesson.md").read_text()
expect("figures.py --lang en writes the figures with the language's decimal sign", code == 0 and "{,}" not in "".join(re.findall(r"<svg\b.*?</svg>", en_md, re.S)) and (fi_dir / "lesson.md").read_text() == (SRC / "content/fi/FY3" / LESSON / "lesson.md").read_text(), out)
code, out = run("check_i18n.py")
expect("translated lesson, course titles and figure texts: complete", code == 0 and "en: 0 error(s)" in out, out)

ex = json.loads((en_dir / "exercises/exercises.json").read_text()); ex["level1"][0]["answer"] += 1; (en_dir / "exercises/exercises.json").write_text(json.dumps(ex, ensure_ascii=False))
code, out = run("check_i18n.py")
expect("a translation that changes an answer is an error", code == 1 and "answer" in out and "differs from Finnish" in out, out)
ex["level1"][0]["answer"] -= 1; (en_dir / "exercises/exercises.json").write_text(json.dumps(ex, ensure_ascii=False))
md = (en_dir / "lesson.md").read_text(); m = re.search(r"(?<!\$)\$([^$\n]+?)\$(?!\$)", re.sub(r"<svg\b.*?</svg>", "", md, flags=re.S))
(en_dir / "lesson.md").write_text(md.replace(m.group(0), m.group(0)[:-1] + "+1$", 1))
code, out = run("check_i18n.py")
expect("a translation that changes a formula is an error", code == 1 and "lesson.md: formulas differ" in out, out)
(en_dir / "lesson.md").write_text(md)

# reviews: the translation has its own hash and its own reports; the Finnish lesson is untouched
en_hash = run("reviews.py", "hash", LESSON)[1].strip()
expect("the Finnish hash does not change when a translation is added", en_hash == fi_hash, en_hash)
sys.path.insert(0, str(T / "scripts"))
import reviews, courses
h_en = reviews.content_hash(courses.find_lesson(LESSON, "en"))
expect("the translation has a hash of its own", h_en and h_en != fi_hash, h_en)
code, out = run("build.py")
expect("an unreviewed translation is not published", code == 0 and not (T / "site/en" / f"{LESSON}.html").exists() and (T / "site/en/index.html").is_file(), out[-400:])
for role in ("science", "pedagogy"):
    (en_dir / "review").mkdir(exist_ok=True); (en_dir / "review" / f"{role}.md").write_text(f"VERDICT: PASS\nCONTENT-HASH: {h_en}\n\n## Blocking\nnone\n")
code, out = run("build.py")
page = (T / "site/en" / f"{LESSON}.html").read_text() if (T / "site/en" / f"{LESSON}.html").exists() else ""
expect("a reviewed translation is published at site/en/", code == 0 and page, out[-600:])
expect("the English page is in English", '<html lang="en"' in page and "Physics Lab" in page and ">Check<" in page, page[:400])
expect("its assets are the shared ones in site/", 'href="../site.css"' in page and 'src="../vendor/katex/katex.min.js"' in page and 'href="../../../index.html"' in page
       and not re.search(r'(?:src|href)="(?!\.\./|https?:|#|[\w.-]+\.html)', page), re.findall(r'(?:src|href)="[^"]*"', page)[:20])
expect("its lesson links stay in English", 'href="FY3.html"' in page and 'href="index.html"' in page)
expect("the numbers in the English page use a decimal point", re.search(r'data-answer="[\d.]+"', page) is not None and "{,}" not in "".join(re.findall(r"<svg\b.*?</svg>", page, re.S)))
fi_page = (T / "site" / f"{LESSON}.html").read_text()
expect("the pages link to each other's language", f'href="en/{LESSON}.html" hreflang="en"' in fi_page and f'href="../{LESSON}.html" hreflang="fi"' in page, re.findall(r'<a class="lang"[^>]*>[^<]*</a>', fi_page + page))
other = next(f.name for f in courses.lessons() if f.name != LESSON)
expect("a page the other language lacks links to its front page", 'href="en/index.html" hreflang="en"' in (T / "site" / f"{other}.html").read_text())
expect("the English course page lists the translated lesson, the rest as coming", f'href="{LESSON}.html"' in (T / "site/en/FY3.html").read_text() and "(en)" in (T / "site/en/FY3.html").read_text())
code, out = run("check_layout.py", "--site")
expect("the English pages pass the 360 px layout check", code == 0, "\n".join(l for l in out.splitlines() if not l.startswith("OK ")) or out[-600:])

shutil.rmtree(T, ignore_errors=True)
expect("the real project is untouched", snapshot() == REAL)
print("all i18n tests passed" if not failures else f"{len(failures)} failure(s): {', '.join(failures)}")
sys.exit(1 if failures else 0)
