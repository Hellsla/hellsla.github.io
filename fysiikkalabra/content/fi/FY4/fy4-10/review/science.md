VERDICT: PASS
CONTENT-HASH: e90e74f3120fa3a8

## Blocking
- None.

## Polish
- Notation versus *Liikemäärä ja impulssi*: that chapter uses an unprimed $v$ for the velocity after; this one uses it for the velocity before. Fix: add one bridging line.
- lang/fi.json sims.fy4-10 "lukemat": "Nyt: $v_1$, $v_2$" reuses the symbols of the initial-velocity sliders. Fix: rename them.

## Checked
- The hash was e90e74f3120fa3a8 at the start and at the end. Since round 4 (hash 0c23e9f95fa7ef1f, commit 0d794894), commit 963b44ca changed exactly three places in the lesson files: inquiry.json:415, lesson.md:69 and the siirto solution's Järkevyys. Nothing changed in lessons/FY4/fy4-10, the simulation or the pictures.
- inquiry.json:415 now says the wrong result is larger than the right-moving cart's initial speed 0,40 m/s, and that this is impossible because the left-moving cart brakes it. I recomputed it: the wrong result is (0,20 + 0,18)/0,80 = 0,475 ≈ 0,48 m/s > 0,40 m/s. In a perfectly inelastic collision the common velocity lies between the initial velocities, −0,60 and +0,40 m/s, so the argument is valid. The correct result is 0,025 m/s. The round 4 Blocking item is resolved.
- lesson.md:69 now states the constant-force condition before using $\overline{F}\,\Delta t$. The last sentence still extends the argument to a varying force, with equal and opposite forces at every instant. The text is correct.
- In the siirto Järkevyys check, the mass ratio is 120/50 = 2,4 and the boat's speed is 2,4/2,4 = 1,0 m/s, which is consistent with the answer. The anecdotal sentence is gone and the check is complete.
- Everything else is unchanged since round 4, so the round 4 checks still hold. Those checks covered every recomputed number, the sim model and simState, the conservation conditions, one correct option per choice and the one-dimensional FY4 scope.
