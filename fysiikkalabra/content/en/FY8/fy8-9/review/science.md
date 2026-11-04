VERDICT: PASS
CONTENT-HASH: 7885fb7bfb318f8e

## Blocking

## Polish
- inquiry.json:tarkistus-3 criteria — "in a year hundreds of half-lives pass" contradicts the model answer's ≈1460 (8766 h / 6.01 h = 1459); "over a thousand half-lives".
- inquiry.json:tarkistus-3 model — "the activity has dropped to zero" → "practically to zero" (it never reaches exactly zero, as the Formula figure says) (C).
- inquiry.json:kertaus correct feedback — "Today we find out *when*…" → "In this chapter…".
- lessons/FY8/fy8-9/lesson-answers.py "ex-factor" comment says 0,17750; the computed value and the lesson's 0.17754 agree (comment only).

## Checked
- One script recomputed: Tc-99m λ = 3.20e-5 1/s (32 per million per s); worked example 550 MBq · 0.5^2.4938 = 97.65 → 97.6 MBq; virhe 4.33e10 vs 6.24e10 (≈31 % low); tarkistus-3 ratio ≈ 43 900, Cs 97.7 % left; exit ticket 1/8.
- Independent least-squares fit of the English Pa-234m table: C = 0.010127 1/s, A = 376.6, B = 5.54, T½ = 68.45 s; 1/C = 98.7 s and no-B fit 71.8 s match the mistakes.
- Ba-137m fit C = 0.004564 → 151.9 s, −0.8 % from 153.1 s.
- Sim model values (mulberry32, seed 1000·series+42) reproduced: 1600/792/399/208; 20-nuclei series 7, 12, 13, 7, 10; 1600-nuclei 0.489–0.509 — every prediction's feedback quotes them correctly.
- Exactly one correct option in every choice item; distractor feedback (linear decay, memoryless nucleus, independence of neighbours) physically right.
- Half-life table matches NNDC values to three figures; tarkistus-2 graph (720 kBq, T½ = 5.0 h, 45 kBq at 20 h) consistent.
- Decay law, λ = ln 2/T½, A = λN, mass ∝ N, background term B and its conditions stated where used; model limits in the sim boxes stated.
- Translation changes no physics versus the passed Finnish source; sim labels translated at runtime.
