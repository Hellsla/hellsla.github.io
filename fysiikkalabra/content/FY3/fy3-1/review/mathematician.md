VERDICT: PASS
CONTENT-HASH: fb11a9bb17144bae

## Blocking

## Polish

## Checked
- Hash at start and end: fb11a9bb17144bae (unchanged); lint 0 errors, 0 warnings.
- L3-03 (new): lukema = G / 9,81 m/s² ⇒ G = 26 kg · 9,81 m/s² = 255,06 N (exact, kg·m/s² = N); m = G / g_Mars = 255,06 N / 3,71 m/s² = 68,749… ≈ 68,75 kg → 69 kg (2 sf as the data 26 kg); the rearrangement is correct and nothing is rounded before the end.
- L3-03 sanity check (solutions.md:95): 3,71/9,81 = 0,378 ≈ 0,38; 9,81/3,71 = 2,644 ≈ 2,6; 2,6 · 26 kg ≈ 68 kg and 68,75 kg, both "vajaat 70 kg"; the ratio is only used qualitatively, not to recompute the answer.
- L3-03 notation: "lukema" with unit kg matches lesson.md:50 (scale = force divided by 9,81 m/s²); g_Mars notation matches L3-01; exercises.json:98 states the calibration rule so the task is solvable.
- answers.py line 21 = 26 · 9,81 / 3,71 = 68.749326, equals the solution's intermediate; exercises.json:99 answer 69.
- lesson.md:38 now "1,62/9,81 ≈ 0,17 ≈ 1/6" (0,1651 and 0,167) and lesson.md:55 "on 9,81 N" (exact 1 kg · 9,81 m/s²); both consistent with lesson.md:29, 50.
- L1-01…L3-02 unchanged and re-verified: 39,24; 6,0; 48,6; 9,6; 62; 4,9949; 0,5886; 1187,55; 5,886; 6,807; 133,22; "=" only for exact values, "≈" for rounded ones.
- Exit tickets: 29,43 → 29 N, 4,86 → 4,9 N; 20/8,0 = 2,5, 7,5 cm; 14,715 → 15 N.
- lesson.md example: 1177,2 ≈ 1180 N = 1,18 kN; 445,2 ≈ 445 N; misconception 686,7 ≈ 690 N; spring scaling 5,0 N ↔ 2,0 cm, 10 N ↔ 4,0 cm, 2,5 N ↔ 1,0 cm.
- SVG (lesson.md:10-20, unchanged): spring 34–166 meets block top (200, 166); arrow 236–290 within the 300 px viewBox.
