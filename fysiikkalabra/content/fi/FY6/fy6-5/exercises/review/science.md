VERDICT: PASS
CONTENT-HASH: 22633f9efb51607f
Round: 2 (commit 57a66480d changed only the new task fy6-5-L2-08: two wrong-choice feedbacks, the correct reason's wording, and the current-law sentence in solutions.md).

## Blocking

## Polish
- content/fi/FY6/fy6-5/exercises/exercises.json:261 (carried over from round 1, optional) — no distractor carries this chapter's own warned mistakes (a resistor uses up current; the source voltage used for a branch); the task is mostly fy6-4 parallel-circuit physics. Keep, or make a later task carry the source-voltage mistake.

## Checked
- Hash 22633f9efb51607f at start and end.
- answers.py run against exercises.json: all 18 numeric answers agree within tolerance (one python call).
- Physics unchanged and recomputed: R_k = 10 Ω, U = 3,0 V, I = 0,15 / 0,10 / 0,050 A, sum 0,30 A.
- New correct reason "Haaroilla on sama jännite, joten pienemmän resistanssin haaran kautta kulkee suurempi virta" is true and rules out every wrong choice (equal split, largest current to largest R, full current in each branch); the solution's "kääntäen verrannollinen" is consistent with it and gives the value.
- New wrong-choice feedbacks are correct and no longer state the reason (same voltage, I = U/R): 0,10 A "ei jaa virtaa tasan, kun resistanssit ovat erisuuret"; 0,15 A "suurempi resistanssi vastustaa virtaa enemmän". "erisuuret" matches house usage (fy4-12, fy3-6).
- Reasons are 88–92 characters, similar in form; none alone hedged; the correct choice's feedback still only asks for the reason.
- Inline formula widths measured (KaTeX render at 17 px, 1.21 em, own script): widest 216 px; the split current-law sum 215 px (was 292 px). Page not rendered; the rest from text.
