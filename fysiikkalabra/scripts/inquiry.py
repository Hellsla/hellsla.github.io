"""Inquiry-based lesson structure: validation and rendering of content/<lang>/<course>/<id>/inquiry.json (format version 1).

A lesson with inquiry.json is rendered as stages — Pohdinta → Ennusta → Tutki → Teoria → Esimerkit →
Tarkista osaamisesi (Teoria and Esimerkit were Teoriatiivistelmä and Sovella until 2026-11-05; Esimerkit was Harjoittele for a day, teacher: "pitää olla lyhyt") — each holding activities; stages may repeat, be omitted, or hold the lesson's existing
parts (theory sections of lesson.md, the simulation, the exit ticket). The exit ticket opens Tarkista osaamisesi,
before its checks, with no link of its own in the navigation (teacher 2026-11-04: one step fewer). The exercises always
come last, in their own section "Tehtävät". A lesson without the file renders in the classic layout. See
docs/inquiry.md for the format and docs/inquiry-spec.md for the pedagogy it serves; the page layout (human
decisions 2026-10-26, CLAUDE.md "Lesson page") is in render() and templates/site.css.

  python scripts/inquiry.py <id>     validate one lesson's inquiry.json and print the errors (exit 1 on any)
"""
import hashlib, html as _h, json, pathlib, random, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from i18n import t as T
import answers_shown, mathlayout
import courses, objectives

ROOT = pathlib.Path(__file__).resolve().parents[1]
VERSION = 1
STAGE_IDS = ["herata", "ennusta", "tutki", "selita", "sovella", "tarkista"]   # keys in inquiry.json; titles from lang "inquiry.stage_<id>"
SIM_KEYS = ("howto", "model", "calc")             # the sim activity's boxes, closed by default


# What the student sees comes from lang/<lang>.json (scripts/i18n.py) in the language being built; the
# module-level names below are the Finnish ones, for the checks and tests that compare against a page.
def stages(): return [(s, T(f"inquiry.stage_{s}")) for s in STAGE_IDS]
def nav(): return {"tarkista": T("inquiry.nav_tarkista")}          # nav label when it differs from the stage title
def exit_title(): return T("lesson.exit_ticket")
def exercises_title(): return T("lesson.exercises")
def sim_info(): return tuple((k, T(f"inquiry.sim_{k}")) for k in SIM_KEYS)
def legacy_info(): return T("inquiry.sim_legacy")   # a long sim text written before 2026-10-26, shown behind one box


STAGES, NAV, EXIT_TITLE, EXERCISES_TITLE, SIM_INFO, LEGACY_INFO = stages(), nav(), exit_title(), exercises_title(), sim_info(), legacy_info()
LEAD_WORDS = 30                                   # a sim activity's visible lead is at most this long
CARD_TYPES = ("choice", "numeric", "explain", "experiment", "interpret", "reflect", "exit")   # a task: one card holds its heading, instructions, answers and feedback
TYPES = ("hook", "text", "choice", "experiment", "interpret", "numeric", "explain", "reflect", "theory", "sim", "exercises", "exit")
QUESTION_TYPES = ("choice", "numeric", "explain")
FIGURE_TYPES = ("hook", "text", "choice", "numeric", "explain", "interpret")   # may carry "figure": "<id>" (scripts/figcat.py)
FBD_TAGS = ("identify", "select", "error", "draw", "equations")   # "fbd": the force-diagram skill a task practises (docs/force-diagrams.md)
ID_RE = re.compile(r"^[a-z][a-z0-9-]{1,40}$")
CORE_TYPES = ("choice", "experiment", "interpret", "numeric", "explain")   # may carry "core": true: a task of the lesson marked Ydintehtävä, like a core exercise (teacher 2026-11-05)
OPTIONAL_TYPES = ("hook", "text", "choice", "experiment", "interpret", "numeric", "explain", "reflect", "theory", "exit")   # may carry "optional": true
SOURCES = ("measured", "statistics", "simulated", "model", "example")   # statistics and example: teacher's FY2 rule 2026-10-28 (real sourced data / invented data said so)      # interpret "source"; its badge is lang "inquiry.source_<source>"
RESERVED_IDS = {"sim", "sim-root", "exercises", "exit", "teoria", "herata", "ennusta", "tutki", "selita", "sovella", "tarkista"}   # ids the page already uses


# The stages Teoriatiivistelmä and Sovella were renamed Teoria and Esimerkit (teacher 2026-11-05: the theory stage holds
# more than a summary, and Sovella holds a worked example and practice). The texts written before name them the old way
# ("Palaute avautuu, kun olet lukenut Teoriatiivistelmän kohdan …"); the page shows the new names, so the reviewed
# content (and its hash) stays as it is. New text names the stages Teoria / Esimerkit (Theory / Examples) directly.
_BACK = str.maketrans("äöÄÖ", "aoAO")             # tiivistelmä takes front-vowel endings, teoria back-vowel ones
def _teoria(m):                                   # Teoriatiivistelmä(n) → Teoria(n); a place case → Teoria-osassa, not "teoriassa" (= in theory)
    end = m.group(2)
    return m.group(1) + "eoria" + (end if end in ("", "n") else "-osa" + end.translate(_BACK))
OLD_STAGE_TERMS = ((re.compile(r"\b([Tt])eoriatiivistelmä(\w*)"), _teoria),
                   (re.compile(r"\b([Tt])heory summary\b"), lambda m: m.group(1) + "heory"),
                   (re.compile(r'(<a href="#sovella">)(?:Sovella|Apply)(</a>)'), lambda m: m.group(1) + T("inquiry.stage_sovella") + m.group(2)))


def current_stage_names(html):
    """The page's html with the old stage names of the texts replaced by the current ones (Teoriatiivistelmän → Teorian)."""
    for rx, new in OLD_STAGE_TERMS: html = rx.sub(new, html)
    return html


def heading(title):
    """(key, shown) of a lesson.md `## ` heading. The formula section is named after its law, `## Kaava: Lämpömäärä`:
    the page shows "Lämpömäärä", while inquiry.json, the lint and the build keep using the key "Kaava". A heading
    written in another language (lang "sections", `## Core idea`) has the key of the section it translates; a lesson's
    own section names its Finnish key at the end, `## The structure of matter {Aineen rakenne}`."""
    own = re.match(r"(.+?)\s*\{([^{}$]+)\}\s*$", title.strip())
    if own: return (own.group(2).strip(), own.group(1).strip())
    names = {v: k for k, v in T("sections").items() if not k.startswith("_")}
    m = re.match(r"(.+?):\s*(\S.*)$", title.strip())
    if m and names.get(m.group(1)) == "Kaava": return ("Kaava", m.group(2).strip())
    return (names.get(title.strip(), title.strip()), title.strip())


def section_keys(lesson_md): return {heading(t)[0] for t in re.findall(r"^## (.+)$", lesson_md, re.M)}


def load(folder):
    f = folder / "inquiry.json"
    return json.loads(f.read_text()) if f.exists() else None


# Options are shown shuffled (choice_order), so no text may point at an option by its letter or place.
POSITIONAL = re.compile(r"\b(?:vaihtoehto|vaihtoehdo\w*|kohta|kohda\w*)\s+[A-Da-d]\b"
                        r"|\b(?:ensimmäi|toi|kolma|neljä|viimei|edelli|seuraa|yli|ali)\w*\s+vaihtoehto"
                        r"|\b(?:kaikki|molemmat)\s+(?:edellä|yllä)|\b(?:edellä|yllä|alla)\s+(?:mainit|olev|luetel)\w*\s+(?:vaihtoehd|kohd|vastauks)", re.I)


def _check_choice(a, path, errs):
    if not isinstance(a.get("prompt"), str) or not a["prompt"].strip(): errs.append(f"{path}.prompt: a non-empty string is required")
    ch = a.get("choices")
    if not isinstance(ch, list) or len(ch) < 2: errs.append(f"{path}.choices: at least two choices are required")
    else:
        for i, c in enumerate(ch):
            if not isinstance(c, dict) or not isinstance(c.get("text"), str): errs.append(f"{path}.choices[{i}].text: a string is required")
            if not isinstance(c.get("feedback"), str) or not c["feedback"].strip(): errs.append(f"{path}.choices[{i}].feedback: every choice needs misconception-specific feedback")
            if "correct" in c and not isinstance(c["correct"], bool): errs.append(f"{path}.choices[{i}].correct: true or false")
            if isinstance(c, dict) and "figure" in c:
                import figcat
                for _, msg in (figcat.check_refs(json.dumps({"figure": c["figure"]})) if isinstance(c["figure"], str) else [(0, "an id such as \"fy4-5/vk-a\"")]): errs.append(f"{path}.choices[{i}].figure: {msg}")
            if a.get("layout") == "figures" and isinstance(c, dict) and not c.get("figure"): errs.append(f"{path}.choices[{i}].figure: layout \"figures\" shows each option as a figure")
        if not any(c.get("correct") for c in ch if isinstance(c, dict)): errs.append(f"{path}.choices: one choice must have \"correct\": true")
        texts = [("prompt", a.get("prompt"))] + [(f"choices[{i}].{k}", c.get(k)) for i, c in enumerate(ch) if isinstance(c, dict) for k in ("text", "feedback")]
        for where, t in texts:
            m = POSITIONAL.search(t) if isinstance(t, str) else None
            if m: errs.append(f"{path}.{where}: \"{m.group(0)}\" points at an option by its letter or place, but options are shown shuffled; name the option by its content")
    r = a.get("reveal")
    if r is not None:
        if not isinstance(r, dict) or not isinstance(r.get("after"), str): errs.append(f"{path}.reveal: {{\"after\": \"<experiment or theory id>\", \"min\": n}}")
        elif "min" in r and (not isinstance(r["min"], int) or r["min"] < 1): errs.append(f"{path}.reveal.min: a positive integer")
        elif "pending" in r and (not isinstance(r["pending"], str) or not r["pending"].strip()): errs.append(f"{path}.reveal.pending: the text shown while the feedback waits (e.g. where the evidence is)")
    if "justify" in a and not isinstance(a["justify"], bool): errs.append(f"{path}.justify: true or false")
    if a.get("layout") not in (None, "list", "models", "figures"): errs.append(f"{path}.layout: \"list\", \"models\" or \"figures\" (each option a figure)")


