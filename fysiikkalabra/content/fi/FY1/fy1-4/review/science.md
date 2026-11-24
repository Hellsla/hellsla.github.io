VERDICT: PASS
CONTENT-HASH: 1f755be05cba69e8

## Blocking

## Polish
- lesson.md:336 — the stop question "Jännitettä mitattiin välillä $x = 2\ldots 10$" leaves it unclear whether the voltage is $x$ or $y$, and gives no unit. Fix: "Mittaukset tehtiin välillä $x = 2\ldots 10$", or name both quantities.
- inquiry.json ennuste-2, third option feedback — extrapolating from the first point gives "noin $63\,\text{g}$", but the correct option's feedback and the model answer give $61\,\text{g}$ (best $b$ at $k = 0{,}80$ is $61{,}3\,\text{g}$). Fix: say that a single point gives only about $63\,\text{g}$ because of its own error, or round both values the same way.
- inquiry.json ennuste-2 correct feedback / johtopaatos — "$d \approx 1\,\text{g}$": the minimum is $1{,}23\,\text{g}$ (at $b = 61{,}5$; $1{,}26\,\text{g}$ at $61$). "noin $1\,\text{g}$" is acceptable. $1{,}2\,\text{g}$ would match what the student records.
- inquiry.json koe-1 — the checkbox's best line has a free $b$ ($k = 0{,}48$, $b = 0{,}05\,\text{m}$, $d = 0{,}116\,\text{m}$), while the experiment locks $b = 0$ (best $k = 0{,}49$, $d = 0{,}119\,\text{m}$). A short note that the calculated line is not forced through the origin would avoid confusion.

## Checked
- I recomputed every number in one script with my own formulas. Dataset RMS values: ds1 $b=0$: $k = 0{,}3/0{,}5/0{,}6$ give $d = 0{,}76/0{,}12/0{,}44\,\text{m}$. ds2 with $k = 0{,}8$ and $b = 0$: $d = 61{,}3\,\text{g}$. ds3 with $b = 80$: minimum $d = 5{,}80\,{}^\circ\text{C}$ at $k = -1{,}90$; the initial $d = 17{,}2\,{}^\circ\text{C}$ matches the koe-3 capture.
- Koe-3 residuals with $b = 80$: $+10, -0{,}9, -5{,}7, -6{,}2, -3{,}7, +0{,}9, +7$ (the least-squares line gives the same signs). The "päissä ylös, keskellä alas" pattern is true, so exactly one option is correct.
- Worked example: from $(0;20)$ and $(5{,}0;60)$, $k = 8{,}0\,{}^\circ\text{C/min}$ and $b = 20\,{}^\circ\text{C}$, giving $t = 2{,}5\,\text{min}$ (least squares gives $7{,}85$, $20{,}5$, $2{,}48$). The largest residual is $0{,}8\,{}^\circ\text{C}$. The constant power and small heat losses are stated.
- Numeric tasks: kuvaajasta $15\,\text{km/h}$; siirto $20\,\text{vrk}$; tarkistus-2 $7{,}0\,\text{h}$; exit ticket $k = 1{,}5\,\text{m/s}$, $b = 2{,}0\,\text{m}$. Each mistake value (16,7; 0,067; 25; 16; 8,3; 5,5) matches the error its feedback names.
- Slopes and single-point quotients in the feedback are right: the broken-line slopes (0,2; 0,8; 0,5; 0,3; 0,5) and the $s/t$ values (0,60; 0,40; 0,53).
- The figures are to scale. Scatter: line slope $0{,}50$, three points above and three below. Slope figure: $P_1 = (2;2)$, $P_2 = (8;5)$, $b = 1$. Kettle: line $8t + 20$, 40 °C at 2,5 min. Cyclist: intercept 5 km, $P_1 = (1;20)$, $P_2 = (3;50)$.
- sim.js: the RMS $d$ and the least-squares $k$ and $b$ are correct. `simState` gives `d` at each experiment's initial values, and the slider ranges contain them. The model box states that the data are example data and that the errors are in $y$ only.
- Guardrails: the text says points lie on a line only "yleensä"; it explains outliers before any exclusion; it gives the physical reason the cart's line passes through the origin; it states that extrapolated results are estimates; and it reads the slope from the fitted line, not from raw points.
- Scope: stays inside FY1 (graphical and linear models; $s = vt$ only as an example).
