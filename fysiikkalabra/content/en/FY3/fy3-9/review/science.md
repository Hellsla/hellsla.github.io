VERDICT: PASS
CONTENT-HASH: d8a19b348ef5b4a9

## Blocking

## Polish
1. inquiry.json:43 — the recap distractor "$3.3 \cdot 10^{8}$ N" keeps its unit outside LaTeX (NOTES §1) — write `$3.3 \cdot 10^{8}\,\text{N}$`.
2. lesson.md:256 — the aria-label of `boyle-graphs` still calls the points "measurement points", but they are computed from pV = 2000 kPa·ml — "calculated points" or "model values".

## Checked
- The ml-to-LaTeX change (commit 550ec4d13): every volume with ml in inquiry.json and exit-ticket.json is LaTeX; the number sequence before and after is the same (exit ticket identical; inquiry differs only in "60, 50," becoming "$60$, $50$,").
- Against fi-easy: per activity the same numbers, the same correct option, answer, tolerance, mistakes, initial state, locked and varied parameters, measured keys and reveal.
- Recomputed in one script with my own formulas: recap 30 N (and 300 N, 0.030 N, 3.3·10⁸ N); pred-1 200 kPa, 5.00 J; pred-2 60.2 ml, 0.171 ml/K, 1.20, 110 ml; γ = 1/293 ≈ 3.4·10⁻³ 1/K; syringe pV column, 168 kPa, +7.7 %; 1/V column; worked example 1.036 → 1.0 l, 80.8 kPa·l; misconception 1.04 l, 3.5 %; Find the error 252.5 ≈ 250 vs 40 kPa; transfer 1.07 l, mistakes 2.10 and 1.07·10⁻³; check-c2 1.10; check-2 120 kPa, mistakes 108, 0.12; exit ticket 160 kPa; lesson-answers.py agrees.
- Exactly one correct option in every choice; every distractor's feedback names the right reason.
- Boyle's law with its conditions; V ∝ T and p ∝ T for a closed dilute gas in kelvins; the extension to 0 K is a model prediction (real gas condenses).
- Mechanisms: hit rate, loaded piston balance, compression heating, leak lowering pV.
- Figures to scale from figures.py (p = 2000/V; V/T, p/T through the origin; micro model 2 : 1).
- sim.js implements pV/T = const in the three modes, speed ∝ √T; boxes say the values are model values. exp-1 and exp-2 isolate V and θ; simState/adapter give p, constant (J), T, Vgas, VperT.
- Scope: FY3 central contents only.
- Hash the same at start and end.
