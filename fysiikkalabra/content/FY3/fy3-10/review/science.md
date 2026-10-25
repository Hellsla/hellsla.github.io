VERDICT: PASS
CONTENT-HASH: 6fa12dee8241e9cf

## Blocking

## Polish
- solutions.md:23 — "18 g, mikä on tavallisen patruunan koko": common automatic-lifejacket cartridges are about 24–38 g, so 18 g is on the small side — say "pienen patruunan koko" or leave the claim out.
- sim.js:66 / lesson.md:148 — moving the piston in leaves the speeds unchanged, so the volume slider is an isothermal (slow, heat-exchanging) change; one clause under the canvas ("lämpötila pysyy samana, kun tilavuutta muutetaan") would stop a student wondering why compression does not heat the gas.
- solutions.md:47 — "poikkeaa ideaalikaasusta selvästi (Z ≈ 0,94)": correct, but Z is not defined in FY3; "noin 6 %" says the same without a new symbol.

## Checked
- All 12 answers recomputed with my own formulas (one script): answers.py, exercises.json and my values agree; every stored answer is within 0,5 % of the exact value (tolerance 2 %).
- Exit ticket: n = 150 kPa · 10,0 l / (8,31 · 300,15 K) = 0,601 mol ✓; ticket 2 and 3 reasoning correct.
- Worked example: n = 0,2073 mol, m = 0,829 g; air 6,01 g; molar volume 24,1 l at 20 °C, 101 kPa ✓; symbolic stage precedes substitution; SVG numbers 0,21 mol · 0,83 g / 6,0 g match.
- Solution checks: L3-03 initial mass 2,64 kg (0,72 kg ≈ 27 %), L3-02 Ar 21,8 g / air 15,8 g, L2-02 O₂ 1,32 g / CO₂ 1,81 g, L2-04 23,9 l at 20 °C (−17 %) ✓; gauge-pressure and combined-law unit arguments correct.
- Formulas, conditions (kelvin, total pressure, validity limits) and scope are FY3; p ∝ NT/V figure correct.
- sim.js physics: 2D kinetic theory p = NkT/A with ⟨vx²⟩ = ⟨vy²⟩ = kT/m, impulse 2m|v⊥| per perimeter, P_REF computed not fitted ✓.
- Playwright, live sliders (8 states incl. N 20/T 100/V 25 → pred 0,267, meas 0,254; N 200/T 600/V 25 → 16,0 vs 16,05): ratio 0,95–1,05 in every state.
- simAdvance, 300 independent 2 s windows at T 300 K, V 100 %: N = 20 mean 1,000, sd 5,5 %, range 0,86–1,16, 8 % of windows outside ±10 %; N = 100 sd 2,5 %; N = 200 sd 1,8 %.
- Note under the canvas (plane model, wall-only collisions, 2 s average, ±10 % at N ≈ 20) matches these measurements.
- Screenshots 390/1280: gauge, bars and level consistent (1,00/1,01).
