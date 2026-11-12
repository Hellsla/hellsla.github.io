VERDICT: FAIL
CONTENT-HASH: 90ecbf52970d1698
Mode: delta
Round: 1

## Blocking
- content/fi/FY2/fy2-1/exercises/exercises.json:156 (solutions.md:67, answers.py L1-10) — A, scope: L1-10 rests on $E = c\,m\,\Delta T$, which the FY2 scope notes exclude ("FY2 has no Q = c m Delta T"; FY3 teaches it) and the brief's lesson does not teach. Giving the formula in the task does not bring it into scope. The solution also calls the water "eristetty" while electrical energy flows into it, which contradicts the lesson's definition. — Fix: remove L1-10 from fy2-1 (it belongs in the FY3 heat-capacity chapter, with the condition "no change of state"), or replace it with a MAFY lookup task that uses only $E_\text{alussa} = E_\text{lopussa}$.

## Polish
- solutions.md:147 (L2-08 Järkevyys) — "B on rinteen puolivälissä" does not match the figure: B is at 3/7 of the rim height (57 % of the drop, about 39 % of the path), and friction's share need not follow either. Drop that reason and keep the sum check.
- solutions.md L2-08 Vastaus — a reading to the nearest 100 J does not support "kaksi merkitsevää numeroa"; "pyöristetään kokonaisiin prosentteihin" is more honest.
- Earlier items (L1-09 "likimain eristetyn", L3-04 c), L1-07 option 3) still open.

## Checked
- Hash 90ecbf52970d1698 at start and end; only L1-10 and L2-08 judged.
- L1-10 recomputed: $4{,}19 \cdot 0{,}50 \cdot 40 = 83{,}8\,\text{kJ}$ (83,6 kJ with 4,18), and 84 kJ is within tolerance. The 2 kW check gives 41,9 s, which is correct. The arithmetic is fine; scope is the issue.
- L2-08 recomputed: $700 - (300+300) = 100\,\text{J}$, $p = 14{,}29\,\%$, and 14 % is within 2,1 % (tolerance 3 %). The C check gives 200 J = 28,6 % ≈ 29 %, which is correct.
- answers.py prints 83.8 and 14.285714, the same as exercises.json.
- Figure kitka-pylvaat: the FRICTION data match the solution's readings, B's drawn height (u² = 3/7) matches 300 J of 700 J, and the description carries the same values. No thermal-energy bar or total is drawn, so the figure does not give the answer away.
- L2-08 physics: the system is isolated and friction converts mechanical energy into thermal energy without creating any, as in the brief's worked example. The formula is solved symbolically first.
