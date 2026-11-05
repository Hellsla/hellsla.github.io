VERDICT: FAIL
CONTENT-HASH: 2f4ef416cfc18f88
Round: 2 (delta, commit 442c889ba)

## Blocking
- [Major] L2-06 solution, Model answer — the chain $E = Hm = 26\,\tfrac{\text{MJ}}{\text{kg}} \cdot 3000\,\text{kg} = 78\,000\,\text{MJ}$ is one unbroken inline formula 353 px wide in a 304 px column at 390 px; the render shows "= 78 00(" cut off, so the answer value is unreadable on a phone — essential information clipped — split it like the L3-04 sum, e.g. $E = Hm$, "that is" $E = 26\,\tfrac{\text{MJ}}{\text{kg}} \cdot 3000\,\text{kg} = 78\,000\,\text{MJ}$ on its own line, or break after the second "=". Untouched this round, shared with fi, not seen before because exercise captures exist only at 1280 px.
- [Major] L3-04 solution, Substitution — the L3-04 sum is now split into three groups and the round-1 clip is gone, but the first group $2100 + 1900 + 1600 + 1100 = 6700$ is still 4 px wider than the column at 390 px (the last digit shows as "670("); at 360 px the third group is also over — split each group into its own row or drop the group sums into a "so" step (e.g. "$2100 + 1900 = 4000$, $1600 + 1100 = 2700$") so every formula fits about 300 px.

## Polish
- [Minor] data tables — captions and right-hand columns scroll sideways at 390 px by design.

## Checked
- Rebuilt preview/en/fy2-5.html from the working tree and rendered it at 390 px (and 360 px for measurement) with Playwright, every level and solution open.
- Rendered and opened as images: L3-04 Substitution (groups of four, then the 13 300 step and the aligned E_useful, E_in, m rows: only the first group clips) and L2-06 solution (clip above). L2-08 card opened in round 1, unchanged.
- Measured every .katex in every solution step against its step box at 390 and 360 px: offenders are exactly the L2-06 chain, the first L3-04 group (both widths), and at 360 px also the L2-08 petrol line, the third L3-04 group and, in fi-easy, the 360 000 MJ : 3600 s chain. Page scrollWidth is 390; no page-level overflow. Those 360 px items were measured only, not opened.
- Text only: the solutions.md wording of the split ("Add the months in groups of four", "so the sum is"), units and decimal separators. No fresh packet captures were opened; the packet's 1280 px captures were not used.

## Scores
illustrations 4 · typography 3 · language 4 · accessibility 4
