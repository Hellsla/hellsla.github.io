VERDICT: PASS
CONTENT-HASH: c11560dc57c21b89

## Blocking

## Polish
- sim.js:110, 114 — the slider label and readout write "Lämpötila T = 20 °C = 293,15 K", using T for the Celsius value while the lesson and exp-2 use θ for °C and T for kelvins — write "θ = 20 °C, T = 293,15 K".
- content/FY3/fy3-9/inquiry.json, exp-2 question, correct option feedback — "kaasun γ ei ole vakio … riippuu lämpötilasta, josta lähdetään" is right, but it could add that γ = 1/T₀ holds for an ideal gas at constant pressure only, so the student does not carry 1/293 over to liquids.

## Checked
- One script recomputed all 12 exercise answers: answers.py and exercises.json agree with my values (largest relative gap 1,0 % for L2-01, tolerance 2 %); L2-03 is the least-squares slope through the origin, 2,009 J.
- Formulas: Boyle, V/T and p/T laws with their conditions (closed amount, T constant, kelvins, absolute pressure); pV unit J and 1 kPa·l = 1 J; all inside FY3 central contents.
- Worked example and every solution are symbolic first; magnitudes right (cabin 78 kPa, 1,04 l, 3,5 %, 7 kN lid, 40 min SCBA, Z ≈ 1,1 at 300 bar).
- Figures: fig 1 gas heights 220 : 110 px and hit marks 4 : 8; fig 2 pV constant to 0,1 % on all eight points and the (1/V, p) points on one origin line; fig 3 to scale, 1,2 px/K, points 253–373 K on a line through 0 K.
- Inquiry numbers: pred-1 5,00 J; pred-2 60,2 ml, 0,171 ml/K; pred-3 200/100/50 kPa; γ = 0,171/50 = 3,41·10⁻³ = 1/293; ruisku pV 5040 vs 5430 (+7,7 %), 168 kPa; virhe 252/40,4 kPa; siirto 1,07 l with mistakes 2,10 and 0,00107; check-2 120 kPa with mistakes 108 and 0,12; exit ticket 160 kPa and 1,1.
- Every correct option and each wrong option's feedback physics; leak vs heating reasoning in ruisku right.
- exp-1 locks mode and Tc (20 °C), varies V over 20–100 ml; `p` in Pa and `constant` in J match the labels. exp-2 locks isobaric mode, Tc −50…150 °C; `Vgas` (ml), `VperT` (ml/K) and `T` from the adapter match.
- sim.js implements pV/T = const from 50 ml, 100 kPa, 293,15 K; ranges fit the axes (p 50–250, 76–144 kPa; V 38–72 ml); dashed extension to the origin uses the correct curve end; the calc box says the pressure comes from the formula, not from hits.
- Micro picture: speed ∝ √T, 2D hit rate per wall length ∝ √T/V and flash size ∝ speed, so rate × strength ∝ T/V as claimed.
- Hash c11560dc57c21b89 at start and end.
