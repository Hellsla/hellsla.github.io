VERDICT: DONE

Round 1 fixes for fy3-8 (Lämpölaajeneminen). Levels stay 5/4/3 with a solution for each task, and no task repeats the worked example.

## Blocking findings
1. **mathematician, exercises.json L1-05 (α has 1 sf)**: changed to "α = 9,0 · 10⁻⁶ 1/K" in exercises.json and in solutions.md (Annettu and Sijoitus). answers.py uses `9.0e-6`. The answer stays 0,34 mm. I left the lesson table at "9" because the sim's material menu prints the same table values, so the two match.
2. **lint ERROR, L1-03 (datum-plus-change answer)**: the task now asks for the elongation, which is also the change in the dial-gauge reading. The copper tube is 500,0 mm long, heated from 0 °C to 100 °C, so ΔL = 0,85 mm (2 sf, tolerance 0,02). The solution still shows L = 500,0 + 0,85 ≈ 500,9 mm. It stays level 1. It differs from L1-01 because the length is given in mm, so no unit conversion is needed, and the context is a lab measurement with a dial gauge. answers.py was changed first.
3. **educator, exit-ticket Q3**: replaced with the micro-model check ("Kasvavatko teräksen hiukkaset?"), using the reviewer's q and a word for word. The water anomaly is still in lesson.md.
4. **editor, lesson.md:12 (micro model for liquids and gases)**: added two sentences. A liquid's particles do not stay in place and their bonds are weaker, so a rise in temperature spreads them further apart. A gas's particles are far apart and almost free, so at constant pressure its volume grows much more. The pressure dependence now points to "oppitunnilla fy3-9".
5. **web-designer, lesson.md:62 (display 481 px)**: split it into two `aligned` rows. `check_layout.py fy3-8` reports OK at 360 px.

## Polish applied
- lesson.md:60: `°` became `{}^\circ` (mathematician).
- lesson.md:6: one sentence on why "helpompi loitota kuin puristua" holds: strong repulsion when particles are pushed together, weakening attraction when they are pulled apart (educator). I dropped the repeated "Hiukkaset itse eivät suurene", which the misconception section already says (editor: trim repetition).
- lesson.md:19: what α means, why ΔL ∝ L₀ (twice the length has twice as many particle spacings), and that the table's 12 means 12 · 10⁻⁶ 1/K (educator).
- lesson.md:12: "Tihein, 4-asteinen vesi painuu pohjalle, ja kylmempi vesi jää pinnalle ja jäätyy." (educator).
- lesson.md:21: "Nesteiden (ja vakiopaineessa kaasujen)" (editor, physics, educator).
- lesson.md:25: why γ ≈ 3α. Each of the three dimensions grows by the factor αΔT, and for small changes the relative growths add up to 3αΔT (educator).
- lesson.md SVG: font size 20 → 24. The "L₀ + ΔL" label is centred on the warm rod at x = 295 (web-designer, mathematician).
- sim.js readout and slider labels: each value and its unit sit in a `white-space:nowrap` span, so "120 °C" no longer breaks across lines. Their textContent is unchanged, so the existing readout tests still hold (web-designer).
- exercises.json L2-04: unit "10⁻⁶ 1/K", without the leading dot (web-designer).
- solutions.md L2-03: explains that each rail end moves ΔL/2 and both neighbouring rails narrow the gap, so the gap closes when one rail has lengthened by the gap width. "riittävän leveä" is gone (physics).
- solutions.md L1-04: one sentence saying the γ in the table is the value at 20 °C and that water's γ grows with temperature, so the real increase is slightly larger (physics, optional).
- tests/sims/fy3-8.json: added the tester's two assertions (controls with the button before the readout; simState.E = 100). There are now 43 assertions.

## Skipped
- mathematician polish 1 (tighter L1-03 tolerance) and physics polish 1: they no longer apply, because L1-03 now asks for ΔL.
- mathematician polish 2 (lint rule for coefficients with a power of ten): `scripts/` is not mine to edit. The lint already warns about it (it flagged L1-05).
- editor polish on the unused air row: the row now backs the new gas sentence ("kaasut vielä paljon enemmän"). Adding a gas exercise would change the 5/4/3 set for a matter of taste.
- editor polish that L1-01 resembles the worked example: the educator judged it acceptable at level 1 (different context, no sign crossing, conversion to mm).
- educator polish on gas collisions (fy3-3): the editor's particle-level gas sentence covers the same point. Adding both would repeat it.
- tester's optional determinism and chart-point items: marked low value by the tester.
- proofreader polish (canvas label "välit", "Fe", glossary entries): these were outside its diff and are not needed for this round.

## Checks
`python3 -I answers.py` OK. `lint_lesson.py fy3-8`: 0 errors, 0 warnings. `check_latex.py`: all OK. `build.py --all`: built. `test_sims.py fy3-8`: PASS (43). `check_layout.py fy3-8`: OK at 360 px.

## Files changed
lesson.md, exercises.json, solutions.md, answers.py, exit-ticket.json, sim.js, tests/sims/fy3-8.json.

Stale reviewers to re-run: tester, physics-expert, mathematician, educator, proofreader, editor, web-designer (all seven).
