VERDICT: PASS
CONTENT-HASH: 92395fcf3d320d88
SCOPE: delta figure-words-added,md-paragraphs,numbers,reflow,teacher-figure,typography from 095d05500287de55 base 5b3ca4f

## Blocking

## Polish
- solutions.md (fy2-2-L3-05), Formula: the fat's energy content per kilogram is written $H$, which is the course's symbol for a fuel's heating value, and the line speaks of "burnt fat". By the guardrail, food energy is the energy the body can use, and a heating value is the energy released in combustion. Consider "$E = m \cdot 37\,\text{MJ/kg}$ (energy content of fat)", or name the symbol as the energy content. The number is right. This is level C.
- solutions.md (fy2-2-L2-07), Formula: $E = k \cdot s$ drops the fitted intercept $8\,\text{kJ}$. The Principle and the Reasonableness lines say the line passes almost through the origin, so this is a fair simplification (C).

## Checked
- I ran the hash `--exercises --lang en` at the start and at the end, and both times it was 92395fcf3d320d88.
- I recomputed all 21 numeric answers: answers.py against exercises.json, all within tolerance. My own values: L3-02 $230\,000 : 72 = 3194$, so about 3200 houses. L2-07 least-squares slope 250.5 kJ/km with intercept 7.7 kJ, so $s = 1500 : 250.5 = 5.99\,\text{km}$. L3-05 $(11.45 - 10.35) \cdot 30 : 37 = 0.892\,\text{kg}$.
- L1-07 (nuts): the new start, $E/m = E_{100}/m_{100}$, is the right proportionality, and solving it gives the same formula, 1200 kJ.
- L2-05 (breakfast): the proportionality start and $E = s \cdot E_\text{km} \Rightarrow s = E : E_\text{km}$ are right. The answer of 7.3 km is unchanged.
- L3-05: the chain $30\,\Delta E = mH \Rightarrow m = 30\,\Delta E / H$ is solved symbolically before substitution.
- L3-02 and L3-04: only paragraph splits. The numbers and the CHP remark are unchanged and right.
- figures.json (teacher-approved): the English caption numbers check out. A 0.1 kg apple lifted 1 m takes about 1 J. A day's food is about 10 MJ. 50 L of petrol at 0.75 kg/L and 43 MJ/kg is 1.6 GJ. OL3 at 1.6 GW for 86 400 s is 138 TJ, about 140 TJ.
- No guardrail break (A or B) is introduced by the diff.
