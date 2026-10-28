VERDICT: PASS
CONTENT-HASH: c56ea1f6766e2d73

## Blocking

## Polish
- solutions.md:59 L2-02 — "Lapsi, liukumäki ja vesi muodostavat eristetyn systeemin": the air also warms, so "ja ympäristö" is safer, as L1-05 has it.
- solutions.md:109 L3-03 b — "koska turbiinista tuleva höyry on vielä lämmintä" is fair at FY2. It could be read as a loss that better engineering removes; one clause saying that some of the heat must always be given off to the cooling water keeps it consistent with the efficiency guardrail without bringing in the Carnot limit.
- solutions.md L1-03 — "kolme merkitsevää numeroa kuten 800 J": 800 J is ambiguous in significant figures. "joulen tarkkuudella", as in L1-02, avoids the issue.

## Checked
- One-script recomputation from the task texts: 50 / 239 / 640 / 510 J; 850 J, 3,0 kJ, 360 J, 29 000 J; 130 J and 0,20 J. These agree with answers.py and exercises.json; units and tolerances fit.
- Every energy balance names all forms and the system (E_alussa = E_lopussa). Unknowns are solved symbolically before substitution, and the kJ ↔ J conversions are right.
- Magnitudes are realistic: leaf about 2 % chemical, panel 20 %, e-scooter about 72 %, kettle about 92 % to the water, nuclear plant about one third electric.
- L3-01: thermal energy increases monotonically (0, 20, 150 J), and the mechanical-energy cross-check gives 880 − 750 = 130 J. L3-02: one fifth lost per bounce.
- Word answers L1-04 and L3-03: the energy chains are correct (chemical → thermal; radiant → electrical; potential → kinetic → electrical; nuclear → thermal → kinetic → electrical), with the thermal share named.
- Scope: no E_k, E_p, Q = cmΔT or chain-efficiency products. Symbols are the same as in the brief's lesson.
- Hash identical at start and end.
