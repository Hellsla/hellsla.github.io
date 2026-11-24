VERDICT: PASS
CONTENT-HASH: c75053d468fb5e32

## Blocking
None.

## Polish
- fy3-s1 d) Kaava: the chain stops at $P_\text{häviö} = P - P_\text{vesi}$. It could be simplified to the end, $P_\text{häviö} = P - cm\,\dfrac{\Delta T}{\Delta t}$, and the substitution then made into that one form. The physics is right as it stands.
- fy3-s1 c) Kaava: the number $800\,\text{W/m}^2$ appears in the symbolic chain. A symbol for it (for example $I$, named in Annettu) would keep the chain fully symbolic. The row $P_\text{a} = P$ is fine as a statement that the useful power is the b) power.
- fy3-s3 a) Kaava: the last form keeps $p_1$ and $p_2$, and the substitution computes $p_1$ separately. This is acceptable as a two-step chain. A fully simplified form would be $V_2 = V_1 \cdot \dfrac{p_0 + \rho g h}{p_0} \cdot \dfrac{T_2}{T_1}$.
- fy3-s3 c) Kaava: in $\Delta p_\text{s} V_\text{s} = nRT$, $n$ is the amount of air used, not the amount in the tank. Writing $\Delta n$ in both rows would make this clear. The chain also ends with two formulas. It could finish with $t = \dfrac{\Delta p_\text{s} V_\text{s}}{p\,q}$. The equating is correct because the temperature is equal by the task's assumption, and the tank volume is constant.

## Checked
- I recomputed every number independently (script output matches answers.py and solutions).
  - s1: b) $237\,\text{W}$; the 5 min secant gives $229\,\text{W}$. c) $0{,}594$. d) $P_\text{vesi} = 119\,\text{W}$, loss $118\,\text{W}$.
  - s2: a) $117{,}0\,{}^\circ\text{C}$. c) $0{,}127\,\text{kg}$. d) $0{,}0315$; the steam volume is about $74\,\text{l}$, consistent with "noin $70\,\text{l}$".
  - s3: a) $p_1 = 248{,}15\,\text{kPa}$, $V_2 = 10{,}3\,\text{cm}^3$. b) $14{,}7\,\text{l}$. c) $725\,\text{l}$, $36{,}3\,\text{min}$, $89\,\text{min}$ at the surface. d) the lung/tank warming factor $310/279 \approx 1{,}11$ matches "noin $10\,\%$".
- Every changed Kaava step:
  - Each starts from its basic equations: $Q = P\Delta t$ and $Q = cm\Delta T$; $\eta = P_\text{a}/P_\text{o}$; $E = Pt$, $E_\text{hyöty} = \eta E$ and $Q = rm$; $Q_\text{luovutettu} = Q_\text{vastaanotettu}$; $p = p_0 + \rho g h$ and $pV = nRT$.
  - Each derives the combined formula correctly, and no row is algebraically wrong.
  - Conditions are stated in Periaate: constant pressure, which keeps the boiling temperature fixed (s2 c); the whole mass is used because the evaporated share is small (s2 d); constant $n$, and the bubble is at water temperature (s3 a); equal temperature by the task's assumption (s3 c).
- Scope: everything is within FY3 (heat, phase change, the gas laws, hydrostatic pressure, efficiency). $P = UA\Delta T$ is used qualitatively under heat transfer.
- Units, significant figures and rounding reasons are unchanged and correct. The rubric criteria match the Kaava rows (s1 b, s2 c, s2 d, s3 a), and the points add up.
- Hash at start and end: c75053d468fb5e32.
