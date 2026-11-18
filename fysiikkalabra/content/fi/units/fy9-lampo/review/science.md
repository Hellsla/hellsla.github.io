VERDICT: FAIL
CONTENT-HASH: 105a4152a036315b
SCOPE: delta: new tasks fy9-lampo-s7 (figure fy3-6/heating-line) and s8 (figure fy3-7/melting-curve) and the changed intro; s1-s6 not re-judged.

## Blocking
- s8 a (A, assessment correctness 7): the start point (0 kJ; -16 °C) is not on a grid crossing and -16 °C appears nowhere the student can read (only in the figure's aria-label). It lies between the -10 °C gridline and the unlabelled -20 °C axis. Reading -15 or -17 °C gives 2,2·10³ or 2,0·10³ J/(kg·K), outside the 2 % tolerance of 2083: a fair reading is marked wrong. The figure's own chapter exercise (fy3-7) states -16 °C in its text. Fix: state the initial temperature -16 °C in "jääpalaa … lämmitetään tasaisesti" (s8 text) (the graph is still needed for the Q values), or accept a reading range in a.

## Polish
- s8 b, d call 333 kJ/kg "the table value", while s1 data and s5 in the same set use 334 kJ/kg (P9 allows both).
- s8 text: "the temperature of the ice": after 220 kJ the graph shows the meltwater; "the temperature of the ice/water" would be exact.

## Checked
- Independent recomputation from the figures' own points (heating-line (0; 20)→(180; 60), grid crossings; melting-curve (0; -16), (20; 0), (220; 0), third segment slope 0,3984 K/kJ ⇒ c_w = 4,18 kJ/(kg·K), consistent with the text): s7 a 0,222 K/s, b 900 J/(kg·K) (0,45 % from Al 896), c 360 s (Al 358 s); s8 a 2083, b 333,3 kJ/kg, c 270,2 kJ, d 0,300 kg (wrong-path 0,36). All match tasks.json and answers.py; tolerances admit the 2-figure roundings.
- Constants: Al 896 J/(kg·K) and water 4,18 kJ/(kg·K) as MAFY.
- Rounding: two figures follow the data and grid readings.
- Both tasks need their figures (ΔT, Δt, Q-values only there).
- Physics: s7 d mechanism right (loss grows with temperature difference, net power falls, levels off); s8 b plateau = melting, Q = sm. P1 wording: energy → internal energy, transferred to the surroundings as heat; no "lämmöksi".
- Rubric points add up (s7 3+4+4+3, s8 4+5+4+3; set 125); criteria match the parts.
- Intro: eight tasks, topics consistent.
- practice.py check OK; hash stable at start and end.
