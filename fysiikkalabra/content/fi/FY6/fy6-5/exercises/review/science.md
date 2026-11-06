VERDICT: PASS
CONTENT-HASH: 38efe7d1d9cfde8d
Round: 1 (new task fy6-5-L2-08, two-stage choice with reasons; the rest of the set was PASS before and is unchanged).

## Blocking

## Polish
- content/fi/FY6/fy6-5/exercises/exercises.json:261 — no distractor carries this chapter's own warned mistakes (a resistor uses up current; the source voltage used for a branch); the task is mostly fy6-4 parallel-circuit physics. Optional: make the 0,15 A option's feedback name the "virta kuluu ensimmäisessä haarassa" idea, or add a series resistor in a later task so the source-voltage mistake can be a distractor.

## Checked
- Hash 38efe7d1d9cfde8d at start and end.
- answers.py run against exercises.json: all 18 numeric answers agree within tolerance (one python call); the new comment line in answers.py describes L2-08 correctly.
- L2-08 recomputed: 1/R_k = 1/20 + 1/30 + 1/60 = 6/60 1/Ω, R_k = 10 Ω, U = 3,0 V, I = 0,15 / 0,10 / 0,050 A, sum 0,30 A. Exactly one choice and one reason correct.
- Wrong choices: equal split (0,10 A), largest current to largest R (0,15 A), full current in every branch (0,30 A); each feedback says why with I = U/R or the current law. Wrong reasons: equal split by the junction, series-type voltage division, and a true statement that does not explain (current law sum).
- The correct choice's feedback only says "Oikein. Valitse seuraavaksi perustelu" and does not give the reason away; the four reasons are of similar length and form, none alone hedged.
- Ideal source and wires stated; the unknown source voltage forces the R_k route, which the lesson teaches (Kirchhoff's current law, same voltage over parallel branches).
- Inline formula widths measured (KaTeX render at 17 px, 1.21 em, own script): widest 292 px (solutions.md current-law sum), under 300 px. Page not rendered; the rest from text.
