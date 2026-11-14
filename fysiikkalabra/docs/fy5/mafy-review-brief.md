# FY5 — review: formulas in MAFY form and MAFY names (teacher 2026-11-14)

Work in `fysiikkalabra/`. Your prompt names your role (science, pedagogy, or visual & editorial). Same method as
`docs/fy4/mafy-review-brief.md`; read it for the rules (delta level: judge the changes and what they touch).

## What changed and why
Formulas the students meet are the formulas of the MAFY tables, each named by MAFY's own name in a formula table
(```kaavat fences, `scripts/kaavat.py`; the list is `docs/fy5/kaavanimet.tsv`; an unnamed formula is one that is not in
MAFY). Only fy5-14 and fy5-15 changed in substance (fy5-1, 3, 4, 7, 8, 9, 10 only got names, carried over, not yours):

- **fy5-14** (lesson, inquiry, exit ticket, exercises, solutions, figures `lessons/FY5/fy5-14/figures.py`, the
  simulation's labels `lang/*.json` sims.fy5-14, `sim-spec.md`): MAFY's symbols for the Doppler effect: v_s → **v_L**
  (the source's speed, *lähde*), v_h → **v_H** (the observer's speed, *havaitsija*); the beat frequency f_h → **f_H**
  and its period T_h → **T_H** (en f_b → f_H too). The combined formulas f = f₀·v/(v ∓ v_L) and f = f₀·(v ± v_H)/v are
  now MAFY's four formulas, each named (source approaching / receding, observer approaching / receding); the text says
  which applies instead of "choose the sign". The summary line and the en note on subscripts follow.
- **fy5-15**: the sound intensity level in MAFY's form L = 10 lg(I/I₀) dB (was L = 10 dB · lg(I/I₀)), in the lesson,
  inquiry and solutions where the law itself is stated; difference and derived forms (L₂ − L₁ = 10 dB · lg(I₂/I₁),
  I = I₀·10^(L/10 dB)) are unchanged. The concept card in `kortit/` follows.

Every number and answer is meant to be unchanged (`python3 lessons/FY5/<id>/answers.py`). The diff:
`git diff origin/main -- content/fi/FY5/<id>/ content/fi-easy/FY5/<id>/ content/en/FY5/<id>/ lessons/FY5/<id>/ lang/ kortit/`
(ignore review/ folders and `docs/`).

## What to judge
Read the chapter for the consequences of the new symbols: a symbol changed in one place must be the same everywhere a
student meets it (text, figures, simulation labels, exercises, solutions, all three languages).
- **Science**: each formula equals MAFY's with its conditions; v_L, v_H, f_H, T_H used consistently and defined where
  they first appear; the four Doppler formulas' signs and the sentences saying when each applies are right; the
  intensity-level form is equivalent to the old one; numbers and answers unchanged; fi-easy and en say the same.
- **Pedagogy**: a 16–19-year-old can follow the four-formula presentation; the worked example (train, source moving)
  and the exercises still work with "choose the formula" in place of "choose the sign"; fi-easy is clear.
- **Visual & editorial** (`docs/EDITORIAL_QUALITY_STANDARD.md`): build `python3 scripts/build.py <id>` →
  `preview/<id>.html` (`preview/fi-easy/`, `preview/en/`), look at 390 and 1280 px at the formula tables (the Doppler
  tables, the intensity-level table), the fy5-14 figures (arrows v_L, v_H, T_H), the simulation labels; upright
  subscripts (L, H), Finnish and English. Do not run the full site build.

## Output
For the lesson `content/<lang>/FY5/<id>/review/<role>.md`, for the exercise set
`content/<lang>/FY5/<id>/exercises/review/<role>.md`, overwriting your role's report, starting
```
VERDICT: PASS
CONTENT-HASH: <hash>
```
(or FAIL) with the hash from `python3 scripts/reviews.py hash <id> --lang <lang>` (add `--exercises`), then `## Blocking`
and `## Polish` with numbered findings (file, place, concrete fix), under 300 words. Blocking = a physics error, an
inconsistent symbol a student meets, a changed number or answer, an undefined symbol, broken layout. Do not edit
anything else and do not commit. Report back in under 200 words: verdicts and every Blocking finding.
