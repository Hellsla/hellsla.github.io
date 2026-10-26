"""Inquiry-based lesson structure: validation and rendering of content/<course>/<id>/inquiry.json (format version 1).

A lesson with inquiry.json is rendered as stages — Pohdinta → Ennusta → Tutki → Teoriatiivistelmä → Sovella →
Tarkista osaamisesi — each holding activities; stages may repeat, be omitted, or hold the lesson's existing
parts (theory sections of lesson.md, the simulation, the exit ticket). The exercises always come last, after the
exit ticket, in their own section "Tehtävät". A lesson without the file renders in the classic layout. See
docs/inquiry.md for the format and docs/inquiry-spec.md for the pedagogy it serves; the page layout (human
decisions 2026-10-26, CLAUDE.md "Lesson page") is in render() and templates/site.css.

  python scripts/inquiry.py <id>     validate one lesson's inquiry.json and print the errors (exit 1 on any)
"""
import hashlib, html as _h, json, pathlib, random, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
VERSION = 1
STAGES = [("herata", "Pohdinta"), ("ennusta", "Ennusta"), ("tutki", "Tutki"),
          ("selita", "Teoriatiivistelmä"), ("sovella", "Sovella"), ("tarkista", "Tarkista osaamisesi")]   # ids are keys in inquiry.json, titles are what the student sees
STAGE_IDS = [s for s, _ in STAGES]
NAV = {"tarkista": "Tarkista"}                    # nav label when it differs from the stage title
EXIT_TITLE, EXERCISES_TITLE = "Exit ticket", "Tehtävät"
SIM_INFO = (("howto", "Käyttöohje"), ("model", "Mallin oletukset"), ("calc", "Laskennan selitys"))   # the sim activity's boxes, closed by default
LEGACY_INFO = "Käyttöohje ja mallin oletukset"    # a long sim text written before 2026-10-26, shown behind one box
LEAD_WORDS = 30                                   # a sim activity's visible lead is at most this long
GRID_TYPES = ("hook", "choice", "numeric", "explain", "exit")   # consecutive ones sit side by side on a wide screen
TYPES = ("hook", "text", "choice", "experiment", "interpret", "numeric", "explain", "reflect", "theory", "sim", "exercises", "exit")
QUESTION_TYPES = ("choice", "numeric", "explain")
ID_RE = re.compile(r"^[a-z][a-z0-9-]{1,40}$")
RESERVED_IDS = {"sim", "sim-root", "exercises", "exit", "teoria", "herata", "ennusta", "tutki", "selita", "sovella", "tarkista"}   # ids the page already uses


def heading(title):
    """(key, shown) of a lesson.md `## ` heading. The formula section is named after its law, `## Kaava: Lämpömäärä`:
    the page shows "Lämpömäärä", while inquiry.json, the lint and the build keep using the key "Kaava"."""
    m = re.match(r"(Kaava):\s*(\S.*)$", title.strip())
    return (m.group(1), m.group(2).strip()) if m else (title.strip(), title.strip())


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
        if not any(c.get("correct") for c in ch if isinstance(c, dict)): errs.append(f"{path}.choices: one choice must have \"correct\": true")
        texts = [("prompt", a.get("prompt"))] + [(f"choices[{i}].{k}", c.get(k)) for i, c in enumerate(ch) if isinstance(c, dict) for k in ("text", "feedback")]
        for where, t in texts:
            m = POSITIONAL.search(t) if isinstance(t, str) else None
            if m: errs.append(f"{path}.{where}: \"{m.group(0)}\" points at an option by its letter or place, but options are shown shuffled; name the option by its content")
    r = a.get("reveal")
    if r is not None:
        if not isinstance(r, dict) or not isinstance(r.get("after"), str): errs.append(f"{path}.reveal: {{\"after\": \"<experiment id>\", \"min\": n}}")
        elif "min" in r and (not isinstance(r["min"], int) or r["min"] < 1): errs.append(f"{path}.reveal.min: a positive integer")
    if "justify" in a and not isinstance(a["justify"], bool): errs.append(f"{path}.justify: true or false")
    if a.get("layout") not in (None, "list", "models"): errs.append(f"{path}.layout: \"list\" or \"models\"")


