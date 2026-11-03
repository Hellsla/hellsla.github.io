VERDICT: FAIL
CONTENT-HASH: 35d364ad974a1b27

## Blocking
- lesson.md:132 (Kaiutin, last sentence) — **A (definition; added in the simplification, the fi version ends at "sisäenergiaksi").** "muuttuu ... kelan ja magneetin sisäenergiaksi eli lämmöksi" makes internal energy and heat the same thing. The guardrails say heat is energy in transfer and a body has internal energy, not heat (FY3). — Fix: "...muuttuu kuitenkin kelan ja magneetin sisäenergiaksi, eli ne lämpenevät."

## Polish
- inquiry.json check-1 feedback (also fi): "kääntäisivät silmukkaa puolen kierroksen jälkeen takaisin". The torque reverses as soon as the loop passes the position where it is perpendicular to the field, not after half a turn. — Write "kun silmukka on ohittanut asennon, jossa se on kohtisuorassa kenttää vastaan, voimat kääntäisivät sitä takaisin".
- inquiry.json tarkistus-3 model: "Silloin kela ei liikkuisi" is too strong, because a uniform field across the axis would still give a torque. — Write "ei liikkuisi akselin suuntaan".
- lesson.md:217, the ampere definition: say that the 1 A flows in both wires ("kun kummassakin johtimessa kulkee 1 A ja ...").

## Checked
- The round-1 μ₀ item is fixed and matches fy7-3.
- Recomputed in one script. Worked example: l = 4,901 m, F = 6,98 N (7,0 N), about 71 times a 10 g cone's weight.
- Sim and inquiry: readings 247,75 / 242,85 / 246,52 g, Δm 2,45, 1,22 (3 A and 30°), 2,12 (60°), 0 (0°); B = 0,0801 T, which gives 0,080 T.
- siirto: B₁ 2,0 mT, 0,60 N; mistakes 0,006, 3,77 and 0,30 N. tarkistus-2: 0,20 N (cos 0,346, ⊥ 0,40). virhe: 0,15, 0,26 and 0,30 N. Exit: 0,30 N, force up.
- Directions by cross product:
  - swing: force left; hand rule: down.
  - motor: forces down and up, turning counterclockwise; at the perpendicular position the forces point away from the axis.
  - speaker: both forces toward the cone.
  - angle figure: into the page.
  - wires: like currents attract, opposite currents repel.
  - sim: F up for I > 0, the magnet is pushed down, the reading rises.
- The sim implements m = m₀ + IlB sin α / g. Its model box states its limits.
- koe-1 varies only I and koe-2 only α; the others are locked and simState gives lukema.
- Each choice item has exactly one correct option, and every distractor's feedback is correct (kertaus, ennuste-suunta, ennuste-2, virhe, check-1).
- The hash was the same at the start and the end.
