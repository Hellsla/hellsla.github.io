VERDICT: PASS
CONTENT-HASH: 698712979e3823c0

## Blocking
(none)

## Polish
- [Minor] fy7-s1 d) Vastaus — "Ja Δx ≈ 7,2 cm" starts a sentence with a capital Ja after a boxed result; as in fi, it reads as a stray start. Fix: "Lisäksi Δx ≈ 7,2 cm" or box both.
- [Minor] fy7-s1 mallivastaus a) — the two "- Jotta ioni kulkisi…" / "- Nopeus … ei ole voima" lines follow the paragraph without a blank line and render as plain hyphen lines, not a list (same in fi and en).
- [Minor] subscripts — $F_\text{s}$, $B_\text{s}$, $U_\text{s}$ in the figure and text are consistent with fi; "s" for sähköinen and valitsin is not explained, but each quantity is defined where it appears.
- [Minor] 390 px top — the task tab strip's second tab is overlapped by the Kuuntele button (shared header, as in fi).

## Checked
Own captures (scratchpad/tools/cap_sovella.py, preview/fi-easy/FY7-sovella.html, 390 and 1280, every box open).
- top, s1 at 390 (task text, figure, a)–e) model answers, Hyväksytään myös, Yleisiä virheitä), s2 at 1280 (intro box, graph, parts).
- All six figures: labels Finnish (piikiekko, analysointimagneetti, nopeusvalitsin, lähde, suhteellinen intensiteetti, näkyvä, kuori, ydin, ilma), decimal comma on the spectrum and grating ticks, geometry identical to fi.
- s5 task with tables and graph at 390 (compared with en); layout of the formula boxes: chains break at the product sign, no shrinking; s1 d) split mv line fine.
- Reading level in what I opened: sentences short, no stacked "Tämä tarkoittaa", one voice, units and numbers in LaTeX; no plain number with unit outside LaTeX.
- check_layout.py FY7-sovella --width 340 and 360: OK for fi-easy. scrollWidth equals viewport at 390 and 1280.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
