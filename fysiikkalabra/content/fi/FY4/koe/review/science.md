VERDICT: PASS
CONTENT-HASH: 0935f577ae3e5f4c
## Blocking

## Polish
- solutions.md fy4-k7 d) Kaava — $F$ in "$W = -Fs$ … $F = ma$" is the total stopping force, while in c) $F$ is the helmet's force with $F - G = ma$; write $\Sigma F$ ("kokonaisvoima") here so the two are not confused (carried over, now with the sign right).
- solutions.md fy4-k4 a) — Periaate names the mekaniikan energiaperiaate, the Kaava the työperiaate; both hold here ($E_\text{p}$ constant, only friction works), but one name is cleaner.
- solutions.md fy4-k6 e) Sijoitus — "$0{,}52\,\text{s}$ … $0{,}34\,\text{m}$": $9{,}81 \cdot 0{,}52^2/8 = 0{,}33\,\text{m}$; write $0{,}523\,\text{s}$ and $0{,}457\,\text{s}$ (carried over).
- solutions.md fy4-k7 c) Annettu $a = 600\,\text{m/s}^2$, Sijoitus $603\,\text{m/s}^2$; give $603$ (carried over).
- solutions.md fy4-k5 a), c) etc. — "joten … $\Rightarrow$ …" repeats the inference (carried over).

## Checked
- Round 3: hash 0935f577ae3e5f4c matches the packet; since my round-2 PASS (git diff bc76984351..HEAD) only the Kaava rows of k4 a) and k7 d) changed; no task, number, point, rubric or answer.
- k4 a): $E_{\text{k}0} + W = E_\text{k}$ with $W = -F_\mu s = -\mu mg\,s$ ($N = mg$ on the horizontal table), $E_\text{k} = 0$, so $\mu = v^2/(2gs)$; the sign now agrees with the task's own Yleisiä virheitä.
- k7 d): $E_{\text{k}0} + W = E_\text{k}$, $W = -Fs$, $F = ma$ (total force, average deceleration) gives $a = v^2/(2s)$, the same as the Periaate's $v^2 = 2as$; signed work right.
- Recomputed in one call: $v = 5{,}425\,\text{m/s}$, $a_1 = 613\,\text{m/s}^2$, $a_2 = 1472\,\text{m/s}^2$, ratio $1{,}55$, $a_\text{huippu,2} = 2280\,\text{m/s}^2$ (margin $6{,}9\,\%$); $\mu = 0{,}249$ ($0{,}234$–$0{,}265$). Agree with answers.py.
- The rest as checked in rounds 1 and 2 (all numbers, Osa 1 keys, physics wording, "sisäenergiaksi", lepokitka/lähtökitka terms).
- Captures: none opened (two text rows, judged from the packet and solutions.md).
- Hash 0935f577ae3e5f4c at start and end.
