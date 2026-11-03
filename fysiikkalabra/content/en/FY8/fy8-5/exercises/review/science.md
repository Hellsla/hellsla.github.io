VERDICT: PASS
CONTENT-HASH: defa6505accfdfa4

## Blocking

## Polish
- packet-science.md "Exercise brief" — the brief is still empty. scripts/review_packet.py looks for the Finnish headings (Kaava, Esimerkki) and so misses the English "Formula" and "Worked example". I checked the notation against content/en/FY8/fy8-5/lesson.md instead. — Match the localized headings in review_packet.py.

## Checked
- A script compared exercises.json and solutions.md with the fi source. All 12 `answer` and `tolerance` values are identical, and so is every number and formula once the decimal sign is normalized. The only changes are the subscript names (ulko→out, sisä→in, ulko→outer).
- The units changed from kpl to electrons (L1-01, L2-02, L3-02), hits (L1-03, L2-03, L3-03) and orbitals (L3-01). Each unit matches what its task counts.
- Recomputed in one script with my own formulas:
  - L1: 50, 5.2625 %, 300, 1.5111 eV and −0.544 eV.
  - L2: 102.57 nm, 8, 960 and 364.70 nm.
  - L3: n = 3.986 → 16, then 15 and 4235.

  All of these agree with the answers and the solutions.
- The solutions are symbolic first, eV is converted to J by substitution, and the rounding to 3 significant figures is tied to 13.6 eV.
- Conditions are kept: "expected value", "approximately", "practically entirely", "exactly half full" and "at least".
- The set stays within FY8 scope: E_n is given as data, and there is no de Broglie wavelength or Schrödinger equation.
