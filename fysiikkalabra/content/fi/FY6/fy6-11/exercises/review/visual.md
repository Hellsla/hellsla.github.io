VERDICT: FAIL
CONTENT-HASH: 50aa496a1262650f

## Blocking
- [Major] 11-13 (fy6-11-L2-05) solutions.md, **Vastaus:** line — the page's "Vastaus" chip (and so the answer the student is shown) reads $390\,\text{V}$, because the build takes the first quantity in the line, the range "(390 V – 408 V)"; the real answer is $4{,}0 \cdot 10^{2}\,\text{V}$ (exercises.json 400,1 V, solution 2401 V : 6) — a student who compares with the chip sees an answer that contradicts the model solution — fix: start the line with the result: "**Vastaus:** $4{,}0 \cdot 10^{2}\,\text{V}$, kaksi merkitsevää numeroa kuten testivarauksessa. c) Kenttä pienenee … tulo $E \cdot d$ pysyy lähes vakiona (…)", then rebuild and check the chip reads $4{,}0 \cdot 10^{2}\,\text{V}$. (The other 23 new tasks' chips match their answers.)

## Polish
- [Minor] 11-19 (L3-04) Vastaus — c) and d) form one paragraph of about 110 words; start d) on its own line.
- [Minor] 11-15 (L2-07) Sijoitus c) — "238,5 µN : 4 = 59,6 µN" and "E = …" share one chain, so the equals signs align across two steps; use two boxes.
- [Minor] 11-19 Kaava — "e ≈ suhteiden q : n keskiarvo" is plain words between formulas; write `e \approx \overline{q : n}` with the mean named in text.
- [Minor] 11-13, 11-15 — the F(d) and F(x) tasks have no plot; a small graph beside the solution would help (optional).

## Checked
- Opened open-exercises-1280 parts 7–9 (11-6 end, 11-7, 11-8), L2 parts 6–10 (11-13, 11-14, 11-15), L3 parts 5–9 (11-19, 11-20): MC, tables, solutions, chains; nothing clipped. Deterministic 360 px OK; no 360 px exercise captures exist.
- Compared the Vastaus chip of every new task in preview/fy6-11.html with exercises.json: only 11-13 differs.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
