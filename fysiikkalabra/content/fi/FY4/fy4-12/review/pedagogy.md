VERDICT: PASS
CONTENT-HASH: cbee12aed8d34c3a

## Blocking
(none)

## Polish
- Tutki at 390 px (`fy4-12-exp-exp-2-390-1.png`, `fy4-12-sim-390.png`): canvas and graph labels are about 9 px; in case 3 the lower graph's `x (m)` label touches road B and `150 x (m)` crowds the axis end. Readable, but give the labels a little more room (shared sim layout, sim.js).
- Experiment tables at 390 px: headers wrap as "x_A ( m)" / "v_A ( m/s)"; use a non-breaking thin space before the unit in the `measure` labels (the round-1 clipping at 1280 px is fixed: `v_B` column dropped).
- inquiry.json `sim.calc`: says the gap "on positiivinen, kun B on edellä, ja nolla kohtaamishetkellä"; exp-3 relies on its sign change (B behind = negative). Add "negatiivinen, kun B on takana".
- No check or exit-ticket item on the (t,v)-intersection misconception (lesson text names it); acceptable, but one choice option in check-1 could use it.

## Checked
- Round 1 items fixed: learn goal 3 no longer gives the answer away; the coefficients A, B, C are named in the worked example; "kaukana" is answered in the vt paragraph (25 m maximum lead, 36 m / 64 m); exp-3's roots are no longer an exercise answer.
- Opening illustration matches the Miksi question (car at the line, cyclist ahead); all figure, sim and table labels are LaTeX.
- Chapter names, no ids in student text; 360/768/1280 px: no clipping, one reading column, sim beside the experiments at 1280 px.
- Predictions can be refuted (case 1, 3 tables); each option's feedback repairs its misconception; reveal gating min 2/3 fits the experiments.
- Understanding over formulas: position-versus-speed at the meeting and the area argument for 2v are the core; the algebra serves them.
- Worked example in seven stages, complete; figure data correct (36 m at 12 s; 9 m areas; 64 m at 8,0 s).
- Workload fits one lesson (retrieval, exp-3 and reflect are optional); Finnish correct.
- Hash unchanged at the end.
