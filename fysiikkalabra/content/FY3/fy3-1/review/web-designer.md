VERDICT: PASS
CONTENT-HASH: f0893923f063d748

## Blocking
(none)

## Polish
- scripts/build.py:45 (UNIT) — "kN" is missing from the unit list, so lesson.md:43 "eli noin 1,18 kN." keeps a plain space and can break before "kN" (does not break at 1280, 390 or 360 px today, only by luck of wrapping) — add `kN` (and `cm²`, `m³` if used later) to UNIT.
- scripts/build.py:101 — the `Vastaus` reveal `<p>{ans}</p>` ("39 N", "6,0 cm", 13 of them) is not passed through nbsp_units, so it has a plain space; it is a short line on its own, so no visible break — wrap `ans` in nbsp_units for consistency.
- content/FY3/fy3-1/sim.js:46-50 — readout strings use plain spaces ("m = 10 kg", "9,81 m/s²", "0–248 N"); no break in 36 body/mass states at 1280, 390, 360 px, so only a latent risk — use   if the sim is next edited.

## Checked
- Lint 0/0, build ok, hash unchanged start to end; no console or page errors, no .katex-error, scrollWidth = viewport at 1280, 390, 360 px.
- Number-unit breaks: 117 number+unit pairs in the opened page (all 3 solutions, 15 answer reveals, 12 task texts, exit ticket, theory): 92 use U+00A0, 0 lines break between number and unit at 1280, 390 or 360 px (measured per character with Range rects, all details open).
- Opened solutions and task texts specifically: every pair non-breaking and on one line at all three widths; no horizontal overflow (.katex-display, svg, canvas, tables, pre all inside viewport).
- Sim readout and controls: 36 states (4 bodies x 9 masses) at each width, no number/unit break, readout 4 lines at 1280 and 5 at 390/360, no overlap with canvas or controls; canvas 600x400, 324x216, 294x196 (sim.js unchanged, canvas text sizes from round 3 still hold: min 10,8 px at 390, 10,78 px at 360).
- Voimamittari SVG fits its column (608, 358, 328 px wide; 16 px gutters).
- Text column: 608 px at 17 px font, about 67-74 characters at 1280; 44 at 390, 40 at 360 (phone).
- Tap targets: 0 links, buttons, inputs, selects or summaries under 40 px at any width.
- Contrast: body text rgb(20,23,30) on rgb(247,243,236), well above 4,5:1.
- Screenshots review/fy3-1-r4-{1280,390,360}.png and review/fy3-1-r4-sim-{1280,390,360}.png.
