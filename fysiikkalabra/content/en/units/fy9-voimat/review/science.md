VERDICT: PASS
CONTENT-HASH: cfd99d8374f19dd9
SCOPE: full; the new ```pysahdy boxes judged first against the Finnish version; hero and kalteva figures are now raster images.

## Blocking
- (none)

## Polish
- tasks.json s7 c) and d) rubric: the calculation rows use $v_\text{r}$ and $v_\text{r}'$ (the Finnish "rajanopeus" subscript). The equation rows and the solution use $v_\text{t}$. Make them consistent; the physics is unaffected.
- teacher.md "Assessment" calls the calculation tasks 15-point tasks, but s7 has 17 points and s8 has 19. The Finnish text says the same. Report to the developer, not a translation error.
- solutions.md s5 "Accepted also": the mean of the four tangents is $0.4144$, so it should be $0.414$, not $0.415$ (carried over from the Finnish review).
- s8 c): the remaining $0.02\,\text{m/s}$ comes from the graph's rounded times (the stop is at about $8.67\,\text{s}$), not from rounding alone. The conclusion stands.

## Checked
- **Pysähdy boxes (3)**: same physics as the Finnish boxes at unit.md lines 86, 104 and 137. 1: the third-law pair acts on different bodies, and only the forces on the trailer decide its motion. 2: the net force points along the acceleration, against the motion when braking. 3: $N = mg\cos\alpha$, with its condition stated (only $G$ and $N$ act perpendicular to the surface). "Smaller than $mg$" holds for $\alpha > 0$. All three agree with the Key idea, the Formula text, lt-3 and Common mistakes. None is class A or B.
- **kalteva.webp**: I read the arrows against the overlaid labels. $N$ and $G_y$ are equal, $G_x/G$ and $G_y/G$ fit $\alpha \approx 25^\circ$, and the friction is short and points up the slope. Every label sits at its own arrow, and the $\alpha$ arc lies between $G$ and $G_y$. The "to scale" claim holds and there is no extra force. The hero picture is decorative.
- **inquiry.json**: the only change is a paragraph split in the tarkistus-3 model. I re-checked every choice: each has exactly one correct option and the distractor feedback is right. The numeric items match: aineisto 981 N, nosturi 6.7665 kN, vinoveto 0.3596, pulkkamaki 3.306, lentopallo 12.03, tarkistus-2 48.0 N, pulley 23.5 N, rinne 23 N, and every mistake value. teacher.md $m_\text{p} \approx 0.124\,\text{kg}$.
- **Sovella s1–s8**: my own script (scratchpad recompute.py) agrees with answers.py and the solutions:
  - s1: 1330.8 N, 932.8 N, 19.29°.
  - s2: 118.48 N, 296.2 N.
  - s3: fit $k = 1.175$, intercept 0.239 N; 0.851 kg, 0.238 N, 0.0285; with the extra mass 0.740 and 0.378 N.
  - s5: 0.414 (0.384–0.445); the report's 0.54 corresponds to 28.4°.
  - s6: 10.09 m/s, 64.8 m.
  - s7: 623 N, 48.35 m/s, 55.83 m/s.
  - s8: −1.143 m/s², −2.287 m/s, 0.857 m/s², 12.23 m.
- Each part's rubric criteria add up to its points. The FBD rubrics and solutions show the right forces and directions. The decimal points are right for en, and nothing goes beyond FY4 scope. The hash was the same at the start and the end.
