# FY4 — review: formulas in MAFY form and MAFY names (teacher 2026-11-13)

Work in `fysiikkalabra/`. Your prompt names your role (science, pedagogy, or visual & editorial) and the parts you review.

## What changed and why
The teacher wants the formulas students meet to be the formulas of the MAFY tables (the tables they have in the exam),
each named by MAFY's own name in a formula table (```kaavat fences, `name :: LaTeX`, `scripts/kaavat.py`; the list is
`docs/fy4/kaavanimet.tsv`, 24 named formulas; an unnamed formula is one that is not in MAFY). The teacher decided
(2026-11-13) that FY4 is written with MAFY's symbols. In fi, fi-easy (selkeä suomi) and en:

- **fy4-1**: the average velocity v_k = Δx/Δt (was v_ka, v_avg) everywhere in the chapter (lesson, inquiry, exit
  ticket, exercise solutions). Arithmetic means elsewhere (v_ka in fy4-3, fy4-9 exercises) were left as they are.
- **fy4-2**: the formula section gives the average acceleration a_k = Δv/Δt (MAFY keskikiihtyvyys) and says that a
  constant acceleration equals it, a = a_k; v = v₀ + at and x = x₀ + v₀t + ½at² unchanged.
- **fy4-6**: beside the inequality F_μ0 ≤ μ₀N, MAFY's limiting friction F_μ0 = μ₀N (lähtökitka, the fully developed
  static friction just before sliding); glossary.json got the term lähtökitka.
- **fy4-8** (and **fy4-16**, the Sovella set): MAFY's work and energy formulas: W = Fs with F the component along the
  motion (was F_∥), the work principle E_k0 + W = E_k (was W_kok = ΔE_k), the work-energy principle of mechanics
  E_p0 + E_k0 + W = E_p + E_k with W the work of the forces other than the weight (was E_k,1 + E_p,1 + W_muut =
  E_k,2 + E_p,2), the conservation of mechanical energy E_p0 + E_k0 = E_p + E_k; index 0 = start, no index = end
  (E_mek,1 → E_mek0). The same symbols in the inquiry, exercises, solutions, figures (`lessons/FY4/fy4-8/figures.py`),
  the simulation's labels (`lang/*.json` sims.fy4-8) and the concept cards (`kortit/fy4.json`). Speeds v₁, v₂ in the
  data were kept.
- **fy4-9**: the impulse-momentum principle written I = Δp (was Δp = I), as MAFY.
- **fy4-15**: efficiency η = W_a/W_o = P_a/P_o with P_a the output (here electric) power, P_o the input power (was P_s);
  also in the exit ticket, solutions and the figure.
- Chapters fy4-3, 4, 5, 7, 12 only got the names (carried over, not yours).

Every number and answer is meant to be unchanged. The diff: `git diff 4677a36524 -- fysiikkalabra/content/<lang>/FY4/<id>/
fysiikkalabra/lessons/FY4/<id>/ fysiikkalabra/lang/ fysiikkalabra/kortit/` (ignore review/ folders). Some exercise sets
were already drafts on main because another merged pull request added whole exercises (`reviews.py scope <id> --exercises`);
your review of such a set covers those added exercises too.

## What to judge
Read the whole chapter (lesson, inquiry, exit ticket and, where listed, the exercise set) for the consequences of the
new symbols: a symbol changed in one place must be the same everywhere a student meets it.
- **Science** (`docs/physics-guardrails.md`): each formula is right and equals MAFY's with its conditions; W never means
  two things in one place without saying so (the total work in the work principle, the other forces' work in the
  energy principle); every symbol is defined with units where it first appears; numbers and answers unchanged
  (`python3 lessons/FY4/<id>/answers.py`, `lesson-answers.py`); fi-easy and en say the same.
- **Pedagogy**: a 16–19-year-old meeting the idea for the first time can follow the new notation; the change does not
  break the chapter's inquiry, worked example or exercises; the formula section still reads well; fi-easy is clear.
- **Visual & editorial** (`docs/EDITORIAL_QUALITY_STANDARD.md`): build `python3 scripts/build.py <id>` →
  `preview/<id>.html` (`preview/fi-easy/`, `preview/en/`), look at 390 and 1280 px at the formula tables, the changed
  figures (fy4-8 energy bars, fy4-15), the worked example and opened solutions (`details.solution`), the fy4-8
  simulation's labels; mathematical typography (upright subscripts k, p, o, a, mek), Finnish and English. Do not run
  the full site build.

## Output
For each part you are given write `content/<lang>/FY4/<id>/review/<role>.md` (the lesson),
`content/<lang>/FY4/<id>/exercises/review/<role>.md` (the exercise set) or `content/<lang>/FY4/sovella/review/<role>.md`
(Sovella), overwriting your role's report, starting
```
VERDICT: PASS
CONTENT-HASH: <hash>
```
(or FAIL) with the hash from `python3 scripts/reviews.py hash <id> --lang <lang>` (add `--exercises` for the exercise
set; `python3 scripts/practice.py hash FY4 --lang <lang>` for Sovella), then `## Blocking` and `## Polish` with numbered
findings (file, place, concrete fix), under 300 words. Blocking = a physics error, an inconsistent symbol a student
meets, a changed number or answer, an undefined symbol, broken layout. Do not edit anything else and do not commit.
Report back in under 200 words: verdicts and every Blocking finding.
