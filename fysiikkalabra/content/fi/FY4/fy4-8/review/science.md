VERDICT: FAIL
CONTENT-HASH: d97eb2ce61511fba

## Blocking
- inquiry.json:478 (check-3 model; prompt :471) — **A.** "jokaisen mäen on oltava edellistä matalampi" does not follow from falling mechanical energy. A later hill only has to be lower than the height the remaining energy reaches, so it may be taller than a low hill before it. — Fix: "matalampi kuin korkeus, jolle jäljellä oleva mekaaninen energia riittäisi; siksi mäet yleensä madaltuvat". In the prompt, ask why later hills are lower than the first.
- inquiry.json:474 (check-3 criterion 2) — **A.** The rubric gives the wrong cause: "enintään lähtökorkeudelle, koska huipulla on oltava liike-energiaa jäljellä". The limit comes from energy conservation, and leftover kinetic energy is why a hill must be lower. This was Polish in round 1; it is in the self-assessment rubric. — Split it into "…koska mekaaninen energia säilyy; myöhemmän mäen on oltava matalampi, jotta huipulla jää liike-energiaa".

## Polish
- lesson.md:361 — Write "matalampi kuin ensimmäinen" so the claim is unambiguous.
- lesson.md:481 — "eli kitkan ja ilmanvastuksen voi jättää huomiotta" leaves out pulling or pushing forces. Add "eikä mikään vedä tai työnnä".
- lesson.md (Kaava) — W = F_∥ s is given for straight-line motion but used along curved track. Add "kun vastusvoima on koko ajan liikettä vastaan".

## Checked
- The round-1 Blocking item (the sign of friction work) is fixed, with its condition and the belt counter-example.
- I recomputed every lesson and inquiry number in one script with my own formulas. All match:
  - sled: −645 J, 9,90 m/s, 41 %, 26,9 N
  - cart: 36 J, 6,0 m/s
  - error-spotting: 4,2/6,4/5,4 m/s
  - swing: 4,852 m/s and its mistake values
  - check-2: 14,69 m/s and its mistakes
- For the sim, I solved mgh1 − F(L1+2B+L2) = mgh2 independently. At 100/200 N: h2 is 8,79/7,66 m, s is 47,4/45,9 m and ΔE_mek is −4,74/−9,19 kJ. E_mek ends at 30,1 kJ, and v_pohja is 14,0 m/s for every mass and both tracks.
- The only sim.js change gives the E_mek bar its own colour; the physics is unchanged.
- The experiments isolate their varied parameter, and simState gives the measured keys.
- Every choice item has exactly one correct option, and the distractor feedback is right.
- The derivations of W_kok = ΔE_k and of the energy principle are correct.
- The konservatiivinen-voima recall and "paino eli painovoima" are consistent with fy4-7. The exit ticket and the summary agree with the theory.
