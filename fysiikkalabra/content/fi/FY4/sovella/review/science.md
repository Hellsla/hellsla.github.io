VERDICT: PASS
CONTENT-HASH: 8714d203727c4572
## Blocking

## Polish
- solutions.md fy4-s3 e) — "eli laskettu arvo on alaraja" holds for this one assumption only; the next two items can lower $v_\text{B}$. Fix: "tämän oletuksen osalta laskettu arvo on alaraja".
- solutions.md fy4-s3 b) Kaava — a display block followed by ", josta …" reads oddly. Fix: end the sentence after the block and start "Siitä ratkaistaan $v_\text{B} = …$".
- tasks.json fy4-s3 b criterion units_precision — "$v_\text{B} \approx 14\,\text{m/s} \approx 50\,\text{km/h}$" while the solution gives $49\,\text{km/h}$ (from $13{,}6\,\text{m/s}$); both are accepted, but one value in both places would be clearer.

## Checked
- Captures: none opened (judged from the packet text; the change since the last PASS is the Kaava text only).
- New Kaava rows (commit fcc9aacbfc): s1 c starts from $\Sigma F = ma$ and $F_\mu = \mu N$; s2 a from $E_{\text{p}0} + E_{\text{k}0} = E_\text{p} + E_\text{k}$; s2 b, c and s3 a from the chapter's $E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}$ with $W = -F s$ (negative, as taught); s3 b from $p_\text{ennen} = p_\text{jälkeen}$; s3 c from $I = F_\text{ka}\,\Delta t = \Delta p$. Each simplifies symbolically before substitution.
- Recomputed all numbers in one script: $g\sin 4{,}0^\circ = 0{,}684$, $g\cos 4{,}0^\circ = 9{,}786$; $\mu_\text{A} = 0{,}030$, $\mu_\text{B} = 0{,}045$, with $a_0 = 0{,}45$: $0{,}024$; $\sqrt{2gh} = 17{,}2\,\text{m/s} = 61{,}8\,\text{km/h}$; $F_\text{vast} = 29{,}1\,\text{N}$, lost share $0{,}574$; 95 kg: $13{,}6\,\text{m/s}$; $v' = 7{,}86\,\text{m/s}$, $v_\text{B} = 13{,}64\,\text{m/s} = 49{,}1\,\text{km/h}$; $E_\text{k}$ 158 → 91 kJ; $F_\text{ka} = 4455\,\text{N} = 6{,}7\,mg$; friction impulse $\le 2605\,\text{N·s}$, $v_\text{B} \le 15{,}2\,\text{m/s}$. All agree with answers.py.
- Points: every part's criteria sum to its points (s1 3+3+5+3+5, s2 3+4+3+4, s3 4+4+3+3+2); each criterion asks only what the task gives and asks.
- Physics: rope force normal to the motion does no work; friction proportional to $N = mg\cos\alpha$; air drag treated as a systematic error with the right sign; momentum over the short collision only; Newton I and impulse for the whiplash; "muuttuu sisäenergiaksi" (P1) kept.
- Significant figures justified by the limiting data in every part.
- Hyväksytään myös gives fit ranges and the $29\,\text{N}$ route; scope inside FY4.
- Hash 8714d203727c4572 at the start and at the end.
