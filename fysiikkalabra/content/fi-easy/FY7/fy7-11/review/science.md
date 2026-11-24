VERDICT: PASS
CONTENT-HASH: 1c23c153f54b8069

## Blocking


## Polish
- lesson.md:199 — theta-graph aria-label says "punaisen valon (n = 1,332)" while the text and the plotted curve use $n = 1{,}3315$ (the peak at 42,3° belongs to 1,3315; 1,332 gives 42,2°) — write "n = 1,3315".
- inquiry.json:370 (tarkistus-2 solution) — the three figures are justified by $c = 3{,}00 \cdot 10^8$ m/s, but the real limit of a difference of near-equal speeds is $n_\text{v} - n_\text{p} = 0{,}0116$ (three figures) — name that as the reason.
- lesson.md:116–123 — water indices 1,3315 / 1,3334 / 1,3375 / 1,3431 run about 0,0004 above the usual 20 °C values (1,3311 / 1,3330 / 1,3371 / 1,3428); check them against the cited Daimon & Masumura table (rainbow angle changes by < 0,1°, no conclusion changes).
- inquiry.json:80 — the pending text names "Teoriatiivistelmän"; the stage is now *Teoria* (pedagogy/visual to confirm).

## Checked
- One script recomputed every number of lesson, inquiry and exit ticket with my own formulas: crown-glass speeds 198 111 / 196 053 km/s; worked example 34,88° / 34,47° / 0,41°; rainbow extremes by brute-force max of $4\beta - 2\alpha$: 42,30° at α = 59,5° (red), 40,63° (violet), θ(90°) = 14,7°; secondary 50,5° / 53,5°; siirto 25,40 mm, mistakes 11,23 mm, 0,0254 m, 3464 mm; tarkistus-2 1946 km/s, mistake 2000 lies outside the 2 % tolerance; virhe 39,2° and 91,8°; exit −7,7°. All match lesson-answers.py.
- Prism δ(A) at α₁ = 50°: 0,53 / 0,70 / 0,94 / 1,40 / 4,45° spread; koe-2 minimum 38,43° near 49°, 40,0° at 40°, 50,3° at 80°; flint 3,92°, water 0,85° (F2 Cauchy fit reproduces SCHOTT nC, nd, nF).
- sim.js re-implemented in Python: Cauchy coefficients give the table values (1,5143/1,5302, 1,3315/1,3431); deviation sign positive; koe-1/koe-2 readouts equal my δ; no ray reaches the base for any slider setting; simState carries dP, dV, dd; experiments lock a1/aine or A/aine and vary only the named parameter.
- Derivations: α₂ + α₃ = A, δ = α₁ + α₄ − A, total turn 180° + 2α − 4β → θ = 4β − 2α correct; conditions (exit possible, air n ≈ 1) stated.
- Figures: n(λ) graph points and axes to scale; θ-graph peak (59,4°, 42,3°) to scale; drop, observer (upper drop red/violet passes above eye, lower drop red hits ground) and prism-angle diagrams physically right.
- Causality: dispersion from electron response rising toward UV absorption (normal dispersion, fair C); secondary bow dimmer through partial exit at each reflection; Alexander's band explanation correct.
- Assessment: each choice has exactly one correct option; distractor feedback correct; model answers and criteria match theory; exit ticket consistent with "Sun below 42°".
- Scope: refraction/dispersion within FY7 central contents and slot täsmennys.
