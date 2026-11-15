VERDICT: PASS
CONTENT-HASH: 3255f7774d0e9cda

## Blocking

## Polish
- lesson.md:291 — (B, minor) "rinteen on oltava niin jyrkkä, että pulkka liukuu: $\tan\alpha > \mu$". Every sled here starts from rest, and starting from rest needs $\tan\alpha > \mu_0$ (lähtökitka). $\tan\alpha > \mu$ only keeps an already sliding sled from stopping on the slope — fix: "…jotta liikkuva pulkka ei pysähdy rinteeseen: $\tan\alpha > \mu$ (lähteäkseen levosta $\tan\alpha > \mu_0$)".
- inquiry.json:178 — the johtopaatos prompt says "pysähtyy silti lähes yhtä kauas", but the model table gives exactly $60{,}0\,\text{m}$ on every row and the model answer says the slope has no effect. Fix: drop "lähes", or tie it explicitly to real hills (the bend).
- lesson.md:407 — "Hississä lattian tukivoima on liikkeen suuntainen ja tekee työtä": in a lift going down, the work is negative. Fix: "…on liikkeen suuntainen tai sitä vastaan ja tekee työtä".

## Checked
- I recomputed every lesson and inquiry number in one script with my own formulas: lift $648{,}6\,\text{N}$/$66\,\text{kg}$, canopy $78\,\text{kJ}$, force-plate $a = 1{,}023$ and $-0{,}643\,\text{m/s}^2$ (and the 9,0 → 12,2 s stop the figure shows), the slope table ($x_1$, $v$, $x_2$, sum $60{,}0\,\text{m}$, $\sqrt{2gh} = 10{,}8\,\text{m/s}$), example $8{,}69\,\text{m/s}$, $h = 8{,}55\,\text{m}$, $13{,}0\,\text{m/s}$ and $a = 1{,}51\,\text{m/s}^2$, siirto $95{,}6\,\text{kJ}$, check-2 $48{,}3\,\text{kg}$, suitcase $T = 150\,\text{N}$. Mistake values and lesson-answers.py agree.
- The friction-work derivation $W_\mu = -\mu mgx$ and the result $h/\mu$ state their conditions (straight surface, same μ, only weight and normal force across the surface, short bend, no air resistance).
- Energy principle stated with W as the work of forces other than weight, consistent with the prior chapter. Energy ends up as internal energy (guardrail P1); the term is liukukitka.
- Figure kolme is to scale: lift $N/G = 1{,}10$ for $a = 1{,}0\,\text{m/s}^2$, canopy $F_\text{v} = G$, sled $N = G\cos 20^\circ$ and $F_\mu \approx 0{,}2N$. Directions right; v and a apart from the forces.
- Example force diagram: $N$, $F_\mu$, $G_x$ and $G_y$ lengths match $\cos/\sin 20^\circ$ and $\mu = 0{,}200$. Components are dashed and the axes match the text.
- The hero is claimed to scale and is: both flags $520\,\text{px}$ from the summit, $h \approx 130\,\text{px}$ (μ ≈ 0,25), and both slopes steeper than $\tan^{-1}\mu$.
- hissi-kuvaaja phases agree with the text, the hints and the solutions.
- Exactly one correct option in kertaus, pred-1, pred-2, kelkka-taulukko, check-1 and check-3, and each distractor's feedback is right.
- The piirra rubric and model are right: tension at the handle, $T = m(g - a) < mg$, positive direction down, no "lift force".
