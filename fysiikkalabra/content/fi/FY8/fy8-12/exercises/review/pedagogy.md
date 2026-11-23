VERDICT: PASS
CONTENT-HASH: fb46aec0512cf1e0
SCOPE: delta numbers,reflow,typography from 15261a26498e83ce base 4b05399

## Blocking

## Polish

- solutions.md (L2-?? photon wavelength, Kaava) — `E = hf, josta f = c/λ` does not follow from E = hf; the basic law c = λf is missing — add `ja $c = \lambda f$` as fy8-15-L2-03 does.
- solutions.md (two-barrier ratio task, Kaava) — I_2 is written without showing that I_1 is substituted into it before the ratio I_2/I_0 — add the line `I_2 = I_0 (1/2)^a (1/2)^b` or say `sijoitetaan I_1`.
- solutions.md (L2-09, Sijoitus) — still writes `pulssia/min` while the unit field is `min^{-1}` (from the earlier report).

## Checked

- Diff = Kaava step only: basic law first, then `josta:` aligned derivation, symbolic before substitution; Sijoitus, answers and tolerances untouched.
- Sampled the source: aligned blocks render as separate lines (the packet diff flattens them); no stray numbers in Kaava.
- L3-02: required net rate 30 = R_t, so (1/2)^(d/d1/2) = R_t/(R_0-R_t) is right; logarithm steps complete.
- Count-rate and logarithm derivations are consistent across L2-L3 tasks; the student can follow each step.
- Hash unchanged at end.
