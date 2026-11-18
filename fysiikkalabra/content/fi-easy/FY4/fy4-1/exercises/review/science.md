VERDICT: PASS
CONTENT-HASH: 1500ef8744b0673d
SCOPE: delta Kaava-step rewrite (8g) and paragraph splits; previous PASS bf3a4ac783331157
## Blocking

## Polish
- content/fi-easy/FY4/fy4-1/exercises/solutions.md:195 — "Kaikki pituudet kasvavat samalla luvulla" says the lengths grow by an amount; the correction multiplies them — "Kaikki pituudet kerrotaan samalla luvulla $k$".
- content/fi-easy/FY4/fy4-1/exercises/solutions.md:195 — the Kaava step defines $x_0 = k\,x_{0,\text{ohj}}$, but the substitution computes "Todellinen alkupaikka" without naming the symbol — write "$x_0 = 1{,}25 \cdot 0{,}31\,\text{m} = 0{,}39\,\text{m}$" so the substitution follows the symbolic form.

## Checked
- L2-06 Kaava: $x_\text{A} = x_\text{B}$ → $(v_\text{A} - v_\text{B})\,t = x_{0\text{B}} - x_{0\text{A}}$ → $t$; algebra correct, final form unchanged; $t = 19{,}0/3{,}3 = 5{,}8\,\text{s}$ recomputed.
- L3-04 Kaava: $x = k\,x_\text{ohj}$, $v = k\,v_\text{ohj}$, $x = x_0 + v\,t$ with $x_0 = k\,x_{0,\text{ohj}}$, $t = (x - x_0)/v$; derivation correct and now starts from the basic equation $x = x_0 + v\,t$ of the lesson; $k = 1{,}25$, $v = 0{,}80\,\text{m/s}$, $x_0 = 0{,}39\,\text{m}$, $t = 7{,}0\,\text{s}$ recomputed.
- L3-05 Kaava: $x_{0\text{R}} + v_\text{R}\,t = v_\text{P}\,t - v_\text{P}\,t_0$ → $(v_\text{P} - v_\text{R})\,t = x_{0\text{R}} + v_\text{P}\,t_0$; correct; $t = 331/6{,}1 = 54\,\text{s}$, $x \approx 7{,}4 \cdot 10^2\,\text{m}$ recomputed.
- Every Kaava step now starts from the basic equations and ends in the same symbolic form the substitution uses (lesson rule "start from the basic principle").
- L1 (laskeva suora), L3-04, L3-05 Järkevyys and L1-09 changes are paragraph splits only: words, numbers, signs and units unchanged.
- No number, answer, unit, tolerance, option or figure changed; answers.py not touched by the diff.
- Notation ($x_0$, $v$, $x_{0\text{A}}$, $v_\text{ohj}$) consistent with the brief's lesson.
- Content hash 1500ef8744b0673d at start and end.
