VERDICT: PASS
CONTENT-HASH: 1ed699cbb90173d7

## Blocking

## Polish
- exercises.json L3-03 — "välillä 0–$10\,\text{s}$", "10–$20\,\text{s}$", "20–$40\,\text{s}$" leave the range's first number outside the LaTeX and without a unit, so the text breaks into plain and math mid-range — write each range as one expression, e.g. "välillä $0\text{–}10\,\text{s}$" (or "ajanhetkestä $0\,\text{s}$ hetkeen $10\,\text{s}$"); likewise "arvosta 0 arvoon $30\,\text{m}$" could read "arvosta $0\,\text{m}$ arvoon $30\,\text{m}$".
- solutions.md L1-04 Järkevyys — "jokaista 0,7 sekuntia kohden" is the one number with a unit still in plain text — "$0{,}7\,\text{s}$".
- exercises.json L3-02 — "paikasta 0" is a position without unit — "paikasta $0\,\text{m}$" (the same task already uses $90\,\text{m}$).

## Checked
- Delta judged: every changed line only wraps a number and unit in LaTeX; no value, unit or wording of the question changed, so levels, counts and the worked-example distinction hold from the earlier PASS.
- Case endings after LaTeX units read correctly in Finnish ($120\,\text{m}$:n, $15\,\text{s}$:ssa, $3{,}5\,\text{m/s}$:n, $1{,}2\,\text{km}$:n, $40\,\text{s}$:n).
- Decimal commas inside LaTeX use {,}; negatives use a proper minus ($-5{,}0\,\text{m}$), better than the former plain "−5,0 m".
- Situation first and question last still holds in all twelve tasks; solutions keep their seven steps.
- Solutions' changed Järkevyys lines read the same as before, units now consistent with the rest of each solution.
- Phone capture of the exercises stage (390 px): readable, nothing clipped; the level cards are closed and unchanged by this diff.
