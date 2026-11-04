VERDICT: FAIL
CONTENT-HASH: e6d018827d4ef414

## Blocking
- content/fi/FY1/fy1-1/exercises/solutions.md:176 (L2-07, B) — "yhden arkin paksuuden epävarmuus on vain noin 0,001 mm" is stated as the uncertainty of the sheet thickness, but it is only the reading contribution (0,25 mm / 300). The task itself names a method effect (the stack pressed by hand), the points scatter about ±0,3 mm round the fit, and line 175 of the same solution gives 0,10 mm with two figures and accepts 0,097–0,107 mm. The 0,25 mm sentence also lacks the guardrail condition. — Fix: use the guardrail wording ("lukeman epävarmuutta voidaan yksinkertaisessa tilanteessa arvioida …"), call 0,001 mm *lukeman osuus* yhden arkin paksuudessa, and add that pressing the stack, air between the sheets and the eye fit make the total uncertainty larger, which is why the answer has two figures.

## Polish
- lessons/FY1/fy1-1/answers.py:41 (L3-05) — uses 1 AU = 149 597 870,7 km, while the task gives 1,496·10⁸ km. The result is the same (143,16 AU), but the comment's 23,47 AU differs from the solution's 23,46 AU. Use the task's value.
- content/fi/FY1/fy1-1/exercises/solutions.md:171 (L2-07) — the line is read at (300; 30,5 mm), which is also a raw point. That is allowed (the fitted line passes through it), but one sentence saying the value is read off the line, not taken from the table, would match the guardrail.

## Checked
- Recomputed all 19 numeric answers in one script from the task text: every one agrees (e.g. L2-07 slope 0,1019 mm; L3-04 1,194·10⁹; L3-05 143,16 AU).
- L1-06: exactly one correct option; each distractor's feedback is right, and model, prediction and test are defined as in the glossary.
- L2-06: the order-of-magnitude rule (a > about 3 → 10ⁿ⁺¹) matches the glossary; 9,46·10²⁰ m → 10²¹; Δn = 21.
- L2-07 data: residuals −0,09…+0,31 mm, consistent with reading to 0,5 mm; the origin has a physical reason (zero sheets, zero height).
- L3-04: assumptions stated in the task; the sensitivity 1,2³ = 1,73 → −42 % is right; 20 drops/cm² is plausible.
- L3-05: t = 7,25 a fits 2018-11-05 → Feb 2026; the student's error (km/s · a, adding km to AU) is identified correctly; "supports but does not prove" is worded well.
- Rounding: every stated figure count follows from the limiting datum, and each shown value lies within the tolerance.
- Old 12: unchanged apart from the typography; scope within FY1.
