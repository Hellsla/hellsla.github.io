VERDICT: PASS
CONTENT-HASH: 1197865df5c60483
SCOPE: delta: new tasks s8 (Laserkoe akryylilevyllä) and s9 (Käämin vuo ja induktiovirta) and the intro; older tasks untouched

## Blocking
- (none)

## Polish
- s8 a and s9 a repeat chapter exercises almost as they are: s8 a is fy7-10-L2-09 (same figure `fy7-10/fit`, same two-point slope, same n); s9 a is fy7-5-L2-08 (same figure `fy7-5/flux-task-2`, same interval 0–0,40 s, only N differs). CLAUDE.md says never to relabel chapter exercises. The parts b-d (s8 b-d, s9 b-c) carry the independent demand, so the tasks pass, but a variant figure or data for a would make them original. Both are also less "unfamiliar situation" than s1-s7: the context is the chapter's own experiment. The workload is fair (15 and 12 points, five minutes each part).
- s8 text gives the axes ($\sin\alpha_1$ vertical, $\sin\alpha_2$ horizontal), which tells the student the model is a straight line through the origin; part d then asks why. Acceptable (the figure needs its axes named), but d would test more if the text only said "kuvaajassa on mittaustulokset".
- s9 c: the question names the zero-flux moment, which tells where the trap is. A more open "Selitä induktiovirran suunta koko ajalta 0–0,80 s" would keep the 4th criterion as a discovery.
- s8 d: the criterion "toteaa, että taitekerroin on aineen ominaisuus" is observable but its point is easy to earn with a generic sentence; fine for a 3-point word part.

## Checked
- Read the fi packet's checks (practice.py check OK), the intro (nine tasks; seventh is the data task, matches s7), the task texts, rubrics and worked solutions of s8 and s9.
- Physics and numbers recomputed by hand: n = 0,45/0,30 = 1,5; v = 2,0·10^8 m/s, t = 0,75 ns; critical angle 41,8° (42°); e1 = 120·8,0 mWb/0,40 s = 2,4 V, e3 = 1,8 V; W = 0,288 + 0,081 = 0,369 J ≈ 0,37 J; flux zero at 0,25 s with rate -20 mWb/s. Lenz directions right. Answer tolerances accept the two-figure roundings (42 vs 41,81 is 0,5 %).
- Rubrics: criterion points equal part points (4+4+4+3, 4+4+4); criteria ask what the part asks; common mistakes are real (inverted slope, cm not converted, arcsin 1,5, ΔΦ = 5-3, mWb unconverted).
- Figure alt-texts (catalog descriptions) use the task's names ($\sin\alpha_1$, $\sin\alpha_2$, $\Phi$, $t$, grid 0,1 and 1 mWb, 0,1 s) and give no slope or voltage; the figures are needed to answer.
- Rounding to the data's precision stated in the solutions; calculation chains are aligned rows; the unit fields ("", "· 10⁸ m/s", "ns", "V", "J", "°") are language-neutral.
- Opened sovella captures 390 px parts 8-9: they show older tasks (s6), not s8/s9, so 360 px layout is left to check_layout and the visual reviewer.
- Hash same at start and end (1197865df5c60483).
