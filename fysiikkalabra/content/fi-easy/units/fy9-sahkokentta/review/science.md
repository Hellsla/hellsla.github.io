VERDICT: PASS
CONTENT-HASH: f9bba1ca0381a58c
SCOPE: full, with the three new ```pysahdy boxes in unit.md judged first. The diff since the last PASS (894eada2c0c82540) is only these boxes plus three figures (hero, kipina, levyt) whose drawn SVG was replaced by the shared WebP images. The LaTeX labels are unchanged.

## Blocking
None.

## Polish
- teacher.md, Arviointi: it says "muut viisi … (15 pistettä kukin). Yhteensä 95". The set has eight tasks (7 × 15 + 20 = 125 points), and the 65–75 min row also says "muut viisi tehtävää". The same text is in the Finnish teacher.md, which was written before s7 and s8 were added. Correct both languages together.
- s7 b, Järkevyys: "noin $2 \cdot 10^{10}$ kertaa pienempi". My value is $2{,}5 \cdot 10^{10}$. As an order of magnitude it is fine.
- The earlier Polish points still apply: s7 does not state the plate gap, s7 a compares with the breakdown field of air although the plates are in a vacuum, and s8 c could accept about $125\,\Omega$.

## Checked
- I ran `units.py hash --lang fi-easy` at the start and at the end: f9bba1ca0381a58c both times.
- I compared all three pysahdy boxes with fi. The physics, numbers and reasoning are the same:
  - Electron in a field pointing right: the force points left, because $q<0$.
  - $U = Ed = 3\,\text{MV/m} \cdot 2\,\text{mm} = 6\,\text{kV}$.
  - $C \propto 1/d$, so doubling $d$ halves $C$. fi-easy says "d on jakajana" where fi says "kääntäen verrannollinen". That is correct and keeps the condition "muu pysyy samana".
  - Each box sits after the paragraph it practises, and none of them contradicts the theory, the Virheet list or the inquiry (lt-2, lt-4).
- The replaced figures. In levyt the field points down from + to −, the proton's force points down and the electron's force points up, which matches the labels and the aria-label. In kipina the field lines run from the + plate to the − fingertip, and the gap bar matches $d \approx 3\,\text{mm}$.
- Recomputation (scratchpad `recomp.py`): 80 values from my own formulas. They cover:
  - the hook numbers (9 kV, 0,9 µC, 4 mJ)
  - every inquiry answer and every mistake value (7264 km/s and the three wrong values; 35,95 µN; 6,008 pF; 1690 V; 3,865 h and the three wrong values; 112,6 mJ)
  - the choice feedbacks (43×, 190 Ω / 8,5 mA, 5,0 µF / 0,49 mJ)
  - s1–s8, including the exact non-small-angle s1 d (6,35 cm), my own least-squares fit for s3 (354 pF·mm, 22 pF, 8,84 pF/m), the s5 power column, the s6 momentum and energy cross-checks, and s7 and s8.
  - All agree within rounding. The only differences are "noin 12 kV" for $20/\sqrt3 = 11{,}5\,\text{kV}$ (fine) and the s7 ratio above.
- Every choice question has exactly one correct option, and each distractor's feedback is physically right. The point totals of every task and part add up. Rubric criteria ask only what the tasks ask. "Sisäenergiaksi" is used throughout. The scope is FY6, with FY4 and FY1 links only.
