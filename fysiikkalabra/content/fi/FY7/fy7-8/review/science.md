VERDICT: PASS
CONTENT-HASH: 072bc679bb45dcdc

## Blocking
- none

## Polish
- lesson.md:199 — photo caption writes the loss as $P = RI^2$, elsewhere $P_\text{h}$ — write $P_\text{h} = RI^2$.
- lesson.md:356 — summary "Kaksinkertainen siirtojännite pienentää häviöt neljäsosaan" drops the condition "sama teho, sama johto" stated in Kaava — add it.
- lesson.md:344 — the rounding reason cites $20\,\text{kV}$ as two significant figures; under NOTES §2 a nominal 20 kV is ambiguous — say the distribution voltage 20 kV is a nominal value read with two figures, or give 81,8 A.

## Checked
- Recomputed (own script, = lesson-answers.py): worked example N1 = 1980, I1 = 81,8 A → 82 A, both sides 9,0 MW; sim/koe-1 at 150 km (R = 6,0 Ω), 200 MW: 50/100/200/400 kV → I 4000/2000/1000/500 A, P_h 96/24/6,0/1,5 MW, 48/12/3,0/0,75 %; virhe 2,67·10^10 W vs 1,5 MW, RI = 3,0 kV; siirto 300 A, 720 kW (2,2 %), mistakes 1 512 500 / 2,4 / 0,72; tarkistus-2 0,261 A, mistakes 5,0 and 95,8 A; exit 11,5 V and 1/9. All agree.
- Loss graph to scale: x 0–400 kV at 96–470 px, y 0–25 % at 290–60 px; points (100 kV, 12 %), (200 kV, 3,0 %), (400 kV, 0,75 %) and curve start (70 kV, 24,5 %) sit exactly on R P/U².
- sim.js implements I = P/U, P_h = R I², R = 0,040 Ω/km · l, N2:N1 = U/20 kV; "mahdoton" when RI ≥ U is exactly P_h ≥ P in the two-wire model; simState gives I, Ph (MW), osuus (%) for koe-1; P and l locked isolate U; 50–400 kV reachable with the 10 kV step.; limits stated in Mallin oletukset.
- Transformer mechanism (changing flux through every turn, U ∝ N, DC gives only a switching pulse), power conservation for an ideal transformer, real losses (winding resistance, eddy currents, laminated core), U²/R misconception and its correction (RI is the drop across the line), three-phase note (√3 U I cos φ, 400 kV line voltage, 400/230 V low voltage): correct, conditions stated.
- Predictions: exactly one correct option each (0 V; a quarter); each distractor wrong and its feedback right. check-1, virhe: one correct option, feedback right. explain model answers and criteria agree with the theory. Energy wording follows P1 (sisäenergia, lämpönä ympäristöön).
- Hash identical at start and end.
