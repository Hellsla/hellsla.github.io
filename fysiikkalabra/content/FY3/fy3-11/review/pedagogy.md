VERDICT: PASS
CONTENT-HASH: d1ddfcf862eff861
## Blocking

## Polish
- inquiry.json:124,223,392 (also 7, 66, 79 and lesson.md "Tarvitset") — teacher's rule "symbols in prose as maths": bare "(V, p)-kuvaaja" and "(s, F)-kuvaaja" stay plain text, while Ydinajatus writes "($V$, $p$)-kuvajassa" — write "($V$, $p$)-kuvaaja" everywhere. Same for the generated "Alkutila: lämpö Q = 500 J, paine p₂ = 100 kPa" line and table headers ("ΔV (l)", "Q₁ (J)"), and "10¹² J" in exercises.json:48.
- inquiry.json pred-1 — the prediction needs W = pΔV, which the student meets only in Teoriatiivistelmä; the sim computes ΔV = 2Q/(5p), so exp-1 mostly confirms the arithmetic. Fine as a first-contact derivation (F = pA, s), but add a one-line cue in the prompt ("kaasu painaa mäntää voimalla pA") so a student can actually argue the options.
- inquiry.json pred-2/exp-2 — two return methods refute Aino's specific mechanism, not the general claim; lesson.md "Kokemus osoittaa" carries the second law. Say once in the exp-2 question feedback that this is an experience-based law, not something two runs prove.
- inquiry.json "suunnittele" (hints, line 532-534) — a two-equation system with an unknown pump power is the heaviest step of the lesson; with three experiments, heat pump and cogeneration the workload is at the upper limit of one lesson. Keep, but consider dropping option 3 to the exercises.
- Sim canvas labels ("p (kPa)", "ΔU + W_k", "Q") at 390 px are small and not LaTeX; the cylinder and particles are tiny. Legible, but the weakest part of the print-quality rule.

## Checked
- Figures 1-4 (piston-work, heat-engine, heat-pump, pv-work): all labels LaTeX, large, uncluttered; arrow widths in scale (60/24/36, 20/40/60); colour backed by labels and hatching; legible at 390 px.
- Opening question answered in Ydinajatus and reflect; goals of the slot met without computing cycles.
- Chapter names used ("luku *…*"), no lesson ids in learner text.
- Worked example: five stages, one step each, LaTeX aligned; sensible check; does not repeat the exercises.
- Experiments: parameters locked and varied correctly, min 2, exp-2 compares A and B; speakers: only Bea right.
- Exercises: three levels, answers verified (12 kJ, 172 J, 500 J, 120 MW, 9,6 MWh, 12 kW); solutions in LaTeX; exit ticket tests the core idea.
- Layout: 1280 px two-column Tutki and Pohdinta read well; 390 px nothing clipped.
- Finnish: no errors found.
