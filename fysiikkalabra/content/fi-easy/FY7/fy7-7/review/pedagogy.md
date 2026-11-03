VERDICT: PASS
CONTENT-HASH: d5bac6dee83b4a91

## Blocking

## Polish
- lesson.md Kaava (the "missä Φ on ..." paragraph, 53 words) and the Tehollinen arvo "missä U₀ ja I₀ ..." sentence — one sentence defines seven symbols; too long for Selkeä suomi (rest of the lesson averages 9 words per sentence) — make it a bullet list, one symbol per line.
- inquiry.json ennuste-asento (correct option feedback) — quotes "2,51 V, kun f = 2,0 Hz" before the student has seen N and B — add "kun N = 500 ja B = 0,20 T".
- lesson.md "Voimalaitoksen generaattori ja tuulivoimala" — taajuusmuuttaja, vaihteisto, nimellisteho are heavy compounds for Selkeä suomi; a one-clause gloss on first use would help (e.g. "taajuusmuuttaja, laite, joka sovittaa taajuuden verkkoon").

## Checked
- Translation keeps the Finnish lesson's structure, ids, numbers, correct flags (structural diff of inquiry.json against fi: none).
- Opening question answered by the Ydinajatus text and by koe-1; slot goals covered (rotating coil, sinusoidal voltage, wind power), nothing extra.
- Predictions can be refuted by koe-1 (pause at peak, read flux and angle); min 2 before reveal.
- Staged example, 7 steps, readable at 390 px; unit check and order-of-magnitude step present.
- Figures (generator, phi-e, derive, power) legible at 365 px, colour paired with labels; simulation readout and controls usable at 390 and 1280 px.
- Exit ticket tests the main misconception (peak vs effective value) and the stationary-coil idea.
- Finnish: case endings after number+unit correct (230 V:n, 100 kV:n style); glossary terms used consistently.
