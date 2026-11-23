VERDICT: PASS
CONTENT-HASH: b5df027644f73b9c
SCOPE: delta, Kaava steps rewritten (basic equation, then simplified symbolically)

## Blocking
(none)

## Polish
1. solutions.md:300 (banked curve without friction) — the step `tan α = N sin α / (N cos α)` skips what makes it work: the row above gives N cos α − mg = 0 but never writes N cos α = mg, and the next row never writes N sin α = m v₀²/r over it. Add the two rows "N cos α = mg" and "N sin α = m v₀²/r", then "tan α = (m v₀²/r)/(mg)", so the student sees where N and m cancel.
2. solutions.md:302 (banked curve with friction) — the aligned block repeats the same left side twice (`ΣF_x = N sin α + μ₀ N cos α` and `ΣF_x = m v²/r`), which reads like a chain of equalities. Write it as `N sin α + μ₀ N cos α = m v²/r` on one row and the y-equation on another.
3. Rows of the form `ΣF_y = N − mg` then `ΣF_y = m a_n` (the circle-top and bottom tasks) have the same layout problem: one row with the two sides, `N − mg = m a_n`, is clearer.
4. solutions.md:5, :15, :45, :74 — single-formula Kaava rows. Fine; the first two come from the given data, so no step is missing.

## Checked
- Every changed Kaava now starts from Newton's second law (ΣF = m a_n) or from the lesson's definition (a_n = v²/r, v = 2πr/T), then simplifies symbolically to the asked quantity (v, N, μ₀, r, f, m). Substitution and answers are unchanged. This is the house rule for a Kaava step.
- Force tasks first state the equilibrium in the y-direction (N = mg), then the maximum static friction F_μ = μ₀N = μ₀mg at the limit, then F_μ = m a_n. This is the right order and uses the glossary terms.
- The graph task derives F = m v²/r, then F = (m/r)v², then the slope k = m/r before m = kr. The student sees why the slope gives the mass.
- The vertical loop task has separate bottom and top equations and the N = 0 limit giving v_min = √(gr); the sign convention (towards the centre) is stated.
- The mass-in-a-car Mallivastaus and the long Järkevyys paragraphs are split into short ones with one idea each.
- Wall of the explanation: the three false statements (centrifugal force, no sideways force) are each named and refuted. Content unchanged.
- Text read only; no renders opened.
