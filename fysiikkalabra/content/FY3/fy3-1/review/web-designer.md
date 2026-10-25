VERDICT: PASS
CONTENT-HASH: cc4638d29309873c

## Blocking
(none)

## Polish
- templates/lesson.js:38-40 (template proposal) — nav marks the wrong tab: with levels collapsed, "Tehtävät" highlights "Lähtölippu" (390x844, 1280x800); "Lähtölippu" at 1280x1000 highlights "Tehtävät" (page cannot scroll further) — set the active tab on click and pick the last section whose top is above ~35 % of the viewport.
- templates/lesson.js:33-42 (template proposal) — nav is 411 px wide, so at 360 px the last tab is cut off and the active tab is never scrolled into view — call `scrollIntoView({inline:'nearest', block:'nearest'})` on the active link.
- content/FY3/fy3-1/sim.js:87-93 — scale line "asteikko 0–2480 N …" sits tight against the top bar's value label at m=100 kg, Jupiter (390 px) — raise the line a few px or lower BARS.y.
- content/FY3/fy3-1/sim.js:84,89,93 — at 360 px the smallest canvas text is 9,7 px (Jupiter, 100 kg); 390 px is fine (min 10,7) — floor the shrunk scale line at ~10 px or shorten it.
- content/FY3/fy3-1/solutions.md:5 — at 390 px the solution box is 265 px wide and "9,81 / N/kg" breaks between number and unit — use U+00A0 between numbers and units; template proposal: smaller left indent of `.steps` and exercise `ol` under 600 px.

## Checked
- Lint 0/0; no console or page errors, no `.katex-error` at 390 or 1280.
- No horizontal scroll at 390 or 1280; display formula and table fit.
- Text column 67 characters at 1280 (608 px, 17 px); 40 at 390 (phone limit).
- Sim at 390: canvas 324x216, readout, select and slider stacked below without overlap; at 1280 native 600x400.
- Canvas text at 390 measured via fillText x transform: min 10,7 px in default, Kuu 1 kg, Mars 37 kg and Jupiter 100 kg states; example SVG about 11,9 px.
- Sim sits after Kaava and before Esimerkki; simState populated once scrolled into view.
- All links, buttons, inputs, selects, summaries and nav tabs are at least 40x40 px, including 12 answer inputs and buttons.
- Answer check: wrong gives "Ei aivan", correct (decimal comma too) gives "Oikein."; inputs have aria-labels.
- First "Ratkaisu" per level opens, 15,2 px, no raw `$`, no overflow at either width.
- Sticky nav does not cover anchor targets; contrast of grey text, button and feedback colours above 4,5:1.
