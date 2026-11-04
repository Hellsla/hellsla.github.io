VERDICT: PASS
CONTENT-HASH: 12f7e2cfc1c54b61

## Blocking

## Polish
- inquiry.json:89 (ennuste-2 feedback), sim-spec "tyypillinen arvontajärjestys" — seed 73 is slower than the median at small N (18,4 cm against a median of 4,2 cm at N = 10, and 4,0 cm against 1,4 cm at N = 20). Over seeds 1–100, 94 runs are within 1,5 cm at N = 100 but the worst is still 19 cm, and all 100 are within 1,5 cm only by N = 150. Write "vasta noin 100–150:llä" and "melko hidas arvontajärjestys", or leave the claim as it is: "kymmeniä" holds.
- lesson.md:14 "volframilla ne ovat noin 59 keV:n kohdalla" — tungsten's K lines are at about 58–59 keV (Kα) and 67–69 keV (Kβ). Write "noin 59 ja 67 keV:n kohdalla".
- lesson.md:27 "kalsiumatomeissa on paljon elektroneja" — the main cause is the larger atomic number (photoabsorption rises steeply with Z). Carried over from round 1.
- lesson.md:69 figure and ennuste-3 "terve kudos … noin 0,40 Gy" — this is less than the entrance dose (L3-01 gives 1,3 ×). Carried over from round 1.
- lesson.md:142 "noin 150 000-kertainen" and PET about 6 mSv (FDG only, without the CT part of a PET-TT scan). Carried over from round 1.

## Checked
- Blocker A fixed: I reran the sim model over seeds 1–100 (case seed s + 1000). The median distances are 4,18 / 1,41 / 1,00 cm at N = 10 / 20 / 50; 86 runs are within 1,5 cm at N = 50 and all 100 at N = 150. Seed 73 gives 18,4 / 4,0 / 1,4 / 0 cm at N = 10 / 20 / 50 / 200. This matches the developer's comment, ennuste-2, the johtopäätös model and the sim-spec.
- sim.js and lesson-answers.py are the same model: generator, seed 73 + 1000·case, the order of the rand() calls, PT, σ, 0,6 cm and the 1,0 cm share.
- "Kymmeniä" is now the only correct option of ennuste-2. Both distractors' feedback cites seed 73's values correctly.
- Blocker B (TOF) fixed: the theory, ennuste-1 (correct option and the midpoint distractor), the model box, the johtopäätös and the exit ticket now state that the arrival-time difference is not used. 0,3 ns gives cΔt/2 = 4,5 cm, i.e. "muutama cm".
- Blocker B (characteristic X-rays) fixed: the definition, the glossary entry and the summary include inner-shell transitions.
- Worked example: n = d : d½, then 2^(n_B − n_A) = 2^1,845 = 3,59 → 3,6. The second route 0,1957 : 0,05449 gives the same value.
- Am-241: 1,6 % in 10 a, so "noin 2 %" is fine. Siirto 772,0 → 770 MBq. f = 1,2355·10²⁰ Hz.
- The lesson-answers.py comments are corrected (0,05449, 772,0).
- The NIST d½ table, the Pb 3,9 / 0,26 mm values and the ratio 15 are unchanged from round 1 and still correct.
