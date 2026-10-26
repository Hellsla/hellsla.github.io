VERDICT: PASS
CONTENT-HASH: b402e872b3e97159

## Blocking

## Polish
- sim-spec.md / inquiry.json:simulaatio.model — The spec says "höyryn oletetaan pysyvän astiassa". In a closed vessel the pressure would rise, and so would the boiling point. The model's 100 °C plateau assumes constant pressure, so add "vakiopaineessa" to the model note. Something like "höyry pysyy astiassa vakiopaineessa (kuin männän alla)" would do.
- inquiry.json:88 (pred-2) — The text says "565/83,5", but the sim readout and chart show "84 s" and the other options say "noin 84 s". Write "565/84 ≈ 6,7…6,8" or "noin 84 s" to match.
- lesson.md:87 — "esiteltiin edellisellä oppitunnilla" refers to a lesson, not a chapter. The owner wants the chapter named (for example "luvussa Aineen lämpeneminen ja jäähtyminen"). The same applies to inquiry.json:20 "Kertaa edelliseltä tunnilta" and to the "(fy3-6)" and "(fy3-2)" ids in `prior`, if students see them. This is a language and style matter, not science.
- lesson.md Kaava SVG — The heating curve is in fact to scale per kilogram. I measured 6,4 kJ/(kg·px): ice from −30 °C is 10 px, melting 52 px, water 65 px, boiling 351 px and steam to 140 °C is 12 px. The aria-label still says "kaavakuva", so you could say it is to scale. This is optional.

## Checked
- All 12 exercise answers recomputed in one independent script match answers.py and exercises.json, all within 0,6 %. L3-03: r = 2,264 MJ/kg, and the loss power of 60,4 W is consistent in both runs. The single runs give 2,45 and 2,67 MJ/kg, and the text correctly says these are too large.
- Inquiry numbers: pr-lampo 209,5 kJ, with distractors 2,1 kJ (ΔT dropped) and 419 kJ (m dropped). virhe 66,8 kJ, siirto 188,3 W (mistakes 27,8 and 11 300), check-2 0,597 kg (mistakes 0,677 and 4,04), check-3 2524 J vs 264 J (ratio 9,6, "lähes kymmenen").
- pred-1/2/3: the correct options are right. The model durations 167/83,5/565/1130 s and the ratio 6,77 match sim.js. pred-3 feedback now separates the model's built-in assumption from the evidence (the plateau length ∝ m).
- Experiments: exp-1 locks m and varies P; exp-2 locks P and varies m. 0,25 kg, 1000 W and 2000 W are reachable on the sliders, and simState exposes tMelt and tBoil.
- sim.js: the piecewise T(Q) is correct, Q = Pt, the plateaus are sm/P and rm/P, and pace changes only the speed. The 1280 px capture shows the correct curve and readout.
- Lesson claims: r/s ≈ 6,8, r/(c·100 K) ≈ 5,4 and s/c ≈ 80 K all hold. The slope ratio ice:water:steam ≈ 2:1:2 is right. The explanations of pressure dependence, sublimation and steam scalds are correct.
- Worked example: solved symbolically first, r = Pt/Δm = 2,34 MJ/kg. Losses cause an overestimate, which is correct, and the error is 3,5 %.
- solutions.md: each solution is symbolic first and the magnitudes are realistic. Ice layers are 4,9 and 3,9 cm, milk warms by ≈ 54 K, 0,90 MJ heats ≈ 2,7 kg of water by 80 K, and the energy shares are 90 %, 24 % and 87 %.
- Scope: everything is within "olomuodon muutokset" and the vaporisation-heat experiment, and there is no FY4 content.
- Mikromalli SVG: the solid, liquid and gas arrangements and the arrows are correct.
