VERDICT: PASS
CONTENT-HASH: 5404e1fb42f97550

## Blocking
- none

## Polish
- fy6-13 solutions.md: 15.0 uJ is called three significant figures "like 120 pF and 500 V", but trailing-zero data are ambiguous; fine for a school set, optionally write the data as 1.20e2 pF.

## Checked
- 360, 320, 370 uJ/V -> 3.6e2, 3.2e2, 3.7e2: correct, no ambiguous zeros.
- 144 mJ -> 1.4e2 mJ (calculated 144 mJ shown) with the limiting data 6.0 V and 18 V: correct and the stored answer still passes.
- 63 mJ: limiting datum (24 V, two figures) now named.
- Reasonableness lines changed to match.
