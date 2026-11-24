VERDICT: PASS
CONTENT-HASH: 4661288f1dcc7a5b
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,typography,wording from e1cbdbd39a48e885 base b5600a6
Delta from the version I passed (e1cbdbd39a48e885): I judged only the diff in the packet. The packet shows the aligned blocks flattened, so I read the Formula steps for their row order.

## Blocking
(none)

## Polish
- exercises.json:304 (fy6-12-L2-09): still open from before. The task text does not say where the positive plate is, and only the alt text states it. Add "the positive plate is at $x = 5.0\,\text{cm}$".

## Checked
- Proton task (L1): the Formula step is $\Delta E_\text{k} + \Delta E_\text{p} = 0$, then $\Delta E_\text{p} = e\Delta V = e(V_2 - V_1)$, then $\Delta E_\text{k} = e(V_1 - V_2)$. The signs are right, and the result fits the unchanged $150\,\text{eV}$.
- $\Delta V = -Es$, then $\Delta E_\text{p} = e\Delta V = -eEs$: the potential falls along the field, which is correct for a proton.
- Electron at point P: $E = U/d$ and $V_P = Ex$ give $E_\text{p} = -eUx/d$. The negative sign for the electron is right.
- Energy tasks (alpha particle, accelerating voltage, the speed ratio in L3-02, the ion mass in L2-07): each now starts from $E_\text{k} = W = qU$ before $\tfrac{1}{2}mv^2 = qU$. The work is the field's, which matches each Principle. Each solves to the same symbolic form as before:
  - $\sqrt{4eU/m}$
  - $mv^2/(2e)$
  - $\sqrt{m_\text{p}/m_\text{e}}$
  - $2eU/v^2$
- Electron from A to B: the step starts from energy conservation $E_{\text{k},A} + E_{\text{p},A} = E_{\text{k},B} + E_{\text{p},B}$ with $E_\text{p} = -eV$, so $E_{\text{k},B} = \tfrac12 mv_A^2 + e(V_B - V_A)$. This is correct.
- Turning point of the proton: $V = Ex = Ux/d$ and $E_{\text{k},0} = eV$ give $x = E_{\text{k},0}d/(eU)$, measured from the negative plate. The asked distance is $d - x$. This is correct.
- L3-04: the derivation chains $v^2 = 2eU_\text{a}/m$, $a = eU_\text{d}/(md)$ and $t = L/v$. That gives $y = \tfrac12 \cdot \tfrac{eU_\text{d}}{md} \cdot \tfrac{mL^2}{2eU_\text{a}} = \tfrac{U_\text{d}L^2}{4dU_\text{a}}$. I checked the algebra and the mass cancels correctly.
- The hunks that only split paragraphs (L1 option tasks, L2-05, L2-06, L2-07, L2-08, L3-04 parts a–c, L3-05) keep every number, sign, unit and causal step, so nothing was lost.
- The changed captions only drop the esimerkkiaineisto marker, which the teacher approved.
- No Substitution, Answer or answers.py value changed, so the recomputations from my earlier reviews still hold.
