VERDICT: DONE

Round 1 fixes for fy3-7. Checks after the fixes: `answers.py` ok, `lint_lesson.py fy3-7` 0 errors / 0 warnings, `check_latex.py content/FY3/fy3-7` ok (30 fragments), `build.py --all` ok, `test_sims.py fy3-7` PASS (62 assertions, run twice).

## Blocking
1. **physics-expert 1 / mathematician 1 (lesson.md SVG, slopes reversed).** Redrew the heating curve to scale for 1 kg from −30 °C to 140 °C (0,155 px/kJ, 0,9 px/K): `70,197 80,170 132,170 197,80 548,80 560,44`. Slopes are now ice 2,7, water 1,38 and steam 3,0 px/px (ratios 2,0 and 2,2 against 2,0 and 2,1). The plateaus are 52 : 351 px (334 : 2260). Moved the dashed lines (0 °C to x=132, 100 °C to x=197), the tick labels and every text label. Checked the screenshots at 360, 390 and 1280 px: nothing overlaps. Added one sentence before the figure: the smaller the c, the steeper the rise, so ice and steam are about twice as steep as water.
2. **educator (melting label).** The plateau label now reads "sulaa, Q = sm", to match "kiehuu, Q = rm".
3. **web-designer, blocking 1 (DOM order).** The order is now canvas, controls (Lämmitä, Nollaa, then the sliders), readout, note. From the top of the canvas to the bottom of Lämmitä is now 244 px at 360 and 264 px at 390 (it was 639 / 611).
4. **web-designer, blocking 2 (canvas text).** Changed the layout so that `ts()` keeps its full size. The chart floor is at y=315. The tick labels sit at x0−10. Only every second x tick label is drawn when k > 1,5 (there is a tick mark at every step). "t (s)" is at y0+ts(36), inside the canvas. "T (°C)" sits above the axis. The heater label is left-aligned at the heater's end. The thermometer reading moves up one line when it would touch the container label or the "120" column. The plateau labels sit on a light background, and the boiling label stays left of the steam segment. Every label goes through `label()`, which records its box in `window.simLabels`. Sweep: m 0,10/0,15/0,35/0,50/0,75/1,00 × P 500/700/1000/1700/2300/3000 × 21 points across all five phases, at 360, 390 and 1280 px. That is 2268 frames, with 0 intersecting boxes and 0 boxes outside the canvas. Two assertions now check the same thing at the extreme settings.
5. **tester (history rescales).** The sliders are disabled while heating. A slider `input` event resets the run to t = 0, so Q = Pt always holds. sim-spec.md says so.

## Polish applied
- web-designer: SVG "jää" moved right of the axis, at font size 20 (the same as the other labels, 10,9 px at 360). The "kuumennin" label moved off the edge. The boiling label has a background. Bubbles stay below the water surface.
- tester: added the slider-range assertion. Added the boundary checks Q = 188 000 J → 'vesi', T = 0, Q = 187 999 J → 'sulaa', and Q = 1 527 500 J → 'höyry', T = 100. Added assertions for the locked and unlocked sliders and the reset on slider input. `simState.content` is now exposed and asserted for two phases. Also added checks for the DOM order and the note text.
- physics, mathematician, editor: the example now says "Oletetaan, että …", and the error is explained as loss through the vessel to the surrounding air (the vessel no longer warms up). Added "Vakiopaineessa" to the constant-temperature sentence.
- mathematician: the example and the summary both use Δm (vaa'an lukeman muutos). s, r, Q, m, ΔT and the formulas in running text are now in `$...$`. solutions.md L3-02 has units on every factor. L3-01 now checks that all the ice melts (36 662,5 J > 20 040 J), and answers.py asserts it.
- educator, editor: constants table after the formula (s, r, and c for ice, water and steam).
- physics: "höyryn oletetaan pysyvän astiassa" added to sim-spec.md and the sim note. I used the grammatical genitive form.
- editor, educator: exit ticket Q1 is now a particle-model question.
- editor: L3-03 is now a two-power measurement (800 W / 196 g and 400 W / 90,0 g, 10,0 min each). r = (P₁ − P₂)t/(Δm₁ − Δm₂) = 2,26 MJ/kg, and the student explains why the loss cancels and why each single run gives too much (2,45 and 2,67 MJ/kg). It is computed in answers.py, and the counts stay 5/4/3. It does not repeat the example: that has one run, this one needs two equations and the loss term.

## Skipped
- editor, educator: faasikaavio figure. This is a design decision about scope and length, not a correction, and the orchestrator did not list it. The sentence and the summary bullet stay.
- educator: extending the q2 answer. The new Q1 already tests the particle model.
- tester: a tighter SPEED ratio test. Real-time ratios are timing-sensitive in headless CI, and the tester said "accept as is".

Files changed: lesson.md, exercises.json, solutions.md, answers.py, exit-ticket.json, sim.js, sim-spec.md, tests/sims/fy3-7.json.
Stale reviewers (gate.py): tester, physics-expert, mathematician, educator, proofreader, editor, web-designer.
