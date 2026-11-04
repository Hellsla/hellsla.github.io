VERDICT: FAIL
CONTENT-HASH: bebeb9ecaaeaf3c1
Round: 2

## Blocking
- [Major] L3-05, "Vastaus" disclosure (open-exercises-L3-1280-7; preview/fy2-5.html) — the revealed answer reads "930 kg" (the oil mass from part a)), while the answer box expects 940 kg (part b), the one the text asks for) and the solution says 940 kg. The page picks the first value in the Vastaus line within the 3 % tolerance, and 930 is 1,1 % from 940. A student who opens "Vastaus" is shown the wrong number — fix: in exercises.json set L3-05 `"tolerance": 0.005` (930 is then outside, 937-940 still accepted) so the reveal shows $940\,\text{kg}$; re-run the build and check the chip.

## Polish
- [Minor] all data tables (L2-05, L2-07, L3-04, L3-05) — numeric column headers sit left of their right-aligned numbers (e.g. "$H\,(\text{MJ/kg})$" over 19,0..8,3) — right-align numeric columns' headers (site.css `.ex-data`).

## Checked
- Round 1 Blocking (L3-04/L3-05 sub-tasks run together, box ambiguous): resolved. a)–d) are own bold paragraphs, the closing "Anna vastauslaatikkoon kohdan b) tulos kilogrammoina." is last (L3-04 and L3-05 captures).
- Round 1 Polish (L1-08 Kaava line): resolved (fraction with 3,6 MJ/kWh).
- open-exercises-1280-8 (L1-08), L2-1280-5, -6, -7, -8 (L2-05 table, L2-06 MC, L2-07 table and solution), L3-1280-4, -5, -6, -7, -8 (L3-04, L3-05 tables, Sijoitus, Vastaus).
- Table decimals in the new data tables use the comma; 1280 px only (no 360 px exercise capture; layout checks clean).

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
