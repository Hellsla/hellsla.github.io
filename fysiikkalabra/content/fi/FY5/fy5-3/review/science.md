VERDICT: PASS
CONTENT-HASH: 33990645fb664192

## Blocking

## Polish
- lesson.md:260 — the two-radii aria-label still says "kaksi kohtaa A ja B ovat samalla säteellä". This sits awkwardly beside "A etäisyydellä r ja B etäisyydellä 2r" — fix: write "samalla keskipisteestä lähtevällä suoralla" (carried over from round 1; not physics).

## Checked
- Round-1 sim finding fixed. sim.js:78 now takes `before` at `max(t − T/12, rel.t)` after the release, and `state()` returns the straight-line velocity for tt ≥ rel.t. So |Δv̄| = 0 from the moment of release, which matches the conclusion's model answer (inquiry.json:238).
- sim.js panel rework: the triangle is recentred, labels are larger, and both arrows are BLUE. The vectors and Δv̄ = v̄₂ − v̄₁ are unchanged; only the drawing offset moves. The physics in `state()` and `advance()` is unchanged.
- tarkistus-3: the gravity criterion and its model-answer sentence are gone. The remaining 3 criteria ask only what the prompt asks, and the model answer is still right.
- koe-1 intro: breaking at different points (top and left edge) and at two radii tests whether the departure direction depends on the release point. The setup still locks T and varies r, and α, v and vIrti are in simState.
- lesson.md "Suunnan muutos": the new sentence says the net force points toward the centre, not outward. That is correct for uniform circular motion, and it previews fy5-4 without introducing a_n.
- Unit wording (1/s as \tfrac) and the rpm-conversion mistake sentence have the same physics as before.
- Exit ticket 2: the ratio 9,0 cm / 3,0 cm = 3,0 is correct, and so is the reason (same T, v ∝ r).
- figures.py: the Δv̄ figure's v̄₁ colour changed only. Its geometry, checked in round 1, is unchanged.
- All lesson numbers from round 1 still hold, because none of the changed text alters them.
- Hash taken at the start and the end: 33990645fb664192.
