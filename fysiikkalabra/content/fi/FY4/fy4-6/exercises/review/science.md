VERDICT: FAIL
CONTENT-HASH: 92a29494f4fbe0d8

## Blocking
- solutions.md:104-112 (fy4-6-L2-01) — A, figure magnitudes: the friction arrow $\overline{F}_\mu$ (25,8 N) is drawn about 1,5 times as long as the dashed component $\overline{G}_x$ (40,8 N), and $\overline{a}$ points down the slope. The figure therefore shows the net force up the slope, against $\overline{a}$. The cause is in fbdspec.py: `shown` enlarges forces below 40 % of G, but the components are drawn at true scale. — Fix: in fbdspec.py, draw components with the same `shown` map, or keep the order between forces and components along each axis, then re-render. The same cause makes $F_\mu$ about 10 % longer than $G_x$ in L1-04 (solutions.md:65-73), where they must be equal.

## Polish
- solutions.md:84-92 (L1-05) — The diagram adds $\overline{N}$ and a static friction equal to $G_x$ (a = 0). The Voimakuvio sentence draws only G and its components, and the task never says the box is at rest ("on rinteellä" reads as at rest, so this is C). Mention N and friction in the sentence, or write "levossa oleva laatikko" in the task.
- solutions.md:157-165 (L2-04) — $\overline{F}_\mu$ is drawn at $\mu_0 N$ = 48,2 N while $\overline{a}$ points down the slope. Once the box slides, kinetic friction acts, and the task does not give it. Say in the sentence that the arrow shows the largest possible static friction, which is not enough.
- solutions.md:7-12 (L1-01) — Carried over: N = G assumes the astronaut stands still, which the task does not state.

## Checked
- All 11 diagrams rendered (`fbdspec.py show`) and checked in screenshots.
- The sizes follow from the task data:
  - L1-02: 0,12·294,3 = 35,3.
  - L1-03: 120 = 120.
  - L1-04: N = 7,848 cos 20°.
  - L1-05: 117,7 sin 30° = 58,86.
  - L2-01: μN = 25,79, and a = 0,75 from 3,0/4,0.
  - L2-02: 0,30·392,4.
  - L2-04: N = 80,36.
  - L3-01: 50·3,5 = 175.
  - L3-02: 0,25·9,218.
  - L3-03: μ = 0,342 gives a = 2,0.
- Directions are right: $\overline{a}$ points down the slope where the body slides down; in L3-02 $\overline{v}$ points up the slope and $F_\mu$ and $\overline{a}$ down; in L3-01 friction points forward from the front corner.
- The components of G are dashed and labelled $\overline{G}_x$ and $\overline{G}_y$, and they are not counted twice. $\overline{N}$ is perpendicular to the surface.
- Answers and text are unchanged since round 1. The hash was the same at the start and at the end.
