VERDICT: PASS
CONTENT-HASH: 8002279b2f8d7cc7

## Blocking

## Polish
- inquiry.json:363 (tarkistus-3 model) — "joten kela ei liikkuisi": in a uniform field the net force on the closed coil is zero, but a field across the axis would still give a torque. — "joten kelaan ei kohdistuisi kokonaisvoimaa eikä se liikkuisi akselin suuntaan" (the lesson's own "kelaa ei työntäisi mikään" is already right).
- inquiry.json:319 (check-1 correct feedback) — "puolen kierroksen jälkeen takaisin" does not match the theory and pysähdy, where the reversal comes once the loop passes the position perpendicular to the field. — "kun silmukka on ohittanut asennon, jossa se on kohtisuorassa kenttää vastaan, voimat kääntäisivät sitä takaisin".
- lesson.md:106 — the two-wire force uses B₁ of a long straight wire, but the condition is not stated here. — "Kahden pitkän rinnakkaisen virtajohtimen …" (or "kun $l$ on paljon suurempi kuin $r$").
- lesson.md:63 — "muuttuu … kelan ja magneetin sisäenergiaksi": the guardrail wording adds "joka siirtyy lämpönä ympäristöön"; mostly it is the coil (resistive heating). This is optional.

## Checked
- Recomputed every number in one script with my own formulas: kertaus 10/5,0 µT; the sim readings 247,75 / 242,85 / 246,52 / 247,42 g, Δm 2,45 / 1,22 / 2,12 g; F = 0,0240 N and B = 0,080 T in the conclusion; the example gives l = 4,90 m and F = 6,98 ≈ 7,0 N; siirto gives 2,0·10⁻³ T and 0,60 N, with mistakes 0,0060 / 3,77 / 0,30, a weight of 61 g and 40 × Earth's field; tarkistus-2 0,20 (cos 0,346); virhe 0,15 (0,26); pysähdy 0,25 N; exit 0,30 N. All of them agree with lesson-answers.py and the text.
- Directions checked with cross products: swing figure (F left; the hand rule gives I × B toward the viewer = down), motor (counterclockwise torque matches the drawn arrow), speaker (both gaps push toward the cone), wires (attract/repel), angle figure (F into the page), exit ticket 2 (up).
- sim.js: F = I l B sin α, sign up for I > 0 with B from N to S matches the top view; reading m₀ + F/g by Newton's third law; the lead forces are horizontal and leave the reading unchanged; the model box states its limits (uniform gap field, rigid wire, model values without error).
- Experiments: koe-1 locks α, the magnet and l and varies I (slider step 0,5 reaches ±3, ±6). Koe-2 locks I, the magnet and l and varies α (step 5 reaches 0, 30, 60, 90). simState gives `lukema` at these values.
- Predictions: exactly one correct option in each; every distractor's feedback cites the right model values and mechanism.
- Scope matches the slot (F = IlB sin α, force between wires, DC motor, loudspeaker). The commutator, the radial field and the copper/non-ferromagnetic statement are correct for this level (C). The ampere definition (2·10⁻⁷ N/m until 2019) is correct.
- The top-view α arc measured from the field line opposite to B gives the same sin α (C).
