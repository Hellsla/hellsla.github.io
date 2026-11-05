VERDICT: PASS
CONTENT-HASH: 5a691da5f3916a2a

## Blocking

## Polish
- content/fi/FY1/fy1-6/exercises/exercises.json:313 (fy1-6-L2-08, reason 2) — **Causality wording.** "Raskaampi pallo vetää itseään voimakkaammin kohti Maata" makes the ball the source of the pull. The feedback then builds on the claim without correcting who pulls. — Write "Maa vetää raskaampaa palloa voimakkaammin, joten sen nopeus kasvaa nopeammin." This keeps the misconception and gets the agent right.
- content/fi/FY1/fy1-6/exercises/solutions.md:201 and exercises.json:314, 323 (L2-08) — The argument that a greater pull and greater inertia cancel is correct (C), but it reaches into force and Newton II, which the FY1 scope notes leave to FY2/FY4. The lesson only states that g is the same for all bodies without air. The Mallivastaus already has the in-scope reason ("v = g t ei sisällä massaa"). Consider marking the cancellation sentence as extra ("Myöhemmin FY2:ssa nähdään…") or shortening it.
- solutions.md:201 — The Mallivastaus computes 9,81 · 2,0 = 19,62 m/s, while the task gives the heavier ball's 19,6 m/s as data. The simplest model answer is "sama kuin raskaammalla, 19,6 m/s", with g t only as a check. Correct either way.

## Checked
- I recomputed all 18 numeric answers in one script with my own formulas. All agree with answers.py. L2-05 slope 9,743 m/s² (intercept 0,01 m/s), L2-06 b/k = 0,201 s, L2-07 9,82 m/s², L3-04 62,0 %, L3-05 0,15 s.
- L2-08: only 19,6 m/s is correct. 4,9 (= 19,6/4), 9,8 (g read as a speed) and 78 (= 4·19,6) are each wrong for the reason their feedback states.
- L2-08 reasons: only reason 3 is correct. Reason 1 is true but irrelevant, and its feedback rightly notes that size does not matter in vacuum. Reasons 2 and 4 are wrong, with physically correct feedback.
- L2-08: "tyhjiökammio" states the no-air condition, and the solution names it.
- L2-07 (light gates): the mean speed over the interruption is assigned to the midpoint of the interruption. That is correct for uniform acceleration, and the release time cancels.
- L3-04: the filter paper levelling off near 1,5 m/s is attributed to air resistance growing with speed. The mechanism is right and the model condition is stated.
- L2-02 and two-planets: the A line passes (5; 20) and the B line (5; 40), giving 2,5 s. The caption matches the drawing.
- Notation v = g t, g = 9,81 m/s² and Δv = g Δt matches the lesson.
