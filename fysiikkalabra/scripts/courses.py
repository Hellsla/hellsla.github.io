"""Courses: the one place that turns a course code or a lesson id into its configuration and folders.

  python scripts/courses.py show <FY4 | fy4-1>     the resolved configuration of a course or a lesson (JSON)
  python scripts/courses.py init-lesson <id>       write content/<COURSE>/<id>/meta.json from its curriculum slot (once)
  python scripts/courses.py deps                   which lessons use which simulation folder and picture

`curriculum.json` is the single source of truth. Each module (FY1–FY8) holds the LOPS 2019 data from the texts in
`docs/lops2019/` (tavoitteet, keskeiset_sisallot, temaattiset_yhteydet, kokeet, laaja_alainen) and the lesson slots
(id, title, goals, prerequisites, sim, glossary). The pipeline adds per course only what it needs, all optional:

  "initialized": "2026-10-26"            set by scripts/new_course.py: content and asset folders exist
  "scope_notes": ["..."]                  what belongs in this course and what does not (packets carry them)
  "exercise_levels": {"level1": 5, ...}   overrides the shared 5/4/3 (CLAUDE.md)
  "shuffle_salt": 1                        re-seeds the course's option order (scripts/check_choices.py)
  "paths": {"pics": "...", "sims": "..."}  overrides of the derived folders (normally absent)

Folders derived from the code (FY4, slug fy4), each published under site/ at the same relative path, so a page at
site/fy4-1.html refers to them relatively and they work on GitHub Pages under any base path:

  content/FY4/<lesson-id>/         the lesson folders
  assets/pics/fy4/<file>           pictures of the course; lesson text refers to them as pics/fy4/<file>
  assets/sims/fy4/<name>/          one simulation per folder: sim.js and its own sim.css and images; published as
                                   sims/fy4/<name>/ and found by the sim at document.getElementById('sim-root').dataset.base
  assets/shared/pics/, assets/shared/sims/<name>/   genuinely shared across courses -> shared/pics/, shared/sims/<name>/

A lesson's simulation (meta.json "sim"): true is the lesson's own, `assets/sims/<slug>/<lesson-id>/`; a name reuses
another folder of the course (`"fy4-2"`), `"<slug>/<name>"` one of another course, `"shared/<name>"` a shared one.
FY3's simulations predate the folders and stay as `sim.js` in their lesson folders, published as `<id>-sim.js`;
they keep their URLs and their review hashes. A lesson's course is its id prefix (fy4-1 -> FY4)."""
import datetime, functools, json, os, pathlib, re, sys

ROOT = pathlib.Path(os.environ.get("FYSIIKKALABRA_ROOT") or pathlib.Path(__file__).resolve().parents[1])
DEFAULT_LEVELS = {"level1": 5, "level2": 4, "level3": 3}
LESSON_ID = re.compile(r"^([a-z]+)(\d+)-([0-9][0-9a-z]*)$")
PIC_REF = re.compile(r"""(?:src=["']|\]\()((?:pics/[a-z0-9]+|shared/pics)/[^"')\s]+)""")
BINARY = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".mp4", ".webm", ".woff2")


@functools.lru_cache(maxsize=None)
def curriculum():
    return json.loads((ROOT / "curriculum.json").read_text())


def codes():
    return [k for k in curriculum() if not k.startswith("_")]


def slug(code): return code.lower()


def course(code):
    """The course's curriculum entry plus its code, slug and resolved folders. Exits on an unknown code."""
    cur = curriculum()
    if code not in cur or code.startswith("_"): sys.exit(f"unknown course {code!r}: curriculum.json has {', '.join(codes())}")
    c = dict(cur[code]); s = slug(code); p = c.get("paths", {})
    c.update(code=code, slug=s, paths={
        "content": ROOT / p.get("content", f"content/{code}"),
        "pics": ROOT / p.get("pics", f"assets/pics/{s}"), "sims": ROOT / p.get("sims", f"assets/sims/{s}"),
        "shared_pics": ROOT / "assets/shared/pics", "shared_sims": ROOT / "assets/shared/sims"})
    c.setdefault("exercise_levels", DEFAULT_LEVELS)
    return c


def course_of(lid):
    """FY4 for fy4-1: the id prefix, which must name a module of curriculum.json."""
    m = LESSON_ID.match(lid)
    code = f"{m.group(1).upper()}{m.group(2)}" if m else None
    if code not in curriculum(): sys.exit(f"{lid!r} is not a lesson id of a known course (expected e.g. fy4-1; courses: {', '.join(codes())})")
    return code


def slot(lid):
    """The lesson's slot in curriculum.json ({} when the lesson is not planned there)."""
    return next((l for l in course(course_of(lid)).get("lessons", []) if l["id"] == lid), {})


def lessons(code=None):
    """Lesson folders (content/<COURSE>/<id>/ with meta.json), the reference lesson content/_gold excluded."""
    out = [f.parent for f in sorted((ROOT / "content").glob("*/*/meta.json")) if f.parent.parent.name != "_gold"]
    return [f for f in out if code is None or f.parent.name == code]


def find_lesson(lid):
    for f in sorted((ROOT / "content").glob(f"*/{lid}")):
        if f.parent.name != "_gold" and (f / "meta.json").exists(): return f
    sys.exit(f"no lesson folder for {lid!r} (python scripts/courses.py init-lesson {lid} creates it from the curriculum slot)")


