VERDICT: PASS
CONTENT-HASH: 5575f15b7bd4bcfd

## Blocking

## Polish
- solutions.md:103 (L3-01) — Formula still reads "dose $= (\ldots) \cdot 100\,\%$" without the symbol, while Substitution now gives $D$ as a pure ratio and L3-05 (line 204) defines $D = \sum t_i/t_{\text{ref},i}$; write the Formula as "dose $D = \dfrac{t_1}{t_{\text{ref},1}} + \dfrac{t_2}{t_{\text{ref},2}}$ ($D = 1$ means $100\,\%$)" so formula and substitution match.

## Checked
light delta review (teacher 2026-11-07), L3-01 chain: HEAD~1 diff of solutions.md only. Recomputed t_ref,1 = 8 h/2¹ = 4.0 h, t_ref,2 = 8 h/2⁻¹ = 16 h, D = 1 + 0.25 = 1.25; 1.25 = 125 % is exact (% = 1/100). D as a dimensionless ratio (h/h) agrees with L3-05's D = Σ t_i/t_ref,i; answer 125 % and Reasonableness unchanged and right. Only the Formula line keeps the old ·100 % form (Polish).
