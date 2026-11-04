VERDICT: FAIL
CONTENT-HASH: 98623ccc1f2e8db3

## Blocking
- content/fi/FY5/fy5-2/exercises/solutions.md:181–190 (L3-04, new **Voimakuvio** block) — **A**: the model answer to a) draws the ladder as a horizontal box standing on the floor. It puts the wall force at mid-height of the box's left side and friction on the floor line, with no tilt, so no force is at the ladder's real point of application. In a moment task the points of application (N and friction at the foot, the wall force at the top end, the weights at the middle) are what give the arms s cos α and L sin α. As drawn, the figure contradicts the Periaate and docs/force-diagrams.md ("each force starts at its point of application"), and a student copying it cannot read the arms from it. — Fix: draw the ladder as a rectangle tilted 65° to the floor, with N up and $\overline{F}_\mu$ toward the wall at the foot, the wall force away from the wall at the top end, and the weight(s) at the middle. Merging G_t and G_h into one arrow is valid only because the person is at the midpoint, so say that. Use the same symbols in the figure and the text: currently the figure has F_μ and F_s while the Periaate and Kaava use f and N_s. If the block cannot do this, use fbd.py.

## Polish
- exercises.json:82, :74 (L1-08, L1-07) — close to L1-05 and L1-02 (same formula); acceptable.

## Checked
- Round 1 Blocking fixed: L3-05 now states "Henkilön jalat eivät ylety lattiaan, joten koko hänen painonsa on tuolin varassa"; the Periaate repeats it. x_h,max = 42,22 cm, θ = 52,97° → 53° unchanged.
- The diagram's numbers are right: with the person at the midpoint the wall force and friction are 853,5 N · 2,5 m · cos 65° / (5 m · sin 65°) = 199 N < 341 N; the force directions are right (friction toward the wall, wall force away from it).
- L1-06 rewritten options: exactly one correct (moments of a couple in the same sense → the rod turns while its centre of gravity stays put); every distractor wrong and its feedback right.
- L2-07 rewording: the spread of 108,5–111,4 g is a few per cent with no trend in m: right; back-check 6010/210,2 = 28,6 cm right.
- answers.py and every answer unchanged; the round-1 independent recomputation of all 8 new answers stands.
- Scope, levels and plan +3/+3/+2 still fit.
