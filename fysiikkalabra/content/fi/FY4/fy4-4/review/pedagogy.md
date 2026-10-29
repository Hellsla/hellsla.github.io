VERDICT: FAIL
CONTENT-HASH: 9ea0a6d10fb17aff

## Blocking
- inquiry.json:177,280 — table headers `"ΣF_x (N)"` show as raw text with an underscore (1280 and 390 captures), against the all-labels-LaTeX rule; `"a_x (m/s²)"` (181,232,284) and `"v_x lopussa (m/s)"` (288) are likewise plain strings — fix: `"$\\Sigma F_x$ (N)"`, `"$a_x$ (m/s$^2$)"`, `"$v_x$ lopussa (m/s)"`.
- sim at 390 px (fy4-4-sim-390, exp-3-390) — canvas is the desktop picture shrunk to about 0.55: axis ticks and "Tilannekuva" are ~8 px, the cart, the blue and orange arrows and the graph points are tiny, yet exp-3 tells the student to watch them. Not readable on a phone — fix: at narrow widths stack picture, force diagram and graph full width, or raise label and arrow sizes.

## Polish
- inquiry.json pred-2 option 3 feedback: "Vaakasuoraa veto ei tarvitse voittaa painoa" → "Vaakasuora veto ei tarvitse voittaa painoa".
- inquiry.json check-2 prompt: "vaakasuoralla lattialla vaakasuoralla 30 N:n voimalla" repeats the word; same in exercises L1-04.
- Worked example (esimerkki figure) has only the force diagram, no pictorial situation picture beside it (docs/force-diagrams.md Representations).
- Workload: three predictions, three experiments, conclusion, reflection, example, selection, transfer, three checks and 12 exercises is more than one hour; consider making pred-3/exp-3 optional.
- Sim card at 1280 px cuts its last readout line at the sticky edge; make the scroll visible.

## Checked
- Hero (loaded truck behind, empty ahead, green light) matches the Miksi question at FY3 level of detail; legible at 390 px.
- Chapter names used everywhere; no lesson id shown to a student.
- Understanding first: the opening answer comes from the data (linear graph, mass halves a), the equation only after the diagram.
- Force teaching: identify, select, equations and a `draw` task with model figure and criteria.
- Each valitse distractor has one error (T=G, T<G, invented F), its feedback names it, the descriptions state arrows without judging them.
- Every solution and the example draw the force diagram before any equation.
- Layout at 360/768/1280 passes the checks; figures sit beside their paragraphs, the example is staged.
- Predictions can be refuted (exp-3 sign change, exp-1 and exp-2 two values); feedback gated and repairing.
- Exit ticket tests the core idea; Finnish otherwise correct.
