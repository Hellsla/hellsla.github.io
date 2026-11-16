VERDICT: PASS
CONTENT-HASH: 17e2a10800bbe32f

## Blocking

## Polish
- inquiry.json:62,71,75 — pred-n feedback says "In measurements the pressure …"; these are the simulation's wall-hit measurements — "In the simulation's measurements" keeps model values and real data apart, as the conclusion's model answer does.

## Checked
- Recomputed in one script with my own formulas: weighing masses = pV M/(RT) with 0.2072 mol within ±0.02 g (He 0.829, N₂ 5.80, air 6.01, CO₂ 9.12 g), m/M 0.2075/0.2064/0.2076/0.2068 mol, mean 0.2071, R = 8.32 → 8.3; helium-row R 8.302 and its mistakes 121.7, 8302, 0.008302; worked example 0.2073 mol → 0.21 mol, 0.83 g, air 6.0 g, molar volume 24 l; Find the error 1.2 vs 0.083 mol; hot-air balloon 2645 kg (mistakes 9870, 2.64; 1.2 kg/m³ check 3360 kg); check 2 (1.07), check 3 (3.0; mistakes 2.25, 1.69); exp-2 N = 50 (mistakes 71, 200 → 4.00, 25 → 0.50); table pV/(NT) 1.05/1.00/0.98/0.98/0.99; exit ticket 0.601 mol. All agree.
- Ideal gas model stated with its limits (point particles, no interaction energy, fails at high p and low T); p is absolute; T in kelvins; Avogadro's result tied to equal p, V, T.
- Mechanisms: more particles → more hits; higher T → more often and harder; smaller V → more often; light helium particles hit more often but more weakly (momentum ∝ √m at equal T).
- sim.js: 2D box, elastic wall hits, impulse 2m|v⊥| per unit perimeter; derivation gives p = NkT/A = P_REF scale; v ∝ √T, volume change keeps speeds (isothermal, stated in the model box).
- Ran the sim in the browser (simAdvance, 8 × 2 s): (100,300,100) 1.01; (200,300,100) 2.02; (50,600,100) 1.00; (100,600,100) 2.00; (150,450,75) 3.00; (180,300,35) 5.17 vs 5.14; N = 20 spread ±13 % (sd 6 %), matching "about ±10 %".
- exp-1 and exp-2 lock T and V and vary N (slider 20–200, step 10; T up to 600 K); simState has `pMeasured` and `hitRate`.
- Figures: speed arrows He : air 2.7 : 1 = √(29/4); 2T arrows ≈ √2 longer; mole-masses bars 4 : 29 : 44; V/2 cylinder half height.
- Every choice has exactly one correct option, distractor feedback right.
- Scope: equation of state, amount of substance and molar mass are FY3 central contents.
