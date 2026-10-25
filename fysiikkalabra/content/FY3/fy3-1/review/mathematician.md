VERDICT: PASS
CONTENT-HASH: a0e6a00025fcf31a

## Blocking

## Polish
1. lesson.md:38 — "1,62/9,81 ≈ 0,17" is followed by "noin kuudesosa" without linking the two — write "1,62/9,81 ≈ 0,17 ≈ 1/6" so the student sees why 0,17 means a sixth.
2. lesson.md:55 — "paino Maassa on noin 9,81 N" while lesson.md:29 states the exact "on siis 9,81 N" — drop "noin" (1 kg · 9,81 m/s² is exactly 9,81 N with this g).

## Checked
- Hash at start and end: a0e6a00025fcf31a (unchanged); lint 0 errors, 0 warnings.
- L1-04 (new spring): F = 4,0 N · 6,0 cm / 2,5 cm = 9,6 N; ratio 6,0/2,5 = 2,4 in the sanity check correct; answers.py line 11 matches; spring differs from lesson.md:8 (5,0 N ↔ 2,0 cm), L1-02 (4,0 N ↔ 2,0 cm) and exit ticket 2 (8,0 N ↔ 3,0 cm).
- solutions.md:45, 85, 93 now use "≈" for 4,995 kg, 133,2 kg and 0,991 kg (exact 4,9949…, 133,22…, 0,99083…); all other "=" values are exact (39,24; 48,6; 62; 0,5886; 1422,45; 234,9; 1187,55; 1,962; 5,886; 215,82; 9,72).
- lesson.md:38 — 1,62/9,81 = 0,1651 ≈ 0,17 (2 sf) and ≈ 1/6 = 0,167, consistent with lesson.md:3, 50 and solutions.md:23, 63.
- Exit ticket 3: 1,5 kg · 9,81 m/s² = 14,715 N ≈ 15 N; question now refers to the water's mass consistently.
- Exit tickets 1 (29,43 → 29 N; 4,86 → 4,9 N) and 2 (20/8,0 = 2,5; 7,5 cm) correct.
- Rearrangements m = G/g, m_Kuu = F/g_Kuu, lukema = G/(9,81 m/s²) correct, units N ÷ m/s² = kg; L3-01 1,8349 kg · 3,71 m/s² ≈ 6,807 N, sanity 0,378 ≈ 0,38.
- answers.py re-run: all twelve values equal the unrounded intermediates in solutions.md.
- lesson.md numbers: 1177,2 ≈ 1180 N = 1,18 kN; 445,2 ≈ 445 N; 686,7 ≈ 690 N; 5,0 N : 2,0 cm scaling to 10 N ↔ 4,0 cm and 2,5 N ↔ 1,0 cm.
- SVG (lesson.md:10-20, unchanged): spring 34–166 meets block top centre (200, 166); arrow 236–290 inside the 300 px viewBox; labels fit in 600 px. Arrow starting at the block edge is accepted as is.
