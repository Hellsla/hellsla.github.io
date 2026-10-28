VERDICT: PASS
CONTENT-HASH: 2c3491834a24668e

Delta review over the audit's PASS (7ade301110d15aed): L1-04 (chainsaw W = Q1 − Q2) replaced by a figure task (fy3-11/pv-isobaari, work in an isobaric expansion); L3-02 answer 9.60 -> 9.6 (same value).

## Blocking
- none
## Polish
- none
## Checked
- Figure code: horizontal segment at p = 250 kPa from V = 1 to 4 l, grid 1 l / 50 kPa, every y tick labelled; end points on grid crossings; arrow shows expansion; no area or work value; screenshot matches the description.
- W_k = 250 000 Pa · 0,0030 m³ = 750 J (= 750 kPa·l); answers.py = 750.
- Tolerance 0,02 -> 735–765 J (the solution says so); rejects p·V2 = 1000 J and p·V1 = 250 J.
- Positive work in expansion, units (Pa·m³ = J, kPa·l = J) and 2 s.f. reasoning right; task text gives no values from the figure.
- L3-02: 9.6 equals 9.60, unit and tolerance unchanged.
