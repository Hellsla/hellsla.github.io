VERDICT: PASS
CONTENT-HASH: 919ae046ec360cf5
ROUND: 3 (delta, work queue 5d: calculations re-broken; en)

## Blocking

## Polish
- [Minor] inquiry.json transfer solution, Substitution — `f = 2000 Hz·` | fraction | `= 2076.8 Hz` are three inline pieces while `v_L` just above is a boxed aligned block; at 390 px the fraction sits alone on its line, flush left, and at 1280 px the gap after `·` is narrower than before `=` — one aligned block (`f &= 2000 Hz \cdot \\ &\quad \dfrac{…}{…} \\ &= …`) would match its neighbour.

## Checked
- fy5-14-390-0.png, fy5-14-1280-0.png, ctx-14-siirto-390.png, ctx-14-siirto-1280.png: Substitution of the transfer task; the `·` ends the first piece, no line starts with a bare dot, nothing clipped; 1280 px reads as one row.
- top-14-390.png: opening and hero unchanged in layout (teacher-figure change carried earlier, outside this diff).
- Own Playwright captures of preview/en (`?ratkaisut=1`, every details box opened) at 390 and 1280 px in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-en-13/; page scan at both widths: no horizontal overflow, no formula past the viewport, no KaTeX error.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 5
