VERDICT: FAIL
CONTENT-HASH: df48e4dcb6b9a326
SCOPE: delta: new tasks fy9-tasavirta-s7 and s8 and the changed intro of the unit's Sovella set (fi-easy); s1–s6 not re-judged. Line 2: unit hash (units.py, read by the gate); task-set hash (practice.py) a7a058b9720f1015; both unchanged start to end.

## Blocking
- B (s7, model condition; task text, c solution and c criteria): the task says only "Lamppua halutaan käyttää $4{,}0\,\text{V}$:n paristosta." The whole of c and d takes the battery's terminal voltage as exactly 4,0 V at 0,25 A ($E = U_\text{L} + U_\text{R}$, "in parallel the lamp would have the whole 4,0 V", $P = EI$ = total power). That holds only for a battery with negligible internal resistance, which the text never states, in a set whose own s1 d and s3 teach internal resistance. s8 states the assumption; s7 must too. Fix: add "Pariston sisäinen resistanssi jätetään huomiotta" (en: "The internal resistance of the battery is neglected.") to the task text, and name the assumption in c's Annettu/Periaate.

## Polish
- s8 d: $P_{60}' = 1{,}35\,\text{W}$ is given to three figures where the data carry two ($1{,}4\,\text{W}$); the ratio is right as $2{,}25 \approx 2{,}3$.
- s8: symbols put $R_3$ in series, the reverse of fy6-4's figure convention; harmless (figure shows values).

## Checked
- Lamp curve recomputed from fy6-3 figures.py ($I = U/(1 + 11(U/3)^{0{,}6})$): $I(2{,}0\,\text{V}) = 0{,}208\,\text{A}$ (read 0,21 A on the 0,05 A grid is fair), $R = 9{,}6\,\Omega$ from the curve, 9,5 from the reading; 9,1 to 10 (readings 0,22 to 0,20 A) all inside the 6 % tolerance. $I(3{,}0\,\text{V}) = 0{,}250\,\text{A}$ at the end point, $R = 12\,\Omega$; ratio 1,26. Slope $dU/dI$ at 2,0 V is 21 Ω, so "the slope is not the resistance" is a real distractor; slope rises monotonically ("steepens the whole way" true).
- b physics: filament heats, lattice vibrations raise R, nonlinear U–I: correct.
- c: series resistor, $U_\text{R} = 1{,}0\,\text{V}$, $R = 4{,}0\,\Omega$, check 16 − 12 Ω; d: 0,75 + 0,25 = 1,0 W, 75 % (apart from the blocking condition).
- s8 (topology checked in fy6-4 figures.py): $R_\text{p} = 20\,\Omega$, $R = 40\,\Omega$, $I = 0{,}30\,\text{A}$, bounds 0,60 and 0,11 A, $U_\text{p} = 6{,}0\,\text{V}$, 0,10/0,20 A, 1,8 + 0,60 + 1,2 = 3,6 W; d: 80 Ω, 0,15 A, 9,0 V, 1,35 W, ×2,25. The prediction (current falls but the 20 Ω drop falls, so the 60 Ω voltage and power rise) is correct and the criterion asks exactly it.
- answers.py agrees; points add up (16, 18); two figures as data; FY6 scope; data labelled invented.
- Fidelity to fi: every part, point, answer, tolerance and criterion of s7 and s8 matches; the numbers in the s7–s8 solutions match the Finnish ones one for one (script count); model answers say the same physics; the intro matches.
