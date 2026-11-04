VERDICT: FAIL
CONTENT-HASH: c53dc15ad7e8996c

## Blocking
- exercises.json:363 (L3-05 a) and solutions.md:186, :191 — **A, definition.** The task defines kynnysjännite as "jännite, jolla virta ylittää 1 mA" and gets 1,85 V. The course glossary defines it by extending the straight, steep part of the curve to the voltage axis. With this table that gives 2,05 V − 20 mA : (420 mA/V) ≈ 2,0 V. The Järkevyys then compares 2,02 V with "kynnysjännite 1,85 V". So the set teaches a second, conflicting definition, and the comparison turns on it. Fix: ask a) as in the glossary ("jatka ominaiskäyrän jyrkkää suoraa osaa (2,05–2,10 V) jänniteakselille") and change the solution to ≈ 2,0 V and the Järkevyys to "työpisteen jännite on hieman kynnysjännitettä suurempi". Or keep the 1 mA criterion but do not call it kynnysjännite ("jännite, jolla virta alkaa selvästi kulkea").

## Polish
- L1-06: "diodin yli on vain pieni osa pariston jännitteestä" holds only when the battery voltage is well above the diode's ~0,7 V (**B**). Fix: give the battery voltage in the text, for example 9,0 V.
- L1-08: the Vastaus 17 % lies 1,99 % from 16,67, at the very edge of the 2 % tolerance. Safe as it is, but `tolerance` 0.03 would remove the risk.
- L2-07 repeats the lesson's first misconception, and its calculation is the same as L1-02 and the Esimerkki. The plan asked for an error analysis of a LED burning out without a resistor (explained with the characteristic curve). Physics fine. The planning side should decide.

## Checked
- One script recomputed every new answer: L1-08 16,7 %; L2-05 red (lowest U_D) 207 Ω; L2-06 powers 98/146/178/181/165/145/109/54 mW, maximum 181 mW at 22 Ω; L2-07 387 Ω (600 Ω → 9,7 mA); L3-04 ΣH = 1027 kWh/m², E = 4683 kWh, Σ consumption 5340 kWh → 87,7 %, deficit months Jan–Mar and Oct–Dec, 853 vs 3370 kWh, deficit 2517 kWh; L3-05 operating point 2,02 V, 13,78 mA (an exponential interpolation gives 13,77). All match answers.py.
- L2-06 data are self-consistent: U : I ≈ R in every row, I_sc ≈ 100 mA, U_oc ≈ 2,4 V, fill factor ≈ 0,75 (realistic).
- L3-04 yield ≈ 975 kWh/kWp is realistic for Finland. "Verkosta ostetaan vähintään" the deficit is right as a lower bound when nothing is stored from season to season.
- L1-06 and L1-07: exactly one correct option, and the feedback is right. Forward bias and conventional current direction are as the lesson says.
- Levels 8/7/5. Units, tolerances, symbols and scope are correct. L3-04 and L3-05 render at 1280 px without overflow.
- Hash identical at start and end.
