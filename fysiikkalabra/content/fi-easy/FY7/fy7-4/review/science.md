VERDICT: PASS
CONTENT-HASH: 027593ed88728c4a

## Blocking

## Polish
- inquiry.json simulaatio `model` — "Vain johtimen vaakasuora alaosa on kentässä" conflicts with the side view, where the vertical lead passes between the poles and through the drawn field lines. The next sentence (lead forces are horizontal) covers the physics. — Say "Pystysuorat tulojohtimet ovat osin kentässä, mutta niihin kohdistuvat voimat ovat vaakasuoria…", or drop the first claim.
- lesson.md Kaiutin, last sentence — "muuttuu … sisäenergiaksi, eli ne lämpenevät" is not wrong, but the guardrail wording is "muuttuu sisäenergiaksi, joka siirtyy lämpönä ympäristöön". The energy is dissipated mainly in the coil (Joule heating), and the magnet warms through it. — Use "kelan sisäenergiaksi (kela ja magneetti lämpenevät), joka siirtyy lämpönä ympäristöön".
- inquiry.json hook — "Molemmissa on kuitenkin magneetti": a mains desk fan usually has an AC (shaded-pole or induction) motor whose stator is electromagnets, not a permanent magnet. The photo caption already notes that AC motors differ. — Write "magneetti tai sähkömagneetti", or keep it as is: a fair simplification (C).

## Checked
- Recomputed every number in one script with my own formulas: worked example 6,98 N → 7,0 N, pysähdy 0,25 N, virtavaaka readings 247,75, 242,85 and 246,52 g, Δm 2,45, 1,22 and 2,12 g, B = 0,080 T, siirto 0,60 N plus the mistakes 0,006, 3,77 and 0,30, check-2 0,20, 0,346 and 0,40, virhe 0,15 and 0,26, exit 0,30 N, kertaus 5,0 µT. All match lesson-answers.py and the texts.
- Direction of every figure checked with cross products: swing (F to the left; the rule's palm pointing down is right), motor (forces turn the loop counterclockwise as the caption says), speaker (both F towards the cone), angle (F into the page, B sin α perpendicular to the wire), wires (parallel currents attract, opposite currents repel).
- Exit ticket 2: current to the east and B to the north gives F upward. Right.
- sim.js: with B to the left, I·d×B gives F = +I l B sin α upward. The scale reads m0 + F/g (Newton's third law). The side view is right-handed (into the page = +y), and the force symbol in the top view matches. simState gives `lukema` for both experiments. The adapter keys I, alpha, magneetti and l match `initial` and `locked`, and the slider steps reach 3,0 A, 30° and 60°.
- Each experiment isolates its variable: koe-1 varies I with α, magnet and l locked; koe-2 varies α with I, magnet and l locked.
- Predictions: each has exactly one correct option, and every distractor's feedback gives the right reason and the right model values.
- Motor: the forces point outward in the perpendicular position, the commutator flips the current every half turn, and without one the loop oscillates. Consistent in the theory, pysähdy, check-1 and the glossary.
- The radial-field argument (zero net force on a closed coil in a uniform field) and the explain model answer are consistent.
- The old ampere definition (2·10⁻⁷ N/m at 1 m) is correct. The two-wire force is inside FY7's LOPS content.
