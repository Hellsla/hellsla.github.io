VERDICT: PASS
CONTENT-HASH: 5416b79b37190477

## Blocking
None.

## Polish
- k3-c Sijoitus: $0{,}217 \cdot 15 = 3{,}255$ is written $3{,}25$, and the factor $0{,}0386$ belongs to $3{,}255$ ($e^{-3{,}25} = 0{,}0388$). The result $31$ holds either way.
- k7-d Vastaus: "annos on yksittäisen vuoden luonnon säteilyn kokoluokkaa". $5{,}9\,\text{mSv}$ includes medical dose; "keskimääräisen vuosiannoksen kokoluokkaa" is exact.
- k5-b Vastaus: "absorboi fotoneja vain, kun fotonin energia on vähintään $10{,}2\,\text{eV}$" reads as a threshold; the Periaate says it exactly (the energy of a level pair).

## Checked
Hash was 5416b79b37190477 at the start and the end. Full review; my own script recomputed every number from the task data, and all agree with answers.py and the solutions. The three sentences changed since the last passed version (k3-c $0{,}04 \cdot 800 = 32$; k6-b "$\ln R$ riippuu paksuudesta lineaarisesti", no longer "suoraan verrannollinen"; k7-c wording) are correct.
- **Osa 1.** b: figure points $0{,}37/0{,}78/1{,}20/1{,}61\,\text{V}$, $f_0 = 5{,}60 \cdot 10^{14}\,\text{Hz}$, $W = 3{,}71 \cdot 10^{-19}\,\text{J} = 2{,}32\,\text{eV}$. d $5{,}4$; e $2{,}74\,\text{V}$; g $20\,\text{h}$ (linear $7{,}75$); h $5 \cdot 10^{7}$; i $20$ and $1\,\text{mSv}$. Each of a–j has exactly one correct option; every distractor is wrong and its explanation right (j: d→u by the weak interaction).
- **k2.** $f = 4{,}80$–$6{,}97 \cdot 10^{14}\,\text{Hz}$; least squares $h = 6{,}81 \cdot 10^{-34}\,\text{J s}$, intercept $-0{,}11\,\text{V}$; graph reading $6{,}76$. A slope scan over all five bars gives $h$ from $6{,}18$ to $7{,}37 \cdot 10^{-34}$, so $\Delta h = 0{,}60 \cdot 10^{-34}$; both stated extreme lines stay inside every bar. Model deficits $0{,}02$–$0{,}07\,\text{V}$, as part d says.
- **k3.** Fit $\lambda = 0{,}218\,\text{min}^{-1}$, $T_{1/2} = 3{,}18\,\text{min}$, $N(15) = 30{,}5$; solution $0{,}217$ and $31$. $\sqrt{803}/803 = 3{,}5\,\%$; residuals at most $16$.
- **k4.** $E_\text{s}(\text{He}) = 28{,}30\,\text{MeV}$, $7{,}07$ per nucleon; D $1{,}11$, T $2{,}83$; $Q = 17{,}59\,\text{MeV}$ (also from binding energies); $3{,}37 \cdot 10^{14}\,\text{J/kg}$, ratio $1{,}1 \cdot 10^{7}$.
- **k5.** $656{,}5$ and $121{,}6\,\text{nm}$; $6{,}20 - 3{,}4 = 2{,}8\,\text{eV}$; limit $365\,\text{nm}$.
- **k6.** Net $7{,}9\,\text{s}^{-1}$; $\mu = 0{,}114\,\text{mm}^{-1}$; $d_{1/2} = 6{,}1\,\text{mm}$; $d = 31{,}4\,\text{mm}$; $\sqrt{950}/790 = 3{,}9\,\%$ ($3{,}4$ and $3{,}7\,\%$ for the accepted variant); without background $0{,}110$. Narrow-beam and extrapolation limits are stated.
- **k7.** $0{,}321$; $1540\,\text{MBq}$; $511\,\text{keV}$, $2{,}43\,\text{pm}$; $5{,}32\,\text{mSv}$ ($90\,\%$); C-11 $0{,}0022$ and $2{,}7\,\text{TBq}$.
- **Rubrics and scope.** Criteria ask only what each part gives and asks; point sums match; alternative methods accepted. Example data are marked as such. No de Broglie, no Schrödinger.
