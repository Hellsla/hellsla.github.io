VERDICT: PASS
CONTENT-HASH: f628c9c4d2493275
Round: 1 (new task fy6-4-L2-08, ordering; the rest of the set was PASS before and is unchanged).

## Blocking

## Polish
- content/fi/FY6/fy6-4/exercises/solutions.md:220 — "B ja C vaihtavat paikkaa" is incomplete: forgetting to invert also makes D look like 100 Ω + 0,012 ≈ 100 Ω, so D moves before E as well — write "B ja C vaihtavat paikkaa ja D siirtyy E:n edelle" or drop D from the sentence explicitly ("rinnakkaisten kytkentöjen B ja C").
- content/fi/FY6/fy6-4/exercises/exercises.json:265 — connection C (three 330 Ω in parallel) is the same calculation as L1-05 in this set; consider e.g. three 300 Ω (100 Ω) so the order stays C < B < E.

## Checked
- Hash f628c9c4d2493275 at start and end.
- answers.py run against exercises.json: all 18 numeric answers agree within tolerance (one python call).
- L2-08 recomputed: A 550 Ω, B 132 Ω, C 110 Ω, D 265 Ω, E 150 Ω; order C, B, E, D, A matches `order` and `answer`; 1/R_B = 0,0076 1/Ω and 1/R_C = 0,0091 1/Ω are right.
- The prompt names the quantity and the direction (pienimmästä suurimpaan).
- The lesson's second warned mistake (every added resistor increases R) is what the order tests: C has the most resistors and the smallest R, and B lies below the single 150 Ω.
- Formulas (series sum, 1/R sum, R1R2/(R1+R2), mixed connection inside out) are the lesson's; wire resistance neglected is stated.
- Inline formula widths measured (KaTeX render at 17 px, 1.21 em, own script): widest 239 px. Page not rendered; the rest from text.
