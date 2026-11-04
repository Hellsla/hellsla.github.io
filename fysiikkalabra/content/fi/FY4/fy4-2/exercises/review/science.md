VERDICT: FAIL
CONTENT-HASH: cccd86d72dd6b1a0

## Blocking
- content/fi/FY4/fy4-2/exercises/solutions.md:180 (L3-04, Järkevyys) — **A, definition**: "Tulos on alle keskinopeudella $27{,}8\,\text{m/s}$ kuljettavan $222\,\text{m}$". 27,8 m/s is the final speed, and the car's mean speed is 128 m / 8,0 s ≈ 16 m/s. In a chapter that teaches keskinopeus vs. hetkellinen nopeus, this sentence teaches the wrong meaning. Fix: "Tulos on alle loppunopeudella $27{,}8\,\text{m/s}$ koko ajan kuljettavan $222\,\text{m}$".

## Polish
- exercises.json:69 (L1-06, option 4) — "painon vastavoima, joka osoittaa ylöspäin" plants a wrong term: the normal force is not the reaction to the weight. The feedback does not correct it, and forces come only in later chapters. Replace it with a distractor that has no force words, e.g. "Alaspäin, koska jarrutus painaa autoa tietä vasten".
- solutions.md:136 (L1-07) — "kolme merkitsevää numeroa, koska luetut arvot ovat tarkasti ruudukon viivoilla" contradicts L1-04, which gives 1,0 m/s² (two figures) from the same figure. Give 23 m (two figures, with 22,5 m as the intermediate value), or say the same in both.
- solutions.md:163 (L2-06) — "kolme merkitsevää numeroa … hajonta rajoittaa … kahteen" contradicts itself. Answer 1,2 m/s² (≈ 1,15) or explain why three figures are kept. A quadratic fit to the same data gives 1,20, so the second figure is already uncertain.
- solutions.md:191 (L3-05) — the reasonableness check uses $g\sin\alpha$, which fy4-2 does not teach. Mark it as a look ahead or drop it.
- solutions.md L3-04 Vastaus — "kolme merkitsevää numeroa kuten nopeuksien muunnoksessa": the data 36 km/h has two figures, so state 128 m as ≈ 1,3·10² m or justify the third figure.

## Checked
- All 20 answers recomputed in one script: L1-07 22,5 m; L2-05 slope 0,837 → 0,84 m/s² (v₀ 0,217); L2-06 (t²,x) slope 0,577, a = 1,154 m/s², intercept −0,005 m; L3-04 a per interval 5,0 / 3,61 / 2,92 / 2,36 m/s², trapezoids 10,0 + 27,2 + 40,3 + 50,8 = 128,3 m; L3-05 a −0,811 m/s², v₀ 2,420 m/s, t_k 2,99 s, s 3,61 m, x(5,0 s) 1,97 m > 0; α ≈ 4,7°. All match answers.py and the tolerances fit.
- L3-04: the v(t) graph is concave down, so the chords lie below it and the trapezoid sum underestimates; the solution says this correctly.
- L3-05: "kitka on pieni" covers the constant a through the turning point. c) (t,a) is a horizontal line and (t,x) a downward parabola with its top at 3,0 s, both correct.
- MC L1-06, L1-08, L2-07: exactly one correct option each, the distractors are wrong and their feedback right (L1-08: ½gt² ≈ 20 m; L2-07: two gates give one mean value).
- Figure fy4-2/ex-tv is shared by L1-04 (slope) and L1-07 (area): different questions, not a duplicate, and its alt text gives the values.
- Scope: everything stays within uniformly accelerated 1-D motion, (t,v) area, linearisation and polynomial fit; (t,a) at level 3 follows the plan. No vector symbols in the new tasks (the \overline rule does not apply) and no arrow figures.
- The render of the L3-05 table and solution at 1280 px is clean. Plan +3/+3/+2 met, 8/7/5 = 20.
- The hash was identical at the start and the end.
