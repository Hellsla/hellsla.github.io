VERDICT: FAIL
CONTENT-HASH: f837f3909e24cfc0

## Blocking
- exercises.json (L3-04 `"answer": 73.4`) and lessons/FY4/fy4-6/answers.py (`sf(..., 3)`) — A: the answer box now holds three figures, but the solution's Vastaus rounds part c) to $73\,\text{m}$, "kaksi merkitsevää numeroa kuten kitkakertoimessa 0,45". So the key and the solution disagree, the same mismatch as fy4-13 L2-07 in round 1. Fix: key 73 with `sf(v0 ** 2 / (2 * acs), 2)` (|73 − 73,38|/73,38 = 0,5 %, inside the 0,03 tolerance). Keep "(laskettu 73,4 m)" in the Vastaus.

## Polish
- L2-05 and L2-03 — both fit $(N, F_\mu)$ through the origin to get μ. The overlap is acceptable, because L2-05 adds computing N from the mass (carried over).
- L3-05 — the fbd tag `error` still names an equation error, not a drawn diagram made `wrong=` (pedagogy's call).

## Checked
- L3-05 new data (30°, μ = 0,35): $a = 1{,}9315\,\text{m/s}^2$, $s = 8{,}69\,\text{m} \to 8{,}7$ (key 8.7). The student's version gives 1,47 → "≈ 1,5". $N = 169{,}9$ N, the kinetic friction is 59,47 N, and the student's μmg is 68,7 N. The voimakuvio sums to $m\overline{a}$ along the slope: 98,1 − 59,5 = 38,6 = 20 · 1,93. The data no longer repeat the lesson's example.
- L3-05: the sliding condition is now right (tan 30° > μ while sliding, and $\mu_0 < \tan 30^\circ$ from the task statement).
- L3-04: the solution now carries unrounded intermediates: $v_0^2 = 493{,}8$, $a_c = 3{,}365$, $s_c = 73{,}4$ m, and a) and b) give 33,6 m and 55,9 m. Recomputed 73,38 m. "Auton massaa" is fixed.
- L2-07 shows tan 25,4° = 0,4748 → 0,47.
- L1-06 options now use $F_{\mu 0}$, and exactly one option is correct.
- L2-06 now states that the pull is horizontal throughout.
