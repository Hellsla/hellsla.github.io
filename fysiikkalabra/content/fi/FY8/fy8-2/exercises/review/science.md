VERDICT: PASS
CONTENT-HASH: ee5dfc08e51a45b0

## Blocking

## Polish
- exercises/solutions.md:109 (L3-02 Järkevyys) — the sentence "Näin pienellä energiaerolla molekyyli ei voi absorboida näkyvää valoa tästä tilasta" reads as if one small gap rules out all visible absorption. Say instead that this vibrational transition matches infrared, not visible light, e.g. "tämä siirtymä vastaa infrapunaa eikä näkyvää valoa".

## Checked
- I recomputed all 12 answers with my own formulas in one script. Each agrees with answers.py and exercises.json to within 0,4 %: 2,4701 eV, 433,57 nm, 4,5701·10¹⁴ Hz, 1,89 eV, 655,60 nm, 486,27 nm, 670,27 nm, 121,57 nm, 2,1053 eV, 364,70 nm, 82,666 meV, 564,34 nm.
- The only change since round 2 is the L2-01 reasonableness check, which now states hc ≈ 1240 eV·nm with units. It is correct.
- L2-02: the pair differences are 1,85, 2,15 and 4,00 eV. The smallest gives the longest line, 670 nm (red); the others are 577 nm and 310 nm.
- L2-03: 10,2 eV gives 122 nm, which is UV. The conclusion that cold H is transparent to visible light holds.
- L3-01: the Balmer limit is 364,7 nm, below the 410 nm line and just under 380 nm.
- L3-02: the CO₂ 15,0 µm band gives 82,7 meV. The ×30 estimate against 500 nm is a real check.
- L3-03: the task states that no energy becomes heat. The 1,20 eV photon is IR (1033 nm), the second photon carries 2,197 eV, so 564 nm. Rounding to 0,01 eV in the subtraction keeps 3 significant figures.
- The real lines are correct: He 502 nm (501,6), Na 5,09·10¹⁴ Hz, which is 589 nm, and H 656/486/434 nm.
- Every solution is complete: given, asked, principle, symbolic formula, conversion by substitution, rounding reason and reasonableness check. Signs and units are right, and the tolerance of 0,02 fits the 3-significant-figure data.
- Notation (E_y, E_a, ΔE, hc/λ) matches the brief. Scope stays inside FY8.
