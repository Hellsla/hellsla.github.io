VERDICT: PASS
CONTENT-HASH: 33dfc521a544302e
## Blocking

## Polish
- exercises/solutions.md:272 (L2-06) — the substitution shows $\mu = 0.295$ and the answer rounds it to $0.29$. The exact value is $2.167/7.358 = 0.2945$, so 0.29 is right, but the shown intermediate value looks as if it rounds to 0.30 — write $0.294$ (or $0.2945$); the comment in answers.py says 0.295 too.
- exercises/solutions.md:160 (L2-04) — the diagram draws $F_\mu = \mu_0 N = 48.22\,\text{N}$ together with an acceleration down the slope. Once the box slides, the friction is $\mu N$ (μ is not given), not $\mu_0 N$ — draw the comparison diagram without `a alas`, or say that it shows the upper limit compared with $G_x$ at the moment of release.
- exercises/solutions.md:99 (L2-01) — the reasonableness check compares with "a plastic sled and snow", but the task says nothing about the material — say "a sled and snow".

## Checked
- I recomputed every numeric answer in one script with my own formulas and it agrees with exercises.json within tolerance: L1-01 259.2, L1-02 35.3, L1-03 0.306, L1-04 7.37, L1-05 58.9, L1-07 220.7 → 230 N (rounded up as an "at least" value per P7, tolerance 0.05), L1-09 6.18, L2-01 0.134, L2-02 0.807, L2-03 0.2145 (least squares through the origin), L2-04 8.05, L2-05 0.416, L2-06 0.2945 (μ0 0.449), L2-07 0.4748, L2-09 2.10, L3-01 0.357 → at least 0.36, L3-02 0.795, L3-03 0.330, L3-04 33.6/55.9/73.4 m, L3-05 8.69 m. answers.py output equals exercises.json for every id.
- L2-08 order B (30 N) < C (44.1) < A (58.9) < D (122.6). D's upper limit is 148.7 N and B's 196 N, so both really stay at rest.
- L1-06 and L1-08: exactly one correct option each. Each distractor's feedback names the right physics.
- L3-05: the student's error ($N = mg$, which gives $a = 1.47\,\text{m/s}^2$) is the one described. Friction 69 N against 59 N is right.
- L3-01: friction points forward, the only horizontal force. L3-02: the friction is down the slope while the puck slides up.
- Diagrams (voimakuvio blocks): the magnitudes match the computed forces. The velocity and acceleration are not drawn as forces, and the components are dashed and not double-counted.
- mittaus figure points = MITTAUS = the data used in answers.py.
- The MAFY steel–ice value 0.014 is used consistently (tolerance 4 %).
