VERDICT: FAIL
CONTENT-HASH: cb6554f946268815

## Blocking
- exercises.json:91 (L3-02) — the task's data are a Markdown table inside the task text, which does not render: the 1280 px screenshot shows raw `| … |---|` pipes, so the (U, I) data cannot be read. This breaks the FY6 thread rule of 2026-11-04 — give the nine pairs as a list, e.g. "$(0\,\text{V};\ 3{,}30\,\text{A})$, …", or draw them as a figure.
- exercises.json:49 (L2-01), solutions.md:60 — (B) the answer 9,0 V assumes that no reverse current flows. Yet the solution's own Järkevyys says a typical LED is rated for only about 5 V in reverse and that 9,0 V may break it, and after breakdown the voltage across the LED is no longer 9,0 V. State the condition in the task: "Oleta, ettei LEDin läpi kulje estosuunnassa virtaa."

## Polish
- solutions.md:106 (L3-02) — "maksimitehopisteessä $U = RI$": Ohm's law holds for the load at every operating point, not only at the maximum. Write "kuormalle $U = RI$".
- solutions.md:24 (L1-03) — "diodin jännite on kynnysjännitteen suuruinen": the task gives 0,70 V directly. Say "diodin jännite on annettu $0{,}70\,\text{V}$, ja se muuttuu virran mukana vain vähän".

## Checked
- All 12 answers recomputed in one script with own formulas; all match answers.py.
- L3-02 powers 0…49,3…0 W; maximum at 17,0 V, 2,90 A → 5,86 Ω; data realistic.
- ex-led: the green model curve passes exactly (2,20 V; 10 mA) on the gridlines; description does not give the answer.
- Symbolic first, conversions by substitution, significant figures from the limiting datum, real reasonableness checks.
- Energy wording "sisäenergiaksi"; LaTeX units, \cdot, colon division; scope inside the lesson's formulas; units and tolerances fit.
