VERDICT: PASS
CONTENT-HASH: 828149724ec250da

## Blocking

## Polish
- solutions.md (L3, induction hob $f_\text{C}$) — "$\sim \dfrac{f^2}{R}$" means "is proportional to" (carried). — Use $\propto$ or the word "verrannollinen".

## Checked
- Round-1 finding fixed: L3-01 now ends with "$\text{vahvistimien määrä} = k - 1$". No $N$ clashes with the coil's number of turns.
- dB chains start from $A = 10\,\text{dB}\cdot\lg(P_0/P)$ and $A = aL$, solve for $L = A/a$ or $P = P_0\cdot 10^{-A/(10\,\text{dB})}$, and invert the logarithm correctly.
- Splice task: $L = (A - 4\cdot 0{,}50\,\text{dB})/a$ and $t = L/v = nL/c$, with $v = c/n$ now shown.
- Half-length: $a = A_{1/2}/L_{1/2} = 10\,\text{dB}\cdot\lg 2/L_{1/2}$.
- L1-05: $\eta Pt = cm\Delta T$ gives $t = cm\Delta T/(\eta P)$; no change of state.
- L3-02/L3-04: $\Phi_0 = B_0\pi r^2$, $e_0 = 2\pi f\Phi_0$ and $P = e_0^2/(2R)$; equal powers give $f_\text{C} = f\sqrt{R_\text{C}/R_\text{A}}$.
- Charger task: $\Phi_0 = e_0/(N\cdot 2\pi f)$ comes from $e_0 = N\cdot 2\pi f\Phi_0$; the interpolation is unchanged. L2-09: the ratio holds at fixed $N$ and $f$.
- Earlier recomputation stands, since no number or answer changed: 150 km, 5,24 min, 10, 1596 W, 42,4 kHz, 2,8 V.
- Hash identical at start and end.
