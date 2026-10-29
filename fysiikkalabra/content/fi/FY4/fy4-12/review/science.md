VERDICT: PASS
CONTENT-HASH: cbee12aed8d34c3a

## Blocking

## Polish
- inquiry.json:322 (exp-3, option "Kerran") — "juoksija saavuttaa bussin ja jää sen jälkeen pysyvästi bussin taakse" contradicts itself: reaching the bus and then falling back without passing would be a touch. The option is still wrong and its feedback is right. — For example: "Kerran: juoksija ohittaa bussin ja pysyy sen jälkeen edellä."
- inquiry.json:473 (siirto, Periaate) — "Ohitushetken jälkeen nopeus saadaan …" reads as "after the passing". — Write "Kun ohitushetki tunnetaan, nopeus saadaan …".
- lessons/FY4/fy4-12/figures.py:232 — the kaksi_karrya docstring says B starts "from 30 m", but the code draws it from 40 m. — Fix the comment.
- Sim canvas at 390 px (shots exp-*-390-1) — the ruler's "150" runs into "$x\ (\text{m})$", and the graph's "$x\ (\text{m})$" overlaps lane B. This is a layout problem, not a physics one.

## Checked
- One script recomputed every number from the task data with my own meeting-root model: the head-on figure (12 s, 36 m), the same-place pass (6,0 s, 36 m, 12 m/s, maximum gap 9,0 m), the worked example (roots −2,0 and 8,0 s, 64 m, 16 m/s, gap 25 m at 3,0 s), cases 1–5 (10 s/50 m; 5,0 s; −10 s; 4 ± √6 s), the transfer task (8,0 s, 96 m, 24 m/s), check-2 and its mistakes (6,0; 15; 30; 10 s), pr-paikka (25/50/10) and exit ticket 3. All agree with the text and lesson-answers.py.
- Round-1 B and A findings are fixed: the summary allows two positive roots, the largest gap carries "kun takana oleva lähtee hitaampana" (this is true for any constant accelerations, because the relative speed is linear in t), and check-3 states that the cyclist is ahead.
- Figures 2–6 and the example figure are to scale and match their data. The two vt areas are ±9 m.
- sim.js implements x = x0 + v0 t + at²/2 and the meeting roots on 0 < t ≤ 12 s. Every case stays on its axes. The Mallin oletukset box states the limits (points, constant a, model values).
- Experiments: tapaus is locked and t is varied. 10 s and 8,0 s lie on the 0,5 s slider grid. The keys xA, xB, vA, gap and meetings exist in simState.
- Every prediction, Etsi virhe, ei-kohtaa, exp-3 and check-1 has exactly one correct option. Each distractor's feedback gives the right reason.
- Model answers (johtopäätös, check-3) and the exit ticket agree with the theory.
- Standing rules: every symbol is in LaTeX (the canvas, readout and table headers render as LaTeX). Multiplication uses \cdot and × never appears. Vectors are \overline{v} and \overline{a}, with no \vec or \mathbf. Velocity arrows are blue (#1971c2) and acceleration arrows orange, distinct from the green and brown body colours. No forces are drawn here.
- Scope: within FY4 tasainen / tasaisesti kiihtyvä suoraviivainen liike.
