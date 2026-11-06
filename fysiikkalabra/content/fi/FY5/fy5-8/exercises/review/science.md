VERDICT: FAIL
CONTENT-HASH: 06bb76b9d2209c38

## Blocking
- fy5-8/exercises/exercises.json:267 (L2-08) — The correct option (third) is the only one that mentions the measurement uncertainty. In a type-10 data task, a student can pick it by form alone (FY2 lesson). — Make option 2 bring in the uncertainty as a wrong idea, for example "…suhde $F_\text{v}/x$ on siinä suurin, $25{,}5\,\text{N/m}$, ja ero muihin riveihin on suurempi kuin lukeman epävarmuus $0{,}05\,\text{N}$". Its feedback then names the unit mismatch: N/m compared with N, when the ratio's uncertainty here is ±1,3 N/m.

## Polish
- exercises.json L2-08 choices — No distractor carries a mistake the lesson warns about. The method warnings in "Jousivakio mittauksesta" fit a data task: reading the slope from two neighbouring raw points, and total length instead of extension (the bank plan says "venymä vs. kokonaispituus"). One of these could replace option 1 or option 4.
- solutions.md:270 — The bare "$\Delta$" has no quantity. Write $\Delta\!\left(\tfrac{F_\text{v}}{x}\right)$, or name it in the text before it ("suhteen epävarmuus").

## Checked
- New task L2-08 (type 10): I recomputed every row. The ratios are 24,5 / 25,5 / 24,5 / 25,0 / 25,1 N/m, with uncertainties 0,05 N/x = ±2,5 / 1,25 / 0,83 / 0,63 / 0,50 N/m. The value 25 N/m lies inside every interval, so the correct key is right.
- The guardrails hold. The line goes through the origin for a physical reason (F_v = kx, the spring at rest length). The slope is read from two points on the fitted line. The uncertainty ±0,05 N is larger than the 0,01 N resolution, which is consistent. "Erot mahtuvat mittausepävarmuuteen" does not claim the values are equal.
- The correct option's feedback gives no reason it should not. The cm→N/cm distractor is real physics.
- The data caption is short, and the table uses decimal points as the README schema says.
- Formula chains in the solution are short two-line aligned blocks. From the text they fit 300 px. I did not render them.
- The scope uses F_v = kx from this chapter and simple uncertainty division from FY1 measurement.
- answers.py ran once. All 22 numeric answers in exercises.json agree within tolerance (one script).
- The hash was the same at the start and at the end.
