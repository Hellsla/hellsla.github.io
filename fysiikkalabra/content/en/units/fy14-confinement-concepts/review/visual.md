VERDICT: PASS
CONTENT-HASH: 19e029c637aecc7b

## Blocking
(none) The earlier blocking finding is fixed: the "Find the error" news quote now uses curly quotes. Also fixed: the energy-chart bars are visible and the theta-pinch label clears the coils. The 2024 table value is now explained in the source note.

## Polish
1. [Minor] `unit.md`, "What it does *not* mean": "In 2014 NIF fired about one shot every two days, and most of its shots are not ignition attempts, while a power plant would need…" is a run-on sentence that mixes tenses. Fix: "NIF fires only a few shots a week (about one every two days in 2014), and most are not ignition attempts. A power plant would need several shots every second, each with a cheap target."
2. [Minor] Options padded to equal length read unnaturally: "Z: current along the plasma; theta: around the tube.", "There is no error; the news text is quite correct.", "…a data-centre firm from 2028 on." Fix: "In a Z-pinch the current runs along the plasma; in a theta-pinch, around it." Drop "quite" and "on".
3. [Minor] Italic followed by a space renders with no gap ("*along*a column"): the shared font issue.

## Checked
- New captures for this hash: contact sheets, top/intro at 390 and 1280, stage-selita-390-1 and -2 (pinch, ICF, energy and aspect figures), the NIF table, and the Check stage.
- Playwright at 390 and 1280: no overflow, no `.katex-error`, no raw `$`, no backslashes, no console errors. Labels are at least 13.7 px at 390.
- The hash was the same at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4

## Shared issues
- Known: raw select keys and true/false in experiment tables; the unit repeats in the initial-state line.
- Italic-space rendering in the site font.

## Re-check 2026-11-01: photographs
- Screenshots at 360, 768 and 1280 px (details opened, image loaded); check_layout.py OK at 360 and 1280 px; figure gaps 20 px above and 24 px below, no overflow, credit on its own line and legible.
- NIF chamber photo fine at all widths; the text paragraph and the side-by-side figure row that follow are not crowded.
