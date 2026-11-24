VERDICT: FAIL
CONTENT-HASH: 76e86f953efa066e

## Blocking
1. **fy3-s3 c, Formula (B).** The chain opens with $\Delta p_\text{tank} V_\text{tank} = nRT$. That is the equation of state with a pressure difference on the left and an amount $n$ that is never named. It holds only if $n$ is the amount of air *taken out* of the tank, $\Delta n = n_1 - n_2$, at constant $V_\text{tank}$ and $T$, and the text does not say so. Written as a "basic equation", it teaches a wrong form of $pV = nRT$. The fix stays symbolic and starts from the basic law: $p_1 V_\text{tank} = n_1RT$, $p_2 V_\text{tank} = n_2RT$, so $(p_1 - p_2)V_\text{tank} = \Delta n\,RT$. Then $pV = \Delta n\,RT$ for the breathed air, and $V = \dfrac{\Delta p_\text{tank} V_\text{tank}}{p}$, $t = \dfrac{V}{q}$. Here $p_1 - p_2$ equals the gauge difference, as the Principle already explains. The numbers do not change.

## Polish
- fy3-s1 c, Formula: $P_\text{o} = 800\,\text{W/m}^2 \cdot A$ puts a number inside the symbolic chain. Naming the irradiance (e.g. $I = 800\,\text{W/m}^2$ in Given) would give $\eta = \dfrac{P}{IA}$. $P_\text{a}$/$P_\text{o}$ are Finnish subscripts in the en text. Not an error.
- fy3-s2 c: $m$ in $Q = rm$ is the vaporised mass, while the task's $1.50\,\text{kg}$ is also water mass. Find defines it, so this is only a possible confusion.

## Checked
- I recomputed every number in one script with my own formulas. s1: $P = 237\,\text{W}$ (first 5 min: $229\,\text{W}$), $\eta = 0.594$, $P_\text{water}(50\,\text{min}) = 119\,\text{W}$, $P_\text{loss} = 118.7\,\text{W}$. s2: $T = 117.0\,{}^\circ\text{C}$, $m = 0.127\,\text{kg}$, fraction $0.0315$, $43\,\text{g}$ ≈ $73\,\text{l}$ of steam. s3: $p = 248.15\,\text{kPa}$, $V_2 = 10.3\,\text{cm}^3$, $14.7\,\text{l}$, $725.8\,\text{l}$, $36.3\,\text{min}$, $89\,\text{min}$ at the surface, warming to $37\,{}^\circ\text{C}$ ≈ $+11\,\%$ (the "about 10 %" in d is fine). All of these agree with answers.py, tasks.json and the solutions.
- The changed Formula steps. s1 b ($Q = P\Delta t$, $Q = cm\Delta T$ → $P = cm\,\Delta T/\Delta t$), s1 d (power balance $P = P_\text{water} + P_\text{loss}$), s2 a (total pressure, then linear interpolation solved for $T$), s2 c ($E = Pt$, $E_\text{useful} = \eta E$, $Q = rm$ → $m = \eta Pt/r$), s2 d ($Q_\text{released} = Q_\text{received}$ first, then $cm\Delta T = rm_\text{v}$ → $m_\text{v}/m = c\Delta T/r$, with the approximation $m \approx$ whole mass stated in the Principle) and s3 a ($p_1 = p_0 + \rho gh$, $p_2 = p_0$, $pV = nRT$ with constant $n$ → combined gas law → $V_2$). Each one starts from the basic laws, simplifies symbolically to the end, is physically correct, and matches the rubric's `equation` details. s3 b (Boyle, body temperature) is correct.
- Scope is within FY3. Units, significant-figure reasons and rubric point sums (13, 15, 15) are consistent. No data is invented.
- Hash at the start and the end: 76e86f953efa066e.
