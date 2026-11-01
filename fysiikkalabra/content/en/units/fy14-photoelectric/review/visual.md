VERDICT: FAIL
CONTENT-HASH: f66de27277e0e818

## Blocking
1. [Major] Simulation canvas (`assets/sims/fy14/photoelectric/sim.js`, `p.quad(96, 52, CAT, TOP + 6, …)` and the photon packets ending at `CAT`; captures `sim-1280`, `sim-390-1`). The beam lights the **outer (left) face** of the cathode, while the electrons leave its **inner face** towards the collector. The photoelectric effect is a surface effect, so the picture suggests that electrons travel through the plate. Fix: aim the lamp and beam at the inner face. For example, move the lamp to about (300, 40) and send the beam and the packets to `x = CAT + 6`, so that the light comes in from above the gap. For science: confirm.
2. [Major] Simulation labels (`sim.js` line 86, `fh = Math.round(11 * k)`). The labels render at about 11 CSS px at both 390 and 1280 px. NOTES §"Readable on a phone" asks for about 14 px. *cathode* and *collector* in muted grey are hard to read on a phone, and the canvas looks small next to 17 px text at 1280. Fix: `fh = Math.round(14 * k)`, then rerun `test_sims.py`. Every label still fits inside 600 px.
3. [Major] Experiment tables (`inquiry.json` `exp-stop` measure `"label": "U"`; captures `stage-tutki-1280-1`, `stage-tutki-390-2`). The column `U` has no unit. The varied column shows only *wavelength* / *intensity*, also without a unit, even though `data-cols` holds `(nm)` / `(%)`. Fix: label `$U\;(\text{V})$`. In the experiment builder, render the varied column as `$\lambda\;(\text{nm})$` and `intensity (%)`.
4. [Major] "Back to your predictions" (`templates/inquiry.js` §6, `plainText(legend)`; capture `stage-selita-390-6`). The quoted prediction loses its maths and spacing: "…from 30 % to 90 %.What happens to the current I and to the largest kinetic energy Ek,max…". Fix (shared): copy the legend's rendered HTML (`legend.innerHTML`, with the `.scenario` and `.ask` spans joined by a space) instead of its plain text.

## Polish
5. [Minor] Worked example, step 6 (`unit.md` "**Result.**"). The display chain splits the sentence: "One photon has the energy [display] three significant figures as in the wavelength." Fix: "One photon has the energy $E \approx … \approx 3.06\ \text{eV}$. The answer has three significant figures, as in the wavelength."
6. [Minor] Inline maths. `\dfrac` in running text (the `planck-data` prompt and solution **Principle**) stretches the line spacing; use `\tfrac` or `(h/e)\,f - W/e`. Inline equations also break after "=" ("charge $e =$ / $1.602…$" at 1280; the sim readout "$W =$ / $2.36\,\text{eV}$" at 390). Keep each equality together, or move it into a display.
7. [Minor] Figures. Energy diagram: label the dashed level (for example `$\text{free electron}$`). $U_\text{s}$–$f$ graph: mark $f_0$ on the axis for both metals. The white rings on the points cut the sodium line so it looks dashed; draw the rings thinner or put the line on top. The `slope = h/e` label with `\dfrac` is about 8 px at 390; use `h/e`.
8. [Minor] Simulation: the electrons (6 px canvas, about 3 px on a phone) are nearly invisible, and at 400–490 nm the photon packets are as blue as the electrons. Fix: r 8 with a white ring.
9. [Minor] French corner (`fx-pe-french`): the tip for *un électron* "uh-nay-lek-TRON" contradicts the tip for *un photon* ("do not say the n"). Write "uh-nay-lek-TRÕ (nasal)".

## Checked
top-390/1280, intro-390/1280, every stage at 390 and 1280, sim-390-1/2, sim-1280 (zoomed), fx-1/2 at both widths, sources, teacher; the hero, energy and $U_\text{s}$–$f$ figures at both widths. The worked example with all seven steps, and the opened Planck-data and find-the-error solutions, recaptured by me with every step revealed (the unit captures show step 1 only). sim.js source read for the label size and the beam geometry. Hash unchanged at the end.

## Scores
illustrations 3 · typography 4 · English 4 · accessibility 3
