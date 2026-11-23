VERDICT: PASS
CONTENT-HASH: 754be9e49009ab18
SCOPE: delta numbers from 47c6ed01597a514a base 3076572c597d

## Blocking
- none

## Polish
- none

## Checked
- The loop tasks now open with $\sum \Delta V = 0$, followed by the signed row $U_\text{lat} - RI - R_\text{s}I - E = 0$. This is the voltage law as the course writes it. It was $\Sigma U = 0$ until an edit made during this review, and I checked the edit.
- I recomputed all 19 changed solutions in one script from the task data: 16 h, 4,0 Ah, 5,0 A, 0,20 Ω, 97,5 min, 84 %, 1,28, 33,3 %, 3,24 kJ, 5,2 h, 9,32 Wh, 1,5 Wh, 0,40 Ω, 61,05 Wh, 1,8 MJ / 4,2 h, 77,45 % / 0,10 Ω, 7,125 h / 6,0 h. All agree, and no Sijoitus number changed.
- The charging loop has the right signs, with the drop $E$ because the current passes through the battery from + to −. This is as in the lesson.
- The $R_\text{kok}$ task's row $I = U_\text{lat} : R_\text{kok} - E : R_\text{kok}$ correctly gives the slope $1 : R_\text{kok}$.
- In the charge–discharge task, $E = U_\text{ka} + R_\text{s}I$ is the discharging terminal voltage. Equating it for both currents gives $R_\text{s} = (U_{1,\text{ka}} - U_{2,\text{ka}}) : (I_2 - I_1)$.
- The internal-energy task goes $P = UI$, $U = R_\text{s}I$, $P = R_\text{s}I^2$. The energy goes to internal energy and then leaves as heat, as the guardrail requires.
- The loss task: $W_\text{häviö} = W_\text{lat} - W_\text{akku} = (U_\text{lat} - E)It$, as in the lesson.
- Content hash checked at start and end.
