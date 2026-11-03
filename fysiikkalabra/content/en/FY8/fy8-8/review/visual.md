VERDICT: FAIL
CONTENT-HASH: 0e1654f7d66a7eee

## Blocking
- [Major] Figure `fy8-8/spectrum` (fig-5 in the Tutki stage, repeated in the theory summary capture #28/#26) — the y-axis label is still Finnish ("fotonien määrä"), and its description/alt text is Finnish too ("Kaavamainen gammaspektri koboltti-60-lähteestä…", decimal commas 1173,2); `figures.json` has no entry for it — an English student gets Finnish in an essential graph, and the alt text is unusable for an English screen-reader user — translate the label to `\text{number of photons}` (in `lessons/FY8/fy8-8/figures.py` for en or via the language mechanism the other figures use) and add the English description to `figures.json` (peaks 1173.2 and 1332.5 keV, decimal points).

## Polish
- [Minor] decays figure (fig-11) — the label "excited state *" is set larger than the other labels and sits on the dashed divider line — reduce to the label size and keep clear of the line.
- [Minor] levels figure (fig-13) — the transition labels 1173.2 and 1332.5 have no unit — add `\,\text{keV}` like the level labels.
- [Minor] lesson.md, "Energy levels…" — "Transitions of an atom are electronvolts" — write "are of the order of electronvolts".
- [Minor] chart figure (fig-9) — the "N = Z" label touches the band's lower end — move it left/up.
- [Minor] exit ticket answer 1 (capture open-exit-1280) — "conserved (" ends a line and the maths starts the next, leaving a dangling bracket — keep the bracket with the formula (non-breaking) or write the check as a separate sentence.

## Checked
- contact-1 to contact-4; fig-5, fig-7, fig-9, fig-11, fig-13, fig-15 at 390 px; example-390-1 (steps 1–4); theory-1280-2; intro-1280; open-exit-1280; sim in contact sheets (#2, #24, #39, #42). Exercise captures are covered in the exercise-set report.

## Scores
illustrations 3 · typography 4 · Finnish (English prose) 4 · accessibility 3
