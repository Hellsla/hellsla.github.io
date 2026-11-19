VERDICT: PASS
CONTENT-HASH: 97c516b0e2108e09

## Blocking
None.

## Polish
- fy7-s2 c, Periaate and Kaava: $e_0 = NBA \cdot 2\pi f$ is the rotating-coil formula. The claw-pole hub dynamo needs only $e_0 \propto f$ (Faraday: the flux changes faster), and the solution uses only that. The constant $\kappa = 28NBA : (\sqrt{2}D)$ gives $N$, $B$ and $A$ a meaning they do not have in this geometry. A sentence saying only the proportionality is used would avoid that (C, not a finding).
- fy7-s4 a: the solution claims three significant figures because the peak is "on a gridline", but $\lambda_\text{max} = 2{,}0\,\mu\text{m}$ is read to about $\pm 0{,}05\,\mu\text{m}$ (2,5 %). Two figures ($1{,}4 \cdot 10^3\,\text{K}$) or "three, with the uncertainty judged in d" is more honest. The tolerance accepts either.
- fy7-s4 c: "kolme merkitsevää numeroa, kuten taitekertoimissa". $\theta$ depends on $n_1^2 - n_2^2$, so its real precision is lower. This does not affect the answer check.

## Checked
- Kaava steps (work queue 8g) in all 25 parts: each starts from its basic law (energy principle, $F_\text{s} = F_\text{m}$, $F_\text{m} = ma_\text{r}$, $v = s/\Delta t$, $\eta = P_\text{valo}/P_\text{otto}$, $R = \rho l/A$ with $P = UI$, Kirchhoff's voltage sum, $B = \mu_0 I/(2\pi r)$ with $F = IlB$, $m = \rho V$, Snell at $90^\circ$, $\Delta s = 2nd$, slope $= 1/d$). Each simplifies symbolically to the form the numbers are put into. The derived forms are algebraically correct, and $\kappa$ is correct.
- One script recomputed every number from the task text with my own formulas: $v$, $U_\text{s}$, $B$, $\Delta x$, $v_{10}$, the 0,91 ratio; $f$, $U$, 18,8 and 11,4 km/h, 0,95 N, the >250 km/h error case, the 9 N hill; $R$, 846 kW, 28,0 kW, 17,18 kV, 4540 mm², 7,6 cm, 20 t and 613 t, 0,012 and 8,53 N/m, 3,97 N/m; 1449 K / 1176 °C, ±36 K, $\alpha_\text{r} = 80{,}44^\circ$, $\theta = 13{,}84^\circ$ (also from $\sqrt{n_1^2-n_2^2}$), 362 nm, 1000 nm with strong 500 nm and weak 667/400 nm; the six hydrogen angles match $d = 1666{,}7\,\text{nm}$ to 0,1°, fitted slope 6,003·10⁻⁴ 1/nm, 589,1 nm, ±3 nm, He–Na 0,053° and 0,140°, ±1,0 nm. All agree with the text, the answers and answers.py.
- Physics: force directions and plate polarity, the analyser bending up, and the Lenz and eddy-current reasoning in s2 d. Repulsion between opposite AC currents, and the grey-body claim (peak not shifted). Both reflections inverting at 1,00→1,38→1,50, and grating against prisma dispersion. All correct, and the stated model assumptions are in the task texts.
- Scope: within FY7. There is no self-induction (s2 c's "jää käämiin itseensä" names no mechanism), and no photon.
- Rubrics: every criterion matches its task and solution. Points add up (16 + 16 + 17 + 17 + 17). Other methods are listed under Hyväksytään myös. Invented data is declared in source_note. Figures: the Planck peak is at 1,9998 µm, and the implanter arc and force figure are correct.
