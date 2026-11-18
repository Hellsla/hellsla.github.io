VERDICT: PASS
CONTENT-HASH: 3b9eee5b55139e4f
SCOPE: delta: fi-easy diff since 49ba8f9 (new tasks fy9-tasavirta-s7 lamp characteristic with a series resistor and s8 mixed circuit in sovella/tasks.json and solutions.md, intro "kahdeksan"); fidelity of s7/s8 to fi; s1-s6 not re-judged.

## Blocking
(none)

## Polish
(none)

## Checked
- Recomputed in one script. The lamp curve comes from the figure model (lessons/FY6/fy6-3 lamp_I, RK 1, RN 12, UN 3): I(2,0 V) = 0,208 A, I(3,0 V) = 0,25 A.
  - s7: a R = 9,6 Ω from the exact curve; the key 9,5 Ω with 6 % tolerance admits readings of 0,20 to 0,22 A (10 and 9,1 Ω). b R = 12 Ω. c series R = (4,0 - 3,0)/0,25 = 4,0 Ω (check 16 - 12). d 0,75 W, 0,25 W and 1,0 W, which gives 75 %.
  - s8: a Rp = 20 Ω, R = 40 Ω, I = 0,30 A (bounds 0,60 A and 0,11 A). b Up = 6,0 V, so 0,10 A and 0,20 A. c 1,8 W and 3,6 W, which equal 1,8 + 0,60 + 1,2 W. d 80 Ω, 0,15 A and 9,0 V give 1,35 W (2,25 times 0,60 W).
  - All keys are within tolerance.
- Figure fy6-4 siirto-mixed: 20 Ω in series with 60 Ω || 30 Ω on 12 V, as the solution reads it.
- Physics: R = U/I at a point, and not the slope. The lamp's resistance grows as the filament heats, so it does not follow Ohm's law. The series connection is justified and a parallel one rejected. Kirchhoff's voltage law is used, and P = UI = RI² = U²/R. The internal resistance and wire resistance are stated as neglected. s8 d keeps two things apart: the battery current falls, yet the 60 Ω power rises. All of this is in FY6 scope.
- Significant figures follow the readings and data.
- Rubrics: s7 4+3+5+4 and s8 5+5+4+4. The criteria match the parts and solutions. "Hyväksytään myös" covers the total-resistance route, 1/Rp, RI² and UI.
- Fidelity to fi: ids, figures, points, criteria, answers, tolerances and every number in tasks and solutions are identical (compared with a script).
- Intro: eight tasks, matching the set.
- The hash was the same at start and end.
