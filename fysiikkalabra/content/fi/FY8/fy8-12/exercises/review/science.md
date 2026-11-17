VERDICT: PASS
CONTENT-HASH: d74f1bab5e2d2fa5
SCOPE: delta (round 2) fy8-12-L3-07 limit 1/20 -> 1/50, answer 52 -> 68; L2-09 unchanged

## Blocking

## Polish
- exercises/solutions.md:302 (fy8-12-L3-07, Järkevyys) — the check only brackets the result between 60 mm and 72 mm. It could also say that 1/50 lies closer to 1/64 than to 1/32 on a log scale ($\log_2 50 \approx 5{,}64$), so the result falls nearer 72 mm. This is optional.

## Checked
- Hash d74f1bab5e2d2fa5 at the start and the end. Judged the diff (L3-07 text, answer, solution, answers.py line) and its context in solutions.md:290–302.
- I recomputed independently: $d = 12\,\text{mm}\cdot\ln 50/\ln 2 = 12 \cdot 5{,}6439 = 67{,}73\,\text{mm}$. answers.py gives 67,726274, which agrees. The intermediate values $\ln 50 = 3{,}9120$ and $\ln 2 = 0{,}69315$ are correct.
- Allowed rate: $R = 800/50 = 16$ pulses/min, correct. At 48 mm, $800\cdot(1/2)^4 = 50 > 16$, so the conclusion that 48 mm is not enough is correct. The task text, Annettu, Periaate, Kuvaajan lukeminen, Vastaus and Järkevyys all say 1/50 and 16 consistently.
- Rounding: 67,73 is rounded up to 68 mm. That is right for a limit of "enintään" on the rate, which means a minimum thickness (P7). It also matches two significant figures from the 12 mm read off the graph.
- Tolerance 0,02 on 68 accepts 66,6–69,4 mm. That covers 67,7 and 68.
- Reasonableness check: $(1/2)^5 = 1/32 > 1/50 > 1/64 = (1/2)^6$, so the thickness lies between 60 mm and 72 mm. The result fits, so this is a real check of the model.
- The diff showed a stray "d" in the Sijoitus chain. The file on disk now has three separate rows, each starting with $d =$, and no stray symbol, so the chain is correct.
- Extrapolating past the graph's 48 mm uses the exponential law, which the lesson states for photon radiation. The task names gamma radiation and net rates, so the law's conditions are met. The narrow-beam caveat in the lesson is a level-appropriate simplification (C).
- L2-09 is unchanged: $800\cdot0{,}5^{2{,}5} = 141{,}4$, which agrees with answers.py.
