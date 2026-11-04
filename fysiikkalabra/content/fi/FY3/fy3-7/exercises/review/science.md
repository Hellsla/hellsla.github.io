VERDICT: PASS
CONTENT-HASH: 6adc73b630c26584
Round: 3

Round 3 checks the last commit (`git show HEAD -- content/fi/FY3`), which touches only fy3-7 L2-05 (tolerance and Vastaus line); the rest is covered by the round-2 PASS.

## Blocking
- none

## Polish
- none

## Checked
- Arithmetic: s = 600 W · 139 s / 0,250 kg = 333 600 J/kg, so 334 kJ/kg. 334 · 0,95 = 317,3 kJ/kg, so the accepted range is 317,3..350,7 kJ/kg. The naive table-row reading 600 · 130 / 0,250 = 312 kJ/kg is 6,6 % low and is now rejected, as the Vastaus says ("liian pieni").
- Careful readings still pass: Δt = 137..141 s gives 328,8..338,4 kJ/kg, and even Δt = 133 s gives 319,2. Only Δt below about 132,2 s fails.
- Tolerance 0,05 in exercises.json, "±5 %" in the Vastaus line, and the answer 334 kJ/kg agree with the task text (hint to estimate start and end from the slopes) and with the solution (18 s, 157 s, 139 s). The lesson-level answers.py is not used by the exercise set; the exercise answer is in exercises.json.
- Physics unchanged: slopes 1,14 K/s and 0,575 K/s agree with P/(cm).
- The hash was the same at the start and at the end.
