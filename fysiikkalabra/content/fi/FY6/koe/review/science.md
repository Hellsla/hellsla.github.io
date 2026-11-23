VERDICT: FAIL
CONTENT-HASH: acf43efe11978945

## Blocking
1. **A, fy6-k1 b, solutions.md.** The feedback on the distractor "Mittari näyttää nollaa, eikä lampun kirkkaus muutu" says that it "kuvaa rinnalle kytkettyä jännitemittaria". A voltmeter across the lamp shows the lamp's voltage, not zero. Say instead that the option would fit a meter of very large resistance: almost no current passes through it, so it would read about zero and leave the lamp unchanged.

## Polish
- fy6-k1 b: the solution limits the current by the battery's internal resistance, but the intro calls internal resistance negligible. Add "todellisuudessa".
- fy6-k3 b Kaava: name $p$, $n$ and $r$.
- fy6-k6 c: the slope is read from a measured point near the origin. A point on the line near $1000\,\text{m}^{-2}$ would follow graph_read better.
- fy6-k7 d: "vapauttaa sen" (the whole $10\,\text{kWh}$) overstates it. Write "suuren osan siitä nopeasti".

## Checked
- One script recomputed every number from the task data. All agree with answers.py and the solutions, rounding included:
  - k1 c, d, e, f, j
  - k2: $18{,}0\,\Omega$; $8{,}9$ and $20\,\Omega$; $189\,\text{mA}$ and $2{,}6\,\text{V}$
  - k3: $200\,\Omega$; $13{,}6\,\text{mA}$; $(13{,}5 \pm 0{,}8)\,\text{mA}$; $136$ and $74\,\text{mW}$; $40$ and $80\,\%$; the current ranges in d
  - k4: $1{,}38 \cdot 10^{6}\,\text{V/m}$; $2{,}2 \cdot 10^{-13}\,\text{N}$; $40\,\text{km/s}$; $1{,}1 \cdot 10^{19}\,\text{1/s}$; $0{,}21\,\text{kg}$; $1936\,\text{W}$
  - k5: $2{,}1\,\text{C}$; $4{,}76$ and $3{,}82\,\text{J}$; $255\,\text{s}$; $3{,}3$ and $7{,}5\,\text{mA}$; $411$ and $542\,\text{s}$
  - k6: $25\,\text{nC}$; $12\,\%$ shortfall
  - k7: $51{,}2\,\text{V}$; $10{,}24$, $7{,}58$ and $9{,}22\,\text{kWh}$; $97{,}7\,\text{A}$ and $114\,\text{W}$; $6{,}4\,\text{kA}$; $391\,\text{A}$, $610$ and $76\,\text{W}$
- Every Kaava step starts from a basic equation (the Kirchhoff loop, $W = eU$, $\eta$, $W_1 - W_2$) and solves it symbolically before substitution.
- The physics is sound:
  - field direction and why the grid gap does not matter;
  - Newton III in Coulomb's law;
  - charge redistribution on conducting spheres;
  - series and parallel internal resistance;
  - suojajänniteraja;
  - "siirtyy lämpönä".
- Scope: charging is qualitative only, with no capacitor connections.
- Figures:
  - k1 d topology matches the solution;
  - the LEDs are forward-biased;
  - the battery line is right;
  - charging graph C is right;
  - the model graphs are to scale.
- Each Osa 1 item has exactly one correct option. Every rubric sums to its part's points, and other valid methods are accepted.
- All data is marked `source: example`.
- The hash was unchanged at the start and the end.
