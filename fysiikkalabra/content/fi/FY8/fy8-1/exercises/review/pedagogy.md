VERDICT: PASS
CONTENT-HASH: cb48bd7706c41840

## Blocking
(none)

## Polish
- content/fi/FY8/fy8-1/exercises/exercises.json (fy8-1-L2-09) — the solution now gives $4{,}3 \cdot 10^{2}\,\text{nm}$ while the checked answer stays 428 (tolerance 4 %); a student answering 430 passes, so nothing breaks, but the shown answer and the solution's rounded answer differ in form — optional: leave as is, the solution names the calculated value 428 nm.

## Checked
- solutions.md L1-10 Järkevyys: "Pikaarvio" → "Pika-arvio" is the correct Finnish compound (hyphen between the same vowels); nothing else on the line changed.
- solutions.md L2-09 Vastaus: two significant figures now follow the graph reading $7{,}0 \cdot 10^{14}\,\text{Hz}$; the old line claimed three figures and "±1 %", which contradicted the data's precision. The new reasoning is one a student can follow, and the calculated value 428 nm is kept in view so the Järkevyys line (1240 : 428) still connects.
- L2-09 answer 428, tolerance 0.04: the rounded 430 nm (0,5 % off) is accepted; no trap.
- Notation $4{,}3 \cdot 10^{2}\,\text{nm}$: decimal comma, LaTeX number with unit, house form.
- exercises.json: the caption marker removal (teacher-approved) and re-broken chains carry no pedagogical change; task texts of L1-10, L2-08, L2-09 read as before.
- Method: text diff in context (solutions.md around the two hunks, the three exercise entries); captures not needed for a wording and rounding change.
