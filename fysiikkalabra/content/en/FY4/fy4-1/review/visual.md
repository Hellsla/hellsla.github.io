VERDICT: FAIL
CONTENT-HASH: 984ee5cc554c2171

## Blocking
- [Major] simulation, `sim-1280` and `lab-1280-1` (English only) — the Case drop-down is too narrow for its English label: it shows "1: same starting poir", and the longer options ("2: different starting points", "3: opposite directions", "4: back-and-forth motion") would be cut harder still — the student cannot read which case is selected without opening the list; the Finnish page fits because its words are shorter — give the select `width:auto`/a min-width that fits the longest option (or let the Case row wrap to its own line as at 390 px), or shorten the English option names ("1: same start").

## Polish
- [Minor] inquiry.json, Measurement data paragraph (`stage-tutki-390-2`/`-3`) — the coordinate pairs "(0 s; 4.1 m)" are plain text with units, twice (inherited from the reviewed Finnish text) — write `$(0\,\text{s};\, 4.1\,\text{m})$`.
- [Minor] inquiry.json, prediction 2 feedback ("In the values of the model each cart is displaced the same distance…") — awkward English — "In the model's table each cart is displaced by the same amount, $20\,\text{m}$, in $10\,\text{s}$."
- [Minor] Tutki experiment cards at 390 (`exp-exp-*-390-2`) — the status line "Initial state set. Kept constant: case. Adjust moment t…" and the Exercises intro paragraph (`stage-exercises-390`) are set in a much larger type than the rest of the card; shared template, same on the Finnish page.

## Checked
- All six contact sheets (every capture #1–#69 in thumbnail), then at full size: fig-1, fig-4, fig-5, fig-6, fig-7 (390), sim-390, sim-1280, lab-1280-1, theory-1280-1, open-exercises-L2-1280-1.
- Figures 2 and 3 and the worked example, Predict, Apply, Check, exit ticket and exercises read from the contact sheets.
- No Finnish word appears on any English capture (the Finnish strings in figures.json are only translation keys); no horizontal overflow; maths renders with no red source; units are LaTeX; hero and graphs consistent (velocity blue, fitted line orange, dashed extrapolation with open marker).

## Scores
illustrations 5 · typography 5 · Finnish 4 (English 4) · accessibility 3
