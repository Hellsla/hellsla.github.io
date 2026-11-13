VERDICT: PASS
CONTENT-HASH: 7cfdc14b6ecf2865

## Blocking
None.

## Polish
None.

## Checked
- Re-review of the fix: fy4-s2 b) Sijoitus (line 294) now writes the starting potential energy as E_p0 = 9123 J, consistent with E_p0 + E_k0 + W = E_p + E_k and the zero level at the brake (E_p = 0, E_k = 3889 J at the end). git diff HEAD~1: only this line changed in solutions.md; tasks.json untouched.
- Recomputed (own script): a) 17,2 m/s, b) 9123 J, 3889 J, 29,1 N, c) 13,6 m/s; numbers and answers unchanged.
- No leftover W_muut, E_k,1, F_∥ in any Sovella task; fi, fi-easy and en say the same.
