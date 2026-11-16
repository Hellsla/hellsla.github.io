VERDICT: PASS
CONTENT-HASH: 8b0962f5cbc82d0f

## Blocking

## Polish
- lesson.md:314, 318 — (carried over) $F_{\mu 0}$ is used both for static friction ($\le \mu_0 N$) and for its greatest value ($= \mu_0 N$). Write the equality as "juuri ennen liukumista $F_{\mu 0} = \mu_0 N$", or give the maximum its own subscript, so the equality is not read as always true.
- lesson.md:386 — "$\mu = F : mg$" can be read as $(F:m)\,g$. Use $\dfrac{F}{mg}$.
- assets/sims/fy4/fy4-6/sim.js:28 and inquiry.json:104 — above the slip angle, before *Käynnistä*, the readout and `simState` already say "liukuu": $F_\mu = \mu N$ and $a \ne 0$ while $v = 0$ and the box stands still. Fine for a just-released box; add to Mallin oletukset: "lukemat koskevat laatikkoa heti, kun se päästetään irti".

## Checked
- One script recomputed every number of the lesson and inquiry with my own formulas, and all agree with lesson-answers.py and the text to within 1 %. Worked example: $F_\mu = 48{,}0\,\text{N}$, $a = 1{,}48\,\text{m/s}^2$, $G_x = 74{,}6\,\text{N}$. Sim feedback: 3,41/6,71/8,60 N, slip 26,57°, 5,24 N at 27°, 3,22 m/s² at 35°. exp-1: $\tan 26{,}5^\circ = 0{,}499$, with the sin and cos mistakes. Interpret: mean 0,350, mistake 3,44. Siirto: 20,3 N. check-2: 0,306. check-3: N 184 N, T 113 N. Moon: 97 N and 589 N.
- The conditions are stated where they are used: $N = mg\cos\alpha$ only when weight and normal force alone act across the slope and there is no acceleration in that direction. The friction laws are empirical models for dry surfaces. Air resistance and buoyancy are neglected.
- Terms follow P8; no liikekitka.
- Example J (pickup, walking): correct mechanism, friction opposes relative sliding.
- Predictions, Etsi virhe, Valitse and check-1: each has exactly one correct option, and every distractor's feedback gives the right physics.
- figures.py: the friction graph is to scale (50 N → 35 N with N = 100 N). Pickup: $F_\mu = 40\,\text{N}$ against $G = 196\,\text{N}$. Each wrong option figure carries only its own single error. The forces' points of application and directions are right. Components are dashed. No velocity or acceleration is drawn as a force.
- The sim implements the stated model. Koe 1 and Koe 2 isolate their varied parameter by locking the other two, and `simState` gives Gx, N, Fmu and a.
- The hash was the same at the start and at the end.
