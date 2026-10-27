VERDICT: PASS
CONTENT-HASH: 8dc08d0f5628bf05

## Blocking

## Polish
- solutions.md:98 (L3-01): the split substitution drops units from the numerator 16 622,5 and the denominator 1717,9, and then attaches °C to the quotient. The values are right. Writing 16 622,5 J and 1717,9 J/K (quotient 9,68 K, so T = 0 °C + 9,68 K) would make it plain why the result is a temperature. Its T₀ = 0 °C term is already explained under Muunnokset.
- Carried from round 2, still open: in inquiry.json siirto the Vastaus line says 1,9·10² W but `answer` is 188. In check-2 the claim "1500 W on annettu kolmella numerolla" cannot be read from the value. In L2-02, 279 kJ would also be defensible. None of these is blocking.

## Checked
- Since the PASS at d217123, the only lesson change is solutions.md L3-01. One long fraction was split into a numerator, a denominator and a display equation (git diff d217123 -- content/FY3/fy3-7).
- I recomputed the new intermediate values. 4190·0,35·25 = 36 662,5. 334 000·0,060 = 20 040. The difference is 16 622,5. 4190·0,41 = 1717,9. The quotient is 9,676, so 9,68 °C and then 9,7 °C. The check figures are right too: 21,3 °C and 11,7 K, so "yli 11 K".
- The physics of L3-01 is unchanged and correct. The juice could give 36,7 kJ, more than the 20,0 kJ needed, so all the ice melts. The energy balance and the symbolic solution come before the numbers.
- I recomputed everything in one script. answers.py, exercises.json and my own formulas agree on all 12 exercises, with every deviation 0,44 % or less. They also agree on siirto (188,3 W; mistakes 27,8 W and 11 300 W), check-2 (0,597 kg; mistakes 0,677 kg and 4,04 kg) and the example (2,344 MJ/kg, +3,7 %, 133 g).
- Nothing else in the lesson changed: lesson.md, inquiry.json, exercises.json, figures and sim.js are identical to round 2. My round-2 checks of principles, conversions, rounding, reasonableness checks, figures and the sim still hold.
- Hash at start and end: 8dc08d0f5628bf05.
