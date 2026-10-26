VERDICT: PASS
CONTENT-HASH: 944c5d51ce0ef7d1

## Blocking

## Polish
- inquiry.json:check-3, second criterion — the argument that a common R means equal n is slightly circular, because R came from the same weighing. It is still correct at FY3 level. Fix (optional): add that "tarkat mittaukset antavat kaikille kaasuille saman R:n".

## Checked
- The 12 exercises, recomputed independently, are within 0,3 % of exercises.json and answers.py. L2-01's "muutamia prosentteja liian suuren paineen" is correct for O₂ at about 180 bar (Z ≈ 0,94).
- Weighing: helium m/M = 0,2075 mol, and the mistakes are 4,82 and 3,32. A student who rounds to 0,21 is 1,2 % off, inside the tolerance. The four values range from 0,2064 to 0,2076 mol, which is under 1 %. The table masses are within ±0,02 g of the exact values. The ratios are 7,25 and 10,96.
- laske-r: 8,302, with mistakes 121,7, 8302 and 0,008302, all right. In Kaava, the mean of 0,2071 gives 8,32 ≈ 8,3.
- pred-n: p doubles, which is correct. The distractors' feedback is sound, and the gate after exp-1 is consistent. pred-1: "yhtä monta" is correct. Its third option's feedback is right: helium hits more often, each hit is weaker.
- Sim checked in Playwright with 10 windows of 2 s each:
  - N100/300 K: p = 1,01, 94 hits/s.
  - N200: p = 1,99, 184 hits/s.
  - N50: p = 0,50.
  - 600 K: p = 2,01.
  - N50/600 K: p = 0,995.
  - 150/450 K/75 %: p = 3,00, which matches check-2.
  
  pPredicted is still in simState. The canvas shows only the measured bar.
- Taulukko: pV/(NT) = 1,05, 1,00, 0,98, 0,98 and 0,99, which matches the "muutaman prosentin" feedback.
- Worked example: n = 0,2073 mol, m = 0,829 g, air 6,01 g, 24,1 l per mole; it works symbolically first.
- virhe: 1,22 vs 0,0829 mol. siirto: 2645 kg (mistakes 9869 and 2,64); outside air is 3367 kg, so "≈700 kg" holds. Exit ticket: 0,601 mol. exp-2: N = 50 (mistakes 71, 4,00 and 0,50).
- check-3 model answer and figures (0,21 mol, 0,83 g, 6,0 g; 2N, 2T, V/2 → 2p) are correct.
