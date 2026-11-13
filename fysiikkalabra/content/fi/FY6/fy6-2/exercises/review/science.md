VERDICT: FAIL
CONTENT-HASH: 6d39d0db9b9030ff

## Blocking
- content/fi/FY6/fy6-2/exercises/exercises.json:309 — (A, assessment) fy6-2-L2-10 rejects a correct method. The lesson tells the student to round an error limit to one significant figure (ΔU = 0,03 V, exactly as fy6-2-L2-09 and this solution's own check "välin 1,34 V–1,40 V" do); then 0,08 V : 0,03 V = 2,67, which is 10,5 % from the answer 2,98 and outside `tolerance` 0.1. The difference 0,08 V has only one significant figure anyway, so the ratio is "about 3" either way. — Widen `tolerance` to 0.15 (2,67…3,0 both accepted), or say in the task to use the unrounded error limit; keep the conclusion (difference about three error limits, not consistent).

## Polish
- content/fi/FY6/fy6-2/exercises/solutions.md:227 — Vastaus "noin 3,0 kertaa" gives two figures although U₀ − U = 0,08 V has one; "noin 3 kertaa" would match the data's precision.

## Checked
- Hash 6d39d0db9b9030ff at start and end; delta: only fy6-2-L2-09 and fy6-2-L2-10 judged.
- Figure generator: display 1,37 V, pointer at −35° = the 20 V range (highlighted), ranges 2 V, 20 V, 200 mA, 10 A, sockets COM / V mA / 10 A; alt text gives the same reading and range and no error limit. A 20 V range showing two decimals (resolution 0,01 V) agrees with the lesson's table.
- L2-09 recomputed: ΔU = 0,005 · 1,37 V + 2 · 0,01 V = 0,02685 V ≈ 0,03 V; the rounded 0,03 V is 11,7 % off and inside tolerance 0.12. Solution complete, symbolic Δx = p·x + n·r first, rounding by the lesson's rule, sensible check (digits dominate at a small reading).
- L2-10 recomputed: (1,45 V − 1,37 V) : 0,02685 V = 2,98; criterion "difference larger than the error limit → not consistent" is the lesson's use of the manufacturer's limit; 1,45 V lies outside 1,37 ± 0,03 V. The suggested cause (lamp run at a voltage other than its rating) is physically sound.
- Both tasks within the lesson's taught content (error-limit formula, range resolution); notation Δx, p, n, r as in the lesson.
