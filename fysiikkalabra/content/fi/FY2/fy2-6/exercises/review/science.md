VERDICT: PASS
CONTENT-HASH: db6b0a8bbd9663c1

## Blocking

## Polish
- exercises.json:107 vs solutions.md:69 (L1-08) — the answer field is 2750 h, but Vastaus says 2800 h; similarly L2-05 (22,8 vs 23) and L3-05 (16,6 vs 17). All are inside tolerance and follow the existing L2-02 pattern, but the shown answer and the solution should agree — use the rounded value in `answer`, or give both in Vastaus ("2750 h ≈ 2800 h").
- exercises.json:351 (L3-05 c) and :225 (L2-07) — "hiilidioksidipäästöt vuodessa" from life-cycle factors are the life-cycle emissions attributed to one year's production, not CO₂ emitted that year (wind emits mostly at construction). Add "elinkaaren päästöistä vuoden tuotannolle kuuluva osuus" (B-level wording, minor). IPCC values are CO₂-ekv.
- solutions.md:191, :205 (L3-04) — "summa on 20,4 GW" and "67,3 GW · 24 h" add up daily powers as a power. Write "(ΣP)·24 h" as in the Kaava line.
- L2-07 gives wind 12 g/kWh and L3-05 gives wind 11 g/kWh in the same chapter. Use one value, or say they are different examples.

## Checked
- Recomputed all eight new answers in one script: L1-08 2750 h, L2-05 22,79 pp (totals 68,0 and 80,0 TWh), L2-06 A 32 %, B 28,5 %, C 33,3 % (best C), L2-07 1,616·10⁶ t, L3-04 others 1,2/3,2/6,1/6,7/4,7/1,0/−0,5 GW (max 6,7), wind 489,6 GWh = 32 %, L3-05 16,60 €/MWh (nuclear 10,57), 3180 t and 113 530 t. answers.py and exercises.json agree within tolerance.
- Every Järkevyys is numerically true: L1-08 (35 GWh, 31 %), L2-05 (shares sum 1,00; ×13), L2-06 (525 600 MWh, 0,29), L2-07 (1,64·10⁶ t, 0,99, ×68), L3-04 (1615 − 588 − 490 = 537 GWh and 22,4 GW·24 h = 538 GWh; 30 %), L3-05 (×33, ×36, 0,33).
- FY2 scope: no mgh, no cmΔT, no efficiencies at all, only E = Pt, shares and orders of magnitude.
- MC L1-06 (kivihiili) and L1-07 (säätövoima): one correct option each, and the distractor feedback is right (perusvoima, sääriippuvainen).
- L2-06 error task: the student's claim is really wrong (B has the largest E but the smallest share).
- Data that are not real statistics are marked as examples. Magnitudes are plausible (9 GW wind, 8,4–10,6 GW load, IPCC-like life-cycle factors).
- The L3-04 Sunday surplus (−0,5 GW) is correctly read as export, storage or curtailment. The L3-05 assumptions (constant output, build cost only) are stated in the task and used in the solution.
