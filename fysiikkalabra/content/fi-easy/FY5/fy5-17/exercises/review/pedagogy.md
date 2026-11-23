VERDICT: PASS
CONTENT-HASH: fb1a29be4e3f4801
none

## Blocking
(none)

## Polish
- solutions.md:45 — Kaava is only "v = √(gh)" with a remark; fine for a one-step task, keep it.
- The "Kohta a)" and "Kohta b)" paragraphs of the earthquake task are now split into shorter paragraphs; good. The a) paragraph is still long because it holds a dated example from the data page; a later edit could shorten it.

## Checked
- The diff in the packet shows the aligned rows without their line breaks; on disk each Kaava is an aligned block (25 blocks), so only the diff view is garbled.
- The echo-depth rows start from v = s/t, s = 2d, then solve d = vt/2. This shows why the distance is doubled instead of quoting "2d = vt".
- The seismic chain derives Δt = d(1/v_S − 1/v_P) and then d = v_P v_S Δt/(v_P − v_S); the same derivation is reused in the three-station task, followed by the circle subtraction x = (d_A² − d_B² + 120²)/240. Algebra correct.
- The bat case: s = vt = d + (d − v_lep t), so d = (v + v_lep)t/2, correct. The fat–muscle layer and shallow-water rows (λ2/λ1 = v2/v1 = √(h2/h1)) are correct, and the symbolic form is reached before Sijoitus.
- Sijoitus, answers and tolerances unchanged; the exercises.json change is only reflow.
