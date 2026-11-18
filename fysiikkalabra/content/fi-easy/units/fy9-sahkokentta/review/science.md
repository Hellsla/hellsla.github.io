VERDICT: PASS
CONTENT-HASH: 894eada2c0c82540
SCOPE: delta: new tasks fy9-sahkokentta-s7 and -s8 and the changed intro; older tasks s1–s6 untouched

## Blocking
None.

## Polish
- s7: as in fi, the plate gap is not given, and the figure does not mark the positive plate. Part d ("Nollataso valitaan nyt positiiviselle levylle") and the a-solution's check (koko levyväli 0,050 m) need the positive plate at $x = 5{,}0\,\text{cm}$. For an S2 reader an explicit sentence "Levyjen etäisyys on $5{,}0\,\text{cm}$." would help most.
- s7 a, Järkevyys: the comparison with the breakdown field of air ("Ilman läpilyöntikenttä on noin 3 MV/m") does not fit, because the plates are in a vacuum. It is an extra, confusing idea for this audience.
- s8 c: the curve gives $U_\text{D}(30\,\text{mA}) \approx 2{,}25\,\text{V}$, so $R_\text{min} \approx 125\,\Omega$. This is inside the tolerance and still rounds up to $130\,\Omega$, and it could be named in Hyväksytään myös.
- `graph_read` base text (a slope from two points) vs single-value readings in s7 c and s8 a/d: the `detail` sets this right.

## Checked
- I ran `units.py hash --lang fi-easy` at the start and the end (894eada2c0c82540, unchanged). The packet's checks say `practice.py check: OK`.
- I read the fi-easy intro, s7 and s8 tasks.json and the solutions' answers, checks, graph readings, mistakes and accepted alternatives, and compared them with fi. Numbers, units, tolerances, points and criteria are identical. Long sentences are split without losing a causal step. For example, b keeps "koska varaus on positiivinen", and d keeps why the speed does not change. "Painovoima on niin pieni, ettei sillä ole merkitystä" is a correct simplification. "Tavallinen laskutapa kelpaa" for the classical limit is acceptable at this level.
- My own recomputation (scratchpad `s78.py`) matches: E = 5,0 kV/m, a = 2,41e11 m/s², v = 98,2 km/s, V = −50 V; I = 17,27 mA, P_R = 65,6 mW, 63,3 %, R_min = 126,7 Ω, 440 Ω and 110 Ω. On the drawn curve, the operating point is I = 17,15 mA and U_D = 2,227 V, inside the tolerance.
- "Sisäenergiaksi" is used (never "lämmöksi"). Field and acceleration directions are right. Rounding is to the safe side in c. The intro's topic list matches the set. Scope is FY6/FY4 only.
