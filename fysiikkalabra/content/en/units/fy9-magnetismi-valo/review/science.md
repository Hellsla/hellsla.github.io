VERDICT: PASS
CONTENT-HASH: 3b6f5d5631f07584

## Delta review (round 4)

`git diff dcad1b122 -- content/en/units/fy9-magnetismi-valo lessons/units/fy9-magnetismi-valo` shows only the concept map `kartta` change: figures.json "liike tai virta" → "motion, current" (was "motion or current") and the regenerated foreignObject in unit.md (x 221→230, width 141→132). Nothing else changed. The grey label is a reading aid naming what the branch is about; "motion, current" keeps the meaning of the source (force on a moving charge and on a current), and no formula, number or unit changed. I restored the earlier report's formulas, which shell expansion had stripped (the earlier report's text only, not the unit). Verdict unchanged: PASS.

# fy9-magnetismi-valo (en): science review of the translation, round 3

Scope: changes since round 2. The translation texts are unchanged; the only content change is the redrawn figures
after `scripts/figlib.py` `translate()` began translating `\textbf{}` contents. The concept map `kartta` now
names the three branches "forces in a field", "induction", "light"; all formulas in it are unchanged and correct
($F = qvB\sin\alpha$, $F = IlB\sin\alpha$, $B = \mu_0 I/(2\pi r)$, $e = -N\,\Delta\Phi/\Delta t$,
$e_0 = NBA\cdot 2\pi f$, $U_1/U_2 = N_1/N_2$, $n_1\sin\alpha_1 = n_2\sin\alpha_2$, $d\sin\theta = k\lambda$,
$I = I_0\cos^2\theta$). The other figures (siirto 174 A / 15 kW / 38 %, 2.0 A / 2.0 W / 0.005 %; ympyra
$r = mv/(qB)$ with force to the centre, anticlockwise for a positive charge in a field into the page; s3-B and s3-lin
with $\mu_0 I/(2\pi) \approx 2.42\ \mu\text{T·m}$, $B \approx 11\ \mu\text{T}$) are as in round 2. The round-1 recomputation
of every number still holds. `check_i18n.py` en: 0 errors; `units.py check`: 77 units ok; `practice.py check`:
en/units/fy9-magnetismi-valo 6 tasks, 95 points; `units.py figures --lang en --check`: up to date.

## Blocking
None.

## Polish
None.
