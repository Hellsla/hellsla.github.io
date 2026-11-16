VERDICT: PASS
CONTENT-HASH: 26546fe8d6e3ece7

## Blocking

## Polish
- lesson.md "Kaava" and "Kitkakertoimen määrittäminen", and the Tiivistelmä — the one symbol $F_{\mu 0}$ stands for any static friction ($F_{\mu 0} \le \mu_0 N$) and for its largest value, the lähtökitka ($F_{\mu 0} = \mu_0 N$). Fix: keep $F_{\mu 0}$ for the lähtökitka only and write the inequality for the static friction $F_\mu \le \mu_0 N$.
- assets/sims/fy4/fy4-6/sim.js `diagram()` (`S = S0 * 4 / M.m`) — the arrow scale changes with the mass, so in Koe 2 the 4,0 kg box's arrows are as long as the 2,0 kg box's. The canvas note says the scale depends on the mass, but the sim lead says "mittakaavassa". Fix: say in Koe 2's intro (or in Mallin oletukset) that the numbers, not the arrow lengths, show that the forces double.
- lesson.md Esimerkki, Sijoitus — the chains are split into rows by hand (`\quad\ \cdot`). Numbers right; wrapping is mathlayout's (visual).

## Checked
- Recomputed every number in one script: worked example $F_\mu = 48{,}0\,\text{N}$, $a = 1{,}48\,\text{m/s}^2$, $g\sin 25^\circ = 4{,}1$, $G_x = 75\,\text{N}$; Moon 97/590 N; friction graph 50/35 N, to scale.
- pred-1 values 3,4 / 6,7 / 8,6 N; exp-1 $\tan 26{,}5^\circ = 0{,}499$ (26° holds with tan 0,488 < 0,50, 27° slides with 0,510); the sin and cos mistakes; the 5,2 N kinetic friction at 27°; exp-2 3,22 m/s² for every mass.
- interpret: ratios 0,347/0,357/0,347/0,352, mean 0,350, the F/m mistake 3,44; siirto 20,3 N (75,8 and 78,5 as mistakes); check-2 $\tan 17^\circ = 0{,}306$; check-3 N 184, $F_\mu$ 46, T 113 N.
- sim.js implements the stated model exactly ($N = mg\cos\alpha$, rest iff $G_x \le \mu_0 N$, then $F_\mu = G_x$, else $\mu N$ and $a = g(\sin\alpha - \mu\cos\alpha)$); simState gives Gx, N, Fmu, a; the experiments lock pinta and m (exp-1) or pinta and α (exp-2), so each varies one parameter.
- The force diagrams (kalteva-ydin at 40°: $G_x$ the same length as $F_\mu$, $G_y$ the same as N, angle α right), virhe (only N's direction wrong), valitse a–d (one error each, feedback right), malli-veto, kuorma (friction forward on the accelerating bed).
- P8 friction terms; the condition for $N = mg\cos\alpha$ stated at each use; components dashed, never double-counted.
- One correct option in kertaus, pred-1, pred-2, virhe, valitse, check-1; distractor feedbacks correct; exit ticket consistent with the theory.
