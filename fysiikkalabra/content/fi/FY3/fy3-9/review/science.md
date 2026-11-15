VERDICT: PASS
CONTENT-HASH: 7d5645fe39460f43

## Blocking

## Polish
- inquiry.json check-2 solution — "$120\,\text{kPa}$, kaksi merkitsevää numeroa" is ambiguous as written. Use $1{,}2 \cdot 10^2\,\text{kPa}$, or keep 120 and say that the trailing zero is not significant.
- inquiry.json ruisku — `"source": "simulated"`, but the data are invented example values (the `source_note` and the text say so). Use the source kind for example data if one exists.
- inquiry.json kertaus option "$3{,}3 \cdot 10^{8}$ N", and prompts with plain "50 ml", "25 ml", "1,50 litran", "60 ml" — move the numbers and units into LaTeX (typography, not physics).
- lesson.md Ydinajatus — "osuvat seinämiin kaksi kertaa niin usein" means per unit area of the wall. check-1's feedback says so, and the theory could too (C, not blocking).

## Checked
- One script recomputed every number from the task data with my own formulas, and all agree. Worked example: $1{,}036\,\textsf{l}$, +30 %, $pV = 80{,}8$. Misconception: $1{,}04\,\textsf{l}$, 3,5 %. Kertaus: $30\,\text{N}$, $3{,}3 \cdot 10^8$. pred-1: $200\,\text{kPa}$, $5{,}00\,\text{J}$. pred-2: $60{,}2\,\text{ml}$, $0{,}171\,\text{ml/K}$, γ = 1/293. Ruisku: $pV$ column, $168\,\text{kPa}$, +7,7 %. Virhe: 252/40 kPa. Siirto: $1{,}07\,\textsf{l}$, mistakes $2{,}10$ and $0{,}00107$. check-c2: 1,10. check-2: $120\,\text{kPa}$, mistakes 108 and 0,12. Exit ticket: $160\,\text{kPa}$.
- Conditions are stated where the laws are used: fixed amount of gas, constant T, total (not gauge) pressure and ordinary pressures for Boyle's law. The kelvin laws are given for a dilute gas, and the extrapolation is called a model prediction (the gas condenses first).
- Mechanism: at constant T the speed is unchanged and the hit rate doubles (check-1). Heating at constant p makes the piston rise until the hits balance the weight (pred-2 feedback). The pressure of a closed gas is not caused by its weight.
- Units: Pa·m³ = J and kPa·l = J are correct. Mixed units in $p_1V_1 = p_2V_2$ are justified.
- The figures are to scale as their labels claim. In boyle-graphs, $pV = 2000\,\text{kPa·ml}$ at 10–40 ml on both the $(V,p)$ and $(1/V,p)$ panels. In absolute-zero, 253–373 K, ratio 1,474, both lines through the origin.
- sim.js implements $pV/T$ = const from 50 ml, 100 kPa, 293,15 K. The `calc` box discloses that the pressure is computed, not counted. The axes contain every state (72,2 ml and 144 kPa at 150 °C, 250 kPa at 20 ml).
- Experiments: exp-1 locks the mode and Tc and varies Vml. simState `p` is in Pa and `constant` is in J in isothermal mode (kPa·ml ×10⁻³). exp-2 is isobaric and varies Tc; the adapter `get` gives `T`, `Vgas` (ml) and `VperT` (ml/K).
- The exp-2 question is consistent with fy3-8's air γ = 3,4·10⁻³ 1/K at 20 °C.
- Every choice item has exactly one correct option. Distractor feedback is right, including the ruisku leak option (a leak would lower $pV$).
