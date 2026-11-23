VERDICT: PASS
CONTENT-HASH: 227a47f287a871f2
none

## Blocking
(none)

## Polish
- solutions.md L3 task with open and closed tubes (line 228): the Kaava gives f1 = f_n/n and v = f1·2L, 4Lf1 without the basic step (L = λ/2 or λ/4, v = fλ); the other tasks now start from it, so add the two lines for consistency.
- Earlier polish still open: L3-01 single step, L2-04/L2-09 near-duplicates, L1-09 look-up at level 1.

## Checked
- Kaava now starts from the node/antinode condition (L = nλ/2, L = nλ/4 with odd n, L = λ/4 − e) and v = fλ, and simplifies symbolically before Sijoitus; chains are algebraically correct (f_n = n v/2L, v = 4Lf, L = 3v/2f3, Δf, f_c = f_o/2, L3 − L1 = λ).
- End-correction task: L1 = λ/4 − e, L3 = 5λ/4 − e gives λ = L3 − L1; easy to follow.
- Closed-tube two-frequency task: f_b − f_a = 2f1 follows from n and n+2 with odd n; correct.
- Substitutions, answers and tolerances unchanged.
