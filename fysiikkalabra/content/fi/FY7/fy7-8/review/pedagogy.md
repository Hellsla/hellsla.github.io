VERDICT: PASS
CONTENT-HASH: 072bc679bb45dcdc

## Blocking

## Polish
- lesson.md "Jännite lasketaan vaiheittain" — first paragraph is about 125 words and holds grid steps, the safety reason and 400 V/230 V; the charger paragraph is already separate — split the grid steps from the safety reason.
- inquiry.json `ennuste-jannite` — the prompt asks only about the factor, while the experiment records three voltages; consider asking the student to justify with the current ("virta puolittuu") before the evidence. This is optional, since `justify` already does it.
- inquiry.json `tarkistus-2` — a student who computes the secondary current first and then uses `U₁I₁ = U₂I₂` is well served; the third hint could name this route. Taste only.

## Checked
- Learning path: prior (induction, AC from fy7-7) is retrieved, the opening question is answered only after commitment, and the goals (transformer, transmission) are covered and no more.
- Ennuste 1 (battery) is a real misconception test, revealed after the theory. Ennuste 2 is refutable by the Koe 1 table, with a locked `P` and `l` and a varied `U`.
- Each wrong option's feedback repairs its misconception (U²/R, "halves", "power added", "voltage passes through iron"). The feedback uses model values and does not restate the answer.
- Simulation: the model is stated (two conductors, ideal transformers), and the text sits in Käyttöohje, Mallin oletukset and Laskennan selitys. The result emerges from the model's current, so it is mild but acceptable.
- Worked example has seven stages with one step each, symbolic before numeric, with a reasonableness check.
- Etsi virhe and the wind-farm transfer task have three hints and common-mistake feedback. The unit-slip mistake is real (MW vs kW).
- The exit ticket tests the core ideas (turns ratio, I²). The explain criteria are observable and match the prompt.
- Figures: the 360 px captures are legible. The loss graph's description gives the data. The 3-phase caveat is placed at the point of use.
- Workload is about one lesson. Finnish is correct (case after number+unit, glossary terms, loss as internal energy transferred as heat).
