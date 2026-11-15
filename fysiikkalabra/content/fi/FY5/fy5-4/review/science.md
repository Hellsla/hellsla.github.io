VERDICT: PASS
CONTENT-HASH: 093745b877297051

## Blocking

## Polish
- lesson.md:459 (Tiivistelmä): "Kaarteessa keskeisvoiman antaa tien kitka" drops the condition the theory states (a level road, no air resistance). Add "vaakasuoralla tiellä".
- lesson.md:450 (Järkevyys): on wet asphalt $\mu_0 \approx 0{,}50$ is just under the $0{,}51$ needed, so "pito on rajoilla" undersells it. Say "pito ei aivan riitä".
- inquiry.json pred-2, the "vauhti hidastuu" feedback: "Se ei hidasta autoa" is true while the grip holds, and in the model. A real skid does slow the car, as Mallin oletukset says. Add "mallissa".
- inquiry.json check-3: $T$ stands for the cord's tension, while the same lesson uses $T$ for the period ($v = 2\pi r/T$, check-2). Consider $\overline{F}_\text{j}$ or a note.
- lesson.md:20 and check-2 say "kierrosaika", while the prerequisite chapter and the scope notes say "jaksonaika". Use one word, or write "kierrosaika eli jaksonaika" once.

## Checked
- I recomputed every number in one script with my own formulas and set it beside lesson-answers.py. All match:
  - the graph: 2, 8 and $4\,\text{m/s}^2$
  - the worked example: $15\,\text{m/s}$, $6000\,\text{N}$, $\mu_0 \ge 0{,}5097 \to 0{,}51$ (a "vähintään" value, rounded up)
  - Koe 1: $0{,}75$, $3{,}0$, $6{,}75$, $12$, $18{,}75$ and $27\,\text{kN}$ against $11{,}77\,\text{kN}$; the grip holds only at 5–15 m/s
  - the limit speed: $19{,}81\,\text{m/s}$, rounded down to $19{,}8$ for a "suurin" value, about $71\,\text{km/h}$; the mistake values $22{,}15$ and $392{,}4$
  - Koe 2: the ratio $0{,}920$ at every mass
  - siirto: $15{,}34\,\text{m/s}$, mistakes $18{,}79$ and $10{,}85$, $a_\text{n} = 2g$
  - check-2: $148\,\text{N} \to 150\,\text{N}$, mistakes $47{,}1$ and $294\,\text{N}$
  - check-3: $T = 0{,}765\,\text{N}$, $N = 1{,}67\,\text{N}$, ratio 0,46; the exit ticket's factor of 9
- The round-2 change, exp-1 with 6 speeds and min 6: I checked it in the browser on preview/fy5-4.html. At 25 and 30 m/s simState gives pito 0 and done true. The largest distance, $67{,}8\,\text{m}$, is beyond the asphalt edge at $57{,}3\,\text{m}$, so the car leaves the asphalt and pred-2's correct option can be seen. At 20 m/s it slides but stays on the asphalt (51 m); the intro does not ask for Käynnistä at that speed. pred-2's reveal.min of 6 matches the six speeds.
- The calc box now gives the full name "täysin kehittynyt lepokitka eli lähtökitka" as the guardrail requires. It agrees with pred-3 and with "lepokitka on enintään $\mu_0 N$".
- Sim code: $a_\text{n} = v^2/r$, $N = mg$, the grip condition $mv^2/r \le \mu_0 mg$. When sliding, the heading turns at $\mu_0 g/v$, a radius of $v^2/(\mu_0 g)$ (79,6 m and 114,7 m). Its limits are stated in Mallin oletukset.
- Experiments isolate the varied quantity: exp-1 varies v with r, m and the surface locked; exp-2 varies m with r, v and the surface locked. The measured keys are in simState.
- Every correct option is right and each distractor is wrong with correct feedback: kertaus, pred-1–3, virhe, valitse, check-1.
- Figures (unchanged since round 1): the graph's scale; $F_\mu/G \approx 0{,}5$ in kaarre and esimerkki; N = 0,6 G and 1,4 G in nyppyla; malli-kiekko with G, N and T only.
- Centrifugal force: no real outward force in the ground frame, a fictitious force only in the rotating frame. Keskeisvoima is a sum, never drawn as an arrow of its own.
- Scope: FY5 normal acceleration, with no angular quantities.
- The hash was 093745b877297051 at the start and at the end. The packet's line-2 command says `--lang fi-easy`, but this is the fi packet, so I used the fi hash its header names.
