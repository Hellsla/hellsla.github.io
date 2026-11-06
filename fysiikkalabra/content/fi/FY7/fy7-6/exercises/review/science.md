VERDICT: PASS
CONTENT-HASH: 958094b9ba257773
ROUND: 1

## Blocking

## Polish
- exercises.json:263 (L2-08, correct choice) — the feedback "hylkivä voima niin kauan kuin käämin virta kasvaa" names the repulsion and the growing current, which points at reason 3 before the reason stage is answered (FY3 lesson) — shorten to "Oikein: rengas hypähtää ylöspäin." and leave the mechanism to the reason feedback.
- exercises.json:251 (L2-08) — with an air-core coil and a battery the jump is real but small; the classic Thomson ring uses an iron core. Optional: "käämin sisällä on rautasydän" makes the "hypähtää" outcome realistic without changing any option (C, a fair simplification as written).

## Checked
- New task only (git diff b032dcb83~1..HEAD: additions only, the rest of the set was PASS). Checked from the text only; no renders (science role, no formula chains in this task).
- Physics: growing coil current, growing flux through the ring, the induced field opposes the growth, the ring's coil-side face is the same pole as the coil's top, repulsion only while the current changes. All right, and the solution says the same as the lesson (Lenz from energy conservation).
- Exactly one correct choice and one correct reason; each distractor has its own wrong idea: the chapter's warned "metal is attracted" (reason 1), the reversed Lenz direction (reason 2), "DC gives no induction" (reason 4), and a true but irrelevant statement (reason 5).
- Form: the reasons are 85–95 characters each; the correct one is not the longest, not the only hedged one.
- Scope: the coil field (fy7-3) and induction (fy7-5) only; Al called non-ferromagnetic with no para-magnetism, as the scope requires.
- solutions.md L2-08 has Kysytty, Periaate and Mallivastaus, and explains each wrong reason.
- answers.py ran with -I: all 14 numeric answers agree with exercises.json within tolerance; the L2-08 comment line is right.
- Hash 958094b9ba257773 at start and end.