def _check_numeric(a, path, errs):
    if not isinstance(a.get("prompt"), str): errs.append(f"{path}.prompt: a string is required")
    if not isinstance(a.get("answer"), (int, float)) or isinstance(a.get("answer"), bool): errs.append(f"{path}.answer: a number is required")
    if not isinstance(a.get("unit", ""), str): errs.append(f"{path}.unit: a string")
    tol = a.get("tolerance", 0.02)
    if not isinstance(tol, (int, float)) or tol <= 0: errs.append(f"{path}.tolerance: a positive number (relative)")
    for i, m in enumerate(a.get("mistakes", []) or []):
        if not isinstance(m, dict) or not isinstance(m.get("value"), (int, float)) or not isinstance(m.get("feedback"), str):
            errs.append(f"{path}.mistakes[{i}]: {{\"value\": number, \"feedback\": text}}")


CONFIDENCE = re.compile(r"^\s*(?:Osaan|Ymmärrän|Tiedän|Olen varma|Pystyn|Tunnen|Hallitsen|I can|I understand|I know)\b", re.I)


def _check_explain(a, path, errs):
    if not isinstance(a.get("prompt"), str): errs.append(f"{path}.prompt: a string is required")
    crit = a.get("criteria")
    if not isinstance(crit, list) or not crit or not all(isinstance(c, str) or (isinstance(c, dict) and isinstance(c.get("key"), str)) for c in crit):
        errs.append(f"{path}.criteria: a non-empty list of self-assessment criteria (text, or {{\"key\": a shared criterion, \"detail\": its specifics}})")
    else:
        for i, c in enumerate(crit):
            if isinstance(c, dict) and not T.has(f"criteria.{c['key']}"): errs.append(f"{path}.criteria[{i}].key: \"{c['key']}\" is not a shared criterion (lang \"criteria\")")
    if "draw" in a and not isinstance(a["draw"], bool): errs.append(f"{path}.draw: true or false")
    if a.get("draw") and not isinstance(a.get("model_figure"), str): errs.append(f"{path}.model_figure: a drawing task shows its model diagram by id (\"fy4-5/<name>\")")
    if isinstance(a.get("model_figure"), str):
        import figcat
        for _, msg in figcat.check_refs(json.dumps({"figure": a["model_figure"]})): errs.append(f"{path}.model_figure: {msg}")
    if not isinstance(a.get("model"), str) or not a["model"].strip(): errs.append(f"{path}.model: a model answer is required")
    for i, c in enumerate(a.get("criteria") or []):
        c = c.get("detail", "") if isinstance(c, dict) else c
        if isinstance(c, str) and CONFIDENCE.match(c):
            errs.append(f"{path}.criteria[{i}]: a criterion names something the answer shows (\"Vastaus kertoo, että …\"), not how sure the student feels")
    if "practice" in a and not (isinstance(a["practice"], str) and a["practice"].strip()):
        errs.append(f"{path}.practice: where to practise the missing reasoning, markdown with a link (default: the theory and the exercises)")


def validate(folder, inquiry, lesson_md):
    """Errors as strings naming the lesson, the file and the field. Empty list when valid."""
    lid = folder.name; errs = []
    E = lambda m: errs.append(f"{lid} inquiry.json: {m}")
    if not isinstance(inquiry, dict): return [f"{lid} inquiry.json: the top level must be an object"]
    if inquiry.get("version") != VERSION: E(f"version: must be {VERSION}")
    extra = inquiry.get("self_extra")   # Tarkista osaamisesi: statements of what the tasks did not measure (teacher 2026-11-06)
    if extra is not None and not (isinstance(extra, list) and 1 <= len(extra) <= 5 and all(isinstance(x, str) and x.strip() and len(x.split()) <= 25 for x in extra)):
        E("self_extra: one to five short self-assessment statements in the student's words (\"Osaan ...\"), at most about 25 words each")
    if not isinstance(inquiry.get("contribution"), str) or not inquiry["contribution"].strip(): E("contribution: one sentence on what this lesson adds that earlier lessons did not")
    learn = inquiry.get("learn")
    if not (isinstance(learn, list) and 2 <= len(learn) <= 3 and all(isinstance(x, str) and x.strip() for x in learn)):
        E("learn: two or three learning goals from the student's side, each completing the heading \"Tällä tunnilla opit\" (\"laskemaan …\", \"selittämään …\"; teacher 2026-10-27, grammar 2026-10-29: scripts/objectives.py)")
    else:
        for i, x in enumerate(learn):
            if len(x.split()) > 22: E(f"learn[{i}]: {len(x.split())} words; a goal is one short line (at most about 20 words), the explanation belongs to the theory")
        for m in objectives.check(learn, courses.lang_of(folder))[0]: E(m)
    deepen = inquiry.get("deepen")   # "Voit myös syventää osaamistasi": the goals of the chapter's Lisätiedoksi and Syventävä parts (teacher 2026-11-07, LOPS 2019)
    if deepen is not None and not (isinstance(deepen, list) and 1 <= len(deepen) <= 2 and all(isinstance(x, str) and x.strip() and len(x.split()) <= 22 for x in deepen)):
        E("deepen: one or two short goals of the extension parts, each completing the heading \"Voit myös syventää osaamistasi\"")
    prior = inquiry.get("prior", [])
    if not isinstance(prior, list) or not all(isinstance(x, str) and x.strip() for x in prior): E("prior: a list of short strings (what the student already knows, with the lesson it comes from)")
    acts = inquiry.get("activities")
    if not isinstance(acts, list) or not acts: E("activities: a non-empty list is required"); return errs
    sections = section_keys(lesson_md)
    ids, exp_ids, hints_ok = set(), set(), True
    for i, a in enumerate(acts):
        p = f"activities[{i}]"
        if not isinstance(a, dict): E(f"{p}: must be an object"); continue
        aid = a.get("id")
        if not isinstance(aid, str) or not ID_RE.match(aid): E(f"{p}.id: a short lowercase id such as \"pred-1\" is required")
        elif aid in ids: E(f"{p}.id: \"{aid}\" is used twice")
        elif aid in RESERVED_IDS: E(f"{p}.id: \"{aid}\" is an id the page already uses (section or stage); choose another, e.g. \"simulaatio\", \"tehtavat\", \"lahtolippu\"")
        else: ids.add(aid)
        if a.get("stage") not in STAGE_IDS: E(f"{p}.stage: one of {', '.join(STAGE_IDS)}")
        t = a.get("type")
        if t not in TYPES: E(f"{p}.type: one of {', '.join(TYPES)}"); continue
        path = f"{lid} inquiry.json: {p}"
        for where, x in ((p, a), (f"{p}.question", a.get("question"))):
            if isinstance(x, dict) and "figure" in x:
                import figcat
                if t not in FIGURE_TYPES: E(f"{where}.figure: a figure goes on a {', '.join(FIGURE_TYPES)} task")
                for _, msg in (figcat.check_refs(json.dumps({"figure": x["figure"]})) if isinstance(x["figure"], str) else [(0, "an id such as \"fy1-4/scatter\"")]): E(f"{where}.figure: {msg}")
        if "optional" in a and (not isinstance(a["optional"], bool) or (a["optional"] and t not in OPTIONAL_TYPES)):
            errs.append(f"{path}.optional: true or false, and only on {', '.join(OPTIONAL_TYPES)} (the simulation and the exercises are never folded away)")
        if "core" in a and (not isinstance(a["core"], bool) or (a["core"] and (t not in CORE_TYPES or a.get("optional")))):
            errs.append(f"{path}.core: true or false, only on {', '.join(CORE_TYPES)} and never with optional (a core task is on the core path)")
        if "fold" in a and (not isinstance(a["fold"], str) or not a["fold"].strip() or len(a["fold"]) > 24 or t not in OPTIONAL_TYPES or a.get("optional")):
            errs.append(f"{path}.fold: a short tag (at most 24 characters) for a required part kept closed until it is opened, only on {', '.join(OPTIONAL_TYPES)} and not with optional")
        if "fbd" in a and a["fbd"] not in FBD_TAGS: errs.append(f"{path}.fbd: one of {', '.join(FBD_TAGS)} (docs/force-diagrams.md)")
        hints = a.get("hints")
        if hints is not None and (not isinstance(hints, list) or len(hints) > 3 or not all(isinstance(h, str) for h in hints)):
            errs.append(f"{path}.hints: a list of at most three strings (question, representation, worked step)")
        if t in ("hook", "text"):
            if not isinstance(a.get("text"), str) or not a["text"].strip(): errs.append(f"{path}.text: markdown text is required")
        elif t == "choice": _check_choice(a, path, errs)
        elif t == "numeric": _check_numeric(a, path, errs)
        elif t == "explain": _check_explain(a, path, errs)
        elif t == "reflect":
            if not isinstance(a.get("predictions"), list) or not a["predictions"]: errs.append(f"{path}.predictions: the ids of the predictions to show")
            if not isinstance(a.get("prompt"), str): errs.append(f"{path}.prompt: a string is required")
        elif t == "theory":
            secs = a.get("sections")
            if not isinstance(secs, list) or not secs: errs.append(f"{path}.sections: the lesson.md section titles to place here")
            else:
                for s in secs:
                    if s not in sections: errs.append(f"{path}.sections: \"{s}\" is not a ## section of lesson.md (have: {', '.join(sorted(sections))})")
        elif t == "experiment":
            if isinstance(aid, str): exp_ids.add(aid)
            if not isinstance(a.get("intro"), str): errs.append(f"{path}.intro: what the student does, one short paragraph")
            if not isinstance(a.get("initial"), dict) or not a["initial"]: errs.append(f"{path}.initial: the explicit initial conditions {{param: value}}")
            if not isinstance(a.get("vary"), str): errs.append(f"{path}.vary: the one parameter the student changes")
            if not isinstance(a.get("locked"), list): errs.append(f"{path}.locked: the parameters held constant (a list, may be empty)")
            elif isinstance(a.get("vary"), str) and a["vary"] in a["locked"]: errs.append(f"{path}.locked: the varied parameter cannot be locked")
            if not isinstance(a.get("measure"), list) or not a["measure"]: errs.append(f"{path}.measure: the simState keys to record")
            if "min" in a and (not isinstance(a["min"], int) or a["min"] < 1): errs.append(f"{path}.min: measurements before the linked predictions are revealed")
            for key in ("units", "names"):
                if key in a and (not isinstance(a[key], dict) or not all(isinstance(v, str) for v in a[key].values())): errs.append(f"{path}.{key}: {{param: text}}")
        elif t == "sim":
            for k, _ in SIM_INFO:
                if k in a and (not isinstance(a[k], str) or not a[k].strip()): errs.append(f"{path}.{k}: markdown text")
        elif t == "interpret":
            if not isinstance(a.get("text"), str) or not a["text"].strip(): errs.append(f"{path}.text: the representation (table, figure or measurements) in markdown/HTML")
            src = a.get("source")
            if src is not None and src not in SOURCES: errs.append(f"{path}.source: one of {', '.join(SOURCES)} (what the numbers are: measured, official statistics with their source, simulated example data, values computed from the model, or an invented example)")
            if src in ("measured", "statistics") and not (isinstance(a.get("source_note"), str) and a["source_note"].strip()):
                errs.append(f"{path}.source_note: measured data needs a note on who measured it and how (never present invented numbers as measurements)")
        if t == "explain" and "after" in a and not (isinstance(a["after"], list) and a["after"] and all(isinstance(x, str) for x in a["after"])):
            errs.append(f"{path}.after: the ids of the experiments whose measurements the conclusion rests on")
        if t in ("experiment", "interpret") and "question" in a:
            q = a["question"]
            if not isinstance(q, dict) or q.get("type") not in QUESTION_TYPES: errs.append(f"{path}.question.type: one of {', '.join(QUESTION_TYPES)}")
            else: {"choice": _check_choice, "numeric": _check_numeric, "explain": _check_explain}[q["type"]](q, f"{path}.question", errs)
    for i, a in enumerate(acts):                      # references
        if not isinstance(a, dict): continue
        r = a.get("reveal") if a.get("type") == "choice" else None
        theory_ids = {b.get("id") for b in acts if isinstance(b, dict) and b.get("type") == "theory"}
        if isinstance(r, dict) and isinstance(r.get("after"), str) and r["after"] not in exp_ids | theory_ids: E(f"activities[{i}].reveal.after: \"{r['after']}\" is not an experiment or theory id")
        if a.get("type") == "explain" and isinstance(a.get("after"), list):
            for x in a["after"]:
                if x not in exp_ids: E(f"activities[{i}].after: \"{x}\" is not an experiment id")
                elif not a.get("optional") and any(b.get("optional") for b in acts if isinstance(b, dict) and b.get("id") == x):
                    E(f"activities[{i}].after: the required conclusion rests on the optional experiment \"{x}\"")
        if isinstance(r, dict) and not a.get("optional") and any(b.get("optional") for b in acts if isinstance(b, dict) and b.get("id") == r.get("after")):
            E(f"activities[{i}].reveal.after: a required prediction cannot wait for the optional experiment \"{r['after']}\"")
        if a.get("type") == "reflect":
            for pid in a.get("predictions", []):
                if pid not in ids: E(f"activities[{i}].predictions: \"{pid}\" is not an activity id")
    placed = [s for a in acts if isinstance(a, dict) and a.get("type") == "theory" for s in a.get("sections", [])]
    for s in placed:
        if placed.count(s) > 1: E(f"theory: section \"{s}\" is placed more than once")
    for kind in ("exit", "exercises", "sim"):
        if sum(1 for a in acts if isinstance(a, dict) and a.get("type") == kind) > 1: E(f"only one activity of type {kind} is allowed")
    return errs


