VERDICT: PASS
CONTENT-HASH: 70411a3fa44fd758

## Blocking

## Polish
- solutions.md:233 (fy4-4-L2-07): the Vastaus gives two significant figures "kuten jännitysvoimassa 5,40 kN", but 5,40 kN has three, and the lesson's example keeps three (1,02 m/s²). Fix: give 0,990 m/s², or say why two figures are enough: T − mg = 495 N is known only to about ±5 N.
- solutions.md L2-06 (fy4-4-L2-06): the answers to a) "Mitä kulmakerroin kertoo?" (the pulling force F) and b) "Mitkä suureet vakioina?" (the force, the track and friction; only the mass changes) appear only in Periaate. Fix: repeat them as a) and b) in the Vastaus line.
- solutions.md L1-08 Järkevyys (fy4-4-L1-08): "Moottorikelkan ja kuljettajan yhteismassa", but the task asks for the snowmobile's mass. Fix: make the two say the same thing.
- exercises.json L1-07/L1-08: both are near copies of L1-02 (ΣF = ma) and L1-03 (m = ΣF/a). This is for pedagogy to judge.
- exercises.json L3-05: the plan asks for an "(t, a)-hissikuvaaja", but the task gives a two-row table plus text. A (t, a) graph would match the plan.

## Checked
- Recomputed all 20 answers in one script. All match answers.py and the solutions.
- L2-05: a least-squares fit through the origin gives k = 2,009 1/kg, so m = 0,498 kg (answer 0,5, tol 0,04).
- L2-06: a fit of (1/m, a) through the origin gives F = 1,206 N. The products ma lie between 1,17 and 1,24 N.
- L3-04: a linear fit gives slope 0,499, so m = 2,00 kg. The F-intercept is 1,19 N, which matches 1,18 N. The points read off the line, (2,0; 0,41) and (6,0; 2,40), agree with the fit.
- L3-05: v_max = 3,0 m/s and a₃ = −0,75 m/s², so N = m(g + a₃) = 634 N, less than the weight 686,7 N. The diagram (N < G, a down, v up drawn separately) is right.
- L1-06 (MC): exactly one option is correct, and each distractor's feedback is right (ΣF follows a, not v).
- The scope fits FY4.4. No task uses later-course physics. Kinematics from fy4-2 is used only at level 3.
- Notation follows the lesson: ΣF = ma, $\overline{G}$, $\overline{T}$, $\overline{N}$, \mu$, positive direction stated.
- No new task duplicates an existing one. The levels and the 8/7/5 counts fit docs/exercise-bank/FY4.md.
- The hash was the same at the start and at the end.
