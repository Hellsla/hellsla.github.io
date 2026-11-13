# FY1–FY3 — review: formulas in MAFY form (teacher 2026-11-12)

Work in `fysiikkalabra/`. Your prompt names your role (science, pedagogy, or visual & editorial) and the parts you review.

## What changed and why
The teacher wants the formulas students meet to be the formulas of the MAFY tables (the tables they have in the exam),
each named in the formula table by MAFY's name (```kaavat fences, `name :: LaTeX`, `scripts/kaavat.py`; an unnamed row is
a formula that is not in MAFY's tables). In these chapters the formulas and their symbols were rewritten, in fi,
fi-easy (selkeä suomi) and en, in the lesson and, where the symbols appear there, the exercise set:

- **fy1-6** (Putoamiskiihtyvyys): in the formula section, the average acceleration a = Δv/Δt (MAFY's keskikiihtyvyys,
  without the vector bar, the teacher's choice) with Δv = aΔt as its other form, then v = gt from rest (Δv = v, Δt = t).
- **fy3-8** (Lämpölaajeneminen): l = l₀(1 + αΔT) and V = V₀(1 + γΔT), then Δl = l − l₀ = αl₀ΔT for the calculations;
  the length symbol L → l everywhere (lesson, inquiry, exit ticket, exercises, solutions, figures, the simulation's
  labels in `lang/*.json` and two canvas labels in `lessons/FY3/fy3-8/sim.js`).
- **fy3-10** (Ideaalikaasun tilanyhtälö): the amount of substance as MAFY's two formulas n = N/N_A and n = m/M
  (was one chain).
- **fy3-11** (Kaasun tekemä työ ja lämpövoimakone): W = pΔV; the first law ΔU = Q + W with W the work done ON the gas, as
  fy3-5 teaches it (was ΔU = Q − W_k); η = W/Q₁ = (Q₁ − Q₂)/Q₁; the heat pump with Q₁, Q₂, W and ε = Q₁/W = Q₁/(Q₁ − Q₂)
  (was Q_sisälle, Q_ulko, E_s); the worked example's useful power P_a (was P_hyöty).
- **fy3-15** (Voimalaitosten hyötysuhde): η = W_a/W_o = P_a/P_o with P_o the input and P_a the useful power (was P_0,
  P_hyöty), the stage chain from P_o, the losses P_h = P_o − P_a; also P_tulo → P_o (L1-03), P_sisään − P_ulos → P_o − P_a
  (L1-04), E_0 → E_o (L2-07).

Every number and answer is meant to be unchanged. The diff: `git diff 3ec8cc24 -- fysiikkalabra/content/<lang>/<COURSE>/<id>/ fysiikkalabra/lessons/<COURSE>/<id>/ fysiikkalabra/lang/`
(ignore review/ folders; in lang/ only the sims strings of fy3-8 and fy3-11 changed).

## What to judge
The scope rule asks for a review of the changed part; read the whole chapter (lesson, inquiry, exit ticket and, where
listed, the exercise set) for the consequences of the new symbols, since a symbol changed in one place must be the same
everywhere a student meets it.
- **Science** (`docs/physics-guardrails.md`): each formula is right and equals MAFY's with its conditions; the first-law
  sign convention in fy3-11 is consistent with fy3-5 and with every solution (no W meaning two things without saying
  so); every symbol is defined with units where it first appears; P_o (letter o) is never confused with a zero; numbers
  and answers unchanged (`python3 lessons/<COURSE>/<id>/answers.py`, `lesson-answers.py`); fi-easy and en say the same.
- **Pedagogy**: a 16–19-year-old meeting the idea for the first time can follow the new notation; the change does not
  break the chapter's inquiry, worked example or exercises; the formula section still reads well; fi-easy is clear.
- **Visual & editorial** (`docs/EDITORIAL_QUALITY_STANDARD.md`): build `python3 scripts/build.py <id>` →
  `preview/<id>.html` (`preview/fi-easy/`, `preview/en/`), look at 390 and 1280 px at the formula tables (named rows,
  the continued row in fy1-6), the changed figures, the worked example and opened solutions (`details.solution`), the
  simulation's labels in fy3-8; mathematical typography (upright subscripts a, o, h, A), Finnish and English.

## Output
For each part you are given write `content/<lang>/<COURSE>/<id>/review/<role>.md` (the lesson) or
`content/<lang>/<COURSE>/<id>/exercises/review/<role>.md` (the exercise set), overwriting your role's report, starting
```
VERDICT: PASS
CONTENT-HASH: <python3 scripts/reviews.py hash <id> --lang <lang>>      (add --exercises for the exercise set)
```
(or FAIL), then `## Blocking` and `## Polish` with numbered findings (file, place, concrete fix), under 300 words.
Blocking = a physics error, an inconsistent symbol a student meets, a changed number or answer, an undefined symbol,
broken layout. Do not edit anything else and do not commit. Report back in under 200 words: verdicts and every Blocking
finding.
