VERDICT: PASS
CONTENT-HASH: 12818391684b0010

## Blocking

## Polish
- inquiry.json ennuste-2, third option's feedback — extrapolating the first point with $0{,}80\,\text{g/ml}$ gives "noin $63\,\text{g}$", while the correct option's feedback and Koe 2 give $b \approx 61\,\text{g}$. Both numbers are right for their method, but a student may read them as a contradiction. Fix: add "(yhdestä pisteestä laskettuna; sovitus antaa noin $61\,\text{g}$)".
- sim.js readout and lesson "keskimääräinen poikkeama $d$" — $d$ is the RMS deviation, not the mean absolute deviation. The Laskennan selitys box says so, so this is C. Fix (optional): add "(neliöllinen)" in the box's first sentence.
- lesson.md, second pysahdy — "Jännite mitattiin välillä $x = 2\ldots 10$" gives no unit and does not say that $x$ is the voltage. Fix: "Jännite $x$ mitattiin välillä $2\ldots10\,\text{V}$".

## Checked
- Recomputed everything in one script. Data set 1 with $b=0$: $d(0{,}5)=0{,}122$, $d(0{,}3)=0{,}758$, $d(0{,}6)=0{,}436\,\text{m}$, best $k=0{,}49$. Segment slopes are 0,2/0,8/0,5/0,3/0,5, the one-point values 0,60/0,40/0,53. All agree with the text.
- Data set 2 with $k=0{,}80$: $d(b=0)=61{,}3\,\text{g}$, best $b=61{,}5\,\text{g}$ with $d=1{,}2\,\text{g}$. Data set 3 with $b=80$: best $k=-1{,}90$, $d=5{,}80\,{}^\circ\text{C}$, residuals $+10/-1/-6/-6/-4/+1/+7$. So the "ends above, middle below" option is the only correct one.
- Worked example: $k=8{,}0\,{}^\circ\text{C/min}$, $b=20\,{}^\circ\text{C}$, $t=2{,}5\,\text{min}$ (linear interpolation of the data gives 2,48). Residuals are at most $0{,}8\,{}^\circ\text{C}$. The condition (constant power, small heat losses) is stated, as the guardrail requires.
- Pyöräilijä 15 km/h (mistakes 16,7 and 0,067 right), siirto 20 vrk (25, 16), tarkistus-2 7,0 h (8,3, 5,5), exit ticket $s=1{,}5t+2{,}0$, pysahdy 2,0 m/s: all right.
- Figures to scale, checked from the SVG coordinates. Scatter points are 0,6…2,9 m on $s=0{,}5t$, three above and three below. The kettle points and the 2,5 min / 40 °C lines are right. The slope figure has P₁(2,2), P₂(8,5), $b=1$. On the cyclist graph the line goes through (0; 5), (1; 20), (3; 50).
- sim.js: the least-squares fit, the RMS and the deviation segments implement the stated model. The Mallin oletukset box states the limits (error in $y$ only, example data, data set 3 curved).
- Adapter: the Koe 2 capture shows $k=0{,}80$, $b=0$, $d=61{,}35\,\text{g}$, so the change of data set does not overwrite the initial $k$. Each experiment locks everything except its varied parameter.
- The origin line in ennuste-1 has a physical reason (the cart is released at $s=0$, $t=0$). The fit, outlier and extrapolation statements follow the guardrails ("yleensä", don't remove a point automatically, extrapolation is only an estimate).
- Exactly one option is correct in each choice item. Every distractor's feedback gives the right reason.
- The theory, the summary, the glossary terms, the model answers and the exit ticket agree with one another. Scope stays within FY1 (graphical and linear model).
