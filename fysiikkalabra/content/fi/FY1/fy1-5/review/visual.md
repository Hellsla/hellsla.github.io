VERDICT: PASS
CONTENT-HASH: 7b52dab5ddaec0d4

## Blocking
(none)

## Polish
- [Minor] lesson.md Esimerkki, Järkevyys (example-390-2) — "Malli on siis tarkka murto-osan prosentista" is unnatural and repeats the sentence before it (the same sentence is in the tarkistus-3 model answer) — "Malli poikkeaa JPL:n arvosta vain murto-osan prosentin."
- [Minor] lesson.md Järkevyys (example-390-2) — "noin 26 AU" and "8 vuodessa" are numbers with units in plain text, and "26 / AU" breaks across a line — `$26\,\text{AU}$`, `$8$ vuodessa`.
- [Minor] Experiment "Alkutila" line (koe-1/koe-2) — values such as "= 6 m" and "= 2 m/s" in plain text next to maths labels — set the values as maths in the generator.
- [Minor] sim-390 — tick numbers on the graph canvas are about 9 px, hard to read on a phone — raise the canvas font size on narrow widths.
- [Minor] sim-1280 — the s0 slider sits beside the buttons while the others sit in a row below, so the reading order is uneven — put the sliders in one row or column.

## Checked
- Round-1 Major resolved: "(t, s)-kuvaaja" is now $(t, s)$ in Suoraan verrannollisuus, Nopeus kuvaajasta and Tiivistelmä (theory-1280-1 and -2). The solutions' Periaate and the tarkista hints render the same way (open-tarkista-1280-2). The only plain "(t, s)" left in lesson.md is the figure's aria-label, which is allowed.
- Hash 7b52dab5ddaec0d4 at start and end; the captures are current.
- Captures opened: top-390, fig-3-390, theory-1280-1, theory-1280-2, example-390-1/2, sim-390, sim-1280, open-tarkista-1280-2, open-exercises-L3-1280-1.
- Maths after the multiplication dot stays together: "· 2922 vrk", "· 3,16 · 10^7 s", "v · 1,0 s"; chains are aligned in rows. No red KaTeX and no clipping or overflow.
- Not opened at full size: the contact sheets, fig-1/2-390 (the motion figure was seen in theory-1280-1, the hero in top-390), the ennusta, selita, exit and L1/L2 exercise captures. These are unchanged by the fix and judged from the source and the deterministic checks.

## Scores
illustrations 4 · typography 5 · Finnish 4 · accessibility 4
