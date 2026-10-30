VERDICT: PASS
CONTENT-HASH: 75ec76da240a1f2c

## Blocking

## Polish
- solutions.md:63 (fy4-4-L2-02): adding "kun vastapainoa ja kitkaa ei oteta huomioon" would state the lift model (C as it stands; carried from round 3).
- solutions.md:74 (fy4-4-L2-03): "kaksi merkitsevää numeroa" is defensible but conservative. $g + a = 10{,}8\,\text{m/s}^2$ keeps three figures, so $1{,}30\,\text{kN}$ would also be justified. Either answer is inside the tolerance.
- solutions.md:11 (fy4-4-L1-02), Järkevyys: "kun tien voima renkaaseen vähennetään vastusvoimilla" reads backwards. Suggest "kun tien voimasta renkaaseen vähennetään vastusvoimat". Language only.

## Checked
- The round-3 Blocking item is fixed: L1-04 now says "vaakasuoraan suuntaan $38\,\text{N}$:n voimalla". The horizontal pull matches the solution's diagram, $F - F_\mu = ma$ and 1,5 m/s².
- I recomputed all 12 answers with my own formulas in one script: 2,4; 120; 15; 1,5; 78,48; 3000; 7479; 1297; 0,50; 0,981 (down); 20; 6,67. They equal exercises.json and answers.py.
- Rounded student answers (78 N, 7500 N, 1300 N, 0,98 m/s², 6,7 s) are within 0,7 % of the key. The relative tolerance is 2 %.
- Directions and signs:
  - L2-02: positive is down, $mg - T = ma$.
  - L2-03: the load moves down and slows, so $\overline{a}$ points up and $T = m(g + a)$.
  - L3-01: $N < G$, so $a$ points down when the lift starts from rest. The alternative (moving up, slowing) is correctly noted.
  - L3-03: friction is the only horizontal force, and the net force is opposite to the velocity.
- Force-diagram checklist for L1-04, L1-05, L2-02, L2-03, L2-04, L3-01 and L3-03: every force has a cause; the object is a rectangle; weight starts at the centre and $\overline{N}$/$\overline{T}$ at the contact or attachment point; friction starts at the outline corner; there are no third-law pairs; $v$ and $a$ are not drawn as forces; relative lengths agree with the acceleration; the equations follow from the diagram with a stated positive direction.
- L1-01–03, L2-01 and L3-02 give or ask for the net force directly, so no diagram is needed (C).
- Every solution is symbolic before substitution. The conversions are right: 90 km/h = 25 m/s, 36 km/h = 10 m/s, t → kg, kN.
- Significant figures follow the limiting datum. L3-01's 2 s.f. follows from the 6,0 kg difference.
- The magnitudes are realistic: car 2,5 m/s²; truck 12,5 kN net force; sled μ ≈ 0,06 on snow; lift 1,5 m/s².
- Scope stays within FY4 Newton's laws, the equation of motion and the prerequisite kinematics ($a = \Delta v/\Delta t$). The notation matches the brief ($\Sigma F$, $\overline{G}$, $\overline{T}$, $\overline{N}$, $\overline{F}_\mu$).
- The hash was identical at the start and the end.
