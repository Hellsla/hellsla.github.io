VERDICT: PASS
CONTENT-HASH: 0153dce31f9e43a0

## Blocking

## Polish
- exercises/solutions.md (helium-bottle task, Kaava last row) — the balloon count is now written $N = \Delta n / n_\text{p}$, but the lesson uses $N$ for the number of particles ($N = nN_\text{A}$, $p \propto NT/V$). Use another symbol (e.g. $N_\text{p}$ or "pallojen lukumäärä $= \Delta n/n_\text{p}$").
- exercises/solutions.md (oxygen-bottle and argon tasks) — Kaava now ends with $p = mRT/(MV)$, while Sijoitus still computes $n$ first and then $nRT/V$. Correct physics; the house rule asks to substitute into the last symbolic form, so either stop the Kaava at $p = nRT/V$ or substitute into $mRT/(MV)$.

## Checked
- Every changed Kaava starts from $pV = nRT$ (or $n = m/M$, $M = m/n$) and solves symbolically: $n = pV/(RT)$, $p = nRT/V$, $V = nRT/p$, $T = pV/(nR)$, $M = mRT/(pV)$, $N = pVN_\text{A}/(RT)$; all algebra and the absolute pressure/kelvin conditions right.
- Diesel task: $p_1V_1 = nRT_1$, $p_2V_2 = nRT_2$ → $T_2 = T_1\,p_2V_2/(p_1V_1)$; closed valves give constant $n$; 828 K, 555 °C recomputed.
- Two-gas graph task: $n_\text{A} - n_\text{B} = (p_\text{A}-p_\text{B})V/(RT)$ and $n_\text{A}/n_\text{B} = p_\text{A}/p_\text{B}$ at the same $T$ and $V$: 0,0241 mol and 1,67 recomputed.
- Window gap: $\Delta m = n(M_\text{Ar} - M_\text{ilma})$, $pAd = nRT$ → $d = \Delta m\,RT/(pA(M_\text{Ar}-M_\text{ilma}))$; same $n$ at same $p, V, T$ is the right reason.
- Leak tank: $\Delta p\,V = \Delta n\,RT$ at constant $V, T$; gauge offset cancels; 0,719 kg recomputed.
- Combined law derived from $pV/T = nR$; 2,31 l recomputed. Tyre leak: $1 - p_2T_1/(p_1T_2) = 5{,}47\,\%$ recomputed.
- Slope task: $V = (nR/p)\,T$, $k = nR/p$, $n = kp/R$; units cm³/K → 10⁻⁶ m³/K; 4,95 mmol recomputed.
- Weather balloon and helium bottle: the added first row $pV = nRT$ and rows unchanged otherwise; interpolation formula right.
- Numbers, Muunnokset and Sijoitus unchanged against the previous PASS; spot recomputation of 1,3·10²² molecules, 10,9 mol, 157,7 kPa, 8,96 l, 324 K, 179,6 bar, 27,9 g/mol agrees.
- Hash the same at start and end.
