VERDICT: PASS
CONTENT-HASH: f9f9e2931bcf38c1

## Blocking
(none)

## Polish
- lesson.md "Siirtohäviö" and inquiry.json johtopaatos model — "kaukolämmön häviö on suhteessa suurempi, koska kuuma vesi on ympäristöä lämpimämpää" explains why district heat loses at all (conduction through insulation, grows with temperature difference), but the electricity grid loses by a different mechanism (Joule heating), so the "koska" over-claims as the cause of the difference between the two percentages (C/B). Say "lämpöä karkaa eristeen läpi ... ja siksi häviö on kaukolämmössä merkittävä" without presenting it as the reason for the comparison.
- lesson.md "Muuntaja nostaa jännitteen..." — a transformer works only with alternating voltage; condition unstated (B, fine at FY2 level).
- inquiry.json check-c2 correct option — "siirtyy ympäröivään ilmaan"; the lesson says "ympäristöön" (underground cables and pipes heat the ground). Use "ympäristöön".
- lesson-answers.py — has exit-1 and exit-3 values, but exit-ticket.json holds only one question; stale.

## Checked
- Hash at start and end b356ea48282f972e; recomputed all lesson and inquiry numbers in one script (example 222,95/22,05 MWh; kaukolämpö 3,3 TWh = 9,17 % -> 9,2; wrong 10,1; sähkö 83 · 4 % = 3,3 TWh; 3 : 83 = 3,6 % ≈ 4; battery 15 %; check 375 : 0,75 = 500, wrong 281/469; Etsi virhe 480/20 MWh).
- Voltage table: loss scales as 1/U^2 (0,80 -> 0,0264 at 110 kV -> 0,0020 at 400 kV); 8,0 % and 0,020 %; 400-fold vs 20-fold correct; labelled as model values, not measurements.
- Exactly one correct option in every choice; each distractor wrong and its feedback right (incl. "kaksinkertainen jännite puolittaa häviön").
- Sankey proportions (80 / 77 / 3 and 73 / 7 px) match 96/4 and 91/9; electricity base (consumption incl. losses as input) stated.
- Scope: no Q = cmΔT, no P = UI or I^2R formulas, no chain efficiencies; data sourced (Energiateollisuus 2024) and examples marked.
- Worked example symbolic first, rounding reasons sound; exit ticket and summary agree with theory.
- Delta (commit 01da3ae6, option texts rebalanced): every changed option re-read; correct options still correct and match feedback, distractors still wrong with fitting feedback.
