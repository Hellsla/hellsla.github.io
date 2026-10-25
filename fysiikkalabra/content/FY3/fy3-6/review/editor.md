VERDICT: FAIL
CONTENT-HASH: 435cf1ab9fd1cc9c

The lesson tells one story: the sand hook is answered, the mökki contexts run through the exercises, and the calorimeter sim matches the worked example. Length (843 words, 5/4/3 exercises) matches fy3-3 (829) and fy3-5 (722). The heating/cooling and calorimetry goals are covered. The third goal, solving a multi-term equation, is not: nothing shows how to solve the balance equation for T, which appears in two terms. Only L3-01 uses that equation, and it solves for a mass. Yet the misconception (35 °C) and exit-ticket q3 (65 °C) expect students to find T.

## Blocking
- lesson.md:23 — The lesson says T can be solved but never shows how. — Show the steps (expand, collect T, factor) and give T = (c₁m₁T₁ + c₂m₂T₂)/(c₁m₁ + c₂m₂) in display LaTeX, or work the 35 °C case from line 71.
- exercises.json:46–51 — No exercise asks for T, and L2-01 (pan) nearly duplicates L1-02. — Replace L2-01 with a mixing task for T, masses in grams. Update answers.py and solutions.md.
- lesson.md:8 — C = cm is only inline, against the display-formula house rule. It is also used at line 68, in exit q3 and in the sim. — Add it in display under ## Kaava with C (J/K) named.

## Polish
- lesson.md:17,21 — Line 17 makes Q negative on cooling, but the balance equation uses positive amounts. — Add one sentence saying so.
- lesson.md:10 — The calorimetric measurement procedure gets one sentence. — Name the steps (weigh, measure, transfer quickly, stir, read the peak) and the error sources.
- exercises.json:78–102 — No calorimetric determination from measured data. — Optionally make one level-3 task include the calorimeter's heat capacity.

## Checked
- Lint clean; hash unchanged during review.
- Goals match curriculum.json; glossary terms exist.
- FY3 scope kept; P = W/t comes from fy3-2.
- No exercise repeats the worked example.
- All 12 answers and the exit-ticket answers recomputed and consistent.
- Sim spec fits the lesson's story.
