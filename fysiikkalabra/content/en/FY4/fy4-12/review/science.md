VERDICT: PASS
CONTENT-HASH: c6e3189dc252a922

## Blocking

## Polish
- lesson.md:381 (and :214, inquiry.json `contribution`) — "When the one behind starts slower, the lead is greatest when the velocities are equal" is true only when the one behind then speeds up past the other one. Two uniform motions with the slower one behind give no greatest lead. The context implies the condition. — e.g. "When the one behind starts slower and then accelerates, …".
- lesson.md:155 — "If one of them accelerates, the equation is quadratic" — the equation is linear when both bodies have the same acceleration. — "If their accelerations differ, …".
- assets/sims/fy4/fy4-12/sim.js:209 — `tx()` always uses a decimal comma, so the English readout shows "10,0 m" (see the 1280 px screenshot). — Use the page language's decimal separator.
- assets/sims/fy4/fy4-12/sim.js `simState.meetings` — the column counts the meetings up to `tmax` (the latest moment visited), not up to the current `t`. If a student records exp-3 out of time order (for example 7 s and then 2 s), the 2 s row shows 2 meetings. — Count `m <= tau`, or tell the student to record the moments in time order.

## Checked
- I recomputed everything in one script with my own formulas: sim cases 1, 3, 4 and 5 (10 s/50 m; 8.0 s/64 m/16 m/s with root −2.0 s; −10 s; 1.55 s and 6.45 s), the figure cases (12 s/36 m; 6.0 s/36 m/12 m/s), the greatest leads (25 m and 9 m), siirto 24 m/s (mistake values 12, 96 and 8), check-2 6.0 s (mistake values 15, 30 and 10) and the recall item 25 m. All agree with lesson-answers.py and the texts.
- The figures tilanne, kohtaus, kaava, vt, esimerkki and ei-kohtaa are to scale: I checked the axis pixel scales, the intersections, the shaded areas of 9 m each and the 3:2 arrow lengths.
- In the worked example the symbols come first (x_A = x_B, the quadratic formula, the positive root), the substitution is right, the two significant figures are justified, and the negative root is discussed.
- pred-1 to pred-3, exp-3, ei-kohtaa, virhe and check-1 each have exactly one correct option. Every distractor is wrong, and its feedback gives the right numbers.
- Experiments: `tapaus` is locked and `t` is varied. The simState keys xA, xB, vA, gap and meetings exist, and the 0.5 s slider steps reach 10 s and 8.0 s.
- sim.js: pos and vel follow the constant-acceleration model. `meetings()` solves the quadratic or linear equation and keeps 0 < t ≤ 12 s. Since the last review the sim changed only its layout (f9955f0b8b), not its physics.
- The model box states the assumptions: point bodies that pass through each other, no friction or drag, and acceleration from the start.
- The (t,x) "higher line" wording follows the guardrail: it says "larger position coordinate" and gives the direction condition.
- The exit ticket, conclusion and check-3 model answers agree with the theory: a meeting means equal positions, and equal velocities give the greatest lead.
- The content stays within FY4's central contents (uniform and uniformly accelerated rectilinear motion).