def meta_of(folder):
    return json.loads((folder / "meta.json").read_text())


def sim_dir(folder, meta=None):
    """(kind, folder holding sim.js, published folder) or None. kind: 'lesson' (FY3: sim.js in the lesson folder,
    published as <id>-sim.js), 'course' or 'shared' (a folder of its own under assets/sims/)."""
    lid = folder.name
    if (folder / "sim.js").exists(): return ("lesson", folder, "")
    s = (meta if meta is not None else meta_of(folder)).get("sim")
    if not s: return None
    c = course(course_of(lid))
    if s is True: kind, name, base, pub = "course", lid, c["paths"]["sims"], f"sims/{c['slug']}"
    elif not isinstance(s, str): sys.exit(f"{lid} meta.json sim: true, false or a simulation folder name")
    elif s.startswith("shared/"): kind, name, base, pub = "shared", s[7:], c["paths"]["shared_sims"], "shared/sims"
    elif "/" in s: other, name = s.split("/", 1); kind, base, pub = "course", course(other.upper())["paths"]["sims"], f"sims/{other}"
    else: kind, name, base, pub = "course", s, c["paths"]["sims"], f"sims/{c['slug']}"
    return (kind, base / name, f"{pub}/{name}")


def sim_script(folder, meta=None):
    """The published path of the lesson's sim.js, relative to site/ ('fy3-2-sim.js', 'sims/fy4/fy4-1/sim.js'), or None."""
    d = sim_dir(folder, meta)
    if d is None: return None
    return f"{folder.name}-sim.js" if d[0] == "lesson" else f"{d[2]}/sim.js"


def sim_files(folder, meta=None):
    """[(content name, path)] of the simulation's files, as the content hash and the packets see them."""
    d = sim_dir(folder, meta)
    if d is None: return []
    if d[0] == "lesson": return [("sim.js", folder / "sim.js")]
    return [(f"{d[2]}/{p.relative_to(d[1]).as_posix()}", p) for p in sorted(d[1].rglob("*")) if p.is_file()]


TEXT_FILES = ("lesson.md", "inquiry.json", "exercises.json", "solutions.md", "exit-ticket.json", "sim-spec.md")


def pic_refs(folder):
    """Picture paths the lesson's text refers to (pics/fy4/x.webp, shared/pics/y.svg), in order, without repeats."""
    seen = []
    for n in TEXT_FILES:
        f = folder / n
        if f.exists():
            for r in PIC_REF.findall(f.read_text()):
                if r not in seen: seen.append(r)
    return seen


def pic_source(ref):
    """The file in assets/ that a picture reference names (pics/fy4/x -> assets/pics/fy4/x)."""
    return ROOT / "assets" / ref


def deps():
    """{simulation folder or picture: [lesson ids]} for every lesson."""
    out = {}
    for folder in lessons():
        d = sim_dir(folder)
        if d and d[0] != "lesson": out.setdefault(d[2], []).append(folder.name)
        for r in pic_refs(folder): out.setdefault(r, []).append(folder.name)
    return out


def init_lesson(lid):
    """content/<COURSE>/<id>/meta.json from the curriculum slot; refuses a lesson that is not planned there."""
    code = course_of(lid); c = course(code); s = slot(lid)
    if not c.get("initialized"): sys.exit(f"{code} is not initialized: run python scripts/new_course.py {code} first")
    if not s: sys.exit(f"{lid} is not a lesson slot of {code} in curriculum.json; add the slot there first (the teacher decides the sequence)")
    folder = c["paths"]["content"] / lid
    if (folder / "meta.json").exists(): print(f"{folder.relative_to(ROOT)}/meta.json exists"); return folder
    folder.mkdir(parents=True, exist_ok=True)
    meta = {"id": lid, "course": code, "title": s["title"], "goals": s.get("goals", []), "prerequisites": s.get("prerequisites", []),
            "glossary": s.get("glossary", []), "sim": bool(s.get("sim")), "solutions": "first", "image": False}
    (folder / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
    print(f"wrote {(folder / 'meta.json').relative_to(ROOT)} from the {code} slot ({datetime.date.today()})")
    return folder


def _jsonable(x):
    if isinstance(x, pathlib.Path): return str(x.relative_to(ROOT)) if x.is_relative_to(ROOT) else str(x)
    if isinstance(x, dict): return {k: _jsonable(v) for k, v in x.items()}
    if isinstance(x, list): return [_jsonable(v) for v in x]
    return x


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    if a[0] == "show" and len(a) == 2:
        if LESSON_ID.match(a[1]):
            folder = next((f for f in lessons() if f.name == a[1]), None)
            info = {"course": course_of(a[1]), "slot": slot(a[1]), "folder": folder}
            if folder: info.update(sim=sim_dir(folder) and _jsonable(sim_dir(folder)[1]), sim_script=sim_script(folder), pictures=pic_refs(folder))
            print(json.dumps(_jsonable(info), ensure_ascii=False, indent=1))
        else:
            c = course(a[1].upper()); c = {k: v for k, v in c.items() if k != "lessons"} | {"lessons": [l["id"] for l in c.get("lessons", [])]}
            print(json.dumps(_jsonable(c), ensure_ascii=False, indent=1))
    elif a[0] == "init-lesson" and len(a) == 2: init_lesson(a[1])
    elif a[0] == "deps": print(json.dumps(deps(), ensure_ascii=False, indent=1))
    else: sys.exit(__doc__)
