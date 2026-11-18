VERDICT: FAIL
CONTENT-HASH: f7b8d233f6ae25a0

## Blocking
- content/fi-easy/FY4/fy4-16/exercises/solutions.md:121, 179, 214, 331, 351 (fy4-16-L2-02, L3-01, L3-03, L3-04, L3-05 Kaava) — the new lead-ins name a resisting force's work as positive: "Kitkan työ on $F_\mu L$", "kitkan työ on $W_\mu = F_\mu s$", "ilmanvastuksen työ $W_\text{v} = F_\text{v} h$", then use $E_\text{alku} = E_\text{loppu} + W$. Friction and air resistance oppose the motion and do negative work; the brief's lesson writes $W_\mu = -\mu m g x$ and "ilmanvastuksen työ on $-mgh$" with $E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}$, and this set's own L1-04 (line 64) says "$W = -F_\mu s$". The equations that follow are right, but the step teaches a wrong sign for the same symbol $W_\mu$ — write $W_\mu = -F_\mu s$ (and $W_\text{v} = -F_\text{v} h$) with $E_\text{alku} + W = E_\text{loppu}$, or say "kitkan työn suuruus on $F_\mu s$"; numbers unchanged.

## Polish
- solutions.md:351 (L3-05 Kaava) — the interval mean of the end speeds is exact only for uniformly changing speed; the canopy deceleration is not uniform, so "likimain" belongs with $h = \sum \tfrac{v_i + v_{i+1}}{2}\Delta t$.
- solutions.md:179 (L3-01 Kaava) — "vaakasuora osuus on $x = s\cos\alpha$" uses $s$ for each part's own length while the task's parts are $x_\text{a}$, $x_\text{b}$, $x_\text{c}$; name it per part.
- solutions.md (L3-04 Järkevyys, L3-05 Järkevyys) — the new breaks leave "Lopussa ilmanvastus lähestyy painoa …" alone as a one-sentence paragraph; keep it with the preceding one.

## Checked
- Hash f7b8d233f6ae25a0 at the start and the end; since 062f457c28^ only solutions.md changed: `**Kaava:**` lines and one L3-04 Sijoitus line (label "Sulkulauseke", the repeated symbolic $v$ dropped because Kaava now ends in it); numbers, answers, tolerances, tasks, ids, exercises.json and answers.py unchanged.
- Lift tasks: $\Sigma F = ma$ with positive up $N - mg = ma$, positive down $mg - N = ma$; $v = v_0 + at$ with $v_0 = 0$ correct.
- Constant-speed incline: $\Sigma F = 0$ in both directions → $\tan\alpha = \mu$; braking $\mu = |a|/g$ from $\mu mg = m|a|$.
- Energy chains reach the same final equations as before ($v_2 = \sqrt{2gh}$, $s = v_1^2/(2\mu g)$, $x = h/\mu$, $L = \mu_2 d/(\sin\alpha - \mu_1\cos\alpha)$, $F_\text{v} = mg + (E_{\text{k}0} - E_\text{k})/h$); L3-04 recomputed $L = 16{,}33\,\text{m}$, $v = 7{,}67\,\text{m/s}$.
- Hoist: $T = mg$, $W = Th$, $P = W/t$ right.
- Captures: none opened (fi-easy judged from text and the packet).
