VERDICT: PASS
CONTENT-HASH: 46ac8e1c30d0df71

## Blocking

## Polish
- solutions.md fy8-k6 (Kaava for $d_{1/2}$) — the row $\tfrac{R_0}{2} = R_0 e^{-\mu d_{1/2}}$ jumps straight to $d_{1/2} = \ln 2/\mu$. This is correct. Optionally add $\ln 2 = \mu d_{1/2}$ as in k3.

## Checked
- The hash was 46ac8e1c30d0df71 at the start and the end.
- The previous science PASS was for 74a741769156fbc5 (commit 0e62ee5a0d). Since then only solutions.md changed among the judged files: tasks.json and answers.py are unchanged.
- A script removed the Kaava steps, collapsed whitespace and compared the rest: it is identical. The other edits are paragraph splits in Perustelu and Mallivastaus texts.
- k2 b) and c): $eU_\text{k} = hf$ gives $U_\text{k} = \tfrac{h}{e}f$, so slope $= h/e$ and $h = e\,\Delta U_\text{k}/\Delta f$. Each extreme line gives its $h$, and $\Delta h = (h_\text{max} - h_\text{min})/2$. Recomputed: $h = 6{,}81 \cdot 10^{-34}\,\text{J}\,\text{s}$, which matches answers.py.
- k3: $N_0/2 = N_0 e^{-\lambda T_{1/2}}$ gives $\lambda = \ln 2/T_{1/2}$. The derivation is correct.
- k4 a)–c): $\Delta m$, $E_\text{s} = \Delta m c^2$, $E_\text{s}/A$; $Q = \Delta m c^2$; $E/m = Q/(m_\text{D} + m_\text{T})$. Recomputed: $28{,}30\,\text{MeV}$ ($7{,}07$ per nucleon), $Q = 17{,}59\,\text{MeV}$ and $3{,}37 \cdot 10^{14}\,\text{J/kg}$.
- k5 a)–c): $E = hf$ and $c = f\lambda$ give $\lambda = hc/E$. The ionisation balance from $n = 2$ is $E_\text{fotoni} = \lvert E_2\rvert + E_\text{k}$, which is right. Recomputed: $656{,}5\,\text{nm}$, $121{,}6\,\text{nm}$ and $2{,}80\,\text{eV}$.
- k6 c)–e):
  - The linearisation $\ln R = \ln R_0 - \mu d$ is correct.
  - The inverse-square factor at $r = 3r_0$ is $1/9$, combined with the attenuation, giving $d = \tfrac{1}{\mu}\ln\tfrac{\dot H_0/9}{\dot H}$. Recomputed: $31{,}4\,\text{mm}$.
  - The Poisson net-count uncertainty $\sqrt{N + N_\text{t}}$ is now derived from the two counts' $\sqrt{N}$ added in quadrature. Recomputed: $3{,}9\,\%$.
- k7: annihilation at rest, $2E = 2m_\text{e}c^2$, then $\lambda = hc/E$. Recomputed: $2{,}43\,\text{pm}$ and $0{,}321$ of the F-18 left after $3\,\text{h}$.
- Every new Kaava step starts from the basic law and ends in the form substituted. No points, rubric or answer changed.
