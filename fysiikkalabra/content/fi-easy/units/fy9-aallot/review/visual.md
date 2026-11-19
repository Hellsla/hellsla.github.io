VERDICT: PASS
CONTENT-HASH: 487d83df3bf17103

## Blocking
(none)

## Polish
(none)

## Checked
- Read `git diff origin/main...HEAD` for fi-easy (excluding review/): only sovella/solutions.md and inquiry.json, 36 insertions / 12 deletions. Changes are paragraph breaks (blank line inserted between sentences of Periaate and Mallivastaus fields); words, maths, units and figures unchanged. A display-math block that opens mid-paragraph stays in the later paragraph, so no formula is split by the new break.
- Read the previous Sovella visual report (PASS) as evidence.
- Opened fi-easy 390 px (sovella-390-2) from review/shots/: Sovella task cards render cleanly, KaTeX and units intact, no clipping or overflow, one reading column.
- Not opened: captures of the solution panels with the solution button open, so the rendered paragraph spacing inside solutions rests on the diff and the earlier Sovella report, not on my own view.
