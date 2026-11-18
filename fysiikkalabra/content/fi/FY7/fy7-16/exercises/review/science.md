VERDICT: FAIL
CONTENT-HASH: 905164bba71904d9

## Blocking
- solutions.md:95 (fy7-16-L3-01) — the new symbol $N = k - 1$ is never named and is not used afterwards: the Sijoitus says "vahvistimia $11 - 1 = 10$". In this chapter $N$ already means the number of turns of the receiver coil ($e_0 = N \cdot 2\pi f \cdot \Phi_0$, used in L2-09, L3-02 and L3-03 of the same set), so a student reads a symbol the lesson defines differently. The physics and the answer (10) are right. Fix: write the last row as "vahvistimien määrä $k - 1$" as before, or use a distinct named symbol (e.g. $N_\text{v}$, vahvistimien määrä) and use it in the Sijoitus ($N_\text{v} = 11 - 1 = 10$).

## Polish
- solutions.md (L3, induction hob $f_\text{C}$) — "$\sim \dfrac{f^2}{R}$" means "is proportional to"; $\propto$ or a word ("verrannollinen") is clearer.

## Checked
- Delta: only Kaava steps rewritten as aligned blocks (L1-04, L1-05, L3-01, L3-02, L3-03, L1-07, L1-08, L2-07, L2-08, L3-04, L3-05, L2-09, L2-10) plus paragraph splits; no number, answer, unit or tolerance changed.
- dB chains start from $A = 10\,\text{dB}\cdot\lg(P_0 : P)$ and $A = aL$ and solve right: $L = A : a$, $P = P_0 \cdot 10^{-A/(10\,\text{dB})}$, $a = 10\,\text{dB}\cdot\lg 2 : L_{1/2}$, with splices $A = aL + 4\cdot 0{,}50\,\text{dB}$ and $t = nL : c$.
- L1-05: $Q = cm\Delta T = \eta P t$ gives $t = cm\Delta T : (\eta P)$; no change of state, stated.
- L3-01: $l_\text{max} = A_\text{max} : a$, $k \ge L : l_\text{max}$ rounded up, amplifiers one fewer than sections: physics right, 10 amplifiers.
- L3-02 and L3-04: $\Phi_0 = B_0\pi r^2$, $e_0 = 2\pi f\Phi_0$, $P = e_0^2 : (2R)$ from $U = e_0 : \sqrt2$; equal powers give $f_\text{C} = f\sqrt{R_\text{C} : R_\text{A}}$: right.
- L2-09: ratio $e_0' : e_0 = \Phi_0' : \Phi_0$ at fixed $N$ and $f$: right.
- Recomputed in one script: 150 km, 5,24 min, 10, 1596 W, 0,441 ms, 0,504 mW, 15,05 km, 1,0 %, 42,4 kHz, 2,8 V, 0,78 %: all unchanged and right.
- Hash 905164bba71904d9 at the start and at the end.
