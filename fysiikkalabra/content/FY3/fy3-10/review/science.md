VERDICT: PASS
CONTENT-HASH: 77f93e9fe50a5b6d

## Blocking

## Polish
- inquiry.json:pred-1, third option feedback: "kevyt hiukkanen painaa seinää osumassa heikommin, ja nämä kumoavat toisensa". The mechanism is easier to follow if both factors are named: a light particle hits more often (it is faster), and each hit carries less momentum (m·v ∝ √m at equal T). Fix: name "osuu useammin" explicitly before "painaa heikommin".
- solutions.md fy3-10-L2-01: the "noin 6 %" real-gas correction for O₂ at about 180 bar is plausible (Z ≈ 0,94) but has no source. Fix: soften it to "muutamia prosentteja" or keep it as is.

## Checked
- All 12 exercise answers recomputed independently, matching answers.py and exercises.json within 0,3 % (each within tolerance). The Järkevyys numbers in the solutions also check out: 0,32 kg, 9,0 l, 51 °C, 1,32/1,81 g, 23,9 l and −17 %, 0,55 mol with 22/16 g, 2,6 kg with 27 % leaked.
- Weighing table: the exact masses with R = 8,314 are 0,829/5,80/6,01/9,12 g, and the table values are within ±0,02 g of them. m/M = 0,2075/0,2064/0,2076/0,2068 mol, mean 0,2071, R = 8,32 ≈ 8,3. The ratios 7,25 (≈7) and 10,96 (≈11) are correct.
- Worked example: n = 0,2073 mol, m = 0,829 g, molar volume 24,1 l. The solution is symbolic first.
- inq-* values in answers.py: koe2-N = 50, the mistake values 71, 200 (→4,00) and 25 (→0,50) are consistent, and check-2 = 3,0 with mistakes 2,25 and 1,69. Exit ticket: 0,601 mol.
- virhe: 1,2 mol (wrong) and 0,0829 mol (right). siirto: 2645 kg (answer 2640), Celsius mistake 9870, kPa mistake 2,64, outside air 3,37·10³ kg so the "noin 700 kg" lift is right.
- sim.js physics: per-perimeter impulse rate = NkT/A with kT = m⟨vₓ²⟩ = KT300 is consistent. P_REF is computed, not fitted. Thermalisation after a change in N and the √T rescale are correct. The model hit rate is 0,920 per particle per second → 92/s at N = 100.
- Sim measured with Playwright, 15 two-second windows each: N = 100, 300 K: hits 93 (86–99), p 0,96–1,05. N = 100, 600 K: hits 132, p 1,94–2,10. N = 50, 600 K: hits 68, p 0,94–1,04. N = 40 and 60 give 0,81 and 1,18, so N = 50 is clearly identifiable. This supports the pred-2 feedback (≈1,4× hits, 2× pressure), the exp-2 solution (≈65 hits) and the numeric answer.
- Taulukko rows reproduced by the sim: 4,04 (pred. 4), 1,03 (pred. 1), 5,16 (pred. 5,14). Their pV/(NT) ≈ 1 matches the table.
- Experiments: exp-1 and exp-2 lock T and V and vary only N. The initial values are within the slider ranges (T max 600, N step 10 reaches 50). The measured keys hitRate, pMeasured and pPredicted exist in simState.
- Figures: the Ydinajatus balloons (0,21 mol, 0,83 g and 6,0 g; helium arrows longer) and the Kaava cylinders (2N, 2T, V/2 → 2p) are correct. The check-1 and check-3 model answers are correct kinetic theory.
