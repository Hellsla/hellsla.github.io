VERDICT: FAIL
CONTENT-HASH: a58c8532ef458c62

Delta review over the audit's PASS (d990e0039cdcf7a7): new choice check-c2 (Kelvin temperature, rigid bottle 7 -> 35 °C) from the exit ticket, checks renumbered, exit text "kaksi", lesson-answers.py added.

## Blocking
- inquiry.json:424 — (A, guardrail "Absolute zero") check-c2's correct-option feedback says "vasta kelvinasteikon nollakohdassa hiukkasten liike loppuu". At absolute zero the particles' energy is at its lowest; their motion does not stop entirely. Fix: "Suhde lasketaan kelvineinä, koska kelvinasteikon nollakohta on absoluuttinen nollapiste, jossa hiukkasten energia on pienimmillään." (the lint's physics_phrases rule should catch this; check why it did not).
## Polish
- none
## Checked
- T2/T1 = 308,15/280,15 = 1,0999 -> "noin 10 %" and "≈ 1,10"; option text 280 K -> 308 K consistent.
- Distractor "viisinkertaiseksi" (35/7 = 5) wrong, feedback right (Celsius zero not the temperature zero).
- Distractor "28 %": 28 K / 280,15 K = 0,0999 -> 10 %; feedback right.
- Distractor "ei muutu": wrong; kinetic explanation (more frequent, harder hits) right.
- Exactly one correct option; condition (rigid, closed bottle, same volume) stated in the prompt.
- lesson-answers.py reproduces 1,0999, 9,99 %, 5 and 9,99 %.
- Removed exit question is the one converted to check-c2; two remain; text "kaksi" matches.
