VERDICT: PASS
CONTENT-HASH: 2c1761040ce1f1cd
SCOPE: delta added-exercise from 8ae950d4924a8353 base 81db4a6fd727

## Blocking

## Polish
- content/fi/FY4/fy4-2/exercises/solutions.md (L1-09, Vastaus) — the line gives "1,3 s (tarkemmin 1,27 s)" and then says the result is given to three significant figures like 24,79 m/s². The two do not agree. Lead with 1,27 s, or say why 1,3 s is enough. Either is inside the 4 % tolerance.

## Checked
- L1-09: the value g_Jupiter = 24,79 m/s² is the VERIFIED fy4-2 row of docs/mafy-arvot.tsv (Aurinkokunta, Jupiter). The hint names only the table ("Aurinkokunta").
- Physics: free fall from rest with air resistance left out (stated in the task), so a = g is constant and h = ½gt² follows from the chapter's x = x₀ + v₀t + ½at² with x₀ = 0 and v₀ = 0. The solution says why it applies and solves t = √(2h/g) in symbols first.
- Recomputed in one script (python -I answers.py beside my own formula): t = √(40/24,79) = 1,2703 s. answers.py, exercises.json and my value agree. Tolerance 0,04 (relative) covers the small differences between tables and a student who rounds to 1,27 s or 1,3 s.
- The check is a real one: on Earth the same drop takes 2,02 s, and √(24,79/9,81) ≈ 1,59 gives 1,27 s.
- Notation as in the chapter: h, g, v₀, x₀, t, and SI units in LaTeX.
- Scope: uniformly accelerated motion from this chapter. Nothing from a later course. It does not repeat L1-03 (distance in a given time, on Earth) or L2-04 (g found from a drop on the Moon).
- Hash 2c1761040ce1f1cd at the start and at the end.
