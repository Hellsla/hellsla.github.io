VERDICT: PASS
CONTENT-HASH: bed302f98fcec0a3

## Blocking
(none)

## Polish
- [Minor] inquiry.json:510 (model answer) — the two blocks are centred in the answer box while solution blocks elsewhere are left-aligned; it reads well, no change needed in content.
- [Minor] same — on a wide screen `N = … ≈ 59 N` keeps its two rows although one would fit (the known join_wide behaviour).

## Checked
- Delta, round 2: the model answer of the selitystehtävä (inquiry.json:510). Opened fy5-8-inq-laatikko-390.png and fy5-8-inq-laatikko-1280.png (the locked model box shown by the page's own reveal state): `N = 6,0 kg · 9,81 m/s² ≈ 59 N.` and `x = F_μ/k = 18 N : 120 N/m = 0,15 m.` as aligned rows, fractions upright and uncramped, full stops inside the formulas, the prose between them intact.
- Own Playwright captures from preview/ (?ratkaisut=1, every details box open) at 390 and 1280 px in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis2-fi-7/; measured there: page scrollWidth equals the viewport, no formula past its box.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5
