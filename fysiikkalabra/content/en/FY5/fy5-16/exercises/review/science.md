VERDICT: PASS
CONTENT-HASH: 8c7366b5969f48e3

## Blocking
(none)

## Polish
- content/en/FY5/fy5-16/exercises/solutions.md:103,105,204,207,219 — L3-01 and L3-04 still use the symbol t_perm,i while their text now says reference time — rename to t_ref,i for consistency.

## Checked
light delta review (teacher 2026-11-07): only the passages changed against origin/main were judged, in context; no full review was done even where the tooling asks for one. packet says Mode full, done as a light review of git diff of exercises/ and answers.py instead. 'Permitted time' replaced by reference time (time to reach the dose of 8 h at 85 dB) in L1-01, L2-01, L2-07, L3-05 and solutions; action values not called safe; lower action value 80 dB, protectors and noise reduction above 85 dB match VNA 85/2006. Recomputed 2.0 h, 4.0 h, 150 %, 1.875 min, 125 %, 3.75 min, 1.59 h, 190 %, 47 %: all correct.
