VERDICT: PASS
CONTENT-HASH: f6871d16e360cf2a
SCOPE: delta added-exercise from 73724f23756ef0b4 base 5b3ca4f81c77

## Blocking

## Polish
- solutions.md fy8-6-L2-09 Answer — "three significant figures like the constant c and the value read from the graph": the reading 5.8 has two figures; three are justified only because the line meets the grid crossing exactly (5.80) — say that, or note the reading is good to about ±0.05·10^14 Hz (±1 %).
- solutions.md fy8-6-L2-10 Model answer (c) — the list of method factors (structure, current range, fit) does not by itself explain why the voltage is *lower*; the sign comes from the thermal energy the carriers bring (hf ≈ eU_k + a little), which is mentioned last — lead with that mechanism, keep the method factors as "and the value depends on the method".
- exercises.json fy8-6-L2-10 tolerance 0.1 — ±0.0095 V means a reading of 2.79 or 2.81 V (0.105 / 0.085 V) falls just outside; acceptable since the line passes exactly through the (7.0; 2.80) crossing, but 0.12 would forgive one-hundredth misreadings.
- Earlier polish items (L1-06, L2-06 b, L2-05, L2-08) still apply.

## Checked
- Hash f6871d16e360cf2a at start and end.
- Figure ryhma (figures.py and capture L2-16): line through (4.6; 1.80) and (7.0; 2.80), k = 1/2.4 V per 10^14 Hz; grid 0.2·10^14 Hz × 0.1 V, so 5.8 and 7.0, 2.30 and 2.80 are grid lines on which the line hits crossings; description gives the same information.
- L2-09 recomputed: f = 4.6 + 0.5·2.4 = 5.80·10^14 Hz, λ = c/f = 516.9 nm → 517 nm, answers.py agrees; 517 nm is green; hc/(e·2.30 V) = 539.1 nm and hc/(eλ) = 2.40 V > 2.30 V, so the reasonableness remark is right.
- L2-10 recomputed: line 2.800 V, hf/e = 2.8953 V, ΔU = 0.0953 V → 0.095 V, answers.py agrees; intercept −0.117 V ("about 0.12 V below zero") right; 3.3 % and c/f = 428 nm, 1240/428 = 2.90 V right.
- Data consistency: all six points lie 0.095–0.103 V below hf/e, matching the chapter's "about 0.1 V"; slope gives h = ek = 6.68·10^-34 J s, a realistic class result.
- Both solutions: principle (c = fλ; eU_k ≈ hf), symbolic form before substitution, unit J/C = V, graph reading described. Notation U_k, f, h, e as in the brief; within FY8 scope.
