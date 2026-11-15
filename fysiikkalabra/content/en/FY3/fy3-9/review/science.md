VERDICT: PASS
CONTENT-HASH: 3ccad76c26d15915

## Blocking

## Polish
- lesson.md:256 — the aria-label of `boyle-graphs` calls the points "measurements", but they are computed from pV = 2000 kPa·ml — say "model values" (or "calculated points").

## Checked
- Recomputed in one script (68 values): recap force (30 N and its three mistakes), pred-1 (200 kPa, pV = 5.00 J), pred-2 (60.2 ml, V/T = 0.171 ml/K, γ = 1/293 K⁻¹), syringe pV column (5040; 30 ml row 5430, expected 168 kPa), worked example (1.036 l → 1.0 l, pV 80.8 kPa·l), misconception (1.04 l, 3.5 %), Find the error (250 vs 40 kPa), transfer (1.07 l; mistakes 2.10 l and 1.07·10⁻³ m³), checks (1.10, 120 kPa; mistakes 108, 0.12), exit ticket 160 kPa, lesson-answers.py: all agree.
- Boyle's law stated with its conditions (fixed amount, isothermal, total not gauge pressure, ordinary p and T); V ∝ T and p ∝ T for a closed dilute gas in kelvins; the extrapolation to 0 K flagged as a model prediction (real gas condenses).
- Mechanisms: halved volume → twice as many hits at the same speed; heating at constant p → faster, harder hits push the loaded piston up until the thinner gas balances the weight; fast compression warms the air (syringe row), leak would lower pV.
- Every prediction, choice and check: exactly one correct option, each distractor's feedback names the right reason.
- Figures to scale: `boyle-graphs` (pixel values 201/135/100/67/51 kPa vs 200/133/100/67/50; lower line slope 2000 kPa·ml), `absolute-zero` (V/T and p/T constant to 0.3 %, extension to 0 K = −273 °C), `micro-boyle` heights 2 : 1 with 4 vs 8 hit marks.
- sim.js implements pV/T = const in the three modes (p = p₀V₀/V, V = V₀T/T₀, p = p₀T/T₀), particle speed ∝ √T, flash rate ∝ √T/V; its boxes say the pressure is computed from the law, not measured.
- exp-1: isothermal, θ locked at 20 °C, V varied (slider 20–100 ml, step 1 reaches 25 ml); simState `p` (Pa) and `constant` (pV in J, 100 kPa·50 ml → 5.00 J) match the column labels.
- exp-2: isobaric mode locked, θ varied −50…150 °C; adapter gives `T`, `Vgas` (ml), `VperT` (ml/K); axis ranges hold the extremes (72.2 ml, 144 kPa, 250 kPa).
- Scope: changes of state and Boyle's law are FY3 central contents; nothing from FY4.
- Conclusion and check-4 model answers agree with the theory; syringe data labelled invented.
