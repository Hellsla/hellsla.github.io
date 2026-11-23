VERDICT: PASS
CONTENT-HASH: eb20b821dc5ff1d9
Mode: delta (Kaava steps rewritten as aligned derivations from the decibel definition and equal-dose condition; paragraph splits)
Round 1

## Blocking
(none)

## Polish
(none)

## Checked
- Every reference-time derivation starts from the same basic principle: the dose is energy, so $I\,t_\text{v} = I_\text{v}\,t_0$ with $I = 2^{\,n} I_\text{v}$. This gives $t_\text{v} = t_0/2^{\,n}$. It is the equal-energy model the Periaate states, and "every $3\,\text{dB}$ doubles $I$" is the stated approximation ($10^{0{,}3} = 1{,}995$), not a hidden one.
- Two equal sources: $L_1 = 10\,\text{dB}\lg(I_1/I_0)$ and $L = 10\,\text{dB}\lg(2I_1/I_0)$ give $L - L_1 = 10\,\text{dB}\lg 2$. This is correct: the intensities add, not the levels.
- Distance: $I_2/I_1 = r_1^2/r_2^2$ (point source, the condition named in the Periaate). This gives $L_1 - L_2 = 20\,\text{dB}\lg(r_2/r_1) = 20\,\text{dB}\lg 2^{\,k} \approx k \cdot 6\,\text{dB}$, which is correct.
- Reverberation: equal decay rate, $(L_1 - L_2)/\Delta t = 60\,\text{dB}/T$, is correct under the stated steady-decay assumption.
- Multi-phase dose and protectors: $D = \sum t_i/t_{\text{v},i}$. A protector reduces every phase's $I$ by the same factor $2^{\Delta L/(3\,\text{dB})}$, so $D_\text{korva} = D/2^{\Delta L/(3\,\text{dB})} \le 1$. This is correct and consistent with the Periaate.
- Every final symbolic form is the one the unchanged Sijoitus line substitutes into.
- Recomputed in one script: 2.0 h, 73.01 dB, 82 dB (exact 81.98), 4.0 h, 150 %, 16 m, 0.90 s, 125 %, 46 dB, 2.52 h, 75.6 min. All agree with the solutions.
- Sijoitus, answers and tolerances are unchanged. The paragraph splits (L1-04 and L2-04 Järkevyys, L3-03 Mallivastaus, L2-10 Järkevyys) change no physics, model limits or safety statements.
