VERDICT: FAIL
CONTENT-HASH: f9f00f9009a8df82

## Blocking
- content/fi-easy/FY4/fy4-9/exercises/solutions.md:185 (fy4-9-L3-04 Kaava) — the added sentence "Jäykällä esteellä $I = F_\text{ka}\,\Delta t$, joten $F_\text{ka} = \dfrac{I}{\Delta t}$" uses $\Delta t$ for the stopping time against the rigid obstacle ($0{,}025\,\text{s}$), while the same step ($I = \Delta t \cdot \Sigma F$) and Muunnokset define $\Delta t = 10\,\text{ms}$ as the strip width; substituting the defined $\Delta t$ gives $98\,\text{kN}$, not the $39\,\text{kN}$ Sijoitus c computes, so the last symbolic form does not say what is substituted — give the stopping time its own symbol (e.g. $\Delta t_\text{e}$, named as the stopping time on the rigid obstacle) or rename the strip width; numbers unchanged.

## Polish
- solutions.md:195 (L3-05 Kaava) — full stop missing after "$v_1 = -g\,t_\text{putoaminen}$" before "Nousussa"; also say $v_0 = 0$ at release ("pallo lähtee levosta") so $v_1 = -g\,t$ follows from $v = v_0 + at$.
- solutions.md:174 and 185 (L2-07, L3-04) — $\Sigma F$ here is the sum of the table's interior forces, while L3-05 (line 195) and the lesson use $\Sigma F$ for the total force; a word ("$\Sigma F_i$, mittauspisteiden voimien summa") avoids the clash.
- solutions.md:65, 85, 106, 153 — "joten …, joten …" twice in one sentence; "ja siitä" or "jolloin" reads better.
- solutions.md:55 and 163 — the chain starts with $F\,\Delta t$ and ends with $F_\text{ka}$; writing $F_\text{ka}\,\Delta t$ from the start (as line 65 does) keeps one symbol.

## Checked
- Hash f9f00f9009a8df82 at the start and the end; since 062f457c28^ only the `**Kaava:**` lines of solutions.md changed (no number, answer, tolerance, task or id changed; exercises.json and answers.py untouched).
- answers.py run: every value as before (e.g. L2-02 6,44 kN, L2-04 25,6 m/s, L3-04 50,45 km/h, L3-05 447 N).
- Each rewritten Kaava now opens with $I = \Delta p$, $I = F\,\Delta t$ (or the graph's area) and $p = mv$ and solves for the asked quantity before Sijoitus; signs right (braking $-mv_0$, rebound $v_0 + v_\text{k}$, airbag $-I$).
- L3-01 trapezoid area and L2-07 strip sum correctly placed before the impulse principle.
- L3-05: $v = v_0 + at$ with $a = -g$, $\Sigma F = N_\text{ka} - mg$; derivation consistent with the substitution.
- L3-03: $F = m|v - v_0|/\Delta t$ and $\Delta F = mv_\text{k}/\Delta t$ correct, $F_\text{k}$/$F_\text{s}$ named.
- Notation matches the brief's lesson ($\overline{I} = \Delta\overline{p}$, $F_\text{ka}$).
- Captures: none opened (fi-easy judged from text and the packet).
