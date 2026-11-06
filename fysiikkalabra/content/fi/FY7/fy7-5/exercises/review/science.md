VERDICT: PASS
CONTENT-HASH: 58b13b3e6286c0a5

## Blocking
- (none)

## Polish
- exercises.json:98 fy7-5-L1-09 tilanne C — 8,0 mWb through one turn means 0,5 T over 160 cm², far more than a bar magnet gives inside a school coil (about 0,1 mWb); use e.g. 0,080 mWb (the order does not change, e = 0 still).

## Checked
- Round 1, full mode; only L1-09 is new (type 9, ordering; prompt names |e| and "pienimmästä suurimpaan"). Hash identical start and end.
- Recomputed: A 200 · 3,0 mWb / 0,50 s = 1,2 V, B 50 · 6,0 mWb / 0,10 s = 3,0 V, C 0 (no change of flux), D vBl = 4,0 · 0,30 · 0,50 = 0,60 V, E 1 · 40 mWb / 0,020 s = 2,0 V; order C, D, A, E, B matches `order`, `answer` and the answers.py comment. Gaps between values are large, so rounding cannot change the order.
- Conditions stated: uniform change, "yhden kierroksen vuo" defined in the task (as in the lesson), rod, v and B mutually perpendicular for e = vBl.
- The chapter's warned mistakes are built in and named in the solution: forgetting N (A, B drop to 6,0 mV and 60 mV, checked) and "large flux, large voltage" (C). Sign of E handled correctly as magnitude only.
- Solution complete, each formula before substitution; inline chains short (estimated under 250 px, text only, not rendered).
- All numeric answers of the chapter recomputed in one script: all within tolerance.
