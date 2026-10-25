VERDICT: PASS
CONTENT-HASH: e46974a555df8d9d

## Blocking

## Polish
1. solutions.md:45, 85, 93 — "= 4,995 kg", "= 133,2 kg" and "= 0,991 kg" are rounded values written with "=" (exact: 4,9949…, 133,22…, 0,99083…) — write "≈" as line 77 already does.
2. lesson.md:15 — the weight arrow now starts on the block's bottom edge (200, 236), which is acceptable; for the usual convention start it at the block's centre (200, 201) and move the "m" label aside (e.g. x = 180).
3. exercises.json:30 — L1-04 uses the same spring as the scaling example in lesson.md:8 (5,0 N ↔ 2,0 cm), so it only interpolates between the given 4,0 cm and 1,0 cm cases — use a different spring, e.g. 6,0 N ↔ 2,4 cm, and update answers.py and solutions.md:26-29.
4. exit-ticket.json:11 — the question gives the mass of the water but quotes "pullo painaa puolitoista kiloa", which would include the bottle — write "vesi painaa puolitoista kiloa" or "pullossa on puolitoista kiloa vettä".

## Checked
- Hash at start and end: e46974a555df8d9d (unchanged); lint 0 errors, 0 warnings.
- L1-04 (new): F = 5,0 N · 3,0 cm / 2,0 cm = 7,5 N; ratio 1,5 in sanity check correct; matches answers.py.
- L1-02 (reworded): 2,0 cm · 12 N / 4,0 N = 6,0 cm, ratio ×3 correct.
- Exit ticket 3 (new): 1,5 kg · 9,81 m/s² = 14,715 N ≈ 15 N (2 sf), unit argument correct.
- solutions.md:7, 47 — 1 kg ≈ 10 N gives ≈ 40 N and ≈ 5 kg, consistent with 39,24 N and 4,995 kg.
- solutions.md:23 — 30 · 9,81 = 294,3 ≈ 294 N; 48,6 / 294,3 = 0,165 ≈ 1/6.
- solutions.md:63 — 1,62 / 9,81 = 0,165 ≈ 1/6, drop 1187,55 / 1422,45 = 0,835 ≈ 5/6 = 83 %.
- answers.py re-run: all twelve values equal the unrounded intermediates in solutions.md; rearrangements m = G/g, m_Kuu = F/g_Kuu, lukema = G/(9,81 m/s²) correct with units N ÷ m/s² = kg.
- SVG (lesson.md:10-20): spring 34–166 attaches at the block's top centre (200, 166); block 160–240 × 166–236; arrow shaft 236–272 starts on the block, head tip at 290 inside the 300 px viewBox; "G = m g" label (x ≈ 222–300) and spring labels fit in the 600 px width.
- lesson.md numbers: 1177,2 ≈ 1180 N; 445,2 ≈ 445 N; 686,7 ≈ 690 N; 0,1 kg ≈ 1 N; 5,0 N : 2,0 cm scaling to 10 N and 2,5 N; exit tickets 1 (29 N, 4,9 N) and 2 (7,5 cm) correct.
