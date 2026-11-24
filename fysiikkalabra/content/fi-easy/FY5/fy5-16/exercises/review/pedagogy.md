VERDICT: PASS
CONTENT-HASH: eb20b821dc5ff1d9
none

## Blocking
(none)

## Polish
- solutions.md:35, 139, 174 — Kaava stays a single line (L = L_m − ΔL, ΔL = L_ulko − L_sisä); fine for one-step tasks.
- The old Polish items on L2-10 (terms "toiminta-arvo" and "raja-arvo" unexplained; b) and c) packing several questions) still stand; they are task text, not part of this change.

## Checked
- The diff in the packet shows the aligned rows without their line breaks; the files on disk have them, so only the diff view is garbled.
- The dose rule is now derived: n = (L − L0)/3 dB, I = 2^n I_v, equal dose I t_v = I_v t_0, so t_v = t_0/2^n. Each step is one row, correct, and shows why the time halves per 3 dB.
- Distance rule derived: I2/I1 = r1²/r2², L1 − L2 = 20 dB·lg 2^k ≈ 6k dB, k = (L1 − L2)/6 dB, r2 = 2^k r1. Algebra correct (20·lg 2 = 6,02).
- Combining two equal sources and the reverberation time (ΔL/Δt = 60 dB/T) start from the definition or the constant rate, then solve for the unknown; correct.
- The protector case adds I_korva = I/2^(ΔL/3 dB) and D_korva = D/2^(ΔL/3 dB), correct and explained in Periaate.
- Sijoitus, answers and tolerances unchanged; paragraph splits in L1-04, L2, L3 solutions only improve readability.
