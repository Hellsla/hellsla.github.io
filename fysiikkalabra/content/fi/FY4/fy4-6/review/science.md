VERDICT: PASS
CONTENT-HASH: 2a75402576207a6d

## Blocking

## Polish
- lessons/FY4/fy4-6/figures.py (*kalteva-ydin*, the first situation picture in Ydinajatus): the plank's upper end overhangs the post's top instead of clearly resting on it, as it does in *kalteva*. This is not a physics error. Make the two pictures agree.
- lesson.md, *Kaava*: "Levossa olevaan kappaleeseen vaikuttava lepokitka on yhtä suuri kuin $G_x$" relies on the condition in the sentence before it (only G, N and friction act). This is acceptable (C). Optionally add "kun muita rinteen suuntaisia voimia ei ole".

## Checked
- Round 1 blocking items are resolved. The $N = mg\cos\alpha$ condition is now stated in Ydinajatus, Kaava, virhekäsitys, Tiivistelmä and the glossary. $\overline{N}$ now starts on the bottom face uphill of the $\overline{G}$ shaft in *kalteva*, *kalteva-ydin*, *esimerkki* and *valitse-a…d*. I checked this in renders at 2.5×.
- Every lesson and inquiry number was recomputed in one script with my own formulas, and all agree: 48,0 N; 1,48 and 4,15 m/s²; 3,41/6,71/8,60/17,6/5,24 N; 26,57°; tan 26,5° = 0,499 (26° and 27° inside 3 %); 3,22 m/s²; 0,350; 20,3 N (20 is 1,5 % off against a 2 % tolerance); 0,306; T = 113 N; 97/589 N; truck 40 N.
- Figure magnitudes are to scale: N and $G_y$, friction and $G_x$, T = $G_x$ + friction (0,577 G), and the truck's friction at 0,20 G. The friction graph is at 50/35 N.
- FBD checklist on every figure, the sim and the solutions: interactions, directions, friction placed at the outline, dashed components, $\overline{a}$ and $\overline{v}$ not drawn as forces, and the equations' signs match the axes. Each *valitse* distractor has exactly one error, and its feedback names it.
- sim.js implements the stated model (box starting at rest, 1° slider steps, $\mu_0$ check), and its boxes state the limits. Exp-1 and exp-2 isolate their varied parameter, and simState gives Gx, N, Fmu and a.
- Choice items: exactly one correct option each, and every feedback is correct. The model answers and exit ticket agree with the theory. Friction in the direction of motion (truck, walking, conveyor) is explained by relative sliding.
- Scope fits FY4 (paino ja kitka, kitkakertoimen määrittäminen).
