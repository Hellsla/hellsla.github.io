VERDICT: PASS
CONTENT-HASH: fb09e6f60334216a

## Blocking

## Polish
- inquiry.json:265 — the correct option's feedback in *Etsi virhe* says the energy "purkaa hiukkasten välisiä sidoksia", while the theory, summary, checks and exit ticket use the guardrail wording — use "muuttaa hiukkasten keskinäisiä vuorovaikutuksia ja kasvattaa niiden välistä vuorovaikutusenergiaa" so the explanation is worded the same everywhere.
- lessons/FY3/fy3-7/sim.js:8 — the code comment says "breaks the bonds between particles" (not shown to students) — align it with the same wording.

## Checked
- One Python run recomputed every number: pr-lampo 209,5 kJ (distractors 2,1 kJ = one kelvin, 419 kJ = mass dropped); plateau lengths 83,5/167 s and 565/1130 s, r/s = 6,77; worked example r = 2,34 MJ/kg, +3,7 %, 133 g vs 128 g; siirto 188,3 W (mistakes 27,8 W and 11 300 W); check-2 0,597 kg (mistakes 0,677 and 4,04 kg, 0,54 kg reasonableness); check-3 2,52 kJ vs 264 J (×9,6).
- Text ratios: r/s ≈ 6,8 ("lähes seitsemän"), r vs 0→100 °C heating 5,4 ("yli viisi"), s ≈ heating 0→80 °C, ice and steam slopes ≈ 2× water's, steam volume ≈ 1700×, expansion work ≈ 7 % of r ("pieni osa").
- Guardrails: constant temperature stated for a pure substance at constant pressure (Ydinajatus, Virhekäsitys, Tiivistelmä, learn, contribution); melting/evaporation wording as agreed; no chemical bonds break; work against the surroundings named; condensation releases energy.
- Worked example: symbolic first, 3 sf from 128 g, invented data labelled, the sign of the deviation explained correctly by losses.
- Simulation: implements the five piecewise stages with the lesson's constants; tMelt = sm/P, tBoil = rm/P in simState; the piston model justifies 101 kPa, steam c_p and the 100 °C plateau, and the box says what open and rigid vessels would do.
- Experiments: exp-1 locks m and varies P, exp-2 locks P and varies m; both isolate the varied parameter and measure tMelt and tBoil.
- Predictions: exactly one correct option in pred-1, pred-2, pred-3, virhe and check-1; each distractor's feedback says correctly why it is wrong; pred-3 feedback notes that the sim is built on the explanation and does not prove it.
- Model answers, criteria and exit ticket agree with the theory; scope inside FY3.
- Hash identical at start and end.
