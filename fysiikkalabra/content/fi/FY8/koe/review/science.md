VERDICT: FAIL
CONTENT-HASH: ca214688db6c05ec

## Blocking
1. **A, fy8-k1 h, solutions.md Perustelu (assessment correctness):** "$5 \cdot 10^{9}$ syntyy, kun se luetaan gigaelektronivolteiksi" is false. $200\,\text{GeV} / 4\,\text{eV} = 5 \cdot 10^{10}$, not $5 \cdot 10^{9}$. The other two distractor reasons are right: $50$ (mega dropped) and $5 \cdot 10^{4}$ (read as keV). The keyed option ($5 \cdot 10^{7}$) is correct. Fix one of two ways: change the option to $5 \cdot 10^{10}$ so the GeV reason holds (it stays a single wrong option), or keep $5 \cdot 10^{9}$ and give it a reason that is true.

## Polish
- k2 b, Sijoitus: the slope through $(4{,}0;\ 1{,}59)$ and $(7{,}0;\ 2{,}87)$ is $1{,}28 / 3{,}0 \cdot 10^{14} = 4{,}27 \cdot 10^{-15}\,\text{V}\,\text{s}$, not $4{,}25$ (that is the least-squares value). This gives $h = 6{,}84 \cdot 10^{-34}$, which still rounds to $6{,}8$ and is still about $3\,\%$ above the known value.
- k6 e: the task does not say how long the background was measured. The solution assumes $100\,\text{s}$ ($N_\text{t} = 80$). Say so in the task, or name it as an assumption. No student loses points, because Hyväksytään myös gives full points for $\sqrt{N}$ alone.
- k4 b, Järkevyys: with the rounded values shown, $28{,}30 - 2{,}22 - 8{,}48 = 17{,}60$. Either show $28{,}296 - 2{,}224 - 8{,}482$ or write $\approx 17{,}6$.

## Checked
I recomputed every number independently, in one script, from the task data. Hash at the start and at the end: ca214688db6c05ec.
- **k1, all ten items:** each has exactly one correct option, and each item's Perustelu matches its options.
  - b: $f_0 = 5{,}61 \cdot 10^{14}\,\text{Hz}$, $W = 3{,}7 \cdot 10^{-19}\,\text{J} = 2{,}3\,\text{eV}$. The figure's points ($0{,}37$ to $1{,}61\,\text{V}$) and the line's start at $0{,}24\,\text{V}$ match $h/e$. The eV/J distractors are correct.
  - d: $5{,}4$, with distractors $3{,}0$ and $0{,}6$.
  - e: $2{,}74$, with distractors $3{,}96$ and $1{,}32$.
  - g: $20\,\text{h}$, with the linear distractor $7{,}75\,\text{h}$.
  - i: $20$ and $1\,\text{mSv}$.
  - j: d→u by the weak interaction.
  - a, c, f: their physics and distractor reasons are correct.
- **k2:** frequencies $4{,}80$ to $6{,}97 \cdot 10^{14}\,\text{Hz}$. The least-squares fit gives $h = 6{,}81 \cdot 10^{-34}\,\text{J}\,\text{s}$, with intercept $-0{,}11\,\text{V}$. A brute-force search for the extreme lines through all five error bars gives $h_\text{max} = 7{,}37$, $h_\text{min} = 6{,}18$ and $\Delta h = 0{,}60 \cdot 10^{-34}$, matching the end points named in the solution. The error-source reasoning in d is right.
- **k3:** the fit gives $\lambda = 0{,}218\,\text{min}^{-1}$ and $T_{1/2} = 3{,}18\,\text{min}$. The solution's path ($T = 3{,}2$, $N_0 = 800$) gives $31$; the fit gives $30{,}5$. Both are inside the tolerance. $\sqrt{803}/803 = 3{,}5\,\%$, and the deviations are at most $16$ counts.
- **k4:** $28{,}30\,\text{MeV}$ and $7{,}07\,\text{MeV}$ per nucleon; D and T give $1{,}11$ and $2{,}83\,\text{MeV}$ per nucleon. $Q = 17{,}59\,\text{MeV}$, $3{,}37 \cdot 10^{14}\,\text{J/kg}$, $1{,}1 \cdot 10^{7}$ times coal. The atomic-mass and electron bookkeeping and the Coulomb-barrier explanation are correct.
- **k5:** $656{,}5\,\text{nm}$, $121{,}6\,\text{nm}$, $6{,}20 - 3{,}4 = 2{,}80\,\text{eV}$, ionisation limit $365\,\text{nm}$.
- **k6:** net rates; $\mu = 0{,}1137\,\text{mm}^{-1}$, $d_{1/2} = 6{,}10\,\text{mm}$; the points read from the line, $(0;\ 4{,}78)$ and $(24;\ 2{,}05)$, lie on the fitted line. Shield thickness: $160/9 = 17{,}8\,\mu\text{Sv/h}$, required factor $35{,}6$, $d = 31{,}4\,\text{mm}$. Uncertainty: $3{,}9\,\%$, with the alternatives $3{,}4$ and $3{,}7\,\%$. The no-background slope is $0{,}110$.
- **k7:** $0{,}321$; $1540\,\text{MBq}$; $511\,\text{keV}$ and $2{,}43\,\text{pm}$; $5{,}32\,\text{mSv}$, $90\,\%$ of the yearly average. C-11: $0{,}0022$ left and $2{,}7\,\text{TBq}$ needed. The momentum argument for two photons is correct.
- **Scope and rubrics:** everything is inside the FY8 central contents, and every rubric criterion asks only what its task gives.
