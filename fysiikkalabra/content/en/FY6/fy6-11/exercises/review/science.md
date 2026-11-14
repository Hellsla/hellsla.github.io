VERDICT: PASS
CONTENT-HASH: cb845d98a8762a90
SCOPE: delta added-exercise from 4161a9356eed0c2b base 8f23aa7ae3bd

## Blocking
(none)

## Polish
(none)

## Checked
- Delta: only the added exercise fy6-11-L1-09 judged; the rest unchanged per `reviews.py added_exercises`.
- Physics: uniform field between plates, E = U : d; breakdown when E reaches the dielectric strength of air, so U_max = E_max d. Condition (uniform field, air) stated in the task; the dielectric strength as a fixed table value is a fair simplification at this level (C).
- Recomputed: U = 3.0 kV/mm · 2.5 mm = 7.5 kV; answers.py 7.5; the 10 % tolerance covers table editions giving about 3 MV/m.
- Units: kV/mm · mm = kV correctly shown as no conversion needed; answer unit kV as asked.
- Solution complete: given/asked, principle with reason, symbolic rearrangement U = Ed before numbers, substitution with units, 2-sf rounding reason, reasonableness check (about 3 kV per mm).
- Lookup hint names the right MAFY table; scope inside FY6 (uniform field, LOPS dielectric strength under electrical safety).