def _check_numeric(a, path, errs):
    if not isinstance(a.get("prompt"), str): errs.append(f"{path}.prompt: a string is required")
    if not isinstance(a.get("answer"), (int, float)) or isinstance(a.get("answer"), bool): errs.append(f"{path}.answer: a number is required")
    if not isinstance(a.get("unit", ""), str): errs.append(f"{path}.unit: a string")
    tol = a.get("tolerance", 0.02)
    if not isinstance(tol, (int, float)) or tol <= 0: errs.append(f"{path}.tolerance: a positive number (relative)")
    for i, m in enumerate(a.get("mistakes", []) or []):
        if not isinstance(m, dict) or not isinstance(m.get("value"), (int, float)) or not isinstance(m.get("feedback"), str):
            errs.append(f"{path}.mistakes[{i}]: {{\"value\": number, \"feedback\": text}}")


def _check_explain(a, path, errs):
    if not isinstance(a.get("prompt"), str): errs.append(f"{path}.prompt: a string is required")
    if not isinstance(a.get("criteria"), list) or not a["criteria"] or not all(isinstance(c, str) for c in a["criteria"]):
        errs.append(f"{path}.criteria: a non-empty list of self-assessment criteria")
    if not isinstance(a.get("model"), str) or not a["model"].strip(): errs.append(f"{path}.model: a model answer is required")


def validate(folder, inquiry, lesson_md):
    """Errors as strings naming the lesson, the file and the field. Empty list when valid."""
    lid = folder.name; errs = []
    E = lambda m: errs.append(f"{lid} inquiry.json: {m}")
    if not isinstance(inquiry, dict): return [f"{lid} inquiry.json: the top level must be an object"]
    if inquiry.get("version") != VERSION: E(f"version: must be {VERSION}")
    if not isinstance(inquiry.get("contribution"), str) or not inquiry["contribution"].strip(): E("contribution: one sentence on what this lesson adds that earlier lessons did not")
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
        if t in ("experiment", "interpret") and "question" in a:
            q = a["question"]
            if not isinstance(q, dict) or q.get("type") not in QUESTION_TYPES: errs.append(f"{path}.question.type: one of {', '.join(QUESTION_TYPES)}")
            else: {"choice": _check_choice, "numeric": _check_numeric, "explain": _check_explain}[q["type"]](q, f"{path}.question", errs)
    for i, a in enumerate(acts):                      # references
        if not isinstance(a, dict): continue
        r = a.get("reveal") if a.get("type") == "choice" else None
        if isinstance(r, dict) and isinstance(r.get("after"), str) and r["after"] not in exp_ids: E(f"activities[{i}].reveal.after: \"{r['after']}\" is not an experiment id")
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


def inline(md, text):
    """Markdown rendered without the outer <p>, for a choice, a legend or a prompt that sits inside another block."""
    h = md(text).strip()
    m = re.fullmatch(r"<p>(.*)</p>", h, flags=re.S)
    return m.group(1) if m else h


def hints_html(hints):
    if not hints: return ""
    names = ["Vihje 1: ohjaava kysymys", "Vihje 2: mikä yhteys", "Vihje 3: välivaihe"]
    return '<div class="hints">' + "".join(f'<details class="hint" data-n="{i + 1}"><summary>{names[i]}</summary><div>{h}</div></details>'
                                           for i, h in enumerate(hints)) + "</div>"


_NO_ERROR = re.compile(r"\s*(Laskussa|Päättelyssä) ei ole virhettä")


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
    rest = [c for c in choices if not _NO_ERROR.match(c["text"])]
    random.Random(hashlib.sha256((f"{lid}:{aid}" + (f":{salt}" if salt else "")).encode()).hexdigest()).shuffle(rest)
    return rest + [c for c in choices if _NO_ERROR.match(c["text"])]


