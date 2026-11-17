VERDICT: PASS
CONTENT-HASH: 745807716c462177
Mode: delta (fi-easy version of the reviewed Finnish fy8-8-L2-09 and fy8-8-L3-06)
Round 1

## Blocking

## Polish
- content/fi-easy/FY8/fy8-8/exercises/solutions.md:350 — fy8-8-L3-06: the reason "kolme merkitsevää numeroa kuten annetuissa aallonpituuden vakioissa" is wrong, because h, c and 1 eV are given to four figures. 0,495 is inside the tolerance. Fix: give 0,4949 pm, or keep 0,495 and give a correct reason. This follows the same Polish item on fi.
- content/fi-easy/FY8/fy8-8/exercises/solutions.md:304 — fy8-8-L2-09: in a sum the decimal places set the precision, so 2158,6 keV (the answer field) is the natural answer. 2159 keV "neljä merkitsevää numeroa" is acceptable but loose. This is optional.

## Checked
- Recomputed both answers in one script with my own formulas. L2-09: E_X = 1332,5 + 826,1 = 2158,6 keV. L3-06: E_C = 2505,7 keV = 4,0141·10⁻¹³ J, λ = 0,49487 pm. These agree with answers.py and with the JSON (2158,6 keV and 0,495 pm, tolerance 0,02).
- The physics matches NNDC Ni-60: the levels are 1332,5, 2158,6 and 2505,7 keV, and the weak lines 826,1 keV and 347,1 keV are real. The data are labelled esimerkkiaineisto. The direct C → perustila transition is stated conditionally ("lähettäisi").
- L3-06 a): the elimination argument is valid. With A = 1173,2 keV, the transition C → A would be 1173,2 keV, so 1332,5 keV would go unexplained.
- In L2-09 the cascade order is given in the task, so E_1 = 1332,5 keV follows from it.
- Reasonableness checks: 0,93 pm and 1,06 pm are right, and X lies below 2505,7 keV.
- Compared with content/fi: the id, level, kind, figure, answer, unit, tolerance, data rows and every number in the texts and solutions are identical. The plainer, shorter sentences change no physics.
- The notation (E_γ = E_y − E_a, λ = hc/E) and the constants match the brief's Kaava. The tasks are inside the FY8 scope and the slot's täsmennys.
- Figure fy8-8/spectrum labels both peaks and shows no level diagram, so it does not give the answer away.
- The hash was the same at the start and at the end.
