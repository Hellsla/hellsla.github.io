VERDICT: PASS
CONTENT-HASH: 177053466bf26f9c

## Blocking

## Polish
- content/fi/FY4/fy4-5/exercises/exercises.json:153 (L1-09 option D) — now that v is blue, D can read as "C plus an allowed velocity arrow"; the error is that the arrow sits on the box and is drawn like a force (thick, filled head, from the face) — say so in the feedback ("nuoli lähtee laatikosta ja on piirretty voiman tavoin") and in the pick-nopeus description (lessons/FY4/fy4-5/figures.py:402: "paksu, umpikärkinen kuten voimat"), so a screen-reader user can tell it from a correct drawing too.
- Carried from round 1: options A, B, D lack the F-to-G ratio sentence that C's description has; stem names option B's F_k error ("laatikon voima työntäjään"); label N on the box's top edge (visual's call); L2-05, L2-07, L1-07 and "Taulukon lukeminen" items.

## Checked
- Round 2, delta since commit 5a93acbfc (packet generated in full mode; reviewed the change against the round-1 PASS): L1-09 option D figure and feedback only.
- Figure from the code (SVG built in memory, not written): the velocity arrow uses VELOCITY #1971c2 (line, head, label), the four forces stay FORCE red; the description now says "sininen nopeuden nuoli v". Follows the house rule force red, velocity blue.
- D is still unambiguously wrong: the taught rule (solutions L3-01, L2-06, L3-05; docs/force-diagrams.md) puts the thin blue v beside the diagram, never on the body, and YO 2025 marks velocity drawn on the body −5. D's arrow starts on the box face.
- New D feedback is correct physics: velocity is not a force, has no cause, belongs beside the diagram. The correct option C's feedback is unchanged and gives no extra reason.
- Distractors each keep one error (A push 2 × friction, B third-law partner on the box, D velocity drawn on the box); exactly one correct option.
- answers.py run once: all 18 numeric answers within tolerance; the 3 multiple-choice tasks each have exactly one correct option.
- Not re-rendered this round; checked from the code, the SVG text and the feedback.
- Hash 177053466bf26f9c at the start and at the end.