# ---------------------------------------------------------------- rendering
def esc(s): return _h.escape(str(s), quote=True)


GREEK = {"Σ": r"\Sigma ", "Δ": r"\Delta ", "ρ": r"\rho ", "θ": r"\theta ", "η": r"\eta ", "γ": r"\gamma ", "α": r"\alpha ", "μ": r"\mu ", "λ": r"\lambda ", "ν": r"\nu ", "φ": r"\varphi ", "ω": r"\omega "}
SUBS = dict(zip("₀₁₂₃₄₅₆₇₈₉", "0123456789"))
SYMBOL = re.compile(r"[A-Za-zΔρθηγαμΣλνφω](?:[A-Za-zΔρθηγαμΣλνφω₀-₉/]|_[A-Za-z0-9μ]+)*")
UNIT = re.compile(r"[µμ]?[A-Za-zΩ/%]+[²³]?|°")   # µT and ° too (FY7, 2026-11-03); Ω, kΩ (FY6)


def unit_tex(u):
    """m/s² -> \\text{m/s}^2, % -> \\%: a unit as maths (teacher 2026-10-28, "kaikki LaTeXilla")."""
    if u == "%": return "\\%"
    if u == "°": return "^\\circ"
    if u[0] in "µμ": return "\\mu" + unit_tex(u[1:])   # µT -> \mu\text{T}
    t = ("\\text{" + u.rstrip("²³") + "}").replace("Ω", "}\\Omega\\text{").replace("\\text{}", "")   # Ω, kΩ: \\Omega in maths
    return t + ({"²": "^2", "³": "^3"}.get(u[-1], ""))


def is_symbol(tok):
    """A quantity symbol or a short formula of symbols (m, ΔL/L₀, p_ref, ρgh, pV), not a Finnish word."""
    return bool(SYMBOL.fullmatch(tok)) and (len(tok) <= 2 or bool(re.search(r"[Δρθηγαμλνφω₀-₉_/Σ]", tok)))


def sym_tex(tok):
    """ΔL/L₀ -> \\Delta L/L_0, p_ref -> p_\\text{ref}, x_B -> x_\\text{B}."""
    out = re.sub(r"_(\w+)", lambda m: "_" + (m.group(1) if re.fullmatch(r"[0-9]+|[a-z]|[μ]", m.group(1)) else r"\text{" + m.group(1) + "}"), tok)   # v_0, F_x italic; x_B, p_ref upright
    out = re.sub(r"[₀-₉]+", lambda m: "_" + "".join(SUBS[c] for c in m.group(0)) if len(m.group(0)) == 1 else "_{" + "".join(SUBS[c] for c in m.group(0)) + "}", out)
    for k, v in GREEK.items(): out = out.replace(k, v)
    return out.strip()


def tex_name(s):
    """An experiment's quantity name or table label on the page, with its symbol as maths (NOTES 1): "massa m" ->
    "massa $m$", "θ" -> "$\\theta$", "ΔT (K)" -> "$\\Delta T$ (K)", "p mitattu" -> "$p$ mitattu". Plain words stay."""
    toks = str(s).split(" ")
    unit = len(toks) > 1 and re.fullmatch(r"\((" + UNIT.pattern + r")\)", toks[-1])
    if unit: toks[-1] = "$(" + unit_tex(unit.group(1)) + ")$"   # "(m/s²)" -> "$(\\text{m/s}^2)$", one unbreakable piece
    last = len(toks) - (2 if unit else 1)
    for i in sorted({0, last}):
        if is_symbol(toks[i]): toks[i] = "$" + sym_tex(toks[i]) + "$"
    return esc(" ".join(toks))


_PLAIN_SYM = {"Sigma": "Σ", "Delta": "Δ", "alpha": "α", "beta": "β", "theta": "θ", "lambda": "λ", "mu": "μ", "rho": "ρ",
              "eta": "η", "omega": "ω", "Omega": "Ω", "varphi": "φ", "phi": "φ", "pi": "π", "tau": "τ", "circ": "°", "cdot": "·"}
