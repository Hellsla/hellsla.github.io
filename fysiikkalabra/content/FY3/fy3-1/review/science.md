VERDICT: PASS
CONTENT-HASH: 7243e2b1131e0f2d

## Blocking

## Polish
- inquiry.json:check-3 model — the fourth criterion ("voimamittari mittaa painoa, ei massaa") is only implicit in the model answer — add one sentence saying the spring reads the force (weight), so the same mass gives a smaller reading on the Moon.
- inquiry.json:pred-2 choice 4 feedback — "riippumatta siitä, mitä mittarin alla on" is right for this model, but the table already says Jupiter's g is taken at the cloud tops — optionally echo that here so the "no surface" objection is answered with the lesson's own caveat.
- sim.js:1019 — readout prints g with two decimals (24,80 m/s²) while the table has 24,8 — print g with the table's precision.

## Checked
- answers.py and my own formulas agree on all 12 answers; every key rounded to its data's significant figures is within 0,02 relative tolerance (largest 0,8 %, L1-03).
- solutions.md: each solves symbolically (G = mg, m = G/g, x = x₁F/F₁, G_Mars = G_Maa g_Mars/g_Maa, m_Kuu = m g_Maa/g_Kuu, m = L g_Maa/g_Mars) before substituting; units and checks correct.
- Worked example: 1177,2 N → 1180 N, 445,2 N; symbolic stage first; ratio 0,38 correct.
- siirto 72,7 N and mistakes 19,44 / 117,72 / 7,41; check-2 8,8 m/s² and mistakes 0,114 / 44,9 recomputed.
- Predictions: 98,1 / 294 / 248 N, ratio 2,53; every correct option right, every feedback's numbers right; retrieval 6,0 km and distractor arithmetic (14, 18, 4,0 km) correct; calibration 3,5 N and 9,0 N distractor correct.
- Experiments: exp-1 locks body, varies m; exp-2 locks m = 10 kg, varies body; simState exposes m, g, G, body; adapter params match the select options.
- SVG figures: stretch graph 40 px/N, 50 px/cm, line through all three points; G(m) end points 53,8 / 175,8 / 217,6 px and Jupiter x = 251,3 px match 981, 371, 162 N and 1000 N at 40,3 kg.
- sim.js: G = m g, stretch and arrow purely proportional to G on the fixed 2480 N scale; bars proportional to G at the current mass; ruler ticks on the same scale; screenshot consistent (98,1 N on Maa).
- Misconception and exit ticket: 690 N, 29 N / 4,9 N, 7,5 cm, 15 N correct; bathroom-scale reasoning correct.
- Scope: force only as a measure of interaction; 1 N = 1 kg·m/s² deferred to FY4; Newton's laws absent.
