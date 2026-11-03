VERDICT: PASS
CONTENT-HASH: 3fa2c76f56f19e19

## Blocking

## Polish
- packet-science.md "Exercise brief" — the brief is empty (a tool bug: the extractor looks for the Finnish section names Kaava/Esimerkki, but the English lesson uses "Formula"/"Worked example"). I checked notation against content/fi/FY8/fy8-5 instead. — Fix scripts/review_packet.py so it matches the localized headings.

## Checked
- A script compared exercises.json with the fi source key by key: all 12 `answer` and `tolerance` values are identical, and every number and $…$ formula in the task texts matches apart from the decimal sign.
- A script compared solutions.md with the fi source line by line. Every number and formula is identical; the only change is the subscript names (ulko→out, sisä→in, ulko→outer).
- Recomputed in one script with my own formulas: L1 50, 5.2625 %, 300, 1.5111 eV, −0.544 eV; L2 102.57 nm, 8, 960, 364.70 nm; L3 n = 3.986 → 16, 15, 4235. All agree with answers.py and the solutions.
- Conditions are kept: "expected value", "approximately", "practically entirely" (L3-03), "exactly half full" (L3-02), "at least" (L1-04), "greatest wavelength" (L2-04), "exactly the difference" (L3-01 absorption).
- L2-04 says "just below the visible range, near ultraviolet". "Near ultraviolet" is the correct English term for 365 nm, so the source's polish point does not carry over.
- The solutions are symbolic first, eV→J by substitution, and the 3-significant-figure rounding is tied to 13.6 eV, as in the source.
- Within FY8 scope: E_n is given as data, with no de Broglie and no Schrödinger equation.