_SUP = str.maketrans("0123456789-+", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺")


def plain_label(s):
    r"""A table heading without LaTeX, for the exported table (teacher 2026-11-03): "$\Sigma F_x$ (N)" -> "ΣFx (N)",
    "$a_x$ (m/s$^2$)" -> "ax (m/s²)", "$f\;(10^{14}\,\text{Hz})$" -> "f (10¹⁴ Hz)". A spreadsheet shows it as written."""
    def math(t):   # inside $…$ a space is no space; \, \; \  are
        t = re.sub(r"\\([A-Za-z]+)", lambda m: "\\" + m.group(1) if m.group(1) in ("text", "mathrm", "operatorname", "overline", "mathbf")
                   else _PLAIN_SYM.get(m.group(1), "\x00" if m.group(1) in ("quad", "qquad") else m.group(1)), t)
        t = re.sub(r"\\[,;:! ]", "\x00", t)
        t = re.sub(r"\\([%#&$])", r"\1", t)   # \% -> % ("kasvaimen kautta (\%)", fy8-14 2026-11-04)
        t = re.sub(r"\\(text|mathrm)\{([^{}]*)\}", lambda m: "\\" + m.group(1) + "{" + m.group(2).replace(" ", "\x00") + "}", t)   # words keep their spaces
        t = t.replace(" ", "")
        for _ in range(3): t = re.sub(r"\\(?:text|mathrm|operatorname|overline|mathbf)\{([^{}]*)\}", r"\1", t)
        t = re.sub(r"\^\{([^{}]*)\}|\^(.)", lambda m: (m.group(1) if m.group(1) is not None else m.group(2)).translate(_SUP), t)
        t = re.sub(r"_\{([^{}]*)\}|_(.)", lambda m: m.group(1) if m.group(1) is not None else m.group(2), t)
        return t.replace("{,}", ",").replace("{", "").replace("}", "").replace("\x00", " ")
    parts = str(s).split("$")
    t = "".join(math(x) if i % 2 else re.sub(r"_\{([^{}]*)\}|_(?=\w)", lambda m: m.group(1) or "", x) for i, x in enumerate(parts))
    return re.sub(r"\s+", " ", t).replace("( ", "(").strip()


def inline(md, text):
    """Markdown rendered without the outer <p>, for a choice, a legend or a prompt that sits inside another block."""
    h = md(text).strip()
    m = re.fullmatch(r"<p>(.*)</p>", h, flags=re.S)
    return m.group(1) if m else h


def hints_html(hints):
    if not hints: return ""
    names = [T(f"inquiry.hint_{i}") for i in (1, 2, 3)]
    return '<div class="hints">' + "".join(f'<details class="hint" data-n="{i + 1}"><summary>{names[i]}</summary><div>{h}</div></details>'
                                           for i, h in enumerate(hints)) + "</div>"


def _no_error(): return re.compile(r"\s*(?:" + "|".join(map(re.escape, T("inquiry.no_error").split("|"))) + ")")   # "Laskussa ei ole virhettä"


def shuffle_salt(lid):
    """The course's "shuffle_salt" in curriculum.json (0 when absent or when lid names no course, as in tests)."""
    try:
        import courses
        return courses.curriculum().get(courses.course_of(lid), {}).get("shuffle_salt", 0)
    except SystemExit: return 0


def choice_order(choices, lid, aid, salt=None):
    """The order the options are shown in: shuffled once per activity with a seed from its id, so the page is the
    same on every build but the correct option is not in the same place from question to question (authors tend to
    write it second). "Laskussa ei ole virhettä" stays last, where a reader expects it. A course's shuffle_salt
    (scripts/check_choices.py) re-seeds the whole course without touching a lesson; without one the seed is the
    lesson and activity id alone, so FY3 keeps the order it was published with."""
    salt = shuffle_salt(lid) if salt is None else salt
    no_error = _no_error()
    rest = [c for c in choices if not no_error.match(c["text"])]
    random.Random(hashlib.sha256((f"{lid}:{aid}" + (f":{salt}" if salt else "")).encode()).hexdigest()).shuffle(rest)
    return rest + [c for c in choices if no_error.match(c["text"])]


def fig_of(a):
    """The figure a task refers to by its id ("figure": "fy1-4/scatter-points", scripts/figcat.py), drawn in the page's
    language from the one figures.py that owns it; empty without one."""
    if not a.get("figure"): return ""
    import figcat
    return figcat.figure_html(a["figure"], T.lang)


def choice_html(a, md, lid, aid):
    opts = ""
    for i, c in enumerate(choice_order(a["choices"], lid, aid)):
        opts += (f'<li><label><input type="radio" name="{esc(aid)}" value="{i}" data-correct="{"1" if c.get("correct") else "0"}">'
                 f'<span>{inline(md, c["text"])}{fig_of(c)}</span></label><div class="feedback" data-for="{i}" hidden>{md(c["feedback"])}</div></li>')
    reveal = a.get("reveal") or {}
    attrs = f' data-reveal="{esc(reveal["after"])}" data-reveal-min="{reveal.get("min", 1)}"' if reveal else ""
    justify = (f'<label class="justify">{T("inquiry.justify")}<textarea rows="2"></textarea></label>' if a.get("justify") else "")
    sol = f'<div class="solution-text">{md(a["solution"])}</div>' if a.get("solution") else ""
    pending = f'<p class="pending" tabindex="-1" data-theory="{esc(reveal.get('pending') or T('inquiry.pending_theory'))}" hidden>{esc(reveal.get("pending")) if reveal.get("pending") else T("inquiry.pending")}</p>' if reveal else ""
    return (f'<fieldset class="choice {esc(a.get("layout", "list"))}"{attrs}><legend>{legend_html(inline(md, a["prompt"]))}</legend>{fig_of(a)}{sol}'
            f'<ul class="choices">{opts}</ul>{justify}<div class="choice-actions"><button type="button" class="commit">{T("inquiry.commit")}</button></div>'
            f'{pending}<output aria-live="polite"></output></fieldset>')


def truefalse_html(a, md, aid):
    """True-or-false statements about one phenomenon (teacher 2026-11-05, like the first task of the YO exam): every
    statement gets Tosi or Epätosi, then one "Vastaa" for the whole list. The first answer marks the statements that are
    wrong; they may be changed once, then every statement shows its truth and reasoning (inquiry.js part 2b). The
    statements stay in the authored order: they often build on each other."""
    rows = ""
    for i, s in enumerate(a["statements"]):
        name = f"{aid}-s{i}"
        rows += (f'<li data-true="{"1" if s["true"] else "0"}"><p class="tf-text" id="{esc(name)}-t">{inline(md, s["text"])}</p>'
                 f'<span class="tf-opts" role="radiogroup" aria-labelledby="{esc(name)}-t">'
                 f'<label><input type="radio" name="{esc(name)}" value="1"> <span>{T("inquiry.tf_true")}</span></label>'
                 f'<label><input type="radio" name="{esc(name)}" value="0"> <span>{T("inquiry.tf_false")}</span></label></span>'
                 f'<div class="feedback" hidden>{md(s["feedback"])}</div></li>')
    return (f'<fieldset class="tf" data-id="{esc(aid)}"><legend>{legend_html(inline(md, a["prompt"]))}</legend><ol class="tf-list">{rows}</ol>'
            f'<div class="choice-actions"><button type="button" class="commit">{T("inquiry.commit")}</button></div><output aria-live="polite"></output></fieldset>')


def order_html(a, md, lid, aid):
    """Putting situations in order by a quantity (teacher 2026-11-05): the items are written in the correct order and
    shown shuffled (choice_order); the student gives each a place 1..n from a menu, one "Vastaa" for all. The first
    answer marks the misplaced items; one change, then each item shows its correct place (inquiry.js part 2c)."""
    items = [dict(c, rank=i + 1) for i, c in enumerate(a["order"])]
    n = len(items)
    opts = "".join(f'<option value="{k}">{k}</option>' for k in range(1, n + 1))
    rows = ""
    for j, c in enumerate(choice_order(items, lid, aid)):
        sid = f"{aid}-o{j}"
        rows += (f'<li data-rank="{c["rank"]}"><label for="{esc(sid)}" class="ord-text">{inline(md, c["text"])}{fig_of(c)}</label>'
                 f'<select id="{esc(sid)}" aria-label="{esc(T("inquiry.order_place"))}"><option value="">{esc(T("inquiry.order_pick"))}</option>{opts}</select>'
                 f'<span class="ord-right" hidden></span></li>')
    return (f'<fieldset class="order" data-id="{esc(aid)}"><legend>{legend_html(inline(md, a["prompt"]))}</legend><ul class="order-list">{rows}</ul>'
            f'<div class="choice-actions"><button type="button" class="commit">{T("inquiry.commit")}</button></div><output aria-live="polite"></output></fieldset>')


def answer_label(unit):
    """An answer field's accessible name: "Vastaus yksikössä m/s²" (the question describes it, aria-describedby)."""
    return T("inquiry.answer_in", unit=unit) if unit.strip() else T("inquiry.answer")


def numeric_html(a, md, aid):
    unit = esc(a.get("unit", ""))
    # a mistake's feedback may carry Markdown (a chapter link "[*…*](fy7-10.html)"): it goes to the page as HTML too
    ms = [dict(m, html=inline(md, m["feedback"])) if isinstance(m, dict) and re.search(r"\]\(|\*", m.get("feedback", "")) else m
          for m in a.get("mistakes", []) or []]
    mistakes = esc(json.dumps(ms, ensure_ascii=False))
    sol = (f'<details class="solution"><summary>{T("inquiry.show_solution")}</summary><div class="steps">'
           f'{mathlayout.steps_html(md(mathlayout.solution_md(a["solution"], T("lesson.solution_display_steps"))), T("lesson.solution_answer_step"))}</div></details>' if a.get("solution") else "")
    shown = answers_shown.shown(a.get("solution") or "", T("lesson.solution_answer_step"), a["answer"], a.get("tolerance", 0.02))
    st = answers_shown.step(shown, a["answer"]) if shown else None    # one unit in the shown answer's last digit; the check allows half of it (lesson.js part 1)
    return (f'<div class="numeric">{task_text(inline(md, a["prompt"]), pid=f"{aid}-q")}{fig_of(a)}'
            f'<form class="check" data-answer="{a["answer"]}" data-tol="{a.get("tolerance", 0.02)}"' + (f' data-step="{st:g}"' if st else "") + f' data-mistakes=\'{mistakes}\' novalidate>'
            f'<input type="text" inputmode="decimal" autocomplete="off" enterkeyhint="done" aria-label="{esc(answer_label(a.get("unit", "")))}" aria-describedby="{esc(aid)}-q" placeholder="?">'
            + (f'<span class="unit">{unit}</span>' if unit else "") + f'<button type="submit">{T("lesson.check")}</button><output aria-live="polite"></output></form>'
            f'{hints_html([md(mathlayout.display_chains(h)) for h in a.get("hints", [])])}{sol}</div>')


def criterion_html(c, md):
    """A self-assessment criterion: its own text, or a shared criterion by key (lang "criteria", e.g. the force-diagram
    criteria fbd_*) with the task's specifics after it."""
    if isinstance(c, str): return inline(md, c)
    detail = f' <span class="crit-detail">{inline(md, c["detail"])}</span>' if c.get("detail") else ""
    return inline(md, T(f"criteria.{c['key']}")) + detail


def explain_html(a, md, aid):
    """A written explanation, assessed by the student in a guided sequence (teacher 2026-10-28): their own answer first;
    the model answer opens only after it (inquiry.js); then observable criteria from the model answer to tick; then
    "what is missing" lists the unticked criteria as the reasoning to add, with where to practise it (the task's own
    `practice`, markdown, or the theory and the exercises). A conclusion with "after" also waits for the measurements of
    those experiments, and offers to copy the tables and the student's own text for their notes. No grading, no model."""
    crit = "".join(f'<li><label><input type="checkbox"> <span>{criterion_html(c, md)}</span></label></li>' for c in a["criteria"])
    draw = a.get("draw")
    pair = f'<div class="pair">{md(a["pair"])}</div>' if a.get("pair") else ""
    after = a.get("after") or []
    attrs = f' data-after=\'{esc(json.dumps(after))}\'' if after else ""
    copy = f'<button type="button" class="copy-notes">{T("inquiry.copy_notes")}</button>' if after else ""
    own = (f'<label class="drew"><input type="checkbox"> <span>{T("inquiry.drew_on_paper")}</span></label>'
           f'<textarea rows="2" aria-label="{T("inquiry.draw_notes")}" placeholder="{esc(T("inquiry.draw_notes"))}"></textarea>' if draw else
           f'<textarea rows="4" aria-label="{T("inquiry.own_answer")}"></textarea>')   # the model opens once the student has written an answer (the tick "Olen tehnyt ratkaisun" removed, teacher 2026-11-06)
    model_fig = fig_of({"figure": a["model_figure"]}) if a.get("model_figure") else ""
    return (f'<div class="explain{" draw" if draw else ""}"{attrs}>{task_text(inline(md, a["prompt"]))}{fig_of(a)}{own}{pair}'
            f'<div class="choice-actions"><button type="button" class="show-model">{T("inquiry.show_model_drawing" if draw else "inquiry.show_model")}</button>{copy}</div>'
            f'<p class="explain-status" role="status" aria-live="polite"></p>'
            f'<div class="model" hidden><h4>{T("inquiry.model_drawing" if draw else "inquiry.model_answer")}</h4>{model_fig}{md(a["model"])}<h4>{T("inquiry.self_assess")}</h4>'
            f'<p class="crit-lead">{T("inquiry.self_assess_lead")}</p><ul class="criteria">{crit}</ul>'
            f'<div class="choice-actions"><button type="button" class="check-criteria">{T("inquiry.criteria_done")}</button></div>'
            f'<div class="crit-result" role="status" aria-live="polite" hidden><p class="crit-msg"></p><ul class="crit-missing"></ul>'
            f'<p class="crit-practice" hidden>{md(a["practice"]) if a.get("practice") else T("inquiry.further_practice")}</p></div></div></div>')


def question_html(q, md, lid, aid):
    t = q["type"]
    if t == "choice": return choice_html(q, md, lid, f"{aid}-q")
    if t == "numeric": return numeric_html(q, md, f"{aid}-q")
    return explain_html(q, md, f"{aid}-q")


def experiment_html(a, md, lid):
    units = a.get("units", {}); names = a.get("names", {})
    nm = lambda k: tex_name(names.get(k, k))   # the status line typesets its $…$ (inquiry.js)
    tn = lambda k: tex_name(names.get(k, k))
    fi = lambda v: str(v).replace(".", T("format.decimal")) if isinstance(v, (int, float)) else str(v)   # decimal comma on the page
    words = a.get("values", {})   # {param: {value: words}}: a select's option named in words, not by its index
    sim_words = (T(f"sims.{lid}.values") if T.has(f"sims.{lid}.values") else None) or {}
    bare = lambda k: tex_name(re.sub(r"\s+\([^()]*\)$", "", names.get(k, k)))   # "wavelength λ (nm)" -> "wavelength λ" beside a value that has its unit
    def fmt(k, v):   # name, value and unit on one line; a number and its unit are maths (teacher 2026-10-28, "kaikki LaTeXilla")
        tn = bare
        if str(v) in words.get(k, {}): return f'<span>{tn(k)}: {esc(words[k][str(v)])}</span>'   # words may wrap at 360 px ("direction of the current: downwards at the front", FY7 2026-11-04)
        if isinstance(v, str) and str(sim_words.get(v, v)) != v: v = sim_words[v]   # a sim value named in the page's language (lang sims.<id>.values), the Finnish page unchanged
        u = units.get(k, "")
        if isinstance(v, str) and re.fullmatch(r"-?\d+(?:\.\d+)?", v) and (not u or UNIT.fullmatch(u)):   # a select's number ("0.5"):
            return f'<span class="nobr">{tn(k)} = ${esc(v.replace(".", "{" + T("format.decimal") + "}"))}' + ((("" if u == "°" else "\\,") + unit_tex(u)) if u else "") + "$</span>"   # maths as written (FY4 audit 2026-11-01)
        if isinstance(v, (int, float)) and (not u or UNIT.fullmatch(u)):
            num = fi(v).replace(T("format.decimal"), "{" + T("format.decimal") + "}")
            if isinstance(v, int) and abs(v) >= 10000: num = f"{v:,}".replace(",", "\\,")   # 20\,000
            unit = (("" if u == "°" else "\\,") + unit_tex(u)) if u else ""
            return f'<span class="nobr">{tn(k)} = ${esc(num)}{unit}$</span>'
        return f'<span class="nobr">{tn(k)} = {esc(fi(v))}' + (f" {esc(u)}" if u else "") + "</span>"
    init = ", ".join(fmt(k, v) for k, v in a["initial"].items())
    locked = ", ".join(tn(k) for k in a["locked"]) or T("inquiry.nothing_locked")
    labels = [m["label"] if isinstance(m, dict) else m for m in a["measure"]]
    vary_plain = plain_label(names.get(a["vary"], a["vary"]) + (f" ({units[a['vary']]})" if units.get(a["vary"]) else ""))
    cols = "".join(f'<th data-plain="{esc(plain_label(l))}">{tex_name(l)}</th>' for l in labels)   # data-plain: the heading in the exported table
    measure = json.dumps([m["key"] if isinstance(m, dict) else m for m in a["measure"]])
    q = f'<div class="exp-question" data-min="{a.get("min", 2)}">{question_html(a["question"], md, lid, a["id"])}</div>' if a.get("question") else ""
    return (f'<div class="experiment" data-initial=\'{esc(json.dumps(a["initial"]))}\' data-locked=\'{esc(json.dumps(a["locked"]))}\' '
            f'data-vary="{esc(a["vary"])}" data-vary-name="{nm(a["vary"])}" data-locked-names=\'{esc(json.dumps([_h.unescape(tex_name(names.get(k, k))) for k in a["locked"]], ensure_ascii=False))}\' data-measure=\'{esc(measure)}\' data-min="{a.get("min", 2)}"' + (f' data-words=\'{esc(json.dumps(words, ensure_ascii=False))}\'' if words else "") + '>'
            f'<div class="intro">{md(a["intro"])}</div>'
            f'<p class="exp-setup"><strong>{T("inquiry.setup")}</strong> {init}. <strong>{T("inquiry.locked")}</strong> {locked}. <strong>{T("inquiry.varied")}</strong> {tn(a["vary"])}.</p>'
            f'<div class="exp-controls"><button type="button" class="exp-start">{T("inquiry.exp_start")}</button><button type="button" class="exp-record">{T("inquiry.exp_record")}</button>'
            f'<button type="button" class="exp-reset">{T("inquiry.exp_reset")}</button>'
            f'<button type="button" class="exp-copy" disabled>{T("inquiry.exp_copy")}</button>'
            f'<span class="exp-export-status" role="status" aria-live="polite"></span></div>'   # the table's export (teacher 2026-11-03, templates/inquiry.js part 3)
            f'<table class="exp-table"><caption>{T("inquiry.exp_table")}</caption><thead><tr><th data-plain="{esc(vary_plain)}">{tn(a["vary"])}</th>{cols}</tr></thead><tbody></tbody></table>'
            f'<p class="exp-status" role="status" aria-live="polite"></p>{q}</div>')


def sim_parts(a, md):
    """(visible lead, closed boxes) of the sim activity. The page shows the picture, the controls and the values first;
    the lead is one or two sentences and the longer texts sit behind Käyttöohje, Mallin oletukset and Laskennan
    selitys. A long text written before 2026-10-26 without those fields goes behind one box (LEGACY_INFO)."""
    text = a.get("text") or ""
    boxes = [(title, a[k]) for k, title in sim_info() if a.get(k)]
    if text and not boxes and len(text.split()) > LEAD_WORDS: boxes, text = [(legacy_info(), text)], ""
    info = "".join(f'<details class="sim-box"><summary>{t}</summary><div>{md(x)}</div></details>' for t, x in boxes)
    return (md(text) if text else ""), (f'<div class="sim-info">{info}</div>' if info else "")


def prior_html(item, md):
    """One Pohjatiedot item: the fact, and the chapter it comes from as a quiet link ("(luku <title>)" in inquiry.json
    -> a link to that lesson when it is in the curriculum; CLAUDE.md "Chapter names, not ids")."""
    h = inline(md, item)
    m = re.search(r"\s*\(" + re.escape(T("inquiry.prior_chapter")) + r"\s+(?:<em>)?(.+?)(?:</em>)?\)\s*\.?$", h)
    if not m: return f"<li>{h}</li>"
    title = _h.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
    href = chapter_href(title)
    ref = f'<a href="{href}">{esc(title)}</a>' if href else f"<em>{esc(title)}</em>"
    return f'<li>{h[:m.start()].rstrip(" .;")}<span class="prior-ref">{T("inquiry.prior_chapter")} {ref}</span></li>'


def chapter_href(title):
    """The page of the lesson with this title (curriculum.json), or None."""
    try:
        import courses
        for code, mod in courses.curriculum().items():
            if code.startswith("_"): continue
            for l in mod.get("lessons", []):
                full = l.get("title", "").strip().lower()
                if title.lower() in (full, full.split(":")[0].strip()):   # "Aineen lämpeneminen ja jäähtyminen: Q = cmΔT"
                    try: courses.find_lesson(l["id"])
                    except SystemExit: return None
                    return f'{l["id"]}.html'
    except Exception: return None
    return None


def intro_html(intro, inquiry, n_opt, md):
    """The opening (teacher 2026-10-27): the title and the Miksi question first, across the reading column; under them
    the chapter's illustration and "Tällä tunnilla opit" (2–3 goals) side by side, both starting at the same height and
    about as tall (.intro-row); then "Pohjatiedot" as a list and the core path in one quiet line (.intro-more). One
    column on a phone: title, question, illustration, goals, prior knowledge."""
    m = re.search(r"<p>\s*<svg\b", intro)
    head, media = (intro[:m.start()], intro[m.start():]) if m else (intro, "")
    learn = inquiry.get("learn")
    goals = ("<ul>" + "".join(f"<li>{inline(md, x)}</li>" for x in learn) + "</ul>") if learn else f'<p>{inline(md, inquiry["contribution"])}</p>'
    deepen = inquiry.get("deepen")
    goals += (f'<h2 class="intro-h deepen-h">{T("inquiry.deepen")}</h2><ul class="deepen">' + "".join(f"<li>{inline(md, x)}</li>" for x in deepen) + "</ul>") if deepen else ""
    aside = f'<div class="learn"><h2 class="intro-h">{T("inquiry.learn")}</h2>{goals}</div>'
    prior = inquiry.get("prior") or []
    more = f'<div class="prior"><h2 class="intro-h">{T("inquiry.prior")}</h2><ul>' + "".join(prior_html(x, md) for x in prior) + "</ul></div>" if prior else ""
    if n_opt: more += f'<p class="path-note">{T("inquiry.core_path", n=n_opt)}</p>'   # what is the path, what may be left (spec 2026-10-26)
    row = (f'<div class="intro-row' + ("" if media else " no-media") + '">' + (f'<div class="intro-media">{media}</div>' if media else "")
           + f'<aside class="intro-aside">{aside}</aside></div>')
    return f'<div class="intro"><div class="intro-head">{head}</div>{row}' + (f'<div class="intro-more">{more}</div>' if more else "") + '</div>'


KEY_CONCEPTS = (3, 5)    # how many "Luvun tärkeät käsitteet" a Selkeä suomi lesson shows (teacher 2026-11-03)


def key_concepts_html(lid, items, md):
    """"Luvun tärkeät käsitteet" (teacher 2026-11-03, NOTES.md §12): the S2 vocabulary activity of a Selkeä suomi
    lesson, between the opening and the first stage. meta.json "key_concepts" lists 3–5 {"term", "explain"}: the
    Finnish physics term in bold and a short plain-Finnish explanation. The student writes the meanings in a notebook
    in any language (teacher 2026-11-03: no note fields on the page). Voluntary and never assessed; no language is
    asked or translated. Only a language whose lessons carry the list shows it (check_i18n.py: fi-easy only)."""
    if not items: return ""
    rows = []
    for k in items:
        term = k["term"][:1].upper() + k["term"][1:]   # a symbol in the term is LaTeX: "$(t,x)$-kuvaaja"
        rows.append(f'<dt class="kc-term">{inline(md, term)}</dt><dd class="kc-explain">{inline(md, k["explain"])}</dd>')
    return (f'<section class="kc" id="kasitteet" aria-labelledby="kc-{lid}-h"><h2 class="intro-h kc-h" id="kc-{lid}-h">{T("lesson.kc_title")} '
            f'<span class="opt-tag">{T("lesson.kc_optional")}</span></h2><p class="kc-lead">{T("lesson.kc_lead")}</p>'
            f'<dl class="kc-list">{"".join(rows)}</dl></section>')


SENT = re.compile(r"(?<=[.!])\s+(?=[A-ZÅÄÖ])")


def split_prompt(html, words=28):
    """A long task text as the situation and the question asked (teacher 2026-10-27, "tehtäväkortit"): the sentences
    from the first one that asks something ("?") on are the question (.ask), the ones before it the situation
    (.scenario). The text is not changed, only given a paragraph break; maths and tags are never cut, and a text
    without a clear question, or a short one, stays whole."""
    plain = re.sub(r"<[^>]+>|\$[^$]*\$", "", html)
    if len(plain.split()) < words: return None
    stash = []
    safe = re.sub(r"\$[^$]*\$|<[^>]+>", lambda m: (stash.append(m.group(0)), f"\x00{len(stash) - 1}\x00")[1], html)
    cuts = [m.end() for m in SENT.finditer(safe)]
    q = safe.find("?")
    if q < 0: return None
    before = [c for c in cuts if c <= q]
    if not before: return None
    cut = before[-1]
    back = lambda t: re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], t).strip()
    a, b = back(safe[:cut]), back(safe[cut:])
    if a.count("<") != a.count(">") or re.search(r"<(\w+)[^>]*>(?:(?!</\1>).)*$", a, re.S): return None   # an element open across the cut
    return a, b


