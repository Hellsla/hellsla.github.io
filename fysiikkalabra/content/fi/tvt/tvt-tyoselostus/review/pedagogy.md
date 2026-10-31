VERDICT: PASS
CONTENT-HASH: 3336b3617eb6b37b

## Blocking

None.

## Polish

- Step 6 says "ensin kirjaimin ja sitten lukuarvoin yksiköineen" but the example shows only $g = \tfrac{4\pi^2}{k}$. Add the substitution from tvt-kulmakerroin ($g = 4\pi^2 : 4{,}05\,\text{s}^2/\text{m} \approx 9{,}75\,\text{m/s}^2$) so the model calculation is shown in full.
- Step 4: label $y = 4{,}05x + 0{,}02$ as an example ("keksitty esimerkki") like the other guides do, and note the letters GA Pro shows in its fit box (see tvt-suoran-sovitus polish).
- Figure section numbers 4, 5, 6 match the FY10 template (docs/FY10_PLAN.md); saying "pohjan osat 4–6" in the intro would tie the figure to the text.

## Checked

- Read guide.json, guide.md and the figure's labels in full; ran the hash. Section names (Mittaustulokset, Tulosten käsittely ja graafinen analyysi, Tulos) match the teacher's report template. GA names used (Export graph as png, Show units in linear fit parameters, Export data as csv) are verified.
- Steps follow the report order: table → consistent precision → graph → equation with quantities and units → caption and reference → model calculation → result with uncertainty → legibility. Each says what and why (reader must be able to check).
- Goals (table and graph; reference and result with uncertainty) match; checklist covers table, caption/reference, equation and result.
- Mistakes are real ones (only derived columns, mixed precision, figure not referenced, x/y without units, result without uncertainty/unit, unreadable image), each with a fix.
- Page figure uses grey bars for the student's own values, so no invented data. Units in LaTeX; result $g = (9{,}7 \pm 0{,}4)\,\text{m/s}^2$ consistent with tvt-epavarmuus.
- Cross-links to kuvaaja, suoran-sovitus, epavarmuus sensible. No Word/Excel/spreadsheet leftovers.

## Delta 1 (2026-10-31, Finnish UI and screenshots)

- No screenshot in this guide (not needed); guides.py check: ok. Rendered preview checked: no leftover markdown or {{ga:}} markers.
- Terminology (tulosruutu, decimal comma in the report) now matches the GA guides. No screenshot needed.
