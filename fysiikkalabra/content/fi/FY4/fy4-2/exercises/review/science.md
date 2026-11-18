VERDICT: PASS
CONTENT-HASH: f9d814df52959b10
## Blocking

## Polish
- content/fi/FY4/fy4-2/exercises/solutions.md (L2-03 Sijoitus) — the row still computes $t \approx 1{,}529\,\text{s}$, which the new symbolic $h = \dfrac{v_0^2}{2g}$ no longer needs; it is used only in Järkevyys. Could move to Järkevyys or say why it is kept (presentation only).

## Checked
- Delta only: Kaava steps rewritten in L2-03, L3-02, L3-03, L1-07, L2-06, L3-04; paragraph splits in L2-07 Mallivastaus and L2-08 Periaate; exercises.json caption marker and reflow only. No answer, tolerance, task or id changed.
- L2-03: from $v = v_0 - gt$ and $y = y_0 + v_0t - \tfrac12 gt^2$, $v = 0 \Rightarrow t = v_0/g$, $h = v_0^2/g - v_0^2/(2g) = v_0^2/(2g)$: right. New substitution $225/19{,}62 \approx 11{,}47\,\text{m}$ gives the same $11{,}5\,\text{m}$ (recomputed).
- L3-02: area of triangle + rectangle + triangle; $s = 1162{,}5\,\text{m}$ unchanged (recomputed).
- L3-03: $y = y_0 + v_0t + \tfrac12 at^2$ compared with $At^2 + Bt + C$ gives $v_0 = B$, $a = 2A$, $v = B + 2At$; $v = -1{,}76\,\text{m/s}$ (recomputed).
- L1-07: rectangle $v_1t$ plus triangle $\tfrac12(v_2-v_1)t$ = trapezoid; $22{,}5\,\text{m}$ unchanged.
- L2-06: from rest $x = \tfrac12 at^2 = kt^2$, so $a = 2k$: right; consistent with the lesson's $a = 2A$.
- L3-04: $v_1\Delta t + \tfrac12(v_2-v_1)\Delta t = \tfrac{v_1+v_2}{2}\Delta t$: right; the stated per-interval assumption (linear within each interval) is in Periaate.
- Each Kaava now opens from the basic equations of the lesson ($v = v_0 + at$, $x = x_0 + v_0t + \tfrac12 at^2$, area under $(t,v)$) and ends in the symbolic form substituted into. Notation as in the brief.
- Capture opened: review/shots/fy4-2-open-exercises-L2-1280-3.png (L2-03 Kaava renders as an aligned derivation).
- Hash f9d814df52959b10 at start and end.
