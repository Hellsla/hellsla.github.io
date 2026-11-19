VERDICT: PASS
CONTENT-HASH: 338baa44a2d54eaa

## Blocking
(none)

## Polish
- inquiry.json check-3 (Selitä) — the model answer repeats the lesson's section "Vastaus alun kysymykseen" almost word for word, so the check is recall, not a new situation. Fix: ask about a new pair, e.g. a /bin/bash{,}20\,\text{kg}$ ball hitting a /bin/bash{,}60\,\text{kg}$ ball at rest.
- inquiry.json siirto prompt — "nopeudella $2{,}4\,\text{m/s}$ laituriin (maahan) nähden" is clumsy. Fix: "nopeudella $2{,}4\,\text{m/s}$ maahan nähden".
- inquiry.json hook — "Jos punainen pallo olisi raskas keilapallo, lyöntipallo kimpoaisi takaisin" gives away the mass dependence that exp-2 is meant to reveal. Fix: put it in the question as "entä jos...?" or drop it.
- lesson.md "Täysin kimmoton törmäys" — the sticky-cart example (0,40 kg, 0,60 m/s) is the same as pred-1 and exp-1 and gives the result before the experiment is done. Fix: it is behind the prediction gate, so move it to the worked example or change its numbers.
- fig "tyypit" (390 px) — in the explosion row, the label \text{kok}=0$ sits tight against the carts and is pale. Fix: raise it and darken it.

## Checked
- Learning path follows from fy4-9 impulse and Newton III: system, internal and external forces, the conservation condition, collision types, explosion.
- The opening question is answered by the elastic derivation v_1'v_2'=0$ in the lesson, and check-3 asks it again.
- Predictions can be refuted: the sim's model values, with buffer forces computed from compression, give the figures the feedback quotes (0,30 m/s; 0,80/0,20/-0,12 m/s; 0,63 and 1,26 m/s). I recomputed them.
- Variable control: only m2 varies in exp-1 to exp-3, and the others are locked. The experiment questions' distractors are misconception-based (no sign, energy conserved, braking removes momentum).
- Core path is one hour: exp-3, reflect, Etsi virhe and pred-3 are optional.
- The worked example has seven stages with sensible numbers (38,3 to 32,5 kJ, 15 %). Its same-direction case differs from the check-2 and virhe tasks (opposite directions).
- The siirto hints go from system to explosion to formula, and the mistake values (2,4; 0,706; 5,76) are real errors.
- Figures: the hero, vuorovaikutus and tyypit are legible at 390 px with meaningful colour. The simulation at 390 px has Käyttöohje, Mallin oletukset and Laskennan selitys behind closed boxes and a short visible text.
- Finnish and glossary terms (kimmoisa, kimmoton, räjähdys, sisäenergia) are correct. The exit ticket tests the condition and a new explosion case.
- The exercise set was not judged (reviewed separately).
