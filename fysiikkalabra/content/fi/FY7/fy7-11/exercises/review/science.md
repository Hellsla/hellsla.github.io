VERDICT: PASS
CONTENT-HASH: 5a4e18b049e83472

## Blocking

## Polish
- solutions.md:173 and :178 (fy7-11-L2-07) — the reading uncertainty "±0,001" is finer than the figure allows: the n-graph grid is 0,005, so half a division is 0,0025, and n at 589 nm (1,5167) cannot be read from it either — write "lukematarkkuus noin ±0,002" (still ≈0,15 % in v) and give 1,5167/1,5143 as "kuvaajan pisteet (valmistajan taulukko)" or drop the fourth decimal.
- solutions.md:187 (fy7-11-L3-04) — "vedellä noin 42,2°" while the table maximum is 42,25° (Sijoitus line 186) — write 42,3° (or keep 42,25°), so the Vastaus matches the Sijoitus and the 42,3° in Järkevyys.
- solutions.md:199 (fy7-11-L3-05) — the last clause lacks a verb ("... ja herkkä pyöristykselle") — "... ja sen suunta on herkkä pyöristykselle". Optional: say that 65,0° is only 0,02° past A_max = 64,98°, which is why 1,0005 is so close to 1.
- exercises.json fy7-11-L1-08 — the plan (docs/exercise-bank/FY7.md, Taso 1) asks for "taitekulma kahdelle värille"; L1-08 is instead a one-step version of L2-04 (θ − h). Not a defect, but either update the plan line or note the swap.
- exercises.json fy7-11-L2-06 vs L3-03 — both compute θ for red and violet with θ = 4β − 2α; the error-analysis framing makes L2-06 distinct enough, but L3-03's level-3 status now rests only on the different α per colour. Consider noting this in the plan.

## Checked
- Recomputed all 20 answers in one script (own formulas): every value matches answers.py and exercises.json; units and tolerances fit.
- L2-05: Δα flint 0,7646°, crown 0,4140°, acrylic 0,4610°; small-angle check Δn/n·tan α₂ ≈ 0,764° correct.
- L2-06: θ_p 42,29°, θ_v 40,63°, turning 137,7°/139,4°; red outer edge reasoning correct.
- L2-07: Cauchy fit of the n-graph gives n(600 nm) = 1,5163, v = 197 854 km/s; answer 197 889 within tolerance; λ in glass 396 nm.
- L3-04: table regenerated with n = 1,3315 and 1,400 (|Δθ| ≤ 0,03°); row n 1,3997–1,4002, mean 1,4000; true maxima 42,30° and 33,25°; "liuoskaari sisäpuolella" correct.
- L3-05: A_max violet 64,977°, red 66,573°; A = 64°: δ_p 56,40°, δ_v 63,82°, Δδ 7,417°; A = 60°: 3,909°; n_v sin α₃ at 65° = 1,0005.
- L1-06: exactly one correct option, distractor feedback correct (frequency unchanged, colours not created by glass).
- L1-07: λ = λ₀ : n = 264,7 nm; L1-08: 42,3° − 30,0° = 12,3°.
- Notation (α₁…α₄, A, δ, θ = 4β − 2α, n(λ), v = c : n) matches the lesson brief; all within FY7 scope.
- Hash checked at start and end: unchanged.
