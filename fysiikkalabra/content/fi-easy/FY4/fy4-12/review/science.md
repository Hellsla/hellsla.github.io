VERDICT: PASS
CONTENT-HASH: e6499168f4b2e820

## Blocking
(none)

## Polish
- none

## Checked
- batch delta review: key_concepts, reworded sentences, photo captions, objective-form and level-policy edits, chapter-reference titles judged against the guardrails and the lesson text; restyled figure lines are styling only.
- Delta (figures.json): the 4 new pick-* figure entries (fy4-5: 4 force-diagram descriptions; fy4-12: 4 v(t) graph descriptions plus the re-keyed (t,x) description) compared with the Finnish strings drawn by figures.py; every number, unit, symbol (F, F_k, v, N, G), direction, arrow-length relation and intersection time (6.3 s, 8 s, 4 s) matches; Selkeä suomi text is the Finnish with short sentences, no content change. Lesson content otherwise unchanged (git diff 88e803e touches only figures.json); figures.py up to date, check_i18n clean, build.py fy4-12 builds.
