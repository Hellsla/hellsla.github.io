VERDICT: PASS
CONTENT-HASH: 6f2cf62a1b9423b6

## Blocking

## Polish
- tests/sims/fy4-12.json (canvas assertion) — the 600×400 check now holds only on a wide screen, so nothing checks the phone canvas. This is acceptable: the change is layout only, and the physics assertions are unchanged and pass. — If wanted, assert `c.height===575` on a narrow root.
- inquiry.json exp-3, correct option — "ensin juoksija saavuttaa bussin" is right, but the juoksija also passes the bus (the gap changes sign). Fine (C); optionally "saavuttaa ja ohittaa".

## Checked
- One script recomputed every number from the task data with my own meeting-root model. All agree with the text and with lesson-answers.py: the figure (12 s, 36 m), the same-place pass (6,0 s, 36 m, 12 m/s, largest gap 9,0 m, both vt areas 9 m), the worked example (roots −2,0 s and 8,0 s, 64 m, 16 m/s, gap 25 m at 3,0 s), cases 1–5 (10 s and 50 m; −10 s; 4 ± √6 s = 1,55 s and 6,45 s), the transfer task (8,0 s, 96 m, 24 m/s), check-2 and its mistakes (6,0; 15; 30; 10 s), pr-paikka (25/50/10) and exit ticket 3.
- Round-2 polish is fixed. The exp-3 "Kerran" option ("ohittaa … pysyy edellä") is now consistent and still wrong, and its feedback is right. The gaps at 0, 2, 6 and 7 s are −5, +1, +1 and −1,5 m, so the sign changes twice. The siirto Periaate now reads "Kun ohitushetki tunnetaan".
- sim.js diff: only the layout changed (WIDE/NARROW lane, ruler and graph boxes, and the legend row). The physics and simState are untouched. GX, GY and X read the active box, so the graph and the ruler stay true to the model in both layouts. The 390 px captures show the axes and the starting positions correctly.
- Experiments: tapaus is locked and t is varied. 10 s and 8,0 s lie on the 0,5 s grid. xA, xB, vA, gap and meetings exist in simState.
- Each choice item has exactly one correct option, and every distractor's feedback gives the right reason.
- Theory, summary, contribution, model answers and exit ticket all say the same thing. The largest gap carries the condition "kun takana oleva lähtee hitaampana", and two positive roots are allowed.
- Scope: within FY4 "tasainen ja tasaisesti kiihtyvä suoraviivainen liike". The standing rules hold (LaTeX, \cdot, \overline{v}, blue v and orange a).
