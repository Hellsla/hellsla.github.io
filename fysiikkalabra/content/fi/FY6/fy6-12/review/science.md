VERDICT: PASS
CONTENT-HASH: 58b94744514c92ce

## Blocking

## Polish
- lesson.md Tiivistelmä (4th item) — "Levosta lähtenyt hiukkanen saa liike-energian $\tfrac{1}{2}mv^2 = |q|U$" leaves out the condition "kun vain sähköinen voima tekee työtä", which the Kaava section and the worked example state; C at this level, optionally add the four words.
- sim.js bars() comment says "E_p green" while the bar is drawn in ink (INKC), as the howto says ("tummia"); comment only, no change needed for the student.

## Checked
- Proofreading fixes: the formula block names $V = E_\text{p} : q$ "sähkökentän potentiaali" with $E_\text{p} = qV$ as its other form, matching the lead sentence and the Tiivistelmä; section name names the right laws. The Dallas caption now says the energy becomes light, sound and air's internal energy "joka siirtyy lämpönä ympäristöön" — correct heat/internal-energy wording per the guardrails.
- One script, own formulas: koe-1 $E$ = 20 000 / 10 000 / 5000 V/m, $t$ = 161,6 / 323,2 / 646,3 ns, $E_\text{k}$ = 500 eV each; koe-2 500 / 500 / 1000 eV, 309 / 13 262 / 220 km/s, ratio 42,9 ("noin 43").
- Worked example: $E_\text{k} = 4{,}806 \cdot 10^{-16}\,\text{J}$, $v = 3{,}248 \cdot 10^{7}\,\text{m/s}$ = 0,108 c; symbolic first, rounding to two figures from 3,0 kV, classical KE justified.
- Revontulet: 5 keV → 41 900 km/s ("noin 40 000"); auroral potential drop and altitudes, green from oxygen, are right.
- siirto 42,0 km/s, mistakes 1,33 / 29,7 / 41 996 recomputed; Xe/e mass ratio 2,4·10⁵; "ten times rocket exhaust" plausible.
- tarkistus-2 300 eV (mistakes 30 000 eV and 4,8·10⁻¹⁷ J), Etsi virhe sign of $q = -e$, exit ticket −50 eV and 4,8·10⁻¹⁶ J; every distractor wrong with right feedback; exactly one correct option in each choice.
- Weight vs electric force: 4,9·10¹⁰ in the figure's 5000 V/m, ≥ 4,9·10⁹ in the sim (alpha, 100 V over 10 cm); sim speeds ≤ 6,3 % of c ("alle 7 %").
- Figures: equipotential lines 50 V per 1,0 cm evenly spaced; vx-graph line through origin to (4,0 cm; 200 V), triangle 1→3 cm, 50→150 V gives 5000 V/m; energy bars for proton and electron (Ep 200→0, 0→−200 eV) right.
- sim.js integrates constant acceleration exactly with an exact arrival step, Ek from ½mv² (not from |q|U), Ep = qV with V = Ex from the negative plate; simState gives E, tns, EkeV, EpeV, vkms; koe-1 locks U and particle, koe-2 locks U and d, so each isolates its varied parameter.
- Concept physics: conservative force, free zero level, field from high to low potential, electron towards higher potential with falling $E_\text{p}$, lightning with a negative cloud base — consistent with glossary and earlier chapters.
