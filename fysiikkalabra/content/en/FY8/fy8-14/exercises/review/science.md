VERDICT: PASS
CONTENT-HASH: 207d724bbb879a97
SCOPE: delta added-exercise from 1e964fbac349ac61 base 5b3ca4f81c77

## Blocking
(none)

## Polish
- exercises.json fy8-14-L2-08 — the stated reading accuracy is 0.1 cm, but the box accepts only 1.52–1.71 cm (6 %). A student who reads the bone half-value thickness as 1.2 cm, still inside that accuracy, gets 1.76 → 1.8 cm, which is rejected. 1.0 cm gives 1.5 cm, which is only "Lähellä". The part c check against the graph does give 1.6 cm, so this is not an error — fix: widen the tolerance to about 0.09, or ask for the reading to 0.05 cm.
- solutions.md fy8-14-L2-09 Answer — "three significant figures like the half-life read from the graph": $T_{1/2}$ is read to ±5 min, so 110 min is barely three figures — fix: say that the reading accuracy limits the result to about ±15 min, or give $3.3\cdot10^2\,\text{min}$ (5.5 h).
- exercises.json fy8-14-L2-08 text — "bone can be replaced by a layer of soft tissue" runs the other way from what part c asks (the bone layer that matches the tissue) — fix: "a layer of bone and a layer of soft tissue are equivalent when they let through the same share".

## Checked
- Hash 207d724bbb879a97 (`--exercises --lang en`) was the same at the start and the end.
- I recomputed both answers with my own script. L2-08: $I:I_0 = 0.5^{5.0/3.4} = 0.361$; $d_\text{bone} = 5.0 \cdot 1.1/3.4 = 1.618$ cm, the same as $1.1\log_2(1/0.361)$; the graph check $0.5^{1.6/1.1} = 0.365$. L2-09: $110\log_2 8 = 330$ min. Both agree with answers.py and exercises.json.
- The data are realistic: NIST-type values give half-value thicknesses at 60 keV of about 3.2–3.4 cm for soft tissue and 1.15 cm for cortical bone (lesson-answers.py: 3.37 and 1.15 rounded). F-18 $T_{1/2}$ is 110 min, and a 480 MBq FDG syringe is a plausible size.
- Models and conditions: equal shares mean an equal number of half-value thicknesses (exponential attenuation, the energy of about 60 keV is stated; the narrow-beam condition is a C simplification at this level). The decay law applies because the task states that decay is the only loss.
- Both solutions solve symbolically before substituting, show how the graph is read, say that no conversions are needed, and end with a real reasonableness check (a factor of about 3.1, three half-lives).
- Figures: kontrasti-points draws $0.5^{d/3.4}$ and $0.5^{d/1.1}$ on a 0.5 cm / 0.05 grid; fdg draws $480\cdot0.5^{t/110}$ on a 20 min / 20 MBq grid. The darker lines match the descriptions (every 1 cm and every 0.1; every 60 min and every 100 MBq). Neither figure marks the half-value thickness or the half-life, so neither gives the answer away.
- The box tolerance (the larger of 2 % and the task's tolerance, templates/lesson.js) for L2-09 accepts 317–343 min; a half-life read as 105 or 115 min is "Lähellä".
- Scope: half-value thickness and the decay law are in FY8's central contents (applications of ionising radiation, hajoamislaki).
