VERDICT: PASS
CONTENT-HASH: b91a832e250a3f5f
SCOPE: delta: en tasks fy9-tasavirta-s7 (fy6-3/lamp-curve) and s8 (fy6-4/siirto-mixed) in sovella/tasks.json and solutions.md, and the changed intro (git diff 49ba8f9 HEAD); fidelity to fi; s1-s6 not re-judged. Language: en.

## Blocking
(none)

## Polish
- s7 b reasonableness argues from the curve getting steeper, while part a rightly says the slope is not the resistance; "the line from the origin to the point gets steeper" would argue U/I directly.
- s8 d: 1.35 W carries three figures where the data carry two (1.4 W).
- s8 symbols: the solution names 20 ohm R3 and 60 ohm R1, the figure labels 20 ohm R1, 60 ohm R2, 30 ohm R3; values are written beside every symbol, so harmless.

## Checked
- Recomputed in one script, the lamp current from the figure model (lessons/FY6/fy6-3 figures.py lamp_I): I(2.0 V) = 0.208 A, so R = 9.6 ohm, and the 0.21 A reading gives 9.5 ohm (0.20-0.22 A gives 10-9.1 ohm, inside 6 %); I(3.0 V) = 0.25 A, R = 12 ohm; U_R = 1.0 V, R = 4.0 ohm, check 16 - 12 ohm; P_L 0.75 W, P_R 0.25 W, P 1.0 W, 75 %. s8 Rp = 20 ohm, R = 40 ohm, I = 0.30 A, Up = 6.0 V, 0.10 and 0.20 A, P20 = 1.8 W, P = 3.6 W (1.8 + 0.60 + 1.2); d 80 ohm, 0.15 A, 9.0 V, 1.35 W, ratio 2.25.
- Physics: R = U/I at a point for a non-ohmic lamp; hot filament, stronger lattice vibrations, resistance grows; series resistor takes E - U_L; neglected internal resistance stated in the task, so P = EI valid; d prediction (current falls, 20 ohm drop falls, 60 ohm voltage and power rise) correct. Scope FY6.
- Assessment: criteria sum to part points (s7 4+3+5+4, s8 5+5+4+4); criteria ask only what the parts ask; alternatives accepted.
- Fidelity to fi: ids, figures, points, criteria, answers and tolerances identical; every number in s7/s8 text, criteria and solutions matches fi.
- Intro: "Eight problems", matches.
- Hash b91a832e250a3f5f (units.py hash --lang en) at start and end.
