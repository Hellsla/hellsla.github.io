VERDICT: PASS
CONTENT-HASH: eced6a5c7d9e54b5

## Blocking

## Polish
- lesson.md Ydinajatus, "Kaasun lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta" — the "harva kaasu, etenemisliike" condition comes only in *Mallin rajat* a few paragraphs later (C, no wrong picture) — optionally add "harvan" here so the first statement already carries it.
- inquiry.json pred-2, the "seinää on vähemmän" option's feedback — "törmäyksiä seinän pituutta kohti" is right for the 2D sim only — "seinän pituutta (todellisuudessa pinta-alaa) kohti".
- inquiry.json pred-1 and johtopäätös, "27 °C = 300 K" — the chapter uses 273,15 elsewhere. The rounding is fine but could be marked "≈".

## Checked
- Definitions: systeemi, ympäristö, suljettu systeemi, tilanmuuttujat, paine and lämpötila match the glossary. At absolute zero the energy is lowest and the motion does not stop (guardrail). Temperature is not internal energy: the ice/water example and the summary agree.
- Model conditions: p ∝ T is stated with constant V and n and a thin gas far from condensing. The extrapolation's limit is stated (real gases liquefy, the line is a model).
- Causality: heating means more frequent and harder hits. Compression means more frequent hits but not harder ones. The theory, the sim boxes, the feedback, the exit ticket and the explain model answer all say the same.
- Recomputed in one script: pred-1 ratio 600/300 = 2.00 (distractors 12.1 and 1.41 right). pred-2 50→100. Example: the table fits 100·T/273,15 kPa, k = 0,37 kPa/°C, θ₀ = −270 °C, cross-check 136,6 kPa. Etsi virhe 128 kPa. siirto 121,7 → 122 kPa, mistakes 404 and 83,8. check-2 −273 °C (table = sim pTheory). check-c2 1,035.
- Worked example: symbolic first, the 2-figure rounding comes from Δp = 37 kPa, and the slope comes from the endpoints of a line the points fit.
- Figures: kelvin-scale is to scale (1,20 px/K on both intervals). The extrapolation graph's points, axes (vertical axis at −300 °C) and zero crossing (−270 °C) match the data. The micro-model's equal boxes and equal N agree with the caption.
- sim.js: speed ∝ √T. The measured pressure is the momentum per time per wall length over the effective box, which gives N v²/(2A). The reference uses the same effective width, so pRel = 100·(T/300 K)/V matches pTheory with no offset. Speed changes pace only, and the window resets on a change of state.
- Sim limits are stated in the model box: 2D, no particle–particle collisions, one common speed, values are model values.
- Experiments: exp-1 locks V = 1 and varies T. exp-2 locks T = 300 and varies V from 2,0. The measured keys theta, vRel, pRel and pTheory all exist in simState, and 600 K and 2,0 dm³ are within the sliders' ranges.
- Assessment: exactly one correct option in every choice item, and each distractor's feedback names the actual error. The criteria of johtopäätös and check-3 ask only for what the prompt asks.
- Scope: within FY3's "termodynaaminen systeemi, tilanmuuttujat, lämpötila". The gas laws are only previewed and are deferred to their chapter.
