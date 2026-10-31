VERDICT: PASS
CONTENT-HASH: b191ea9ccf473f7b

## Blocking

## Polish
- lessons/FY1/fy1-3/answers.py:31 — the comment says "relative error" — make it "relative uncertainty" to match the term the lesson now uses.
- exercises/solutions.md fy1-3-L1-02 Järkevyys — one reading against a known reference cannot alone separate a systematic error from a random one. "todennäköisesti systemaattinen" is fair, but adding "toistamalla mittauksen voisi varmistaa" would be better.

## Checked
- Recomputed all 12 answers in one script with my own formulas: 0,51 s; +0,3 cm; 0,35 s (figure points 12,2–12,9 s, checked in figures.py); 47,5 g; 0,5 mm; 4,83 %; 10,67 mm; 12,4 cm; 10; −0,06 s; 2,0 µm; 0,26 cm. Every value matches answers.py and exercises.json.
- The rounded answers in the solutions (0,4 s; 5 %; 11 mm; 2 µm) fall inside each relative tolerance.
- L3-01: the signs of the start and stop delays are right (reading = true − τ1 + τ2).
- L3-02: dividing the uncertainty by n assumes equal sheets, and the task states this.
- The solutions are complete (given and asked, principle, symbolic form, conversions, substitution, rounding reason, a real check). They use "suhteellinen epävarmuus" and the half-range consistently with the guardrails.
- The levels fit FY1 scope.
