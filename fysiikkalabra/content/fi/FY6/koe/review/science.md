VERDICT: PASS
CONTENT-HASH: b1a896e1400b409c

## Blocking
None.

## Polish
- fy6-k3 b Kaava: name $p$ (the percentage error), $n$ (the number of digits) and $r$ (the resolution) in $\Delta U = p \cdot U_R + n \cdot r$.
- fy6-k6 c: the slope is read at the measured point $(400\,\text{m}^{-2};\ 2{,}24\,\text{mN})$. That point lies on the fitted line ($5{,}62 \cdot 10^{-6} \cdot 400 \approx 2{,}25\,\text{mN}$), but a line point near $1000\,\text{m}^{-2}$ would fit graph_read ("kaukana origosta") better.
- fy6-k7 d: "voi vapauttaa sen" (all $10\,\text{kWh}$) still overstates it. "suuren osan siitä nopeasti" would be accurate.

## Checked
- Round 1 blocking item, fy6-k1 b: fixed. The distractor is now described as a meter of very large resistance (almost no current, reads about zero, lamp unchanged) and is ruled out because an ammeter has a small resistance. The internal-resistance sentence now begins "Todellisuudessa", so it no longer clashes with the intro's ideal-source assumption.
- One script recomputed every number from the task data with my own formulas. All agree with answers.py and the solutions, rounding included:
  - k2: $18\,\Omega$; $8{,}9$ and $20\,\Omega$; series point $188{,}6\,\text{mA}$, $2{,}6\,\text{V}$
  - k3: $200\,\Omega$; $13{,}6\,\text{mA}$; $(13{,}5 \pm 0{,}8)\,\text{mA}$; extreme values $12{,}7$ to $14{,}4\,\text{mA}$; $136$ and $74\,\text{mW}$; $40$ and $80\,\%$; the current ranges in d ($\pm 3\,\%$ and $\pm 20\,\%$)
  - k4: $1{,}375 \cdot 10^{6}\,\text{V/m}$; $2{,}2 \cdot 10^{-13}\,\text{N}$; $40{,}2\,\text{km/s}$; $1{,}10 \cdot 10^{19}\,\text{1/s}$; $0{,}207\,\text{kg}$; $1936\,\text{W}$ by both routes
  - k5: $2{,}1\,\text{C}$; $4{,}76$ and $3{,}82\,\text{J}$; $255\,\text{s}$; $3{,}3$ and $7{,}5\,\text{mA}$; $7$ and $16\,\text{mV/s}$; $411$ and $542\,\text{s}$
  - k6: $2{,}24\,\text{mN}$; slope $5{,}62 \cdot 10^{-6}\,\text{N} \cdot \text{m}^2$; $25\,\text{nC}$; $12\,\%$ shortfall; the uncertainty budget in d
  - k7: $51{,}2\,\text{V}$; $10{,}24$, $7{,}58$ and $9{,}22\,\text{kWh}$; $97{,}7\,\text{A}$ and $114\,\text{W}$; $6{,}4\,\text{kA}$ ($4{,}3\,\text{kA}$ with the cable); $391\,\text{A}$, $610$ and $76\,\text{W}$, $14\,\%$
  - the exact solutions of $P = (E - RI)\,I$: $100\,\text{A}$; $467\,\text{A}$, $874$ and $109\,\text{W}$
  - Osa 1 items c, d, e, f and j
- Physics:
  - k1 a–j each have exactly one correct option, and every distractor's feedback is correct;
  - field direction, and why the grid gap does not matter;
  - Newton III;
  - charge redistribution on the conducting spheres;
  - constant-power discharge;
  - series and parallel internal resistance;
  - the safety-voltage limit;
  - "siirtyy lämpönä".
- Every Kaava step starts from a basic equation and is solved symbolically before substitution.
- Scope: charging is treated qualitatively only, and there are no capacitor connections.
- Every rubric sums to its part's points, and other valid methods are accepted. All data is marked `source: example`.
- The hash was the same at the start and the end.
