VERDICT: PASS
CONTENT-HASH: 6a4faf6c5bd230df

## Blocking
(none)

## Polish
- content/FY3/fy3-1/sim.js:84-85 — at 360 px, Jupiter 100 kg the top bar's value label "2480 N" is shrunk to 9,98 px (99 kg: 10,36 px; 390 px is fine, min 10,8) — floor the shrunk size at 10 px x scale, or give the bar chart a little more width (BARS.x smaller).
- content/FY3/fy3-1/solutions.md:2,5,21,45,53,61,69,74,77,85 (every "number unit") — at 390 and 360 px a line still breaks between number and unit ("9,81 / N/kg", "3,71 / N/kg", "4,995 / kg", "18 / N"); the content has no U+00A0 — use a non-breaking space between number and unit (lint rule candidate).
- templates (proposal, optional) — the sim readout line "Palkkikaavion asteikko …" is 2 lines at 390 px; fine, no change needed unless the readout grows further.

## Checked
- Lint 0/0, build ok; no console/page errors, no `.katex-error` at 1280, 390, 360 px; no horizontal scroll (scrollWidth = viewport) at all three.
- Text column 67 chars at 1280 (608 px, 17 px); 40 at 390, 36 at 360 (phone limit).
- Canvas text, measured by the fillText transform at 390 px: min 10,8 px in Maa 10, Kuu 1, Mars 37, Jupiter 100, 99 and 1 kg; at 1280 min 11 px. At 360 px min 10,8 px except the Jupiter 100/99 value label above.
- Round-1 scale line: "asteikko 0–2480 N" is 10,8 px at 390 and 360, no longer touches the top value label (screenshots review/fy3-1-r2-sim-{360,390}-Jupiter-100.png); title 12,6 px at 390, 11,4 px at 360, inside canvas.
- DOM readout states the scale explanation at 390/360 (2 lines); readout, select and slider stacked below canvas without overlap at 390/360; at 1280 controls below the 600x400 canvas.
- Nav: active tab is correct for scroll position at every section top and after tapping each tab, at all three widths; at 390 and 360 (nav 411 px) the active tab ends fully inside the viewport (scrollIntoView works).
- All links, buttons, inputs, selects, summaries and nav tabs at least 40x40 px at all three widths (0 smaller).
- Solutions: indent 0 under 600 px (box 314 px at 390, 284 px at 360, 14,7 px text, no overflow, no raw `$`); 1280 box 515 px, 15,2 px.
- Sim sits after Kaava and before Esimerkki; simState populated once scrolled into view.
- Contrast and answer-check behaviour unchanged from round 1 (templates only changed in nav JS and solution indent).
