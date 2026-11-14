VERDICT: PASS
CONTENT-HASH: a9fa68c9a1a5eb01
SCOPE: delta added-exercise from 279de6f0ff1eeacc base 8f23aa7ae3bd

## Blocking

## Polish
- solutions.md (fy6-14-L2-09, Kuvaajan lukeminen) — "se kulkee 200 mA:n ruudukkoviivalla" is slightly stronger than the drawing: the model current at 4,0 V is 198,7 mA. "lähes 200 mA:n viivalla" is exact, and the answer stays the same.

## Checked
- Hash a9fa68c9a1a5eb01 at start and end; I judged only fy6-14-L2-09 (delta added-exercise).
- I evaluated the figure model in figures.py myself (M_PV = 0,40 V, I_sc = 0,200 A, U_oc = 6,0 V):
  - I(4,0 V) = 198,7 mA, and I(3,9–4,1 V) = 198,3–199,0 mA, so the reading near 4 V is robust.
  - P = 4,0 V · 0,200 A = 0,80 W, which equals answers.py (0,795 W with the model current).
  - The tolerance of 4 % covers readings from about 192 to 208 mA.
- The same model has its maximum at 4,96 V, 185 mA and 0,918 W. This agrees with the brief's panel (about 5,0 V, 184 mA, 0,92 W), so the solution's comparison with 0,92 W is consistent and correct.
- Physics: P = UI at the operating point, as the brief teaches. The check uses the brief's point that I_sc and U_oc never occur together (1,2 W is an upper bound), and the result is below the maximum power point, as it should be.
- The alt text gives the shape (about 200 mA, flat up to about 4 V) and so serves a reader who cannot see the graph. It marks no power and no point, so it does not give away the answer.
- The task states that the irradiance is constant, which is the condition for using one (U, I) curve.
- The solution is complete: given and asked, principle, how the graph is read, the formula, mA → A, the substitution, the rounding reason and a real check.
- Scope: aurinkokenno as a circuit component (FY6 puolijohteet, komponentteina virtapiirissä); no materials physics is needed.
