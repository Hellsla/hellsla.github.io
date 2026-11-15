VERDICT: FAIL
CONTENT-HASH: 4add4725eaf9f05d

## Blocking
- [Major] content/fi-easy/FY1/fy1-1/exercises/exercises.json, Voyager 2 task (captures 14-15) — the student's quoted solution lifts two formulas into displays, and the sentence marks after them are not set inside the last row: '$$…$$. Etäisyys on' and '$$. Voyager olisi…' leave a lone '.' at the start of the next line, and the quotation is chopped into three blocks — reads broken, and a lone full stop is an explicit failure of the reflow rule — fix: set the full stop as the last-row '\text{.}' (or put the sentence mark inside the display), or keep these two short formulas inline split at '=' ('$s = vt$ $= 15{,}341\,\text{km/s}\cdot7{,}25$ $= 111{,}2\,\text{km}$') so the quote wraps as running text; then recapture.

## Polish
- [Minor] fy1-1 solutions captures 07-08 — '(' alone at line end before the formula — keep it with the formula.

## Checked
- delta review 5d reflow, round 1: opened the 360 px captures (inquiry 01, solutions 02, 05-13); nothing clipped or scrolling, rows break at sensible points, equals signs aligned, except 14-15.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
