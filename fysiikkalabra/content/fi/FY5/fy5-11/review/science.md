VERDICT: PASS
CONTENT-HASH: dc39a8f223100a24

## Blocking

## Polish
- sim.js:10 and sim-spec.md — the comment and spec still call the field "2D Kirchhoff (Kirchhoffin 2D-malli)". Without the obliquity factor it is a Rayleigh–Sommerfeld / monopole sum, appropriate for a rigid barrier — fix: rename the comment; this is not student-facing.
- sim.js wall mode — β = asin(sin α) only reproduces the law being tested, so koe-1 confirms the construction rather than showing an emergent result. Acceptable as Huygens geometry.

## Checked
- Round-1 B fixed: the semicircle claim is now "selvästi aallonpituutta kapeampi (b < λ)" in lesson.md, the figure label and caption, ennuste-3, johtopäätös, tarkistus-1, tarkistus-3 and its criterion. "b ≈ λ: leviäminen suuri" agrees with the model's θ = 37°.
- Round-1 A fixed: slit() has no (1+cos)/2 factor, so the drawn field and the thetaHalf readout use the same model, and the calc text's "ei putoa puoleen" now holds at b = 1 cm, λ = 2 cm.
- este-AP recomputed with the new kernel: 83,9 / 70,7 / 32,6 % (b = 1, 2, 8 cm), matching 84 / 71 / 33 %.
- siirto Järkevyys: (180° − 70°) + (180° − 110°) = 180° is correct now.
- tarkistus-1 distractor feedback now correctly says that b/λ grows and the spreading weakens.
- θ values 8,7°/17,6°/37,4°/90° and 11,7°/23,8° (koe-4) do not depend on the obliquity factor, so they are unchanged.
- The Huygens derivation of β = α, the rope image-pulse model (±3,0 cm, free end 2A), the example 50°/50°/40°, and the exit ticket 65° were all rechecked from round 1.
- Exactly one correct option per prediction and check; the distractor feedback is physically right.
