VERDICT: PASS
CONTENT-HASH: 50bc0cf584ffc7a4
ROUND: 3

## Blocking
(none)

## Polish
- [Minor] inquiry.json:333 (prompt) — where the three inline formulas meet, the equals sign has its space only on the right (`fλ= 2,0 Hz`, `0,50 m= 1,0 m/s`), because each piece begins with `=`; readable, but slightly uneven. A leading `{}` in the second and third formula (`$ {}= 2{,}0…$`) restores the relation spacing without touching a number, sign or unit.
- [Minor] same prompt (as on main, untouched) — the emphasised question part starts at "Koska taajuus on…", in the middle of the student's quotation, so "Missä on virhe?" is not what stands out.

## Checked
- Delta, round 3: the prompt of Esimerkki 2: Etsi virhe (inquiry.json:333), now three consecutive inline formulas instead of a display block. Round 2's blocking item (a line beginning with `.”`) is gone.
- Opened r3/fy5-10-inq-virhe-0-390.png: the chain wraps inside the sentence as `v = fλ = 2,0 Hz · 0,50 m` | `= 1,0 m/s.” Missä on virhe?`; the break falls before a relation, no quantity is split, the full stop and closing quotation mark follow the unit directly.
- Opened r3/fy5-10-inq-virhe-0-1280.png: the whole chain on one line, `… = 1,0 m/s.”` then "Missä on virhe?"; choices and the Vastaa button unchanged.
- Measured in the same run: page scrollWidth equals the viewport at both widths, no formula past its box.
- Own Playwright captures from the rebuilt preview/fy5-10.html (?ratkaisut=1, details open) in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis2-fi-7/r3/.
- Not re-judged: the formula names in lesson.md (teacher-approved, not in this branch's diff).

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 5
