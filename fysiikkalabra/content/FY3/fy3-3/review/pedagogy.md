VERDICT: PASS
CONTENT-HASH: b771002b9af91a64

## Blocking
(none)

## Polish
- sim.js canvas (fy3-3-sim-390.png) — at 390 px the KaTeX labels on the canvas ("600 K", "100 K", "300 K", "V = 1,0 dm³") render at roughly 7-8 px, well below the readout text, and "100 K" crowds the thermometer bulb. Legible at 1280 px, marginal on a phone. Fix: raise the canvas label size or scale it with the canvas width so the smallest label is at least about 11 px at 390 px.
- sim readout (fy3-3-sim-390.png, fy3-3-exp-exp-1-390-1.png) — on load "Paine p ≈ 0 ... teoria 100" shows until the 1,5 s collision window fills. A student reading the first screen sees a measured 0 beside a theory 100 and may take it as a fault. Fix: show "–" or "mitataan…" until the window has data.
- readout wrap — "v = 1,00 · v300 K" breaks after the dot at 390 px and orphans the subscript. Fix: a non-breaking space or put the unit part on its own line.
- experiment table headers (fy3-3-lab-1280.png, exp-1-390-1.png) — KaTeX italics (T, p, v) sit in a monospace header font beside "p mitattu"; mixed typefaces look uneven, and the table is wider than 366 px so "p teoria" is cut off (scrolls). Fix: header in the page font; allow the header to wrap.
- lesson.md "Kaasun hiukkasten koko ... ei kasva lämmetessä; muuttuu niiden liike" (inquiry.json pred-3, Aino) — better: "vaan muuttuu niiden liike".

## Checked
- Learning path: hook, prior (pump), three predictions, two controlled experiments (one variable locked each), theory, reflect, staged example, spot-the-error, transfer, three checks, exit ticket; covers system, state variables, temperature, kelvin and absolute zero, nothing beyond FY3.
- Predictions can be refuted by the sim: v and p both emerge, p mitattu versus p teoria; wrong-option feedback repairs (Celsius ratio, "v" confusion, volume affects speed).
- Opening question is answered only after the student commits; reopened Ennusta wording stays valid.
- Worked example has five stages, one step each, figure 4 right after the first; symbolic before substituted; −270 °C sensible.
- Canvas text is LaTeX and limited to labels and values; usage and model sit behind Mallin oletukset and Laskennan selitys; speed control present.
- 1280 px lab layout: sim beside experiments, no overlap, readable; 390 px stack is clean, locked slider shown greyed with "(vakio)".
- Exercises 5/4/3, none repeats the example; L3-01 is a plain proportion (a level 2 in difficulty) but L3-02 and L3-03 reason in kelvins.
- Finnish and glossary terms correct (kelvin, absoluuttinen nollapiste, no "kelvinaste").
- Workload fits one lesson.
