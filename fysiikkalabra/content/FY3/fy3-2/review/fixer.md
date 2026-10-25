VERDICT: DONE

Fixer report for fy3-2 (Työ ja energia): lesson-form rework to the human rules of 2026-10-25 (CLAUDE.md, NOTES.md section 4). Physics, numbers, exercise answers, sim and tests unchanged.

## Findings and changes
1. Lint ERROR, no figure in ## Ydinajatus. Added two schematic inline SVGs (600×300, currentColor, 24 px text, aria-label says "Kaavakuva"):
   - after the backpack paragraph: carrying sideways (force up, motion sideways, W = 0) next to lifting (force and motion both up, W = F s);
   - after the Joule paragraph: falling weight, rope over a pulley, paddle wheel in water, drop height h, "työ → lämpö".
2. Lint ERROR, no figure in ## Kaava. Added after the area paragraph two schematic (s,F) graphs: constant force (rectangle F · s) and a force that rises then stays constant (triangle A₁ + rectangle A₂).
3. Lint ERROR, worked example not staged. Rewrote ## Esimerkki as 5 stages separated by `<!-- vaihe -->`: Tunnetut ja kysytty / Kaava ratkaistuna (W = A_kolmio = ½ F_max s) / Sijoitus (symbolic rows, then 40 N and 0,20 m with units, = 4,0 J) / Tulos / Järkevyys (average force 20 N gives the same 4,0 J; 8,0 J would be wrong). Added the explicit question to the problem statement. Existing (s,F) graph kept (it is to scale; font raised from 20 to 24 px, aria-label says "mittakaavassa"). Inline units now use `\,`.
4. solutions.md, **Kaava:** lines now end with the formula solved for the asked quantity in symbols: L1-04 (W = F s), L2-03 (W = m g h, Sijoitus in one row), L2-04 (W = F₁ s₁ + ½ (F₁ + F₂) s₂, symbols added to Annettu), L3-01 (symbols s₁, s₂, s₃; F_ka = W / s; trimmed to under 120 words), L3-02 (Q = n m g h, n = 20 in Annettu). No numbers in any Kaava line.
5. Lint WARN, no answers.py. Wrote answers.py (one commented line per answer); its output matches exercises.json.
6. No paragraph is over 120 words (lint reports none).
7. Old review reports (pre-publication rounds): every Blocking finding was resolved before publication; the proofreader's diff is already in lesson.md. Nothing new to apply.

## Not fixable here
- scripts/lint_lesson.py `first_row_has_numbers`: its docstring says `\frac{1}{2}` constants do not count, but the code flags them (the regex removes only sub/superscripts). Worked around by starting the example displays with `W = A_kolmio`. Worth fixing in the lint.

## Checks
answers.py OK; lint 0 errors 0 warnings; check_latex all OK (15 fragments); build --all OK; check_layout OK at 360 px; test_sims PASS. Figures and the staged example inspected in screenshots at 360 px: no overlaps, no horizontal scroll.

## Files changed
lesson.md, solutions.md, answers.py (new). Not touched: meta.json, exercises.json, exit-ticket.json, sim.js, sim-spec.md, tests/sims/fy3-2.json.

Stale reviewers to re-run: all (the existing reports have no CONTENT-HASH line; lesson.md, solutions.md and answers.py changed): proofreader, physics-expert, mathematician, educator, editor, web-designer; tester only for the gate's hash line (its files did not change).
