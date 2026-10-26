VERDICT: PASS
CONTENT-HASH: 227a1ba145001404

## Blocking

## Polish
- sim.js:1062 — the lattice particles vibrate symmetrically (sin) about mean positions whose spacing is imposed as 1 + EαΔT, so the sim shows Cem's picture (symmetric swing) with the expansion added by hand; the asymmetry the lesson and Bea's feedback rely on is not modelled — say in the sim's model note that the spacing is set from the formula and the vibration is drawn symmetric, or skew the swing outward.
- lesson.md:116 (figure particles) — the amplitude arrows are symmetric about each particle; an outward-longer arrow pair would match "heilahtaa kauemmas naapuristaan kuin lähemmäs".
- lesson.md:187 — "muutamia kymmeniä kelvinejä" as the range of validity, while L1-03, L3-01 and the sim use ΔT = 100 K; for metals α is near-constant over 100 K, so say "metalleilla vielä noin sata kelviniä" or similar.
- inquiry.json olomuodot — the correct option attributes the gas's large expansion to weak bonds; for a gas at constant pressure the cause is V ∝ T (ideal gas, next chapter), not weaker bonding — a half-sentence pointer to *Kaasujen tilanmuutokset* would keep it honest.

## Checked
- All 12 answers recomputed from task text: answers.py and exercises.json agree within tolerance (L3-03 457 → 460 cm³, L2-01 52,08 → 52 m).
- Worked example: 0,0864 m, 0,072 %; symbolic first; units shown.
- Predictions/feedback: 6,00 mm / 12,0 mm, 0,0600 %; every correct option right, wrong-option feedback physically sound.
- olomuodot table 0,36 / 2,1 / 11 / 34 cm³; virhe 27,9 mm vs 1,84 mm, factor 15; siirto 44 mm, mistakes 0,044 and 110, glass-corrected 42,9 mm, ratio 41.
- check-2: 23·10⁻⁶ 1/K, mistakes 46 and 15,3; check-3 air/steel ≈ 94; exit ticket 21 mm.
- Coefficient tables (α: 12, 23, 17, 9, 3,3; γ: 0,21, 1,1, 0,95, 3,4 ·10⁻³) realistic at 20 °C; L1-04 remark on water's growing γ true (real ≈ 0,90 l).
- solutions.md: rail-gap reasoning, bimetal bends toward steel, shrink-fit hole grows — all correct.
- Figures: rod, flask and particle figures labelled exaggerated; ΔL, ΔV, d > d₀ consistent; heading names both laws.
- sim.js: ΔL = αL₀ΔT from 20 °C, amplitude ∝ √T, ×100 stated, "under 0,3 %" true (max 0,23 %); chartRange always returns.
- Experiments isolate T (exp-1) and L₀ (exp-2); simState carries dT, dL, rel.
