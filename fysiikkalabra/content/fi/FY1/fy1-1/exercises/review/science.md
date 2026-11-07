VERDICT: PASS
CONTENT-HASH: 4ea094c3a76b7a09
Mode: light (teacher 2026-11-07, "kevyt katselmointi": round-2 diff since edb368de4 only)

## Blocking
- none

## Polish
- L3-05: the answer 142,5 AU is the distance from the Sun and 143,05 AU is from the Earth; the solution says this, and the 0,6 AU difference is under the stated 1 AU limit. Physically right (in February Voyager 2 lies about 50° from the Sun's direction, so Earth−probe ≈ d + 0,6 AU).

## Checked
- diff exercises.json, solutions.md, answers.py (L3-04 10 min exact; L3-05 Voyager d0 119,0 AU).
- Recomputed: 15,341 km/s · 7,25 · 3,156·10⁷ s = 3,510·10⁹ km = 23,46 AU; 119,0 + 23,46 = 142,46 → 142,5 AU (key 142.5). L3-04 1,19·10⁹ unchanged.
- Voyager values agree across chapters: fy1-2 says Feb 2026 ≈ 142,5 AU, fy1-5 says 15.2.2026 142,6 AU (exact dates 142,4–142,7 AU).
