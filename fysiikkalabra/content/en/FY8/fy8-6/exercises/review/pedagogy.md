VERDICT: PASS
CONTENT-HASH: 02af06d85c6fff13
SCOPE: delta md-paragraphs,numbers,reflow,typography from ceed05861c35b96a base 64d4935

## Blocking

## Polish

- solutions.md (energy-gap task, Kaava) — the last row jumps from `E_g = hc/λ` to `λ = hc/E_g` with no remark that it is being solved for λ. Fix: add "solving for λ:" in the lead-in or put the rearrangement as its own row.
- solutions.md (Kaava blocks of the LED tasks) — `\frac` and `\dfrac` are mixed between the aligned rows and the text; use `\dfrac` throughout for a consistent look.
- solutions.md (slope task, Kaava) — the line `k = ΔU_k/Δf ≈ h/e` appears without saying that k is the slope read from the fit; one clause fixes it.

## Checked

- The diff changes Kaava steps only; each now opens with the basic laws (E = hf, c = fλ, eU_k = E, I = Ne, P = NE) and derives the formula by rows. Numbers, answers and tolerances are unchanged.
- The packet's diff shows the aligned blocks flattened (e.g. "hf = hc/λ λ = …"); the file itself is correct, with one relation per row and the equals signs aligned.
- The earlier blocking item (L2-06: h_0 without 10^-34) is fixed; h_0 = 6.626·10^-34 J s is now right in the formula.
- L1-05, L3-04 and L2-06 Kaava are now stepwise. The earlier L3-04, L3-05 and L2-05 prose-paragraph polish items are done.
- The symbolic chain is simplified to the end before Substitution in every changed solution; each first row starts with the quantity it computes.
- The power and photon-ratio tasks keep a clear order (N, E, P), so a student can follow them without skipping a step.
