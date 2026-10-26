VERDICT: PASS
CONTENT-HASH: e1b2bff902cba378

## Blocking

## Polish
- inquiry.json:111,116,121 (pred-3) — The feedback for Aino, Bea and Cem uses the model's built-in assumptions as evidence: the model has no losses, no thermometer lag and a plateau coded in, so "Tutkimus tukee tätä" overstates what the simulation can show about the mechanism. Rest the argument on what holds outside the model too. If the losses matched the input, the plateau would never end. The plateau length grows in proportion to m at a fixed P, so a fixed energy per kilogram is being stored. Say that the model *assumes* no losses rather than that it shows there are none.
- inquiry.json:79,84,88,92 (pred-2) — The feedback quotes 83,5 s, but the sim readout and chart label show "84 s" (`fi(tMelt, 0)`). Write "noin 84 s" or show tMelt with one decimal.
- lesson.md Kaava SVG — The aria-label says "kaavakuva", yet the curve is in fact to scale: slopes ice:water:steam ≈ 2:1:2.2, plateaus melt:boil = 52:351 ≈ s:r, and melt:water-heating = 0,80 ≈ s/(c·100 K). You could state that it is to scale. This is optional.
- inquiry.json pred-3 / sim.js — The sim calculates T from Q and cannot tell the three micro-explanations apart. The micro-model support comes from the theory, not from the experiment. This is a pedagogy matter that I note for the record only.

## Checked
- I recomputed all 12 exercise answers in one script and they match answers.py and exercises.json (all within 0,4 %). The L3-03 two-power difference method gives r = 2,264 MJ/kg and a loss power of 60,4 W, consistent in both runs. The single runs give 2,45 and 2,67 MJ/kg.
- The inquiry numbers are right: pr-lampo 209,5 kJ, with distractors 2,1 kJ and 419 kJ diagnosed correctly. The rest also match: virhe 66,8 kJ, siirto 188 W (mistakes 27,8 and 11 300), check-2 0,597 kg (mistakes 0,677 and 4,04), and check-3 1 g of steam gives 2524 J against 264 J, ratio ≈ 9,6.
- pred-1 and pred-2: the model durations 1130/565 s and 83,5/565/167/1130 s with ratio 6,77 match sim.js. The correct options are right, and every wrong option's feedback is physically correct.
- Experiments: exp-1 locks m and varies P; exp-2 locks P and varies m. The initial values are reachable on the sliders, and simState exposes tMelt and tBoil.
- sim.js: the piecewise T(Q) is correct for the constants, Q = Pt, the plateaus last sm/P and rm/P, and the speed control scales only the pace. The model's assumptions (no losses, steam kept in the container) are stated in the `model` box.
- Lesson claims hold: r/s ≈ 6,8 ("lähes seitsemän"), r/(c·100 K) ≈ 5,4, s/c ≈ 80 K, and the pressure dependence, sublimation and steam-scald explanations are correct.
- Worked example: solved symbolically, r = Pt/Δm = 2,34 MJ/kg. The sign of the error (loss → overestimate) is argued correctly.
- solutions.md: each is symbolic first and the magnitudes are realistic (ice 4–5 cm, steam milk ΔT ≈ 54 K, löyly 87 % evaporation).
- Scope: everything is within "aineen lämpeneminen ja jäähtyminen sekä olomuodon muutokset" and the vaporisation-heat experiment. No FY4 content appears.
- Mikromalli SVG: the solid/liquid/gas arrangement and the arrows are correct.
