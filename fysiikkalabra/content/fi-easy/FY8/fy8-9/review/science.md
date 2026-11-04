VERDICT: PASS
CONTENT-HASH: 7bf9de3c30e2ec2f

## Blocking

## Polish
- lesson.md (half-life table) — jodi-131 $8{,}02\,\text{d}$ is said to be NuDat 3 rounded to three figures; the current ENSDF value 8,0252 d rounds to 8,03 d (8,02 d is the older 8,0207 d). Kept from the passed source and used consistently in every task (C) — optionally reword the source note or keep 8,02 as "pyöristetty" textbook value.

## Checked
- All numbers in lesson.md, inquiry.json, exit-ticket.json and meta.json match the passed Finnish source token for token; the translation keeps every condition (large sample, no daughter regrowth, constant background, memorylessness).
- Recomputed: Tc-99m λ = 3,20·10⁻⁵ 1/s (≈ 32 per million per second), Ba-137m fit 0,6931/0,004564 = 152 s vs 153 s, I-131 example 97,65 → 97,6 MBq, Etsi virhe 4,33·10¹⁰ vs 6,24·10¹⁰ (−31 %), tarkistus-3 ratio ≈ 43 900, 1459 half-lives, Cs left 97,7 %.
- Pa-234m fit redone (least squares, own code): C = 0,010127 1/s, A = 376,6, B = 5,54, T½ = 68,45 s; mistakes 1/C = 98,7 s and no-B fit 71,8 s reproduce.
- Predictions 1–2, tarkistus-1: exactly one correct option, distractor feedback correct; model values 1600/792/399/208 and 7–13 of 20 consistent with sim-spec.
- Experiments lock N0, T and series and vary only t or series; measured keys N, frac exist in simState.
- Simulation is the shared course sim (passed with the source): exponential lifetimes give constant hazard ln 2/T½; limits stated in the model box.
- meta.json key_concepts (hajoamislaki, puoliintumisaika, aktiivisuus, hajoamisvakio) correct and consistent with glossary and theory.
- Exit ticket: (1/2)³ = 12,5 %; background term B explanation correct.
