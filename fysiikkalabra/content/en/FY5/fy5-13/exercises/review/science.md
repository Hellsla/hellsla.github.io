VERDICT: PASS
CONTENT-HASH: b9c26731e5db9e1f

## Blocking

## Polish
- exercises.json fy5-13-L1-07, feedback of the $600\,\text{Hz}$ option — "the factor $n$ is odd, because the natural frequencies are $f_n = n f_1$" gives no reason for the oddness. Fix: "because the tube's length must be an odd number of quarter wavelengths".
- solutions.md fy5-13-L1-09, Reasonableness — "positive … because helium is a lighter gas" skips a step. Fix: "because sound travels faster in helium (lighter molecules), and $f_1 \propto v$".

## Checked
- One script recomputed all 19 numeric answers from the task text with my own formulas (string and open tube $v/(2L)$, closed tube $v/(4L)$ with odd $n$, $L_3 - L_1 = \lambda$, the mean of $f/n$, $f_1^2/F$). Each one agrees with exercises.json and answers.py within the tolerance.
  - Results: L2-05 $122.8$, L2-06 $343.0$, L3-04 $199.0$, L3-05 $330.8\,\text{m/s}$ ($v_\text{A} = 330.9$, $v_\text{B} = 330.7$).
- Round-1 blocker fixed in L2-02. The task and the Principle now say the end correction is ignored. The check now states the cause correctly: the antinode lies slightly above the mouth, so the column is a little shorter than $\lambda/4$.
- The L3-02 rounding reason now names the nearest-hertz data.
- Figure `kuvio-tehtava` (1280 capture):
  - It shows four equal loops and five nodes, with the vibrator at 0 and the pulley node at $1.20\,\text{m}$.
  - It gives L2-04 ($60.0\,\text{m/s}$) and L2-09 ($31.25\,\text{Hz}$) their data, and it shows neither answer.
- L1-06, L1-07, L2-07 and L2-08 each have exactly one correct option, and the physics of every distractor's feedback is right.
- L2-06 b: $e = 0.45\,\text{cm}$, and the cause is right. The checks against $L_2$ and $L_3$ are real checks.
- L3-04 tests $f_1^2/F$ against $f_1/F$, gives $\sqrt{4} = 2$ for b), and flags the extrapolation to $120\,\text{N}$.
- L3-05 identifies the tubes from the 1:2:3 and 1:3:5 ratios. The swapped-type check ($165$ and $662\,\text{m/s}$) is real.
- Significant figures and their reasons hold: L2-01 is $5.4\,\text{Hz}$ from $7.0\,\text{m/s}$, and L1-08 and L1-09 have two figures. The units and tolerances fit.
- The scope is FY5 standing waves only, and every solution is solved symbolically before substitution.
- Hash unchanged at the end.
