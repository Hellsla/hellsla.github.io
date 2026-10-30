VERDICT: FAIL
CONTENT-HASH: 0e9004dded5fe968

## Blocking
- solutions.md:75–83 (L1-05) — **A**: the figure contradicts the stated balance. At constant velocity the step says $G_x$ and $F_\mu$ cancel (both 14,83). Yet $\overline{F}_\mu$ is enlarged under the 40 % rule to 30,6 px, while the dashed $\overline{G}_x$ stays at true scale, 14,6 px. — Fix: fbd.py must scale a component by the same enlargement as the forces along its axis.
- solutions.md:112–120 (L2-02) — **A**, same cause, with the order reversed. In truth $G_x$ = 20,8 > $F_\mu$ = 13,4, and the sled accelerates down the slope, as the drawn $\overline{a}$ says. Yet $F_\mu$ is drawn 29,9 px and $G_x$ 18,9 px, so the net force along the slope looks up-slope, against $\overline{a}$. — Fix: as above.

## Polish
- solutions.md:165–179 (L3-01) — The text says "Kummallakin rinteen osalla" but only the 25° and flat parts are drawn. Add the 10° part (N 98,48, F_μ 11,82, a alas), or say that it looks the same.
- solutions.md:21–27 (L1-02) — The point is a up while the jumper moves down; add `v alas` as L2-03 and L3-03 do.
- solutions.md:36–43 (L1-03) — The chute's 30° is not in the task. Fair, since the shape does not matter; the step could call it an example point.

## Checked
- All 12 blocks rendered and viewed; every arrow (and dashed component) measured from the SVG.
- Spec values recomputed from the task text: 686,7 and 742,7; 882,9 and 2100; 259,8 = 300·cos 30°; μ 0,080; α = tan⁻¹ 0,15 = 8,53°, N 98,89, F_μ 14,83; 588,6 and 652,4; N 97,81, F_μ 13,43; mean F_v = 784,8 + 40·2668/145 = 1520,8; 8338,5 twice; 90,63, 10,88, and 100 with 12 on the flat; 735,75 and 650; 686,7 and 2124,0.
- `pinta −α` rises to the left. Friction is drawn up the slope from the upper corner, and a, v and +x point down the slope, as "x rinnettä alas" says.
- N is perpendicular to the slope, G vertical from the centre, and the components are dashed with open heads. tan 12° > μ gives the down-slope a in L2-02.
- In the lift and force-plate tasks, N is a push to the bottom face: longer than G when a is up, shorter when a is down (drawn 1,08, 1,11 and 0,885).
- The earlier polish on L2-03's relative lengths is resolved: F_v is drawn 1,94 × G.
- Text and answers are unchanged since the PASS.
- Hash 0e9004dded5fe968 at the start and at the end.
