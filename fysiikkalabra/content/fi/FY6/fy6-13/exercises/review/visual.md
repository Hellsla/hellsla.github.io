VERDICT: FAIL
CONTENT-HASH: 73c55536e9b48ef1

Delta: new L1-09 (13-9, true-or-false list of five statements).

## Blocking
- [Major] 13-9 statement 1 feedback, `Q = CU = 100 μF · 12 V = 1,2 mC` — one inline formula 307 px wide at 390 px in an indented feedback box; the card clips it to "= 1,2" and the unit mC is lost — the unit of the central result is unreadable — split it (`Q = CU` / `= 100 μF · 12 V = 1,2 mC`) or drop the substitution.
- [Major] 13-9 model answer, `W = 1/2 C U² = 1/2 · 100 · 10^-6 F · (12 V)²` — 338 px wide at 390 px, clipped at "(12" (the right edge 381 px vs 347 px card edge); the rest of the chain and the value are cut off — the 300 px rule is broken — break the chain into `W = ½CU²` and the substitution on its own line.

## Polish
- [Minor] 13-9 model answer closing paragraph gives the five statement verdicts as one run-on paragraph ("1 tosi: ... 2 epätosi: ..."); make it five short lines.
- [Minor] Statements 3 and 5 share the "24 V" scenario; fine, but both open with the same clause, so read quickly they look alike.

## Checked
- Renders (own script, 390 px and 360 px, every statement answered correctly, feedback, answer and solution open): card layout, true/false buttons and feedback inside the card; overflow found in the two formulas above (and at 360 px also more).
- Rendered: no feedback of a correct statement gives away a later stage; distractor statements catch the chapter's mistakes (current through the dielectric, C depends on U, W = QU instead of ½QU).
- Text only: compound words and the order of true/false (T, F, F, F, T) read in the JSON.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 3
