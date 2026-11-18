VERDICT: PASS
CONTENT-HASH: 2e5d53eab6b173d8
## Blocking

## Polish
- content/fi/FY4/fy4-1/exercises/solutions.md (L3-04 Kaava) — the Kaava step is now long prose with three inline equations; the final form $t = \dfrac{x - x_0}{v}$ sits at the end of a sentence. Acceptable; a display row for $t$ would read more easily (presentation only).

## Checked
- Delta only: L2-09, L3-04 and L3-05 Kaava steps rewritten; paragraph splits in L1-06 Mallivastaus, L3-04 and L3-05 Järkevyys and L1-09; caption marker removed from exercises.json. No number, answer, tolerance, task or id changed in the diff.
- L2-09: $x_{0\text{A}} + v_\text{A}t = x_{0\text{B}} + v_\text{B}t \Rightarrow (v_\text{A}-v_\text{B})t = x_{0\text{B}}-x_{0\text{A}}$, gives the same $t$ formula as before; algebra right.
- L3-04: $x = k\,x_\text{ohj}$, $x_\text{ohj} = x_{0,\text{ohj}} + v_\text{ohj}t$, so $x = x_0 + vt$ with $x_0 = k\,x_{0,\text{ohj}}$, $t = (x-x_0)/v$: right; matches the substitution row ($0{,}39\,\text{m}$, $0{,}80\,\text{m/s}$, $7{,}0\,\text{s}$).
- L3-05: $x_{0\text{R}} + v_\text{R}t = v_\text{P}t - v_\text{P}t_0 \Rightarrow x_{0\text{R}} + v_\text{P}t_0 = (v_\text{P}-v_\text{R})t$: right; same final formula as the substitution.
- Recomputed: L2-09 $t = 16/4 = 4{,}0\,\text{s}$; L3-04 $k = 1{,}25$, $t = (6{,}0 - 0{,}39)/0{,}80 \approx 7{,}0\,\text{s}$; L3-05 $t = 331/6{,}1 \approx 54\,\text{s}$, $x \approx 7{,}4\cdot10^2\,\text{m}$. All unchanged and consistent.
- Each derivation starts from the basic equations (tasainen liike $x = x_0 + vt$, the meeting condition), simplifies symbolically to the end and substitutes into the last form, as the 8g rule asks.
- Paragraph splits change no wording or physics; the Järkevyys checks remain real checks.
- Notation as in the brief ($x_0$, $v$, $\Delta x$, subscripts A/B/R/P).
- Capture opened: review/shots/fy4-1-open-exercises-L3-1280-5.png (L3-04 Kaava renders as derived, aligned).
- Hash 2e5d53eab6b173d8 at start and end.
