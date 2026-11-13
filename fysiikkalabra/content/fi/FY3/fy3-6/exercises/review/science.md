VERDICT: PASS
CONTENT-HASH: b1d7dd63f21652d2
SCOPE: delta added-exercise from 3dd71e954a48a7f8 base 89bcb63b7431

## Blocking

## Polish
- exercises/solutions.md (fy3-6-L2-09, Kuvaajan lukeminen) — "kupari lämpenee ja jäähtyy helposti" and "kuparista irtoaa kilogrammaa kohti vähän lämpöä": both mean per kilogram and per kelvin; adding "kelviniä kohti" keeps the C-level simplification exact. The doubled "Kuvaajan lukeminen kuvasta" lead-in is wording only.

## Checked
- MAFY value verified on mafytaulukot.fi (*Ominaislämpökapasiteetteja*, 20 °C): alumiini $0{,}896\,\text{kJ/(kg·K)}$, as the solution uses.
- L1-09 recomputed: $Q = cm\Delta T = 0{,}896 \cdot 0{,}80 \cdot 80 = 57{,}3\,\text{kJ}$; with the lesson's 900 J/(kg·K) 57,6 kJ, inside tolerance 0,04; answers.py agrees.
- L1-09 condition stated (aluminium stays solid, so $Q = cm\Delta T$ applies); $\Delta T$ in K = °C difference; kJ unit carried through; two figures justified (0,80 kg, 80 K); check (0,72 kJ/K · 80 K) real.
- L2-09 recomputed: $c_\text{Cu} = 385\,\text{J/(kg·K)}$ from the bar label (figure code prints it beside the bar), $Q_\text{luov} = 385 \cdot 3{,}0 \cdot 60 = 69{,}3\,\text{kJ}$; answers.py agrees; 69 kJ inside tolerance 0,03.
- L2-09 sign: the task asks for the released heat as a positive number and the solution uses $|\Delta T|$, consistent with the brief's convention ($Q < 0$ on cooling).
- L2-09 check (same heat cools 3,0 kg water by ≈ 5,5 K) real and right.
- Figure description lists all six values, the same as the lesson's table; the task needs only reading, so nothing is given away beyond the datum.
- Both in FY3 scope; solutions symbolic before substitution.
- Rest of the set unchanged since PASS; hash same at start and end.
