VERDICT: FAIL
CONTENT-HASH: d683ac7a621baa2e

## Blocking
- [Major] exercises.json fy6-7-L2-07 task text (open-exercises-L2-1280-9) — "Mittarin lukema oli alussa $0.00\,\text{kWh}$" is set with a decimal point (renders "0.00 kWh"); every other number in the chapter has the Finnish decimal comma, and the table below it shows "0,00" — write `$0{,}00\,\text{kWh}$` (JSON: `$0{,}00\\,\\text{kWh}$`).

## Polish
- [Minor] solutions.md fy6-7-L3-04 Sijoitus (L3-1280-5) — the parenthetical "(esimerkiksi $1{,}2\,\text{kWh} \cdot 3{,}9\,\tfrac{\text{snt}}{\text{kWh}} = 4{,}68\,\text{snt}$)." is turned into a display block mid-sentence, leaving ")." orphaned on its own line — take the example out of the parentheses ("Esimerkiksi ensimmäinen jakso: ...") so the block ends the sentence. The same mid-sentence split recurs in fy6-7-L3-05 Sijoitus ("... vuodessa ja [block] vuodessa. Takaisinmaksuaika on"): write each result as a complete sentence before its block.
- [Minor] solutions.md fy6-7-L3-04 Kaava (L3-1280-5) — "$S = E_\text{varaaja}(...)$" breaks after "S =" onto a second line, leaving the formula hard to read on a phone; give $S$ its own line or break before the equals sign.
- [Minor] solutions.md fy6-7-L2-05, L2-06, L2-07, L3-04, L3-05 Vastaus — parts a), b), c) run together in one paragraph; start each part on its own line as the Sijoitus blocks already do.
- [Minor] solutions.md fy6-7-L2-06 — a "Kuvaajan lukeminen" heading on a task without a graph; either write "Ei kuvaajaa; arvot luetaan taulukosta." like FY6-4 or drop the line. Task text "kello $8.00$": clock times are better in plain text (kello 8.00), not italic maths.

## Checked
- 1280 px captures open-exercises-1280-6, -7, -8 (L1-06, L1-07, L1-08), L2-1280-5 to -10 (L2-05, L2-06, L2-07), L3-1280-4 to -7 (L3-04, L3-05) read at full size; exercises.json and solutions.md of the eight new tasks read. No 390/360 px capture of the exercise cards exists (only stage-exercises-390); packet layout checks are clean.
- Tables (L2-05, L2-06, L2-07, L3-04) render with units in headers; all solution headings present; answers agree with the Vastaus values within tolerance (numbers recomputed, no mismatch).

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
