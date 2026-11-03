VERDICT: PASS
CONTENT-HASH: bc699d48d2b345a8

## Blocking

## Polish
- inquiry.json:108 / sim.js:382,480 — the impossible-transfer condition in the code is R I ≥ U (P_h ≥ P); the model box and readout say "suurempi kuin" and the bar label "P_h > P". "vähintään yhtä suuri" would match exactly (trivial).
- lesson.md Ydinajatus / tarkistus-3 model — "magneettikentän, jonka suuruus ja suunta vaihtelevat virran tahdissa" is the school picture (C); keep it from becoming "more load, more flux".
- Exercises: see exercises/review/science.md (no blocking; the round-1 L1-04 item is fixed).

## Checked
- U₁ : U₂ = N₁ : N₂ = I₂ : I₁ with "ideaalinen" and effective values stated; DC case (constant flux, pulse only at switching) right in theory, ennuste-dc and exit ticket.
- P_h = R I² = R P²/U²; warning against U²/R with the right reason (only R I across the line).
- Worked example: N₁ = 1980, I₁ = 81,8 A → 82 A, 9,0 MW both sides.
- Sim: R = 6,0 Ω; 50/100/200/400 kV → 4000/2000/1000/500 A, 96/24/6,0/1,5 MW, 48/12/3,0/0,75 %; 20 kV impossible (R I = 60 kV); koe-1 locks P and l; simState has I, Ph, osuus.
- Kaava graph (12 %, 3,0 %, 0,75 % at 200 MW, 6,0 Ω) matches the sim.
- ennuste-jannite: exactly one correct; U²/R, "puoleen" and "sama" distractor feedback right.
- virhe: 26 667 MW absurd, 1,5 MW, R I = 3,0 kV; siirto 720 kW (2,2 %) and mistakes 1 512 500 / 2,4 / 0,72.
- tarkistus-2 0,261 A, mistakes 5,0 A and 95,8 A; exit ticket 11,5 V and 1 : 9.
- lesson-answers.py output equals my own recomputation.
- Grid voltages 400/220/110 kV, 20 kV, 230 V, > 99 % transformer efficiency, ≈ 2 % grid losses sourced.
