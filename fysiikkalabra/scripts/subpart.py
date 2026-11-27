"""Which part of a multi-part task the answer box checks, and which parts have no check (work queue 29.9; teacher 2026-11-27).

The task text says it: "Vastauslaatikkoon tulee kohdan c) tulos." (fi, fi-easy), "The answer box takes the result of part c)." (en).
`info(text)` gives {"part": "c", "compare": [("b", "reason")]} or None. compare lists the other lettered parts the student
should hold against the model solution: a part that asks for a justification ("reason"), a graph ("graph") or a drawing
("drawing"); when none of them does, every other part, kind "other". templates/lesson.js composes the feedback from lang
"js" correct_part / compare_*; a single-part task and a task whose box sentence is missing are unchanged (None)."""
import re

BOX = re.compile(r"Vastauslaatikko\w*\s+(?:tulee\s+)?(?:(?:osan|kohdan)\s+([a-e])\)|([a-e])\)?-kohdan)"
                 r"|answer (?:box|field)\s+(?:takes the result of\s+)?part\s+([a-e])\)")
PARTS = re.compile(r"(?m)^([a-e])\)\s*(.*)$")
KINDS = (("graph", re.compile(r"kuvaaj|graph|plot", re.I)), ("drawing", re.compile(r"piirr|draw|sketch|diagram", re.I)),
         ("reason", re.compile(r"perustel|selit|miksi|säilyy|kommentoi|virhe|justify|explain|why|conserved|comment|mistake|error", re.I)))


def info(text):
    m = BOX.search(text)
    if not m: return None
    part = next(g for g in m.groups() if g)
    parts = dict(PARTS.findall(text))
    if len(parts) < 2 or part not in parts: return None
    others = {k: v for k, v in parts.items() if k != part}
    named = []
    for k, v in others.items():
        kinds = {kind for kind, rx in KINDS if rx.search(v)}
        if "graph" in kinds: kinds.discard("drawing")   # "Piirrä kuvaaja" is a graph
        if len(kinds) == 1: named.append((k, kinds.pop()))
        elif kinds: named.append((k, "other"))
    return {"part": part, "compare": named or [(k, "other") for k in others]}


def attrs(text):
    """The form's data attributes ('' when the task has no such box sentence)."""
    i = info(text)
    return "" if not i else f' data-part="{i["part"]}" data-compare="{",".join(f"{k}:{kind}" for k, kind in i["compare"])}"'
