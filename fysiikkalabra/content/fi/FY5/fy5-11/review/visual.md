VERDICT: PASS
CONTENT-HASH: 3e865786391f97b7

## Blocking
(none)

## Polish
- [Minor] inquiry.json:387 (Järkevyys), both widths — the piece that begins with `+` renders as `+(180° − 2 · 55°)` with no space after the plus (a leading `+` is set as a sign), and at 1280 px `…35°) +(180°…` looks tight. `{}+ (180^\circ …)` gives the binary spacing (known join matter).

## Checked
- Delta, round 3: inquiry.json:387, the turn-angle sum in Järkevyys now four consecutive inline formulas inside the sentence. Round 2's third column is gone.
- Opened fy5-11-jark-nurkka-0-390.png: `(180° − 2 · 35°)` | `+(180° − 2 · 55°)` | `= 110° + 70° = 180°: aalto palaa…`; breaks only between whole terms, the colon follows the formula directly and the sentence runs on; Sijoitus and Vastaus boxes above intact.
- Opened fy5-11-jark-nurkka-0-1280.png: the sum on one line, `= 110° + 70° = 180°:` on the next; degree signs raised, nothing clipped.
- Own Playwright captures from the current preview/ pages (?ratkaisut=1, every details box open, hidden feedback/model boxes revealed) at 390 and 1280 px in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-fi-7/; measured in the same run: page scrollWidth equals the viewport, no formula past its box.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
