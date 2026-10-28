VERDICT: FAIL
CONTENT-HASH: 3d67762731586994

## Blocking
- inquiry.json:131 (johtopaatos, stage Tutki) — the conclusion asks why weather-dependent production needs adjustable production and how nominal power differs from annual output, but nothing in Tutki shows either: the two tables give annual energies and unit sizes only, no variation in time, no wind capacity. Groups and nominal/mean power first appear in the later theory, and the model answer discloses them. The opening "Miksi monta voimalaa?" is therefore answered without evidence. Fix: add a data item (a day or week of wind output against consumption, invented and marked as an example, or real with source) before the conclusion, or put the conclusion `after` the theory stage.
- lesson.md:59-65 — the criteria list has no blank line before it, so it renders as one run-on paragraph "– Hinta: … – Teho: …" (1280 px capture): a text wall at the lesson's key comparison. Fix: blank line before the list.
- Tutki tables (data-fi, data-yksikko) at 390 px: the value column is clipped ("20,", "14,", "5 M", "100", "160"); the student cannot read the numbers the tasks need. Fix in the shared table component (or narrow columns); must fit 360 px.
- inquiry.json:173 (virhe), feedback of the last option — "123 000 GW olisi tuhat kertaa koko maailman sähköntuotanto" is false (world mean electric power is about 3 000 GW, so roughly 40 times). Fix: "moninkertainen koko maailman sähköntuotantoon verrattuna" or drop the comparison.

## Polish
- lesson.md:114 — "kapasiteettikerroin" is introduced and never used; the share (32 %) is carried by "osuus nimellistehosta". Drop the term; the nominal/mean distinction itself earns its place (it explains weather dependence and the lesson's main misconception).
- lesson.md:8 figure "plants" — nuclear fuel and fuel look identical (höyryturbiini), no generator and no heat arrow, though the Ydinajatus text stresses that heat is always lost. Add generator and a "lämpö" arrow (orange vs another cue, not colour alone).
- Figure "unit-power": bars on a log axis starting at 10^3 W make 5 kW look nearly equal to 1600 MW; a bar's length no longer means size. Use dots on the log axis, or label "pylvään pituus = tehon logaritmi" visibly; the "ruutu" in the text matches no drawn cell.
- lesson.md:59-65 — the criteria (price, transportability) are used only in the optional check 3; the core path never practises "vertaile kriteerien avulla". Also "voiko polttoaineen kuljettaa voimalaan (kyllä)" is cryptic; and "Ydinvoima tuotti eniten, noin neljänneksen tuotti tuulivoima" reads oddly: "Ydinvoima tuotti eniten ja tuulivoima noin neljänneksen."
- The source-note box in Tutki renders as a large pill with multi-line text (390 px capture); shared component.

## Checked
- Example: seven stages, one step each, symbolic first, units, check present; chain with colon as division.
- Prerequisites (Teho, Hyötysuhde) used; scope stays out of emissions and FY3 content.
- Prediction ennuste-1 has per-option repairing feedback, though it is mostly fact recall (justify on).
- Figures 2 and the opening figure legible and beside their paragraphs at 1280 px.
- Exit ticket tests grouping, E = P t and nominal vs mean.
- Finnish otherwise correct; "5,0 MW:n" cases right.
- Workload fits an hour on the core path; E = P t drilled five times (kertaus, tarkistus-2, siirto, exit, L1).
