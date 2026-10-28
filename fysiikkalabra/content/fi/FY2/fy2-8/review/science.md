VERDICT: PASS
CONTENT-HASH: 1a0dc50dd6998ead

## Blocking

## Polish
- assets/sims/fy2/fy2-8/sim.js:8–9 — the header comment breaks off mid-sentence: "…and still warms." is followed by "towards the level's value gradually…", which has lost its subject. Fix: start line 9 with "The ground temperature moves".
- content/fi/FY2/fy2-8/inquiry.json koe-1 `measure` — the recorded key `Teq` is the level's constant. The intro now tells the student to wait for the thermometer, but "Kirjaa mittaus" could still record `T` once `tila` is "asettunut", so the row is something the student actually observed.

## Checked
- Round 1 blocking 1 is fixed. The 420 ppm level settles at +16 °C (14 + 3 · log₂(420 : 280) ≈ 15,8). `reset` starts at today's measured +15 °C, and the readout shows "lämpenee" towards +16 °C (screenshot). The `model` box, the sim-spec and the koe-1 correct feedback all say that today's temperature is measured but not settled. 280 ppm (+14 °C) and 560 ppm (+17 °C) are now both equilibrium values, so the four levels are consistent.
- Round 1 blocking 2 is fixed. `names` and the measure label render as LaTeX ($\text{CO}_2$-pitoisuus, asettuva $T\ ({}^\circ\text{C})$, seen in the screenshot). `values` names all four levels, and both the 0 level and the intro say that water vapour and methane are removed too.
- The ennuste-1 feedback names water vapour as the main greenhouse gas, and the 33 K figure is right.
- With a time constant of 3 s, the half-life is 2,08 s ("puolittuu noin kahdessa sekunnissa"). The step from +15 °C to +16 °C settles in about 9 s at normal speed.
- Every lesson, inquiry and exit-ticket number is unchanged since round 1, and I recomputed all of them then (all match lesson-answers.py).
- In round 2 lesson.md changed only in whitespace, and lesson-answers.py did not change.
- The sim physics is unchanged apart from the 420 level and the start value: the absorbed share, the ∝T⁴ photon rate, the random re-emission, and no radiative balance (FY3).
- The figures, the emission-factor table (IPCC AR5) and m = e · E stay within scope and are correct.
