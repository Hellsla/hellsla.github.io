VERDICT: PASS
CONTENT-HASH: 2099e517d51d3416
SCOPE: full (focus: the three new ```pysahdy boxes in unit.md; figures redrawn as WebP; solutions.md split into paragraphs)

## Blocking
None.

## Polish
- Box 2 (spark of 2 mm): the answer uses "=" for $3\,\text{MV/m} \cdot 2\,\text{mm} = 6\,\text{kV}$ after "$\approx$". The Finnish version does the same, and it is correct.
- The Polish items from my previous report on s7 and s8 (plate gap not stated, the vacuum vs breakdown comparison, $R_\text{min} \approx 125\,\Omega$ from the drawn curve) still apply. They are unchanged and not blocking.

## Checked
- I ran `units.py hash fy9-sahkokentta --lang en` at the start and the end: 2099e517d51d3416 both times.
- **Pysähdy boxes.** I compared all three with `content/fi/units/fy9-sahkokentta/unit.md` (same lines 13, 84, 169). The physics, numbers and units are the same as in fi:
  - Box 1: the electron is negative, so $\overline{F} = q\overline{E}$ points against the field, that is, left. Correct.
  - Box 2: $U = E_\text{max}d = 3\,\text{MV/m} \cdot 2\,\text{mm} = 6\,\text{kV}$. Correct, and consistent with the 3 mm → 9 kV of the text.
  - Box 3: $C \propto 1/d$, so doubling $d$ halves $C$. This holds under the conditions stated in the paragraph just above: $d$ is small compared with the plates and the dielectric fills the gap.
  - Each box sits right after the paragraph it tests.
- **Diff since the passed version (33c3acb83).**
  - unit.md: apart from the boxes, only the drawn SVG shapes were replaced by WebP images. The LaTeX labels are unchanged.
  - solutions.md: I compared the old and new text word for word (whitespace normalised). It is identical apart from the s1 image swap, so the change is paragraph splits only.
  - tasks.json, inquiry.json, exit-ticket.json and answers.py are unchanged.
- **New images.** I looked at each one against its physics:
  - `levyt`: field down from the + plate to the − plate, proton force down, electron force up.
  - `kipina`: induced + on the handle, − on the finger, and the field lines point from the plate to the finger.
  - s1 FBD: weight down, horizontal repulsion away from the other ball, tension along the thread. The drawn components close the triangle: T·cos α ≈ G and T·sin α ≈ F_s. No velocity or extra force is drawn, and the enlarged angle is stated in the text.
  - hero: an illustration only.
- **Recomputation.** My own script (`recalc.py` in the session scratchpad; it uses its own formulas and prints its values beside answers.py's) agrees on:
  - the boxes;
  - the spark paragraph: 9 kV, 0.9 µC, 4.05 mJ ≈ 4 mJ, and 0.05 C / 0.9 µC ≈ 5.6·10⁴ > 50 000;
  - s1: 0.493 mN, 18.7 nC, 0.247 mN, 6.35 cm;
  - s2: 184 pF, 0.830 µC, 1.87 mJ, 804 V, 0.334 mJ;
  - s6: 40.2 km/s, 87.5 mN, 349 m/s, 1.76 kW;
  - s7: 5.0 kV/m, 2.41·10¹¹ m/s², 98.2 km/s;
  - s8: 17.3 mA, 65.6 mW, 127 Ω.
- **Theory text.** The formulas and their stated conditions are correct: the parallel-plate condition, the work being path-independent, $\lvert Q\rvert U$ in the derivation, the dielectric strength giving $U_\text{max} = E_\text{max}d$, and the efficiency formula for perpendicular light marked as non-MAFY. The common mistakes are physically right. The scope stays within FY6 (plus FY4 for s6).
