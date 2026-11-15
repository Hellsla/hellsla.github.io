VERDICT: FAIL
CONTENT-HASH: 8fd79cadff819b5c
Review of the recognition chart (queue 9c) and the term change against the version passed at 8fb4b213f8bfbe4b; full on the chart, delta on the rest.

## Blocking
- B (row 3, "tanko tai vipu voi kiertyä" → $\Sigma M = 0$): $\Sigma M = 0$ holds only when the body does not start to rotate, that is, in equilibrium. "Voi kiertyä" states the opposite situation, and the aria-label repeats it. The unit teaches no moments, so the chart is the only place this appears. The same chart in *Ympyräliike* gets it right ("tanko pysyy paikallaan"). Fix: "tanko tai vipu pysyy paikallaan" (or "on tasapainossa").
- B (row 9, "ilmanvastus, nopeus tasaantuu" → $F_\text{v} = G$): This is true only for vertical fall (buoyancy neglected). For a cyclist, a car or a skier on a slope, the levelled speed means air resistance balances the other forces along the motion, not the weight. The aria-label says the same. Fix: "putoaa, nopeus tasaantuu" (or "pystysuora putoaminen").

## Polish
- C (row 7): $F \le F_{\mu_0}$ is ambiguous about $F$. The static friction is the force bounded by $F_{\mu_0}$; the pull equals it only on level ground with a horizontal pull. Clearer: $F_\mu \le F_{\mu_0}$.
- C (row 1): "levossa" means "pysyy levossa". A momentary rest (top of a throw) has $a \neq 0$. Acceptable.

## Checked
- Rows 1–2 → $\Sigma\overline{F} = \overline{0}$ and $\Sigma\overline{F} = m\overline{a}$, with vectors overlined: match Kaava.
- Row 4 → one equation per body, $\Sigma F_i = m_i a_i$ (along the motion; equal $a$ for a taut light rope, as in the text).
- Rows 5–6: no friction on a frictionless surface; liukukitka $F_\mu = \mu N$.
- Row 8: lähtökitka = täysin kehittynyt lepokitka, $F_{\mu_0} = \mu_0 N$. Both match Kaava.
- The aria-label otherwise matches the chart.
- Term change in unit.md, inquiry.json, sovella tasks/solutions, answers.py comments and figures.py: the physics is unchanged.
- I recomputed the inquiry numbers I touched: $\mu = 54{,}38/151{,}22 = 0{,}360$ ($0{,}308$ with $N = mg$, so a 15 % difference); $a = 9{,}81(\sin 28^\circ - 0{,}15\cos 28^\circ) = 3{,}31\,\text{m/s}^2$ (with force-diagram values 88,29 and 13,24); $P = 48{,}0\,\text{N}$; the distractor $0{,}10 \cdot 25 \cdot 9{,}81 = 24{,}5 \approx 25\,\text{N}$. All are correct.
- The lepokitka distractor's feedback is correct.
