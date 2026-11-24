VERDICT: PASS
CONTENT-HASH: 4ff4935c29dd33cb

## Blocking

## Polish
- exercises/solutions.md (last task, Kaava row 1) — $\theta = T - 273{,}15\,\text{K}$ lost its old note "(celsiusasteina)"; as written the right side is in kelvins while $\theta$ is in degrees Celsius. Optional: keep the note or write it as in the lesson, $T = \theta + 273{,}15\,\text{K}$ with $\theta$ the numerical value.

## Checked
- Every changed Kaava starts from the line $p = p_0 + k\theta$ or $p = p_1 + k(\theta - \theta_1)$, sets $p = 0$ at $\theta_0$, isolates $k(\theta_0 - \theta_1) = -p_1$ and gives $\theta_0 = \theta_1 - p_1/k$ (or $-p_0/k$): the same derivation as the lesson's Kaava; signs right.
- Gauge-pressure task: $p = p_\text{y} + p_\text{ilma}$ first (absolute pressure is the linear one), then the line; 110 and 132 kPa, $k = 0{,}3667$, $\theta_0 = -270\,{}^\circ\text{C}$ recomputed.
- Uncertainty tasks: $\Delta\theta_0 = (\theta_{0,\text{max}} - \theta_{0,\text{min}})/2$ from the steepest and shallowest lines; 14,14 °C and 20,31 °C recomputed. The new note defining $p_a$, $p_b$ is right.
- Calibration (freezer): $\theta = \theta_1 + (p - p_1)/k$ and $\Delta\theta = \Delta p/k$ correctly rearranged.
- Mean-point task: line through $(\theta_\text{ka}, p_\text{ka})$, $\theta_0 = \theta_\text{ka} - p_\text{ka}/k$; 50 °C and 117,78 kPa.
- Kelvin proportionality: $p/T = p_0/T_0$ → 28,19 kPa at 77,0 K; the condition "gas stays gas" is stated (guardrail).
- Scale offset: $T = \theta + T_0$, $T = 0$ → $\theta_0 = -T_0$.
- Graph tasks: $k = 0{,}275\,\text{kPa}/{}^\circ\text{C}$, $\theta_0 = -272{,}7\,{}^\circ\text{C}$; at 200 K $p = 54{,}9\,\text{kPa}$.
- Numbers, Sijoitus and answers unchanged against the previous PASS. Hash the same at start and end.
