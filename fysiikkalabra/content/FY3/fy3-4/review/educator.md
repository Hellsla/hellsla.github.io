VERDICT: PASS
CONTENT-HASH: c81585f20e7bd942

## Blocking
(none)

## Polish
- lesson.md:3 — the dam question is never answered; the student must combine lines 8 and 10 alone. — Close the loop as fy3-1 does, after line 12: "Tämä vastaa alun kysymykseen: yläreunassa veden ylipaine on nolla, pohjalla suurin, joten muurin alaosaa painaa paljon suurempi voima."
- lesson.md:10 — "paine vaikuttaa joka suuntaan yhtä suurena" is only asserted, yet line 8 explains only the downward push of the water's weight, and the dam needs the sideways push. — Add one reason: "Jos paine sivulle olisi pienempi, vesi valuisi sivuun; pullon kyljen alimmasta reiästä vesi suihkuaa kauimmas."
- lesson.md:8 — "massa ρAh" uses m = ρV silently and names ρ only afterwards; two steps in one breath. — "Tiheys ρ on massa tilavuutta kohti (FY1: m = ρV), joten patsaan massa on ρAh ja paino G = mg = ρAhg."
- exercises.json:72 (L2-04) — repeats the example's second half (overpressure × area, cm² conversion) and adds bar and kN conversions, more than level 2 allows. — Give the overpressure as 85 kPa or the area in m², or make the student form the overpressure from two given pressures.
- meta.json:14 — "ylipaine" is a key term (lesson.md:25, 51, 54; L2-02, L2-04, L3-03) but missing from `glossary.json` and the meta glossary. — Add it to both.

## Checked
- lint_lesson.py fy3-4: 0 errors, 0 warnings.
- Prerequisites available: G = mg (fy3-1), gas micro-model and Pa/kPa (fy3-3), density (fy1-7).
- Skill goal p = p₀ + ρgh is linked to fy3-3's p = p₀ + kθ and FY1's y = kx + b.
- Motivating question and the nail/ski hooks are concrete, student-level questions.
- meta glossary drops "noste" (MAOL puts it in FY4, not treated here): correct.
- Level 1: five single-formula tasks with the values given.
- Level 2: L2-01–L2-03 each need one conversion or rearrangement.
- Level 3: G = mg with p = F/A, Pascal's barrel with a distractor, and two liquid layers.
- All 12 answers recomputed; significant figures match the data.
- Exit ticket tests the three core ideas: force vs pressure, p₀ + ρgh, and shape independence.
