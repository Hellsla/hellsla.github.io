VERDICT: PASS
CONTENT-HASH: 3daf47c3361e7181

## Blocking

## Polish
- solutions.md:71–79 (L1-05) — $\overline{F}_\text{r}$ is drawn 15 units (6 : 24 on the horizontal scale, which is right), but its filled head is about as long as that, so it reads as a bare arrowhead at the left face. Its text alternative also calls it only "voima Fr". — Fix: let fbdspec give it the word "vierimisvastus", or draw the head shorter for short arrows.
- solutions.md:38–44 (L1-03) — This is still open from round 1. The task is about $\overline{a}$ pointing against the motion. Add `v alas`, as in L1-04 and L2-03.
- solutions.md:159–167 and 179–187 (L3-01, L3-02) — This is still open from round 1. Each diagram shows one body at two moments, but the text alternative says "Voimakuviot kummastakin kappaleesta … Kappale 1 / Kappale 2". — Fix: give fbdspec a "two moments" wording.

## Checked
- Hash 3daf47c3361e7181 at the start and at the end. The only change since round 1 is solutions.md:75 (`F 24 oikea kitka`).
- I rendered all 12 blocks with `fbdspec.py show`, viewed them, and measured every arrow from the SVG.
- Round-1 blocker 1 (L1-05) is gone. The horizontal forces are on their own common scale: F 60, F_v 45, F_r 15, so 45 + 15 = 60 is visible under `a 0`. G and N are both 100. The text alternative says that the horizontal scale is different.
- Round-1 blocker 2 (L1-05) is gone. The road's friction force $\overline{F}$ now starts at the front lower corner of the contact surface and points forward along the surface. The step text ("tien kitkavoima $\overline{F}$ … eteenpäin"), the equation $F - F_\text{v} - F_\text{r} = 0$ and the task use the same symbol.
- Round-1 polish item L2-04 is resolved: F_v 60 and F_r 24 (0,40, which is the true 450 : 180). The axis has its own scale, a points left, and the text alternative says so.
- These one-scale ratios match the true ones within 0,5 px: L1-02 25,5 % (true 25,5 %), L1-03 G 73,5 % (73,6 %), L1-04 27 % (27,2 %), L2-02 39 % (38,8 %), L2-03 44,5 % (44,7 %), L3-01 35 : 70 (½), L3-02 21,5 : 70 (30,6 %), L3-03 33,5 % (33,7 %). No force falls under the 15 % floor.
- At terminal speed the forces are drawn equal (L1-01, L2-01, L3-01 first moment). F_v opposes v in every diagram: down while rising (L1-04, L2-03, L3-02 first moment).
- No diagram now contradicts its step text, equation or motion.
- I recomputed all 12 answers in one script from the task text; all agree (L3-03 from the tangent slope 6,5 m/s²).
