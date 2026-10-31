VERDICT: PASS
CONTENT-HASH: 47b36b1d0f3d0d64

## Blocking

## Polish
- lesson.md:492 — "Suurin voima on aina keskimääräistä suurempi" leaves out the case it fails: a constant force has a peak equal to its mean. — Say "Kun voima muuttuu, suurin voima on keskimääräistä suurempi" if you touch the line.

## Checked
- Round-4 blocker fixed: inquiry.json:104 now says the crushable pulse rises smoothly to its peak half-way, is sine-shaped, and has a mean of about 0,64 F_max, not half. That matches 2/π = 0,6366, the calc box formula, the sim's curve and lesson-answers Fka (50,9/25,5/12,7 N). The en and fi-easy boxes say the same.
- model.js:53 timing fix: the contact step now adds exactly dt. Final t equals (XB−XS)/v1 + Δt to 6 digits in 7 crushable runs (e.g. 0,479270 s for the hard bumper; it was 0,47937 before). Δt, I and the readout are unchanged.
- The model.js:7 and :71 comments and the calc/sim-spec clause ("muovautuvan suoraan annetusta pulssista") are now correct.
- Node model test passes (652 checks). Energy E_k + E_b = ½ m v1² holds with zero error through a crushable run.
- My script reproduces exp-1 (0,0393/0,0785/0,157 s; 80,0/40,0/20,0 N; −2,00 N·s), exp-2 (−2,00/−4,00 N·s; v = −2,00 m/s), exp-3 (28,3/40,0/56,6 N; −1/−2/−4 N·s) and I = Δp in every run.
- Limits: the largest crush is 0,222 m (crushable) and 0,283 m (spring), both under 0,32 m. The longest contact is 0,444 s, inside the 0,5 s axis. The largest force is 113 N, under 120 N.
- I recomputed the worked example (3,48 kg·m/s, 870 N, weight ratio about 1500, sign-error 145 N), siirto (80 N; distractors 4,0/0,20/800; stiff hand 400 N, about 8 kg), check-2 (5,4 N·s, 12 m/s, 43 km/h, mean 450 N = half the peak of the triangle; distractors 24/5,4/12 000), kertaus 1,5 m/s, virhe −4,0 kg·m/s and check-1 ±120.
- Every prediction and experiment question has exactly one correct option, and each distractor's feedback is right. The Johtopäätös "neljäsosa voimasta" holds.
- Experiment setups lock m, v1 and the collision type or the bumper as intended. simState gives dt, Fmax, I, v2, dp and p1.
- Theory, summary, opening answer (surface force = net force + weight) and exit ticket agree.
