VERDICT: FAIL
CONTENT-HASH: f790eb2be657d8e1

## Blocking
- exercises/solutions.md:37 (L1-04) — A, quantitative: the intermediate numerator $3{,}192 \cdot 10^{-12}\,\text{J}\,\text{m}$ is wrong; $3{,}0 \cdot 10^{-3}\,\text{J} \cdot 1064 \cdot 10^{-9}\,\text{m} = 3{,}192 \cdot 10^{-9}\,\text{J}\,\text{m}$, and the line's own quotient $\frac{3{,}192 \cdot 10^{-12}}{1{,}9865 \cdot 10^{-25}}$ would give $1{,}6 \cdot 10^{13}$, not the stated $1{,}6069 \cdot 10^{16}$ — write $3{,}192 \cdot 10^{-9}\,\text{J}\,\text{m}$. (Present before the colon-division edit; the final value and exercises.json are right.)

## Polish
- exercises.json (L2-02) — stores 1.6 while the solution answers 1,60 with three significant figures — store 1.60 or 1.605 (tolerance already covers it).

## Checked
- Content hash identical at start and end.
- Colon-division rewrites of L1-01, L1-03, L1-04: brackets group numerator and denominator correctly, operator precedence unambiguous; L1-01 gives 3,1382e-19 J = 1,9589 eV and L1-03 6,9274e-7 m = 692,74 nm, as written.
- All 12 answers recomputed in one script with my own formulas; exercises.json within tolerance and answers.py (lessons/FY8/fy8-7/answers.py) identical to mine for every task.
- Physics unchanged from the passed version: photon energy hc/λ, P = (N/t)·hf, quantum defect λp/λL, inversion to a ground-state lower level needs over N/2 ions, two 1064 nm photons → one 532 nm photon.
- Units, conversions and rounding by the limiting datum checked in every solution.
