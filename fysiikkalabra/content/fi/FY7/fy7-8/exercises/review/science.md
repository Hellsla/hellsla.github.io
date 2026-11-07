VERDICT: PASS
CONTENT-HASH: fb4a6839555b1dd9
Mode: light (teacher 2026-11-07, "kevyt katselmointi": the FY7 editorial-correction diff since origin/main only)

## Blocking
- none

## Polish
- none

## Checked
- L1-05 recomputed: $\sqrt3\cdot400\,\text{kV}\cdot800\,\text{A} = 554{,}26\,\text{MW}$ = answers.py (3**0.5*400e3*800/1e6) = exercises.json 554.2563 in fi/en/fi-easy; task states three-phase, line voltage, $\cos\varphi = 1$, so the data suffice; two-wire comparison 320 MW and the √3 factor right. L2-01 826,4 kW, L2-03 0,9917 %, L2-08 $I=150\,\text{A}$, $P_\text{h}=11\,\text{kW}$ ~10 kW, L3-01 0,75 %, L3-02 4,0 Ω, L3-03 3,306, L3-04 (R = 6,0 Ω; 909 A / 500 A; 4,96 / 1,50 MW; ≈1,52 M€) recomputed; all now state the two-wire model, answers unchanged. L1-03 note: in a three-phase transformer $\sqrt3 U_1 I_1 = \sqrt3 U_2 I_2$, so the current ratio is still the inverse line-voltage ratio — correct. L3-03 note: three-phase loss share $= R_\text{ph}P/(U^2\cos^2\varphi)$, so the $(400:220)^2$ ratio holds at the same power factor — correct. Consistent with the lesson's "ellei tehtävässä toisin mainita". Hash identical at start and end.
- Round 2: L1-05 Sijoitus now $\approx 554\,260\,000\,\text{W} = 554{,}26\,\text{MW}$ (exact 554 256 258 W → 554,26 MW; Minor resolved). New Periaate: each of three phase conductors carries power at the phase voltage $U:\sqrt3$, total $3\cdot(U:\sqrt3)\cdot I = \sqrt3\,UI$ — correct for a balanced load at $\cos\varphi = 1$; the stated reason (phase voltages are out of phase, so the line voltage is $\sqrt3$ times the phase voltage) is a fair simplification. Answer 554 MW = answers.py; fi, en, fi-easy agree.
