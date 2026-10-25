VERDICT: PASS
CONTENT-HASH: fc5375c46d696bd5

Checks done: gate hash (start and end) fc5375c46d696bd5; check_latex.py "all LaTeX ok (7 fragments)"; all 12 solutions recomputed in `python3 -I`; every exercises.json `answer` equals the solutions.md final answer; worst relative deviation of the exact value from the stored answer is 0,82 % (L1-03), tolerance is 2 %. Lesson numbers, g table, SVG geometry and worked example verified. No wrong mathematics, no rounding that pushes a correct answer outside the tolerance.

Findings (all advisory, none blocks):

1. solutions.md:23 / exercises.json (fy3-1-L1-03) — advisory — "30 kg" is read as 2 sf (answer 49 N, exact 48,6 N). A student who reads 30 as 1 sf and answers 50 N is 2,04 % from 49 and outside the 0,02 tolerance. Correct step: nothing required (30 kg is 2 sf with g = 1,62 N/kg, and 48,6 and 49 both pass); optionally write "30,0 kg" or raise tolerance to 0,025 for this item.
2. solutions.md:77 / exercises.json (fy3-1-L3-01) — advisory — a student who rounds the intermediate mass to 1,8 kg gets 1,8 · 3,71 = 6,68 N, which is 1,8 % from 6,8 N, only just inside the 2 % tolerance. Correct step: solution already shows the unrounded intermediate 18/9,81 kg and the rule "round only at the end" is applied correctly; no change needed.
3. solutions.md:62 / exercises.json (fy3-1-L2-03) — advisory — exact difference 1187,55 N rounds to 1190 N at 3 sf (data 145 kg, 1,62 N/kg). Stored answer 1190 is correct; 1188 or 1,19 kN also fall within tolerance (0,2 %). No change needed.
4. lesson.md:45-47 — verified — 120 kg · 9,81 N/kg = 1177,2 N ≈ 1180 N (3 sf) = 1,18 kN; Mars 120 · 3,71 = 445,2 N ≈ 445 N. Consistent with the table and with the unrounded-until-the-end rule.
5. lesson.md:52 — verified — 70 kg · 9,81 = 686,7 N ≈ 690 N at 2 sf; consistent.
6. lesson.md:6, 21-28, 57 — verified — g table (Kuu 1,62; Mars 3,71; Maa 9,81; Jupiter 24,8 N/kg) is consistent with the g values in the exercises and solutions; N/kg = m/s² claim is correct; Moon/Earth ratio 1,62/9,81 = 0,165 ≈ 1/6; 0,1 kg · 9,81 = 0,981 N ≈ 1 N (apple). The Moon task L1-03 reads 1,62 from the table, matching the solution.
7. lesson.md:10 — verified — proportional-stretch examples (5,0 N → 2,0 cm; 10 N → 4,0 cm; 2,5 N → 1,0 cm) are correct.
8. lesson.md:33-43 (SVG) — verified — spring polyline alternates x = 184/216 around the axis x = 200 and connects 34→166; mass box 166-246; arrow line 170→258 with head 250→272, all inside viewBox 600×300; labels are plain text with no LaTeX, per NOTES.md.
9. solutions.md:15, 23, 39, 63, 79, 87, 95 — verified — all sanity-check numbers are correct (49,05 N; 294,3 N; 24,8/9,81 = 2,53; 1 − 1,62/9,81 = 83 %; 3,71/9,81 = 0,378; 9,81/1,62 = 6,06; 0,991/6 = 0,165).
