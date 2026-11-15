VERDICT: FAIL
CONTENT-HASH: 511f0021bf1d22ba

## Blocking
- content/fi/FY4/fy4-6/exercises/solutions.md:253, exercises.json:85, lessons/FY4/fy4-6/answers.py:36 — (A, assessment/rounding) L1-07 asks for the force that must *at least* (vähintään) be applied. The computed limit is 220,7 N. The answer 2,2·10² N lies below it, and the solution itself says that a smaller push leaves the box at rest. House rule P7 (CLAUDE.md, guardrails "Values and significant figures") rounds a "vähintään" value up: with two figures that gives 2,3·10² N. With answer 220 and tolerance 0,02, a student who follows the rule gets only "Lähellä" (4,5 % off). — Fix: answer 230, rounded up in answers.py (math.ceil to two figures). In Vastaus write "$2{,}3\cdot 10^2\,\text{N}$, pyöristetty ylöspäin, koska $220\,\text{N}$ ei vielä riittäisi". Widen the tolerance to about 0,05 so that 221 N is also accepted.

## Polish
- solutions.md:187 — L3-01 is also a "vähintään" value (0,357 → 0,36). The result is right, but the reason given for the rounding should say it is rounded up to the safe side, not only "kaksi merkitsevää numeroa".
- solutions.md:160 — L2-04 force diagram: it draws the friction at the full lähtökitka 48,2 N together with an acceleration down the slope. Once the box slides, the friction is liukukitka, and μ is not given. Draw a = 0 at the moment of comparison, or write that the arrow shows the upper limit μ₀N.
- solutions.md:57 — L1-03: "tavallinen arvo puulle lattiaa vasten", but the task does not say the box is wood. Write "tavallista suuruusluokkaa".
- L1-05 (exercises.json:238) — the task does not say the box is at rest, yet the diagram draws a = 0 and lepokitka. Add "levossa" to the task (the asked G_x does not depend on it).

## Checked
- One script recomputed all 20 numeric answers with my own formulas. Every one agrees with answers.py and exercises.json to within 0,0–3,3 %, inside each task's tolerance. L2-03 and L2-09 use a least-squares slope through the origin, 0,2145; L2-05 gives 0,416.
- L2-08 order: B 30 N < C 44,1 N < A 58,9 N < D 122,6 N. D's limit 148,7 N > 122,6 N and B's limit 196 N > 30 N, so both boxes really stay at rest.
- L2-06: μ₀ = 0,449 and μ = 0,2945, so μ < μ₀. The data are consistent with sliding at constant speed from 3,5 s.
- L3-04: dry 33,6 m, wet 55,9 m, downhill 73,4 m. The deceleration stays positive because μ > tan 6°. The mass cancels, as the solution states.
- L3-05: the student's 1,47 m/s² comes from the stated error. The correct answers are N = mg cos α, a = 1,93 m/s² and s = 8,69 m. The task's premise that the box slides holds, since tan 30° > μ.
- L1-06 and L1-08: exactly one correct option. Each distractor's feedback gives the right physics, and lepokitka is "only as large as needed".
- The force diagrams: forces are named, friction directions are right (forward in L3-01, down the slope in L3-02), velocity and acceleration are not drawn as forces, and components are dashed. The equations' signs match the diagrams.
- The terms follow the guardrails: liukukitka, lepokitka, täysin kehittynyt lepokitka eli lähtökitka; liikekitka does not appear. The notation follows the brief, and every task stays inside FY4's central contents.
- The figure fy4-6/mittaus gives all five points, its description gives the same values, and no fitted line gives the answer away.
- Content hash is the same at the start and at the end.
