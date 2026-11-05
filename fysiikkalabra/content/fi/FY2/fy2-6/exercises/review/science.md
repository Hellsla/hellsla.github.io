VERDICT: PASS
CONTENT-HASH: 6ef997bed0905b37
Round: 3

Since round 2 (9fd1b2088 → HEAD) the only change to fy2-6's exercise set is one line in solutions.md, from commit 4ab4e1a5d. In the L1-09 "Muut vaihtoehdot", "… : 5000\,kWh \approx 5300" now reads "… : 5000\,kWh, mikä on noin 5300". exercises.json and answers.py are unchanged. The packet was regenerated, mode full.

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
- All 19 numeric answers were recomputed again in one python run, all within tolerance; the largest deviation is L1-03 (+1,05 %). L1-06 and L1-07 each have exactly one correct option. Hash 6ef997bed0905b37 at start and end.
- Round-3 line: 3,0 MW · 8760 h = 2,628·10⁷ kWh, and divided by 5000 kWh that is 5256, so "noin 5300" is right. The meaning is the same as before and still matches the "noin 5000" option and its feedback. The round-2 checks above still stand.
- FY2 scope: only E = Pt, shares and factor × energy are used.
