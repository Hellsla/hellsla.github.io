VERDICT: PASS
CONTENT-HASH: b00b18d0b241bb39
SCOPE: delta added-exercise from 593f504a543bc1e6 base 8f23aa7ae3bd

## Blocking

## Polish
- content/fi/FY6/fy6-3/exercises/solutions.md (fy6-3-L1-10, Järkevyys) — "40 · 0,0112 Ω = 0,45 Ω" repeats the substitution in two steps rather than checking it; a comparison with the lesson's L1-04 cable (25 m, 2,5 mm², 0,17 Ω) or the remark that the lesson table's 1,7·10⁻⁸ Ω·m gives the same 0,45 Ω would be a real check.

## Checked
- Hash b00b18d0b241bb39 at start and end; delta: only fy6-3-L1-10 judged.
- Law and conditions: R = ρl/A for a uniform copper wire, the lesson's formula and notation; 20 °C table value, nothing heats the wire in the task.
- MAFY value: copper 1,678·10⁻⁸ Ω·m is the VERIFIED row of docs/mafy-arvot.tsv (Virtapiirit > Resistiivisyyksiä, Johteet), and the hint names that table.
- Recomputed: A = 1,5 mm² = 1,5·10⁻⁶ m²; R = 1,678·10⁻⁸ Ω·m · 40 m : 1,5·10⁻⁶ m² = 0,4475 Ω ≈ 0,45 Ω; answers.py agrees. With the lesson table's 1,7·10⁻⁸ Ω·m: 0,453 Ω, still inside tolerance 3 %, so either source is accepted.
- Magnitude realistic (a 40 m run of 1,5 mm² installation cable, about 0,45 Ω); two significant figures follow from l and A; unit Ω and tolerance fit.
- Solution complete: given, principle and why, symbolic formula, mm² → m² conversion, substitution with units, rounding reason, unit check.
