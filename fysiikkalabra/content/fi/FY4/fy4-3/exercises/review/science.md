VERDICT: FAIL
CONTENT-HASH: aed639aa12699893
## Blocking
- content/fi/FY4/fy4-3/exercises/solutions.md:295 (L3-05 Kaava) — the rewritten step says "kokonaisvoima on nolla" and then writes $F_\text{ka} = \dfrac{\Sigma F}{n}$, $F_\text{k} = \dfrac{\Sigma F}{n}$, where $\Sigma F$ is the sum of three sensor readings ($10{,}2\,\text{N}$). In the lesson and in every other Kaava step of this set (now "Ensimmäinen laki: $\Sigma F = \dots = 0$") $\Sigma F$ is the net force, which here is zero; read that way the formula gives $F_\text{k} = 0$. $F_\text{ka}$ is also not named. — Write the mean with its own symbols, e.g. "köyden voima on lukemien keskiarvo $F_\text{ka} = \dfrac{F_1 + F_2 + F_3}{3}$; ensimmäinen laki: $\Sigma F = F_\text{ka} - F_\text{k} = 0$, joten $F_\text{k} = \dfrac{F_1 + F_2 + F_3}{3}$", and in Sijoitus "Lukemien summa on $10{,}2\,\text{N}$".

## Polish
- solutions.md (all "Ensimmäinen laki: $\Sigma F = \dots$" rows) — the lesson's worked example writes the component $\Sigma F_x$; a direction subscript ($\Sigma F_y$ for the vertical cases L1-01, L2-01, L2-03, L2-04, L3-01, L3-02, L3-03; $\Sigma F_x$ for the horizontal ones) would match the lesson and the vector form $\Sigma\overline{F} = \overline{0}$.

## Checked
- Delta: Kaava steps of L1-01, L1-02, L1-04, L2-01…L2-05, L3-01…L3-05 now open from the first law; paragraph splits in L3-03 Periaate, L2-07 and L2-08 Mallivastaus. No answer, tolerance, task or id changed.
- Each first-law sum has the right forces and signs for the force diagram given in the solution; each result is solved symbolically before substitution and unchanged: $18\,\text{N}$, $850\,\text{N}$, $240\,\text{N}$, $13\,\text{N}$, $65\,\text{N}$, $833{,}85\,\text{N}$, $8939{,}2\,\text{N}$, $0{,}27\,\text{kN}$, $0{,}60\,\text{N}$, $1{,}9\,\text{N}$, $4{,}8\,\text{N}$, $450/480\,\text{N}$, $3{,}40\,\text{N}$ (recomputed).
- L2-04: the load's weight now has its own symbol $G_\text{m} = mg$ before substitution: right.
- L3-04: first law for cart and horse separately, third-law pair used between them: right.
- Paragraph splits change no wording; L2-08 still names the third-law pair and why they do not cancel.
- Capture opened: review/shots/fy4-3-open-exercises-L3-1280-7.png (L3-05 Kaava as rendered: the $\Sigma F/n$ collision is visible right after "kokonaisvoima on nolla").
- Hash aed639aa12699893 at start and end.
