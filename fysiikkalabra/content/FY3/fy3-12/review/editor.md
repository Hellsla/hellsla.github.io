VERDICT: PASS
CONTENT-HASH: c4e06f33e1001537

The lesson delivers its three goals and tells one story. It covers the three transfer modes, then heat loss of a house through the U-value, then the planet's energy balance, then the greenhouse effect and climate change. The opening question is answered explicitly (lesson.md:31). The exercises, solutions and exit ticket use both halves, the house and the planet, at every level. At about 1240 words it is as long as the reviewed FY3 lessons (fy3-1 1245, fy3-2 1362), and no paragraph is over 96 words. Ydinajatus has two figures and Kaava one, each placed after the paragraph it explains. The worked example has five staged steps, each with a bold lead-in and a symbolic first row. What remains is polish: the Sijoitus stage, the planet formula used by three exercises, and the thin ethics thread. The albedo framing (L2-04) and the line crossing the "eriste" label are already with the fixer, so they are not repeated here.

## Blocking
(none)

## Polish
- lesson.md:100–111 — Sijoitus does not use the combined formula from stage 2. It computes two separate parts, rounds P_seinä to 730 W, and the asked total P appears only as an inline line after the display. — Substitute into P = (U_s A_s + U_i A_i)ΔT: one row with values and units, then (20,4 W/K + 20 W/K) · 36 K ≈ 1454 W ≈ 1,5 kW. Move the 734 W vs 720 W comparison to Järkevyys. Keep each row under 25 characters.
- lesson.md:54–59 — Kaava formalises only the house half. L1-05 and L2-04 rely on "absorbed = (1 − r)·incoming = emitted", which appears only in prose at line 31. — After line 59, add one short display, P_im = (1 − r) P_tulo, name r (heijastuva osuus), and add one sentence: in balance, P_im equals the emitted power.
- lesson.md:41 — The "heijastuu" arrow starts at (190,104), about 75 px from the incoming ray, so the reflection is not connected to anything. — Start it where the ray enters the atmosphere band, at about (118,110).
- lesson.md:52 — The climate-change paragraph is the module's key goal, but it has no picture. The energy-balance figure shows only the steady state. — Optional: add a small before/after pair to the figure at line 33 (out = in; out < in, so the surface warms), or a caption saying the arrows show today's balance.
- exercises.json:64, lesson.md:52 — The ethics and environment goal rests on one sentence. No task links saved energy to emissions. — Optional: give an emission factor in L2-03 and ask for the CO₂ saved in kg. Update answers.py and solutions.md to match.

## Checked
- Goals (curriculum.json) vs content: all three transfer modes, U-value/home energy, energy balance, greenhouse effect, climate change, ethics.
- Scope: MAOL FY3 thematic contexts "rakentaminen ja energia kotona, ilmastonmuutos"; the OPH environmental-competence goal text matches.
- Lint 0 errors/0 warnings; answers.py values match exercises.json.
- Example arithmetic: 734 W + 720 W ≈ 1,5 kW; 1,45 kW · 24 h ≈ 35 kWh; the ×6 U-ratio in Järkevyys holds (1,0/0,17 ≈ 5,9).
- Stages: 5, bold lead-ins, symbolic first rows.
- Wall figure uses the example's 21 °C / −15 °C; aria-labels describe each figure.
- Exercise counts 5/4/3; none repeats the worked example (L2-01 asks for T_ulko).
- Exit ticket: one formula use, the three modes, the greenhouse mechanism — matches the summary.
- Glossary has every meta term, including U-arvo.
- Misconception section targets real confusions (ozone hole, "villapaita tuottaa lämpöä").
