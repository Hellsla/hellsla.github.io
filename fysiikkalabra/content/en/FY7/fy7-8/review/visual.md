VERDICT: FAIL
CONTENT-HASH: 725adfdc8c3bfd9f

## Blocking
- [Major] simulation canvas (assets/sims/fy7/fy7-8/sim.js:134, seen in sim-390, sim-1280, lab-1280, koe-1 captures) — the green bar legend is drawn as $P_\text{perille}$, a Finnish word visible to English students, while the readout below says $P_\text{arriving}$ — breaks the "no Finnish visible in en" rule and makes the legend and readout look like two different quantities — pass the subscript through the sim's translation function (en "arriving"), as the readout already does.
- [Major] figure "grid" (fig-7-390, theory-1280-2) — the English label "local substation" (fi "muuntamo") is much longer than the Finnish word and runs under the roof of the house, hiding the "l" and touching the roof line — an overlapping label in a translated figure — shorten or break the label in figures.json (e.g. two lines, or "substation" with a different word for the upper one), or move the label box in figures.py for every language.

## Polish
- [Minor] inquiry.json ennuste-dc "pending" — "read the part Core idea of the Theory summary", but the page heading is "Key idea" — use "Key idea".
- [Minor] inquiry.json kertaus-induktio feedback — "Today the transformer is based on this." is a literal rendering of the Finnish — "The transformer in this chapter is based on this."
- [Minor] koe-1 table headers — "transmission voltage" has no symbol or unit while the other columns do (same in fi) — "$U$ (kV)".

## Checked
- contact-1,2,3,5,6; sim-390; lab-1280; theory-1280-1 and -2; fig-7 (grid) and fig-9 (loss graph) at 390; transformer figure and worked example (390 and contact-2); prediction/check/exit captures via contact-2/3/5; exercise captures contact-5/6.
- Transformer figure, loss graph (axes, units, labelled points, decimal point), maths chains and the hero/charger illustrations are fine.

## Scores
illustrations 3 · typography 5 · Finnish 4 (English) · accessibility 4
