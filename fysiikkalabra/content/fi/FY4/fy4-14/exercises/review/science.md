VERDICT: PASS
CONTENT-HASH: 512f517d5051bf4f

## Blocking

## Polish
- exercises/solutions.md:97 (L2-04) — the 3-sf justification "kuten voimissa 450 N ja 180 N" is ambiguous, because trailing zeros (and 1200 kg) need not be significant. Either say the data are taken as three-figure values or give 0,53 m/s². 0,53 is within the 2 % tolerance.
- L1-05 — "tie työntää eteenpäin" alongside a separate rolling resistance from the same road is a fair simplification (C). Optionally add "renkaiden vierimisvastusta lukuun ottamatta" to the Periaate.

## Checked
- All 12 answers were recomputed with my own formulas. They equal exercises.json and answers.py: 735,75; 14,62; 6,31; 5,6145; 24; 0,050031; 266,7; 14,196; 0,525; 4,905; 6,00; 0,4965.
- Rounding versus tolerance: every answer rounded to the data's figures is within its tolerance (largest error 0,95 % on L2-04 at 2 sf, 0,7 % on L3-03 against 5 %).
- Signs: rising bodies give |a| = g + F_v/m; falling bodies give g − F_v/m; L3-02 Δa = 2F_v/m.
- L3-03 figure: the tanh curve with v_T = 14,2 m/s touches the tangent through (0; 2,0) and (2,0; 15,0) at P (0,96 s; 8,2 m/s), slope 6,5 m/s².
- Every solution names the forces and the positive direction before its equation and solves for the unknown in symbols. Its conversions (g → kg) are right, and its checks are real checks.
- Notation: \overline vectors, \cdot. Scope: F_v is given, never computed from v.
