VERDICT: PASS
CONTENT-HASH: 6ceba1d590513df3

## Blocking

## Polish
- solutions.md:23 — "18 g, mikä on tavallisen patruunan koko": automatic life-jacket cartridges are usually about 24–38 g of CO₂ (and inflate about 15–25 l) — say "pienen patruunan koko" or drop the comparison.

## Checked
- All 12 exercise answers recomputed independently (one script) and compared with answers.py: all inside tolerance.
- Solutions: symbolic first; gauge-pressure difference in L3-03 correctly cancels p₀ (initial 2,6 kg, >¼ leaked); L2-01 non-ideal remark has the right sign for O₂ near room temperature (Z < 1, ideal value too high); diesel L2-03 (ratio 16,7, 46 bar, ≈ 550 °C) realistic.
- Weighing table: masses are the ideal values for 5,00 l, 101 kPa, 293,15 K (0,2072 mol) within ±0,02 g; m/M 0,2075 / 0,2064 / 0,2076 / 0,2068 mol, R = 8,32 (lesson) and 8,30 (helium); every mistake value matches its stated error.
- Worked example 0,2073 mol, 0,83 g, 24 l/mol, air balloon 6,0 g; Etsi virhe 1,2 → 0,083 mol; siirto 9,12·10⁴ mol, 2,64·10³ kg, mistakes 9870 and 2,64, outside air 3,4·10³ kg, lift ≈ 700 kg; check-2 3,0 (mistakes 2,25, 1,69); exit ticket 0,601 mol.
- Figures: helium/air speed arrows 2,7 : 1 = √(29/4) and equal particle counts; mole-mass bars to scale 4 : 29 : 44; the N, 2N, 2T, V/2 cylinders have 6/12/6/6 particles, √2-longer arrows at 2T and half the gas height at V/2.
- sim.js: 2D kinetic theory is right — impulse 2m|v⊥| per hit per unit perimeter gives p = NkT/A with kT/m = ⟨v²⟩/2, Box–Muller radius gives the 2D Maxwell speeds, exact thermalisation on N change, v ∝ √T; the 2D area-as-volume, no inter-particle collisions and isothermal wall motion are stated in the model box.
- Ran the preview in Playwright with simAdvance, 12 windows of 2 s each: measured/predicted 1,00 ± 0,03 at N = 100, ± 0,06 (range 0,89–1,09) at N = 20 (matches the "±10 %" in calc), 1,00 at (50, 600 K) for the exp-2 target N = 50; the five example table rows (1,05; 2,00; 3,91; 0,98; 5,11) lie inside the observed spread, and their pV/(NT) column is correct.
- Experiments isolate N (T, V locked) in both; exp-2 numeric 50 with mistakes 200 (p = 4,00), 71 (√2) and 25 (p = 0,50) correct. Hash identical at start and end.
