VERDICT: FAIL
CONTENT-HASH: 4ae84ded355a8eeb

## Blocking
- fy5-8/exercises/exercises.json:286, solutions.md:241 (L3-05) — A, internal contradiction: the task says "jänteen ja jousen massa jätetään huomiotta", but c) asks where the lost 27 % went and the model answer puts it into "jousen ja jänteen liike-energiaan, värähtelyyn" — energy a massless spring and string cannot carry. The assumption is not needed — delete "ja jänteen ja jousen massa jätetään huomiotta" from the task and "että jousen massa on pieni" from the Vastaus (keep the Hooke-line assumption).
- fy5-8/exercises/solutions.md:147 (L1-08) — A, wrong reading of the figure: "(0,10 m; 2,5 N)" is called a ruudukon piste, but ex-kaksi has gridlines at whole newtons, so 2,5 N lies between gridlines (screenshot 1280-8), as is the check point (0,050 m; 1,25 N). Use the real grid points of line B: (0,08 m; 2,0 N) or (0,12 m; 3,0 N), and (0,04 m; 1,0 N) for the check.

## Polish
- solutions.md L3-04, L3-05 and exercises.json:245, 286 — "Hooken laki" is not a term of this lesson (it says harmoninen voima, F_v = kx); write "harmonista voimaa F_v = kx" or define the name once.
- exercises.json:66 (L1-06, option 3 feedback) — B: "eikä jousi palaa enää lepopituuteensa": past the proportional range a spring may still return; write "eikä jousi välttämättä palaa".
- solutions.md:162 (L2-05) — Vastaus says 24 N/m (two figures) while the line and the answer field give 24,4 N/m and the scatter is about ±2 %; make them agree.
- solutions.md L3-04 — a rubber band returns less energy than the stretching work (hysteresis); say "venyttävän voiman tekemä työ" for what the area gives.
- exercises.json:105 (L1-08) — same figure and skill as L2-04 step 1, and its Järkevyys reveals k_A = 60 N/m; consider another figure.

## Checked
- One script recomputed every new answer: L1-08 25 N/m, L2-05 24,40 N/m (LSQ through origin, intercept ≈ 0), L2-06 24,53 N/m, L2-07 0,60 J, L3-04 0,255 J (Hooke from first point 0,36 J, +41 %), L3-05 73,05 % (answers.py 73,15 %) — all within tolerance.
- L2-05 F/x 23,9…24,8 N/m for 100–400 g, 22,3 N/m at 500 g: exclusion argued and not deleted, per guardrails.
- L3-04 F/x 50, 37, 31, 33 N/m; trapezoids right; L3-05 F/x 295…307 N/m, Hooke fair.
- L1-06, L1-07: one correct option each.
- L2-06 error (length vs extension) and L2-07 (same force → softer spring stores more) correct.
- Scope and notation (F_v, k, ½kx²) as in the lesson.
- Hash identical at start and end.
