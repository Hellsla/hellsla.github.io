VERDICT: PASS
CONTENT-HASH: 9915b25c3d7b3277

## Blocking

## Polish
- [Minor] inquiry.json johtopaatos — "Kirjoita taulukkosi perusteella" sits directly under the phone-measurement card and its $E$ table; for an S2 reader "Kirjoita kokeen 1 taulukkosi perusteella" says which table.
- [Minor] optional boxes — summaries read "VALINNAINEN · Syventävä: …" (two labels for one status); harmless, could be trimmed at template level.
- [Minor] inquiry.json virhe (untouched text, only the title changed) — the quoted chain is a `kx-wide` scroller at 360/390 px, cut mid-formula with no scroll cue; one line as required.
- Tooling (not content): `scripts/screenshot.py fy7-15` crashes at `.worked .all-steps` because the worked example now sits in a closed optional box; captures were taken with an equivalent Playwright script.

## Checked
- Hash at start a46a26471bbb008d; lesson.md and inquiry.json were edited at 11:57 during the review, so I rebuilt, re-captured and reviewed that edit too; end hash 9915b25c3d7b3277, stable.
- Captures of preview/fi-easy/fy7-15.html at 360, 390, 1280 px, every stage closed and with all boxes open: Tutki (phone measurement card, Johtopäätös with Ydintehtävä tag), Selitä (Yleinen virhekäsitys in three short paragraphs, Tiivistelmä, Syventävä boxes opened), Sovella (3D task core, with "Vastaa näihin kysymyksiin järjestyksessä"), Tarkista (2. Selitä with tag, Syventävä laser task), exit ticket with answers open.
- Programmatic check at 360/390/1280, closed and open: no inline KaTeX on two lines, no page-level horizontal overflow; only wide inline maths is the `kx-wide` scroller in #virhe.
- Selkeä suomi: short sentences, a term explained where new ("komponentti eli osa"), physics unchanged; quantities in LaTeX with correct case endings.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 4
