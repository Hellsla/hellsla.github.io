VERDICT: PASS
CONTENT-HASH: dca543627b04711a
SCOPE: full: unit.md (three new ```pysahdy boxes judged first; hero and kalteva figures now raster images), inquiry.json, teacher.md, Sovella tasks.json, solutions.md, answers.py, figures.py.

## Blocking
- (none)

## Polish
- solutions.md s5 "Hyväksytään myös": the mean of the four tangents is 0,4144, which rounds to $0{,}414$, not $0{,}415$.
- s8 c): the left-over $0{,}02\,\text{m/s}$ comes from the graph's rounded times, not only from rounding (the exact stop is at about $8{,}67\,\text{s}$). The conclusion still holds.
- kalteva.webp is drawn with a height of 387.5 in a 380-unit viewBox, so the bottom edge is cut off. This is for the visual reviewer; the physics is not affected.

## Checked
- **Pysähdy 1** (forces between the car and the trailer): correct. It is a third-law pair acting on different bodies, and only the forces on the trailer decide its motion. This matches the Ydinajatus text, the hook and the "Voima ja vastavoima" item in Yleisiä virheitä.
- **Pysähdy 2** (braking on a straight road): correct. The net force points along the acceleration, against the motion. This matches the Kaava paragraph and lt-3.
- **Pysähdy 3**: $N = mg\cos\alpha$, with its condition stated (only the weight and the normal force act perpendicular to the surface). The answer that the normal force cancels $G_y$ is correct because nothing accelerates perpendicular to the slope. "Pienempi kuin $mg$" holds for $\alpha > 0$. The box repeats the theory sentence word for word. Not class B.
- **kalteva.webp** (the arrows on the new raster image, measured): $G \approx 140$, $G_y \approx 128$, $N \approx 127$, $G_x \approx 60$ in viewBox units. That is consistent with $\alpha \approx 25^\circ$ (the old vector figure: 145, 131, 132, 61), so "to scale" holds. $N$ starts at the bottom face, the friction is short and points up the slope, $G_x$ points down the slope, $G_y$ points into the slope, and there is no extra force. The angle arcs are in the right places. The hero picture is decorative only.
- **inquiry.json**: the only change is a paragraph split in the tarkistus-3 model answer, with the text unchanged. I re-checked every choice: one correct option each, the distractor feedback is right, and the numeric answers and their mistakes hold (aineisto 981/588,6/6100; nosturi 6,7665/5,9865/6,3765/0,39; vinoveto 0,3596/0,3080/0,3398/0,1677; pulkkamäki 3,306/4,606/3,134/5,905; lentopallo 12,03/7,588/2,222/9,812; tarkistus-2 48,0/18,57/72). Also hihna, virhe-rinne (23,0 vs 8,39 N) and kaksi-kappaletta ($T = 23{,}5\,\text{N}$, 49,1, 9,8).
- **teacher.md**: the extra hanging mass $m_\text{p} = (ma + F_\mu)/(g - a) = 0{,}124\,\text{kg}$.
- **Sovella s1–s8**: I recomputed them in my own script with my own formulas, and every part matches answers.py and the solutions:
  - s1: 1330,8 N, 19,29°, 932,8 N.
  - s2: 118,48 N, 296,2 N, ratio 0,40.
  - s3: least-squares fit $k = 1{,}175$, $F_0 = 0{,}239\,\text{N}$; values read from the line 0,851 kg and 0,238 N; $\mu = 0{,}0285$; with the extra mass $0{,}740$ and $0{,}378\,\text{N}$.
  - s4: 7,85 and 0,98 m/s².
  - s5: $\tan 22{,}5^\circ = 0{,}414$; the range 0,384–0,445; the report's 0,54 corresponds to 28,4°.
  - s6: 1,272 m/s², 10,09 m/s, 64,8 m, 7,9 s.
  - s7: 9,3 and 1,5 m/s², 623 N, 48,3 m/s, $k = 0{,}315$, 55,8 m/s.
  - s8: −1,143 m/s², −2,287 m/s, 0,857 m/s², 12,23 m.
- The rubric points match the parts, and the force diagrams have the right forces and directions. Half the range is called a chosen simple estimate, and outliers are dropped only for the recorded jerk, both as the guardrails require. Nothing goes beyond FY4 scope.
- The units.py hash was the same at the start and the end.
