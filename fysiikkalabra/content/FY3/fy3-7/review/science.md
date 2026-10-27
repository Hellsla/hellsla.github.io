VERDICT: PASS
CONTENT-HASH: 2027383a0b3b19e2

## Blocking

## Polish
- inquiry.json siirto: the Vastaus line gives 1,9·10² W, but `answer` is 188. Both are inside the tolerance. Give one value: either `answer: 190`, or say that 188 W is accepted.
- inquiry.json check-2, Vastaus: "teho 1500 W on annettu kolmella numerolla" cannot be read from 1500 W, which is ambiguous. The time difference 15,0 min alone justifies three figures. The check's "samaa suuruusluokkaa" is fair: 180 kJ heats the 0,597 kg that boils away from about 28 °C, not from 20 °C.
- solutions.md:69 (L2-02): −18 °C limits only the small term Q₁ ≈ 28 kJ. The sum 278,85 kJ is good to about 1 kJ, so 279 kJ would also be defensible. 280 kJ follows the school rule "as precise as the least precise datum" and is inside tolerance, so this is not blocking.

## Checked
- Round-2 Blocking item is fixed. L1-03 now says "pakkasviikolla", which matches its check. 15 MJ/m² over a week is about 25 W/m², which a lake can plausibly lose. The 4,5 cm in the check is the thickness of the water layer, and the check calls it that (ice would be 4,9 cm). The answer is still 15 MJ.
- I recomputed everything in one script. answers.py, exercises.json and my own formulas agree on all 12 exercises, with every deviation 0,44 % or less. They also agree on siirto (188,3 W; mistakes 27,8 W and 11 300 W), check-2 (0,597 kg; mistakes 0,677 kg and 4,04 kg) and the example (2,344 MJ/kg, +3,7 %, 133 g, about 5 g).
- In every solution the principle applies, for the right reason. L3-01 tests that all the ice melts (36,7 kJ > 20,0 kJ). In L3-03 the loss power cancels (60,4 W), and the single runs give 2,45 and 2,67 MJ/kg. In the example, losses make r too large, which is the right direction.
- Conversions are right (g→kg, kJ/MJ→J, min/h→s), and ΔT has the same value in K and in °C. Every Vastaus line names the datum that limits the figures. L1-05 and L3-03 use the precision of a difference.
- Every reasonableness number is right: 2,7 kg, 54 K, 3,9 cm, 90 %, 24 %, 87 %, 540 K, 21 °C, 11,7 K, 0,54 kg and ×7,5, 2,52 kJ and ×9,6.
- The lesson ratios are right: r/s = 6,8, r/(c·100 K) = 5,4, and s = c·80 K. The heating-curve slopes are ice 1,97, water 0,98 and steam 1,96, which match c ratios of 2,0 and 2,1. The plateaus are labelled "not to scale". The phase diagram's melting line has a negative slope, as it should for water.
- Sim: stateAt and stages implement the five-stage model, and the plateau lengths are sm/P and rm/P. The piston keeps the pressure at 101 kPa, and the text says so, with the open-pot and rigid-vessel limits. In exp-1 and exp-2 one parameter is locked and the other varied, and the measured keys tMelt and tBoil are in simState. pred-1 and pred-2 numbers are right: 1130/565 s, 83,5/565 s and 167/1130 s.
- Since round 2, only the L1-03 text in exercises.json has changed (git diff ee66002..3c205de).
- Hash at start and end: 2027383a0b3b19e2.
