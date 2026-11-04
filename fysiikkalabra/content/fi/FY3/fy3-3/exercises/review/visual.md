VERDICT: PASS
CONTENT-HASH: d6c4bf6ac501e57b
ROUND: 4
Mode: delta

## Blocking
(none) Earlier Blocking: none. Round-1 Polish resolved: L3-05 Vastaus now says 145 °C (tarkasti 145,46 °C) and the Kaava is split into four display lines; L2-07 Sijoitus is one aligned block of four rows; L1-07 Vastaus has a subject.

## Polish
- [Minor] L3-05 Kaava (open-exercises-L3-1280-7) — each display formula sits in its own box with generous space, which makes the section long; one aligned block of the four lines would be tighter.
- [Minor] L3-04 Sijoitus — the sentence with three inline half-range fractions is unchanged (tiny \tfrac, a fraction may break at line end); the new aligned block with "(37,2 − 36,8) : 2" is the better form and could be used for the other lines too.
- [Minor] Task tables (all new ones) — header centred, numbers left or right aligned.
- [Minor] No 360 px captures of the new tasks (check_layout 360 is clean).

## Checked
- open-exercises-L2-1280-10: L2-07 (aligned four-row differences, Vastaus, Järkevyys).
- open-exercises-L3-1280-6: L3-04 end (aligned sums and half-ranges, Vastaus 0,6 K, Järkevyys) and the start of L3-05.
- open-exercises-L3-1280-7: L3-05 (Annettu, Periaate, split Kaava, Muunnokset); numbers re-computed (796,7 kPa, 418,61 K, 145,46 °C, 13,6 %).
- No clipping or overflow at 1280; °C written as ^\circ\text{C}.

## Checked in round 3
- Delta (HEAD): split rows read well in source: each continuation "\\ &= result" aligns under the first "=" of its aligned block, the Finnish decimal comma / English point and unit spacing are unchanged. check_layout.py 360 px --site is OK for fy3-2 (the site still serves the previous version of the formulas, so this does not yet prove the new rows). No 360 px solution captures exist in review/shots (only 390 and 1280 shots), so the 360 px result is judged from the source: rows are now at most about one line of text at 360 px.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4

## Checked in round 4
- Delta (HEAD~3..HEAD, solutions.md display maths only): The corrected forehead temperature is now a single display formula, which fits a 360 px line better than the old split row; the aligned block above ends cleanly (the trailing space after the last row is harmless). check_layout.py fy3-3 --width 360 on freshly built preview: OK (fi, en, fi-easy), no formula overflow, only the existing wide-table scroll warning.
