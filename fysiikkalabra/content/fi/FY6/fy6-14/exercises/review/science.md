VERDICT: FAIL
CONTENT-HASH: cb6554f946268815

## Blocking
- exercises.json:91 (L3-02) — the task's data are a Markdown table inside the task text, which does not render: the 1280 px screenshot shows raw `| … |---|` pipes, so the (U, I) data cannot be read. This breaks the FY6 thread rule of 2026-11-04 — give the nine pairs as a list, e.g. "$(0\,\text{V};\ 3{,}30\,\text{A})$, …", or draw them as a figure.
- exercises.json:49 (L2-01), solutions.md:60 — (B) the answer 9,0 V assumes that no reverse current flows. Yet the solution's own Järkevyys says a typical LED is rated for only about 5 V in reverse and that 9,0 V may break it, and after breakdown the voltage across the LED is no longer 9,0 V. State the condition in the task: "Oleta, ettei LEDin läpi kulje estosuunnassa virtaa."

## Polish
- solutions.md:106 (L3-02) — "maksimitehopisteessä $U = RI$": Ohm's law holds for the load at every operating point, not only at the maximum. Write "kuormalle $U = RI$".
- solutions.md:24 (L1-03) — "diodin jännite on kynnysjännitteen suuruinen": the task gives 0,70 V directly. Say "diodin jännite on annettu $0{,}70\,\text{V}$, ja se muuttuu virran mukana vain vähän".

## Checked
- I recomputed all 12 answers in one script with my own formulas. Each one matches answers.py: 30 mW, 95 Ω, 8,3 mA, 94,5 W, 22 mW, 9,0 V, 250 Ω, 20,3 %, 7,56 kJ, 36 %, 5,86 Ω and 25 %.
- L3-02 powers: 0; 32,5; 44,5; 48,8; 49,3; 45,9; 36,1; 19,0; 0 W. The maximum is at 17,0 V and 2,90 A, giving 5,86 Ω. The data are realistic (I_k 3,3 A, U_t 21 V).
- In the ex-led figure the green LED's model curve passes exactly through (2,20 V; 10 mA), on the gridlines, and ends at 2,26 V and 30 mA. The figure's description does not give the answer away.
- Every solution solves symbolically before substituting, and the conversions are done by substitution (1,0 kΩ = 1,0 · 1000 Ω; 6,0 h = 6,0 · 3600 s).
- Significant figures follow the limiting datum in each answer (L2-03: 20 % from 1,6 m²; L2-04: 7,6 kJ).
- Every reasonableness check is a real one: power balance, the Wh cross-check, a single LED versus a series string, the share of the supply voltage.
- Energy wording: "etuvastusten sisäenergiaksi" is used. Units are in LaTeX, products use \cdot, and divisions in the prose use a colon.
- Scope: every task stays inside the lesson's formulas (the series resistor, P = UI, η = P : (GA), E = Pt).
- Units and tolerances fit the data.
