VERDICT: PASS
CONTENT-HASH: 0c746c938ac9ccb7

## Blocking

## Polish
- content/fi/FY6/fy6-14/exercises/solutions.md (L2-09 Järkevyys) — "kuvan paneelin suurinta tehoa ($0{,}92\,\text{W}$)" refers to the lesson's figure, which the task's own figure does not show (same model: ISC 0,200 A, UOC 6,0 V, P_max 0,918 W at 5,0 V, so the number is right) — say "luvun teoriaosan kuvan paneelin" or compute it from this curve.
- exercises.json L2-08 — the correct option's feedback "Oikein: vain LED A palaa." only repeats the option; one clause on why (anodi plusnavan puolella vain haarassa 1) would help; the reason stage covers it, so not blocking.
- exercises.json L1-05 — tolerance 0.02 on 22 mW: a reading of 2,15 V or 2,25 V (half a 0,2 V cell off) lands at 2,3 % ("Lähellä"). The curve meets the gridline crossing exactly, so it is acceptable, but 0.03 would be kinder.

## Checked
- All 20 numeric/choice answers recomputed independently in one script from the task texts: every value matches answers.py (L3-04 sum H 1027 kWh/m², production 4683 kWh, consumption 5340 kWh, 87,7 %).
- L3-04 c: deficit months recomputed (Jan–Mar, Oct–Dec; Sep 388 > 370 and Apr 547 > 400 are surpluses); 3370 kWh vs 853 kWh, deficit 2517 kWh = 47 %; "vähintään" correct.
- L3-05: linear intersection 2,020 V / 13,78 mA; an exponential fit between the table rows gives 13,76 mA, inside tolerance 0.05; threshold extrapolation 2,00 V right; c) 0,10 V ≈ 5 % right.
- L3-02 and L2-06: P = UI for every row; maxima 49,3 W (5,86 Ω) and 181 mW (22 Ω); table U:I agrees with the listed R within rounding.
- Figures: ex-led passes (2,20 V; 10 mA) exactly (i_led reference point); ex-kenno gives 198,7 mA at 4,0 V, so 200 mA read on the gridline is right; neither description gives the answer away.
- L1-06, L1-07, L2-08: exactly one correct option; every distractor really wrong and its feedback's physics right (forward/reverse by anode side, parallel branches independent, series diode blocks the lamp).
- L2-01: reverse direction, I = 0, U_R = 0, U_D = U stated as an assumption in the task; the 5 V reverse-rating remark is correct.
- Rounding per P7: limiting data named correctly (1,6 m² in L2-03, 19 %/24 m² in L3-04, 3,1 V difference in L1-02/L2-05); every rounded answer within tolerance.
- Solutions: principle → symbolic form → conversion → substitution → answer → check in every task; notation (U_D, P_R, G, A, η) as in the brief.
- Scope: component level only, no p–n microphysics; all within FY6 central contents.
