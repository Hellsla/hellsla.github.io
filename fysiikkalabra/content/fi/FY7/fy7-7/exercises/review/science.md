VERDICT: FAIL
CONTENT-HASH: 8d88f4983a8ef167

## Blocking
- exercises.json:270 (L3-04) — **A**, unrealistic data for the device named. A hub dynamo turns with the wheel, so f = 5–30 Hz means 5–30 wheel turns a second, about 38–227 km/h on a 2,1 m wheel. A real hub dynamo is also multipole, so the single-coil model e₀ = NBA·2πf with f as the wheel rotation rate does not describe it. — Fix: change the device to a "pullodynamo" (roller on the tyre wall: 5–30 r/s is walking to slow cycling speed), or to "opetusgeneraattori", in exercises.json:270, the caption and solutions.md:178–188. The numbers can stay.

## Polish
- solutions.md:135 (L2-06 c) — the prediction 8,2 V = 2 · 4,1 V carries twice the reading uncertainty (±0,2 V), so the combined uncertainty is about ±0,3 V, not that of "kahden lukeman" (0,2 V). The conclusion still holds. Also write "ei voida osoittaa eroa", not "tukee verrannollisuutta" alone (guardrail: overlapping ranges do not prove equality).
- exercises.json:125 (L2-05) — `kind` lists "graph", but the task has only a table. Either drop "graph" or ask for a sketch of e(t). The plan's `trace`/`phi-e` follow-up (three rotation rates → NBA) was not made.
- solutions.md:181 (L3-04) — "Pyörimättömässä käämissä jännite on nolla" is the right physical reason for the line through the origin. Calling c = −0,11 V a measurement error should be "todennäköisesti" (it is within ±0,1 V reading).

## Checked
- Every answer recomputed in one script with my own formulas (L1-07 20 ms, L1-08 12,02 V, L2-05 5,94 V / T 24 ms / 41,7 Hz, L2-06 2,44 %, L2-07 0,261 A, L3-04 k 0,308 V·s, c −0,107 V, B 0,3404 T, L3-05 22,2 / 56,85 / 113,7 W): all equal answers.py and exercises.json.
- L2-05 table: within ±0,1 V of 8,4 sin(2πt/24 ms), a genuine sinusoid over 26 ms (more than one period).
- L3-04: a fit forced through the origin gives 0,335 T, inside the 4 % tolerance. The 22 Hz prediction 6,67 V vs 6,78 V (1,6 %) is right.
- L3-05: P ∝ f² reasoning right; mean power = half the peak power; 1,1·10² W rounding right.
- L1-06 exactly one correct option, feedback right; L2-07 error identified correctly.
- Notation matches the lesson; unknowns solved symbolically; conversions right.
- Levels fit: L2 data/experiment/error tasks, L3 modelling and multi-step. No duplicate of the existing L3 tasks.
