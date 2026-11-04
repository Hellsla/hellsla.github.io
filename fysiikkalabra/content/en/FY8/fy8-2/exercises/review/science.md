VERDICT: PASS
CONTENT-HASH: f6123a0838802040

## Blocking

## Polish
- exercises/review/packet-science.md (tooling) — the exercise brief block is empty for the English lesson (the brief extractor looks for the Finnish section names Kaava/Esimerkki); the set was judged against the lesson as given in the lesson packet. Fix the packet script for translated headings.

## Checked
- Recomputed all 12 answers in one script with my own formulas: 2.4701 eV, 433.57 nm, 4.5701e14 Hz, 1.89 eV, 655.60 nm, 486.27 nm, 670.27 nm, 121.57 nm, 2.1053 eV, 364.70 nm, 82.666 meV, 564.34 nm; all match exercises.json and answers.py.
- Answers, units and tolerances identical to the fi source; numbers in every solution identical to the fi source.
- Every solution: given/find/principle/formula/conversions/substitution/answer/reasonableness, unknown solved symbolically before substitution, eV→J conversion shown.
- Rounding: 3 s.f. justified by the limiting datum (L1-04 and L2-03 by the hundredths of the level energies / 10.2 eV).
- L2-02: smallest difference 1.85 eV of {1.85, 2.15, 4.00} gives the longest line; three lines for three states right.
- L3-01: series limit from E = 0, 364.7 nm, just below 380 nm; ionisation boundary stated.
- L3-02: vibrational quantisation, exact-match absorption; the improved reasonableness check (30× wavelength → 1/30 energy, vibrational transition = infrared, absorbs ground IR) is correct.
- L3-03: cascade by energy conservation with no heat assumed in the task; 1.20 eV photon at 1030 nm is IR as stated.
- Notation E_u, E_l, h, c, 1 eV value same as the lesson's Formula section; all inside FY8 scope (levels given as data).
