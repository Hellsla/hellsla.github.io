VERDICT: PASS
CONTENT-HASH: 33e3e35d87b23337

The lesson now delivers all three goals and tells one story. Heating and cooling are covered by Q = cmΔT and five level-1 tasks. The calorimetric measurement is covered by the worked example, the sim defaults that reproduce it, and the balance equation. The multi-term-equation skill was missing in round 1 and is now taught explicitly: under ## Kaava the equation is expanded, the T terms are collected and T is factored out. The result is displayed as a weighted mean, and the 35 °C misconception and exit-ticket q3 both rely on it. L2-01 (water–water, grams) and L2-04 (aluminium–water) practise solving for T. L3-01 solves the same equation for a mass. C = cm has its own display and is used consistently in the text, the exercises, exit q3 and the sim readout. The lesson is the longest in FY3 (986 words without the SVG; fy3-3 to fy3-5 run 601–861). The extra length is the derivation the goals require, so it is acceptable.

## Blocking
(none)

## Polish
- lesson.md:87 — The paragraph is about 140 words and does three jobs: significant figures, identifying the metal with the loss explanation, and comparing heat capacities. — Split it after "ilmaan." so the heat-capacity comparison stands as its own short paragraph.
- lesson.md:99 — "Toisella rivillä yhtälö on jaettu puolittain kilogrammalla" leaves out that the brackets were also multiplied out on that line. — Write "jaettu puolittain kilogrammalla ja sulut kerrottu auki".
- exercises.json:78–102 — No exercise asks for c from measured calorimeter data, so the experimental goal is practised only through the worked example. — Optional: rewrite one level-3 task as a determination of c that includes the vessel's heat capacity or a loss estimate.

## Checked
- Lint clean (0/0). Hash unchanged from start to finish of the review.
- The goals in meta.json match curriculum.json, and each goal has theory, exercises and a sim or exit-ticket check.
- The display at lesson.md:31–41 is algebraically correct, and the weighted-mean statement at line 42 matches the 50 °C/65 °C cases in exit-ticket q3.
- C = cm is displayed once with C (J/K) named. The sign convention (Q < 0 on cooling, positive amounts in the balance) is explained at line 29.
- L2-01: (160·95 + 40·8,0)/200 = 77,6 → 78 °C. L2-04: 51 543/1901 = 27,1 → 27 °C. Both are consistent with answers.py.
- No exercise repeats the worked example (a determination of c). L2-01 is distinct from the old pan task L1-02.
- Sim defaults (0,30 kg water at 20 °C, 0,200 kg copper at 100 °C) give 24,6 °C, as line 87 claims. L2-04 is reachable within the slider ranges.
- FY3 scope kept: P = W/t in L2-02 comes from earlier FY3 lessons, and there are no phase changes (those belong to fy3-7).
