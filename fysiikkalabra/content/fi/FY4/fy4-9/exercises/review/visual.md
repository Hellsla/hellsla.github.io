VERDICT: FAIL
CONTENT-HASH: d2dfe6f7b0e18bab

## Blocking
- [Major] solutions.md fy4-9-L2-07, "Kuvaajan lukeminen" (open-exercises-L2-1280-9) — says "kuvaajan alle jää kuusi puolisuunnikasta", but the table has 8 points (0…70 ms) and so 7 intervals, hence 7 trapezoids (the first, 0 to 11,0 N, and the last, 10,0 N to 0, are triangles-as-trapezoids) — a student who counts gets a different number than the model solution, and the sum "Δt · ΣF" is correct only for the 7-interval reading — change to "seitsemän puolisuunnikasta".

## Polish
- [Minor] solutions.md fy4-9-L1-08 Muunnokset (open-exercises-1280-8) — "$\dfrac{36\,\text{m}}{3{,}6\,\text{s}}$" reads as 36 m in 3,6 s (the same pattern was flagged in L2-01) — write "$v = 36\,\text{km/h} = \dfrac{36}{3{,}6}\,\text{m/s} = 10\,\text{m/s}$".
- [Minor] solutions.md fy4-9-L1-08 Järkevyys — "noin satakertainen kävelevän ihmisen liikemäärään ≈100 … verrattuna" is clumsy and the ratio is about 180 — "Liikemäärä on noin 180-kertainen kävelevän ihmisen liikemäärään ($\approx 100\,\text{kg}\cdot\text{m/s}$) verrattuna, mikä sopii pakettiautolle." (for science: check the ratio.)
- [Minor] exercises.json tables of L2-07, L3-05 (open-exercises-L2-1280-9, L3-1280-7) — the column header is centred or left over values aligned right or left, so header and numbers do not line up (L2-07 "$F\,(\text{N})$", L3-05 "$t\,(\text{s})$"); align numeric headers like their values (page CSS, developer).
- [Minor] solutions.md fy4-9-L3-05 Vastaus (open-exercises-L3-1280-9) — one paragraph also carries a) and c) results; fine, but the b) result "$4{,}5 \cdot 10^2\,\text{N}$" differs from the answer-box value 447 without saying it is rounded.
- [Minor] carried over: ex-potku graph tick "$1$" vs "$1{,}0$" (L3-01), the chain layout of left sides (developer).

## Checked
- Source of all new tasks L1-06…08, L2-05…07, L3-04…05 (text, tables, full solutions); numbers recomputed (sums 110,0/51,0/144,0/98,1; answers match).
- open-exercises-1280-6, -8 (L1-06 solution, L1-07, L1-08 solution), L2-1280-6, -8, -9 (L2-05, L2-06, L2-07), L3-1280-6, -7, -8, -9 (L3-04, L3-05); 1280 px only, no per-task 390 captures exist; layout checks 360/768/1280 clean per packet.
- No plain number+unit in student text; no figures in these tasks (tables only).

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
