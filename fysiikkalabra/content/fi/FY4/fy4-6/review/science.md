VERDICT: PASS
CONTENT-HASH: 75e3d3915811c5e0

## Blocking

## Polish
- lesson.md:143–148 — The question gives $m = 80\,\text{kg}$, but the answer uses no number. Either drop the mass or add the value to the answer: "Kuussa paino on noin $130\,\text{N}$, Maassa noin $785\,\text{N}$." (80 · 1,62 = 129,6 N; 80 · 9,81 = 784,8 N.)
- lesson.md:314, 318 — (carried over) $F_{\mu 0}$ stands both for static friction ($\le \mu_0 N$) and for its greatest value ($= \mu_0 N$). Write "juuri ennen liukumista" at the equality.
- lesson.md:386 — (carried over) "$\mu = F : mg$" should be $\dfrac{F}{mg}$.
- assets/sims/fy4/fy4-6/sim.js:28 — (carried over) above the slip angle the readout says "liukuu" before *Käynnistä*. Say in Mallin oletukset that the readings apply just after release.

## Checked
- Delta only: four new `pysahdy` blocks (Paino, Lepokitka ja liukukitka, Kalteva taso, Kitka ei aina vastusta liikettä) and the worked example's knowns split from its question (same values, no physics change).
- Paino: correct. Mass is the same everywhere and weight $mg$ falls because $g_\text{Kuu} < g_\text{Maa}$. The paragraph before it gives both facts.
- Lepokitka: correct. Static friction equals the pull and is opposite to it, because the net force is zero. The paragraph before it says this almost word for word.
- Kalteva taso: correct (A/B check passed). The component along the slope grows. $N$, and with it the greatest static friction $\mu_0 N$, falls. The answer leans on the condition the paragraph states just before it (only weight and normal force act across the slope, no acceleration in that direction), so no condition is missing. Recomputed the slip angle: $\arctan 0{,}5 = 26{,}57^\circ$, the same as the earlier review.
- Kävely: correct mechanism. The foot pushes the ground backwards, and the ground's static friction pushes the foot forwards. The answer comes from the subsection's first paragraph. The second paragraph (buoyancy, drag) sits between them but does not contradict it. The terms follow P8 (lepokitka, lähtökitka, no liikekitka).
- Each question can be answered from the text that comes before it. No answer brings in physics from outside the course.
- No screenshots opened: the change is text only and changes no figure, sim or inquiry behaviour.
- The hash was the same at the start and at the end.
