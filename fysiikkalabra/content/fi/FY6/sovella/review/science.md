VERDICT: FAIL
CONTENT-HASH: 5fb6f421aeb38b44

## Blocking
1. **fy6-s1 d, *Ryöminnän suuruus* (A: definition, magnitude).** The solution says "Se ei ole sama asia kuin varauksenkuljettajien **ryöminnän nopeus** johtimessa". The sentence before has just defined *ryöminnän nopeus* as a voltage change per minute, so one name now stands for two quantities. Use the task's term, *ajautumisnopeus*. "millimetrien luokkaa sekunnissa" is about ten times too large: 0,5 A in 0,5 mm² copper gives $v = I/(nAe) \approx 0{,}07\,\text{mm/s}$. Write "alle millimetri sekunnissa".
2. **fy6-s4 a–b, significant figures (A: rounding reason, rubric).** 300 V, 330 µF and 220 V each have three figures (P7: rated values' trailing zeros count). The reason "enintään kaksi tai kolme numeroa" is therefore wrong. The answers should be 14,9 J, 6,86 J and 46,2 %, not 15 J, 6,9 J and 46 %. Fix the rubric `units_precision` row (E ≈ 15 J) and b's "kaksi merkitsevää numeroa" too, or have the task state two-figure data.

## Polish
- fy6-s2 d *Hyväksytään myös*: "lamppujen jännitteen voi lisäksi laskea" is out of date. The task now asks for it.
- fy6-s3 b/c: the "yläraja" also leaves out gravity, which adds about 1 % (13,6 m/s).

## Checked
- My own script recomputed every number from the task data. All agree with answers.py and the solutions:
  - s1: fit −1,194 V/A, 4,598 V; largest residual 0,020 V; c) 0,50 A, 2,0 W, 13 %; d) ±0,08 Ω, 0,06 Ω, 0,005 V/min.
  - s2: 2,5 A; 16,7 + 8,3 + 5,0 = 30 W; c) 1,76 A, 10,6 V, 18,7 W, 2,5 W; d) 4,29 A, 8,6 V, 14,7 W.
  - s3: 1,8·10⁻⁷ N; mg/F 2,2 %; 0,1 of breakdown; 13,4 m/s; 14 %; 3,2·10⁻⁹ N (0,82 mg).
  - s4: 14,85 J, 6,86 J, 46,2 %, 26,4 A, 6,9 kW, 0,30 A.
- The Kaava steps start from the basic equations (loop rule, P = UI with U = RI, branch currents summed, W = ΔE_k) and are solved in symbols first.
- The models' conditions are stated, and the energy goes to the air's internal energy. Point charges hold: droplet radius about 46 µm ≪ 1 mm.
- Scope stays within FY6. Rubric points add up, each criterion asks only what its task asks, and other correct methods are accepted.
- Figures match the data and the circuits.
