VERDICT: FAIL
CONTENT-HASH: fcb044feb02ea296

## Blocking
1. **(A) fy8-k1 d, Perustelu.** The text says the distractor $2{,}0$ comes from energies proportional to $n$. That model gives $1$ ($E \propto 1/n$ gives $3$). No simple model gives $2{,}0$. Give the distractor a real origin, or change it and its feedback to match one (for example $3{,}0$ from $1/n$).
2. **(A) fy8-k2 c, solution and rubric.** The task asks for the steepest and the shallowest lines that stay inside the error bars. The solution draws them through the two end bars only. Its steep line, $(4{,}80;\,1{,}86) \to (6{,}97;\,2{,}89)$, gives $1{,}995\,\text{V}$ at $5{,}08 \cdot 10^{14}\,\text{Hz}$, below that bar's $2{,}02$–$2{,}12\,\text{V}$. Its shallow line gives $2{,}564\,\text{V}$ at $6{,}38 \cdot 10^{14}\,\text{Hz}$, below that bar's $2{,}57\,\text{V}$. A search over lines through all five bars gives $h_\text{max} \approx 7{,}4$, $h_\text{min} \approx 6{,}2$ and $\Delta h \approx 0{,}6 \cdot 10^{-34}\,\text{J}\,\text{s}$. The solution and rubric give $7{,}6$, $6{,}1$ and $0{,}7$. Either recompute the lines, values and answer, or reword the task to use the end-point bars only. The conclusion (the known value is inside the range) still holds.
3. **(A) fy8-k2 d, model answer and rubric.** The fitted line meets the $U$ axis at about $-0{,}11\,\text{V}$, so the points sit below $hf/e$. Needing a slightly higher voltage before the eye sees light moves the points up, not down. So it is not "saman suuntainen virhe". The eye's sensitivity also changes with colour, so this error need not keep the slope. Correct the sentence, and in the rubric credit the eye-threshold source only when its direction is stated correctly.

## Polish
- fy8-k1 e: the squared-ratio error gives $3{,}96\,\text{V}$. The option should read $4{,}0\,\text{V}$, not $3{,}9\,\text{V}$.
- fy8-k1 g: the solution does not show how "linear" reasoning gives $12{,}8\,\text{h}$. In h, dropping the MeV prefix gives $50$, which is not one of the options, so that sentence explains nothing.
- fy8-k1 b: the figure's alt text says the line ends near $0{,}4\,\text{V}$. It ends at $0{,}24\,\text{V}$ (at $6{,}2 \cdot 10^{14}\,\text{Hz}$).
- fy8-k5 a: the solution writes $6{,}57 \cdot 10^{-7}\,\text{m}$, but the value is $6{,}565 \cdot 10^{-7}\,\text{m}$, which the same line then gives as $656\,\text{nm}$.
- fy8-k5 d: "aallonpituus sopii tilaan" uses the electron's wavelength, and the scope note says the de Broglie wavelength is not taught. Say "vain tietyt seisovat aallot mahtuvat atomiin".
- fy8-k4 d: at $10^{8}\,\text{K}$, $kT \approx 9\,\text{keV}$, far below the Coulomb barrier ($\sim 0{,}4\,\text{MeV}$). The explanation "close enough by kinetic energy" is a fair simplification (C), but fusion actually needs tunnelling. Consider crediting it if a student mentions it.
- fy8-k7 e rubric: `\\\\,\\\\text{TBq}` and `\\\\approx` are double-escaped and will render wrong.
- fy8-k6 e Järkevyys: "pidempi mittausaika neljänkertaistaisi" should read "nelinkertainen mittausaika".

## Checked
- I recomputed every number in one script: k1 b, d, e, g, h and i; k2 frequencies, least-squares fit, read points, intercept and the extreme lines; k3 λ, $N(15)$ and $\sqrt N$; k4 binding energies, Q and J/kg; k5 a–c; k6 net rates, μ, $d_{1/2}$, $d$ and the uncertainty; k7 a–e. All match answers.py, apart from the items above.
- Each choice item has exactly one correct option, and the physics of a, c, f, i and j is right.
- k6 combines the inverse-square law with exponential shielding correctly. It uses the public dose limit of $1\,\text{mSv}$, and its assumptions (narrow beam, extrapolation) are stated.
- In k7 the annihilation momentum argument and $m_\text{e}c^2$ are correct.
- The exam stays within the FY8 central contents.
- Section points add up: 20 + 2·15 + 20 = 70.
- The content hash was the same at the start and the end.
