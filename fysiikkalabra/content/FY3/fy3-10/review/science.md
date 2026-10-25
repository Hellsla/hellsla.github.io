VERDICT: PASS
CONTENT-HASH: ba92ddd92dc584ef

## Blocking

## Polish
- solutions.md:47 — at 180 bar oxygen is noticeably non-ideal (Z ≈ 0,94), and the lesson says the model fails at high pressure — add one sentence saying the result is an estimate here.
- lesson.md:148 / sim.js:111 — the sim is a 2D gas (area plays the role of volume), which does not affect p/p_ref — the note could say "tasomalli: pinta-ala vastaa tilavuutta".
- lesson.md:148 — "keskinäiset törmäykset eivät muuta painetta" holds for the time-averaged pressure — add "keskimäärin".
- sim at N = 20 — the 2 s average swings ±12 % (ratio 0,90–1,12). This is correct statistics and allowed by the spec — the note could mention it.

## Checked
- All 12 answers recomputed independently in one script: all match answers.py and exercises.json, are within 0,5 % of the exact value, and have sig figs that follow the data.
- Worked example: n = 0,2073 mol, m = 0,83 g He, air 6,0 g, molar volume 24,1 l/mol. The figure numbers match. The example and every solution solve symbolically first.
- Side numbers correct: L2-02 (O₂ 1,32 g, CO₂ 1,81 g), L2-04 (23,9 l, 17 %), L3-02 (22 g/16 g), L3-03 (2,64 kg initial; the gauge-pressure reasoning is right), exit ticket 0,601 mol.
- Scope: only pV = nRT, n = m/M, N = nN_A and the combined law, with no cycles. The model's conditions are stated, and T = θ + 273,15 is used consistently.
- Kaava figure: the 2T arrows are √2 longer than the start arrows (14,3 → 20,1 px), consistent with v ∝ √T.
- sim.js: impulse 2m|v⊥| per hit divided by the perimeter gives NkT/A, with P_REF computed from pA = NkT. Changing N rethermalizes to ⟨vx²⟩ = kT/m, and changing T rescales speeds by √(T_new/T_old).
- Playwright ratios measured/predicted (N, T, V%): 100,300,100 → 1,02; 200,300,100 → 0,99; 50,300,100 → 1,02; 100,600,100 → 1,00; 100,150,100 → 1,04; 100,300,50 → 0,99; 100,300,25 → 1,01; 200,600,25 → 16,1 vs 16; 150,450,75 → 0,97.
- Averaged over 10 × 2 s via simAdvance, the mean ratio is 1,002 at the reference state and 1,000 at 200/600 K/25 %. v_rms was 138,6/240,0/339,4 px/s at 100/300/600 K, so v_rms/√T is constant.
- Screenshots at 390 and 1280 px show ratio 1,00–1,01 at the reference state. The reference state and units are labelled, and nothing contradicts the lesson.
