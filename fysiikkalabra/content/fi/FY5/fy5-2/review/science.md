VERDICT: PASS
CONTENT-HASH: 3739f2bb63324abb

## Blocking

## Polish
- lesson.md:264 — "momentin antaa kappaletta vastaan kohtisuora komponentti kerrottuna etäisyydellä momenttipisteestä" is true only for a rod-like body with the moment point on its line (as in every task here); for a general body the arm is the distance to the line of action — add "sauvamaiselle kappaleelle (lankku, tanko)" or similar (B-type, minor).
- inquiry.json:365 (tarkistus-1, distractor "yläreuna on siirtynyt pohjan reunan ulkopuolelle") — for a uniform box the whole top edge passes the pivot exactly when the CoM does (diagonal vertical), so the option is only clearly wrong if read as the front top edge; write "yläreunan etureuna" so exactly one option is unambiguously right.

## Checked
- Worked example (hirsi): N_B = 392 N, N_A = 196 N recomputed; figure arrows to scale (39 : 78.5 : 117.5 px), ccw arc correct.
- Figure "lankku" (N1 : N2 = 1 : 1.5 vs r1 : r2 = 1.5 : 1, sum = G) and "kaatuu" (30° slope, 150 px/m boxes, plumb lines land inside / outside the base; tipping angles 45° and 20.6°) are to scale as claimed.
- ennuste-1/koe-1: 98.1/98.1, 78.5/117.7, 49.1/147.2 N; ennuste-2/koe-2: N1 = 47.1 N at 3.2 m, 0 at 3.5 m, x_pp = 3.0 m; every option's feedback number correct, exactly one correct option each.
- virhe: correct N1 = 78.5 N, N2 = 117.7 N; student figure has equal arrows summing to G as stated; distractor feedback correct.
- piirra/siirto: F_p = 1079 N (both moment points), N = 1962 N; mistakes 1962, 981, 883 N reproduce the named errors; model figure lauta-voimat to scale (N = sum of the three downward arrows).
- tarkistus-2: 294 N; mistakes 188 N, 235 N; kertaus 16 Nm.
- sim.js: ΣM about support 1 and ΣF implemented correctly, tipping when a support force would be negative, tip direction right, one force scale per box mass; simState gives N1, N2, xpp, kaatuu at the experiments' settings; slider ranges cover all suggested values.
- Scope: static equilibrium, no ω or rotational dynamics; force diagrams show only forces on the plank, box force (not box weight) on the plank.
- lesson-answers.py matches my recomputation for every lesson/inquiry number.
- Glossary, summary, exit ticket and model answers agree.
