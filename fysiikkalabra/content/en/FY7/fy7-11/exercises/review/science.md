VERDICT: PASS
CONTENT-HASH: ab4937454aa19c11

## Blocking

## Polish
- exercises/review/packet-science.md:57 — The "Exercise brief" block is empty for en, probably because review_packet.py looks for the Finnish section headings. I judged the exercises against the en lesson as seen in the lesson packet. Fix the packet tool to look for "Formula / Worked example / Common misconception / Summary" (not a content finding).

## Checked
- Every number in exercises.json and solutions.md equals the Finnish source after normalising the decimal separator. The ids, answers, tolerances and units are identical.
- Recomputed in one script from the task text: L1 35.107°, 196 078 km/s, 1.5161, 37.0°, 42.0°; L2 265.0 ns, 34.983°, 183 038 km/s (n = 1.639 read; key 183 072 from 1.6387, within 2 %), 15.646°; L3 0.9659°, 30.703°, 1.6650° (key 1.6647, within tolerance).
- L2-03 figure: the flint curve gives n(450) = 1.63866, between the 1.638 and 1.640 grid lines as the solution says. The en aria-label (figures.json) is translated and gives no answer. The axis labels use a decimal point.
- L2-01 states the assumption v = c : n, and the solution names group velocity as what is ignored (a condition is stated, so this is not a B).
- L2-04 / L3-02 / L3-03: θ = 4β − 2α; the top of the arc is at θ − h; 30.7° < 42.3° is inside the arc; a width of 1.66° is about 3 sun diameters.
- The rounding reasons (difference of nearly equal numbers, limiting data) and the symbolic-first steps carry over correctly in English.
