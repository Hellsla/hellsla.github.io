VERDICT: PASS
CONTENT-HASH: 210723c3675594ef

Round 2 (delta review; round 1 PASS at 23902d39dc18f729). Fresh captures were taken at 390 and 1280 with every details element open and the model answers and Esimerkki stages revealed (Playwright, preview built with `build.py fy12-koe`).

## Blocking
- none

## Polish
1. [Minor] inquiry.json, Tutki "Vastaus B": the list fixes the line breaks at 1280. At 390 the Sijoitus line still breaks after "=" and leaves "1,111 m/s²" alone on the next line. Optional: use display math for the Sijoitus line.
2. [Minor] unit.md, Esimerkki: the stage labels (Tunnetut ja kysytty, Yksikkömuunnokset, Tulos) differ from the steps figure (Annettu ja kysytty, Muunnokset, Vastaus). Using the same labels would also let the mapping sentence go. This is the same issue as pedagogy Polish 1.
3. [Minor] fy12-koe-s2-graph at 390: the tick numbers render at about 10 px (the figure is scaled to 298 px). Round 1 Polish 4 on the tick size still applies.

## Checked
- The round 1 Polish fixes are in. The source_note chips read "Keksitty esimerkkiaineisto" once, and the note text starts with its content ("Luvut on valittu…"). The steps figure uses one neutral tint, with no green or orange groups. The pendulum point labels sit clear of the L axis and the dashed reading lines at both widths.
- The new text (the mapping paragraph, the Esimerkki mapping line, testi-15, testi-22, the s2 Yleisiä virheitä list and the Tutki rubric) renders with LaTeX and decimal commas. No `.katex-error`, no raw `$`, and no horizontal overflow (scrollWidth 390/1280). The page load has no console errors.
- The other round 1 passes stay: the hero, the graph figure and the tables.

## Shared issues
- The preview teacher-notes box is wide at 1280 (preview only), unchanged.

## Scores
illustrations 4 · typography 5 · Finnish 4 · accessibility 4
