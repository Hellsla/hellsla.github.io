VERDICT: FAIL
CONTENT-HASH: 0907b18528ce64eb

## Blocking

1. **A, fy8-k2 d, Mallivastaus (solutions.md).** It says "Suora leikkaa pystyakselin noin $-0{,}1\,\text{V}$:n kohdalla, eli mitatut kynnysjännitteet ovat kaikilla väreillä noin $0{,}1\,\text{V}$ pienempiä kuin malli $\tfrac{hf}{e}$ ennustaa." This is wrong in number and in reasoning. Computed from the task data, $U_\text{k} - \tfrac{hf}{e}$ is $-0{,}074$, $-0{,}032$, $-0{,}052$, $-0{,}018$ and $-0{,}044\,\text{V}$, so the measured values are only $0{,}02$–$0{,}07\,\text{V}$ below the model. The intercept of $-0{,}11\,\text{V}$ equals the offset from the model only if the fitted slope is $\tfrac{h}{e}$. Here the fitted slope is 3 % steeper, so the "eli" does not follow. This mixes up the shift of the line with a change in its slope, which is the distinction this part asks the student to make. Fix: keep the intercept (about $-0{,}1\,\text{V}$) and change the clause to say the points are $0{,}02$–$0{,}07\,\text{V}$ below $\tfrac{hf}{e}$ (or simply "model $\tfrac{hf}{e}$:n alapuolella", as in the rubric). The rubric detail is correct as written.

## Polish

- fy8-k3 c rubric (reasonableness): "noin viisi puoliintumisaikaa" with "noin $4\,\%$" does not match. Five half-lives gives 3 %, but the solution correctly uses $15 : 3{,}2 \approx 4{,}7$, which gives 3,9 %. Write "noin $4{,}7$".
- fy8-k5 d rubric: criteria 2 and 3 both give a point for "seisova aalto → vain tietyt energiat", so one statement can earn 2 p. The alternative in criterion 3 (uncertainty principle) is something the question does not ask.
- fy8-k4 a rubric detail "massaa ei muunneta kilogrammoiksi" could be read as a penalty on the valid kg route ($\Delta m c^2$ in J, then MeV). Say that both routes are accepted.

## Checked

- I ran `practice.py hash` at the start and at the end: both gave 0907b18528ce64eb.
- One independent script recomputed every number: Osa 1 (b, d, e, g, h with their distractor values), the LSQ line of k2, its read points and $h_\text{max}$/$h_\text{min}$, the k3 exponential fit and the 15 min prediction, $\sqrt{N}$, the k4 binding energies, $Q$, J/kg and the coal ratio, the k5 wavelengths and KE, the k6 net rates, $\mu$, $d_{1/2}$, inverse-square plus attenuation thickness and the difference uncertainty, and the k7 decay factors, 511 keV, 2,43 pm, the dose and the C-11 comparison. All agree with the solutions and answers.py.
- I checked the k2 extreme lines against all five error bars by hand. Both stay inside, and the touching endpoints are named correctly.
- I checked each multiple-choice item: exactly one correct option, the `correct` index matches it, and every distractor's stated origin reproduces its value (eV/J swap, $1/n$, $n^2$, squared ratio, linear decay, prefix errors). The explanations in a, c, f, i and j are physically right: flavour change only through the weak interaction, $\text{d} \to \text{u}$, $H = w_\text{R} D$.
- Scope stays within FY8 central contents. Units, significant figures, point sums, and rubric criteria against tasks are all consistent, apart from the items above.
