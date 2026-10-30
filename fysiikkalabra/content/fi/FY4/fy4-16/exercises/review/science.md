VERDICT: PASS
CONTENT-HASH: 006567f202fb0e9c

## Blocking

## Polish
- solutions.md:42 (L1-04, Järkevyys) — "$6\,\text{s} : 0{,}8 \approx 7{,}5\,\text{s}$" mixes units and rounds μg to 0,8; write $(6{,}0\,\text{m/s}) : (0{,}785\,\text{m/s}^2) \approx 7{,}6\,\text{s}$ (the distance check is unaffected).
- solutions.md L2-04 — a real lift has a counterweight; a half-sentence that the task asks only for the rope's power on the car (no counterweight) would pre-empt the question.

## Checked
- All twelve answers recomputed with my own formulas in one script; each agrees with exercises.json and answers.py to < 1e-6 (742,7 N; 1,217 kN; 7,924 m/s; 22,94 m; 8,531°; 1,063 m/s²; 0,1373; 220,5 kJ; 6,671 kW; 37,5 m; 2,287 m/s; 2,124 kN).
- L3-02 against figure ex-hissi: 650 N for 1,0–3,0 s, 735,75 N at constant speed, 800 N stops the lift in 2,67 s (6,0 → 8,67 s) as drawn; ramps symmetric.
- L3-01: h/μ independent of the angles; both slope parts steeper than tan⁻¹0,120 = 6,8°, bend losses excluded in the task text.
- Signs and positive directions in every lift, canopy and slope solution; F_v from the energy principle in L2-03/L3-03 with E_k and E_p both counted; L3-03 cross-check by kinematics (20,5 m/s², 60 m).
- Force diagrams described in the solutions follow docs/force-diagrams.md (N ⟂ surface, friction up the slope from the outline, no forward force, v and a not drawn as forces, relative lengths stated).
- Units, conversions, significant figures and their stated limiting data; every task within FY4 scope.
