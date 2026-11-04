VERDICT: DONE
Round-1 fixes; check_lesson.py fy7-11 all ok.
Science Blocking (water n): Daimon & Masumura 2007 (20 °C) values 1,3315 / 1,3334 / 1,3375 / 1,3431 now used throughout.
- lesson-answers.py: WATER 1.3315 / 1.3431, docstring, stale comments fixed (flint 3,92°, water 0,85°, pool 25,4 mm, bows 42,30° / 40,63°, width 1,66°, secondary 50,5° / 53,5°, θ(30°) 28,2°).
- lesson.md: table; violet n = 1,3431; θ max 42,3° at n = 1,3315 (Polish: matches the table).
- sim.js + figures.py: water Cauchy refit through 405/589/656 nm (1.32289, 0.00395357, −0.000105379); tests/sims vesi-ero 0,9108 → 0,852.
- figures.py theta-graph: n = 1,3315 (description "n = 1,332"), peak label and description 42,3°; drop uses 1,3315; observer comment 1,7°. Figures regenerated.
- inquiry.json: johtopäätös water 0,85°; siirto n values, hint β 40,57° / 40,15°, solution tan 0,85628 − 0,84358, answer 25.396, mistakes 0,025396 m and 11,23 mm (sin); tarkistus-2 n values, 225 310 − 223 364 = 1946 km/s (1,95 · 10³), 2000-mistake feedback and ratio updated.
Pedagogy Blocking: hook no longer gives the directions; θ step "Kokonaiskääntymä on 180° + 2α − 4β … 180° miinus kokonaiskääntymä" added; prism-angles aria-label "huippukulma A".
Polish: koe-1 model answer names the approach to total internal reflection.
