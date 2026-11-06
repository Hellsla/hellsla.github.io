VERDICT: PASS
CONTENT-HASH: ae1ef4425b8ef94d
Round: 1

## Blocking
(none)

## Polish
- exercises.json:273 (L2-08) — the five example points lie within 0,16 kPa of the fitted line although Δp = 1,0 kPa; the set is labelled esimerkkiaineisto, so not an error, but a little more scatter (as in the lesson's example) would make the "within the uncertainty" judgement less artificial.
- lessons/FY3/fy3-13/answers.py — no comment that L2-08 is multiple choice with no number (fy3-14..16 and FY2 note this); add one line.
- solutions.md:237 (L3-05) — "desimaali annetaan, jotta tulos vastaa vastauskentän arvoa" is not a physics reason (carried over).

## Checked
- Recomputed in one script: Δp(60–20 °C) = 13,5 kPa; Δp(22–20 °C) = 0,8 kPa < Δp; intervals 101,0–103,0 / 101,8–103,8 overlap, 101,0–103,0 / 114,5–116,5 disjoint; least-squares line k = 0,3365 kPa/°C, p0 = 95,27 kPa, p(−100 °C) = 61,6 ≈ 62 kPa; −100 °C is 120 °C below the range. All numbers in options, feedback and solution agree.
- Exactly one correct option; each distractor really wrong and its feedback right: overlap = "ei voi osoittaa", not "ei eroa" (guardrail "cannot be shown ≠ equal"); extrapolation as estimate, not certain (the chapter's own warned mistake "nollapiste on mitattu").
- Correct option not identifiable by form: options 1 and 3 have the same structure, option 2 also cites the uncertainty; option 4 alone says "varmasti" but is wrong.
- Conditions stated: closed rigid bottle, temperature uncertainty negligible; data labelled as example data; "todennäköisesti todellista" wording per guardrail.
- Notation (p, θ, Δp, kPa, °C) as in the lesson; within fy3-13 and fy3-3.
- Renders: measured at 390 px in Chromium (preview/fy3-13.html, all feedback and solution opened): widest inline formula 299 px (115,5 − 102,0 = 13,5 kPa), within ~300 px; rest ≤ 120 px. Physics judged from text.
- Hash identical at start and end.