def legend_html(html):
    """A choice's prompt in its legend (the group's accessible name), split like task_text into two blocks."""
    sp = split_prompt(html)
    return f'<span class="scenario">{sp[0]}</span><span class="ask">{sp[1]}</span>' if sp else html


def task_text(html, cls="task", pid=None):
    """A task's prompt as <p class="task">, or as the situation and the question when it is long (split_prompt).
    pid: an id on the question, so that an answer field can be described by it (aria-describedby)."""
    sp = split_prompt(html); idattr = f' id="{esc(pid)}"' if pid else ""
    if not sp: return f'<p class="{cls}"{idattr}>{html}</p>'
    return f'<p class="{cls} scenario">{sp[0]}</p><p class="{cls} ask"{idattr}>{sp[1]}</p>'


EXAMPLE_NAMES = ROOT / "example-names.json"   # short names of the worked examples (teacher 2026-11-06), outside the lessons: no review goes stale
GENERIC_TITLES = {"käsite", "laskeminen", "laskenta", "laskutehtävä", "selitä", "concept", "calculation", "calculating",
                  "calculation exercise", "explain"}   # a check's title that only names its kind: the kind's name replaces it


def example_name(lid):
    """The worked example's short name in the language being built ("Paineen nollakohta"); Selkeä suomi and a
    language without its own names show the Finnish one, a lesson without one ""."""
    names = json.loads(EXAMPLE_NAMES.read_text()) if EXAMPLE_NAMES.is_file() else {}
    lang = T.lang if T.lang in names else "fi"
    return names.get(lang, {}).get(lid) or names.get("fi", {}).get(lid, "")


