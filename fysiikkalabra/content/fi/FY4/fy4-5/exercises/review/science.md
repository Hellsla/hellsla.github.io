VERDICT: FAIL
CONTENT-HASH: 8a86a0c579dbd292

## Blocking
- exercises.json:161 (fy4-5-L2-05 text) — **B**: The ring hangs in a vertical plane, but the task never says that the ring's weight is negligible. Only the solution (solutions.md:238) assumes it, and the answer relies on F_B sin α = F_C. Otherwise y: F_B sin α − F_C − mg = 0, with an unknown m. — Fix: add to the task "Renkaan massa on niin pieni, että sen paino jätetään huomiotta" next to "Köysien massat jätetään huomiotta".

## Polish
- exercises.json L2-07: the plane of the forces is not stated, and neither is a negligible ring weight. Fix: add "Rengas on vaakasuoralla pöydällä" or "renkaan paino jätetään huomiotta".
- solutions.md:330 (L3-04): c) is rounded to two significant figures (84 N), but d) gives "N ≈ 185 N" with three. Fix: write 1,9·10² N, or explain the difference.
- exercises.json L1-08, distractor "N on nolla": the feedback's reason is weak ("narun pystykomponentti on pienempi kuin paino" is not given). The real reason: if N = 0, friction would also be zero, and T cos α would move the box. Fix: use that reason in the feedback.
- Plan (docs/exercise-bank/FY4.md): level 1 asks for an MC with "fbd: select", and level 3 for a "draw" task. The new tasks use identify/equations only. This is for pedagogy to judge.

## Checked
- Recomputed in one script: 55 N, 40,1° (39,81/40,18/40,36), 2,5 m/s², 12,17 N, 83,9 N, 14,38 m. All match answers.py and the solutions.
- L2-05 data: √(F_A² + F_C²) gives 3,91 / 5,89 / 7,87 N, which agrees with the F_B readings 3,9 / 5,9 / 7,9.
- L2-07 data: computed sums 13,5 / 12,2 / 10,0 N vs table 13,4 / 12,3 / 10,1 N.
- L3-04: a least-squares fit gives a = 0,803 m/s², so F_μ = 83,8 N (tol 0,03). N = mg − T sin α = 185 N.
- L3-05: the phase means are 880,7 / 784,7 / 689,7 N, so a = 1,20 / 0 / −1,19 m/s². h₁ + h₂ + h₃ = 14,4 m, and v returns to about 0. The rendered diagram (T > G, a and v drawn separately) is right.
- L2-06: the error ("potkun voima" with no agent) is identified correctly. The diagram has only friction horizontally, and a = 2,5 m/s² points against the motion.
- MC L1-06, L1-08: one correct option, every distractor wrong.
- The hash was the same at start and end. The sims FAIL concerns the lesson.
