VERDICT: PASS
CONTENT-HASH: f3218e7a2ffa30c3
SCOPE: delta added-exercise from bfb2af3a6b840af5 base 81db4a6fd727

## Blocking
- none

## Polish
- none

## Checked
- fy1-2-L1-10 only (delta, added exercise; round 3). The hash was f3218e7a2ffa30c3 at the start and at the end.
- I recomputed the answer myself: t = s/c = 3,844·10⁸ m / 2,998·10⁸ m/s = 1,28219 s (1,28222 s with the exact c). answers.py gives 1.282188, and the key 1,282 s is right.
- Significant figures: both data, 3,844·10⁸ m and 2,998·10⁸ m/s, have four, so 1,282 s with four figures is justified. The solution's reason now matches the figures it gives, so my round-2 polish point is resolved.
- Tolerance 0,04 is relative here (as in L3-05's 0,03 → 1,455…1,545), so the solution's "noin ±4 %" is right. A student who rounds to 1,28 s or 1,3 s is still inside it, and so is one who uses the MAFY table's own c value.
- The MAFY Moon mean distance (384 400 km, table Aurinkokunta) and the hint are right. The km → m conversion is right, and t = s/c is stated symbolically before substitution.
- Physics: the radio signal travels at c. Taking the vacuum value and the centre-to-centre mean distance is a fair simplification (category C). The reasonableness check is a real one. The task stays within the FY1 scope and uses the lesson's notation.
