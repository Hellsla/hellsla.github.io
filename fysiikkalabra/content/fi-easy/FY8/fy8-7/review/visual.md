VERDICT: FAIL
CONTENT-HASH: 2bd317b00068550c

## Blocking
- [Major] lesson.md "Tunneloituminen" + preview/fi-easy/fy8-7.html (#tunneli) — the optional (Valinnainen) tunnelling box is a closed `<details class="opt">` that also swallows the following "Yleinen virhekäsitys" and "Tiivistelmä" (the page has no other Tiivistelmä); opened at 390 and 1280 px, all three sit inside it — the chapter summary and the misconception about laser danger are hidden from a student who skips the optional box — move `## Tunneloituminen` after `## Tiivistelmä` in lesson.md (or end the optional box before Yleinen virhekäsitys) and rebuild.

## Polish
- [Minor] tunnel figure at 390 px (opened box) — labels "este", "E", "tuleva elektroni", "esteen takana" are about 7 px tall and the diagram is small — enlarge label font in the SVG.
- [Minor] inversion figure (fig-7-390) — the green pump arrow passes through the E2 level line, so it can look like it stops at E2 — offset it from the E2 line or draw it with a gap.
- [Minor] qdots figure (fig-11-390) — hf column is black while λ is colour-coded; fine, but the 5 nm and 6 nm dots (orange, red) nearly merge with the lines' red/orange palette — acceptable, optional.
- [Minor] lesson.md "Atomi ja fotoni" first sentence — "Luvussa *Vetyatomin…* atomi voi ottaa vastaan eli absorboida fotonin" lacks a verb for the reference — "Luvussa … nähtiin, että atomi voi absorboida eli ottaa vastaan fotonin."

## Checked
- contact-2; fig-2 (hero), fig-5 (processes), fig-7 (inversion), fig-9 (cavity), fig-11 (qdots), fig-13 (rate-graph) at 390 px.
- Example stages and the simulation in contact-2 (#17–#23); fy8-7 tunnel box opened with Playwright at 390 and 1280 px (no horizontal overflow, scrollWidth equals width).
- Text of Ydinajatus, Kaava, Esimerkki, virhekäsitys read for notation and Finnish.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 3
