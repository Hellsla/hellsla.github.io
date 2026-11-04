VERDICT: PASS
CONTENT-HASH: b07176193a006b48

## Blocking

## Polish
- exercises.json:56 (fy5-3-L1-06, first option's feedback) — typo "keskipistä" — write "keskipistettä".
- solutions.md:149 (fy5-3-L2-05 Periaate) — "kierrosajan virhe on kymmenesosa": the guardrails keep virhe and epävarmuus apart, and the reaction-time error is not exactly known — write "kierrosajan epävarmuus on vain kymmenesosa reaktioajan epävarmuudesta"; in the a) answer say the mean reduces random scatter, not systematic error.
- solutions.md:225 (fy5-3-L3-04 Vastaus b) — the 2 sig. figs are put down to "5,2° has two digits", but cos 5,2° hardly depends on that digit (the limit comes from 62,7° and the 7,7 km/s); give a reason like "data rounded, the difference to a few metres per second" or keep 250 m/s without a digit argument.
- solutions.md:198 (fy5-3-L2-07 Järkevyys) — "32 m/s olisi noin 116 km/h, mikä ei sovi tämän kokoiselle renkaalle" is not a check: 116 km/h is a normal speed. Use instead "the student's v is twice πdf = 16 m/s, so the diameter went in as the radius".
- docs/exercise-bank/FY5.md fy5-3 — the plan's disc video analysis is missing and the radius/diameter error task is at level 2, not 3: note the swap in the plan.

## Checked
- Recomputed every new answer in one script: L1-07 0,020 s; L1-08 0,2094 mm/s; L2-05 T 4,12 s, v 3,203 m/s; L2-06 7,588 / 3,874 / 3,0745 km/s; L2-07 16,08 m/s; L3-04 462,7 / 408,3 / 213,1 m/s, Δv 249,6 m/s, 6,0 %; L3-05 458 and 198 1/min, N 20 625, s 5378 m, t 74,7 min. All agree with answers.py and the solutions.
- L2-06 data are physically consistent: Kepler T from r gives 95,5 / 718,0 / 1435,9 min.
- L3-04: r = R cos φ is given in the task; T = 86 164 s is the sidereal day, which is the right value; plausible launch latitudes.
- L3-05: N·2π·r_ka is exactly the Archimedean-spiral length (π(r₂²−r₁²)/Δr = 5378 m); the CD data are realistic.
- L1-06 MC: exactly one correct option; every distractor's feedback is right and matches the lesson's misconception section.
- Scope: v = 2πr/T, f = 1/T only, no angular quantities; units, tolerances, symbolic-first steps fine; no duplicates, 8/7/5.
- Round 2 delta: the diff is empty and the hash is unchanged, so the verdict stands.
