VERDICT: PASS
CONTENT-HASH: 95b438af4632227f
SCOPE: delta added-exercise from 35a961c55c19b541 base 81db4a6fd727

## Blocking
(none)

## Polish
(none)

## Checked
- fy3-16-L1-09 (new situation: boiling pot on a hob): water already at 100 °C, so Q = r m = 2260 kJ/kg * 0.30 kg = 678 kJ, answer 680 kJ in two figures; 4 % tolerance covers other table values (2257 kJ/kg); the check 678/126 = 5.4 times the warming heat 0-100 °C is right.
- fy3-16-L2-09: constant power, no losses stated in the task; read (0 s; 20 °C) and (180 s; 60 °C) on grid crossings of heating-line; c = P t / (m Delta T) = 400 * 180 / (2.0 * 40) = 900 J/(kg K), as answers.py. The note that losses make the true c smaller is the right direction (less heat reaches the block for the same Delta T).
- fy3-16-L2-10: figure melting-curve gives (0; -16), (20; 0), (220; 0) kJ/°C; my own check c_ice m Delta T + s m = 2100 * 0.60 * 16 + 334 000 * 0.60 = 20.2 + 200.4 = 220.6 kJ agrees with the graph; t = 220 000 J / 25 W = 8800 s = 2.44 h, answer 2.4 h inside the 3 % tolerance.
- L2-10 conditions: the temperature stays at 0 °C while the ice melts (pure substance at constant pressure), constant transfer power stated in the task; the slope after melting (80 kJ for 31.9 K) matches c_water * 0.60 kg, so the figure is consistent to scale.
- Solutions complete: given, principle, symbolic formula first, conversions (kJ to J, s to h), substitution, rounding reason, an independent check.
- Scripted comparison with the Finnish exercises.json: all 24 exercises have the same answers, units, tolerances, figures and task-text numbers; every answers.py value within its tolerance.
- Hash identical at start and end.
