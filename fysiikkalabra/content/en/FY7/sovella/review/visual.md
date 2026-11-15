VERDICT: PASS
CONTENT-HASH: 73d5f564adacfc16

## Blocking
- none

## Polish
- [Major, outside this change: work queue item 5d, own PR] docs/clipped-formulas.tsv lists five clipped open-solution formulas for FY7-sovella (the s5 gradient `6.00 \cdot 10^{-4}\,\tfrac{1}{\text{nm}}`, the s3 short-circuit force `0.012 \cdot (8000 : 300)^2`, the aluminium mass chain, `6.0\,\text{MW} - 0.85\,\text{MW}`, and the boron-11 momentum substitution). Not judged here; fix in 5d.
- [Minor] tasks.json `intro` — "Five tasks bring the module together: …" then lists seven topics in one long sentence (incl. "force between current-carrying conductors", "interference in a thin film"), so it reads as seven tasks — split it into a task-by-task list or "five tasks: … ; …".
- [Minor] fy7-s4-spectrum graph (fi capture fig-20) — the "visible" label sits tight against the violet band's edge; move it 8–10 px right.
- [Minor] fy7-s1-implanter (fig-1) — the accelerating electrodes and the "U" label are small at 390 px; acceptable as a schematic, but enlarge if the figure is touched again.

## Checked
- No English captures exist (`screenshot.py` captures FY7-sovella only in fi), so I judged from the Finnish captures of the same structure (fi hash 35d50fed…) and the English source and figures.json translations. Layout findings carry over; English wording was judged from the source only.
- Opened: top-390, top-1280, contact-1, stage-fy7-s1-390-1 and -5, figs 1, 3, 11, 20, 22, 25 (set-up, force diagram, voltage graph, spectrum, fibre, grating graph).
- English source: every quantity with its unit is LaTeX (no plain quantity found in solutions.md); no ×, ÷ or decimal comma; the labels in figures.json are LaTeX words.

## Scores
illustrations 4 · typography 4 · Finnish 4 (English 4) · accessibility 4
