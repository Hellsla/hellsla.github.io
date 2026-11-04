VERDICT: PASS
CONTENT-HASH: cd198f4f9413a502
ROUND: 2

## Blocking
(none) No visual Blocking in round 1. Changed tasks re-read: ice-melting 8-13 (plateau-reading hint, tolerance, "Taulukon lukeminen"), boiling 8-15 (now 60,0 kPa, linear interpolation between 50,0 and 70,0 kPa: 85,65 -> 14,4 K, matches answer 14.4), stearin 8-19 (split paragraphs, colon division), milk (units added). Solutions and answers agree.

## Polish
- [Minor] 8-13 ice (L2-06) — tolerance 0,08 accepts 312 kJ/kg (-6,6 %), the very value the Vastaus calls "liian pieni" (the naive 130 s reading); use tolerance 0,05 (334 +/- 17 kJ/kg) so the unwanted reading is not marked correct. For pedagogy/science to confirm.
- [Minor] 8-19 stearin Mallivastaus c) — "4190 · 35,0 J = 146 650 J" and "2 406 650 J" lack units on the factors; add them.
- [Minor] Data tables (L2-06, L2-07, L3-05) — header/number alignment (site-wide).
- [Minor] 8-13 vs existing L1-05 overlap in context (heating curve, melting heat); different method, acceptable.
- [Minor] Answer-field wording "Vastauslaatikkoon" vs "Vastauskenttään" in fy3-4.

## Checked
- 1280 px: L2-1280-5 (8-12 solution), -6, -7 (8-13 task, table, solution), -8, -9 (8-14 error analysis, 8-15 task and table), L3-1280-6 (stearin table, split Taulukon lukeminen), -9 (milk end). Captures newer than the fixed content. Slopes 1,14 K/s and 0,575 K/s agree with 600 W / (0,250 kg c). No red KaTeX, nothing clipped.
- Diff HEAD~1 read. No 360/390 open-state capture; relied on the layout check.
- No plain-text quantity in the changed text.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
