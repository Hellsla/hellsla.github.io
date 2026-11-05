VERDICT: PASS
CONTENT-HASH: 2949b01f2b88f424
Round: 1

## Blocking
(none)

## Polish
- exercises.json:275 / solutions.md:206 (L2-08) — "U-arvot on annettu kahdella [numerolla]", but $U = 0{,}09$ has one significant figure. Give the roof $U = 0{,}090\,\text{W/(m}^2\cdot\text{K)}$ (realistic for a modern yläpohja), and the 2-figure rounding then holds.
- solutions.md:206 — the Arvio checks only the largest and smallest; the close pair (yläpohja 216 W vs ikkunat 288 W) is the one a reader would want checked, e.g. "yläpohja 0,09 · 80 ≈ 7 W/K < ikkunat 1,2 · 8 ≈ 10 W/K". Optional.
- Not tied to the lesson's warned mistakes (greenhouse/ozone, sweater); it trains P = UAΔT with "U alone / A alone" orders as the traps. Optional.

## Checked
- New task L2-08 (järjestäminen), recomputed: ΔT = 21 − (−9) = 30 K; P = 60 W (ovi), 216 W (yläpohja), 288 W (ikkunat), 459 W (seinä); order ovi < yläpohja < ikkunat < seinä is right and robust (roof U from 0,085 to 0,095 keeps 204–228 W < 288 W).
- The claims "U alone" (yläpohja, seinä, ovi, ikkunat) and "A alone" (ovi, ikkunat, yläpohja, seinä) give wrong orders: true.
- Condition stated in the task (temperatures constant, same ΔT across every part), as the brief's lesson states for P = UAΔT; parts in parallel; notation P, U, A, ΔT as in the brief.
- Values realistic for a Finnish house (wall 0,17, window 1,0–1,2, door 1,0 W/(m²·K)).
- `prompt` names the quantity and the direction; answer string matches the solution (2-figure values).
- Renders: L2 screenshot 12 at 1280 px (solution). Phone width judged from text: each line "Seinä: UA = 15,3 W/K, P = 15,3 W/K · 30 K = 459 W" is two separate inline formulas, each ≤ ~230 px, so the line breaks at the comma.
- answers.py and other tasks unchanged since the previous PASS; hash identical at start and end.
