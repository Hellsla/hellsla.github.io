VERDICT: PASS
CONTENT-HASH: 8e38a43298c1653c

## Blocking
(none)

## Polish
- [Minor] Graph fy8-s3-inv (R against 1/r^2): axis tick labels and the dashed R ~ 1/r^2 label are small at 390 px (about 11 px); enlarge the figure's text slightly.
- [Minor] Graph fy8-s3-inv has no marker legend saying the dashed line is the model and the dots the measurements; the "R ~ 1/r^2" label carries it, a short caption would make it explicit.
- [Minor] fy8-s3-lin, point labels "(20.0; 12.0)" and "(-1.3; 0)" use a semicolon and a decimal point (English): fine, but check they stay in one convention in fi.

## Checked
- The packet's screenshots were stale or missing and screenshot.py cannot capture the English Sovella page, so I built preview/en/FY8-sovella.html (build.py FY8-sovella) and took my own 390 px captures with every box open.
- Opened: the top of the page (title, intro, task 1), the three inline figures (energy levels of oxygen, R against 1/r^2, linearised R^-1/2 against r), all 12 Formula blocks (two contact sheets) and the Substitution rows of task 1 in the open solution.
- Measured at 360 and 390 px: no page horizontal overflow; KaTeX outside the graphs' own labels not clipped; no red KaTeX source.
- Formula blocks (work queue 8g, aligned rows): equals aligned, fractions in display size, subscripts legible, prose lead-ins read correctly. Graphs: units on both axes, data as dots, model as a line, circled points and the extrapolation read-off marked.
- Hash (practice.py hash FY8 --lang en) re-run at the end: unchanged. The packet header's c355f45d310c2f53 is the review-packet hash, not this one.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
