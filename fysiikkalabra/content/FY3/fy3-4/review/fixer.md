VERDICT: DONE

Round 2 fixes for fy3-4. Only `content/FY3/fy3-4/sim.js` changed. Proofreader diff: nothing new to apply.

## Blocking (web-designer)
1. Reading over the p axis ticks at 390/360 px (h 4,5–8 m). The fixed rule `up = h > 4` is gone. A general routine now places the label. It measures the reading's ink box at the current text size (`ts()`, `measureText`). Then it takes the first free candidate from this list: above-left, above-right, below-right, below-left of the point, then right of the point under the line's start level (p₀ or the h axis), as far right as the rising line needs, then down the left side of the chart. A box is free when it lies inside the chart area (x ≥ x0 + 3, above the h axis, inside the canvas) and keeps a 3-unit gap from every other text box (ticks, axis titles, p₀ label), from the red guides and the grey p₀ line (as thin boxes), from the dot and from the blue line (segment test). At h = 5–6 m on a phone the reading now sits below-right of the point (screenshots: "150 kPa", "178 kPa" clear of the axis).
2. Guide and line through the reading for h ≳ 16 m. This is covered by the same routine, because the guides and the line are obstacles. The old clamp that pushed the label down onto the horizontal guide is gone. At h = 18 and 20 the reading sits above-left of the point, above the guide.
3. "h (m)" cut by the vertical guide. The title now sits below the tick-label row at the right end. The guide stops at the axis, so the two can never cross. To make room, the chart's h axis moved up 10 units (CH.y0 345 → 335).
- Every canvas text now has a halo: a stroke in the background colour, 3 px on screen (3·k canvas units), drawn under the fill.
- The grey p₀ label is placed in the same way. Its spots are below the dashed line (right end, left end, three spots in between), then above it, and it falls back to the short form "p₀" when the guides block every long spot (3 of 123 states at 360 px). The p₀ label takes the first spot that still leaves the reading a near place, so the reading wins.

## Polish
- web-designer 1: the bracket's "h" is drawn only when h ≥ 2 m. Applied.
- web-designer 2 (column width): template property, not fixable here.
- tester 1: covered by item 1.
- tester 2 (optional label and kulmakerroin text assertions): not added. They are optional, and the instruction was to leave tests/sims unchanged unless a renamed string forced it.

## Verification
- `window.simDebug` (kept) exposes `boxes` (ink box of every canvas text), `obstacles`, `line`, `used` (candidate index) and `readingPlaced`.
- Sweep in headless Chromium at 360, 390 and 1280 px: ρ ∈ {700, 1000, 1300}, both checkbox states, h = 0…20 m in 0,5 m steps, 246 states per width, 738 in all. I asserted that no two text boxes intersect, every box lies inside the 600×400 canvas, no box touches a guide, the p₀ line, the dot or the blue line, the reading never takes the fallback, and the p₀ label exists whenever it should. Result: 0 problems at every width, with a minimum gap of 3 units around the reading, the p₀ label and "h (m)". The reading used the far left-column spot once (360 px, ρ 1000, ylipaine, h = 20: it sits at the left end of the horizontal guide).
- Screenshots viewed: h = 5, 6, 18, 20 at 360 and 390 px (ρ 1000 and 1300), plus h = 0, 1, 2, 3, 3,5, 4,5, 11, 16, 19 and 20 in both modes and 1280 px cases. No collisions.
- `lint_lesson.py fy3-4`: 0 errors, 0 warnings. `check_latex.py`: ok. `build.py --all`: built. `test_sims.py fy3-4`: PASS, no console errors.

## Files changed
content/FY3/fy3-4/sim.js only (tests/sims/fy3-4.json unchanged).

Stale reviewers: tester, web-designer, physics-expert and proofreader. sim.js is in the physics-expert and proofreader domains too (`DOMAINS` in gate.py). mathematician, educator and editor stay valid.
