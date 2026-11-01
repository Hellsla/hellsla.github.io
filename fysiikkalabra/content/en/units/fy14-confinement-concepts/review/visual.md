VERDICT: FAIL
CONTENT-HASH: f99d2c16745c6793

## Blocking
1. [Major] `inquiry.json` line 251, optional task "Find the error" (`stage-sovella-390-*`, contact #17/#45) — the prompt shows literal backslashes: `A news text says: \"The target gain of 1.5 … can be built.\"`. The JSON has `\\\"`. Visible markup garbage in a student task. Fix: use `\"` or typographic quotes “ … ”.

## Polish
2. [Minor] Investigation 1 table (`stage-tutki-390-1`) — laser energies mix precisions: "2.2" (12 Feb 2024) next to "2.05" and "2.08". Use the published value with the same number of decimals, or footnote it. (for science: confirm the LLNL value.)
3. [Minor] Figure `energy` — on the 0–300 MJ linear axis the laser (2.05) and fusion (3.15) bars are hairlines, so their colours cannot be seen. The contrast is the point, so keep the axis. Draw both bars at least 3 units wide, or add a magnified inset ×20.
4. [Minor] Figure `pinch`, theta-pinch — the label "$I$ around the tube" touches the top of the first coils. Move it up about 8 units.
5. [Minor] Emphasis followed by a space renders with no visible gap ("*along*a column", "*not*mean"): the shared italic font issue.

## Checked
- Fresh build and captures for this hash: all contact sheets; top/intro at 390 and 1280; stage-selita-390-1, -2, -3 (pinch, ICF, energy and aspect figures); the 1280 theory sheet (aspect figure); the NIF table with hints and solution; the sorting task; the Check stage; the French corner.
- Playwright at 390 and 1280 with all `details` open: no overflow, no `.katex-error`, no raw `$`, no console errors. Figure labels are at least 13.7 px at 390. The hero has no text.
- Z-pinch field symbols (⊙ above, ⊗ below for current to the right) and the inward red forces are consistent.
- The hash was the same at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4

## Shared issues
- Known: raw select keys and true/false in experiment tables; the unit repeats in the initial-state line.
- Italic-space rendering (site font/CSS).
