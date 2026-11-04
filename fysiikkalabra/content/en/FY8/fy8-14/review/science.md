VERDICT: PASS
CONTENT-HASH: 6a1e34abe8699d59

## Blocking

## Polish
- inquiry.json:157–167 (koe-1 `names`/`values`) — "potilas", "ilmaisu" and "koinsidenssi" are untranslated and show on the page ("Initial state: … potilas: one tumour, ilmaisu: koinsidenssi"). Write "patient", "detection", "coincidence".
- lesson.md:58 "for tungsten they are at about 59 keV" — tungsten's K lines are at about 58–59 keV (Kα) and 67–69 keV (Kβ). Write "at about 59 and 67 keV". Carried over from the Finnish review.
- lesson.md:178 "the calcium atoms in it have many electrons" — the main cause is the larger atomic number (photoabsorption rises steeply with Z). Carried over from the Finnish review.

## Checked
- Every number in lesson.md (text and SVG labels), inquiry.json and exit-ticket.json matches the passed Finnish version (decimal commas mapped to points); figures.json labels keep their numbers.
- One script recomputed: worked example n_A 2.353, n_B 4.198, 2^1.845 = 3.59 and 0.1957 : 0.05449; E_γ = 8.187·10⁻¹⁴ J = 511 keV; f = 1.2355·10²⁰ Hz with mistakes 1.24·10¹⁷ and 7.71·10³⁸; transfer 772.0 → 770 MBq with mistakes 116.6, 600, 304.8; error-spotting 0.36 · 0.15 = 0.054.
- Interpret table: 20 cm tissue 0.05 / 1.6 / 3.3 %, ratios 7 and 2; Tc-99m 6 % after a day; Am-241 1.6 % in 10 a; 25 kGy → 6 K; lead 3.9 / 0.26 mm → ratio 15; TOF 0.3 ns → 4.5 cm.
- The TOF, characteristic X-ray and "model does not use arrival times" fixes of the Finnish round are carried over correctly in the theory, ennuste-1, the sim model box, the conclusion and the exit ticket.
- ennuste-2/johtopäätös model values (18 / 4.0 / 1.4 / 0 cm) are named model values; exactly one correct option in every choice item; distractor feedback is correct.
- Radiotherapy 5 × 0.40 Gy = 2.0 Gy agrees between figure, ennuste-3 and theory.
- Graph capture (fig 12) to scale: halves at 1.1 / 2.2 cm (bone) and 3.4 cm (tissue).
