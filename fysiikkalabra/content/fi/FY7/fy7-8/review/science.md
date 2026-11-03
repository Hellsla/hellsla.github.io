VERDICT: PASS
CONTENT-HASH: aa93c04b647589b2

## Blocking

## Polish
- lesson.md:92 and inquiry.json:312 (tarkistus-3 model) — "ensiökäämin vaihtovirta synnyttää … magneettikentän, jonka suuruus ja suunta vaihtelevat virran tahdissa" is the usual school picture (C); under load the core flux is set by the primary voltage and the load currents' fields cancel. No change needed at this level; keep it from growing into "more load, more flux".
- inquiry.json:108 / sim.js header — the impossible-transfer condition is R I ≥ U, i.e. P_h ≥ P; the sim's readout says "häviö olisi suurempi kuin lähetetty teho". "vähintään yhtä suuri" would match the code exactly (trivial).
- Exercises: see exercises/review/science.md (one blocking item there, in a solution's reasonableness check; nothing in the lesson).

## Checked
- U₁ : U₂ = N₁ : N₂ = I₂ : I₁ with "ideaalinen" and effective values stated; DC case (constant flux, pulse only at switching) right in theory, ennuste-dc and exit ticket.
- P_h = R I² = R P²/U²; warning against U²/R with the reason (only R I across the line) right; R P²/U² is also exact for balanced three-phase with R per phase, so the two-conductor model note is fair.
- Worked example: N₁ = 1980, I₁ = 81,8 A → 82 A, power check 9,0 MW both sides.
- Sim: R = 0,040 Ω/km · l = 6,0 Ω; recomputed 50/100/200/400 kV → 4000/2000/1000/500 A, 96/24/6,0/1,5 MW, 48/12/3,0/0,75 %; 20 kV impossible (R I = 60 kV); simState has I, Ph, osuus; koe-1 locks P and l.
- Kaava graph (12 %, 3,0 %, 0,75 %) to scale and matching the sim.
- ennuste-jannite: exactly one correct option; the U²/R and "same power" distractor feedback right.
- virhe: 26 667 MW absurd, 1,5 MW right, R I = 3,0 kV; siirto 720 kW and its three mistake values (1 512 500 kW, 2,4, 0,72) recomputed.
- tarkistus-2 0,261 A, mistakes 5,0 A and 95,8 A.
- Grid voltages 400/220/110 kV, 20 kV distribution, 230 V, transformer efficiency > 99 %, grid losses ≈ 2 % plausible and sourced.
- Transformer figure: primary more turns (step-down), flux loop in the closed core.
