VERDICT: PASS
CONTENT-HASH: 1a68fec8b98d05e5

## Blocking

## Polish
- solutions.md:300 (fy3-3-L2-08): $p_0$ here is the pressure at $0\,{}^\circ\text{C}$, but in L3-05 (line 247) $p_0$ is the air pressure. Within each task the meaning is clear. Writing $p(0\,{}^\circ\text{C})$ or $p_1$ in L2-08 would avoid the clash.

## Checked
- I read every changed Kaava block on disk as an aligned block (the packet's diff shows the rows joined). They are L1-02, L1-03, L1-04, L1-05, L2-01, L2-02, L2-04, L2-08, L3-01, L3-02 and L3-03.
- The scale relation. L1-02, L1-03 and L1-05 rearrange $T/\text{K} = \theta/{}^\circ\text{C} + 273{,}15$ correctly for $\theta$. The results are $76{,}85$, $-195{,}75$ and $-270{,}45\,{}^\circ\text{C}$.
- L1-04: the derivation now shows the constant $273{,}15$ cancelling in the difference, so $\Delta T/\text{K} = (\theta_2 - \theta_1)/{}^\circ\text{C}$. Correct, and it is the principle the task asks for.
- L2-01: $T_2 = T_1 + \Delta T$ is converted at the end and gives $59{,}85\,{}^\circ\text{C}$. Correct.
- L2-02: the line through $(0;\ p_1)$ gives $p = p_1 + \frac{p_2 - p_1}{\theta_2 - \theta_1}\theta$. The condition $\theta_1 = 0\,{}^\circ\text{C}$ is stated, and the result is $101{,}55\,\text{kPa}$.
- L2-08: $\theta = (p - p_0)/k = 25/0{,}275 = 90{,}9\,{}^\circ\text{C}$. Correct.
- L2-04: the ratio is formed from kelvin temperatures, $400{,}15/100{,}15 = 3{,}9955$. Correct, and the Periaate gives the reason, the absolute zero.
- L3-01 and L3-02: $p \propto T$ at constant volume and amount of gas, with total pressure. The results are $320{,}8\,\text{kPa}$, and $400{,}2\,\text{K}$, which is $127{,}05\,{}^\circ\text{C}$. Correct.
- L3-03: $E \propto T$ for a dilute gas, with the condition stated in the Periaate. $T_2 = T_1/2 = 146{,}575\,\text{K}$. Correct.
- L3-04 and L3-05: the answer paragraphs were split only. The numbers are unchanged and still correct ($796{,}7/701 = 1{,}136$, $695{,}7/600 = 1{,}16$). The difference between total pressure and overpressure is explained right.
- exercises.json: only caption markers changed. The hash was the same at the start and the end.
