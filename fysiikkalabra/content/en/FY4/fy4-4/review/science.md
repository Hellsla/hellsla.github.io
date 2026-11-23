VERDICT: PASS
CONTENT-HASH: 5c04f349d4da89af

## Blocking

## Polish

## Checked
- inquiry.json exp-2 `min` 2 -> 3 and pred-2 `reveal.min` 2 -> 3: the sim's mass selector offers exactly three values (0.50, 1.0, 1.5 kg, sim.js:52), so three distinct rows with F = 1.0 N locked are reachable; simState gives `m` and `a`, so the measured keys exist at those values. Expected model values a = 2.0, 1.0, 0.67 m/s^2 show the inverse relation better than two points.
- The change brings the English version into line with the Finnish inquiry.json, which already has `min` 3 for exp-2 and pred-2.
- pred-2's correct option and feedback (2.0 m/s^2 at 0.50 kg, 1.0 m/s^2 at 1.0 kg) are unchanged and still agree with a = F/m.
- lesson.md crane example: only the alignment points of the two aligned blocks moved (`&` before `=`); the equations, order (sigma F = ma, then T - mg = ma, then a symbolically) and numbers are unchanged. Recomputed: mg = 480 kg * 9.81 m/s^2 = 4708.8 N, a = (5200 - 4708.8) N / 480 kg = 1.023, about 1.02 m/s^2.
- The continuation rows `&= 4708.8 N` and `&\approx 1.02 m/s^2` still read as mg and a, the same as the removed `\phantom` rows.
