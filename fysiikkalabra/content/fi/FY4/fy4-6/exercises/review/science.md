VERDICT: PASS
CONTENT-HASH: 83e11ade6985ea12

## Blocking

## Polish
- solutions.md:160 — L2-04 force diagram: it draws the friction at the full lähtökitka 48,2 N together with an acceleration down the slope. Once the box slides, the friction is liukukitka, and μ is not given. Draw a = 0 at the moment of comparison, or write that the arrow shows the upper limit μ₀N.
- solutions.md:57 — L1-03: "tavallinen arvo puulle lattiaa vasten", but the task does not say the box is wood. Write "tavallista suuruusluokkaa".
- exercises.json (L1-05) — the task does not say the box is at rest, yet the diagram draws a = 0 and lepokitka. Add "levossa" to the task (the asked G_x does not depend on it).
- exercises.json (L1-07) — tolerance 0,05 around 230 accepts 218,5–241,5 N. Unrounded 221 N is accepted, as intended, but so is 220 N, which is below the limit. This is lenient, not wrong; the solution states the rule.

## Checked
- Round 2 judged the diff since 3a8e80c783 and what it touches.
- L1-07 is fixed. answers.py computes ceil(220,7 N to two figures) = 230. exercises.json has 230 with tolerance 0,05. The Vastaus says the value is rounded up because 220 N would not yet be enough, as P7 requires.
- L3-01: the Vastaus now says "vähintään 0,36" and gives the reason for rounding up. 0,357 → 0,36 is right.
- Terminology: "enimmäisarvo" became "lähtökitka" in the L1-06 options, its feedback and model answer, and in the principles of L1-07, L2-06 and L2-07. This follows the guardrails, and each option's correctness is unchanged (exactly one correct).
- One script again recomputed all 20 numeric answers with my own formulas. They agree with answers.py and exercises.json within tolerance; L1-07's computed 220,7 N lies inside the tolerance band around 230.
- Nothing else in the set changed. My round-1 checks of the other tasks' physics, force diagrams, figure, scope and terms stand.
- Content hash is the same at the start and at the end.
