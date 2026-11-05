VERDICT: PASS
CONTENT-HASH: 410641b2006a3acc
Round: 2

The round-1 Blocking item is resolved. Commit 9fd1b2088 changed three lines of exercises.json for fy2-6, all in L1-09: the task text, the 4th option and its feedback. The L1-09 solution was also changed. The packet was regenerated, mode full.

## Blocking

## Polish
- exercises.json:136 (L1-09, correct option's feedback) and solutions.md:73 (Kysytty) — both still say "suuruusluokaltaan 2000" / "suuruusluokka". The question now says "Valitse lähin arvo". Write "lähin vaihtoehto on $2000$", as the Mallivastaus does (solutions.md:83).
- exercises.json:116 (L1-09) — the fix dropped "Esimerkkinä olevan" from the turbine and the house. The situation is generic, not a statistic, so this is minor. The FY2 scope note asks for invented situations to be marked as examples. Restore one marker, e.g. "(esimerkkiarvot)".
- exercises.json L2-07 and the L3-05 table — the IPCC life-cycle factors are CO₂ equivalents but are called "hiilidioksidimäärä" (carried over).
- exercises.json:398 (L3-05) — "Tehon säädettävyys: Tasainen" (carried over).

## Checked
- L1-09 recomputed. With mean power the answer is 1734 houses; with rated power it is 3,0 MW · 8760 h = 2,63·10⁷ kWh, divided by 5000 kWh that is 5256 houses. Of the options 2 / 200 / 2000 / 5000, the nearest is 2000 for the right method and 5000 for the rated-power error, both linearly and on a log scale. The task now separates the misconception the lesson names.
- L1-09 distractors: 8670 MWh : 5000 = 1,7 → "2"; the 3,3 % reading → 173 → "200"; rated power → 5256 → "5000". Each feedback's mechanism and numbers are right, including 2,6·10⁷ kWh. There is exactly one correct option.
- "Valitse lähin arvo" fits the option set. The solution's "Muut vaihtoehdot" (≈ 5300 with rated power) agrees with the new option and its feedback, and the solution no longer calls a value wrong while the key rewards it.
- answers.py comment for L1-09 (1735 houses → about 2000) still holds.
- All 19 numeric answers were recomputed again in one python run, all within tolerance; the largest deviation is L1-03 (+1,05 %). L1-06 and L1-07 each have exactly one correct option. Hash 410641b2006a3acc at start and end.
- FY2 scope: only E = Pt, shares and factor × energy are used.