def extension_kind(title):
    """"Syventävä" or "Lisätiedoksi" (lang inquiry.extension, inquiry.further) when an optional box's title starts
    with it, else None. LOPS 2019 extension material (teacher 2026-11-07): the box's tag names it, not Valinnainen."""
    m = re.match(r"\s*([^:]+?)\s*:", title or "")
    return m.group(1) if m and m.group(1) in (T("inquiry.extension"), T("inquiry.further")) else None


def task_titles(lid, by_stage, md):
    """{activity id: shown title} for the boxes of Esimerkit and Itsearvio (teacher 2026-11-06).
    Esimerkit: every box is a guided example, "Esimerkki 1: Paineen nollakohta", "Esimerkki 2: Etsi virhe", numbered
    in page order (the worked example by its name in example-names.json). Itsearvio: each task named by its kind
    (Käsitetehtävä, Laskutehtävä, Selitystehtävä; the exit ticket is Pohdintatehtävä, lang lesson.exit_ticket), its own name after a colon unless it only names
    the kind, numbered on the page from the exit ticket on ("1. Pohdintatehtävä", "2. Käsitetehtävä",
    "3. Laskutehtävä: Lämpötilan kasvu"; teacher 2026-11-06), whatever number the title carries."""
    out, n, k = {}, 0, 0
    is_worked = lambda a: a["type"] == "theory" and "Esimerkki" in a.get("sections", ())
    for a in by_stage["sovella"] if any(map(is_worked, by_stage["sovella"])) else ():   # a unit's tasks without a worked example (FY9) stay tasks
        t = a["type"]
        worked = is_worked(a)
        if not (worked or t in CARD_TYPES or (t == "theory" and a.get("title"))): continue
        n += 1
        name = inline(md, example_name(lid)) if worked else esc(re.sub(r"^(?:Valinnainen|Optional)\s*:\s*", "", a.get("title") or T(f"inquiry.optional_{t}")))
        kind = extension_kind(a.get("title")) if a.get("optional") and not worked else None
        if kind: name = esc(a["title"].split(":", 1)[1].strip())   # the box's tag says Syventävä / Lisätiedoksi
        name = name[:1].upper() + name[1:]
        out[a["id"]] = T("inquiry.example_n", n=n) + (f": {name}" if name else "")
    for a in by_stage["tarkista"]:
        t = a["type"]
        if t == "exit": k += 1; out[a["id"]] = f"{k}. {exit_title()}"; continue   # "1. Pohdintatehtävä", then the checks 2, 3 … (teacher 2026-11-06)
        if not T.has(f"inquiry.task_{t}"): continue
        k += 1
        m = re.match(r"\s*(\d+\.)?\s*(.*)$", a.get("title", ""))
        own = m.group(2).strip()
        p = re.match(r"([^:]+):\s*(\S.*)$", own)
        if p and p.group(1).casefold() in GENERIC_TITLES: own = p.group(2)[:1].upper() + p.group(2)[1:]   # "Concept: what the bounces showed"
        own = "" if own.casefold() in GENERIC_TITLES or own.casefold() == T(f"inquiry.task_{t}").casefold() else own
        out[a["id"]] = f"{k}. " + T(f"inquiry.task_{t}") + (f": {esc(own)}" if own else "")   # the number of the page, not the one in the title
    return out


