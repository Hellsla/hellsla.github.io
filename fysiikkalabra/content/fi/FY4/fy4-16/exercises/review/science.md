VERDICT: PASS
CONTENT-HASH: 0e9004dded5fe968

## Blocking

## Polish
- solutions.md:166–179 (L3-01) — The flat-part friction is on its own horizontal scale: it is drawn 42 units, while the slope-part friction is lifted to the floor and drawn 11 (true 12 and 10,9 N). In one figure the flat friction therefore looks four times the slope friction. The note about this exists only in the text alternative. — Fix: draw both moments at one scale, or say in the step that the flat part is at its own scale. Also still open from round 1: the text says "Kummallakin rinteen osalla" but the 10° part is not drawn.
- solutions.md:166–179 (L3-01) — The text alternative puts both scale notes before "Kappale 1 … Kappale 2", but this is one sled at two places, and only the second needs the split-scale note. — Fix: give fbdspec a "two moments" wording, and attach each note to its body.
- solutions.md:23–27 (L1-02) — This is still open from round 1. The point is a up while the jumper moves down. Add `v alas`, as L2-03 and L3-03 do.
- solutions.md:38–43 (L1-03) — The chute's 30° is not in the task. The step could call it an example angle.

## Checked
- Hash 0e9004dded5fe968 at the start and at the end. The text is unchanged since round 1; only the renderer changed.
- I rendered all 12 blocks with `fbdspec.py show`, viewed them, and measured every arrow and dashed component from the SVG.
- Round-1 blocker L1-05 is gone. The dashed $\overline{G}_x$ is 14,6 and $\overline{F}_\mu$ is 15,1 (true 14,83 each, F_μ at the 15 % floor). They are visibly equal under `a 0`, and the text alternative says that small forces are lengthened.
- Round-1 blocker L2-02 is gone. $\overline{G}_x$ is 21,0 and $\overline{F}_\mu$ is 14,9 (true 20,8 and 13,4), so the drawn net force along the slope points down the slope, as $\overline{a}$ does.
- L1-04 (level ice): F_μ is on its own horizontal scale (60), a points left, and the text alternative says the scales differ.
- One-scale ratios match the true ones within 0,5 px: L1-01 92,5 % (92,5 %), L1-02 42 % (42,0 %), L1-03 N 86,5 % (cos 30°), L2-01 90 % (90,2 %), L2-03 51,5 % (51,6 %), L3-02 88,5 % (88,3 %), L3-03 32,5 % (32,3 %). L2-04 is equal.
- In the lift and parachute diagrams the longer arrow agrees with $\overline{a}$ in every case. On the slopes N is perpendicular to the slope and friction points up the slope from the outline.
- I recomputed every answer in one script from the task text; all agree (L3-01 x = h/μ = 37,5 m).
