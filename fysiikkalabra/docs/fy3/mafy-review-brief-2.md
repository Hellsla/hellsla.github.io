# FY3 — review: the remaining MAFY symbols in exercises, Sovella and the example exam (teacher 2026-11-13)

Work in `fysiikkalabra/`. Your prompt names your role (science, pedagogy, or visual & editorial) and the parts.

## What changed
The chapters fy3-8, fy3-11 and fy3-15 now write their formulas in MAFY's form (docs/fy3/mafy-review-brief.md):
length l, l₀, Δl (thermal expansion); the heat pump with Q₁ (heat given to the warm side), Q₂ (heat taken from the
cold side), W (electric work), ε = Q₁/W = Q₁/(Q₁ − Q₂); efficiency η = W_a/W_o = P_a/P_o (a = output, o = input).
The places that still used the old symbols were changed the same way, every number and answer unchanged:
- **fy3-11 exercises** (fi, fi-easy, en): L2-04 η = P_a/P_o (was P_mek/P_in), L3-02 the heat demand Q → Q₁.
- **fy3-15 exercises** (fi, fi-easy, en): L3-03 a missing full stop.
- **FY3 Sovella itsenäisesti** (fi, fi-easy, en), task 1 c): η = P_a/P_o with P_a the power the water gets and P_o the
  radiation power (was P/P_tuleva, P/P_in).
- **FY3 example exam** (fi): k5 Δl = αl₀ΔT (was ΔL, L₀); k7 b)–e) the heat pump with Q₁, Q₂, W (was Q, Q_sisälle,
  Q_maa, E_s), also in its rubric texts (tasks.json); the answer keys of answers.py (`name`) are unchanged.

**Also in the exercise sets:** fy3-11's and fy3-15's exercise sets were already drafts on main, because another merged
pull request added whole exercises to them (`reviews.py scope <id> --exercises`: "whole exercises added or replaced").
Your review of these two sets covers those added exercises too, as `reviews.py scope` asks.

The diff: `git diff 6de15d457a -- fysiikkalabra/content/<lang>/FY3/` (these commits) and, for the added exercises,
`git diff 81db4a6 6de15d457a -- fysiikkalabra/content/<lang>/FY3/fy3-11/exercises fysiikkalabra/content/<lang>/FY3/fy3-15/exercises fysiikkalabra/lessons/FY3/fy3-11 fysiikkalabra/lessons/FY3/fy3-15`.

## What to judge
- **Science** (`docs/physics-guardrails.md`): the new symbols are right and defined where they appear, consistent with
  the chapters; the added exercises are physically right and their answers come out of `python3 lessons/FY3/<id>/answers.py`
  (`lessons/FY3/koe/answers.py`, `lessons/FY3/sovella/answers.py` for the exam and Sovella if present).
- **Pedagogy**: a student can follow the solutions; the added exercises fit their levels and the chapter.
- **Visual & editorial**: build `python3 scripts/build.py fy3-11` (and fy3-15; `python3 scripts/build.py` builds the
  Sovella and exam pages site/FY3-sovella.html, site/FY3-koe.html) and look at the changed solutions opened at 390 and
  1280 px (Playwright via node), typography of the new symbols, Finnish and English.

## Output
Write (overwrite) your role's report for each part you are given:
- exercise sets: `content/<lang>/FY3/<id>/exercises/review/<role>.md`, hash `python3 scripts/reviews.py hash <id> --exercises --lang <lang>`;
- Sovella: `content/<lang>/FY3/sovella/review/<role>.md`, hash `python3 scripts/practice.py hash FY3 --lang <lang>`;
- the exam: `content/fi/FY3/koe/review/<role>.md`, hash `python3 scripts/practice.py hash FY3/koe`.
Each starts exactly
```
VERDICT: PASS
CONTENT-HASH: <hash>
```
(or FAIL), then `## Blocking` and `## Polish` (file, place, concrete fix), under 300 words. Do not edit anything else,
do not commit. Report back in under 200 words: verdicts and every Blocking finding.
