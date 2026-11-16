VERDICT: PASS
CONTENT-HASH: bb3bf9b86f19bb9a

## Blocking
(none)

## Polish
- [Minor] inquiry.json:389 (Sijoitus of the kansi task), both widths — the trailing `·` sits tight against the unit (`4,0 cm·`), because an operator at the end of a piece gets no space before it; `\text{cm} \cdot{}` restores the binary spacing. Readable as it is: the dot at the row's end signals that the product goes on.
- [Minor] same line — as inline formulas the chain has no white formula box and no aligned equals signs, unlike every other Sijoitus; an `aligned` block with `&\quad \cdot \sin(…)` would be the house form. May wait.
- [Minor] same line, 1280 px — `)= 4,0 cm` tight before the relation (known join matter; `{}=`).

## Checked
- Delta, round 3b: inquiry.json:389, the `·` now ends the first piece instead of opening the second. Same tokens in the same order.
- Opened r3b/fy5-7-sij-kansi-0-390.png: rows `x = 4,0 cm·` | `sin(2π · 0,50 Hz · 0,40 s)` | `= 4,0 cm · sin 1,257` | `= 4,0 cm · 0,9511 = 3,804 cm`; no row begins with a multiplication dot, every break between whole quantities, no mantissa or unit split; Kaava box above and Vastaus box below intact.
- Opened r3b/fy5-7-sij-kansi-0-1280.png: two rows, `x = 4,0 cm· sin(…) = 4,0 cm · sin 1,257` and the rest after a break before a relation; units upright, decimal commas, nothing clipped.
- Own Playwright captures from the rebuilt preview/fy5-7.html (?ratkaisut=1, every details box open) at 390 and 1280 px in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-fi-7/r3b/; measured in the same run: page scrollWidth equals the viewport, no formula past its box.
- Not re-judged: lesson.md changes that are not in this branch's diff.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
