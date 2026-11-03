VERDICT: PASS
CONTENT-HASH: a5f83ab368fa4a88

## Blocking

## Polish
- inquiry.json check-1 feedback (carried over from round 2): "kääntäisivät silmukkaa puolen kierroksen jälkeen takaisin". The torque reverses as soon as the loop passes the position where it is perpendicular to the field, not after half a turn. — Write "kun silmukka on ohittanut asennon, jossa se on kohtisuorassa kenttää vastaan, voimat kääntäisivät sitä takaisin".
- inquiry.json tarkistus-3 model (carried over): "Silloin kela ei liikkuisi" is too strong, because a uniform field across the axis would still give a torque. — Write "ei liikkuisi akselin suuntaan".
- lesson.md:217, the ampere definition (carried over): say that the 1 A flows in both wires ("kun kummassakin johtimessa kulkee 1 A ja ...").

## Checked
- The round-2 blocker is fixed. lesson.md (Kaiutin) now reads "muuttuu ... sisäenergiaksi, eli ne lämpenevät", which agrees with the guardrail that a body has internal energy, not heat. The glossary entry for kaiutin says the same.
- Recomputed in one script. Worked example: l = 4,901 m, F = 6,98 N (7,0 N), about 71 times a 10 g cone's weight.
- Sim readings: 247,75 / 242,85 g. Δm is 2,45 g at 6 A, 1,22 g at 3 A and at 30°, 2,12 g at 60° and 0 at 0°. B = 0,0801 T, so 0,080 T.
- siirto: B₁ = 2,0 mT, F = 0,60 N. The mistakes give 0,006, 3,77 and 0,30 N, and the load matches 61 g. B₁ is 40 times the Earth's field.
- tarkistus-2: 0,20 N (cos gives 0,346, perpendicular 0,40). virhe: 0,15, 0,26 and 0,30 N. Exit ticket: 0,30 N, and east × north = up. The ampere value is 2·10⁻⁷ N/m.
- Directions checked by cross product:
  - swing figure: force left; hand-rule figure: force down.
  - motor: forces down and up, turning the loop counterclockwise.
  - speaker: both forces toward the cone.
  - angle figure: force into the page.
  - wires: like currents attract, opposite currents repel.
  - sim top view: d × (−x̂) = +sin α ẑ, so F is up for I > 0 and the reading rises. The side view's into/out-of-page symbol agrees.
- The sim implements m = m₀ + IlB sin α / g, and its model box states its limits (uniform field, leads give no vertical force, model values).
- koe-1 varies only I and koe-2 only α. The other parameters are locked, and simState gives lukema.
- Each choice item has exactly one correct option, and every distractor's feedback is correct (kertaus, ennuste-suunta, ennuste-2, virhe, check-1).
- The hash was a5f83ab368fa4a88 at both the start and the end.
