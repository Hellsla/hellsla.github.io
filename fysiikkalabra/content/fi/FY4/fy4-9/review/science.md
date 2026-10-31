VERDICT: FAIL
CONTENT-HASH: 57a12d426ce70b31

## Blocking
- lesson.md:387 ("Alustan voima on kokonaisvoimasta suurin osa, sillä paino on … paljon pienempi"), inquiry.json:497 (check-3 model, "siitä suurin osa tulee alustan voimasta") — **B, the landing's forces.** ΣF = N − G: the support force is larger than the net force, not a part of it, and the weight works against the stopping. "The weight is much smaller" holds on hard ground (Δt ≈ 0,015 s: G/N ≈ 3 %) but not on the mat (Δt ≈ 0,2–0,3 s: G/N ≈ 30–40 %, with 70 kg and Δp ≈ 310 N·s). The conclusion still holds, since N_ka = G + |Δp|/Δt. — Write "Alustan voima on tätä kokonaisvoimaa painon verran suurempi, mutta sekin pienenee, kun pysähtymisaika pitenee", and the same in the check-3 model.

## Polish
- lesson.md:490 vs :551 — F_ka is defined as |Δp|/Δt, but the example's F_ka is signed. — Say that the direction comes from the sign of Δp.
- sim.js:169 — the axis label "F (N)" differs from the figure's F_x, though the curve is signed. — Use F_x.
- sim-spec.md — "F = kc" is a magnitude; model.js uses F_x = −kc. — Say so.

## Checked
- Round-1 fixes: (1) pysaytys shows signed F_x with the time axis at 0 at the top. The curves are below it: hard −80 N / 0,0393 s, soft −20 N / 0,157 s, each with area 2,000 N·s. The caption gives −2,0 N·s. (2) "kokonaisvoiman impulssi" appears in the lesson, the misconception and the check-3 criterion and model. (3) Rebound: Δp = −2mv, magnitude 2mv (:382, :558, summary).
- model.js, 72 combinations, against analytic SHM: Δt agrees to 1e-10 s, I to 5e-6 N·s and F_max to 2e-4 N, and I = Δp. No curve point is positive, and the crush is ≤ 0,283 m. The test passes (616).
- Sim graph: the scale is ≥ 1,04 × the largest shown peak (max 113 N), and the 0,444 s contact fits in 0,5 s, so nothing is cut. The shaded signed area is I_x.
- Arrows: blue v, purple p and red F, each from its signed component. F is hidden after the crushable stop.
- The bumper models agree across model.js, the sim boxes and sim-spec.
- All the inquiry, example, siirto and check numbers, mistakes and the exit ticket were recomputed.
- Exactly one correct option per item. Each experiment varies only its key, and simState gives every measured key.
