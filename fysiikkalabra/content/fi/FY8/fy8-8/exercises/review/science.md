VERDICT: PASS
CONTENT-HASH: 007cd121579068a3
Round: 1

## Blocking

## Polish
- content/fi/FY8/fy8-8/exercises/solutions.md:348 — fy8-8-L3-06: the reason "kolme merkitsevää numeroa kuten annetuissa aallonpituuden vakioissa" is wrong. h, c and 1 eV are all given to four figures (6,626, 2,998, 1,602) and the energies to four or five. Three figures is the house default, and 0,495 is inside the tolerance, but the reason given is false. Fix: give $0{,}4949\,\text{pm}$ (four figures, as in the constants), or keep 0,495 and give the house default as the reason.
- content/fi/FY8/fy8-8/exercises/solutions.md:302 — fy8-8-L2-09: "$2159\,\text{keV}$, neljä merkitsevää numeroa kuten annetuissa energioissa". 1332,5 has five figures, and in a sum the decimal places decide, so 2158,6 keV is the natural answer. Either answer is inside the tolerance. Optional: give 2158,6 keV, or say the answer is rounded to the 826,1 keV datum.
- fy8-8-L3-06 b) is conditional ("lähettäisi"), which is right: the direct C → ground transition (4⁺ → 0⁺) is practically not seen. The solution could say in one clause why no such peak appears in the spectrum. This is optional and would be a C-level addition.

## Checked
- Recomputed everything in one script with my own formulas. L2-09: E_X = 1332,5 + 826,1 = 2158,6 keV, the same as answers.py. L3-06: E_C = 2505,7 keV, E_C = 4,0141·10⁻¹³ J, hc = 1,9865·10⁻²⁵ J m, λ = 0,49487 pm, the same as answers.py (0.49487). The tolerances (0,02 → ±43 keV and ±0,0099 pm) fit.
- The level scheme matches NNDC for Ni-60: 1332,5, 2158,6 and 2505,7 keV. The weak lines 826,1 (2158,6 → 1332,5) and 347,1 keV (2505,7 → 2158,6) are real. The label "esimerkkiaineisto" invents no data, and "pitkässä mittauksessa" suits their low intensity.
- In L2-09 the cascade order (1173,2 first, then 1332,5 to ground) is given in the task, so E_1 follows from the given facts.
- In L3-06 a) the elimination argument is right: with A = 1173,2 keV, C → A would be 1173,2 keV again and 1332,5 keV would go unexplained. The check 347,1 + 826,1 = 1173,2 is exact.
- The reasonableness checks are real checks. Their wavelengths are right: 0,93 pm for 1332,5 keV, 1,06 pm for 1173,2 keV, and X below 2505,7 keV.
- Both solutions solve symbolically before they substitute. The keV → J conversion is shown by substitution as the brief's Kaava does, and 1 m = 10¹² pm is stated.
- The notation (E_γ = E_y − E_a, λ = hc/E) and the constants are the same as in the brief. The topic is inside the FY8 central content "atomiytimen rakenne ja muutokset" and the slot's täsmennys (nuclear levels from the gamma spectrum).
- The figure fy8-8/spectrum labels both peak energies, and its description gives the same values. It shows no level diagram, so it does not give the answer away.
- The answers.py lines compute from the task data and the file runs.
- The hash was the same at the start and at the end.
