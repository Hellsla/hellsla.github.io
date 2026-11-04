VERDICT: PASS
CONTENT-HASH: 9f0133e283d84987

## Blocking

## Polish
- Formula: $\tfrac12 mv^2 = |q|U$ "after travelling through a potential difference $U$" — "in the direction its force pushes it" would make explicit what "starting from rest" already implies.
- Aurora: the $5\,\text{keV}$ speed $4.19 \cdot 10^7\,\text{m/s}$ is 14 % of $c$; the classical value is about 1 % high, which "about $40\,000\,\text{km/s}$" absorbs. C, no change needed.

## Checked
- Full review (changed lines with symbols): $V = Ex$ now carries its condition (negative plate as zero, $x$ measured from it) in the Formula section, the Summary, the sim's calc box and lesson-answers.py; the slope reading $100\,\text{V} : 0.020\,\text{m} = 5000\,\text{V/m}$ matches the figures (4.0 cm, 200 V, 50 V per cm).
- Sign conventions consistent throughout: $E_\text{p} = qV$ with $q = -e$ for the electron, $W_{AB} = q(V_A - V_B)$, each charge moves from rest toward lower $E_\text{p}$; proton $+150\,\text{eV}$, electron $-150\,\text{eV}$ at $150\,\text{V}$; energy bars right.
- Recomputed in one script: worked example $4.806 \cdot 10^{-16}\,\text{J}$, $3.25 \cdot 10^7\,\text{m/s}$ (11 % of $c$); aurora $4.19 \cdot 10^7\,\text{m/s}$; experiments 1–2: $E$ 20 000/10 000/5000 V/m, $E_\text{k}$ 500 eV at every $d$, proton $309\,\text{km/s}$, electron $13\,262\,\text{km/s}$ (ratio 43), alpha 1000 eV; weight/electric ratio $4.9 \cdot 10^{10}$; sim $v_\text{max}$ 6.3 % of $c$; error item $-4.8 \cdot 10^{-17}\,\text{J}$; transfer $42.0\,\text{km/s}$ (mistakes 1.33, 29.7, 41 996); check 2 $300\,\text{eV}$ (mistakes 30 000, $4.8 \cdot 10^{-17}$); exit $-50\,\text{eV}$, $4.8 \cdot 10^{-16}\,\text{J}$. All agree with lesson-answers.py.
- Photo captions: lightning potential differences (10⁷–10⁸ V), negative cloud base with electrons moving to higher potential, plasma ball: correct.
- Every choice has exactly one correct option with right feedback; experiments lock all but the varied parameter; sim model (uniform field, $F = |q|E$, step integration, no use of $|q|U$) matches its boxes.
- Hash at start and end: 9f0133e283d84987.
