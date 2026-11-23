VERDICT: PASS
CONTENT-HASH: 7013f5c43b745e8d

## Blocking
(none)

## Polish
- [Minor] sovella s4 b) mallivastaus — the line "Linjan nimellisjännite … $\tfrac{20\,\text{kV}}{\sqrt{3}} \approx 12\,\text{kV}$:n jännitteessä" sets a fraction chain inside running text; it renders legibly at 1280 px, but check the 390 px wrap. A fix is optional.
- [Minor] sovella s4 a) — the resistance row sits in its own display box with a trailing comma ("… $\Omega$,"), then the text continues "joten …". It reads fine, but it is a slight rhythm break. Optional.

## Checked
- Contact sheets 1, 2, 9, 10, 12 and 14 (the opening, ennusta, tutki, selita, esimerkit, tehtävät, tarkista, teacher notes and the Sovella solutions).
- At readable size: stage-exercises-1280-1 (task card, Ydintehtävä layout) and stage-exercises-1280-25 and -26 (the changed s4 solution a), b) and c) with the new b) wording and Yleisiä virheitä). The text is current for hash 7013f5c43b745e8d.
- At contact-sheet scale: the figures (hero, kartta, kipina, levyt, etuvastus, s1 voimakuvio, s3 graphs). I did not open each fig-N-390 capture at full size. The earlier PASS covered them, and the diff touched only s4 b) text.
- In the changed s4 b) text: units are in LaTeX with case endings ("$12\,\text{kV}$:n"), the decimal comma is used, `\cdot` is used, and there are no plain-text quantities and no KaTeX errors. The wording is fluent: it separates the line voltage $20\,\text{kV}$ from the phase voltage $12\,\text{kV}$, calls $4\,\text{mm}$ a lower bound and not a safe distance, and the Yleisiä virheitä items match.
- Layout: no clipping or overflow is visible, reading width is consistent, and open solutions stay inside their cards.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
