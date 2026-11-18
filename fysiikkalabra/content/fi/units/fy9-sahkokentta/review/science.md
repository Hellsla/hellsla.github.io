VERDICT: PASS
CONTENT-HASH: 261376c3ea53b297
SCOPE: delta: new tasks fy9-sahkokentta-s7 and -s8 and the changed intro; older tasks s1–s6 untouched

## Blocking
None.

## Polish
- s7: neither the text nor the figure says where the positive plate is. Part d and the a-solution's check (250 V : 0,050 m) need it at $x = 5{,}0\,\text{cm}$. A student can only infer this from where the line ends, because the figure has nothing marked. Adding "levyjen etäisyys on $5{,}0\,\text{cm}$" to the text would fix this and reveals nothing.
- s7 a, Järkevyys: the comparison with air's breakdown field does not fit, because the plates are in a vacuum.
- s8 c: the drawn curve gives $U_\text{D}(30\,\text{mA}) \approx 2{,}25\,\text{V}$, so $R_\text{min} \approx 125\,\Omega$. This is inside the tolerance and still rounds up to $130\,\Omega$, and it could be listed in Hyväksytään myös.
- The shared key `graph_read` has a base text about a slope from two points, but s7 c and s8 a/d read single values. The `detail` sets this right.

## Checked
- `units.py hash` at the start and the end: 261376c3ea53b297. The packet's checks say `practice.py check: OK`.
- From the packet I read the intro, s7 and s8 in tasks.json, their solutions and their answers.py blocks. I also read the figure sources: ex_vgraph in fy6-12 figures.py and ex_led with i_led/COMP in fy6-14 figures.py.
- Own script (scratchpad `s78.py`), results:
  - s7: E = 5000 V/m, F = 1,602e-15 N, a = 2,411e11 m/s², Ek = 3,204e-17 J, v = 98,2 km/s, F/mg = 2,5e10, V = −50 V.
  - s8: I = 17,27 mA, P_R = 65,6 mW, 63,3 %, LED 38,0 mW, total 103,6 mW, R_min = 126,7 Ω, 29,2 mA at 130 Ω, 440 Ω and 110 Ω.
  - All agree with answers.py and tasks.json.
- Drawn LED curve: U_D = 2,165 / 2,235 / 2,255 V at 5 / 20 / 30 mA. Solving the curve and resistor together gives I = 17,15 mA, inside the tolerance. With the curve values, R = 433 Ω and 112 Ω, inside 10 %.
- Physics: field direction, force on +2e, energy principle and the sign of ΔV, the zero-level change, and the classical limit. Series circuit with Kirchhoff's voltage law, power share U_R/U, the safe-side rounding, and the non-ohmic conclusion.
- Rubric: points add up (15 + 15), and every criterion matches its part. Unit fields are language-neutral, alt-text names match the task text, and the intro matches the set. Scope is FY6/FY4.
