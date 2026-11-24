VERDICT: PASS
CONTENT-HASH: 09aa7395019efc50

## Blocking
- none

## Polish
1. k3 a) Kaava: $n = \dfrac{pV}{RT}$ should carry the state index ($T_1$), as $V = Ah_1$ does. Stopping at $n = pV/(RT_1)$ and not substituting $p$ and $V$ back in is fine, because $p$ is asked on its own.
2. k7 d) The new Kaava now defines $\Delta U = U_\text{vanha} - U_\text{uusi}$. That is correct, but in this exam $\Delta U$ also stands for the change in internal energy (k1 e, k3 d). Writing $(U_\text{vanha} - U_\text{uusi})$ throughout, or $U_1 - U_2$, would avoid the clash.
3. k7 e) Kaava: $Q_1$ and $W$ mean the annual quantities in b) but the per-MWh quantities here. That is acceptable because Periaate says "$1{,}0\,\text{MWh}$". The heat could be named for this part, e.g. $Q_1 = 1{,}0\,\text{MWh}$ under Annettu.
4. Carried over: k2 d) the rubric says "noin $10\,{}^\circ\text{C}$" and the solution "noin $9\,{}^\circ\text{C}$" (the exact shift is $9{,}4\,{}^\circ\text{C}$). k6 d) "Hyväksytään myös" accepts 7–8 min, about 290–330 kJ/kg, but the 6 % tolerance starts at about 297 kJ/kg. k4 a) Järkevyys says "lähes yhtä suuri" for 333 vs 419.

## Checked
I ran the hash at the start and the end: 09aa7395019efc50 both times. Since the last science PASS (815f454d8557aa79, carried to 6c615247d936cbd2), only the **Kaava** lines of solutions.md changed. The diff confirms that the numbers, answers, rubrics and answers.py are unchanged. I judged each of the 17 changed Kaava steps in its part:
- k2 b, d: $k = \Delta L/\Delta\theta$, $L = L_0 + k\theta$ and the zero condition give $\theta_0 = -L_0/k$. Correct, and $L_0'$ in d) is consistent with Periaate.
- k3 a: $G = mg$, then $p = p_0 + G/A$, then the gas law with $V = Ah_1$. Correct.
- k3 b: Charles's law with the area cancelled. Correct.
- k3 c: $W = Fs$, $F = pA$, $s = \Delta h$, so $W = p\,\Delta V$. This is the FY3 scope ($W = Fs$ only), and the force is the gas's force on the piston.
- k4 a: three heats summed. k4 b, c: $\eta = E_\text{hyöty}/E$ with $E = m_\text{k}H$. Correct.
- k5 c: $p_1 = p_2 + \rho g h$. The lower point has the higher pressure, so the sign is right. k5 d: the balance $p_1 - \rho g h = p_\text{k}$ is solved symbolically. Correct.
- k6 c: $P = Q/\Delta t$ and $Q = cm\Delta T$ give $P = cmk$. k6 d: $Q = P\Delta t = sm$. Correct.
- k7 a: parallel conduction, $P_i = U_iA_i\Delta T$, summed. k7 b: $\varepsilon = Q_1/W$ is the heat delivered per unit of electricity, which is correct for a heat pump.
- k7 d: the difference of conduction powers, then $\Delta W = \Delta Q_1/\varepsilon$. This holds because $\varepsilon$ is constant.
- k7 e: $\eta_\text{l} = W/E_\text{pa}$ (electricity out over fuel energy), $\eta_\text{ö} = Q_1/E_\text{pa}$, then emission = energy · factor. Correct.

Every chain starts from its basic equation, simplifies symbolically and ends in the form the Sijoitus line uses. Every Sijoitus agrees with its Kaava.

I recomputed every number in one script with my own formulas, and all agree with answers.py:
- k1: a 4,05 N, d 10,3 m, i 6,8 %
- k2: −272,9 °C and −282,4 °C
- k3: 130,4 kPa, 0,0535 mol, 5,12 cm, 26,7 J, 66 J
- k4: 922 kJ, 47,7 % (45,6–50,1), 252 kJ
- k5: 15,1 cm, 325 kPa, 51,8 m
- k6: 277 W, 316 kJ/kg
- k7: 2420 W, 20,3 MWh, 6,78 MWh, 748 kWh, 284 kg, 296 kg

The rest is unchanged from my previous full review.
