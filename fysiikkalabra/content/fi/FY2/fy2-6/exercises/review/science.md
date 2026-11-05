VERDICT: PASS
CONTENT-HASH: 7ba8761f49283226
Round: 4

Since round 3 (4ab4e1a5d → HEAD) the only change to fy2-6's exercise set is the L1-09 correct-option feedback in exercises.json, from commit 442c889ba. Its chain is split with "eli", and "suuruusluokaltaan 2000" now reads "joten lähin vaihtoehto on 2000". solutions.md and answers.py are unchanged. The packet was regenerated, mode full.

## Blocking

## Polish
- solutions.md:73 (L1-09 Kysytty) — still ends with "suuruusluokka". The feedback now says "lähin vaihtoehto" (resolved there), so this is the last place the old wording is left.
- exercises.json:136 (L1-09, correct-option feedback) — "$1000\,\text{kW} \cdot 8760\,\text{h}$, eli noin $8{,}7 \cdot 10^{6}\,\text{kWh}$" is off: 1000 kW · 8760 h = 8,76·10⁶ kWh ≈ 8,8·10⁶. The 8,7 belongs to 990 kW. Write "$990\,\text{kW} \cdot 8760\,\text{h}$", or keep 1000 kW with ≈ 8,8·10⁶ and ≈ 1800. The keyed option is unaffected.
- exercises.json:116 (L1-09) — the fix dropped "Esimerkkinä olevan" from the turbine and the house. Restore one marker, e.g. "(esimerkkiarvot)".
- exercises.json L2-07 and the L3-05 table — the IPCC life-cycle factors are CO₂ equivalents but are called "hiilidioksidimäärä" (carried over).
- exercises.json:398 (L3-05) — "Tehon säädettävyys: Tasainen" (carried over).

## Checked
- Round-4 feedback: 0,33 · 3,0 MW ≈ 1 MW = 1000 kW; 8,7·10⁶ : 5000 = 1740, so the nearest option is 2000. This agrees with the key, "Valitse lähin arvo" and the Mallivastaus (solutions.md:83). The only slip is the one under Polish.
- L1-09 options recomputed: mean power gives 1734 → 2000; rated power gives 2,63·10⁷ kWh : 5000 = 5256 → 5000; unconverted MWh gives 1,7 → 2; 3,3 % gives 173 → 200. The nearest option is the same linearly and on a log scale. Exactly one option is correct, and every distractor's feedback is right.
- solutions.md "Muut vaihtoehdot" ("noin 5300") and the answers.py comment (1735 houses → about 2000) still hold.
- All 19 numeric answers were recomputed in one python run, all within tolerance; the largest deviation is L1-03 (+1,05 %). L1-06 and L1-07 each have exactly one correct option.
- Hash 7ba8761f49283226 at start and end. FY2 scope: only E = Pt, shares and factor × energy are used.
