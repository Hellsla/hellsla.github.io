VERDICT: DONE

Round 1 fixes; `check_lesson.py fy8-8` all ok, `check_solutions.py` ok.

- `lesson.md`: in the worked example, $E_\gamma = 1{,}0600 \cdot 10^{-13}\,\text{J}$. The Sijoitus step now computes $hc = 1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}$ on its own split rows, so nothing is clipped at 390 px. The Ni-60 level is now 2505,8 keV (ENSDF 2505,753), and one clause says the gamma sum falls short of it because of the nucleus's recoil.
- `figures.py`: in the chart, the α arrow now starts at a heavy nucleus beyond the band's top end and points down-left at 45°, and the description gives the direction. The levels figure shows 2505,8 keV. Figures regenerated and catalog rebuilt.
- `lesson-answers.py`: checks 1,0600e-13 J, hc, the λ from the rounded values, the 2505,8 level and the 0,033 keV recoil gap.
- `inquiry.json`: removed the giveaway clause from ennuste-2. The gammaspektri text and hint 3 no longer give the peak energies, so the figure is the only source. The solution's Järkevyys now cites 2505,8 keV and explains the recoil.
- `sim.js`, `sim-spec.md`: added stable Tl-203 and Pb-204 at N = 122.
- `glossary.json`: beetahajoaminen now covers β⁻ and β⁺.
- Exercises: L2-01 uses 2505,8 keV (1173,3 keV, answer 1,06 pm unchanged; `answers.py` updated), drops the source attribution and explains the recoil in Järkevyys. Removed the stray leading ";" from the Vastaus lines.
