VERDICT: PASS
CONTENT-HASH: 169cf2ec47db5201
## Blocking
(none)
## Polish
- solutions.md:90–93 — L3-03 writes subscripts as `Q_A`, `W_B`, `ΔU_A`, while L3-02 (line 84) uses Unicode `W₁`; no capital Unicode subscripts exist, so keep them, or use `Q(A)` / `Qᴀ`-free wording such as "tavan A lämpömäärä". Only cosmetic: with `meta.solutions` defaulting to `first`, this solution is not published.
## Checked
- Hash 169cf2ec47db5201 before and after; lint 0/0 and check_latex ok, not repeated
- ΔU = Q + W sign convention identical in lesson.md:15–17, all 12 solutions, answers.py header and exit ticket 1
- Worked example lesson.md:41 −40 J + 150 J = 110 J; remark :43 now "sama 150 J:n työ", so Q = −150 J and ΔU = 0 follow exactly
- L1: 570 J, −8,4 kJ, 250 J, −500 J, −70 J; L2-01 W = 60 J, Q = −15 J; L2-02 180 kJ − 20 kJ = 160 kJ; L2-03 Q = −1200 − (−2000) = +800 J
- New L2-04 (solutions.md:65–71): W = ΔU − Q = 12 kJ − 2,0 kJ = 10 kJ, t = W/P = 10 000 J / 250 W = 40 s; signs and kJ→J conversion correct
- L3-01: wording "mäntä työntää ilmaa … 120 N:n voimalla" makes W = Fs = 18 J exact; ΔU = 0 ⇒ Q = −18 J
- L3-02: 12 · 5,0 · 9,81 = 588,6 N, h = 1000/588,6 = 1,699 → 1,7 m, rounded only at the end
- New L3-03 (exercises.json:98, solutions.md:89–95): ΔU_A = 400 − 150 = 250 J, ΔU_B = ΔU_A (same gas amount, same initial and final temperature), Q_B = 250 − (−60) = 310 J; sanity check 310 J < 400 J consistent
- Exit ticket: 1 → 300 J − 120 J = 180 J; 3 → system "termospullo ja sen sisältö" now isolated, so its U is constant while the coffee's U falls and the inner wall's and air's rise equally (lesson.md:10)
- SVG lesson.md:19–34: moved label at x=414 start, 22 px measures 148 px (Liberation Sans) / 174 px (DejaVu Sans), so it spans 414–588 inside the 600 viewBox and clears the box stroke (≤ 401,5); baseline 138 stays above the arrowhead top (528,140) and dashed line (y = 150); arrow tips at x = 200 meet the box, line ends hidden in arrowheads; box formula matches lesson.md:15
