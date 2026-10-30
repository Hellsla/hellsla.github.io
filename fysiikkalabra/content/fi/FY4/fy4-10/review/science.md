VERDICT: FAIL
CONTENT-HASH: ea54b95e9861d776

## Blocking
- lesson.md:64, inquiry.json:10 (prior), inquiry.json:27 (kertaus) — B: "voiman impulssi muuttaa sitä: $\Delta\overline{p} = \overline{F}\,\Delta t$" drops the condition that *Liikemäärä ja impulssi* states. There, Δp equals the impulse of the **total** force, and $\overline{F}\,\Delta t$ applies only to a constant force. This chapter rests on internal versus external forces. A 3,0 N force fixes Δp in kertaus only if it is the total force. — Write "kokonaisvoiman impulssi muuttaa sitä: $\Delta\overline{p} = \Sigma\overline{F}\,\Delta t$ (vakiovoimalla)". In kertaus write "Vaunuun vaikuttava kokonaisvoima on $3{,}0\,\text{N}$ liikkeen suuntaan ajan $0{,}10\,\text{s}$."

## Polish
- lesson.md:69 — "muuttuu impulssin $\overline{F}\,\Delta t$ verran" uses the constant-force expression for a bumper force that varies. — Write "Jos voima on vakio, …", or use $F_\text{ka}\,\Delta t$ as the previous chapter does.
- Notation versus *Liikemäärä ja impulssi*: there an unprimed $v$ is the velocity after ($v_0 \to v$); here it is the velocity before ($v \to v'$). Both chapters define their symbols and no formula mixes them. — Add one bridging line under "Säilymislaki … yhdessä ulottuvuudessa".
- lang/fi.json sims.fy4-10 "lukemat" — "Nyt: $v_1$, $v_2$" are the current velocities, but the sliders use the same symbols for the initial ones. — Rename them.
- inquiry.json siirto Järkevyys — "Kokemus vahvistaa tuloksen" is not a check. — Drop it.

## Checked
- The hash was the same at the start and the end. Every round 1 finding is fixed: pred-2, the exit ticket, lesson.md:333 and siirto.
- I recomputed every number in one script and all agree with lesson-answers.py: the example (1,14 m/s; 38,3 → 32,5 kJ; 15 %), 0,30 m/s with 0,072/0,036 J, pred-1 0,42, the explosion 0,63/1,26 m/s, elastic 0,20/0,80 and −0,12/0,48, exp-1 0,029–0,048 J, virhe 0,025, siirto 1,0, check-2 0,15 and the mistake values.
- sim.js uses equal and opposite forces F = max(0, kd + cΔv), a critically damped tarra that sticks with p conserved, and an explosion spring of 0,24 J. simState gives u1, u2, pJ and EkJ, and each experiment varies only m2.
- The derivation from the third law holds. The condition for conservation is stated in the theory, summary, example, checks and exit ticket.
- Billiards: only the swap satisfies both laws.
- The figures are to scale (½v, equal p).
- Each choice has exactly one correct option, and every distractor's feedback is right.
- The scope is FY4 and one-dimensional only.
