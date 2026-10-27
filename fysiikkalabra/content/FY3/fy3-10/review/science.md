VERDICT: PASS
CONTENT-HASH: 1bfd6e4d506d0b05

## Blocking

## Polish
- solutions.md:126 (L3-03, Vastaus): says M = 29 g/mol "ei rajoita". M has two figures, as Δp = 3,0 bar does, so it limits the answer just as much. Name both data.
- solutions.md:127 (L3-03, Järkevyys): the "30 % ylipaineesta … koska ilmanpaine ei vuoda" sentence is muddled, and the 11,0 bar total assumes an atmospheric pressure of 1,0 bar that is never stated.
- solutions.md:79 (L2-03, Järkevyys): "lämpötila nousee, kun kaasua puristetaan" holds for this data (a fast compression), not for every compression.
- inquiry.json:480 (check-2, Periaate): "pV = NkT" uses a k the lesson never defines. Write "p = nRT/V ja n ∝ N, joten p ∝ NT/V".
- solutions.md:112 (L3-02): 1328,9 J follows from the rounded n = 0,5455 mol. The exact n = 6/11 mol gives 1328,8 J. The result 10,96 mm is the same either way, so this is harmless.

## Checked
- The diff since my round-2 PASS (fdcab429ebd8dd6e) touches only solutions.md L3-01 and L3-02, which split their substitutions. The other files are unchanged from the version that round checked in full.
- L3-01: numerator 101 000 Pa · 0,00055 m³ · 6,022·10²³ 1/mol = 3,345·10²⁵ J/mol. Denominator 8,31 · 310,15 = 2577 J/mol. Ratio 1,298·10²². The units are right: Pa·m³ = J, and N comes out dimensionless.
- L3-02: n = 6,0/11 = 0,5455 mol. Numerator 1328,9 J, denominator 101 000 Pa · 1,20 m² = 121 200 N, and Pa·m² = N is right. d = J/N = 0,01096 m = 10,96 mm, which rounds to 11 mm.
- The Vastaus and Järkevyys lines of both tasks still agree with the new intermediate values:
  - L3-01: n = 0,0216 mol and 2,7·10²¹ O₂ molecules.
  - L3-02: 21,8 g − 15,8 g = 6,0 g.
- One script recomputed all 12 exercise answers independently and compared them with answers.py and exercises.json. All agree, and every stated answer is within 0,42 % of the exact value, inside its 2 % tolerance.
- The rounding reasons in L3-01 and L3-02 are unchanged and still correct:
  - L3-01 is limited by V = 0,55 l.
  - L3-02 is limited by Δm = 6,0 g and by M_Ar − M_ilma = 11 g/mol, a difference with two figures.
- Content hash checked at the start and at the end: unchanged.
