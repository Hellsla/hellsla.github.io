VERDICT: PASS
CONTENT-HASH: d64ab1c8503f8cb7

## Blocking
None. Both round-1 Blocking items are fixed:
- s1 and s4 tables at 390 px: s1 is now Laite | Teho | Käyttö/vrk (table 293 px in a 324 px container), s4 is
  Vaihtoehto | Teho (324/324 px) with the other facts as three bullets. Every column and cell is visible with no
  horizontal scroll (measured: scrollWidth = clientWidth, rightmost cell inside the container). The s3 data table
  (201 px) also fits.
- `kartta` (380-unit viewBox, 358 px wide at 390) and `ketju` (420-unit, 358 px): every label renders at 17,0 px at
  390 px (measured from the computed font size × SVG scale); sub-indices are 11,9 px, normal KaTeX subscript ratio,
  and are clearly legible in the captures. Fractions are now slash fractions on one line. At 1280: 29 px.

## Polish
- [Minor] `ketju` (Sankey) — the loss labels "$248\,\text{MW}$" and "$4\,\text{MW}$" almost touch, and
  "$198\,\text{MW}$" runs into the green arrowhead at 390 and 1280 — move "$4\,\text{MW}$" right of its arrow (or below
  the row) and end the 198 label before the arrowhead.
- [Minor] unit.md, Ydinajatus last paragraph at 390 — the long inline formula fills a line and the next line starts
  with an orphan comma ", enemmän kuin…" — split it: "…$\approx 320\,\text{MJ}$, eli noin $90\,\text{kWh}$. Se on
  enemmän kuin…", or use a display formula.
- [Minor] sovella s3 model graph (solutions) — labels render at 11,9 px at 390 (600-unit viewBox, 24 px), below the
  brief's 14 px; it matches the reviewed FY4 Sovella graphs, so not Blocking — draw it on a narrower viewBox (about
  440) or with 30 px labels. Its reading lines also use orange and blue, the kinematic colours; use grey/green.
- [Minor] inquiry.json lt-5 feedback and `pelletti` solution — units are still stacked ($\tfrac{\text{MJ}}{\text{kg}}$),
  while tasks and solutions now use inline $\text{MJ/kg}$ — use inline units there too.
- [Minor] Shared: the catalog figure `fy2-4/grid` (Sovella `kuvio`) has 13 px labels at 390 — fix in the catalog.

## Checked
- Built `preview/fy9-energia.html`; Playwright at 390 and 1280 with all details open: no `.katex-error`, no raw `$`,
  no console errors, document width = viewport; `check_layout.py` OK at 390 and 1280.
- Opened at readable size: kartta 390/1280, ketju 390/1280, Tutki bar chart 390, s3 graph 390 and its caption,
  tables s1, s3, s4 at 390, theory kWh display formula, hook answer, s4 bullets, heat-pump item.
- Tutki bars are now sand/green (no orange or blue); Sankey and map hub have no orange; losses grey.
- Straight quotes: none left in visible text (only SVG attributes). kWh conversion is a display formula.
- Circled s3 points explained in the caption and alt text.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
