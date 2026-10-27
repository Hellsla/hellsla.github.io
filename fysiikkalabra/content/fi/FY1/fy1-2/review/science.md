VERDICT: PASS
CONTENT-HASH: e59eb0f3031179fc

## Blocking

## Polish
- content/fi/FY1/fy1-2/solutions.md fy1-2-L3-01 Sijoitus — $2{,}998\cdot10^{5}\cdot3{,}156\cdot10^{7} = 9{,}4617\cdot10^{12}$ rounds to $9{,}462\cdot10^{12}\,\text{km}$, not $9{,}461$ (carried from round 3; final AU answer unaffected) — write 9,462.

## Checked
- Diff since PASS (386404c): one line in assets/sims/fy1/fy1-2/sim.js `ruler()`; the Gm number of a major tick is drawn only when the tick is over 64 px from either canvas edge (was 8 px). Ticks and the ruler line are unchanged.
- Readability: step = 10^5 km / 3474 km/px = 28,8 px per 0,1 Gm tick, so major ticks (1 Gm) are 288 px apart; the labelled band 64…536 px of the 600 px canvas is 472 px wide > 288 px, so at least one numbered tick (often two) is always visible, and every distance can still be read by counting 0,1 Gm ticks from it.
- At xc = 0 the Sun's tick (0 Gm, x = 300 px) stays labelled; the margin removes only half-clipped numbers that could be misread.
- The comment's width (100 001 Gm ≈ 110 px, half ≈ 55 px < 64 px) is consistent with keeping a label whole.
- No change to the ruler's scale, the comment "a tick every 0,1 Gm = 10^5 km", the scale bar, simState, answers.py, inquiry.json, lesson.md, exercises or solutions; earlier checks stand.
- Hash identical at start and end.
