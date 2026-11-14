VERDICT: PASS
CONTENT-HASH: ae045ef3e021670a
SCOPE: delta added-exercise from 99bf518cf2d541bd base 8f23aa7ae3bd

## Blocking
- none

## Polish
- none

## Checked
- fy6-11-L1-09 recomputed: U = E·d = 3,0 kV/mm · 2,5 mm = 7,5 kV; matches answers.py and exercises.json (unit kV).
- Lookup value: air's dielectric strength about 3 kV/mm (3 MV/m) is the standard table value; tolerance 0,1 allows for a table edition giving a slightly different value.
- Model: homogeneous field E = U : d (stated in the task), breakdown when E reaches the dielectric strength; the gap dependence of air breakdown at mm gaps is a fair simplification at this level (C).
- Unit handling kV/mm · mm = kV right, no conversion needed; rounding to two figures justified.
- Solution complete (given, principle, symbolic U = Ed, conversions, substitution, rounding reason, check); in scope (LOPS FY6 safety content "läpilyöntilujuus" and the uniform field).
- Content hash checked at start and end.
