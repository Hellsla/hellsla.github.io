VERDICT: PASS
CONTENT-HASH: a6262ad6a5a59e36
SCOPE: delta added-exercise from 166963488269ae93 base 8f23aa7ae3bd

## Blocking

## Polish
- solutions.md (fy6-16-L2-09, Järkevyys) — the second sentence recomputes the same product with rounded numbers, so it is not an independent check. A real check: about 4 kW is a plausible evening load for a house (sauna stove plus cooking), and 17 kWh in four hours is about 0,7 € per hour at 16 snt/kWh.
- exercises.json (fy6-16-L2-09) — L2-05 also gives an evening load of a house "ennen latausasemaa", but for 17–22 h with different values (2,1 … 6,8 kW). If both tasks mean the same house, the data disagree. "Erään omakotitalon" makes clear that they are different houses.

## Checked
- Hash a6262ad6a5a59e36 at start and end; I judged only fy6-16-L2-09 (delta added-exercise).
- figures.py draws steps of 2, 5, 7 and 3 kW, one hour each from 18 to 22. All of them lie on 1 kW grid lines, and the alt text gives the same values and states neither the energy nor the cost.
- Recomputed: W = ΣPΔt = (2 + 5 + 7 + 3) kW · 1,0 h = 17 kWh and K = aW = 0,16 €/kWh · 17 kWh = 2,72 €, the same as answers.py. The tolerance of 2 % covers the rounded answer 2,7 €.
- Physics: the energy is the area under the (t, P) graph, and the power is constant on each step. The house's own consumption is paid by the energy taken from the grid, so no efficiency enters here, which is right. This agrees with the brief's K = aW_verkko.
- The magnitudes are realistic: a peak of 7 kW stays under the 3 × 25 A limit of about 17 kW, as in this chapter's other tasks.
- The solution is complete: given and asked, the principle (rectangles), how the graph is read, the formula before the numbers, snt → €, the substitution, and the rounding reason (the graph readings).
- Scope: energy and cost in the household (FY6 sähköteho; FY2 kWh as prerequisite knowledge).
