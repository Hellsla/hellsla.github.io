VERDICT: PASS
CONTENT-HASH: 3ce5496422f13f04

## Blocking

## Polish
- inquiry.json exp-2 table at 1280 px (fy4-10-lab-1280-1.png) - last column "E'k (J)" still cut at the card edge (round 1 polish, still open) - make the table scroll visibly or narrow the columns.
- Sim readout at 390 px - ", E_p = 0,000 J" can start a line with a comma (round 1, still open) - keep the comma with the preceding value.
- lesson.md "Kimmoisa törmäys" - only the equal-mass swap is given, yet Koe 2 shows rows like v1' = -0,12 m/s; add one sentence that unequal masses need momentum and energy together, beyond this course, and the table is the data (round 1, still open).
- lesson.md Esimerkki, Tulos vs Järkevyys - result rounded to 1,1 m/s but energy after (32,5 kJ) uses 1,14 m/s; say "tarkemmalla nopeudella 1,14 m/s" (round 2, still open).
- Sim, strongest setting (kimmoisa, m1 0,60, m2 0,20 kg, v1 1,0, v2 -1,0): v2' = 2 m/s, so the blue arrow runs edge to edge and its tip touches the canvas border at both widths. It is inside, but a student may read it as cut off; leave a few px of margin.

## Checked
- Hash at start and end identical, 1b4a6b4ef5557e43.
- Only the sim changed since round 2 PASS. I rebuilt the preview (build.py fy4-10) and ran six settings at 390 and 1280 px (elastic 0,6/0,2 and 0,2/0,6 at v1 1,0, v2 -1,0; sticky 0,4/0,4 and 0,6/0,2; elastic 0,4/0,4; explosion 0,2/0,6), mid-collision and after.
- No velocity or momentum arrow or its label leaves the picture in any of them. Arrows stay readable in mild settings (shorter, still visible at 390 px), and the arrow lengths stay proportional within a run, so the comparison before/after still teaches.
- Momentum bars and energy column are unchanged and consistent with the arrows (p_kok equal before/now; E_sis grows for sticky).
- Lesson text, inquiry, predictions, experiments, example and exit ticket are unchanged since round 2; the numbers and the learning path stay as I passed them.

## Round 4 (delta)
Only change: mass options use the page decimal sign. Built fy4-10 and opened fi and en at 390 and 1280 px: no page errors; fi options read 0,20 / 0,40 / 0,60 kg, en 0.20 / 0.40 / 0.60 kg, both masses, matching the readout (0,240 vs 0.240). Round-3 findings carried forward; no new Blocking.
