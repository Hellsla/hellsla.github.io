VERDICT: PASS
CONTENT-HASH: e5734c9f1a8e175a

## Blocking

## Polish
- fy6-k1 b, Perustelu (open from round 1): it says only the battery's internal resistance and the wires limit the current, but the exam intro makes internal resistance negligible. Name the ammeter's own small resistance as well. Category 6; the right option is unaffected.

## Checked
- Full review, round 2. Hash e5734c9f1a8e175a at the start and the end.
- Round 1 polish on k7 a is fixed: the rubric detail now says $W \approx 10{,}2\,\text{kWh}$, which matches the solution and the answer check (10,24, 2 %).
- Round 1 polish on k7 d is fixed. Total dissipation is $EI_\text{k} \approx 330\,\text{kW}$, almost all in the 8 mΩ of the cells. A wrench and contacts of about 0,2 mΩ at 6 kA take about 8 kW. So "satoja kilowatteja, enimmäkseen kennojen sisäisessä resistanssissa" and "kilowatteja ... jakoavaimen ja liitosten pieneen resistanssiin" are both right, and the causal link holds.
- One script recomputed every number from the task data with my own formulas; all agree with answers.py and the solutions:
  - k1: e 2,5; f 0,40 Ω and 4,0 A; d 1/2 → 2/3 and 1/2 → 1/3; j 9,13 / 7,61 / 9,35 / 13,48 A. Each item has exactly one correct option.
  - k2: 17,99 Ω; 8,93 / 20,0 Ω; series point 188,6 mA and 2,61 V.
  - k3: 200 Ω and 13,6 mA; ΔI 0,84 mA; 40 / 80 %; 11,8–17,6 and 13,2–14,1 mA.
  - k4: 4,02·10⁴ m/s; 1,10·10¹⁹ 1/s; 0,207 kg per day; 1936 W, equal to N·½mv².
  - k5: 4,76 J; 255 s; 3,33 / 7,5 mA; 411 / 542 s.
  - k6: 2,24 mN; fitted slope 5,62·10⁻⁶ N·m², q 25,0 nC; 12 % (3 cm) and 5 % (4 cm) short of the model.
  - k7: 51,2 V and 10,24 kWh; 7,58 / 9,22 kWh, 1,64 kWh left; 97,7 A and 114 W (exact solution 100 A); 6400 A; 391 A, 610 W, 76 W (exact 467 A, 874 W).
- Causality is right: the grid spacing drops out (Fd = eU); constant-power discharge; charge redistribution on the conducting spheres; I²R losses against the system voltage.
- The figures match the tasks: k1 d topology, battery line, charging shapes, k3 LED polarity, k2 curve, k6 line.
- Scope stays within FY6: capacitor discharge only qualitative, no exponential law. practice.py check OK.
