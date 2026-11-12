VERDICT: PASS
CONTENT-HASH: 154e845f80e129c9
Delta review (formulas in MAFY form, 2026-11-12) of the version passed at b053cd2d9ea1dacc.

## Blocking
(none)

## Polish
1. `unit.md`, the sentence after the light block: in the same sentence $n$ is the refractive index and also the order in the grating equation, and the thin-film condition then writes the order as $k$. Both meanings are defined, but they clash. Fix: "hilayhtälössä $n$ on kertaluku (ei taitekerroin)", and say that the thin film uses $k$ because $n$ is its refractive index.
2. `unit.md`: $e = vBl$ still uses $l$, while the block now writes the length as $\ell$. Fix: write $e = vB\ell$.
3. `inquiry.json`, `sovella/tasks.json` (and the exit ticket) still use $d\sin\theta = k\lambda$, $qvB$, $e_0$ and $U_0$. They are defined there, but they differ from the theory. Fix: align them in the next task pass.

## Checked
$F_\text{M} = QvB_\perp$ with $B_\perp = B\sin\alpha$. $r = mv/(QB)$. $B = N\mu_0 I/\ell$. $u_0 = NAB\cdot 2\pi f$: I recomputed it with N = 100, A = 0.01 m², B = 0.2 T and f = 50 Hz, giving 62.8 V, and $U_\text{eff}$ = 44.4 V. The transformer is written with ≈ for the currents and the ideal-transformer condition. $\lambda_\text{max} = b/T$. For Snell's law I recomputed $\sin\alpha_1/\sin\alpha_2 = v_1/v_2 = n_2/n_1$ = 1.5. $d\sin\alpha = n\lambda$. All are MAFY's forms with their conditions, and the map matches. The fi-easy text says the same physics as fi. The other rows are unchanged.
