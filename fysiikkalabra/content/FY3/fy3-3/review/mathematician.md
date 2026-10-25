VERDICT: PASS
CONTENT-HASH: 536cade809f2b051

Round 3. All 15 solutions recomputed in Python (python3 -I). Every exercises.json `answer` equals the solutions.md final answer. Correct-student routes (273 vs 273,15, rounded intermediates, rounded slope) all stay within tolerance 0,02. check_latex.py: all LaTeX ok. SVG geometry in lesson.md matches the table (x: 1,25 px/°C, 0 °C at 445; y: 1,5 px/kPa, p=0 at 250; all points within 0,5 px; dashed line ends at (107,250) = −270 °C).

1. content/FY3/fy3-3/exercises.json (L2-03) — minor, no action needed — exact route 92,857 kPa -> 93. Routes with slope 0,286 / 0,29 / 0,2857 give 92,3–92,9 (pass); slope rounded to 1 sf (0,3) gives 92,0 from the 10 °C point (pass) but 91,0 from the 80 °C point (fails by 2,2 %). One-sf slope is not correct rounding for 2–3 sf data, so no FAIL — correct step: keep slope with at least 2 sf (0,29 kPa/°C).
2. content/FY3/fy3-3/solutions.md:61 — verified: k = 20/70 = 0,2857 kPa/°C; p = 110 − 17,14 = 92,86 kPa -> 93 kPa; sanity text correct.
3. content/FY3/fy3-3/solutions.md (all other tasks) — verified: 294,15; 76,85; −195,75; 25; −270,45; 59,85; 101,55 (L2-02, 102 kPa); T-ratio 3,9955 -> 4,0; 320,82 -> 321; 127,05 -> 127; −126,575 -> −127. All match `answer`.
4. content/FY3/fy3-3/exit-ticket.json — verified: 283 -> 293 K is 3,5 %; 0 K = −273 °C (−273,15 exact).
5. content/FY3/fy3-3/lesson.md:52,61,67 — verified: k = 0,37 kPa/°C; −100/0,37 = −270,3 -> ≈ −270 °C; 293/283 = 1,035.

CONTENT-HASH rechecked at end: 536cade809f2b051 (unchanged).
