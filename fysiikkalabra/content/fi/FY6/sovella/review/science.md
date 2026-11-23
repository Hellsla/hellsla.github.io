VERDICT: PASS
CONTENT-HASH: 37ff55bd05bc7116

## Blocking
None.

## Polish
- s2 d (fuse): 4,3 A is only about 1,36 times the 3,15 A rating. Many miniature fuses can carry that current for minutes or longer, so "pieni ylivirta voi kestää hetken" (a small overcurrent can last a moment) understates the time. The claim is hedged ("todennäköisesti", "yksinkertaistus") and leaves no wrong picture, so this is not an error. "Voi kestää pitkäänkin" would be more accurate.
- s1 d: "Lähdejännitteeseen vaikutus on pieni" is right: the drift tilts the fitted line, which shifts the intercept by only about +0,006 V. The reason is that the drift lowers the high-current points, not mainly that the first point was measured on the fresh battery. Optional.

## Checked
- Round-1 fixes. s1 d now separates drift (ryömintä, 0,03 V over about 6 min, ≈ 0,005 V/min) from drift velocity. The drift velocity of 0,07 mm/s at 0,5 A in 0,5 mm² copper is correct (recomputed 0,074 mm/s). s4 a gives 14,9 J to three significant figures, justified by 300 V and 330 µF. s4 b gives 6,86 J and 46,2 %. The mass wording in the s4 a reasonableness check (1,0 kg raised 1,5 m) is correct.
- I recomputed every number in one script with my own formulas, and all agree:
  - s1: least-squares fit −1,194 V/A and 4,598 V. Residuals from U = 4,60 − 1,2 I are at most 0,02 V. Extreme-line spread 0,08 Ω, drift bias 0,06 Ω, I = 0,50 A, P = 2,0 W, P_s = 0,30 W, share 13 %, I_k = 3,8 A.
  - s2: 2,5 A; 10,0 V; 16,7, 8,3 and 5,0 W summing to 30 W. With lamp B gone: 1,76 A, 10,6 V, 18,7 W, cable 2,5 W. With lamp C added: R_r = 2,0 Ω, 4,3 A, 8,6 V, 14,7 W ("melkein kolminkertainen").
  - s3: 3,0·10⁵ V/m, 1,8·10⁻⁷ N, mg 2,2 % of the electric force, field 0,1 of the breakdown strength, 13,4 m/s, a = 450 m/s². With 5,0 m/s: 5,0·10⁻⁹ J, 14 %, 3,1·10⁻⁸ J. Coulomb force 3,2·10⁻⁹ N, 1,8 % of qE and 0,82 mg.
  - s4: 14,85, 7,99 and 6,86 J; 46,2 % against a 27 % voltage drop; 0,0264 C; 26 A; 6,9 kW; 0,30 A.
- Plausibility of the s3 c "measured" 5,0 m/s: the droplet radius is about 46 µm, the Stokes terminal speed about 12 m/s, and the time constant 0,026 s over a 0,2 m gap. A few m/s is realistic, and source_note says the values are prepared for the task.
- Models and conditions are stated: an ideal source with series R_s (constant E and R_s), constant lamp resistances, a uniform field, weight and air drag left out (b), point charges (d). Charging and discharging stay qualitative. Everything is within FY6 scope.
- Guardrails: no "lämmöksi". s3 c says air's internal energy grows and the energy is transferred as heat. The safety reasoning in s4 d is sound (the capacitor keeps 300 V and 15 J, RC ≈ 0,33 s).
- Rubrics: the points add up (15/15/16/14). Every criterion asks only what its part asks, and the solutions show it. The "Hyväksytään myös" ranges (R_s 1,1…1,3 Ω, E 4,5…4,7 V) fall inside the tolerances, and other methods (taking b from a = F/m, Q = CU) are accepted.
- Figures:
  - s1 circuit: the voltmeter is across the terminals and the ammeter in series.
  - s1 graph: points, line, intercept at 4,60 V and the slope triangle −0,60 V / 0,50 A agree with the data.
  - s2: the fuse and R_k are in series with the parallel lamps.
  - s3: the field runs from +60 kV to the grounded workpiece.
- Hash 37ff55bd05bc7116 at both start and end.
