VERDICT: PASS
CONTENT-HASH: 688464c5a7f5edd4

## Blocking

## Polish
- lesson.md:105 (hero) — the bottom skater's wheels sit about 7 px above the ground line (wheel bottom y ≈ 532, ground 540), while the ramp skaters touch the ramp. The physics is not affected, but y + 7 would ground him.
- lesson.md:292 (polut) — the carts reach the floor with the full speed only if the ramp joins the floor smoothly. A sharp corner loses the perpendicular component. Fine at this level (C).

## Checked
- Hero, redrawn: the ground is at y 540 and the stop height h at y 210 (330 px). The ticks at 457,5, 375 and 292,5 are exactly ¼, ½ and ¾ h. The ramp line is at 25,0°. At x = 791 it is at y 292,4 (the v/2 skater's contact point = ¾ h), and at x = 967,5 it is at 210,1 (the v = 0 skater = h). The arrows are 170 px horizontal at the bottom and 85,0 px at 25,1° along the ramp: 2 : 1 : 0 and parallel to the motion. Since (v/2)² leaves ¼ of E_k, ¾ h is right. The ¾ h and ¼ h labels mark the correct segments, the aria-label matches, and the stop lies below the coping.
- Round-1 fixes: the check-1 "Molempiin" feedback no longer says "all forces". The Tiivistelmä conservation sentence now states no friction, no air resistance and no push or pull. "levosta" was added. The new pred-1 distractor (×6) has correct feedback (3× time · 3× mean speed = 9).
- Recomputed in one script against lesson-answers.py: hook 0,459/1,83 m, retrieval 5,1 m, Koe 1–3 (0,051/0,459 m, 3,0 m/s on both slopes, friction 0,378 m, 2,41 m/s, 2,91 J), 1,96, zero level 8,8/3,9/4,9 J, example 21 573 J → 22 kJ, Etsi virhe 50 kJ, transfer 9,83 m (19,7; 127), check-2 0,50 kg, exit ticket ½. All agree.
- Ramp figure h : 4h = 45 : 180 px with arrows 30 : 60. The E_k(v) curve and the 2,0/8,0 J points are on scale. The zero-level figure is at 150 px/m. The polut arrows are equal.
- sim.js: unchanged model. Exact piecewise motion with g(sin α ± μ cos α). The simState keys and the locked parameters isolate the varied one in each experiment.
- Definitions (conservative force, E_p and the zero level, E_mek) agree with the glossary and the slot's täsmennys. Scope is within FY4.
