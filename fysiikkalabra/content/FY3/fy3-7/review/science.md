VERDICT: FAIL
CONTENT-HASH: ca90d49523679b44

## Blocking
- exercises.json L1-03 against solutions.md:29: the task says the 45 kg/m² freezes "Syksyn ensimmäisenä pakkasyönä", but the check now says 4,5 cm "sopii pakkasviikon aikana jäätyneeksi kerrokseksi". So the check no longer confirms the task. It says the stated scenario is unrealistic. A loss of 15 MJ/m² in one night of 12 h needs about 350 W/m², which is far more than a lake loses; over a week it is about 25 W/m², which is plausible. Fix: in the task, "Syksyn ensimmäisellä pakkasviikolla järven pintaan jäätyy 45 kg vettä…". The answer stays 15 MJ.

## Polish
- inquiry.json siirto: the Vastaus line gives 1,9·10² W, but `answer` is 188. Both are inside the tolerance. Still, give one value: either `answer: 190`, or say that 188 W is accepted.
- inquiry.json check-2, Vastaus: "teho 1500 W on annettu kolmella numerolla" cannot be read from 1500 W, which is ambiguous. The time difference 15,0 min alone justifies three figures.

## Checked
- Round-1 Blocking items are fixed. L1-05 now has the right rounding reason: both readings are to the nearest kJ, so their difference 167 kJ is too. Its check says "lähes yhdeksän kertaa", which is right (167/18,9 = 8,8). Two of the round-1 polish items are fixed: L3-03 now names the difference 106 g, and L1-03 was reworded (the new wording causes the Blocking finding above).
- answers.py and my own recomputation agree on all 12 exercises. They also agree on siirto (188,3 W), check-2 (0,597 kg) and the example (2,344 MJ/kg, +3,7 %, 133 g, 4,7 g ≈ 5 g). The mistake values are right: 27,8 W, 11 300 W, 0,677 kg and 4,04 kg.
- Every solution's principle applies, with the right reason. L3-01 tests that all the ice melts (36,7 kJ > 20,0 kJ). In L3-03 the loss power cancels (60,4 W).
- The conversions are right: g→kg, kJ/MJ→J, min/h→s. ΔT has the same value in K and in °C.
- Every Vastaus line names the datum that limits the figures. L1-05, L3-03 and check-2 use a difference of readings.
- Every reasonableness number is right: 2,7 kg, 54 K, 3,9 cm (ice at 920 kg/m³), 90 %, 24 %, 87 %, 540 K, 21 °C and 11,7 K, 0,54 kg and ×7,5, 2,52 kJ and ×9,6.
- The lesson ratios are right: r/s = 6,8, r/(c·100 K) = 5,4, and s ≈ c·80 K. The pred-1 and pred-2 numbers are right: 1130/565 s, 83,5/565 s and 167/1130 s.
- The lesson text, figures and sim are unchanged since round 1 (git diff 9ffbed9..ee66002 touches only solutions.md and siirto). Their round-1 checks hold.
- Hash at start and end: ca90d49523679b44.
