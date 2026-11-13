VERDICT: PASS
CONTENT-HASH: abc777e3a72f3bf7
SCOPE: delta added-exercise from 969eff4b4ef9e204 base 89bcb63b7431

## Blocking
(none)

## Polish
- solutions.md (L2-09) — symbols $Q_\text{vesi}$, $Q_\text{lämm}$, $Q_\text{kaikki}$ differ from the brief's $Q_\text{v}$, $Q_\text{j,läm}$, $Q_\text{j}$; using the lesson's names would tie the task to its case list (case 2: $Q_\text{j,läm} \le Q_\text{v} \le Q_\text{j}$).
- solutions.md (L2-09) Periaate — the 0 °C conclusion needs both $Q_\text{v} \ge Q_\text{j,läm}$ and $Q_\text{v} < Q_\text{j}$; the first is shown only in the reading step. One clause in Periaate would state the full condition where the principle is given.

## Checked
- Only L1-09 and L2-09 judged (delta added-exercise); the rest unchanged per packet.
- L1-09 recomputed: $Q = sm = 333 \cdot 0{,}080 = 26{,}64$ kJ → 27 kJ; with the lesson's 334 kJ/kg 26,72 kJ, both inside tolerance 0.04. MAFY 333 kJ/kg matches docs/mafy-arvot.tsv (VERIFIED); the solution explains the 334 vs 333 difference.
- L1-09 conditions: ice already at 0 °C and melt water at 0 °C stated, so $Q = sm$ alone applies; two figures from 80 g; check (≈ 25 K warming of 0,25 kg water) right.
- L2-09 recomputed: heat left for melting $25 - 5 = 20$ kJ $< 60$ kJ → ice remains, $T = 0$ °C; melted $20/334 = 59{,}9$ g, all ice $60/334 = 179{,}6$ g, left 119,8 g; answers.py 119,76.
- L2-09 data realistic: 5 kJ for 180 g ice means it starts at about −13 °C (freezer), 25 kJ ≈ 0,30 kg water at 20 °C.
- Isolation ("lämpöä ei siirry astiaan eikä ympäristöön") and $s$ given in the task; the boundary-case logic matches the brief's case 2 and the guardrail.
- figures.py energy-bars: bars end at 25, 5, 60 kJ on 5 kJ gridlines, to scale (6,6 px/kJ from one origin); description gives the same values; neither gives the remaining mass.
- Both solutions complete (given/asked, principle with reason, symbolic before numbers, conversions, substitution with units, rounding reason, independent check 2/3 · 180 g).
- Units kJ and g, tolerances fit; inside FY3 (olomuodon muutokset).
- Hash identical at start and end.
