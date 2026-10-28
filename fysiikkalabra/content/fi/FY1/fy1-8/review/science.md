VERDICT: PASS
CONTENT-HASH: 31410c8eab37e2d2

## Blocking

## Polish
- inquiry.json:68 — ennuste-1, correct option's feedback `0{,}2 : 1{,}0 = 20\,\%` has no units on the operands (dimensionless result, so not wrong) — `0{,}2\,\text{s} : 1{,}0\,\text{s} = 20\,\%`, matching the other colon chains.
- inquiry.json:110 / 120–133 — graafi: the text calls the horizontal bars "ajan epävarmuudet $\Delta t$" and two sentences later uses $\Delta t$ as the time interval in the slope $\Delta s : \Delta t$ (hints, mistake feedback and solution likewise: $\Delta t = 5{,}0\,\text{s} - 0\,\text{s}$). Same symbol, two meanings in one task — keep $\Delta t$ for the uncertainty (teacher's rule) and write the slope as $\dfrac{s_2 - s_1}{t_2 - t_1}$ here, or say once that in the slope $\Delta$ means change.

## Checked
- Round-1 blocking fixed: inquiry.json:40 `(4{,}9\,\text{s} - 4{,}6\,\text{s}) : 2 = 0{,}15\,\text{s}` and :195 `0{,}60\,\tfrac{\text{m}}{\text{s}} \cdot 0{,}2\,\text{s} : 0{,}050 = 2{,}4\,\text{m}` now dimensionally correct; round-1 polish (siirto units at :231, "parin senttimetrin" at :197) also done.
- Notation sweep: no `×`/`\times`; every inline division is `:` with units on operands (except :68 above); remaining `/` are unit fractions (m/s, s/m); display fractions use `\frac`; uncertainty written $\Delta t$ throughout.
- Formulas ε = Δt/t and t ≥ Δt/ε_max correct, condition (Δt ≈ constant, reaction time) stated; inside FY1 (measurement reliability, linear model s = vt).
- Worked example: symbolic first; 0,2 s : 0,050 = 4 s, 0,42 · 4 = 1,68 → 1,7 m with rounding justified; check 4,05 s, 4,9 %, 0,50 m → 1,2 s, 17 %.
- Group B table recomputed: means, half-ranges, ε 11,8→12 / 6,1 / 2,8 / 3,2 / 2,5 %, v 0,39–0,42 m/s; A 0,50 ± 0,10, B ±0,013, lowest 0,39 ± 0,05.
- kertaus 23,7 s : 5 = 4,74 s, half-range 0,15 → 0,2 s; graafi 0,42 (mistakes 2,4 and 2,1); virhe 2,4 m vs 0,024 m; siirto 14 m (0,14, 10); tarkistus-2 2,0 % (4,0, 0,02); exit ticket 10 s; suunnittele model 1,6 m at 0,4 m/s = 4 s.
- Figures to scale: setup 150 px/m (2,00 m bracket); ε = 0,2 s : t curve at 1, 4, 10 s = 20, 5, 2 %; graafi points, ±Δt bars (±0,10/0,15 s) and fitted line slope 0,419 m/s through (5,0 s; 2,1 m).
- Every correct option and feedback in inquiry.json and exit-ticket.json physically right; reilu-koe isolates one variable correctly.
- Hash identical at start and end.
