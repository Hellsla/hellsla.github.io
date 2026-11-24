VERDICT: PASS
CONTENT-HASH: 0021887cd241265d

## Blocking

## Polish
- lesson.md "Massa ei vaikuta putoamiseen" / inquiry.json exp-3 feedback — "Eron aiheuttaa ilma, ei massa sellaisenaan": in exp-3 the balls are the same size and differ only in mass, so in air mass does decide the speed; the phrase is defensible (C) but "ilmanvastus vaikuttaa kevyeen kappaleeseen enemmän" would leave less room for misreading — optional rewording.

## Checked
- Recomputed in one script: pr-matka 1,4/1,3 = 1,08 → 1,1 m/s (distractors 1,82; 0,93; 2,7) and the Moon data itself (½·1,62·1,3² = 1,37 m); pred-1 29,4; exp-1 9,81 (mistakes 19,6, 29,4); data slope 4,9/0,50 = 9,8 (least squares through origin 9,78); siirto 3,7 → 11,1 → 11 m/s (mistakes 29,4, 22,2, 3,7); check-2 108 km/h = 30,0 m/s → 3,06 s (mistakes 11,0, 0,327); worked example 14,7 m/s = 53,0 km/h, two figures; exit ticket 4,86 → 4,9 m/s, 29 m/s, ratio 6,06; pysahdy 39,2 and 24,6 → 25 m/s. All agree with lesson-answers.py.
- Simulation air model recomputed: K = ½·1,2·0,47·π·0,10² = 8,86·10⁻³ kg/m, v = v_T tanh(gt/v_T): t = 4 s gives 10,5 (0,1 kg), 27,5 (1 kg), 37,5 (10 kg) m/s — matches the johtopäätös model answer and the exp-3 capture (27,5 m/s, v:t = 6,88 m/s²); vacuum v = gt, s = ½gt²; 80 m scale holds the 78,5 m fall.
- Experiments: exp-1 locks air and masses, varies t (0,5 s steps); exp-2 vacuum, t = 3 s, varies m_B; exp-3 air, t = 4 s, varies m_B with equal size; simState exposes vA, vB. Each setup isolates its variable.
- Exactly one correct option in pr-matka, pred-1, pred-2, exp-2, exp-3, virhe, check-1, check-c2; distractor feedback physically right.
- Figures: free-fall to scale (0; 4,9; 19,6; 44,1 m; intervals 4,9/14,7/24,5); vt-graph points and line pixel-checked (slope 9,81, Δv 19,6 over 2,0 s); data figure line slope 9,81, points match table.
- Model stated where used: "kun ilmanvastusta ei ole" in formula, summary, sim model box; sim values called model values, data labelled simulated, johtopäätös says experiments 1–2 only repeat v = gt.
- Scope: v = gt as a linear (t,v) model, no forces or Newton's laws; mass independence given as an experimental result, cause deferred.
- Units, m/s² for g, sig-fig reasons correct; acceleration not conflated with velocity anywhere.
