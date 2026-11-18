VERDICT: PASS
CONTENT-HASH: e2d1a4f13b4f84c1
SCOPE: delta: new Sovella tasks s7 and s8 (figures from the catalog, aligned calculation rows, LaTeX units, English decimal points) judged at 390 px, check_layout at 360 px; other tasks not re-judged

## Blocking
- none

## Polish
- [Minor] s7/s8 figures (fy3-6/heating-line, fy3-7/melting-curve) — tick numbers are about 10 px at 390 px, readable but small — catalog figures, leave to a figure-fixes pass; s8 graph has no marker for the point read at 120 kJ, which is fine since it is only in the text.

## Checked
- Unit page captures made (screenshot.py fy9-lampo --lang en); packet read; page opened at 390 px with every box open, tasks s7 and s8 captured as element screenshots (statement, figure, parts, model answer, substitution, answer, reasonableness).
- check_layout.py fy9-lampo --width 360: OK for en (known clipped formulas are old rows, none in s7/s8).
- s7 (heating line graph, a–d) and s8 (melting curve, a–d): statement, graph axes with units (T in °C, t in s / Q in kJ), data markers distinct from the line, decimal points, LaTeX units, aligned rows (c = ... rows with = in one column), answer boxes, reasonableness blocks. Opening and intro unchanged in the diff apart from tasks; the surrounding older tasks (Radio mast, Power cut) glanced at for layout only.

## Scores
illustrations 5 · typography 5 · Finnish (English prose) 4 · accessibility 5