TUTKI_FOLD_COURSES = {f"FY{i}" for i in range(1, 10)}   # the modules whose Tutki shows one investigation at first
TUTKI_VISIBLE = 2                                  # at most this many tasks of Tutki in view (teacher 2026-11-06)


def tutki_split(items):
    """(shown, folded) for the Tutki stage. Teacher 2026-11-06: "Tutki-osuudessa saisi olla maksimissaan kaksi
    kysymystä" — too many questions in view hide the whole. The simulation stays as it is; of the tasks only the first
    one (the first clear, easy investigation, usually Koe 1) stays in view, and a core task (Ydintehtävä) as the second
    one at most. The rest, in their own order, go into one closed box "Lisää tutkittavaa" after them; links to them
    (#exp-2) open it (lesson.js openTo)."""
    tasks = [a for a in items if a["type"] != "sim"]
    first = next((a for a in tasks if not a.get("optional")), tasks[0] if tasks else None)
    keep = [first] if first else []
    keep += [a for a in tasks if a is not first and a.get("core") and not a.get("optional")][:TUTKI_VISIBLE - len(keep)]
    if len(tasks) <= 1: return items, []
    return [a for a in items if a["type"] == "sim" or any(a is k for k in keep)], [a for a in tasks if not any(a is k for k in keep)]


def toc_link(sid, n, title):
    """A stage in the navigation: its number (as on the stage heading) and its name. The chip bar shows the short name
    (NAV); a wide window shows the rest of the title too ("Tarkista osaamisesi", .toc-rest)."""
    short = nav().get(sid, title)
    rest = title[len(short):] if title.startswith(short) else ""
    return (f'<a href="#{sid}"><span class="toc-no" aria-hidden="true">{n}</span><span class="toc-label">{short}'
            + (f'<span class="toc-rest">{rest}</span>' if rest else "") + '</span></a>')


SA_LEVELS = ("d", "c", "b", "a", "x")   # reddish on the left, dark green on the right (teacher 2026-11-06 evening); guided self-assessment (teacher 2026-11-06, his 2018 team sheet): five levels, shown as a
# colour scale from a reddish tone to Ruukkilabra green and a grey "not yet" (teacher 2026-11-06: no letters); the
# letters are only the values in the submission file


def sa_fieldset(chapter, sid, label, md_label, legend):
    """One self-assessment row of Tarkista osaamisesi (teacher 2026-11-06): the five levels as radio buttons, the
    chosen level's description under them (inquiry.js part 8). sid: the item's id in the submission file
    (an activity id, or "tavoite-<n>"); label: the item's plain text for the teacher's grading view."""
    opts = "".join(f'<label class="sa-opt" data-level="{v}" title="{esc(T("inquiry.sa_" + v))}"><input type="radio" name="sa-{esc(sid)}" value="{v}">'
                   f'<span class="sa-sw" aria-hidden="true">{T("inquiry.sa_x_short") if v == "x" else ""}</span><span class="sa-text">{T("inquiry.sa_" + v)}</span></label>' for v in SA_LEVELS)
    return (f'<fieldset class="sa-rate" data-chapter="{esc(chapter)}" data-sa="{esc(sid)}" data-label="{esc(label)}">'
            f'<legend>{md_label if md_label else legend}</legend><div class="sa-opts">{opts}</div><p class="sa-desc" aria-live="polite"></p></fieldset>')


def self_statements(chapter, lang):
    """The chapter's closing statements from itsearvio/<lang>.json (teacher 2026-11-06: varied, "Osaan …", "Ymmärrän …",
    "Tunnistan …", like his 2018 sheet, not every goal as "Opin …"); Selkeä suomi uses the Finnish ones. Kept apart
    from inquiry.json so that writing them never stales a lesson's reviews."""
    for l in dict.fromkeys([lang, "fi" if lang == "fi-easy" else lang]):
        f = courses.ROOT / "itsearvio" / f"{l}.json"
        if f.is_file():
            got = json.loads(f.read_text()).get(chapter)
            if got: return got
    return None


def sa_goals_html(chapter, inquiry, md, lang):
    """The start of Itsearvio (teacher 2026-11-06: goals first, then the tasks): the chapter's goals as statements ("Opin erottamaan painon ja massan"), or the
    chapter's own statements of what the tasks did not measure (inquiry.json "self_extra"), on the same scale."""
    extra = inquiry.get("self_extra") or self_statements(chapter, lang)
    items = [(f"tavoite-{i + 1}", x) for i, x in enumerate(extra)] if extra else [(f"tavoite-{i + 1}", T("inquiry.sa_goal_prefix") + " " + x) for i, x in enumerate(inquiry.get("learn") or [])]
    if not items: return ""
    rows = "".join(sa_fieldset(chapter, sid, plain(x), f'<span class="sa-n">{i + 1}.</span> <span class="sa-statement">{inline(md, x)}</span>', "")
                   for i, (sid, x) in enumerate(items))   # numbered (teacher 2026-11-06)
    return (f'<div class="activity act-selfgoals task-card" id="itsearvio-tavoitteet" data-type="selfgoals"><h3>{T("inquiry.sa_goals_title")}</h3>'
            f'<p class="sa-lead">{T("inquiry.sa_goals_lead")}</p>{rows}</div>')


def plain(text):
    """Plain text of a Markdown line for a data attribute: the formulas keep their LaTeX, the marks go."""
    return re.sub(r"\s+", " ", re.sub(r"[*_`]", "", text)).strip()

