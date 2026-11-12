VERDICT: PASS
CONTENT-HASH: 366f0086e97819e0
Delta review (formulas in MAFY form, 2026-11-12) of the version passed at 3b6f5d5631f07584.

## Blocking
(none)

## Polish
1. `unit.md`, the sentence after the light block: $n$ is the refractive index and also the order in the grating equation, both in one sentence, and the thin film writes the order as $k$. Fix: "in the grating equation $n$ is the order (not the refractive index)", and explain the $k$ in the thin film.
2. `unit.md`: $e = vBl$ still uses $l$, while the block now uses $\ell$. Fix: $e = vB\ell$.
3. `inquiry.json` and `sovella/tasks.json` still use $d\sin\theta = k\lambda$, $qvB$ and $e_0$. Fix: align them.

## Checked
$F_\text{M} = QvB_\perp$ with $B_\perp = B\sin\alpha$. $r = mv/(QB)$. $B = N\mu_0 I/\ell$. $u_0 = NAB\cdot 2\pi f$: I recomputed it with N = 100, A = 0.01 m², B = 0.2 T and f = 50 Hz, giving 62.8 V, and $U_\text{eff}$ = 44.4 V. The transformer is written with ≈ for the currents and the ideal-transformer condition. $\lambda_\text{max} = b/T$. For Snell's law I recomputed $\sin\alpha_1/\sin\alpha_2 = v_1/v_2 = n_2/n_1$ = 1.5. $d\sin\alpha = n\lambda$. All are MAFY's forms with their conditions, and the map matches. The English text says the same physics as fi. The other rows are unchanged.
