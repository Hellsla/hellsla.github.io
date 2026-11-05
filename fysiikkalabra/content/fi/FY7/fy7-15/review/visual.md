VERDICT: PASS
CONTENT-HASH: 1716666517002d89

## Blocking

## Polish
- [Minor] inquiry.json johtopaatos — "Kirjoita taulukkosi perusteella" now sits directly under the phone-measurement card and its $E$ table; "Kirjoita kokeen 1 taulukkosi perusteella" removes the doubt about which table.
- [Minor] optional boxes — summaries read "VALINNAINEN · Syventävä: …" (two labels for one status), and the opened theory box repeats its title as "Malusin laki ja Brewsterin laki"; harmless, could be trimmed at template level.
- [Minor] inquiry.json virhe (untouched text, only the title changed) — the student's quoted chain is a `kx-wide` scroller at 360/390 px, cut after "200 W/m² ·" with no scroll cue; one line as required, but a shorter quote would read better.
- [Minor] inquiry.json harjoitukset — the new lead "Aloita tehtävistä, jotka on merkitty Ydintehtäväksi …" is never shown (inquiry.py drops the exercises' lead text by the teacher's 2026-11-04 rule), so the student does not see this guidance.
- Tooling (not content): `scripts/screenshot.py fy7-15` crashes at `.worked .all-steps` because the worked example now sits in a closed optional box; captures were taken with an equivalent Playwright script (every `main details` opened, all-steps clicked).

## Checked
- Hash at start 6264313654dc2c37; the lesson was edited at 11:57 during the review (koe-2/ennuste-3 to core, new Ydinajatus sentence, virhekäsitys wording, harjoitukset text), so I rebuilt (build.py fy7-15), re-captured and reviewed that edit too (git diff); end hash 1716666517002d89, stable.
- Captures at 360, 390, 1280 px, every stage closed and with all boxes open: Ennusta (Ennuste 3 now core), Tutki (Koe 2 core, phone measurement card with table and choice, Johtopäätös with Ydintehtävä tag), Selitä (Kaksi polarisaattoria, Yleinen virhekäsitys, new Tiivistelmä bullets, scene, opened Syventävä theory box with Malus vector figure and graph, malus-koe and sovitus with solutions and fit graph), Sovella (siirto-3d core, Syventävä esimerkki/virhe/järven ranta), Tarkista (2. Selitä with tag, Syventävä laser task), exit ticket with answers open.
- Programmatic check at 360/390/1280, closed and open: no inline KaTeX on two lines, no page-level horizontal overflow; only wide inline maths is the `kx-wide` scroller in #virhe.
- Ydintehtävä tag sits cleanly above its h3; Syventävä boxes dashed when closed, solid when open, titles wrap inside the box at 360 px, nothing clipped.
- Changed Finnish fluent, glossary terms consistent, quantities in LaTeX with correct case endings ($374\,\text{lx}$:sta, $45^\circ$:n).

## Scores
illustrations 5 · typography 5 · Finnish 4 · accessibility 4
