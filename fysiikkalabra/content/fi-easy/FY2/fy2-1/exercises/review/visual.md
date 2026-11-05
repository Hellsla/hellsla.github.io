VERDICT: PASS
CONTENT-HASH: 2c9fdf155f72e6a3
Mode: delta (packet regenerated as full; judged the exercises' delta: new L1-09, split task paragraphs, solutions, plus the 390 px layout)
Round: 2

## Blocking
(none)

## Fixed
- fi-easy L2-05 Järkevyys: now `60 % + 17,5 % = 77,5 %`, `15 % + 7,5 % = 22,5 %`, `77,5 % + 22,5 % = 100 %`; page scroll width at 390 px is 390 (was 405). Confirmed in a render.

## Polish
- [Minor] fy2-1 L2-05, L3-04, L3-05 solutions at 390 px (follow-up, older unchanged content) — sideways-scrolling `eq-chain` boxes (the site's pattern) hold sums wider than the box (L3-04 449 px in 302 px, L3-05 368, L2-05 327), so the last terms are off-screen until scrolled; the page itself does not scroll sideways — split the longest sums (L3-04) at a `+` the way the Järkevyys line was split.
- [Minor] fy2-1 L2-05 Kaava box also scrolls (308 px in 302 px, `E_sauna` just cut) — same follow-up.
- [Minor] Exercise captures at 390 px are not in the packet's list; I rendered them myself.

## Checked
- Own Playwright render at 390 px of preview/fi-easy/fy2-1.html (all details open, choices answered): page scroll width 390; overflow metrics for every KaTeX display, table and svg in the exercises.
- Opened renders: L2-05 solution (end, Järkevyys) and the L1-09 card (round 1, content unchanged since).
- Text only: L3-04 and L3-05 chains judged from metrics, not opened this round; 1280 px captures and figures not re-opened (outside this delta).

## Scores
illustrations n/a · typography 4 · Finnish 4 · accessibility 4
