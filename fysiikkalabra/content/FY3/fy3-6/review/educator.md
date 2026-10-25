VERDICT: FAIL
CONTENT-HASH: b3c4e9982c3bef92

## Blocking
- lesson.md:23, lesson.md:71, exercises.json — The goal skill "useita termejä sisältävän suureyhtälön ratkaiseminen" is never shown or practised where it is hard, solving the balance equation for T (unknown on both sides). The example solves for c by one division, L3-01 solves for m, and line 71 only asserts "35 °C". — Fix: at line 71 show the working in display math: 3,0 kg·(T − 20 °C) = 1,0 kg·(80 °C − T), so 4T = 140 °C and T = 35 °C (c cancels). Replace L2-04, which only rearranges for c as L2-03 does for ΔT, with a two-substance mixing task asking for T, e.g. 0,25 kg of aluminium at 95 °C in 0,40 kg of water at 18 °C. Update answers.py and solutions.md.

## Polish
- lesson.md:17, :21 — Line 17 makes Q negative on cooling, but line 21 writes (T₁ − T) for the hot body without saying why. — Define ΔT = T_loppu − T_alku at line 17. After line 21 add that both sides are magnitudes, so the hot body uses alku − loppu.
- lesson.md:8 — C = cm appears only inline, yet line 68 and the exit ticket use it. The house rule requires one display formula. — Give C = cm a display line in `## Kaava`.
- lesson.md:8 — The hook is credited only to c; water also mixes to depth and evaporates. — Replace "Siksi" with "Tärkeä syy on, että…".
- lesson.md:68 — 1257 J/K and 75 J/K appear without working. — Write "0,300 kg · 4190 J/(kg·K) ≈ 1260 J/K".

## Checked
- Lint: 0 errors, 0 warnings. The proofreader's diff is already applied.
- Prerequisites are covered: Q, sign convention and isolated systems (fy3-5); ΔT is the same in K and °C (fy3-3); P = W/t (fy3-2), used in L2-02.
- The hook is a question students actually ask, and line 8 answers it.
- Each Ydinajatus paragraph adds one idea.
- Level 1: all five use Q = cmΔT once, with c from the table.
- Level 2: each has one conversion, two steps or one rearrangement.
- Level 3: each needs reasoning (the stones' final T, the cancelling area, density vs c).
- No exercise repeats the worked example.
- The exit ticket tests the formula, the meaning of c and the "not an average" idea.
- meta.json matches curriculum.json.
