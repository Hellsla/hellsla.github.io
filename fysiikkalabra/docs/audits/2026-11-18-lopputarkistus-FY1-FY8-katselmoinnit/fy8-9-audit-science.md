VERDICT: PASS
CONTENT-HASH: 63c6cf4b2739bc04

## Blocking

## Polish
- lesson.md:453 — "laskee pulsseja niistä säteilykvanteista" — the detected radiation includes alpha and beta particles, not only quanta (Minor, C-level wording) — "niistä säteilyn hiukkasista ja kvanteista".
- lesson.md:643 — the substitution ends "≈ 97,65 MBq" and the answer is 97,6 MBq; that looks like a double rounding (97,65 → 97,7?) although the true value is 97,648 (Minor) — write "≈ 97,648 MBq" or "≈ 97,6 MBq".
- lesson.md:450 (Geiger caption) — "pulssitaajuus on verrannollinen lähteen aktiivisuuteen" leaves out the background that the next paragraph adds (Minor, consistency) — "taustan vähentämisen jälkeen".

## Checked
- One script: I recomputed every lesson-answers.py number with my own formulas. Worked example 550·0,5^(20,0/8,02) = 97,648 MBq; Tc-99m λ = 3,204·10⁻⁵ 1/s (32 per million per s); the Etsi virhe values 4,33·10¹⁰ / 6,24·10¹⁰ (30,7 % ≈ 31 %); tarkistus-3: ratio 43 900, 1459 half-lives per year, Cs 97,7 % left; hook 370/185 MBq; exit 1/8.
- Sovitus: I fitted A e^(−Ct)+B to the printed table with my own least squares: C = 0,010127 1/s, T½ = 68,45 s; 1/C = 98,7; the fit without B gives 71,8 s. Answer, mistakes and exit ticket agree.
- Koe 1–3 values (1600/792/399/208; 7,12,13,7,10; 0,489–0,509) match the generator sim.js uses; each setup locks three parameters and varies one; simState gives N and frac.
- Figure ydin: 100 → 52 → 28 filled, and no nucleus comes back to life between the panels. Kuvaaja, sovitus (Ba points 249…10, B 4,77), pa-points and aktiivisuus (720 kBq, 5,0 h) are drawn from the stated functions and data.
- The half-lives in the table agree with NNDC NuDat.
- Definitions agree with the glossary; memorylessness is the same in the theory, the misconception, tarkistus-1 and the sim boxes.
- Predictions: each has exactly one correct option, and every distractor's feedback is right. Kertaus: β⁻ I-131 → Xe-131.
- The sim implements an exponential lifetime τ = −T½/ln2·ln u. Its model box names the stable daughter, the missing background and the model values.
- The simulated data carry their source; the fitting text uses the guardrail sentence with *yleensä*.

## Scores
- 1 Physics and mathematical correctness: 5. I reproduced every number, gave every model its conditions and found no A or B finding; the three Polish items are Minor.
- 6 Experimental reasoning (physics): 5. Background is modelled and fitted, the simulated data are labelled, and controlled experiments isolate how sample size affects the random spread.
