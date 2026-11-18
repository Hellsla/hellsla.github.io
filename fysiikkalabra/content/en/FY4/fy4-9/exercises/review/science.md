VERDICT: PASS
CONTENT-HASH: e42850bb00939229

## Blocking

## Polish
- solutions.md:120 (L3-03) — "$F\,\Delta t = m\,|v - v_0|$" puts a signed force against a magnitude — write "$|F|\,\Delta t = m\,|v - v_0|$" or "the magnitude of the force is".
- solutions.md:108 (L3-02) — "$F\,\Delta t = mv_0 - 0$" has the sign of $\Delta p = 0 - mv_0$ turned without saying so (pre-existing, not new) — add "in magnitude" as in L2-01 and L2-06.

## Checked
- Hash e42850bb00939229 at start and end; only solutions.md changed, no number, answer, tolerance, task or id changed.
- Captures: none opened; judged from the text and the packet's diff.
- L2-01, L2-02, L2-04, L3-02, L2-05, L2-06: the Kaava step now starts from $I = \Delta p$, $I = F\,\Delta t$, $p = mv$ and solves symbolically; each derived formula follows.
- L3-01, L2-07, L3-04: impulse as area first, then $I = \Delta p$; L3-04 adds $F_\text{avg} = I/\Delta t$ for part c, consistent with the substitution.
- L3-03: $\Delta F = F_\text{r} - F_\text{c}$ with symbols named; $m(v_0 + v_\text{r})/\Delta t - mv_0/\Delta t = mv_\text{r}/\Delta t$ correct.
- L3-05: $v = v_0 + at$, $a = -g$ (up positive): $v_1 = -g t_\text{fall}$ from rest, $0 = v_2 - g t_\text{rise}$; $\Sigma F = N_\text{avg} - mg$; final form unchanged and right.
- L1-07: $I = \Delta p = mv - mv_0$ right.
- Paragraph splits (L1-06, L1-09, L2-06, L3-04, L3-05, L2-09) move no claim and drop no reason; the run-together formulas in the packet diff are diff rendering only (file lines 230–236 are separate).
- Substitutions still match the last symbolic forms; answers recomputed earlier stand (no value changed).
