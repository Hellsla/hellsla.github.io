VERDICT: FAIL
CONTENT-HASH: f5b9b9db4c7f7ede

## Blocking
- sim.js:76-77: TW, TI and the ice mass are interpolated independently, so the animation contradicts the lesson. In the browser, with 0,10 kg/10 °C water and 0,50 kg/−40 °C ice, liquid water (24 g down to 0,3 g) shows "vesi −0,3 … −3,5 °C". With 60 °C water and −10 °C ice, 25 g of ice melts while it reads −7,5 °C. Fix: animate the transferred heat q = u·Q and derive the state in sequence: first the warming or cooling to 0 °C, then the melting or freezing, then the mixture warming or cooling.
- lesson.md:199: "T = 6,05 K ≈ 6,0 K" states a temperature in kelvins. Fix: write `6{,}05\,{}^\circ\text{C} \approx 6{,}0\,{}^\circ\text{C}`.
- lesson.md:205: "lähempänä veden lämpötilaa" is false. 6,0 °C is 14 K from −8 °C and 18 K from 24 °C. Fix: say that melting pulls the result below the midpoint.
- lesson.md:216 (last sentence): "all-melt formula gives T < 0 → ice remains, T = 0 °C" is false when all the water freezes (L3-03: −3,5 °C). Fix: add that exception.

## Polish
- lesson.md:221: the summary bullet "Q_v < Q_j → 0 °C" needs the same exception.
- lesson.md:157: the "esimerkki" dot (20 °C) is the hook case, not the Esimerkki section. Rename it.
- lesson.md fig 2: the −10 °C ice appears only in the aria-label. Add a visible LaTeX label.
- inquiry.json:110: in the freezing cases the pale lämmitys segment is supplied by freezing water, so "sitä lämpöä ei ole" does not hold.
- sim.js:16: the comment says 200 kJ; the axis goes to 250 kJ.

## Checked
- All 12 answers recomputed in one script: they equal answers.py and are within tolerance of exercises.json. Every Vastaus matches its json answer.
- Every inquiry and exit-ticket number checked, with options and feedback.
- koe-1 and koe-2 isolate their varied parameter; simState gives Tf and iceLeftG at those settings.
- Formulas, conditions and all four cases are correct and within FY3 scope.
- Solutions are LaTeX and symbolic first; their sanity checks hold.
- Figures 1–3 are to scale, their labels are LaTeX, and they are print-clean.
- The sim's end states are correct in Chromium for all four outcomes and for the worked example.
- The chart axis covers the slider extremes.
- No lesson ids appear in student text.
