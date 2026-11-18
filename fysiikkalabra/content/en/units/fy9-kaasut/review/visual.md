VERDICT: PASS
CONTENT-HASH: b61fa0a2e8442d35
SCOPE: delta: new Sovella tasks s7 and s8 (figures from the catalog, aligned calculation rows, LaTeX units, English decimal points) judged at 390 px, check_layout at 360 px; other tasks not re-judged

## Blocking
- none

## Polish
- [Minor] solutions.md s8 — new text writes the gas constant as `8.31\,\text{J/(mol K)}` while the same file also uses `\tfrac{\text{J}}{\text{mol}\cdot\text{K}}` and the project writes unit products with `\cdot` — use `\text{J/(mol}\cdot\text{K)}` throughout.
- [Minor] s8 b) Formula block — the symbolic chain `n_B/n_A = ... = p_B/p_A` and the next row `(n_A−n_B)/n_A = 1 − n_B/n_A` are set in one box with different left edges; give the second its own line starting with the quantity.

## Checked
- Unit page captures made (screenshot.py fy9-kaasut --lang en); packet read; page opened at 390 px with every box open, tasks s7 and s8 captured as element screenshots (statement, figure, parts, model answer, substitution, answer, reasonableness).
- check_layout.py fy9-kaasut --width 360: OK for en (known clipped formulas are old rows, none in s7/s8).
- s7 (nuclear power plant source task, text-only, link to TVO page, assumptions list) and s8 (two vessels, p–T graph with two lines A and B, parts a–c): graph axes and units, distinct colours with line labels, readable rows, formula/substitution/answer order.

## Scores
illustrations 5 · typography 4 · Finnish (English prose) 4 · accessibility 5
