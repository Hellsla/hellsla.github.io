VERDICT: PASS
CONTENT-HASH: 210428203ba1fe2b

## Blocking

## Polish
- inquiry.json:523, :635 (exp-1, exp-3 Vastaus) — "simulaation mallin arvot esitetään kahdella numerolla" is not what the page shows: the readout and table give 40,0 m and 10,0 s. — Fix: say that two figures is the convention chosen for the model values.
- inquiry.json:647–669 (data) — tolerance 0,03 accepts readings x₂ = 18,6 … 19,5 m at t = 10 s, but the solution says the graph can be read "noin metrin tarkkuudella". — Fix: raise the tolerance to about 0,05, or say the reading is good to about half a metre.
- lesson.md:308 (Esimerkki, Tulos) — the two figures of v are attributed to Δt = 40 s alone. Δx = 120 m − 20 m = 100 m is a difference of graph readings and limits just as much. — Fix: name both.

## Checked
- One script ran answers.py and my own formulas on all 12 exercises and every inquiry number, mistake values included: all match and are within tolerance.
- Both round-1 Blocking items are fixed. L2-02 now checks 1,2 · 4,2 min ≈ 5 min. The data solution now reads about 19 m (Δx ≈ 15 m) and justifies two figures by the reading precision and the scatter. The least-squares slope 1,494 ± 0,029 m/s and intercept 4,10 m are confirmed.
- Every solution states the given and asked values, a principle that really applies, and the unknown in symbols before numbers. Conversions are right. The Vastaus lines name the limiting datum.
- The reasonableness checks are real and correct: back-substitutions, x₀ = −11 m for the sledge, 4,8 s through the origin in check-2, L3-01 lying between 5,0 and 3,3 m/s, Eeva's 40 m in L3-02 (50 m > 45 m), the 0,67 m/s trap in L3-03, the km/h comparisons.
- Figures are to scale: displacement axis (40 px/m), jogger graph (0/20/120/170 m), cart E graph, data points and line (4,10 → 19,10 m).
- The predictions and their feedback match sim.js CASES at t = 0, 4, 6 and 10 s. The experiments lock tapaus and vary t, and simState gives xA and x2. pos, vel and path are correct, and the model's limits are stated in Mallin oletukset.
- The hash was unchanged at the end of the review.
