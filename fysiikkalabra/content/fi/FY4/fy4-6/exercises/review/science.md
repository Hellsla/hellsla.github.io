VERDICT: PASS
CONTENT-HASH: 92a29494f4fbe0d8

## Blocking

## Polish
- solutions.md:84-92 (L1-05) — Carried over. The diagram adds $\overline{N}$ and a static friction equal to $G_x$, but the Voimakuvio sentence names only G and its components. Mention them in the sentence, or say in the task that the box is at rest.
- solutions.md:157-165 (L2-04) — Carried over. $\overline{F}_\mu$ is drawn at $\mu_0 N$ while $\overline{a}$ points down the slope. Say that the arrow shows the largest possible static friction, which is not enough.
- solutions.md:7-12 (L1-01) — Carried over. N = G assumes the astronaut stands still, which the task does not state.
- L1-02, L1-03, L2-02, L3-01 — The split horizontal scale is stated only in the text alternative. A visible note under such figures would help sighted readers.

## Checked
- The round-1 blocking item (L2-01) is resolved. Measured lengths: G 100, $\overline{G}_x$ 21,0 (true 20,8), $\overline{F}_\mu$ 14,9 (true 13,1, lifted to the 15 % floor, and the text alternative says so). Friction is now shorter than $G_x$, so the net force points down the slope, along $\overline{a}$. $\overline{G}_y$ 97,7 equals N 98,2.
- Also from round 1, L1-04: $F_\mu$ 34,2 now equals $G_x$ 34,0 (a = 0).
- I rendered, screenshotted and measured all 11 diagrams. Forces and dashed components are drawn on one scale:
  - L1-05: $F_\mu$ = $G_x$ = 50,2.
  - L2-04: $F_\mu$ 49,5 < $G_x$ 57,4, a down the slope.
  - L3-02: $F_\mu$ 23,4 and $G_x$ 34,0, both down the slope, with $\overline{v}$ up the slope.
  - L3-03: $F_\mu$ 29,6 < $G_x$ 50,2.
  - N = $G_y$ in each.
- Split scales on level ground:
  - L1-02: friction only, a opposite to v.
  - L1-03: F = $F_\mu$ = 60.
  - L2-02: T 60, $F_\mu$ 47, which is 117,7/150 = 0,785, net force forward.
  - L3-01: friction forward, along $\overline{a}$.
- No diagram contradicts its Voimakuvio sentence or its motion.
- I recomputed all 12 answers in one script. Each is within tolerance: 259; 35,3; 0,306; 7,37; 58,9; 0,134 (3,3 % against 4 %); 0,807; 0,2145; 8,05; 0,357; 0,795; 0,330.
- The exercise text is unchanged since round 1. Only fbdspec.py changed. The hash was the same at the start and at the end.
