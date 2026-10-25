VERDICT: PASS
CONTENT-HASH: ba92ddd92dc584ef

## Blocking

(none)

## Polish
- lesson.md:148 — the text says "Simulaatiossa voit tutkia tätä" but the simulation sits after the yhdistetty kaasulaki, which comes in between; also the sim shows only relative pressure p/p_ref and N, never n in mol or pressure in Pa — move the sim paragraph next to the sim, or add one sentence: "Simulaatiossa paine näytetään suhteessa vertailutilaan, ei pascaleina."
- lesson.md:8 — "Yksi mooli on 6,022 · 10²³ hiukkasta. Avogadron vakio N_A = 6,022 · 10²³ 1/mol kertoo..." says the same number twice; merge into one sentence.
- lesson.md:200 — "Kemiasta tuttu moolitilavuus" is a new, undefined idea in the sanity-check stage; say "noin 24 litraa yhtä moolia kohti huoneenlämmössä" without the label.
- Exit ticket Q3 (recall of the model's assumptions) is the weakest of the three; a short quantitative or "what if T doubles" item would test the core idea better.
- exercises.json L3-01 and L3-03 ask for a justification, but the answer field is numeric only; the solution text covers the reasoning, fine for a self-check page.

## Checked
- Opening question (helium balloon) is answered in the Ydinajatus text and in figure 1 (0,21 mol each, 0,83 g vs 6,0 g), and again in the example's last stage and the misconception section.
- Learning path from fy3-9: combined gas law, then n, mole, N_A, M, R, pV = nRT; symbols are named once, no paragraph over about 110 words.
- Both required figures are present and legible on the phone page: balloon comparison and the four-vessel p / 2p figure; labels are readable at 390 px.
- The worked example has five stages, one step each with a bold lead-in; it is symbolic first, then substituted with units, and ends with a sanity check. It does not repeat any exercise.
- Exercises follow the levels: L1 five single-formula problems, L2 four with conversions or two steps, L3 three with reasoning; contexts varied; solutions follow given/wanted/formula/substitution/answer/check.
- Finnish and terminology (moolinen kaasuvakio, ainemäärä, moolimassa, Avogadron vakio, "2 s:n ajalta") are correct and match the glossary; no grammar errors found.
- Simulation at 360, 390 and 1280 px (N, T and V each at min and max, 2.5 s waits): the canvas shows coloured particles with speed legend (hidas/nopea), a pressure gauge, a moving right wall, hit flashes, the V % label and bars for mitattu and ennuste that rescale; the ratio stays near 1,00 at every extreme (e.g. 5,14 vs 5,13 at V = 25 %; 2,20 vs 2,20 at T = 600 K).
- No clipping of labels at any width (label boxes lie inside the canvas); at 360 px the canvas is small but readable and the sliders and readout stack below it, with units in K and %.
- The picture helps show why p grows with N and T and falls as V shrinks: more hits, faster hits and a smaller box are visible together with the bar.
- Review screenshots saved as fy3-10-rev-<width>-<state>.png in this folder.
