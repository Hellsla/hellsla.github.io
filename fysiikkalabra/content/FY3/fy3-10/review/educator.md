VERDICT: FAIL
CONTENT-HASH: df0bee215a982990

## Blocking
- lesson.md:8 — The lesson never states N = n·N_A, and it calls N_A a unitless "luku". L3-01 (exercises.json:81) gives N_A in 1/mol and needs N = n·N_A, and the sim shows N and pV/(NT). Neither N nor the unit is explained. — In `## Kaava` after line 25, add the display formula `N = n N_A` with N (hiukkasten lukumäärä) and N_A = 6,022 · 10²³ 1/mol named. In line 8, write "Avogadron vakio N_A = 6,022 · 10²³ 1/mol".
- exercises.json:47 (L2-01) — This repeats the worked example (p, V, T → n → m = nM) with new numbers. — Reverse it: "Pullossa on 2,7 kg happea, 10,0 l, 15 °C. Mikä on paine baareina?" (about 202 bar).
- exercises.json:89 (L3-02) — This repeats the example's last paragraph (same n, mass difference). Its reasoning question is answered verbatim in lesson.md:10, :49 and :55, so it is not level 3. — Make it backward: "Argontäytteinen elementti on 5,5 g raskaampi kuin ilmatäytteinen (101 kPa, 20 °C). Kuinka suuri on välitilan tilavuus?" (n = Δm/ΔM, V ≈ 12 l).

## Polish
- lesson.md:3 — The question presupposes its answer. — "**Miksi** heliumpallo on paljon kevyempi kuin samankokoinen ilmapallo? Onko siinä vähemmän kaasua?"
- lesson.md:8 — The mole, N_A and M come in one paragraph. — Add why particles are counted in moles (mooli voi olla tuttu kemiasta), and give M its own paragraph.
- lesson.md:19 — "joule eli Pa·m³" skips a step. — Add "1 Pa · m³ = 1 N/m² · m³ = 1 N · m = 1 J".
- lesson.md:46 — The sanity check is circular (0,21 mol / 5 l). — Compare with the molar volume of about 24 l/mol from chemistry.
- exit-ticket.json:7 — "moolimääränä" is not a glossary term. — Use "ainemääränä".

## Checked
- Lint is clean (not repeated).
- lesson.md:6 matches fy3-9 (the pV, V/T and p/T laws, kelvins).
- Pa = N/m² and ylipaine come from fy3-4, the joule from fy3-2.
- The mole is introduced from scratch; KE1 is not assumed.
- Level 1: five single-formula tasks (solving pV = nRT is the stated skill).
- Level 2: L2-02 to L2-04 fit the rubric.
- Level 3: L3-01 and L3-03 are genuine combination and reasoning tasks.
- The exit ticket tests the core skill, gas-type independence and the model's limits.
- The misconceptions are real (°C, kPa/l, heavier gas has fewer moles).
- meta matches curriculum.json; the hash was unchanged at the start and end.
