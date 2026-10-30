VERDICT: PASS
CONTENT-HASH: f0b58932dae878ef

## Blocking

## Polish
- lesson.md:216 — "T supistuu pois, koska lanka on kappaleiden välinen sisäinen voima": T is the string's force on each body, and the two equations are along different directions (the pulley turns them). Better: "koska $T$ esiintyy yhtälöissä vastakkaisin etumerkein".
- lesson.md:407 / exit-ticket.json:4 — "Ne vaikuttavat eri kappaleisiin *mutta* kuuluvat eri vuorovaikutuksiin": a force and its counterforce also act on different bodies, so "mutta" suggests a contrast that is not there. The decisive point is the different interactions. Better: "Ne kuuluvat eri vuorovaikutuksiin: …".
- Carried over from round 1, for the pedagogy reviewer: the sim readout shows ΣF₁ and ΣF₂, so the exp-1 and exp-2 numeric questions can be read off. The physics is right.

## Checked
- Round-1 blocker fixed: there are no TAB characters left in any lesson file. The summary formulas are `\frac` and correct. Round-1 polish done.
- Recomputed every number in the lesson and inquiry in one script (scratchpad rc.py), using my own formulas: Esimerkki 2,80 m/s² and 4,20 N, net force 1,68 N; pred-1 3,27 N; exp-1 1,635 N and T 2,45/3,27/3,68 N; pred-2 and exp-2 3,68 N and 0,736 N; aineisto 2s/t² → 3,27 N; siirto 0,3073 kg; check-1 3,3; check-2 3,363 N; check-3 3,27 m/s² and 5,23 N. Each mistake value (0,2446; 0,2032; 4,48; 5,61; 7,85; 1,63) matches the error that its feedback names.
- Choices: kertaus, pred-1, pred-2, virhe and check-1 each have exactly one correct option, and each distractor's feedback is physically right.
- Force diagrams (tilanne, esimerkki, atwood, malli-atwood, virhe, sim): one diagram per body, each body a rectangle, G from the centre, N from the contact surface, T from the attachment point. T₁ = T₂ in length and stated *not* to be a third-law pair. v and a are drawn beside the bodies. virhe has exactly one error (G₂ on the cart).
- sim.js implements both models, including m₁ > m₂ through dir. exp-1 and exp-2 lock tapa and m2 and vary only m1, and simState carries T, a and G1.
- The model's conditions (light, inextensible string; light, frictionless pulley; no friction or air resistance) are stated in the theory, Esimerkki, the sim model box and every task.
- Scope: FY4 "voimakuvio ja liikeyhtälö", slot example F.
- Hash f0b58932dae878ef at start and end.
