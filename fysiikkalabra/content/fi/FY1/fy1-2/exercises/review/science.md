VERDICT: FAIL
CONTENT-HASH: 4ae28724816455e3

## Blocking
- content/fi/FY1/fy1-2/exercises/solutions.md:204 — (A, rounding) The answer is rounded to $t \approx 1{,}3\,\text{s}$ without a reason. The data are $s = 3{,}844\cdot10^{8}\,\text{m}$ (four figures) and $c = 2{,}998\cdot10^{8}\,\text{m/s}$ (four), so this chapter's own rule (kerto- ja jakolaskun tulos niin monella merkitsevällä numerolla kuin epätarkimmassa tekijässä) gives at least three figures. In the chapter that teaches significant figures, a two-figure answer with no reason teaches the wrong rounding — fix: "$t \approx 1{,}28\,\text{s}$, kolme merkitsevää numeroa (lähtöarvoissa neljä)" or give 1,282 s and state the reason.

## Polish
- none

## Checked
- fy1-2-L1-10 only (delta, added exercise); hash the same at start and end.
- Recomputed independently: t = s/c = 3,844·10⁸ m / 2,998·10⁸ m/s = 1,282 s (with c = 299 792 458 m/s, 1,2822 s); key 1.28 is right.
- MAFY Moon mean distance 384 400 km is right; the hint names the right table (Aurinkokunta).
- Conversion km → m is right; t = s/c is solved before substitution; c is given in the task.
- Physics: a radio signal travels at c (vacuum, Earth's atmosphere negligible): C, fine at this level.
- Reasonableness: about 4·10⁸ m / 3·10⁸ m/s, a little over 1 s, is a real check and matches fy1-1-L1-07 (1,28 s).
- Tolerance 0,04 is fine.
