VERDICT: FAIL
CONTENT-HASH: 3de6b1d57fce91b7

## Blocking
- [Major] solutions.md, 7-19 Kaava (`\quad (\text{pienin kokonaisluku k})`) — the symbol $k$ is set in upright plain text inside `\text{}`, so it reads as a letter of the sentence, not the italic quantity used in the rows above — symbol in plain text in new text — write `\quad (\text{pienin kokonaisluku }k)` (k outside `\text`).

## Polish
- [Minor] solutions.md, 7-17 Kaava row 2 (`x = \dfrac{A}{2} &\Rightarrow ...`) — the `&` before `\Rightarrow` puts "x = A/2" left of the equals column, so the rows' equals signs are not aligned (row 1 and rows 3–4 sit further right) — put the condition in its own row, e.g. `x &= A\sin(...)` / `\text{kun } x = \tfrac{A}{2}:\ \sin(...) = \tfrac12` or start the row with `&\Rightarrow`.
- [Minor] Kaava blocks with fractions (7-20, 7-21 task with D and A) — rows with `\dfrac` sit tight against each other at 1280 px; readable, no fix needed beyond optional `\\[0.3em]`.

## Checked
- Delta, solutions.md Kaava rows only. Opened (lesson review/shots): open-exercises-1280-1 (L1 reference layout), L3-1280-1 (7-17), -2 (7-18), -4 (7-19), -5 (7-20), -7 (data-fit task).
- Aligned Kaava blocks render in KaTeX, inside the solution panel at 1280 px, no clipping; symbolic order (basic law → rearrangement) reads well; Sijoitus unchanged and consistent. 390 px not separately opened; check_layout 360/390 ok per packet.
- Other changed tasks (7-2, 7-3, 7-4…) have the same short aligned form; not each opened.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
