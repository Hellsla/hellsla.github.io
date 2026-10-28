VERDICT: FAIL
CONTENT-HASH: ca8d24e8bdfff5b9

## Blocking
- solutions.md:75 (L2-03) — "$A_\text{ha} = \dfrac{A_{\text{km}^2}\cdot k_1}{k_2}$" with abstract factors $k_1$ and $k_2$ is exactly the general conversion formula the teacher ruled out on 2026-10-28. Replace the unit by its value instead: $2{,}4\,\text{km}^2 = 2{,}4\cdot(1000\,\text{m})^2 = 2{,}4\cdot10^{6}\,\text{m}^2$. Then count how many hectares fit: $2{,}4\cdot10^{6}\,\text{m}^2 : 10^{4}\,\text{m}^2 = 240$, so the answer is 240 ha.
- solutions.md:5 (L1-01) and :15 (L1-02) — "$l_\text{mm} = x\cdot10^{-3}$" and "$s_\text{Mm} = x\cdot10^{-3}$" are general conversion formulas (same rule). Write the step as replacing the unit by its value: "µm:n paikalle $10^{-3}\,\text{mm}$" and "km:n paikalle $10^{-3}\,\text{Mm}$".

## Polish
- solutions.md:95–97 (L3-01) — "$L_\text{AU} = \dfrac{ct}{1\,\text{AU}}$" and dividing by "km/AU" read like a factor rule. Say how many AU fit: $9{,}462\cdot10^{12}\,\text{km} : 1{,}496\cdot10^{8}\,\text{km} = 6{,}325\cdot10^{4}$.

## Checked
- answers.py recomputed independently: all 12 answers agree (largest deviation 0,12 %, L1-03 rounded to 2 sf by design); the tolerances accept correct rounding.
- Significant-figure justifications correct (384 400 km read as 4 sf, 1920 px and 86 400 s exact).
- Reasonableness checks are real estimates (L3-03: 145 · 8,3 min ≈ 20 h one way).
- No ×, \times or slash divisions in operations; colon and \frac used correctly; units in LaTeX.
- Physics within FY1 scope (s = vt, t = s : c, N = ft).
