VERDICT: PASS
CONTENT-HASH: af25454f80bec980
SCOPE: delta added-exercise from df56262b52ce34b1 base 8f23aa7ae3bd

## Blocking
- none

## Polish
- lessons/FY6/fy6-10/figures.py ex_pari (alt text) — the description names the curves' start points (3 cm, 4,4 cm) but not the values L2-10 needs (F_A = 4,0 mN at 3,0 cm; curve B at 4,0 mN at 6,0 cm), so a screen-reader user cannot solve the task — add e.g. "käyrä A kulkee pisteen (3,0 cm; 4,0 mN) kautta ja käyrä B pisteen (6,0 cm; 4,0 mN) kautta"; neither gives q_B away.
- solutions.md fy6-10-L2-09 Kuvaajan lukeminen — "noin 0,06 mN viivan yli" is finer than a 1 mN grid allows; the stated ±0,1 mN and "≈ 5,1 mN" are the honest reading (the answer is insensitive: 4,9–5,3 mN give 29,5–30,7 nC, inside tolerance 0,05).

## Checked
- fy6-10-L1-09 recomputed with MAFY k = 8,98755 · 10⁹ N·m²/C²: F = k · 40 · 10⁻¹⁸ C² : (0,040 m)² = 0,2247 mN; matches; tolerance 0,02 covers the lesson's 8,988 · 10⁹ and the rounded 0,22 mN (−2,1 % is borderline but the answer check also accepts half a unit of the last shown digit). Repulsive, both positive: right.
- fy6-10-L2-09 recomputed: curve drawn for 30 nC + 30 nC (figures.py), F(4,0 cm) = 5,06 mN, q = r·√(F/k) = 30,0 nC; matches.
- fy6-10-L2-10 recomputed: F_A(3,0 cm) = 3,99 mN, F_B(6,0 cm) with q_B = 80 nC = 3,99 mN; q_B = 20 nC · (6,0 : 3,0)² = 80 nC; matches; k and the common 20 nC cancel correctly; curve B above A as stated.
- Point-charge model and same-sign charges stated in each task; figures drawn from Coulomb's law at the stated charges; no answer written in the figures.
- All three solutions complete (symbolic solve, conversions, substitution, rounding reason, back-substitution check).
- Content hash checked at start and end.
