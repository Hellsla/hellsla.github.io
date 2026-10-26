VERDICT: PASS
CONTENT-HASH: d976b4674d500fd0

## Blocking

## Polish
- sim.js:941, 945 — the slider label and readout still write "Lämpötila T = 20 °C = 293,15 K", using T for the Celsius value while the lesson and exp-2 use θ for °C — write "θ = 20 °C, T = 293,15 K".
- inquiry.json, exp-2 question prompt — "Oppitunnilla fy3-8" names a lesson id to the student (owner's rule: name the chapter) — write "Lämpölaajenemisen luvussa"; the same ids appear in `contribution` and `prior` ("(fy3-3)", "(fy3-4)", "(fy3-8)").
- inquiry.json, pred-1/pred-2/pred-3 wrong-option feedback — "Kokeessa paine nousi…" calls simulation numbers experiment results, while the brief asks for "mallin arvot" — write "Mallin arvoissa…" as the correct options already do.
- inquiry.json, exp-2 correct-option feedback — γ = 1/T₀ holds for an ideal gas at constant pressure only; one clause would stop the student carrying 1/293 over to liquids.

## Checked
- One script recomputed all 12 exercise answers from the task data: answers.py and exercises.json agree (largest gap 1,0 %, L2-01; tolerance 2 %); L2-03 is the least-squares slope through the origin, 2,009 J, pV column 1980–2030 kPa·ml as stated.
- Formulas: Boyle, V/T and p/T with their conditions (closed amount, constant T, kelvins, absolute pressure); pV in J, 1 kPa·l = 1 J; all inside FY3 central contents (hydrostatic pressure in L3-01 from fy3-4).
- Worked example and every solution symbolic first; magnitudes right (cabin 78 kPa, 1,04 l and 3,5 %, 6,9 kN lid, 40 min SCBA, Z ≈ 1,1 at 300 bar, 216 kPa gauge-pressure trap).
- Figures: micro picture gas heights 220 : 110 px, hit marks 4 : 8; (V, p) points pV constant to 0,1 %, (1/V, p) points on one origin line; (T, V) figure to scale at 1,2 px/K, points 253–373 K on a line through 0 K.
- Inquiry numbers: pred-1 5,00 J; pred-2 60,2 ml, 0,171 ml/K; pred-3 200/100/50 kPa; γ = 0,171/50 = 3,41·10⁻³ = 1/293; ruisku pV 5040 vs 5430 (+7,7 %), 168 kPa; virhe 252/40,4 kPa; siirto 1,07 l, mistakes 2,10 and 0,00107, 71 %; check-2 120 kPa, mistakes 108 and 0,12; exit ticket 160 kPa, 308/280 = 1,1.
- Every correct option and every wrong option's feedback physics; leak vs heating reasoning in ruisku right.
- exp-1 locks mode and Tc, varies V 20–100 ml; `p` (Pa) and `constant` (J) match labels. exp-2 locks isobaric mode, varies Tc; `T`, `Vgas`, `VperT` from the adapter match labels.
- sim.js implements pV/T = const from 50 ml, 100 kPa, 293,15 K; ranges fit the axes (V ≤ 72,2 ml, p ≤ 144 kPa, 1/V ≤ 0,05); the calc note says the pressure comes from the formula, and pred-3 says the sim does not prove the law.
- Micro model: speed ∝ √T, hit rate per wall length ∝ √T/V, flash size ∝ speed, so rate × strength ∝ T/V.
- Hash d976b4674d500fd0 at start and end.
