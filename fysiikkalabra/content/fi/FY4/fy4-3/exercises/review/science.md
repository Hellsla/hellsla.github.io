VERDICT: FAIL
CONTENT-HASH: eabfc51dd0a19623

## Blocking
- solutions.md:58-59 (fy4-3-L1-04) — A, magnitude: the car's diagram gives $G = N = 900\,\text{N}$, so the weight is drawn only about 1,5 times the driving force of 620 N. A real car weighs about $1\cdot 10^4\,\text{N}$, 15–25 times the driving force, so the to-scale diagram gives a wrong picture of the magnitudes. — Fix: use a realistic weight, for example `G 12000` / `N 12000`. Note that fbdspec's enlargement of small forces (`shown`, an affine map) would then draw $F$, $F_\text{i}$ and $F_\text{r}$ almost the same length, and the horizontal balance would no longer show. The tool should therefore enlarge small forces by one common factor, keeping $F = F_\text{i} + F_\text{r}$ visible. The other option is to leave out G and N and keep the sentence "Pystysuunnassa paino ja tukivoima kumoavat toisensa".

## Polish
- solutions.md:39 (L1-03) — The skater's weight of 590 N and the acceleration away from the wall are not in the task. They are reasonable (about 60 kg, frictionless ice), but the text says "Laki pätee riippumatta siitä, liikkuuko kumpikaan", and the diagram shows only one of those cases. Adding "jää oletetaan kitkattomaksi" to the Voimakuvio sentence would cover it (C).
- solutions.md L2-02, L3-01 — In the diagrams buoyancy is $\overline{F}_\text{n}$. docs/force-diagrams.md names it $\overline{F}_\text{noste}$. This symbol issue is carried over from round 1.

## Checked
- All 12 diagrams rendered (`fbdspec.py show`) and checked in screenshots.
- Every diagram has the same body, forces and symbols as its Voimakuvio sentence.
- The sizes match the task data: 18; 850; 6,38; 8,0 + 5,0 = 13; 720/65; 833,85; 5800 + 3139,2 = 8939,2; 4620 = 4350 + 270; 0,30 + 0,30 = 0,60; 1,5 + 0,40 = 1,9.
- Third-law partners are kept off the diagrams: the book's pull on the Earth, the skater's push on the wall, and the apple's force acting on the hook (not on the apple).
- The pushes ($\overline{F}_\text{KL}$, $\overline{F}_2$, $\overline{F}_\text{m}$) end on the correct face. The magnetic force is drawn as a push on the top face, which is acceptable for a non-contact force.
- $\overline{v}$ is drawn in blue apart from the forces (parachutist, balloon). Every equilibrium diagram has a = 0.
- Answers are unchanged from round 1. The text diff is only the added spec blocks.
- The hash was the same at the start and at the end.
