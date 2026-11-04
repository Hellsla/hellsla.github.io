VERDICT: PASS
CONTENT-HASH: 1a94f7b8d17859dd

Full review (scope: a changed line carries a formula). The change of this round: Tiivistelmä now gives the condition of $V = Ex$ (negative plate as zero, $x$ the distance from it), matching the Kaava section.

## Blocking

None.

## Polish

None.

## Checked

- $V = Ex$ with its condition is now stated the same way in Kaava, Tiivistelmä and the sim's calc box; field from higher to lower potential, equipotentials parallel to the plates.
- Definitions: $E_\text{p} = qV$ with signed $q$; $W_{AB} = q(V_A - V_B)$ path-independent; $\tfrac12mv^2 = |q|U$ from rest with only the electric force; potential vs potential energy kept apart (misconception, tarkistus-3); eV defined correctly.
- Sign reasoning: positive charge to lower $V$, electron to higher $V$, both lose $E_\text{p}$; ennuste-2 and virhe/tarkistus-1 have exactly one correct option, distractor feedback right.
- Recomputed: figure $E = 5000\,\text{V/m}$; example $3{,}0\,\text{keV} = 4{,}81\cdot10^{-16}\,\text{J}$, $v = 3{,}25\cdot10^7\,\text{m/s}$ ($10{,}8\,\%$ of $c$, classical KE acceptable); aurora $5\,\text{keV} \to 4{,}2\cdot10^7\,\text{m/s}$ ("noin $40\,000\,\text{km/s}$"); koe-1 $E = 20/10/5\,\text{kV/m}$, $500\,\text{eV}$ at every gap; koe-2 proton $310\,\text{km/s}$, electron $13\,000\,\text{km/s}$, ratio $42{,}9$, alpha $1000\,\text{eV}$; siirto Xe⁺ $42{,}0\,\text{km/s}$, mistakes $1{,}33$, $29{,}7$, $41\,996$; tarkistus-2 $300\,\text{eV}$; exit $-50\,\text{eV}$, $4{,}8\cdot10^{-16}\,\text{J}$. All agree with lesson-answers.py.
- Gravity neglect: $eE/mg \approx 5\cdot10^{10}$ in the figure field ("kymmeniä miljardeja") — right.
- Experiments isolate the varied parameter (koe-1 gap, koe-2 particle at fixed $U$); the sim's calc derives $E_\text{k}$ from force and distance, not from $|q|U$, so the result emerges.
- Photo captions: cloud–ground potential difference of tens to hundreds of MV, negative cloud base, electrons toward higher potential; plasma lamp kV high-frequency AC — correct.
- Hash same at start and end.
