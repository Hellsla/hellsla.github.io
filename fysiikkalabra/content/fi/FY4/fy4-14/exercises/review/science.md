VERDICT: FAIL
CONTENT-HASH: 7476df03d06e713d

## Blocking
- solutions.md:71–79 (L1-05) — **A**: the figure contradicts the motion. At constant velocity the point is $F = F_\text{v} + F_\text{r}$. The weight of 784,8 N pushes all three horizontal forces under the 40 % enlargement, so they are drawn F 26 px, F_v 26 px and F_r 25,5 px. The forward arrow equals the air resistance alone, and the horizontal sum points backwards under `a 0`. — Fix: make fbd.py enlarge the forces along one axis by a common factor, so that 24 = 18 + 6 stays visible. fy4-16 L1-05 and L2-02 have the same root cause. Until then, a smaller weight in the spec keeps them above the clamp; the task gives no mass.
- solutions.md:75 (L1-05) — Drawing rule broken: `F 24 oikea @ala` draws the road's friction from the middle of the bottom face along the contact line, on top of the ground line. Friction starts at the outline, at a corner of the contact surface. — Fix: draw it as friction (`F_mu 24 oikea`) and name it $\overline{F}_\mu$ in the step and equation (course notation).

## Polish
- solutions.md:144–145 (L2-04) — $F_\text{v}$ 450 N and $F_\text{r}$ 180 N are drawn 26,5 px and 25,5 px, so the 2,5 : 1 ratio is lost. The common-factor fix cures this too.
- solutions.md:38–42 (L1-03) — The task is about a pointing against v. Add `v alas`, as in L1-04 and L2-03.
- solutions.md:160–168 and 182–190 (L3-01, L3-02) — Both diagrams show one body at two moments, but the generated description says "Voimakuviot kummastakin kappaleesta … Kappale 1 / 2". That misleads screen-reader users; fbdspec needs a "two moments" wording.

## Checked
- All 12 blocks rendered and viewed, and every arrow measured from the SVG.
- Every spec value recomputed from the task text: 735,75; 0,05003; 19,62 with 5; 5,886 with 8; 4,4145 with 1,2; 686,7 with 266,7; 0,5592 with 0,25; 11 772 with 450 and 180; 706,3 with 353,2; 1,962 with 0,6 twice; 1,4715 with 0,4965.
- $F_\text{v}$ opposes the velocity: up while falling, down while rising (L1-04, L2-03, the first moment of L3-02). In L3-02, a points down at both moments.
- Terminal-speed arrows are equal (L1-01, L2-01, L3-01 before the turn). After the turn in L3-01, F_v is drawn at half length, and in L1-03 F_v is longer than G with a up.
- Other ratios are kept (L2-02: 0,395 drawn, 0,388 true).
- Text and answers are unchanged since the PASS.
- Hash 7476df03d06e713d at the start and at the end.
