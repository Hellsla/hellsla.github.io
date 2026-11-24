VERDICT: PASS
CONTENT-HASH: b21def63bfc47400

## Blocking

## Polish
- inquiry.json:339 (data, solution, Vastaus) — "Mittauspisteet poikkeavat suorasta noin $0{,}1\,\text{m/s}$" overstates the scatter: the five points lie within 0,04 m/s of the line v = 9,81·t (least-squares slope through the origin 9,78 m/s², standard error about 0,04 m/s²). The estimate of 0,2 m/s² is fair, but it comes from reading the graph (±0,1 m/s at 0,50 s), not from the scatter — base the estimate on the reading resolution, or say "alle 0,1 m/s".
- inquiry.json:116 (simulaatio.model) — the air model could name its form in a few words (the drag grows with the square of the speed, so a ball approaches its terminal speed). As written ("sitä enemmän, mitä nopeammin") it is correct at this level; this is optional.

## Checked
- Recomputed in one script and compared with lesson-answers.py: exp-1 9,81 (displayed values give 9,8); data 9,8 (LSQ 9,78); siirto 11,1 with mistakes 29,4/22,2/3,7; check-2 3,058 s with mistakes 11,0/30/0,327; example 14,715 m/s → 52,97 km/h; exit 4,86 and 29,4 m/s, ratio 6,06; retrieval 1,08 m/s with mistakes 1,82/0,93/2,7; the Moon hammer's 1,4 m in 1,3 s agrees with g = 1,62 m/s² (1,37 m); stop-and-think items 39,2 and 24,6 → 25 m/s.
- sim.js: vacuum v = gt and s = ½gt²; air dv/dt = g − (K/m)v² with exact tanh / ln cosh solutions, K = ½·1,2·0,47·π·0,1² kg/m. At 4,0 s: 0,1 kg 10,5 m/s, 1 kg 27,5 m/s, 10 kg 37,5 m/s. These match the model answer of johtopaatos and the exp-3 capture. Fall at 4 s is 78,5 m, inside the 80 m scale.
- Experiments: exp-1 locks the environment and the masses and varies t; exp-2 and exp-3 lock the environment, t and m_A and vary m_B with equal sizes, so mass is the only variable. simState gives vA and vB at those values.
- Exactly one correct option in each of pr-matka, pred-1, pred-2, exp-2, exp-3, virhe, check-1 and check-c2. Every distractor's feedback names the correct physics.
- Figures: free-fall is to scale (8,6 px/m; positions 0/4,9/19,6/44,1 m; intervals 4,9/14,7/24,5 m; velocity arrows proportional). vt-graph points and line give a slope of 9,81. The data graph's points match the table and its line has slope 9,81.
- Conditions stated: v = gt from rest and without air resistance; Δv = gΔt for a body that is already moving down; "eron aiheuttaa ilma, ei massa sellaisenaan" is consistent with the exp-3 model (C).
- Scope: FY1 linear model v = gt; forces deferred explicitly ("Syy selitetään myöhemmin voimien yhteydessä").
- Worked example: symbolic first, 1 m/s = 3,6 km/h derived, converted from the unrounded value, two figures justified, and the interpolation on the graph is a real check.
- Simulated data is labelled as simulated or model values (data source, sim boxes, johtopaatos criterion 4).
- Theory, summary, learn goals, check-3 model answer and exit ticket agree.
