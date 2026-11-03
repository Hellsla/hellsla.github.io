VERDICT: PASS
CONTENT-HASH: b348c811ebef4c35

## Blocking

## Polish

## Checked
- Both round-1 polish points are fixed:
  - solutions.md L2-04 now reads "ultraviolettia, juuri näkyvän alueen ulkopuolella", which is correct for 365 nm.
  - L2-03 now reads "$50\,\%$:n raja on kokonaan $90\,\%$:n rajan sisällä".
- A script compared exercises.json and solutions.md with content/fi/FY8/fy8-5. All 12 answers and tolerances are identical, and so is every formula and number. The only changes are sentence splits and glosses.
- Recomputed in one script:
  - L1: 50, 5.2625 %, 300, 1.5111 eV and −0.544 eV.
  - L2: 102.57 nm, 8, 960 and 364.70 nm.
  - L3: n = 3.986 → 16, then 15 and 4235.

  All of these agree with answers.py and the solutions.
- The glosses are correct: "absorboi eli ottaa vastaan", "alikuori (kuoren osa)" and "odotusarvo (keskimääräinen luku monen sarjan jälkeen)".
- Conditions are kept: "keskimäärin", "käytännössä kokonaan", "täsmälleen puoliksi täynnä", "vähintään" and "odotusarvo".
- The brief's notation (E_n, n², 2n², P ≈ k/N) is used throughout.
