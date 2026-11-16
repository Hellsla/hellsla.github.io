VERDICT: PASS
CONTENT-HASH: 3c90a5200b5f471b

## Blocking

## Polish
- exercises.json:fy7-2-L2-04 — the task asks for the weight but does not give g; the solution uses $9{,}81\,\text{m/s}^2$ (house convention, so not blocking) — add "Käytä $g = 9{,}81\,\text{m/s}^2$." if the S2 reader should not have to assume it.
- exercises.json:fy7-2-L2-06 — with $d_\text{A} = 19{,}2\,\text{cm}$ for $24{,}0\,\text{u}$, the example data give 25,1 u and 25,9 u, not 25 and 26 (0,5 % off each way). The solution says this is "lähellä kokonaislukuja", which is fair, but $d_\text{B} = 20{,}0$ and $d_\text{C} = 20{,}8\,\text{cm}$ would give clean values.
- solutions.md:fy7-2-L3-05 — $n = 31{,}9 \approx 32$ crossings is rounded up, so the energy after 32 crossings ($3{,}08 \cdot 10^{-13}\,\text{J}$) slightly exceeds $E_\text{k}$. That is fine for the model, but one clause ("viimeinen ylitys vie protonin ulosvetosäteelle") would say why it rounds up. 16 T = 1,050 µs and 15,96 T = 1,047 µs both fall inside the 3 % tolerance.

## Checked
- One script recomputed all 20 answers from the task text with my own formulas. Every one matches answers.py and exercises.json, and each tolerance covers rounding to the data's figures (L2-09: 3,4 against 3,35 is 1,5 % off, inside 4 %).
- L3-05 correction: with $r = 0{,}200\,\text{m}$ and $U = 60{,}0\,\text{kV}$ I get $v = 1{,}915 \cdot 10^{7}\,\text{m/s}$, $E_\text{k} = 3{,}07 \cdot 10^{-13}\,\text{J} = 1{,}92\,\text{MeV}$, $qU = 9{,}61 \cdot 10^{-15}\,\text{J}$, 31,9 → 32 crossings, 16 revolutions, $T = 65{,}6\,\text{ns}$, $t = 1{,}05\,\mu\text{s}$, $v/c = 0{,}064$ and the relativistic correction $\tfrac34(v/c)^2 = 0{,}31\,\%$. The data and the answer now carry three significant figures consistently, and B is given in teslas.
- Directions: L2-05 (positive charge, v to the right, B into the page: the force is up) and L2-08 ($\overline{v} \times \overline{B}$ points right, so the electron's force is left: option C). $F = 2{,}4 \cdot 10^{-16}\,\text{N}$ and $mg = 8{,}9 \cdot 10^{-30}\,\text{N}$.
- L2-08 options: exactly one is correct. Each wrong figure (along B, as for a positive charge, along v) shows only the error its feedback names. The velocity is drawn as a motion arrow, not as a force.
- L2-09 figure: the point at $1{,}5 \cdot 10^{6}\,\text{m/s}$ is at 15,7 cm (deuteron). The description does not reveal the mass.
- L3-04 fit through the origin: $k = 0{,}1182\,\text{cm}^2/\text{V}$ gives 22,8 u. A free fit gives 22,7 u with a small intercept, and the 22–23 u band covers both. The comparison values for Li and K are right, and so is $r(400\,\text{V}) = 6{,}9\,\text{cm}$ for Na-23.
- L1-08, L2-07 and L3-02: $T = 2\pi m/(qB)$ is derived symbolically, v cancels, and the classical condition is stated in L3-05 c.
- Scope: everything is inside the FY7 slot (F = qvB, the circular path, the velocity selector, the mass spectrometer, the cyclotron as the particle-accelerator theme), with W = qU and E = U/d from FY6.
- The notation follows the brief: $F_\text{m}$, $|q|$, the overline vectors and $d = 2r$.
