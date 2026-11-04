VERDICT: FAIL
CONTENT-HASH: 03f78491accd52af

## Blocking
- solutions.md:348 (L3-05) — A: "Laatikko lähtee liukumaan, koska $\tan 25^\circ = 0{,}47 > \mu = 0{,}30$" uses the wrong coefficient. By the lesson, a box starts to slide only when $\tan\alpha > \mu_0$, and $\mu_0 \ge \mu$ is not given — write: "Liukuessaan laatikko kiihtyy alas, koska $\tan 25^\circ = 0{,}47 > \mu = 0{,}30$; tehtävän mukaan se lähtee liikkeelle, joten $\mu_0 < \tan 25^\circ$."
- solutions.md:318/321 (L3-04) — A: the shown result $s_c = 73{,}5\,\text{m}$ rounds to 74 m, but the Vastaus gives 73 m. The 73,5 comes from intermediates rounded before the end ($v_0^2 = 494$, $a_c = 3{,}36$), which NOTES forbids — carry unrounded values ($v_0^2 = 493{,}8\,\text{m}^2/\text{s}^2$, $a_c = 3{,}365\,\text{m/s}^2$), which give $s_c = 73{,}4\,\text{m} \approx 73\,\text{m}$. Likewise use $s_b = 55{,}9\,\text{m}$.
- solutions.md:289 (L2-07) — A: the shown $\mu_0 = \tan 25{,}4^\circ = 0{,}475$ is then rounded to 0,47 (line 290), which looks like a rounding error. Write $\tan 25{,}4^\circ = 0{,}4748$.

## Polish
- L3-05 — the angle 25° and μ = 0,30 are exactly the lesson's Esimerkki, so part b) is the example's $a = 1{,}48\,\text{m/s}^2$ copied, which is thin for level 3. Change the data, for example to 30° and μ = 0,35 (then a = 1,93 m/s² and s = 8,7 m in 3,0 s). Its fbd tag `error` also means "a drawn diagram with `wrong=`" in the standard, not an equation error.
- exercises.json:55/66 (L1-06) — the options call the friction $F$, the same symbol a reader takes for the 20 N push. Use $F_{\mu 0}$, as the lesson does.
- solutions.md:250 (L1-07) — $F_{\mu 0,\text{max}}$ is not lesson notation. Write $F - \mu_0 N = 0$.
- solutions.md:321 (L3-04) — "Auton massa ei tarvita" → "Auton massaa ei tarvita".
- L2-05 and L2-03 — both fit $(N, F_\mu)$ through the origin to get μ. L2-05 adds computing N from the mass and drawing the graph, so the overlap is acceptable, but L2-06 (the sensor peak) already carries the data work. State in the L2-06 text that the pull is horizontal from the start.

## Checked
- New answers recomputed: L1-07 220,7 N; L2-05 least-squares 0,416; L2-06 μ = 0,2945 and μ0 = 0,449; L2-07 tan 25,4° = 0,4748; L3-04 33,6, 55,9 and 73,4 m; L3-05 a = 1,479, student 1,203, s = 6,65 m. All are inside their tolerances.
- In L1-06 and L1-08, exactly one option is correct. Every distractor's feedback is right, and L1-08 states the condition "vain paino, tukivoima ja kitka".
- L2-07: the derivation $\mu_0 = \tan\alpha_0$ is right, the mass cancels, and the guardrails' measurement terms are respected.
- L3-04: locked wheels make kinetic friction the model. On the 6° downhill $a = g(\mu\cos\alpha - \sin\alpha)$, the voimakuvio block sums to $m\overline{a}$, and the hidastuvuus stays positive because μ > tan 6°.
