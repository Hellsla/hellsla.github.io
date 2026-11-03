VERDICT: PASS
CONTENT-HASH: b6a7c0dd81df93d1

## Blocking

## Polish
- exercises/solutions.md:18 (L1-02) — "kolme merkitsevää numeroa kuten vakioissa": the constants are given to four; justify by the wavelength $1550\,\text{nm}$ (three or four significant figures), e.g. "kolme merkitsevää numeroa, koska aallonpituus 1550 nm on annettu vähintään kolmella".

## Checked
- All 12 answers recomputed in one script with my own formulas; every answer within 0,9 % of mine and inside its 2 % tolerance (L1-01 1,9589 eV; L1-02 0,800 eV; L1-03 692,74 nm; L1-04 1,607·10^16; L1-05 1,493 mW; L2-01 75,94 %; L2-02 1,605; L2-03 527,66 nm; L2-04 5,04 MW; L3-01 1,806 J; L3-02 2,034·10^18; L3-03 9,22·10^4).
- answers.py computes the right physics for each task text.
- L3-01: inversion with the ground state as lower level needs more than N/2 ions excited; the task's "ei purkaudu" assumption is stated and the solution notes the bound is a lower limit.
- L3-02: one pump photon → at most one 1064 nm photon, two → one 532 nm; energy check 0,76 W < 1,0 W is a real check.
- L3-03: h cancels, so giving only c is enough; qubit gap 2,1·10^-5 eV is correct.
- L2-01 / L2-02: ratios λp/λL and λr/λv derived symbolically before substitution.
- Every solution has Annettu, Kysytty, Periaate, Kaava, Muunnokset, Sijoitus, Vastaus, Järkevyys; unknowns solved symbolically first; conversions correct.
- Rounding follows the limiting datum in all other tasks (L2-03 addition 2,00 + 0,35 eV keeps hundredths → 3 s.f.).
- Notation (hf = E2 − E1, P = (N/t)·hf, λ = hc/(E2 − E1)) matches the brief's lesson; data realistic (He-Ne, ruby, Nd:YAG, 1550 nm fibre, superconducting qubit 5 GHz).
