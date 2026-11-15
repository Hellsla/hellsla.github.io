VERDICT: PASS
CONTENT-HASH: 613e549c949f649f

## Blocking
- none

## Polish
- [Minor] stage rows with a lone unit continuation row (e.g. "· 2,998 · 10^8 m/s" in fy8-4) could join the "=" column; existing layout, not a regression.

## Checked
- batch delta review, round 2: no capture of this lesson was opened. Judged by inference from the shared mathlayout.with_punct build, which I saw working in fy8-4, fy8-8, fy8-13 (and fy8-1 theory); this lesson's own lifted formulas were not individually seen. The lesson's own diff (formula names, reflow) was not inspected in a capture.
