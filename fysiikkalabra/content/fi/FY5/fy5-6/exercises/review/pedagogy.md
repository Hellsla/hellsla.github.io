VERDICT: FAIL
CONTENT-HASH: 0d489920ee94599b
## Blocking
- exercises.json (fy5-6-L1-10) — repeats fy5-6-L1-08: Earth's orbital speed around the Sun, 29,8 km/s, from r = 1,496·10⁸ km (the solution even says the result is the same as from the period). The figure read (mean of 147,1 and 152,1) only replaces a given number. Fix: use the figure for something new at level 1, e.g. compare the speed at the radius of Halley's perihelion circle, or drop it.
- exercises.json (fy5-6-L1-11) — a near copy of L1-05 (probe orbiting the Moon, v from M and r, answer 1,55 vs 1,63 km/s); the only additions are the MAFY lookup and r = R + h. Level 1 already holds v = sqrt(γM/r) five times (01, 03, 05, 07, 10). Fix: keep the MAFY lookup but change the question (e.g. the orbital period of the probe, or the g at the orbit), or replace L1-05.

## Polish
- exercises.json (L2-08) — asks circular-orbit speeds for a comet on a long ellipse; the solution says so, but the situation is artificial. Better: two circular orbits of the Earth and Halley's perihelion distance, as planned in the text.
- Hint of L1-11 names a section (*Aurinkokunta*), not just the table.

## Checked
- Text and figure description only (no renders); arithmetic of all three solutions recomputed: 29,8 km/s, 1,55 km/s, 7,7.
- fy5-6/radat gives all needed values; no answer in it.
- inquiry.json not opened.
