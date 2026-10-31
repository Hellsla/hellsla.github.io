VERDICT: PASS
CONTENT-HASH: 7646d6b7c3a92e84

## Blocking

## Polish
- lessons/FY1/fy1-3/answers.py:31 — the comment says "relative error" for Δt/t̄·100 % — rename it to "relative uncertainty", the term solutions.md L2-01 now uses (comment only).

## Checked
- I recomputed all 12 answers in one script with my own formulas: L1 gives 0,51 s, +0,3 cm, 0,35 s, 47,5 g and 0,5 mm; L2 gives 4,83 %, 10,67 mm, 12,4 cm and 10; L3 gives −0,06 s, 2,0 µm and 0,26 cm. exercises.json and answers.py agree with these.
- The rounded answers stay inside the tolerance: 5 % (3,5 % off), 11 mm (3,1 % off) and 0,4 s (14 % off, tolerance 15 %).
- L1-03: the figure pendulum-dots (lessons/FY1/fy1-3/figures.py) has its points at 12,2, 12,4, 12,6, 12,7 and 12,9 s, with grid lines every 0,1 s and numbers every 0,2 s, as the solution reads it.
- L3-01: the sign is right. A late start shortens the reading by 0,18 s and a late stop lengthens it by 0,12 s, so the error is −0,06 s.
- L3-02: Δh₁ = d/(2n) with an exact count gives 2,0 µm. The reasonableness check (about 2 % of 100 µm, and 500 % for a single sheet) is right.
- Terms follow the guardrails. Mittausvirhe has a sign (L1-02, L3-01). Half the range is a scatter estimate (L1-03, L2-01, L2-04). "Suhteellinen epävarmuus" is used in L2-01 and L3-02, and no "suhteellinen virhe" is left.
- Every solution has all seven steps, solves in symbols first, and justifies its rounding by the limiting datum. The meaning is the same as content/fi.
