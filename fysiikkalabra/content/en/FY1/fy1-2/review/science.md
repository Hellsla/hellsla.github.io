VERDICT: PASS
CONTENT-HASH: 34633fa58b56cc7b

## Blocking
None.

## Polish
- inquiry.json `voyager-malli` / sim model box — the course scope note gives the heliopause crossing at 119.7 AU (NASA/JPL), but the lesson and sim use 119.0 AU (Burlaga et al. 2019). Both are cited values. The model still matches JPL's 143.05 AU (Earth distance, Feb 2026) within the stated ±1 AU. Consider aligning the scope note with the source the lesson cites.

## Checked
- The new table (lesson.md "A unit for every scale") carries the same six rows, sizes, units and unit values as the former list, unchanged: fm 10⁻¹⁵ m, nm 10⁻⁹ m, µm 10⁻⁶ m, km 10³ m, AU ≈ 1.5·10¹¹ m, ly ≈ 9.46·10¹⁵ m. Each unit suits its scale, and the text after the table (0.11 nm, 1.7 fm) agrees with fy1-1.
- Recomputed in one script: AU light time 499 s = 8.32 min; worked example 4.503·10⁹ km, 4.17 h (3 s.f. justified by 30.1 AU); 10⁷/10⁸/10⁹ km → 33.4/334/3340 s; siirto 3.236 AU/a; Mercury 3.22 min (193 s); Saturn 79 min; 1 h of light ≈ 7 AU, 1 week > 1200 AU, 1 ly ≈ 63 000 AU; 1.85·0.92 = 1.702 m².
- Voyager model d = d₀ + v(t − t₀): table rows for 2018, 2022, 2026 and 2030 (119.0/131.9/144.9/157.8 AU; 16.5/18.3/20.1/21.9 h), 2026-01-01 142.2 AU/19.7 h, Feb 2026 ≈ 142.5 AU, ratio 142 to one AU: all reproduced.
- Sim constants (AU, c, Moon 3474 km, JPL semi-major axes, D₀, v, t₀) implement the stated model. Its limits are stated: model values, Sun-referenced signal time ±8 min, and the Speed setting does not change the physics.
- Experiment koe-1 varies n with the date locked, so it isolates the parameter. koe-2 varies the date, and the keys vAU and vTh exist in simState.
- Significant figures rules, the 0.0250 m check and the merkitsevat item are correct, and the exact-number convention is stated.
- km² conversion (error-spotting item, misconception, summary) is correct.
- Every choice item has exactly one correct option, every distractor is wrong and its feedback is right. The model answers and the exit ticket agree with the theory.
- SI base-quantity table is correct, and the Kibble balance caption is correct (kilogram defined through the Planck constant).
