VERDICT: PASS
CONTENT-HASH: b92c444bea98ff05

## Blocking
(none)

## Polish
- inquiry.json pred-2 (correct feedback) — "Kaksi lamppua vastustaa virtaa enemmän kuin yksi" uses resistance, which the student has not met; the prediction is a guess with no basis the student could argue from. Fix: add one sentence to the prompt ("lamppu vastustaa virran kulkua; mitä enemmän vastusta silmukassa, sitä …") or name it as a pre-view of the next chapter.
- Slot skill "kytkentäkaavioiden laatiminen" — in the lesson itself the student only reads (symbol figure) and picks (Etsi virhe, check-3) a diagram; drawing is left to the exercises. Fix: have the siirto or one check ask the student to sketch the circuit (or say in the Tehtävät text that level 1 starts with drawing).
- inquiry.json exp-1/exp-2 — Q_A = Q_B holds by construction of the model (the model box says so honestly), so no experiment can refute the wrong options; the lesson relies on the claim "real ammeters give the same". Fix: one sentence in the johtopäätös model answer that the real check is a real ammeter before and after a lamp (fy6-2 does this).
- lesson.md "Virran suunta" — one dense paragraph (conventional direction, electron drift, why the lamp lights at once). Fix: split into two, the second starting "Miksi lamppu syttyy heti?", so the hero question's answer is findable.
- inquiry.json check-3 — options have empty `text`, so a screen-reader user depends on the figure descriptions alone. Fix: add a short text such as "Kaavio, jossa on kaksi lamppua ja kytkin silmukassa" per option, without giving the answer away.

## Checked
- Path from prior (energy conservation) to current to voltage to diagram is followable; hook question answered in Virran suunta, Virtapiiri, check-1.
- Predictions precede evidence; wrong-option feedback repairs the misconception; exp-1/exp-2 lock and vary correctly, min 2.
- Opening question not answered before commitment; reveal follows experiments.
- Worked example: eight stages, one step each, units converted, estimate in Järkevyys.
- Etsi virhe, siirto (432 kJ, both mistake values check out) and check-2 follow-ups are correct and not a copy of the example.
- Exit ticket tests the core ideas (johde/eriste, U = E/Q, current direction).
- Figures (captures #3–#13) legible at 390 px; colours carry meaning (blue electrons, violet current) with labels; symbols match IEC.
- Finnish: no case or term errors found; glossary terms used as defined.
- Phone: sim controls and readout (#2) unclipped.
- Workload: optional items kept optional; fits one lesson.
