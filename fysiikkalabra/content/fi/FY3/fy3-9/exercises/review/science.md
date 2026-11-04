VERDICT: PASS
CONTENT-HASH: 426f38ee233f858f
Round: 2

## Blocking
(none)

## Polish
- exercises.json:152 (L2-05 a) — the sentence is garbled: "ja perustele, kun $T$ on kelvinlämpötila,, miksi lämpötilan on oltava kelvineinä". Delete the repeated clause "kun $T$ on kelvinlämpötila," and the second comma.
- solutions.md:147 (L2-05 Periaate) — the task no longer says that A is rigid and B has a free piston, so the solution goes from "p/T vakio" to "isokoorinen" without a reason. Add a short reason: the amount of air is fixed, so if p ∝ T the volume cannot change, and likewise for B. The data caption still says "pullossa A … ruiskussa B", so the text and the caption also disagree.
- solutions.md:255 (L3-05 c) — "Tehtävän uutta on tulojen keskiarvon käyttö rajapaineen laskemiseen." is a note to the author, not part of the model answer. Delete it.
- L1-07 is still the third plain Boyle compression at level 1 (after L1-01 and L1-02). Carried over from round 1.
- docs/exercise-bank/FY3.md:70 — the fy3-9 plan line still lists "ruiskumittaus → linearisointi", which L2-03 already covers. Name L2-07 (absolute zero by extrapolation) there instead. Carried over from round 1.

## Checked
- Round-1 Blocking (L3-04) resolved. The task says "ilma on ehtinyt luovuttaa ympäristöön vain osan energiasta", and the solution says "ei ehdi kokonaan" and "osa työstä". The adiabatic limit (about 703 kPa, about 237 °C) is far above 481 kPa and 76 °C, so the data now fit the stated condition.
- Round-1 Polish resolved: L3-05 a now says "mittausepävarmuus" and "pienenevät tasaisesti"; the `graph` tag is gone from L2-05; L2-07 justifies its two read points (fit residuals 0,04 kPa).
- All 20 answers recomputed in one script against exercises.json and answers.py, and they agree: 0,631 l; 126,9 kPa; 1,99 ml (least squares over all rows: 1,99 ml); −276,1 °C (least squares: −276,2 °C); 75,9 °C; 30,4 m.
- L3-05 c rewritten: the pressure ratio 399,7 : 101 ≈ 4,0 and the volume ratio 6,0 : 1,5 = 4,0 are inverse ratios, as Boyle's law requires. Correct.
- L2-05: p/T is constant to 0,3 % and V/T to 0,6 %, while p/θ falls from 4,99 to 1,50. The new "satunnainen vaihtelu" wording is right.
- L1-06 and L1-08: the options were reworded and reordered, and each still has exactly one correct option with correct feedback.
- Hash unchanged at the start and the end.
