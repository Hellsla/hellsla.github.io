VERDICT: PASS
CONTENT-HASH: c47364fb7325d02e
Delta review (merge of #523 solution practice into #522, 2026-11-13) of the version passed at c47364fb7325d02e.

## Blocking
(none)

## Polish
- Spring part (line ~734): Kuvaajan lukeminen still writes $m = -\tfrac{b}{\text{kulmakerroin}}$, but the new Kaava names the slope $a$. $-b/a$ would match.

## Checked
- Organ pipe b: $\varepsilon = v'/v - 1 = -0.0207$ with $v = 343.2$ m/s from part a; $f_1' = 128.3$ Hz. c: $\Delta L = -0.362$ mm and $\Delta f/f_0 \approx -\alpha\Delta T = +2.76\cdot10^{-4}$; the sign is right (a shorter pipe gives a higher frequency) and the small-change condition is stated.
- Line loss $P_\text{j} = R_\text{j}I^2 = 114$ W. Geotherm $T = 109.3\,{}^\circ\text{C}$. Spring: $k = 4\pi^2/a = 25.0$ N/m and $m_\text{j} = b/a = 20.5$ g.
- Note: the hash is unchanged although sovella/solutions.md changed, so the hash appears not to cover this file.
Every number in the changed lines was recomputed with an independent script (scratchpad fy9merge/sci_fi.py); `units.py hash` gave the same value at the start and the end. LaTeX in all added lines has balanced `$` and braces.
