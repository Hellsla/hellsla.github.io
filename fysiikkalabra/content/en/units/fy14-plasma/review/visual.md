VERDICT: FAIL
CONTENT-HASH: 8408172d1fd67ef6

## Blocking
1. [Major] `inquiry.json` line 351–352, task "4. Explain to a friend" (capture `stage-tarkista-390-2`, `stage-tarkista-1280-2`) — the prompt shows literal backslashes: `be \"ten times hotter than the Sun\" and says: \"So ITER …melt.\"`; the model answer starts the same way. The JSON has `\\\"` (escaped backslash plus quote). Visible markup garbage in the main written task of the Check stage. Fix: replace each `\\\"` with `\"`, or better with typographic quotes “ … ” in both `prompt` and `model`.

## Polish
2. [Minor] `unit.md`, worked example, **Reasonableness** — "Twice as many particles (ions and electrons), $500\ 000 : 250\ 000 = 2$ times more per particle" is hard to parse. Fix: "The plasma has 250 000 times fewer ions but is 500 000 times hotter, which gives 2 times the pressure; ions and electrons together double it again: about 4 times air pressure."
3. [Minor] Figure `ionisation` (`stage-selita-390-1`) — red and blue dots are not named. Add two small labels, $\text{ion}$ by one red dot and $\text{electron}$ by one blue dot in the gas panel, or name the colours in the caption.
4. [Minor] Figure `pressure` at 390 — tick labels and value labels render at 13.7 px (the house minimum is met only just) and the chart is crowded. Acceptable. The 1280 rendering is only 416 px wide; it could use the full column.
5. [Minor] Emphasis followed by a space renders with no visible gap ("A reactor *must* be hotter" looks like "mustbe", `stage-sovella-390-3`). The HTML has the space, so this comes from the shared italic font (see Shared issues).

## Checked
- Fresh build and captures for this hash: all 5 contact sheets; top/intro at 390 and 1280; stage-selita-390-1 and -3 (both figures); stage-tutki-390-2 (data table, hints, solution); stage-tarkista-390-2; fx-1/2/3 at both widths.
- Playwright at 390 and 1280 with all `details` open: no horizontal overflow, no `.katex-error`, no raw `$`, no console errors. Smallest figure label is 13.7 px at 390. The hero has no text.
- French corner: the words, the respellings and the Finnish-sound tips are consistent.
- The hash was the same at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4

## Shared issues
- Experiment tables show raw keys and true/false, and the initial-state line repeats the unit (known).
- Site CSS/font: inline `<em>` followed by a space renders with no visible gap ("mustbe", "alongit", "whymagnetic"). Check the italic face or add `em{padding-right:.05em}`.
