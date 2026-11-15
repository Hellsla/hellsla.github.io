VERDICT: PASS
CONTENT-HASH: 8c105b85746eef7d
Mode: full (round 1)

## Blocking
- none

## Polish
- exercises.json fy8-6-L1-06 (feedback of the "kuori absorboi" distractor and of the correct option) — "fotoneja ei synny lainkaan" / "fotonia ei synny" is stricter than the lesson, which says the LED "ei juuri" radiate and that the measured U_k is about 0,1 V below hf/e (thermal energy) — write "ei juuri synny".
- solutions.md fy8-6-L2-06 Vastaus — the deviation 3,65 % is a difference (6,868 − 6,626 = 0,242), so its third figure is not carried by the voltages' three figures; "noin 3,6–3,7 %" would be the honest precision. The answer and tolerance (3 %) accept either.
- solutions.md fy8-6-L2-04 Järkevyys — "kuten fluoresenssissa aina": add "yleensä" (fair at this level, C).
- solutions.md fy8-6-L1-07 Periaate — says "likimain" where the task assumes "täsmälleen"; one word.

## Checked
- All 19 numeric answers recomputed from the task texts with own formulas in one script: agree with answers.py and exercises.json (largest relative difference 0,14 %, all inside tolerance; a student rounding to the data's figures stays inside).
- Fits redone by least squares: L2-05 slope 61,5 mA/V, U_k = 1,857 V (four- or five-point fit agree); L3-01 k = 4,212·10^-15 V s, b = −0,164 V; L3-04 k = 4,208·10^-15 V s, b = −0,062 V → −0,112 V after the zero correction, slope unchanged.
- L2-08: the table's own fit gives k = 3,976·10^-15 V s, b = −0,074 V, standard error 0,21·10^-15 V s, as stated; h = 6,376·10^-34, Δh = 0,336·10^-34 J s; exactly one option is correct, every distractor is wrong and its feedback gives the right reason ("sopusoinnussa", not "equal").
- L1-06: one correct option; distractors (thermal glow, colour shifting with voltage, absorbing casing) really wrong.
- L2-06: h values −11,6 %, −4,5 %, +3,65 %; explanation of the reading methods (current-dependent readings vs the extrapolated line) is right, and "close to the table value does not prove the method" is correct.
- L2-07: half-maximum points 620 and 640 nm read from the table, ΔE = 0,0625 eV, realistic (≈ 2 kT); thermal-spread reason correct.
- L3-05: f = 6,169·10^14 Hz, λ = 486,0 nm, direct formula 504,1 nm, Δλ = 9,5 nm; interval 476–496 nm.
- Models and assumptions stated in the tasks (eU_k = hc/λ "oletetaan", one photon per electron in L2-03, example data marked); internal energy wording follows the guardrails.
- Scope: photon energy, threshold voltage, Planck's constant from a fit, LED and laser-diode spectra, fluorescence; nothing beyond FY8. Notation as in the brief.
- Solutions: symbolic form before substitution, conversions, rounding reasons and real reasonableness checks present for all 21 tasks. Hash identical at start and end.
