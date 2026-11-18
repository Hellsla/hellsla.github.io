VERDICT: PASS
CONTENT-HASH: 298637ea9d4e8509
Mode: delta (round 2)

## Blocking

## Polish
- lessons/FY4/fy4-3/figures.py:433 — still open from before: the float $\sin^2\pi > 0$ at $t = T_1$ adds noise, so the readings are not exactly 0 at $0{,}15\,\text{s}$. Test `T0 < t < T1`.

## Checked
- Hash 298637ea9d4e8509 at the start and the end. The diff changes only the L3-05 Kaava and the Sijoitus lead-in.
- L3-05 Kaava: the mean now has its own symbols, $F_\text{ka} = (F_1 + F_2 + F_3)/3$. The step then uses the first law, $\Sigma F = F_\text{ka} - F_\text{k} = 0$, so $F_\text{k} = F_\text{ka}$. The earlier clash, where $\Sigma F$ was both a sum of readings and the net force, is gone. The fix is right.
- Sijoitus: $F_1 + F_2 + F_3 = 3{,}4 + 3{,}5 + 3{,}3 = 10{,}2\,\text{N}$, and $10{,}2 / 3 = 3{,}40\,\text{N}$. The answer is still 3,4 N with two significant figures. The last symbolic form is what gets substituted.
- No other number, answer, tolerance or task changed.
- Captures opened: none. I judged from the diff, the file on disk and the packet.
