VERDICT: PASS
CONTENT-HASH: 2a124c94003eb9c2

## Blocking

## Polish
- fy4-14 (en) still writes the air-resistance subscript as F_v while this lesson now uses F_d; the other chapter should be aligned when it is reviewed.

## Checked
- Compared lesson.md, inquiry.json, exit-ticket.json, meta.json and figures.json with the Finnish: every step, hint, feedback, model answer and number matches (script check of numbers per string and per line).
- Terms: weight, normal force, kinetic friction, air resistance, net force, work-energy principle, lift. Replaced the Finnish subscript v with d (F_d, W_d) in text and in the figure label via figures.json; no Finnish left in the figures.
- Decimal point everywhere, LaTeX valid (check_latex), figures regenerated and checked, check_i18n clean for this lesson.
- Page built and check_layout passed at 360 and 1280 px.
Delta: figures.json F_v -> F_d matches the text (skydiver F_d); three new voimakuvio blocks in the inquiry solutions recomputed (lift G = 588.6 N, N = 650 N; skydiver G = 765.2 N = F_d; student G = 539.6 N, N = 473.6 N); removed 'levels 2 and 3 deepen it' sentence matches the Finnish.
