VERDICT: PASS
CONTENT-HASH: 6ad8718f45bb8361

## Blocking
(none) All three round-2 items are fixed: the reading no longer touches the p axis ticks, guides or line (h 4,5–8 and 16–20 m), and "h (m)" is never cut by a guide.

## Polish
1. Template (not fixable in the lesson): the text column is 29–33 characters at 360/390 px (58 at 1280). Unchanged since round 1; a template property, not blocking.
2. sim.js: the minimum gap between the reading, p₀ label or "h (m)" and any other box was 2,05–3 canvas units (at 1280 and 390 px, below the 3-unit PAD because of font-size rounding). The halo keeps every case legible; no action needed.

## Checked
- Sweep at 360, 390 and 1280 px: ρ 700/1000/1300 × both checkbox states × h 0–20 m in 0,5 m steps = 246 states per width, 738 in all. From `simDebug.boxes` and `obstacles` I found 0 text boxes overlapping each other, leaving the 600×400 canvas, touching a red guide, the dot or the p₀ line, or sitting on the blue line (sampled along the segment). The reading never took the fallback, and the p₀ label exists whenever the checkbox is off. No console or page errors.
- Screenshots viewed (sticky nav hidden, 2x): h = 5 and 6 at 360/390 (ρ 1000/1300/700, both modes): the reading sits below-right of the dot, clear of ticks "150"/"200". h = 18 and 20 at 360/390/1280: the reading sits above-left of the dot, above the horizontal guide. "h (m)" is under the tick row and the vertical guide ends at the axis. Spot checks at 1280 px (h 5, 6, 18, 20): fine.
- Reading candidate use: first (above-left) 153–194 of 246 states, the far-left column fallback used once (360 px).
- Canvas text 11–12 px on screen at 360/390/1280 (ts() scales by k = 2,04/1,85/1).
- No horizontal page scroll (scrollWidth = viewport) at 360, 390, 1280.
- Controls sit below the canvas at every width (no overlap); sliders 40 px, checkbox row 40 px (24 px box inside), label rows 64–88 px.
- `check_layout.py fy3-4`: OK at 360 px. `lint_lesson.py fy3-4`: 0 errors, 0 warnings.
- Hash checked before and after: 6ad8718f45bb8361 (no edit during the review).
