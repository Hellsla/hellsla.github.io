VERDICT: FAIL
CONTENT-HASH: 31ad7bc4e62fbd77

Delta review over the audit's PASS (901e18a6fefc4a77): new choice check-c2 (rigid vessel 20 -> 40 °C) from the exit ticket, checks renumbered, exit text "kaksi", check-c2 numbers in lesson-answers.py.

## Blocking
- inquiry.json:471 — (A, guardrail "Absolute zero") correct-option feedback: "vasta kelvinasteikon nollakohdassa hiukkasten liike loppuu". The motion does not stop entirely at 0 K; the energy is at its lowest. Fix as in fy3-9: "…koska kelvinasteikon nollakohta on absoluuttinen nollapiste, jossa hiukkasten energia on pienimmillään."
## Polish
- none
## Checked
- T2/T1 = 313,15/293,15 = 1,0682 -> "≈ 1,07", "noin 7 %"; option text 293 K -> 313 K consistent.
- Distractor "kaksinkertaistuu" (40/20) wrong; feedback right.
- Distractor "ei muutu" wrong; p = nRT/V and the kinetic explanation right.
- Distractor "20 %": 20 K / 293,15 K = 0,068 -> 7 %; feedback right.
- Exactly one correct option; rigid, closed vessel stated.
- lesson-answers.py: inq-c2 1,068 and 6,8 % reproduced.
- Removed exit question (doubling T at fixed V) is covered by check-c2; two questions remain; "kaksi" matches.
