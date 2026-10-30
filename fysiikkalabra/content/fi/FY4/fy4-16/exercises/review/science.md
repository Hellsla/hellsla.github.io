VERDICT: PASS
CONTENT-HASH: abd12ce858254990

## Blocking

## Polish
- solutions.md:42 (L1-04, Järkevyys) — "$6\,\text{s} : 0{,}8 \approx 7{,}5\,\text{s}$" mixes units and rounds μg; write $(6{,}0\,\text{m/s}) : (0{,}785\,\text{m/s}^2) \approx 7{,}6\,\text{s}$.
- solutions.md L2-03 (Voimakuvio) — the diagram does not state the relative length; the jumper slows down, so on average $F_\text{v}$ is longer than $G$ (as in L3-03).
- solutions.md L2-04 — a real lift has a counterweight; a half-sentence that the task asks only for the rope's power on the car would answer that question before a student asks it.

## Checked
- The changed line solutions.md:76 (L2-02, Järkevyys): $h = 18{,}0\,\text{m}\cdot\sin 12{,}0^\circ = 3{,}742\,\text{m} \approx 3{,}74\,\text{m}$ (the drop height, as $h = L\sin\alpha$ in the brief); $\sqrt{2\cdot 9{,}81\cdot 3{,}74}\,\text{m/s} = 8{,}57\,\text{m/s} \approx 8{,}6\,\text{m/s}$ (unrounded $h$ gives 8,569, same); $1 - 5{,}10^2/8{,}57^2 = 0{,}65$, so "noin kaksi kolmasosaa" holds; $\tan 12{,}0^\circ = 0{,}213 > 0{,}137$ holds. The line uses the same frictionless limit as the brief's Järkevyys ($\sqrt{2gh}$).
- All twelve answers recomputed with my own formulas in one script; each agrees with exercises.json and answers.py to < 1e-4 (742,7 N; 1,217 kN; 7,924 m/s; 22,94 m; 8,531°; 1,063 m/s²; 0,1373; 220,5 kJ; 6,671 kW; 37,5 m; 2,287 m/s; 2,124 kN).
- L2-02 intermediate values 36,71, 13,01, 23,71 and 172,72 m²/s² recomputed.
- Voimakuvio steps in every solution: right interactions, normal force ⟂ surface, friction up the slope or backwards, no forward force (L1-03, L1-04), velocity and acceleration never drawn as forces, components dashed (L1-05), no third-law pair on one body.
- L3-02 against figure ex-hissi: 650 N for 1,0–3,0 s, 735,75 N at constant speed, 800 N stops the lift by 8,67 s; the description gives the same data and not the answer.
- L3-01: h/μ is independent of the angles, both slope parts are steeper than 6,8°, and the task text excludes bend losses.
- L3-03 kinematic cross-check (20,5 m/s², 60,0 m) and L2-04 cross-check (T = 8,34 kN, P = Tv = 6,67 kW) hold.
- Signs, positive directions, units, conversions, significant figures and tolerances in every solution; every task is within FY4 scope and uses the brief's notation.
