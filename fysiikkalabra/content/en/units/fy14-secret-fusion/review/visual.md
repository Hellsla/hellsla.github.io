VERDICT: PASS
CONTENT-HASH: 76157f25ebed4a23

## Blocking
(none) The four polish items of the first review are resolved:
- `pinch` now draws each $\overline{B}$ ring with a faint back half and a front half with arrowheads. The arrows point downwards at the front, which is right for $I$ to the right. A copper arrowhead on the last coil turn shows the coil current.
- `pred-secret` no longer has a dangling "Their".
- The accelerator bullet in the Summary now matches the section.
- The `neutrons` key is in ink.

## Polish
1. [Minor] `inquiry.json` `zeta-data`, table header at 390: "Share of neutrons in the direction of the original current (%)" hyphenates as "cur- / rent (%)" in a narrow column. Fix: shorter headers, for example "Along the original current (%)" and "Against it (%)".
2. [Minor] Shared badge style (`zeta-data` "Made-up example data"): a four-line note in the pill-shaped badge turns into an oval with text near its edges at 390. Fix (shared CSS): a radius of about 10 px when the badge wraps, or the note as plain small text after a short badge.

## Checked
- Rebuilt; captures regenerated for this hash (contact sheets).
- Own Playwright captures of `hero`, `pinch` and `neutrons` at 390 and 1280. Smallest label 15.5 px at 390. The right-hand rule checked on the drawn arrows.
- `zeta-data` at 390 and 1280: the table fits (322 of 324 px), and the options are balanced.
- No `.katex-error`, no raw `$`, no console errors, no failed requests, no horizontal scroll. Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4

## Re-check 2026-11-01: photographs
- Screenshots at 360, 768 and 1280 px (details opened, image loaded); check_layout.py OK at 360 and 1280 px; figure gaps 20 px above and 24 px below, no overflow, credit on its own line and legible.
- ZETA under its heading and the three portraits (Richter, Spitzer, Sakharov) in the optional box all fit; Richter's wide photo is the only one at full column width at 1280 px, as intended.
