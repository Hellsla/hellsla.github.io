VERDICT: PASS
CONTENT-HASH: f6a09b81393c1325

## Blocking

## Polish
- inquiry.json kertaus option "$3{,}3 \cdot 10^{8}$ N", and the siirto prompt "1,50 litran": the unit is still outside LaTeX. Fix: `$3{,}3 \cdot 10^{8}\,\text{N}$` and `$1{,}50\,\textsf{l}$:n`.
- inquiry.json check-2 solution: "$120\,\text{kPa}$, kaksi merkitsevää numeroa" is ambiguous as written. Fix: write $1{,}2 \cdot 10^2\,\text{kPa}$, or say that the trailing zero is not significant.
- inquiry.json ruisku: `"source": "simulated"` is on invented example values (its `source_note` says so). Fix: use the source kind for example data, if there is one.
- lesson.md Ydinajatus: "osuvat seinämiin kaksi kertaa niin usein" means per unit area of the wall. check-1's feedback says this, and the theory could too. (C, not an error).

## Checked
- The ml-to-LaTeX change keeps every volume's number and unit in inquiry.json and exit-ticket.json; the physics is unchanged.
- One script recomputed every number with my own formulas, and all agree: worked example 1,036 l (+29 %, pV 80,8), misconception 1,04 l, kertaus 30 N, pred-1 200 kPa / 5,00 J, pred-2 60,2 ml / 0,171 ml/K / γ = 1/293, ruisku pV column and 168 kPa (+7,7 %), virhe 250/40 kPa, siirto 1,07 l (mistakes 2,10, 0,00107), check-c2 1,10, check-2 120 kPa (mistakes 108, 0,12), exit ticket 160 kPa.
- Conditions are stated where each law is used: Boyle needs a fixed amount, constant T and total pressure; the kelvin laws need a dilute gas, and the extrapolation is called a model prediction.
- Mechanism: at constant T the particle speed is unchanged and the hit rate doubles; under isobaric heating the piston rises until the hits balance the weight; a closed gas's pressure is not its weight.
- Units: Pa·m³ = J and kPa·l = J are correct.
- The figures are to scale: boyle-graphs has pV = 2000 kPa·ml on both panels; absolute-zero has points at 253–373 K and lines through the origin.
- sim.js implements pV/T = const from 50 ml, 100 kPa, 293,15 K. The `calc` box says the pressure is computed. The flash cue's rate × size ∝ T/V follows p in every mode.
- exp-1 locks mode and Tc and varies Vml; `p` is in Pa and `constant` in J. exp-2 is isobaric, and `T`, `Vgas` and `VperT` show in the capture.
- Every choice item has exactly one correct option, and the distractor feedback is right (a leak would lower pV).
