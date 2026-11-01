VERDICT: PASS
CONTENT-HASH: f66de27277e0e818

Science review of fy14-photoelectric, 2026-11-01. Every number was recomputed in Python with exact h, e and c. Photon energies (650, 530, 500, 450, 405, 400, 300 and 250 nm), thresholds (Na 525 nm and 5.71e14 Hz, Zn 288 nm and 10.4e14 Hz, Cs 5.17e14 Hz, K 541 nm), the slope 1.65 V per 4e14 Hz, the sim's model values (I = 6.0 and 18.0 nA, E_k,max = 0.74 eV, U_s = 0.40 and 1.78 V on the 0.02 V grid), the worked example, the h task (6.597e-34, mistakes 4.12 and 2.91, 0.4 %, 0.9 %) and all checks agree. Every choice task has exactly one correct option, and its distractor feedback is right.

History was checked by WebFetch on 2026-11-01:
- Hertz 1887 and Lenard 1902 (Wikipedia, *Photoelectric effect*).
- Planck: 14 Dec 1900 to the DPG, at first rejected light quanta, Nobel Prize for 1918 (Wikipedia).
- Einstein: the motivation quoted exactly, the prize presented in 1922 (nobelprize.org).
- Millikan: a decade-long programme, a sceptic still in 1916, results 1914, the 1916 h paper, Nobel Prize 1923 (Wikipedia).

The sim (sim.js) implements the stated model. The retarding polarity is correct (cathode +, collector −). Kinetic energies are uniform in [0, E_k,max], so I = I₀(1 − eU/E_k,max). The model box states its limits.

## Blocking
None.

## Polish
1. unit.md, Common misconception, "which only the electrons nearest the surface reach": E_k,max is reached by the least tightly bound electrons that lose no energy on the way out. Being near the surface is not enough by itself. Write "which only the most loosely bound electrons at the surface reach" (B, small).
2. unit.md, Worked example, Substitution: the step shows $4.905 \cdot 10^{-19}$ J, but the Result gives 4.90 (the unrounded value is 4.9049). Show $4.9049 \cdot 10^{-19}\ \text{J}$, or explain the rounding.
3. unit.md, Worked example: the stage labels are "Given and find.", "Rearranged formula." and "Result.". The guide §3 asks for **Given:**, **Formula:** and **Answer:**. In the planck-data solution, rename "**Conversions:**" to "**Unit conversions:**". The content of all seven stages is complete.
4. inquiry.json, planck-data: the guardrails say to read a slope from a fitted line. Add one sentence to the Reasonableness step: "With all five rows, a fitted line gives $h \approx 6.60 \cdot 10^{-34}\ \text{J} \cdot \text{s}$ and $W \approx 1.89\ \text{eV}$; at Fotoni you fit a line." The teacher extension already does this.
5. strings.json, `lukemat_ei`: "$E_{k,max}$ does not exist" is odd physics wording, and it also appears when $hf = W$. Write "$hf \le W$: no electrons leave".
6. inquiry.json, exp-stop/exp-intensity `measure` labels "U" and "I (nA)", and planck-data `unit` "· 10⁻³⁴ J·s": these are not in LaTeX (guide §3). Use `$U\;(\text{V})$` and `$I\;(\text{nA})$`.
7. teacher.md, Organisation: the electroscope demonstration needs a **negatively** charged zinc plate, freshly cleaned. A positively charged plate does not discharge. Add "and protect skin and eyes from the UV-C lamp".
8. unit.md: since 2019, h is exact in the text as $6.626 \cdot 10^{-34}$ and in the sim as 6.62607015e-34. This is consistent to three significant figures and needs no change, but the sim's `calc` box could say "the text rounds to 6.626".

## Checked
Physics, maths, LaTeX (\cdot, decimal point, units), the 7-step solutions, the sim model and readouts, the figures' numbers, history and dates, sources with dates, misconceptions.
