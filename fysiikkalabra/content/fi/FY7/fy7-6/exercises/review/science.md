VERDICT: PASS
CONTENT-HASH: 3e3c0eeec4dee222

## Blocking

## Polish
- exercises/solutions.md:79 (fy7-6-L2-04 Järkevyys) — "pyörrevirtajarrun voimakin pienenee", said of a train slowing from 250 km/h, applies the F ∝ v model outside its range. Real rail eddy-current brakes are past their critical speed there, and their force does not fall as the train slows. — Drop the clause, and keep "teho on verrannollinen vauhtiin, kun voima pysyy samana".
- exercises/exercises.json:56 (fy7-6-L2-02) — "käämin läpi kulkeva magneettivuo" could be read as the flux through the whole coil. fy7-5 uses "yhden kierroksen läpi". — Write "yhden kierroksen läpi kulkeva magneettivuo".

## Checked
- I recomputed the 9 numeric answers independently in one script, and all agree. answers.py agrees with the recomputation.
- L1-01 and L2-03: at constant speed F = mg; vt = mg/k = 0,15 m/s.
- L1-03 and L3-01: energy conservation on level track and in a vertical tube. L3-01 states no heat loss and no change of state; ΔT = 0,073 K.
- L1-04, L2-01, L2-04: P = Fv = mgv. L2-01 is cross-checked with Q/t.
- L2-02: e = NΔΦ/Δt = 3,0 V and I = 0,20 A. Self-induction is ignored, which fits the scope.
- L3-03: F = (Bl)²v/R = 0,60 N, and the power balance Fv = RI² = 1,8 W is right.
- L1-02, L1-05, L3-02 word answers: Lenz direction (S face repels), the hob (glass is an insulator), the slotted Waltenhofen plate. All are correct.
- Units, conversions and 2 s.f. reasons correct; notation matches the lesson.