def choice_html(a, md, lid, aid):
    opts = ""
    for i, c in enumerate(choice_order(a["choices"], lid, aid)):
        opts += (f'<li><label><input type="radio" name="{esc(aid)}" value="{i}" data-correct="{"1" if c.get("correct") else "0"}">'
                 f'<span>{inline(md, c["text"])}</span></label><div class="feedback" data-for="{i}" hidden>{md(c["feedback"])}</div></li>')
    reveal = a.get("reveal") or {}
    attrs = f' data-reveal="{esc(reveal["after"])}" data-reveal-min="{reveal.get("min", 1)}"' if reveal else ""
    justify = ('<label class="justify">Perustelu (valinnainen)<textarea rows="2"></textarea></label>' if a.get("justify") else "")
    sol = f'<div class="solution-text">{md(a["solution"])}</div>' if a.get("solution") else ""
    pending = '<p class="pending" tabindex="-1" hidden>Ennusteesi on tallessa. Palaute näkyy, kun olet tehnyt mittaukset.</p>' if reveal else ""
    return (f'<fieldset class="choice {esc(a.get("layout", "list"))}"{attrs}><legend>{inline(md, a["prompt"])}</legend>{sol}'
            f'<ul class="choices">{opts}</ul>{justify}<div class="choice-actions"><button type="button" class="commit">Vastaa</button></div>'
            f'{pending}<output aria-live="polite"></output></fieldset>')


def numeric_html(a, md, aid):
    unit = esc(a.get("unit", "")); mistakes = esc(json.dumps(a.get("mistakes", []), ensure_ascii=False))
    sol = f'<details class="solution"><summary>Ratkaisu</summary><div class="steps">{md(a["solution"])}</div></details>' if a.get("solution") else ""
    return (f'<div class="numeric"><p class="task">{inline(md, a["prompt"])}</p>'
            f'<form class="check" data-answer="{a["answer"]}" data-tol="{a.get("tolerance", 0.02)}" data-mistakes=\'{mistakes}\' novalidate>'
            f'<input type="text" inputmode="decimal" autocomplete="off" enterkeyhint="done" aria-label="Vastaus" placeholder="?">'
            + (f'<span class="unit">{unit}</span>' if unit else "") + '<button type="submit">Tarkista</button><output aria-live="polite"></output></form>'
            f'{hints_html([md(h) for h in a.get("hints", [])])}{sol}</div>')


def explain_html(a, md, aid):
    crit = "".join(f'<li><label><input type="checkbox"> <span>{inline(md, c)}</span></label></li>' for c in a["criteria"])
    pair = f'<p class="pair">{md(a["pair"])}</p>' if a.get("pair") else ""
    return (f'<div class="explain"><p class="task">{inline(md, a["prompt"])}</p><textarea rows="4" aria-label="Oma selitys"></textarea>{pair}'
            f'<div class="choice-actions"><button type="button" class="show-model">Näytä mallivastaus ja arviointi</button></div>'
            f'<div class="model" hidden><h4>Mallivastaus</h4>{md(a["model"])}<h4>Arvioi oma vastauksesi</h4><ul class="criteria">{crit}</ul></div></div>')


def question_html(q, md, lid, aid):
    t = q["type"]
    if t == "choice": return choice_html(q, md, lid, f"{aid}-q")
    if t == "numeric": return numeric_html(q, md, f"{aid}-q")
    return explain_html(q, md, f"{aid}-q")


def experiment_html(a, md, lid):
    units = a.get("units", {}); names = a.get("names", {})
    nm = lambda k: esc(names.get(k, k))
    fi = lambda v: str(v).replace(".", ",") if isinstance(v, (int, float)) else str(v)   # decimal comma on the page
    fmt = lambda k, v: f"{nm(k)} = {esc(fi(v))}" + (f" {esc(units[k])}" if k in units else "")
    init = ", ".join(fmt(k, v) for k, v in a["initial"].items())
    locked = ", ".join(nm(k) for k in a["locked"]) or "ei mitään"
    cols = "".join(f"<th>{esc(m['label'] if isinstance(m, dict) else m)}</th>" for m in a["measure"])
    measure = json.dumps([m["key"] if isinstance(m, dict) else m for m in a["measure"]])
    q = f'<div class="exp-question" data-min="{a.get("min", 2)}">{question_html(a["question"], md, lid, a["id"])}</div>' if a.get("question") else ""
    return (f'<div class="experiment" data-initial=\'{esc(json.dumps(a["initial"]))}\' data-locked=\'{esc(json.dumps(a["locked"]))}\' '
            f'data-vary="{esc(a["vary"])}" data-vary-name="{nm(a["vary"])}" data-locked-names=\'{esc(json.dumps([names.get(k, k) for k in a["locked"]], ensure_ascii=False))}\' data-measure=\'{esc(measure)}\' data-min="{a.get("min", 2)}">'
            f'<div class="intro">{md(a["intro"])}</div>'
            f'<p class="exp-setup"><strong>Alkutila:</strong> {init}. <strong>Vakiona:</strong> {locked}. <strong>Muutetaan:</strong> {nm(a["vary"])}.</p>'
            f'<div class="exp-controls"><button type="button" class="exp-start">Aseta alkutila</button><button type="button" class="exp-record">Kirjaa mittaus</button>'
            f'<button type="button" class="exp-reset">Nollaa</button></div>'
            f'<table class="exp-table"><caption>Mittaukset</caption><thead><tr><th>{nm(a["vary"])}</th>{cols}</tr></thead><tbody></tbody></table>'
            f'<p class="exp-status" role="status" aria-live="polite"></p>{q}</div>')