def render(folder, inquiry, parts, md):
    """(body html, toc html). parts: {'intro': html, 'sections': {key: html}, 'sim': html (with a <!--sim-info--> slot),
    'exercises': html, 'exit': html}.

    Order: the stages in STAGES order (empty ones left out), then the exercises in their own section "Tehtävät", last
    on the page whatever stage inquiry.json gives them. Layout hooks for templates/site.css, all single-column on a
    phone: the title and the Miksi question, then the illustration beside the lesson's goals and prior knowledge
    (intro_html); every task in one reading column, never two side by side (flow); the stage that holds the simulation as a .lab (the sim beside the
    experiments that use it); the Ennusta stage inside a <details class="fold"> that starts closed and keeps its answers
    when closed; a theory figure beside its paragraph (build.py fig_rows); each CARD_TYPES task as one .task-card that
    holds its heading, instructions, answers and feedback (the three levels of the page: stage, task, what is inside a
    task; teacher's brief 2026-10-27)."""
    lid = folder.name
    acts = inquiry["activities"]
    by_stage = {s: [] for s in STAGE_IDS}
    ex_act = None
    for a in acts:
        if a["type"] == "exercises": ex_act = a; continue
        by_stage[a["stage"]].append(a)
    by_stage["tarkista"].sort(key=lambda a: a["type"] != "exit")   # the exit ticket opens Tarkista osaamisesi, before the checks (teacher 2026-11-04)
    placed = {s for a in acts if a["type"] == "theory" for s in a["sections"]}
    leftover = [s for s in parts["sections"] if s not in placed]
    required = [a for a in by_stage["selita"] if a["type"] == "theory" and not a.get("optional")]
    if leftover and not required:
        by_stage["selita"].append({"id": "theory-rest", "type": "theory", "stage": "selita", "sections": leftover})
    elif leftover:                                     # append to the last required theory activity in Teoriatiivistelmä,
        last = required[-1]; last["sections"] = list(last["sections"]) + leftover   # never into a closed optional box
    body = [intro_html(parts["intro"], inquiry, sum(1 for a in acts if a.get("optional")), md) + parts.get("concepts", "")]

    shown = task_titles(lid, by_stage, md)

    def act(a):
        t, aid = a["type"], a["id"]
        head = f'<h3>{shown[aid] if aid in shown else esc(a["title"])}</h3>' if (a.get("title") or aid in shown) and t != "exit" else ""
        if a.get("core") and not a.get("optional"):   # a task of the lesson on the core path, tagged like a core exercise (teacher 2026-11-05)
            head = f'<p class="act-core"><span class="ex-core">{T("lesson.core_exercise")}</span></p>' + head
        if t == "hook": content = f'<div class="hook">{md(a["text"])}{fig_of(a)}</div>' + (f'<p class="question">{inline(md, a["question"])}</p>' if a.get("question") else "")
        elif t == "text": content = md(a["text"]) + fig_of(a)
        elif t == "choice": content = choice_html(a, md, lid, aid)
        elif t == "numeric": content = numeric_html(a, md, aid)
        elif t == "explain": content = explain_html(a, md, aid)
        elif t == "reflect":
            content = (f'<div class="reflect" data-predictions=\'{esc(json.dumps(a["predictions"]))}\'><p class="task">{inline(md, a["prompt"])}</p>'
                       f'<ul class="my-predictions"></ul><p class="revise"><strong>{T("inquiry.revise")}</strong> '
                       f'<label><input type="radio" name="{esc(aid)}-rev" value="ei"> {T("inquiry.revise_no")}</label> <label><input type="radio" name="{esc(aid)}-rev" value="kylla"> {T("inquiry.revise_yes")}</label></p>'
                       f'<textarea rows="3" aria-label="{T("inquiry.why")}" placeholder="{T("inquiry.why")}"></textarea></div>')
        elif t == "experiment": content = experiment_html(a, md, lid)
        elif t == "interpret":
            src = a.get("source")
            badge = (f'<p class="source" data-source="{src}"><strong>{T("inquiry.source_" + src)}</strong>' + (f' · {inline(md, a["source_note"])}' if a.get("source_note") else "") + '</p>') if src else ""
            content = f'<div class="interpret">{badge}<div class="representation">{md(a["text"])}{fig_of(a)}</div>{question_html(a["question"], md, lid, aid) if a.get("question") else ""}</div>'
        elif t == "theory":
            content = "".join(parts["sections"][s] for s in a["sections"])
            if aid in shown and "Esimerkki" in a["sections"]:   # the box itself says "Esimerkki 1: <name>"; no heading above it (teacher 2026-11-06)
                ex = parts["sections"]["Esimerkki"]
                if '<p class="example-label">' in ex:
                    new = re.sub(r'^<h3 class="theory-h">.*?</h3>', "", ex, count=1)
                    new = re.sub(r'<p class="example-label">.*?</p>', f'<h3 class="example-title">{shown[aid]}</h3>', new, count=1)
                else: new = re.sub(r'^<h3 class="theory-h">.*?</h3>', f'<h3 class="theory-h">{shown[aid]}</h3>', ex, count=1)
                content = content.replace(ex, new, 1)
                head = ""
        elif t == "sim":
            lead, info = sim_parts(a, md)
            content = parts["sim"].replace("<!--sim-info-->", info + (f'<div class="sim-lead">{lead}</div>' if lead else ""))   # the lead under the boxes, at the card's foot (teacher 2026-11-06)
        elif t == "exit":
            content = parts["exit"].replace("</h3>", "</h3>" + md(T("inquiry.exit_lead")), 1)
            if aid in shown: content = content.replace(f"<h3>{exit_title()}</h3>", f"<h3>{shown[aid]}</h3>", 1)   # "1. Pohdintatehtävä"
        else: content = ""
        if t in ("choice", "numeric") and a.get("stage") == "tarkista":   # after a wrong check: a suggestion where to practise, never a verdict (teacher 2026-10-29)
            hint = f'<p class="practice-hint" role="note">{inline(md, a["practice"]) if a.get("practice") else T("inquiry.check_practice")}</p>'
            content = content.replace("<output aria-live=\"polite\"></output></fieldset>", f'<output aria-live="polite"></output>{hint}</fieldset>') if t == "choice" else content[:-len("</div>")] + hint + "</div>"
        hints = hints_html([md(mathlayout.display_chains(h)) for h in a.get("hints", [])]) if t not in ("numeric",) else ""
        sa = ""
        if parts.get("selfassess") and a.get("stage") == "tarkista" and t in ("choice", "numeric", "explain", "exit"):   # every task of Tarkista osaamisesi (teacher 2026-11-06)
            sa = sa_fieldset(lid, aid, plain(_h.unescape(shown.get(aid) or "") or a.get("title") or exit_title()), "", T("inquiry.sa_legend"))   # one plain question (teacher 2026-11-06)
        hints += sa
        if a.get("optional") or a.get("fold") or t == "reflect":   # a closed box, named, that a student may open or leave; "fold": a
            name = shown.get(aid) or esc(a.get("title") or T(f"inquiry.optional_{t}"))   # required part opened later (its own tag, e.g. "Lesson 2");
            name = name[:1].upper() + name[1:]          # Palaa ennusteisiisi: closed until opened, required or not (teacher 2026-11-06)
            tag = esc(a["fold"]) if a.get("fold") else T("inquiry.optional") if a.get("optional") else ""
            kind = extension_kind(a.get("title")) if a.get("optional") else None   # "Syventävä: …", "Lisätiedoksi: …" name the box's kind instead of Valinnainen (teacher 2026-11-07)
            if kind:
                tag, name = esc(kind), re.sub(rf"(^|:\s*){re.escape(esc(kind))}\s*:\s*(\S)", lambda m: m.group(1) + m.group(2).upper(), name, count=1)
            return (f'<details class="opt{" fold" if a.get("fold") else ""}" data-type="{t}"><summary>' + (f'<span class="opt-tag">{tag}</span> ' if tag else "") + f'{name}</summary>'
                    f'<div class="activity act-{t}" id="{esc(aid)}" data-type="{t}">{content}{hints}</div></details>')
        card = " task-card" if t in CARD_TYPES else ""
        return f'<div class="activity act-{t}{card}" id="{esc(aid)}" data-type="{t}">{head}{content}{hints}</div>'

    def flow(items):
        """The activities one under another in the reading column. Tasks never sit side by side: a card grows when
        its feedback, hints, solution or model answer opens, and beside it the other column would be left with a
        tall empty space and the next task pushed far down (teacher 2026-10-27, "avautuvat kortit")."""
        return "".join(act(a) for a in items)

    toc, n, last = [], 0, None
    cards_at = next((s for s in ("sovella", "tarkista", "selita") if by_stage[s]), None) if parts.get("cards") else None
    for sid, title in stages():
        items = by_stage[sid]
        if not items: continue
        n += 1
        si = next((i for i, a in enumerate(items) if a["type"] == "sim"), None)
        more = ""
        if sid == "tutki" and folder.parent.name in TUTKI_FOLD_COURSES:
            items, rest = tutki_split(items)
            si = next((i for i, a in enumerate(items) if a["type"] == "sim"), None)
            if rest:                                   # the rest of the investigation behind one closed box (teacher 2026-11-06)
                k = len(rest)
                more = (f'<details class="fold more" data-fold="tutki-more"><summary><span class="fold-title">{T("inquiry.more_title")}</span> '
                        f'<span class="more-count" data-one="{esc(T("inquiry.more_count_one"))}" data-many="{esc(T("inquiry.more_count_many"))}">{T("inquiry.more_count_one" if k == 1 else "inquiry.more_count_many", n=k)}</span></summary>'
                        f'<div class="fold-body">{flow(rest)}</div></details>')
        if si is not None and (si < len(items) - 1 or more):   # the sim beside the activities that use it
            inner = (flow(items[:si]) + f'<div class="lab"><div class="lab-side">{act(items[si])}</div>'
                     f'<div class="lab-main">{flow(items[si + 1:])}{more}</div></div>')
        else: inner = flow(items) + more
        if sid == "tarkista" and parts.get("selfassess"):   # the goals first, then the tasks with their own ratings (teacher 2026-11-06 evening)
            inner = sa_goals_html(lid, inquiry, md, courses.lang_of(folder)) + inner   # no separate key: the chosen level's text shows under the scale (teacher 2026-11-06)
        if sid == cards_at: inner += parts["cards"]       # the chapter's concept cards close Esimerkit (teacher 2026-11-05)
        if sid == "ennusta":                           # closed at first; reopened later, the answers are still there
            k = sum(1 for a in items if a["type"] == "choice")
            inner = (f'<details class="fold" data-fold="{sid}"><summary><span class="fold-title">{T("inquiry.fold_title")}</span> '
                     f'<span class="fold-status" data-n="{k}">{T("inquiry.fold_question_one" if k == 1 else "inquiry.fold_question_many", n=k)}</span></summary>'
                     f'<div class="fold-body">{inner}</div></details>')
        lead = f'<p class="stage-lead">{T(f"inquiry.lead_{sid}")}</p>' if T.has(f"inquiry.lead_{sid}") else ""   # what the stage is for (teacher 2026-11-05)
        if sid == "tarkista" and parts.get("exercises"):   # Itsearvio closes the page, after the exercises (teacher 2026-11-06 evening)
            n -= 1; last = (sid, title, lead, inner); continue   # numbered after Tehtävät, so the bar reads 1, 2, 3 … in order
        body.append(f'<section class="stage" id="{sid}" data-stage="{sid}"><h2><span class="stage-no" aria-hidden="true">{n}</span>{title}</h2>{lead}{inner}</section>')
        toc.append(toc_link(sid, n, title))
    if parts.get("exercises"):                         # the exercises after the lesson's stages, before Itsearvio
        text = ""                                      # the exercises' own lead text is not shown (teacher 2026-11-04: "turhia")
        aid = ex_act["id"] if ex_act else "harjoitukset"
        n += 1                                         # Tehtävät is a stage like the others: numbered, ticked when its core tasks are answered (teacher 2026-11-06)
        body.append(f'<section class="stage stage-practice" id="exercises" data-stage="exercises"><h2><span class="stage-no" aria-hidden="true">{n}</span>{exercises_title()}</h2>'
                    f'<div class="activity act-exercises" id="{esc(aid)}" data-type="exercises">{text}{parts["exercises"]}</div></section>')
        toc.append(toc_link("exercises", n, exercises_title()))
    if last:
        sid, title, lead, inner = last; n += 1
        body.append(f'<section class="stage" id="{sid}" data-stage="{sid}"><h2><span class="stage-no" aria-hidden="true">{n}</span>{title}</h2>{lead}{inner}</section>')
        toc.append(toc_link(sid, n, title))
    return current_stage_names("\n".join(body)), "".join(toc)


if __name__ == "__main__":
    if len(sys.argv) != 2: sys.exit(__doc__)
    lid = sys.argv[1]
    import courses
    folder = courses.find_lesson(lid)
    inq = load(folder)
    if inq is None: sys.exit(f"{lid}: no inquiry.json (the lesson renders in the classic layout)")
    errs = validate(folder, inq, (folder / "lesson.md").read_text())
    print("\n".join(errs) if errs else f"{lid} inquiry.json: valid ({len(inq['activities'])} activities)")
    sys.exit(1 if errs else 0)
