VERDICT: PASS
CONTENT-HASH: f27fa4065e002a43

## Blocking
(none)

## Polish
- [Minor] inquiry.json:389 (Sijoitus of the kansi task) — as consecutive inline formulas the chain has lost the white formula box and the aligned equals signs that every other Sijoitus has; at 390 px a row begins flush left with `· sin(2π · 0,50 Hz · 0,40 s)`. Readable and unambiguous, so it may wait; the house form would be an `aligned` block with `&\quad \cdot \sin(…)` as the continuation row.
- [Minor] same line, 1280 px — uneven spacing at the joins (`4,0 cm· sin(`, `)= 4,0 cm`): a piece that begins with an operator gets no space before it. Starting the piece with `{}\cdot` / `{}=` evens it (known).

## Checked
- Delta, round 3: inquiry.json:389, Sijoitus now four consecutive inline formulas. Round 2's trailing `&` is gone.
- Opened fy5-7-sij-kansi-0-390.png: rows `x = 4,0 cm` | `· sin(2π · 0,50 Hz · 0,40 s)` | `= 4,0 cm · sin 1,257` | `= 4,0 cm · 0,9511 = 3,804 cm`; every break between whole quantities, no mantissa or unit split; Kaava box above and Vastaus box below intact.
- Opened fy5-7-sij-kansi-0-1280.png: two rows, the break before a relation; units upright, decimal commas, nothing clipped.
- Not re-judged: lesson.md changes that are not in this branch's diff.
- Own Playwright captures from the current preview/ pages (?ratkaisut=1, every details box open, hidden feedback/model boxes revealed) at 390 and 1280 px in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-fi-7/; measured in the same run: page scrollWidth equals the viewport, no formula past its box.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