def sim_parts(a, md):
    """(visible lead, closed boxes) of the sim activity. The page shows the picture, the controls and the values first;
    the lead is one or two sentences and the longer texts sit behind Käyttöohje, Mallin oletukset and Laskennan
    selitys. A long text written before 2026-10-26 without those fields goes behind one box (LEGACY_INFO)."""
    text = a.get("text") or ""
    boxes = [(title, a[k]) for k, title in SIM_INFO if a.get(k)]
    if text and not boxes and len(text.split()) > LEAD_WORDS: boxes, text = [(LEGACY_INFO, text)], ""
    info = "".join(f'<details class="sim-box"><summary>{t}</summary><div>{md(x)}</div></details>' for t, x in boxes)
    return (md(text) if text else ""), (f'<div class="sim-info">{info}</div>' if info else "")


def render(folder, inquiry, parts, md):
    """(body html, toc html). parts: {'intro': html, 'sections': {key: html}, 'sim': html (with a <!--sim-info--> slot),
    'exercises': html, 'exit': html}.

    Order: the stages in STAGES order (empty ones left out), then the exercises in their own section "Tehtävät", last
    on the page whatever stage inquiry.json gives them. Layout hooks for templates/site.css, all single-column on a
    phone: the title and the "new this lesson" box side by side (.intro-row); consecutive GRID_TYPES activities in an
    .act-grid (two columns on a wide screen); the stage that holds the simulation as a .lab (the sim beside the
    experiments that use it); the Ennusta stage inside a <details class="fold"> that starts closed and keeps its answers
    when closed; a theory figure beside its paragraph (build.py fig_rows)."""
    lid = folder.name
    acts = inquiry["activities"]
    by_stage = {s: [] for s in STAGE_IDS}
    ex_act = None
    for a in acts:
        if a["type"] == "exercises": ex_act = a; continue
        by_stage[a["stage"]].append(a)
    placed = {s for a in acts if a["type"] == "theory" for s in a["sections"]}
    leftover = [s for s in parts["sections"] if s not in placed]
    if leftover and not any(a["type"] == "theory" for a in by_stage["selita"]):
        by_stage["selita"].append({"id": "theory-rest", "type": "theory", "stage": "selita", "sections": leftover})
    elif leftover:                                     # append to the last theory activity in Teoriatiivistelmä
        last = [a for a in by_stage["selita"] if a["type"] == "theory"][-1]; last["sections"] = list(last["sections"]) + leftover
    prior = inquiry.get("prior") or []
    aside = f'<div class="contribution"><strong>Tällä tunnilla uutta:</strong> {inline(md, inquiry["contribution"])}</div>'
    if prior: aside += '<p class="prior"><strong>Tarvitset:</strong> ' + "; ".join(inline(md, x) for x in prior) + '</p>'
    body = [f'<div class="intro-row"><div class="intro-main">{parts["intro"]}</div><div class="intro-aside">{aside}</div></div>']

    def act(a):
        t, aid = a["type"], a["id"]
        head = f'<h3>{esc(a["title"])}</h3>' if a.get("title") else ""
        if t == "hook": content = f'<div class="hook">{md(a["text"])}</div>' + (f'<p class="question">{inline(md, a["question"])}</p>' if a.get("question") else "")
        elif t == "text": content = md(a["text"])
        elif t == "choice": content = choice_html(a, md, lid, aid)
        elif t == "numeric": content = numeric_html(a, md, aid)
        elif t == "explain": content = explain_html(a, md, aid)
        elif t == "reflect":
            content = (f'<div class="reflect" data-predictions=\'{esc(json.dumps(a["predictions"]))}\'><p class="task">{inline(md, a["prompt"])}</p>'
                       f'<ul class="my-predictions"></ul><p class="revise"><strong>Muuttaisitko ennustettasi?</strong> '
                       f'<label><input type="radio" name="{esc(aid)}-rev" value="ei"> En</label> <label><input type="radio" name="{esc(aid)}-rev" value="kylla"> Kyllä</label></p>'
                       f'<textarea rows="3" aria-label="Miksi?" placeholder="Miksi?"></textarea></div>')
        elif t == "experiment": content = experiment_html(a, md, lid)
        elif t == "interpret": content = f'<div class="interpret"><div class="representation">{md(a["text"])}</div>{question_html(a["question"], md, lid, aid) if a.get("question") else ""}</div>'
        elif t == "theory": content = "".join(parts["sections"][s] for s in a["sections"])
        elif t == "sim":
            lead, info = sim_parts(a, md)
            content = lead + parts["sim"].replace("<!--sim-info-->", info)
        elif t == "exit": content = (md(a["text"]) if a.get("text") else "") + parts["exit"]
        else: content = ""
        hints = hints_html([md(h) for h in a.get("hints", [])]) if t not in ("numeric",) else ""
        return f'<div class="activity act-{t}" id="{esc(aid)}" data-type="{t}">{head}{content}{hints}</div>'

    def flow(items, grid=True):
        out, run = [], []
        def flush():
            out.append('<div class="act-grid">' + "".join(run) + '</div>' if len(run) > 1 else "".join(run)); run.clear()
        for a in items:
            if grid and a["type"] in GRID_TYPES: run.append(act(a))
            else: flush(); out.append(act(a))
        flush()
        return "".join(out)

    toc, n = [], 0
    for sid, title in STAGES:
        items = by_stage[sid]
        if not items: continue
        n += 1
        si = next((i for i, a in enumerate(items) if a["type"] == "sim"), None)
        if si is not None and si < len(items) - 1:     # the sim beside the activities that use it
            inner = (flow(items[:si]) + f'<div class="lab"><div class="lab-side">{act(items[si])}</div>'
                     f'<div class="lab-main">{flow(items[si + 1:], grid=False)}</div></div>')
        else: inner = flow(items)
        if sid == "ennusta":                           # closed at first; reopened later, the answers are still there
            k = sum(1 for a in items if a["type"] == "choice")
            inner = (f'<details class="fold" data-fold="{sid}"><summary><span class="fold-title">Tee ennusteet ennen tutkimista</span> '
                     f'<span class="fold-status" data-n="{k}">{k} {"kysymys" if k == 1 else "kysymystä"}</span></summary>'
                     f'<div class="fold-body">{inner}</div></details>')
        body.append(f'<section class="stage" id="{sid}" data-stage="{sid}"><h2><span class="stage-no" aria-hidden="true">{n}</span>{title}</h2>{inner}</section>')
        toc.append(f'<a href="#{sid}">{NAV.get(sid, title)}</a>')
        if any(a["type"] == "exit" for a in items): toc.append(f'<a href="#exit">{EXIT_TITLE}</a>')
    if parts.get("exercises"):                         # the exercises close the page, after the exit ticket
        text = md(ex_act["text"]) if ex_act and ex_act.get("text") else ""
        aid = ex_act["id"] if ex_act else "harjoitukset"
        body.append(f'<section class="stage stage-practice" id="exercises" data-stage="exercises"><h2>{EXERCISES_TITLE}</h2>'
                    f'<div class="activity act-exercises" id="{esc(aid)}" data-type="exercises">{text}{parts["exercises"]}</div></section>')
        toc.append(f'<a href="#exercises">{EXERCISES_TITLE}</a>')
    return "\n".join(body), "".join(toc)


if __name__ == "__main__":
    if len(sys.argv) != 2: sys.exit(__doc__)
    lid = sys.argv[1]
    folder = next((f for f in ROOT.glob(f"content/*/{lid}") if (f / "meta.json").exists()), None)
    if folder is None: sys.exit(f"no lesson {lid}")
    inq = load(folder)
    if inq is None: sys.exit(f"{lid}: no inquiry.json (the lesson renders in the classic layout)")
    errs = validate(folder, inq, (folder / "lesson.md").read_text())
    print("\n".join(errs) if errs else f"{lid} inquiry.json: valid ({len(inq['activities'])} activities)")
    sys.exit(1 if errs else 0)
