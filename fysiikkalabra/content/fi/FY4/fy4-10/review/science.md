VERDICT: FAIL
CONTENT-HASH: d15d01b881f4b0bf

## Blocking
- inquiry.json:10 (prior, *Pohjatiedot*) — B: this line still reads "voiman impulssi muuttaa sitä: $\Delta\overline{p} = \overline{F}\,\Delta t$". It is the third location named in the round 2 finding and was not changed. It now contradicts lesson.md:64 and the kertaus prompt, which correctly say that Δp is the impulse of the constant **total** force. — Write "vakiosuuruisen kokonaisvoiman impulssi muuttaa sitä: $\Delta\overline{p} = \Sigma\overline{F}\,\Delta t$ (luku *Liikemäärä ja impulssi*)".

## Polish
- lesson.md:69 — "muuttuu impulssin $\overline{F}\,\Delta t$ verran" uses the constant-force expression for a bumper force that varies. The paragraph's last sentence rescues it. — Write "Jos voima on vakio, …".
- Notation versus *Liikemäärä ja impulssi*: there an unprimed $v$ is the velocity after; here it is the velocity before. — Add one bridging line.
- lang/fi.json sims.fy4-10 "lukemat" — "Nyt: $v_1$, $v_2$" uses the symbols of the initial-velocity sliders. — Rename them.
- inquiry.json siirto Järkevyys — "Kokemus vahvistaa tuloksen" is not a check. — Drop it.

## Checked
- Hash d15d01b881f4b0bf at the start and the end. Since round 2 (commit 5a2b616d), only lesson.md:64 and the kertaus prompt changed in the lesson files.
- lesson.md:64: "vakiosuuruisen kokonaisvoiman impulssi … $\Sigma\overline{F}\,\Delta t$" is correct and matches the previous chapter.
- Kertaus: the force is now the constant total force, so Δp = 0,30 kg·m/s is fixed. The correct option and the two distractor feedbacks (quotient F/Δt, mass not needed) are right.
- Everything else is unchanged from round 2. These round 2 checks still hold: every recomputed number, the sim model and simState, the third-law derivation and its stated condition, the billiards argument, figure scale, one correct option per choice, and FY4 one-dimensional scope.
