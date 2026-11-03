VERDICT: FAIL
CONTENT-HASH: 9b33e8c9e77a651e

## Blocking
- exercises.json:101 (fy6-5-L3-03), B: the answer depends on two things the task does not say. The task does not say which side of the lamp pair the 20 Ω resistor is on, and the lamp pair has two junctions. The solution (solutions.md:112) assumes the order + → resistor → lamps → − and the upper junction, which gives +1,8 V. If the lamps sit next to the plus pole, the upper junction stays at 12 V (0 V change) and the lower one falls by 1,8 V (−1,8 V). In the given order, the lower junction is always 0 V. Fix: "Vastus on kytketty lähteen plusnavan ja lamppujen väliin. Kuinka paljon vastuksen ja lamppujen välisen haarautumispisteen potentiaali muuttuu?"

## Polish
- exercises.json:14, 57, 84, 101 (L1-02, L2-02, L3-01, L3-03): only L2-03 says "Lähteen ja johtimien resistanssit jätetään huomiotta". L3-03 in particular depends on an ideal source, because the current changes. Add the same sentence to L3-03, or state ideal sources once in the set's intro.
- solutions.md:31 (L1-04, Järkevyys): "Potentiaali laskee, koska virta kulkee korkeammasta potentiaalista matalampaan" is circular as a check. Better: the drop RI = 6,0 V is less than a typical source voltage, and its sign follows the current's direction.

## Checked
- All 12 answers recomputed with my own formulas. They agree with answers.py and exercises.json: 1,2 A; 7,5 V; 8,0 V; 6,0 V; 4,0 V; 3,5 V; 8,0 V; 0,50 A; 60 Ω; −9,0 V; 30 Ω; 1,8 V (in the solution's reading).
- ex-graph (figures.py) values: 9 → 7 → 3 → 0 V, drops 2 + 4 + 3 = 9 V, readable on 1 V gridlines. ex-branch: 6,0 V, 20 Ω ∥ 30 Ω. ex-branch2: 12 V, 40 Ω, 60 Ω ∥ ?, 0,20 A. All match the task text and the solutions.
- Each solution solves for the unknown symbolically first. Unit conversions (mA → A) are right, the signs in L1-03 and L3-01 are right, and the Järkevyys checks are real back-substitutions.
- Rounding reasons cite the limiting data. Subtractions (L2-01, L2-04, L3-03) keep reasonable precision.
- The laws are applied inside FY6 scope, with no internal resistance and no Kirchhoff systems beyond one junction.
