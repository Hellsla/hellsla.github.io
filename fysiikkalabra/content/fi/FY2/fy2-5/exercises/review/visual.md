VERDICT: PASS
CONTENT-HASH: fa39dc3b4232eb3a
Round: 4

## Blocking

## Polish
- [Minor] all data tables (L2-05, L2-07, L3-04, L3-05) — numeric column headers sit left of their right-aligned numbers (e.g. "$H\,(\text{MJ/kg})$" over 15..43) — right-align numeric columns' headers (site.css `.ex-data`).

## Checked
- Round 3 -> 4 change (only solutions.md, L3-05 "Vastaus:" line, now "vastauslaatikkoon kohdan b) tulos $940\,\text{kg}$."): opened open-exercises-L3-1280-8 (hash-fresh capture); the line renders as plain text with 940 kg in KaTeX, sits above a)-d), no overflow. 940 kg is the box value and b)'s result.
- Round 2 Blocking (L3-05 "Vastaus" showed 930 kg): resolved. With tolerance 0,01 the reveal chip reads "940 kg", matching the box, the answer and the solution (open-exercises-L3-1280-7).
- L3-05 part b) now ends "Käytä a)-kohdan pyöristämättömiä massoja." and sits in its own bold paragraph; the closing box instruction is last; table, Annettu, Kysytty, Periaate render cleanly.
- Earlier captures still stand: L1-08, L2-05..07, L3-04 (no changes since round 2).
- 1280 px only (no 360 px exercise capture; layout checks clean).

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
