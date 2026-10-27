VERDICT: PASS
CONTENT-HASH: 1587ffd88fdf3c0f

## Blocking

## Polish
- solutions.md:70 (L2-02 Järkevyys) — a fall height of 11,5 m (½gt², a formula this lesson has not taught yet) is about the fourth floor, not the third-floor window — say "noin neljännen kerroksen korkeus" or drop the height sentence and keep the time estimate only.

## Checked
- Round 2 diff only (hash 1587ffd88fdf3c0f at start and end); the rest is unchanged since the round-1 PASS.
- L2-02: 54,0 km/h = 15,0 m/s, t = v/g = 1,529 s → 1,53 s (3 sf); answers.py, exercises.json and solutions.md agree; no longer the example's shape.
- L3-03: t = 3,00 s, 9,81·3,00 = 29,43 m/s, Δv = 4,43 → 4,4 m/s; rounding argument (decimals of 25,0) now correct.
- Exit ticket q3: premise and answer now say vacuum for equal fall and air slowing the feather; consistent with Koe 2 and Koe 3.
- exp-1/2/3 units "(tyhjiö)"/"(ilma)" match initial ilma = 0/0/1 and the sim's 0 = tyhjiö, 1 = ilma.
- Data question: mistake value 10 removed; remaining mistake 0,1 is outside tolerance and names its error.
- Conclusion model answer: added sentence that Koe 1–2 are model values that reproduce v = gt rather than prove it is correct.
- answers.py: unused t_d/v_d removed; all 18 values recomputed and match.
- reflect and virhe marked optional; no physics change.
