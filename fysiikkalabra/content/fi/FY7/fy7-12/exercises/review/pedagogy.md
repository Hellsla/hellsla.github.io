VERDICT: FAIL
CONTENT-HASH: ce7668f796b8c369

Round 2

## Blocking
- exercises.json:fy7-12-L1-08 and solutions.md:fy7-12-L1-08 Vastaus — the model answer is now "1,0 · 10² km (noin 100 km)", but the box answer is 103,4483 with tolerance 0,02 (accepts 101,4 to 105,5), so a student who writes the solution's own 100 km is marked wrong; CLAUDE.md requires rounding to the significant figures to stay inside the tolerance. Fix: tolerance 0.04, or write the answer as 103 km (three figures, as n = 1,45).
- exercises.json:fy7-12-L3-04 and solutions.md Vastaus — the model answer is now "17° (17,4°)", but the box answer is 17,3673 with tolerance 0,02 (accepts 17,02 to 17,71), so 17° is rejected. Fix: tolerance 0.03, or keep the answer 17,4°.

## Polish
- exercises.json:fy7-12-L3-04 — the "n1/n2 − 1" delay measure is still given as a fact; add half a sentence that it is the relative extra path of the steepest zigzag ray (carried over).
- solutions.md:fy7-12-L3-04 Vastaus — "yhden tai kahden merkitsevän numeron luku" is unclear; say the difference n1 − n2 = 0,03 has one figure.
- exercises.json:fy7-12-L2-02 (42 words) and L3-02 (58 words) — existing tasks with long lead paragraphs; split when next touched.

## Checked
- Round-1 Blocking (L2-06 52 words, L3-04 58 words, L3-05 62 words) resolved: each is split into short paragraphs (longest about 38 words).
- L2-06 table rows 49,0 and 49,2 µs now 0 % (nothing arrives before the axial ray at 49,33 µs); width 800 ns and the added "no earlier light" sentence are correct.
- L2-05: the given sum 210,2° removed from the task and shown in the solution; n = 1,493, 1,477 to 1,509; polystyrene limit 39,0° correct.
- L2-07 and L1-06 reworded and reordered without changing the physics; distractors keep their feedback.
- L3-05: R_min = 16,06 mm (box 16,0556, so 16 mm is inside tolerance); sin α = (R − a) : (R + a) correct; the "vain b)" instruction and self-checked drawing are clear.
