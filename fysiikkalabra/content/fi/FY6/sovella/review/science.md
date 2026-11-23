VERDICT: PASS
CONTENT-HASH: 37ff55bd05bc7116

## Blocking
None.

## Polish
- s2 d: 4,3 A is only 1,36 times the 3,15 A rating, and many miniature fuses carry that for minutes or longer. "Pieni ylivirta voi kestää hetken" understates this, but the hedging ("todennäköisesti", "yksinkertaistus") avoids a wrong picture. "Voi kestää pitkäänkin" would be more accurate.
- s1 d: "Lähdejännitteeseen vaikutus on pieni" is right: the intercept shifts by only about +0,006 V. The reason given is incomplete.

## Checked
- Round-1 fixes:
  - s1 d now separates ryömintä (drift, 0,03 V over 6 min) from drift velocity; 0,07 mm/s is correct (recomputed 0,074).
  - s4 a gives 14,9 J to three significant figures, with the reason stated.
  - s4 b gives 6,86 J and 46,2 %.
  - The mass in s4 a (1,0 kg raised 1,5 m) is correct.
- One script recomputed every number with my own formulas, and all agree:
  - s1: fit −1,194 V/A and 4,598 V, residuals at most 0,02 V, ±0,08 Ω, drift bias 0,06 Ω, 0,50 A, 2,0 W, 0,30 W, 13 %, 3,8 A.
  - s2: 2,5 A, 10,0 V, 16,7 + 8,3 + 5,0 = 30 W; then 1,76 A, 10,6 V, 18,7 W, 2,5 W; then 2,0 Ω, 4,3 A, 8,6 V, 14,7 W.
  - s3: 3,0·10⁵ V/m, 1,8·10⁻⁷ N, weight 2,2 %, field 0,1 of breakdown, 13,4 m/s, 5,0·10⁻⁹ J, 14 %, 3,1·10⁻⁸ J, 3,2·10⁻⁹ N (0,82 mg).
  - s4: 14,85, 7,99 and 6,86 J; 27 % voltage drop; 26,4 A; 6,9 kW; 0,30 A.
- The 5,0 m/s in s3 c is plausible: for a droplet of radius 46 µm the Stokes terminal speed is about 12 m/s with τ ≈ 0,026 s. source_note says the values are illustrative.
- Models and their conditions are stated, the scope is FY6 and charging stays qualitative.
- Guardrails: no "lämmöksi". s3 c sends the energy to the air's internal energy, then out as heat.
- s4 d safety reasoning is sound (300 V and 15 J remain, RC ≈ 0,33 s).
- Rubric points add up (15/15/16/14). Each criterion matches its task and solution. The accepted ranges lie within the tolerances.
- Figures agree with the data:
  - s1: circuit, graph line, intercept 4,60 V and slope triangle.
  - s2: fuse and R_k in series with the lamps.
  - s3: field from +60 kV to ground.
- Hash unchanged at start and end.
