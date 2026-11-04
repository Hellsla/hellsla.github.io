VERDICT: FAIL
CONTENT-HASH: b0233d6033e9c661

## Blocking
- content/fi/FY4/fy4-16/exercises/exercises.json:255 (L2-07, B) — the method "nostaa laudan toista päätä hitaasti, kunnes laatikko liukuu tasaisella nopeudella" measures the angle where the box starts to slip, which is set by static friction (μ_s > μ_k); once it slips it speeds up, so tan α of that angle is not the kinetic coefficient the task asks for — add the missing step, for example "Jokaisella kulmalla laatikkoa tönäistään kevyesti liikkeelle, ja kulmaa säädetään, kunnes laatikko jatkaa liukumista tasaisella nopeudella", and add the same condition to the Periaate in solutions.md.

## Polish
- content/fi/FY4/fy4-16/exercises/solutions.md:290, 305 (L2-07) — "virhemarginaali" and "μ = 0,321 ± 0,015" present half the range of five repeats as an uncertainty; the guardrails call this a simple estimate of the scatter — call it "vaihteluvälin puolikas (hajonnan yksinkertainen arvio)" and give μ ≈ 0,32 ± 0,02.
- content/fi/FY4/fy4-16/exercises/exercises.json:209 and solutions.md:272 (L2-06) — "liikkeessa" → "liikkeessä".
- L3-05 Vastaus — "kolme merkitsevää numeroa kuten … nopeuksissa": 7,9 m/s has two; 2,2 kN would follow the rule (the answer box is unaffected). The trapezoid sum slightly overestimates the distance (Simpson 54,8 m, F_v = 2,23 kN, inside tolerance).
- Plan (docs/exercise-bank/FY4.md): "ilmanvastuskertoimen arvio" became the mean air resistance in L3-05, and the phone-sensor lift figure became the video table in L2-05; both are fine physics for FY4 (no F = kv² in the lesson), so update the plan line.

## Checked
- All 20 numeric answers recomputed in one script and from answers.py: all agree (L2-05 fit 0,400 m/s², 633 N; L2-06 quadratic fit μ = 0,081; L3-04 16,33 m, 7,67 m/s; L3-05 55,6 m, 2,205 kN, (c) 851 N > 765 N).
- L2-06 data fit constant deceleration and the sled still moves at 5,0 s.
- L3-04: energy equation, tan 14° > μ_1, 5,0 m margin and mass cancelling all right.
- L1-06, L1-07: exactly one correct option; distractor feedback right.
- L1-08 and the force-diagram blocks: right forces, a drawn apart from forces.
- Scope inside the lesson; no duplicates; level 3 tasks are multi-part modelling/data tasks.
- Hash b0233d6033e9c661 at the start and at the end.
