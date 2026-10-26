VERDICT: PASS
CONTENT-HASH: 2bf5975e86980e7d

## Blocking

## Polish
- sim.js:110 (and the readout line below it) — the slider label reads "Lämpötila T = 20 °C = 293,15 K", so the symbol T stands for a Celsius value, while the lesson, the misconception list and exp-2 use θ for °C and T for kelvins — write "Lämpötila θ = 20 °C, T = 293,15 K".
- solutions.md:23 (L1-03 Järkevyys) — "paine jää hieman pienemmäksi": an adiabatic expansion from 1,00 l to 1,50 l gives about 244 kPa instead of 287 kPa, about 15 % lower — say "selvästi pienemmäksi" or give the order of magnitude.
- sim.js speed control — at "nopea" the wall flashes come twice as often in real time, which a student could read as a higher pressure. The Käyttöohje says the speed does not change p, so this is not blocking; one could also say it in the Nopeus label's tooltip.

## Checked
- I recomputed all 12 exercise answers in one script (Boyle, V/T, p/T with 273 and 273,15; ρgh; gauge pressure; a least-squares fit through the origin for L2-03 gives 2009 kPa·ml). They agree with answers.py and exercises.json within tolerance. The side claims also hold: 216 kPa when the gauge reading is used, about 7 kN on the freezer lid, about 40 min of air, 1,8 m³ with Z ≈ 1,1, a 24 % share and a 14 % shrink.
- Worked example: 1,036 l ≈ 1,0 l and +30 %. Misconception: 1,04 l and 3,5 %. Exit ticket: 160 kPa and a factor of 1,1. All are solved symbolically before substitution.
- inquiry.json: the review item is 30 N, and its three distractors match the errors they name. pred-1 gives 200 kPa and pV = 5,00 J. pred-2 gives 60,2 ml and V/T = 0,171 ml/K. In pred-3 each drop is checked. exp-2 gives γ = 1/293 ≈ 3,41·10⁻³ 1/K, against 1/273 = 3,66·10⁻³ for the distractor.
- Syringe table: pV = 5040, 5050, 5040, 5430, 5040, so the 30 ml row is +7,7 % and 168 kPa is expected there. Heating during compression is consistent with the data, because adiabatic compression from 40 ml to 30 ml would reach about 188 kPa. The distractor feedback "vuoto pienentäisi pV:tä" is correct.
- Error item: 252,5 ≈ 250 kPa and 40,4 kPa. Transfer: 1,07 l, with mistakes at 2,10 l and 0,00107. check-2: 120, 108 and 0,12.
- Experiments: exp-1 locks mode and Tc, varies Vml and measures p in Pa and pV in J (constant × 10⁻³ is correct). exp-2 locks mode, varies Tc, and gets T, Vgas and VperT from the adapter. Each setup isolates its varied parameter, and all the values the student needs are inside the slider ranges.
- sim.js: the three modes implement pV/T = const correctly, and the axis ranges cover their maxima. The hit rate ∝ √T/V times a flash size ∝ √T gives T/V, which matches the pressure. The speed control scales only the particle time step, and p, V, T and the table do not depend on it. The Laskennan selitys says the pressure comes from the formula, and pred-3 says the sim does not prove the law.
- Figures: in boyle-graphs every point lies on pV = 2000 kPa·ml in both panels, and the straight line reaches (0,12; 240). In absolute-zero the points span 253–373 K, the ratios agree to 0,1 % and the extension passes through the origin. micro-boyle shows a 2:1 gas height, 4 hits against 8, and velocity arrows of equal length. iso-processes is labelled a schematic, with longer arrows and a turned gauge.
- Scope: Boyle's law, the isobaric and isochoric laws in kelvins, absolute pressure against gauge pressure, and ρgh from the chapter Paine ja hydrostaattinen paine are all inside FY3's central contents. pV = nRT is not introduced.
- The unit identity 1 kPa·l = 1 J is correct. The 78 kPa cabin pressure is realistic.
