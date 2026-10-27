VERDICT: PASS
CONTENT-HASH: 4b2d2c5bd410ab70

## Blocking

## Polish
- solutions.md:9 — L1-01 check "80 N ≈ 8 kg, 8 kg · 10 m/s² · 25 m = 2000 J" just redoes F·s through a mass, so it checks nothing; the 20 kg / 10 m comparison is also only a restatement — replace with an independent check, e.g. "pushing at 80 N, like lifting an 8 kg bag, over a short street: a couple of kJ, far below a kWh".
- solutions.md:50 — L1-05: 3,0 m/s is about 11 km/h, a ski pace, not "reippaan kävelyvauhdin" — say "hiihtovauhdilla" or drop the pace claim.
- solutions.md:24 — L1-03 "tekee työn tasaisesti" is not given in the task and is not needed: P = W/t is the average power whatever the time profile — say "keskimääräinen teho on kokonaistyö jaettuna ajalla".
- solutions.md:122 — L3-03 "Se vastaa arkikokemusta aurinkosähköstä" is not a check; the 648 kJ/h bound before it is the real one — drop the sentence.
- lesson.md:180 — "muuttaa sähköenergiaa lämmöksi" beside the Joule passage that treats heat as a transfer — "kiukaan ja ilman sisäenergiaksi" (carried).

## Checked
- One script recomputed all 12 exercise answers, siirto 240 W, check-2 180 J, example 4,0 J, predictions 600/1200 J and 120/30 W, pred-3 1960 J, exit 98 J and 20 J: all match answers.py and exercises.json within tolerance.
- Every solution: given/asked with units, principle with the right condition (constant force along motion; area for varying force; hidas nosto ⇒ F = G; constant P ⇒ W = Pt), symbols solved before numbers.
- Conversions right: cm→m, kJ→J, kN→N, min→s, s→min, kW·h check 0,10 kWh = 360 kJ.
- Rounding: differences of readings (6,0 − 2,0; 1,5 − 0,50; 8,0 − 4,0 m) carry two figures, so every 2-sf answer is justified; 250 155 J → 250 kJ and 588,6 J → 590 J right.
- Sanity values right: 36,7 m, 2,9 kW, 8,3 kN, 60 kg·1 m ≈ 589 J, 0,76 h, 15 kg, means 17 N and 22,5 N between bounds.
- Worked example: seven stages, triangle area with reason, 8,0 J error explained.
- Formulas inside the FY3 scope note (no E_p, E_k, cos α).
- Joule table consistent (19,6 J per drop, ΔU/W ≈ 0,99), labelled invented; Joule 1850 ≈ 4,16 J/(g·°C) right.
- Simulation unchanged: W = Fs, P = W/t, area fills linearly, speed changes pace only; exp-1/exp-2 isolate s and t.
- spring-work figure to scale (0,20 m ↔ 40 N vertex).
