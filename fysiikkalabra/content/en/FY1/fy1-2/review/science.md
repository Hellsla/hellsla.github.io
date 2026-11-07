VERDICT: PASS
CONTENT-HASH: 3d04085ff61812ac
Mode: light (teacher 2026-11-07, "kevyt katselmointi": round-2 + round-3 diff since edb368de4 only)

## Blocking
- none

## Polish
- none

## Checked
- git diff edb368de4 of lesson.md, inquiry.json, sim.js and tests/sims/fy1-2.json (fig/exit/meta unchanged).
- Round-2 FAIL resolved: calc, model, source_note and sim D0_AU now all say d0 = 119,0 AU (Burlaga et al. 2019); sim test expectations recomputed.
- Recomputed d = 119,0 AU + v(t - t0), v = 15,341 km/s: 1.1.2026 142,16 AU, 2,127e10 km, 19,71 h, ratio 142 to 8,32 min; table 2018/2022/2026/2030 = 119,0/131,9/144,9/157,8 AU, 1,78/1,97/2,17/2,36e10 km, 16,5/18,3/20,1/21,9 h; Feb 2026 142,4-142,6 AU vs JPL 143,05 AU from Earth: agreement within ~1 AU is stated correctly.
- Solar deceleration GM/r^2 ~ 4e-7 m/s^2 over 7,2 a gives ~0,09 km/s: "about 0,1 km/s" correct; the 1 h, 1 week (1212 AU) feedbacks still right; test trip from 10^10,32 km: s = 4,15e8 km, t = 1384 s, jump x = 6,679e6 px all match.
- lesson.md: new sentence that whole-number data ending in zeros (e.g. 10 min) are exact unless stated is a valid book convention, consistent with the 1000 conversion-factor sentence. The en text matches the Finnish fix number for number.
