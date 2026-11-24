VERDICT: PASS
CONTENT-HASH: b3173cb95ad51c48
Round: 2
Mode: delta

## Blocking

## Polish
- exercises/solutions.md:55, 105, 118, 133 (L1-06-type p = mRT/(MV), N = pVN_A/(RT), d = Δm RT/(pA(M_Ar − M_ilma)), Δm = ΔpVM/(RT)) — the Kaava now ends in the fully combined form, but the unchanged Sijoitus still substitutes step by step (n first) — either substitute into the last form or end the Kaava where the Sijoitus starts.

## Checked
- Every changed Kaava starts from pV = nRT (or M = m/n) and solves the asked quantity symbolically; all rows algebraically right.
- Combined gas law rows (T2 = T1·p2V2/(p1V1); V2 = p1V1T2/(p2T1)) are derived from pV = nRT with constant n, which Periaate states (valves shut, no gas escapes).
- ΔpV = ΔnRT is used only where V and T are constant (stated in Periaate); the gauge-pressure difference cancels p0, as said.
- Leak fraction (n1 − n2)/n1 = 1 − p2T1/(p1T2) right; recomputed 0.0547.
- (T, V) slope k = nR/p → n = kp/R right; (T, p) slope ratio nA/nB = pA/pB at equal V and T right.
- Recomputed by script: p = 1.796·10⁷ Pa, M = 27.93 g/mol, Δm = 0.7192 kg, n = 0.5455 mol; unchanged answers agree.
- Hash identical at start and end.
