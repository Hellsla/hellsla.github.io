VERDICT: PASS
CONTENT-HASH: 1793c2661297d3bf
SCOPE: delta added-exercise from 0d76aa1261e326bd base b2eac257e05e

## Blocking

## Polish
- exercises/solutions.md (fy3-6-L2-10, Järkevyys) — "Siksi ilmiö vaatii jotakin, mikä muuttaa vertailua, kuten haihtumisen": optional to name one or two of the other routes from part c) (contact with the shelf, supercooling of the cold sample) here too, so that evaporation does not read as the only explanation.
- fy3-6-L2-10 b) — the answer field stores 170 for 167,6 kJ. Tolerance 0,02 accepts 167,6 and 168 (1,4 % off), so this is fine. If the shown answer should match the exact value, 168 with the same tolerance would also do.

## Checked
- I recomputed Q = c m |ΔT| = 4190 · 0,50 kg · 80 K = 167 600 J ≈ 170 kJ myself. answers.py, the solution and the answer field agree; the unit is kJ, the value positive as the task asks, and the tolerance fits two significant figures.
- The law's conditions are stated in the task and the solution: no change of state over 80 → 0 °C, no evaporation. Periaate says that freezing itself is not covered by Q = cmΔT (guardrail).
- Comparison: from 20 °C the same water gives out 41 900 J (exactly a quarter), and the difference is 125 700 J. Recomputed, right.
- Against the source facts: Mpemba effect named; hot water freezes faster only under special conditions; the explanation is evaporation in a shallow bowl, plus flows, dissolved gases and impurities; the article gives no temperatures, amounts or times. All stated correctly. The headline-versus-text point is made, and the solution states the lack of consensus without inventing data.
- c) mechanisms (energy carried off by evaporation, smaller mass, area, lid, container material and heat capacity C = cm, frost under the warm container) are physically right.
- d) experiment: the same mass and containers, the same place, "frozen" defined beforehand, T(t) and mass measured before and after, one factor at a time (lid), repeats. Complete and controlled.
- Notation (Q, c, m, ΔT, C = cm, 4190 J/(kg·K)) matches the brief. Inside FY3 central contents.
- Hash the same at start and end.
