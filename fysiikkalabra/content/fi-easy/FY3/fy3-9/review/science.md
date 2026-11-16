VERDICT: PASS
CONTENT-HASH: e9f9fa81916b9e73

## Blocking

## Polish
1. inquiry.json:43 — the recap distractor "$3{,}3 \cdot 10^{8}$ N" keeps its unit outside LaTeX (NOTES §1) — write `$3{,}3 \cdot 10^{8}\,\text{N}$`.
2. lesson.md:256 — the aria-label of `boyle-graphs` says "mittauspisteet", but the points are computed from pV = 2000 kPa·ml — "lasketut pisteet" or "mallin arvot".

## Checked
- Polish of round 1 done: every volume with ml in inquiry.json and exit-ticket.json is LaTeX; the number sequence before and after commit 550ec4d13 is the same (exit ticket identical; inquiry differs only in "60, 50," becoming "$60$, $50$,").
- Recomputed in one script with my own formulas: recap 30 N and its mistakes (300 N, 0,030 N, 3,3·10⁸ N); pred-1 200 kPa, pV 5,00 J; pred-2 60,2 ml, V/T 0,171 ml/K, 1,20, 110 ml; γ = 1/293 ≈ 3,4·10⁻³ 1/K; syringe pV 5040/5050/5040/5430/5040, expected 168 kPa, +7,7 %; 1/V 0,020/0,040/0,010; worked example 1,036 → 1,0 l, 80,8 kPa·l, ~30 %; misconception 1,04 l, 3,5 %; Etsi virhe 252,5 ≈ 250 vs 40 kPa; siirto 1,0693 → 1,07 l, mistakes 2,10 and 1,07·10⁻³, 71 %, 108 kPa·l; check-c2 1,0999, 28/280 ≈ 0,10; check-2 120 kPa, mistakes 108 and 0,12; exit ticket 160 kPa; lesson-answers.py agrees.
- Exactly one correct option in every choice; each distractor is really wrong and its feedback gives the right reason (leak lowers pV, heating raises it; Celsius ratio; no harder hits at constant T).
- Boyle's law with its conditions (fixed amount, constant T, total pressure, ordinary p and T); V ∝ T and p ∝ T for a closed dilute gas in kelvins; extension to 0 K flagged as a model prediction.
- Mechanisms: halved volume → twice the hit rate at the same speed; heated gas under a loaded piston expands until the thinner gas balances the weight; fast compression warms the air.
- Figures to scale from figures.py: p = 2000/V points and line slope 2000 kPa·ml; V/T and p/T lines through the origin (253–373 K); micro model 2 : 1.
- sim.js: pV/T = const in three modes, speed ∝ √T; boxes say the pressure is computed, values are model values.
- exp-1: isothermal, θ locked, V varied; simState p (Pa) and constant (pV in J). exp-2: isobaric locked, θ varied; adapter gives T, Vgas (ml), VperT (ml/K).
- Scope: FY3 changes of state, Boyle's law; nothing from FY4.
- Hash the same at start and end.
