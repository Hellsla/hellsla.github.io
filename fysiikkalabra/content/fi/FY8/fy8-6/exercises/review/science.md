VERDICT: PASS
CONTENT-HASH: 86db7651c7e4bc48
SCOPE: delta added-exercise from ac413b952791b551 base 5b3ca4f81c77

## Blocking

## Polish
- solutions.md fy8-6-L2-09 Vastaus — "kolme merkitsevää numeroa kuten vakiossa c ja kuvaajan luetussa arvossa": the value read, 5,8, has two figures. Three are fair because the line passes exactly through the grid crossing (5,8; 2,30), so say that instead (or give 520 nm, which is also inside the 3 % tolerance).
- Earlier polish items not touched by this diff (L1-06, L2-06, L2-04, L1-07) still apply.

## Checked
- I recomputed both answers in one script from my own model, a line through (4,6; 1,80) and (7,0; 2,80). L2-09: f = 5,80·10^14 Hz, λ = c/f = 516,9 nm → 517 nm, green. L2-10: hf/e = 2,8953 V, line 2,800 V, ΔU = 0,0953 V → 0,095 V. Both match answers.py.
- figures.py ryhma: (5,8; 2,30) and (7,0; 2,80) are both exact grid crossings of the line. The grid is 0,2·10^14 Hz by 0,1 V, so both readings can be taken without guessing. The alt text gives the same two crossings and does not give away either answer.
- Figure data are realistic: the points sit 0,09–0,10 V below hc/(eλ) for 650–430 nm, which matches the brief's "noin 0,1 V in this chapter's data". The intercept is −0,117 V, so the solution's "noin 0,12 V" is right.
- L2-09 Järkevyys: the model gives 539 nm at 2,30 V, so the shorter λ read from the measured line agrees with the lesson's direction of the deviation.
- L2-10 c model answer: it gives the same mechanism and the same wording as the brief's Kaava section (method, temperature, current range, thermal energy, the difference varies between LEDs). No guardrail B issue.
- Tolerances: L2-09 3 % covers both 517 and 520 nm. L2-10 10 % covers a ±0,01 V reading error in the difference. Units are nm and V.
- Symbols U_k, f, λ, h, e, c and the constants are those of the brief. Both tasks stay within FY8 scope ("kynnysjännite ja aallonpituus").
- Both solutions are complete: principle, symbolic formula, conversion, substitution, rounding and check.
- The hash was 86db7651c7e4bc48 at both the start and the end.
