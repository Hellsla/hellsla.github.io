VERDICT: PASS
CONTENT-HASH: e198735ef8b8ce03

Round 2 review: round 1 had no Blocking findings. The changed content was checked at 390 and 1280 with every details element open.

## Blocking
(none)

## Polish
- [Minor] `inquiry.json` `kulmakerroin-g`, solution Kaava, at 390 px. The line "$a = \dfrac{\Delta(T^2)}{\Delta m}$ ja $a = \dfrac{4\pi^2}{k}$, josta $k = \dfrac{4\pi^2}{a}$" wraps inside the prose. The denominator $\Delta m$ then touches the $4\pi^2$ on the next line. Fix: split "josta" into a separate sentence, or write the three as separate equations joined by "ja" so that the renderer stacks them (as in `check-2`).
- [Minor] Tutki table (`aineisto`) at 390 px. The last header "$k = F : x\ (\text{N/m})$" runs past the card, and the unit is visible only after a horizontal scroll. Fix: use the header "$k\ (\text{N/m})$", since the text above already defines $k = F : x$. The table then fits at 390.
- [Minor] Tutki data. The readings $2{,}99$ … $10{,}79\,\text{cm}$ have two decimals, while the zero reading is $1{,}0\,\text{cm}$. Use the same number of decimals throughout (for science: realistic ruler precision).
- [Minor] Shared: no `units.css`, so the preview-only teacher box has no max-width (as in round 1).

## Checked
- **Tutki, 390 and 1280:** the table, the text, the opened model answer and the rubric. LaTeX renders, and division is written with a colon.
- **`virhe` figure in the theory capture at 390:** the "systemaattinen virhe" label is now dark and legible, so round 1 Polish 3 is fixed.
- **Sovella numerics `kulmakerroin-g`, `mittausmatka`, `jaksonaika` and `nollapiste` at 390:** answered, with hints and solutions open. Chains are aligned, and the answer boxes, Järkevyys and units are correct.
- **`linearisointi` at 390:** the options render, and so does the feedback panel.
- **`check-2` at 390:** the extreme-value chain is aligned, and $\text{g/cm}^3$ renders.
- **Hero at 390 and 1280:** unchanged.
- **Tables:** Tutki is 324 px at 390. The s4 and s6 tables are narrow and fit.
- **Page checks at 390 and 1280:** no `.katex-error`, no raw `$`, no chapter ids in the text, no console errors, scrollWidth equals viewport. check_layout reports OK at 360 (1 table scrolls) and at 1280.
- **Finnish:** the new texts are natural and the glossary terms are consistent (resoluutio, epävarmuus, systemaattinen virhe).

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
