VERDICT: FAIL
CONTENT-HASH: f86c668d8d52ca6b
Delta review (solution practice, 2026-11-12) of the version passed before.

## Blocking
1. (A) s5 a, accepted answers disagree in three places: `tasks.json` tolerance 0.04 at 153 accepts 147–159 s, the `units_precision` criterion says 145–160 s, and `solutions.md` *Hyväksytään myös* says 145–157 s. Fix: one range in all three (e.g. tolerance 0.045 and "146–160 s" in both texts).
2. (A) `lessons/units/fy9-moderni/sovella/answers.py`: the part's answer key `fy9-moderni-s5-a` still returns the two-endpoint value 150.83 while `tasks.json` now answers 153 (the fit is only `s5-a-fit`). The check passes only through the tolerance. Fix: `s5-a` = `round(T_fit, 1)`, keep the two-endpoint value under its own key (e.g. `s5-a-two`), and recompute `s5-a-diff` against the fit.

## Polish
3. s5 a Järkevyys: 151 s differs from the fit 153,1 s by 1,5 %, not 1,4 % (1,4 % was against the book's 153 s). Fix the number.
4. s5 b rubric `conclusion` still says "noin 151–153 s" while the model answer now says "noin 153 s"; harmless, align if touched.

## Checked
s5 a recomputed: least-squares line of $\ln(N-5)$ against $t$ over all 11 points gives $k = -4{,}528 \cdot 10^{-3}\,\text{s}^{-1}$, intercept 5,993, value at 300 s 4,635 (the read points are on the fit), $T_{1/2}$ = 153,07 s; two endpoints 150,83 s. Model ($\ln N$ linear, $T_{1/2} = \ln 2/(-k)$) and its condition are right. s1 c–d, s2 a ($E_0$ symbol, 656,5 nm), s3 d ($W = -eb$, $f_0 = -b/k$ = 5,43·10¹⁴ Hz), s6 b recomputed. The fi, fi-easy and en diffs carry identical mathematics (every changed formula compared token by token); answers.py run; `units.py check` passes.
