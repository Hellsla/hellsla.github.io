VERDICT: PASS
CONTENT-HASH: ecd7c7f1f550da9a

## Blocking
None.

## Polish
- fy8-s3 b: the model answer now reads the intercept from the line's points $(2{,}0\,\text{cm};\ 1{,}86 \cdot 10^{-2}\,\sqrt{\text{min}})$ and $(20{,}0\,\text{cm};\ 12{,}0 \cdot 10^{-2}\,\sqrt{\text{min}})$, but the figure circles only $(20{,}0;\ 12{,}0)$ and the intercept. Marking $(2{,}0;\ 1{,}86)$ too would make the reading visible (graph_read).
- fy8-s3 d: $r \approx 36\,\text{cm}$ lies outside the measured range $2$–$20\,\text{cm}$. One clause saying the model is extrapolated there would help (guardrail "Fits"; carried over from round 1).
- fy8-s5 d, criteria 3 and 4 overlap: both reward saying that one natural example does not prove the other site safe. Criterion 4 now asks only what the task asks ("Arvioi väitettä"), with the barriers as examples, so it is no longer blocking.

## Checked
- Hash taken at the start and the end: ecd7c7f1f550da9a both times.
- Round-1 blocking items fixed. fy8-s4 a criterion 4 now asks only for the weak interaction. fy8-s5 d criterion 4 now asks for a justified evaluation, so it no longer needs the Onkalo barriers that the task never gave.
- fy8-s3 b new intercept chain: $k = 10{,}14/18 = 0{,}5633 \cdot 10^{-2}\,\sqrt{\text{min}}/\text{cm}$, $r = 2{,}0 - 1{,}86/0{,}5633 = -1{,}30\,\text{cm}$, and $K = 1/k^2 = 3{,}15 \cdot 10^{4}\,\text{cm}^2/\text{min}$, as the solution says. The two points are on the least-squares line (answers.py gives 1,861 and 11,98) and inside the measured range. d-part: $37{,}5 - 1{,}3 = 36{,}2\,\text{cm}$ and $0{,}23\,\mu\text{Sv/h}$.
- One script of my own recomputed every number from the task text, and all agree:
  - s1: $2{,}22$ and $1{,}97\,\text{eV}$, $296\,\text{nm}$, $1193$, $1107\,\text{nm}$, $0{,}83\,\text{eV}$
  - s2: $0{,}006005\,\text{u}$, $5{,}594\,\text{MeV}$, $3{,}52\,\text{kg}$, $83\,\%$, $1791\,\text{W}$, $98{,}5\,\text{W}$, $0{,}16$, $5 \cdot 10^{7}$, $0{,}566\,\text{mSv}$
  - s3: c-part $14\,\%$, $2\,\%$, $6\,\%$
  - s4: $0{,}782\,\text{MeV}$, $7{,}16$, $0{,}8575$, $135\,\text{s}$, $0{,}735$, $270\,\text{s}$
  - s5: $3{,}67\,\%$, $1 : 26$, $3{,}49\,\text{a}$, $4{,}7 \cdot 10^{17}\,\text{J}$, $5{,}8\,\text{t}$, $83\,000$
  - the alternative-method values too ($0{,}56\,\text{mSv}$, $0{,}27\,\mu\text{Sv/h}$, $0{,}038$)
- The reflowed calculation chains carry the same numbers, signs and units in the same order.
- Each part's criteria add up to its points: totals 15, 20, 17, 16 and 16.
- Rubric criteria ask only what the tasks give and ask.
- Models and stated conditions are correct throughout: atomic masses with the electrons cancelling, $A = \lambda N$, constant activity over one year, the effective dose chain, $1/(r+d)^2$, decay of free neutrons only, $Y = 2N_n/(N_n+N_p)$, the moderator feedback.
- Scope stays inside FY8; no de Broglie. Generated data in s3 is declared as such.
- The levels figure is to scale.
