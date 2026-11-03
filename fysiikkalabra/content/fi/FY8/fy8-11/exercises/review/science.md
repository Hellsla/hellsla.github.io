VERDICT: FAIL
CONTENT-HASH: 6eb0c76702f807b5

## Blocking
- exercises.json:82 (fy8-11-L3-01) — B: the task asks how much U-235 fissions per day from the thermal power 4300 MW. That holds only if all the heat comes from U-235 fissions, but a real OL3 core gets a large share from Pu-239 fission, and the task does not state the assumption (house rule: state the model's assumptions in the task). — Add "Oleta, että kaikki lämpöteho syntyy uraani-235:n fissioista." The solution's Periaate should say the same.

## Polish
- solutions.md:49 (L1-05) and solutions.md:109 (L3-02) — "fissiossa muuttuu energiaksi vain pieni osa massasta" and "Massaa muuttuu energiaksi" use the wording the lesson's misconception section warns against. Write "massa pienenee" / "massan pieneneminen vastaa energiaa".
- solutions.md (L3-02 Periaate) — the sum of atomic numbers is not conserved here (4 → 2). Add one clause on why atomic masses still work: the two positrons annihilate with two electrons, and the task tells the student to use atomic masses.
- solutions.md (L1-04 Järkevyys) — "selittää, miksi voimaloihin suunnitellaan juuri tritiumia": the larger reaction rate of D–T also matters. Soften to "on yksi syy".
- exercises.json L2-01 / L2-04 — `answer` 1.51 and 4.11 against the solutions' answers "1,5 kg" and "4,1 %". The tolerance covers both, but one form would be cleaner.

## Checked
- All twelve answers recomputed with my own formulas: 4,783; 178,4; 348,7; 3,269; 939,57; 1,509 kg; 3,374·10^14 J/kg; 184,7 MeV (x = 2); 4,106 %; 4,526 kg; 8,944·10^37 1/s; 2,402·10^5 a. All agree with answers.py.
- Atomic masses are AME2020 values; the stated conditions (charge-number sum conserved, full power all year, all energy radiated) are correct.
- The reasonableness checks really are checks (round-number estimates, 2^10 ≈ 1000, fission 8,2·10^13 J/kg × 4).
- Rounding reasons are given; the tolerance of 2 % fits.
- Hash 6eb0c76702f807b5 at the start and at the end.
