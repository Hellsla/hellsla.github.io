VERDICT: FAIL
CONTENT-HASH: 1d3421f168ddc7be

## Blocking
- lesson.md:173, 387 (summary), glossary "voima ja vastavoima" — B (missing condition) — These say force and reaction "eivät koskaan kumoa toisiaan". The new subsection (line 176) says that for the system A+B their vector sum is $\overline{0}$, so the two chapters contradict each other. Fix: state the condition, e.g. "kun tarkastellaan toista kappaletta kerrallaan, ne eivät kumoa toisiaan (ne vaikuttavat eri kappaleisiin); kahden kappaleen systeemissä ne ovat sisäisiä ja summa on nolla". Same wording in line 173, the summary, and the en and fi-easy versions.
- lesson.md:176 — B (causality) — "Siksi ne eivät kuulu systeemin voimakuvioon" gives the zero sum as the reason. The real reason is that they are internal forces: they are not exerted by anything outside the system, and they do not change the motion of the system as a whole. The zero sum follows from that. Fix: "Koska ne ovat sisäisiä, ne eivät kuulu systeemin voimakuvioon; niiden summa on nolla."

## Polish
- lesson.md:176 and the "systeemit" figure — the claim that A+B has only vertical external forces holds only if friction is neglected (the "luistelijat" figure says so, the new one does not). Add "kitka jätetään huomiotta" to the text or the aria-label.
- lesson.md:176 — add one sentence that ice friction is the reason the net external force is zero, so A and B together stay at rest while A and B separately accelerate in opposite directions. That shows why the choice of system matters.
- "systeemit" figure — the arrows $\overline{N}_A+\overline{N}_B$ and $\overline{G}_A+\overline{G}_B$ are drawn equal (85 px each) and the A-only diagram is right (108 px each). The figure is correct; the N arrow tip extends past the top of the body, as in the other figures.

## Checked
- Third-law pair $\overline{F}_{AB}=-\overline{F}_{BA}$ and directions in the "systeemit" figure: B pushes A to the left, which is right. A-only diagram: G, N, F_BA (no extra forces); A+B diagram: only external forces; the arrow lengths agree with the equilibrium.
- Recomputed in one script: friction distances 1,125, 2,25, 4,5 and 9,0 m (answer 9,0 m, mistakes 2,25, 4,5, 5,625 are all wrong values); push force 110 N; the aircraft 2·48 = 96 kN; the trailer 420 + 260 = 680 N. All agree with the lesson.
- Sim: model is constant friction, no air resistance, and N = G; the keys s, tl, vl exist; no-friction run gives 12 m, 4,0 s, 3,0 m/s; the box rests with no friction; v is blue and not drawn in the force diagram.
- Both predictions have exactly one correct option and the feedback of each wrong one repairs the misconception. The experiment varies only the surface (v0 locked), and the conclusion's model answer agrees with the theory.
- Curling (example I): no forward force, friction backwards, not to scale and said so. Weight/normal-force pair in the common misconception and in check-2 is correct.
- Worked example (symbolic first, 7 stages) and the last paragraph about speed-dependent drag are correct. The exit ticket and check-1/3 are correct. The lint's physics warnings are not an issue.
- Not judged: the en and fi-easy texts (not in the packet) and the exercises.
