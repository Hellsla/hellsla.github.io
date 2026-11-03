VERDICT: DONE

Round 1 fix.

- `assets/sims/fy5/fy5-4/sim.js`: the header now says the sliding car turns more gently than the track, and straighter the faster it goes. `simState` gains `dmax` and `reuna`. Both acceleration labels read $\overline{a}_\text{n}$. The controls sit in two rows, so the legend stays visible at 1280 px.
- `lang/fi.json` (`sims.fy5-4.liukuu`): the readout says "auto liukuu", not "liukuu radalta".
- `tests/sims/fy5-4.json`: added two checks that at 25 and 30 m/s on dry asphalt (r = 50 m) the car ends up past the asphalt's outer edge.
- `sim-spec.md`, `lesson-answers.py`: same wording as sim.js; added the slide radii.
- `inquiry.json`: neutral hook text and learn goal 3; reworded the pred-1 and pred-2 feedback and the conclusion's model answer. exp-1 now ends with a slide at 25 and 30 m/s. Wrote `massa $m$` in exp-1 and exp-2. The exp-1 diagram has the centre on the right (`akselit 0`), and the Vastaus line is fixed.
- `lesson.md`: neutral Miksi question; added the condition to the friction sentence; one paragraph on why $a_\text{n}$ depends on $v^2/r$; changed the bump to "= g → N = 0, > g → leaves the road"; the example's centre is now on the right.
- `figures.py`: removed the dashed line from the hero; both muutos panels use one arrow length; moved the label positions in fig-10, 12 and 13; flipped esimerkki.
- Exercises: L1-03 rope ≈ 8,3 N. L2-01 is now a cyclist in a dip (1,1 kN). In L3-02 $T$ stays the tension (glossary) and the period symbol is gone ($v = 2\pi r f$). All diagrams use `akselit 0`.
