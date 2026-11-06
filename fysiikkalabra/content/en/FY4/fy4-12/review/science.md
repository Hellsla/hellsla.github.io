VERDICT: PASS
CONTENT-HASH: 0a55878db96bc149

## Blocking

## Polish

## Checked
- batch delta review: title "Comparing the motions of two bodies" in lesson.md and meta.json matches content/fi ("Kahden kappaleen liikkeiden vertailu") and claims nothing physical (no "ahead"/higher-line wording, so the motion-graph guardrail is untouched); the exercises lead lost only its level-policy sentence, the physics advice (position as a function of time, the (t, x) graph) is unchanged; no option, number or symbol touched; hash bd92cdf23aef6c50 at start and end.

Delta review: leftover Finnish words in en names/labels/sim bar labels/figure caption are now English and match the Finnish meaning; no blocking issue.
- Delta (figures.json): the 4 new pick-* figure entries (fy4-5: 4 force-diagram descriptions; fy4-12: 4 v(t) graph descriptions plus the re-keyed (t,x) description) compared with the Finnish strings drawn by figures.py; every number, unit, symbol (F, F_k, v, N, G), direction, arrow-length relation and intersection time (6.3 s, 8 s, 4 s) matches; English reads naturally with decimal point. Lesson content otherwise unchanged (git diff 88e803e touches only figures.json); figures.py up to date, check_i18n clean, build.py fy4-12 builds.
