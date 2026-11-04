VERDICT: PASS
CONTENT-HASH: db89440a4bef0c0d

## Blocking

## Polish
- solutions.md (L3-04, voimakuvio blocks) — the vertical arrows are drawn shortened ($G_1 = 30$ beside $F = 27$, while the real weight is about 235 kN). The text says so, but a model diagram with knowingly wrong length ratios goes against the "arrows in physically meaningful proportion" rule that YTL marks down. Consider drawing the weights to scale, or showing only the horizontal forces plus a note that $\overline{G}$ and $\overline{N}$ cancel.
- solutions.md (L3-05, voimakuvio) — $G_1 = 8{,}92$ uses the mean cart mass 0,909 kg, not this measurement's 0,930 kg. Say "keskiarvomassalla" in the Voimakuvio line.
- L2-06 — the bank plan's "kitkan arvio" is still not done (optional, carried over).

## Checked
- Round-1 items fixed. L2-07 now keys 2.0 with tolerance 0,02 (|2,0 − 1,962|/1,962 = 1,9 %), and answers.py matches. L2-06 now gives a true reason for two figures (3,41 and 3,49 N are about 2 % apart). L3-05 now has a Voimakuvio step before the equations.
- L3-04 voimakuvio blocks: the horizontal forces sum to $m\overline{a}$ in each wagon: 27 − 15 = 12 = 24 t · 0,50; 15 − 6 = 9 = 18 t · 0,50; 6 = 12 t · 0,50.
- L3-04: the Vastaus is now in the order a), b), c), and "ne on kytketty" is fixed.
- L3-05 voimakuvio: $T = 1{,}6$ N and $G_2 - T \approx m_2 a$ are consistent within rounding.
- L2-05: the rounding reason is now the hand-fitted line.
- L2-07: the reworded Järkevyys is correct ($m_2 g - T \approx 0 \ne m_2 a = 1{,}2$ N).
- Changed answers recomputed: 2,0; 3,408 and 3,485; 15,03 kN; 0,909 kg. All are inside their tolerances.
