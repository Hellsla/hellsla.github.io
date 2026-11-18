VERDICT: PASS
CONTENT-HASH: 261376c3ea53b297
SCOPE: delta: new tasks fy9-sahkokentta-s7 and -s8 and the changed intro; older tasks s1–s6 untouched

## Blocking
None.

## Polish
- s7: nothing in the text or the figure says where the positive plate is. Part d and the a-solution's check ("koko levyvälillä 250 V : 0,050 m") need it at $x = 5{,}0\,\text{cm}$, $V = 250\,\text{V}$. A student can only infer it from where the line ends (the axis runs to 5,5 cm, and the figure catalog notes "nothing marked"). A clause such as "levyjen etäisyys on $5{,}0\,\text{cm}$" in the text would remove the guess, and it reveals nothing.
- s7 a, Järkevyys: the comparison with the breakdown field of air (3 MV/m) does not fit, because the plates are in a vacuum. Drop it, or say "jos välissä olisi ilmaa".
- s8 c: on the curve, $U_\text{D}(30\,\text{mA}) \approx 2{,}25\,\text{V}$ (the alt-text also says "hieman 2,2 voltin oikealle puolelle"). That gives $R_\text{min} \approx 125\,\Omega$, which is inside the tolerance and still rounds up to $130\,\Omega$. The solution's "lähes pystysuora kohdassa 2,2 V" is a fair reading, but a line in Hyväksytään myös would cover students who read 2,25 V.
- s7 c and s8 a/d use the shared key `graph_read`, whose base text says "kulmakerroin … kahdesta kaukana toisistaan olevasta suoran pisteestä". These parts read single values. The `detail` sets this right, but the key's base text does not match what is asked.

## Checked
- I re-ran `units.py hash` at the start and the end (fi 261376c3ea53b297, unchanged). The packet's checks say `practice.py check: OK`.
- From the packet I read the intro, s7 and s8 in tasks.json, their solutions.md sections and their answers.py blocks. I also read the figure sources `lessons/FY6/fy6-12/figures.py` (ex_vgraph) and `lessons/FY6/fy6-14/figures.py` (ex_led, i_led/u_led, COMP).
- My own script (scratchpad `s78.py`) recomputed every number. s7: E = 5000 V/m, F = 1,602e-15 N, a = 2,411e11 m/s², Ek = 3,204e-17 J, v = 98,2 km/s, W = Fs check, F/mg = 2,46e10, d = −50 V. s8: I = 17,27 mA, P_R = 65,6 mW, share 63,3 %, LED 38,0 mW, total 103,6 mW, R_min = 126,7 Ω, 3,8 V/130 Ω = 29,2 mA, R = 440 / 110 Ω. All agree with answers.py and tasks.json.
- I checked s8 against the drawn LED curve: U_D = 2,165 / 2,200 / 2,235 / 2,255 V at 5 / 10 / 20 / 30 mA. Solving the curve and resistor together gives I = 17,15 mA and U_D = 2,227 V, inside the 6 % tolerance. With the curve values, R5 = 433 Ω and R20 = 112 Ω, inside 10 %, which matches the Hyväksytään myös line (2,17 V and 2,23 V).
- Physics checked in s7: field direction, force on +2e, energy principle, sign of ΔV, invariance under a change of zero level, and the classical limit (v/c ≈ 0,03 %). In s8: series current, Kirchhoff's voltage law, power share = U_R/U, R_min rounded to the safe side, and the non-ohmic conclusion.
- Rubric points add up (s7 4+4+4+3, s8 4+4+3+4), and every criterion asks only what its part asks. Units are language-neutral, significant figures follow the data, and the alt-text names (V, x, I, U_D) match the task text. The intro's topic list matches s7 and s8. Scope is FY6/FY4 only.
