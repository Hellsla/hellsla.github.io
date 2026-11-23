VERDICT: PASS
CONTENT-HASH: 6eb4939ade4d46cc
SCOPE: delta added-exercise from 2d1c8a6a30bbcd6d base 81db4a6fd727

## Blocking
(none)

## Polish
- solutions.md:129 and :219 — Kaava still reads "λ = v/f ja suhde b/λ" (no starting equation, no simplification); write v = fλ, λ = v/f, then the ratio, as elsewhere.
- solutions.md:273 — Kaava is just "v = f\lambda"; fine for a one-step task, but align with the others if the task rearranges.

## Checked
- The diff in the packet shows the aligned rows without their line breaks; the files on disk have them (`\\` between rows), so this is a rendering of the diff only.
- Every rewritten Kaava starts from basic equations (s = vt, s = 2d, v = fλ, φ = α + β) and is solved symbolically to the end before Sijoitus.
- Algebra checked: d = vt/2, t = 2d/v, Δt = d sinα / v, v = 2L/t, f = v/b, v from the time difference (t0 cancels), α = φ/2, α = sin⁻¹(vΔt/d).
- Sijoitus, answers and tolerances unchanged.
- L1-07, L2-06, L3-01 model answers split into paragraphs only; no content change.
