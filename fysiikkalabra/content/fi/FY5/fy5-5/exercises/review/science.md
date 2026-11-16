VERDICT: PASS
CONTENT-HASH: b6940bfa43676459

## Blocking

## Polish
- exercises.json:327 and solutions.md:262 (L2-08): this task is not marked *Syventävä*, but the feedback of the reason "Kaikki kappaleet putoavat…" and the model answer explain it with the field strength $g = \gamma \tfrac{M}{r^2}$, which P3 makes extension content. The physics is right. Fix: say it with forces ("A:han vaikuttaa vain B:n veto, joka on pieni, koska B:n massa on pieni"), or keep the field sentence and mark it as extension.
- exercises.json level3: once P3 is applied, only L3-01 and L3-03 are not marked *Syventävä*. That leaves two core-path tasks at level 3, against a minimum of 3. Pedagogy should decide; there is no physics error.

## Checked
- The hash was the same at the start and at the end.
- One script recomputed all 19 numeric answers with my own formulas (γm₁m₂/r², γM/R², the neutral point d/(1+√(m/M)), ρ = gR²/(γ·4/3πR³), N = m(g − 4π²R/T²), the γ means of L2-06 and L2-07). Every value matches answers.py and exercises.json within the tolerance. L1-09 gives 315,35 → 3,2·10² N, and a student's 315 is still accepted.
- L3-05 a: a_n = 0,0337 m/s² and N = 606 N against mg = 608 N. Taking N toward the outside and mg − N = ma_n is the correct force model. g is stated in the task to be the same at the pole and the equator.
- L3-04: ρ = 5508 kg/m³, and Cavendish's 5448 kg/m³ is 1,1 % from it. The conclusion about the crust and the core is right.
- L2-09: NASA's 24,79 m/s² for Jupiter is γM/R² without rotation, so scaling it by (R/2R)² is valid. Earth's 9,80 in the figure (NASA, no rotation) against 9,81 in the tasks is explained in the lesson (P9).
- Significant figures (P7): 200 m, 1025 kg and 6378 km keep their trailing zeros as significant. Each answer's stated limiting datum is the real one, including 85 kg (two figures) in L1-09 and 6,0 h in L3-05.
- The *Syventävä tehtävä* mark is on every task that needs g = γM/r² (L1-03, L1-09, L2-02, L2-04, L2-05, L2-07, L2-09, L3-02, L3-04, L3-05). L1-04, L2-01, L2-03, L3-01 and L3-03 use only the law.
- Multiple choice: exactly one option is correct in L1-06, L1-07, L1-08 and L2-08, and its reason is the right one. Every distractor's feedback is correct.
