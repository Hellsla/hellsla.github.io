VERDICT: PASS
CONTENT-HASH: 1c475d117a3c45bd

## Blocking

## Polish
- inquiry.json pred-1 (wrong options 1 and 3): the feedback says "Mittauksesi näyttävät …", but these are simulation numbers. The correct option and pred-2 already say "Mallin arvot …". Fix: write "Mallin arvot näyttävät …" (carried over from round 1).
- lesson.md Kaava: "$\rho g h$ on hydrostaattinen paine eli ylipaine $\Delta p = p - p_0$" equals the glossary's ylipaine (measured against the surrounding air pressure) only when $p_0$ is the air pressure. Fix: add "kun pinnalla on ilmanpaine" (round 1).
- lesson.md Kaava: the conditions of $p = p_0 + \rho g h$ (liquid at rest, constant density) are stated in the derivation, the example and the sim's model box, but not next to the formula itself. Fix: add "levossa olevassa nesteessä, jonka tiheys on vakio" (round 1).
- lessons/FY3/fy3-4/lesson-answers.py: it computes only the retrieval item. The numbers of pred-1/2, exp-1, siirto, check-2, the worked example and the exit ticket are not there. Fix: add them (round 1).
- inquiry.json exp-2 intro: "bensiini 720, vesi 1000" has no units. Fix: write `$720\,\text{kg/m}^3$` and `$1000\,\text{kg/m}^3$`.

## Checked
- Round 1's blocking item is fixed. The worked example now gives $F \approx 1{,}77\,\text{kN}$ with three figures, and the reason (12,0 m, 101 kPa and 150 cm² each have three) follows P7. The check "noin 180 kg" still fits.
- I recomputed every number in one script with my own formulas, and all of them agree: 300 kPa, 294 ≈ 290 kPa, 117 720 / 218 720 Pa, 1765,8 N, 150,1 / 199,1 kPa (×1,33), 121,6 / 222,6 kPa (+11,8 %), 9,81 kPa/m, 0,757 m, 10,3 m, 891,9 kg/m³, 2179, 0,892, 29,4 kPa, 1,77 N, 306 N. The sim's toFixed readouts (node) and every numeric mistake value match.
- The column-weight derivation is correct and stays inside FY3 scope (force as a scalar, $G = mg$). So are the isotropy argument, the perpendicular force, the dam's overpressure, the barometer and the eardrum model answer.
- Every choice item has exactly one correct option. Each distractor is really wrong, and its feedback says why.
- exp-1 locks ρ and varies h. exp-2 locks h = 10 m and varies ρ. The values 720, 1000 and 1240 can be reached with step 5. `simState` gives `pOver` and `pTotal` in kPa.
- The changed sim.js still implements $p = p_0 + \rho g h$. The readout now leaves out the slope and the ratio, which the students work out themselves; they stay in `simState`. The 390 px capture shows 98,1 / 199,1 kPa at 10 m, and the chart scale is right. The model box states the sim's limits.
- The pressure-depth figure is to scale within 1 px (101 kPa and 199 kPa). The contact areas in pressure-area are 1 : 3.
- The formula name "hydrostaattinen paine" for $p_0 + \rho g h$ was kept by the teacher (kaavanimet.tsv, 2026-11-12), so it is not a finding.
- The hash was identical at the start and at the end.
