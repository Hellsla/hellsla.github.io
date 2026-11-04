VERDICT: PASS
CONTENT-HASH: 22726adfb48c9d40

## Blocking

## Polish
- content/fi/FY2/fy2-5/exercises/solutions.md:144 (L1-08) — the rounding is justified "kuten massassa 3,0 kg", but the task gives "kolmesta kilogrammasta" in words and the mass is not used in the conversion; lessons/FY2/fy2-5/answers.py:29 also computes from H·3,0 rather than from the given 144 MJ — justify the figures by 144 MJ (1 kWh = 3,6 MJ is exact), and compute `144 / 3.6`.
- content/fi/FY2/fy2-5/exercises/exercises.json:207 (L2-07) — the "esimerkkimittaus" lies exactly on one line (every step −0,65 kg). The guardrail says real data "eivät yleensä sijaitse täsmälleen samalla suoralla" — add ±0,01–0,02 kg scatter, or say in the solution that the points have been idealised.
- content/fi/FY2/fy2-5/exercises/solutions.md:191 (L3-05 Järkevyys) — "2120 : 0,90 = 2350 kg" is 2356 ≈ 2360 kg. Correct the number (the check still holds).
- exercises.json:275/345 (L3-04, L3-05) — the two new level 3 tasks have the same structure (annual useful heat → η and H → fuel mass, then η falls), and their pellet/oil efficiencies are swapped (85/90 % vs 90/85 %). Vary one of them (for example give it the emissions part from the plan), or use the same boiler values in both.
- docs/exercise-bank/FY2.md:35 — the plan still lists "kynttilän lämpöarvon mittaus vesitölkillä". That needs Q = cmΔT, which is outside FY2 scope (FY3). The set rightly replaced it with the mass-loss task L2-07; update the plan to match.

## Checked
- Recomputed all eight new answers in one script against answers.py and exercises.json: L1-07 15, L1-08 40, L2-05 5,625, L2-07 18,42, L3-04 3313 (oil 1237, η 0,70: +710), L3-05 1075,6 (oil 985, η 0,75: 2824, +471). Every json answer is inside its tolerance.
- Every Järkevyys number recomputed: L2-05 (1,41·13,61 = 19,2), L2-07 (1,1 MJ/min → 18 kW), L3-04 (2820 kg, 3320 kg, ratio 2,68), L3-05 (ratio 1,20). All true apart from the one slip above.
- The L2-05 moisture table matches H = 19,0(1−w) − 2,44w to within 0,03 MJ/kg; consistent with the lesson (dry wood 19 MJ/kg, air-dry wood 15 MJ/kg).
- FY2 scope: no mgh, no c·m·ΔT, and at most one efficiency per task (L3-04 and L3-05 use E_hyöty = ηHm), so there is no chain product.
- MC L1-06 and L2-06: exactly one correct option, and every distractor's feedback is right (78 MJ = 21,7 kWh).
- Food and fuel are kept apart as the guardrail requires. Notation as in the lesson.
- Magnitudes realistic (18 kW pellet boiler, 13 300 kWh/a house).
