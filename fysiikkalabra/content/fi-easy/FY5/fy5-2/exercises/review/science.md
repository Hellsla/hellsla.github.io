VERDICT: PASS
CONTENT-HASH: a013dbc7e633f71e
Mode: delta (Kaava steps rewritten as aligned derivations from ΣM = 0 / ΣF = 0; Periaate paragraphs split)
Round 1

## Blocking
(none)

## Polish
- solutions.md:186 (L3-01) — the derivation stops at $x - x_2 = \dots$, and $x = x_2 + \dots$ is only reached in Sijoitus — add a final line $x = x_2 + \dfrac{m_\text{L}(x_2 - x_\text{L})}{m_\text{m}}$.
- solutions.md:47, 76 (L1-05, L1-08) — $r_1$, $r_2$ in line 2 are not defined before line 3 replaces them with $x_\text{pp} - x_1$ and $x_2 - x_\text{pp}$ — add $r_1 = x_\text{pp} - x_1$, $r_2 = x_2 - x_\text{pp}$ first, the way L2-07 and L3-01 do.

## Checked
- Every rewritten Kaava block (L1-01…L1-08, L2-01…L2-07, L3-01…L3-05) starts from the right basic equation (ΣM = 0 about the stated pivot, ΣF = 0, or the centre-of-mass condition), and each line follows algebraically from the line before it.
- Sign and direction of each moment agree with the Periaate's rotation senses (e.g. L2-01: G counterclockwise and N₁ clockwise about the right support; L3-03: F(L − a) = mg(L/2 − a) about the rear carrier).
- L3-03 expansion (mg − F)a = ½mgL − FL is correct; L3-04: ΣF_y, ΣF_x with f = μN at the limit, and ΣM about the foot with arms L sin α and s cos α are correct.
- L2-05: N₁ = ½m_L g + mg − (mg/L)x, slope k = −mg/L, m = −kL/g are correct.
- Every final symbolic form is the expression the unchanged Sijoitus line substitutes into.
- Recomputed all answers in one script: 960 N, 0.75 N, 206.7 N, 58.86 N, 0.60 m, 0.98 m, 1.6 m, 98.1 N, 555.9 N, 12.53°, 448.65 N, 61.9 kg, 209.9 N, 3.333 m, 196.2 N, 1.213 m, 4.575 m, 42.22 cm / 52.97°. All agree with the solutions.
- Sijoitus lines, answers and tolerances are unchanged apart from layout (`\quad` line breaks in L3-01 Järkevyys and L3-04 Sijoitus).
- The paragraph splits in Periaate/Mallivastaus/Vastaus (L1-06, L2-05 b, L2-06, L3-02, L3-04, L3-05) change no physics.
