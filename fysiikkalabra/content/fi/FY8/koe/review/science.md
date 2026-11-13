VERDICT: PASS
CONTENT-HASH: 8595169e14d96ba2

## Blocking
None.

## Polish
- k7-d Vastaus: "annos on yksittäisen vuoden luonnon säteilyn kokoluokkaa". $5{,}9\,\text{mSv}$ includes medical dose; "keskimääräisen vuosiannoksen kokoluokkaa" is exact.
- k2 Hyväksytään myös d: the protective resistor's voltage drop is accepted as an error source. It is weak, since the current is near zero at threshold; the direction condition guards it.
- k3-d rubric "enintään noin $10$–$20$ pulssia eli $\sqrt{N}$:n suuruisia". True (largest residual $16$), but "samaa kokoluokkaa kuin $\sqrt{N}$" is cleaner.

## Checked
Hash was 8595169e14d96ba2 at the start and the end. My own script recomputed every number; all agree with answers.py and the solutions:
- **Osa 1.**
  - b: the figure's points are $0{,}37/0{,}78/1{,}20/1{,}61\,\text{V}$, so slope·e $= 6{,}62 \cdot 10^{-34}$. Extrapolated $f_0 = 5{,}60 \cdot 10^{14}\,\text{Hz}$ and $W = 3{,}71 \cdot 10^{-19}\,\text{J}$, which is option B. Figure description matches figures.py.
  - The other items: d $5{,}4$, e $2{,}74/3{,}96/1{,}32\,\text{V}$, g $20\,\text{h}$ (linear $7{,}75$), h $5 \cdot 10^7$, i $20/1\,\text{mSv}$.
  - a, c, f and j each have exactly one correct option; every distractor explanation is right. j: d→u by the weak interaction, plus the W boson.
- **k2.** f is $4{,}80$–$6{,}97 \cdot 10^{14}\,\text{Hz}$. The graph reading gives $h = 6{,}76 \cdot 10^{-34}$; LSQ gives $6{,}81 \cdot 10^{-34}$, intercept $-0{,}11\,\text{V}$, f-intercept $0{,}26$ (as in the figure description). I checked the extreme slopes independently by a slope scan over all five bars: $h$ from $6{,}18$ to $7{,}37 \cdot 10^{-34}$, so $\Delta h = 0{,}60 \cdot 10^{-34}$. The model deficits are $0{,}02$–$0{,}07\,\text{V}$, as part d says.
- **k3.** $\lambda = 0{,}217\,\text{min}^{-1}$ and $N(15) \approx 31$; the fit gives $3{,}18\,\text{min}$ and $30{,}5$. $\sqrt{803}/803 = 3{,}5\,\%$. The figure's half-life guide is at $3{,}2\,\text{min}$ and $400$.
- **k4.** BE(He) $28{,}30\,\text{MeV}$ ($7{,}07$ per nucleon); D $1{,}11$, T $2{,}83$; $Q = 17{,}59\,\text{MeV}$ (cross-checked from binding energies); $3{,}37 \cdot 10^{14}\,\text{J/kg}$, ratio $1{,}1 \cdot 10^7$.
- **k5.** $656{,}5$ and $121{,}6\,\text{nm}$; $E_\text{k} = 2{,}80\,\text{eV}$; ionisation limit $365\,\text{nm}$.
- **k6.** Net $7{,}9\,\text{s}^{-1}$; $\mu = 0{,}114\,\text{mm}^{-1}$; $d_{1/2} = 6{,}1\,\text{mm}$; $d = 31{,}4\,\text{mm}$; $\sqrt{950}/790 = 3{,}9\,\%$. Background, inverse-square and narrow-beam/extrapolation limits are stated. The figure's points $(0;\ 4{,}78)$ and $(24;\ 2{,}05)$ lie on the fit.
- **k7.** $0{,}321$; $1540\,\text{MBq}$; $511\,\text{keV}$ and $2{,}43\,\text{pm}$; $5{,}32\,\text{mSv}$ ($90\,\%$); C-11 $0{,}0022$ and $2{,}7\,\text{TBq}$.
- **Rubrics.** Every criterion asks only what its part gives and asks, and the point sums match. Scope stays within FY8: no de Broglie, no Schrödinger.
