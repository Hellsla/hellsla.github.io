VERDICT: PASS
CONTENT-HASH: 6216d93fd96de0cf

Round 3 review of fy3-1. Lint 0/0, check_latex OK, test_sims PASS. Domain hash identical at start and end.

## Blocking
(none)

## Polish
1. lesson.md:22 — "Kuun massa on paljon pienempi kuin Maan, joten ... vuorovaikutus on heikompi" is true for the Moon, but mass alone does not set the surface value: Uranus has about 14,5 Earth masses yet g ≈ 8,9 m/s² < 9,81 m/s². — Soften to "Kuu on paljon pienempi ja sen massa paljon pienempi kuin Maan, joten …"
2. exit-ticket.json:12 — The question gives the mass of the water (1,5 kg), but the quoted sentence is about the bottle, which has more mass than its water. — Quote "vesi painaa puolitoista kiloa", or give the mass of the full bottle.
3. sim.js:189–190 — The scale line "asteikko 0–X N" is centred above the chart (y ≈ 58), while the full-scale tick is at the left of the axis (y = 90). — Optionally print "X N" beside the tick.

## Checked
- lesson.md: G = mg with g as putoamiskiihtyvyys in m/s²; 1 N = 1 kg·m/s² (deferred to FY4) is correct; no N/kg anywhere in the domain files or tests/sims/fy3-1.json.
- Weight is never a cause of motion: the SVG weight arrow acts on the block, line 8 says the bodies pull the spring, and L3-02 states an equal force, not a motion law.
- lesson.md:8: proportionality with its limit, 5,0 N/2,0 cm → 10 N/4,0 cm and 2,5 N/1,0 cm, calibration with 100 g ≈ 0,981 N bodies (additivity, no circularity), the s = vt analogy (both lines pass through the origin).
- lesson.md:25 additivity argument for G ∝ m; g table; bathroom scale 1/6 on the Moon; example 1180 N / 445 N, 690 N.
- answers.py: every line uses the right formula/conversion; output matches exercises.json within tolerance.
- Hand recomputation of the new L1-04 and of L2-04 and L3-03 (below).
- solutions.md: reasoning correct in all 12, including the reworded L1-02/L1-04 (ratio method, the 3× and 1,5× sanity checks).
- exit-ticket.json: 29 N → 4,9 N; 7,5 cm; 1,5 · 9,81 = 14,7 ≈ 15 N.
- sim.js: G = m·g exactly; stretch and arrow are purely proportional on a fixed scale; the y axis now ends at y = 90, exactly where the full-scale Jupiter bar ends (round-2 polish resolved).

## Python output
```
fy3-1-L1-01 39.24 39 N relerr=0.0061
fy3-1-L1-02 6.0 6.0 cm relerr=0.0000
fy3-1-L1-03 48.6 49 N relerr=0.0082
fy3-1-L1-04 7.5 7.5 N relerr=0.0000
fy3-1-L1-05 62.0 62 N relerr=0.0000
fy3-1-L2-01 4.9949 5.0 kg relerr=0.0010
fy3-1-L2-02 0.5886 0.59 N relerr=0.0024
fy3-1-L2-03 1187.55 1190 N relerr=0.0021
fy3-1-L2-04 5.886 5.9 N relerr=0.0024
fy3-1-L3-01 6.8073 6.8 N relerr=0.0011
fy3-1-L3-02 133.2222 133 kg relerr=0.0017
fy3-1-L3-03 0.9908 0.99 kg relerr=0.0008
L1-04 by hand: k=5.0/2.0=2.50 N/cm; F(3.0 cm)=7.50 N
L2-04 by hand: G=1.962 N; F=G*4.5/1.5=5.886 N
L3-03 by hand: G=9.720 N; reading=0.9908 kg
lesson: apple 0.981 N; 120*9.81=1177.2; 120*3.71=445.2; 70*9.81=686.7; Kuu/Maa=0.1651; Jup/Maa=2.528
calibration 2.0 cm@5.0 N: 10 N->4.0 cm, 2.5 N->1.0 cm
exit: 29.43 4.86 7.50 14.715
sim: axis top y=90, Jupiter bar top y=90
sim: stretch/G=0.076613 px/N arrow/G=0.044355 px/N (both fixed)
test_sims: PASS preview/fy3-1
```
