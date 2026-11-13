VERDICT: FAIL
CONTENT-HASH: c8fedeca02ca08f2

## Blocking
- lessons/FY8/fy8-12/figures.py:56 (shown in lesson.md:87, figure `energia`). **A.** The visible-light band runs violet, blue, green, yellow, orange, red from left to right on an axis where photon energy increases to the right. That puts violet at 1,7 eV and red at 3,3 eV, the reverse of E = hf, which the paragraph above the figure teaches. The capture fig-4-390 confirms it. Fix: reverse `cols` so red sits at 1,7 eV and violet at 3,3 eV, then regenerate the figure.

## Polish
- inquiry.json:64 (ennuste-1, correct option's feedback). The alpha source behind 5 mm of aluminium gives a model value of 9 pulses. With a background mean of 4, P(N ≥ 9) is about 2 %, and koe-1 gave 5 behind paper. A student may read 9 as "alpha passes aluminium but not paper". Fix: say that 9 is an unusually high background reading, or change the seed so the value sits near 4.
- lesson.md:250 (HFIR caption). "hiukkaset kulkevat vedessä nopeammin kuin valo vedessä": the particles here are charged ones, mainly electrons. Fix: "varatut hiukkaset, lähinnä elektronit".
- lesson.md:488 (misconception). "Steriloinnissa ja lääketieteessä käytetty … energia ei riitä muuttamaan ytimiä" is not true of high-energy radiotherapy beams (about 15–18 MV), which cause photonuclear activation in the machine. The exit ticket already has the right condition ("tavanomaisessa steriloinnissa, esim. koboltti-60"). Fix: limit the sentence the same way, or add "tavallisesti".
- lesson.md:344. "Pienet annokset lisäävät syövän riskiä" states as fact what is a precautionary model at low doses. Fix: "Pienten annosten arvioidaan lisäävän syövän riskiä".

## Checked
- The script lessons/FY8/fy8-12/lesson-answers.py recomputes: n_i = 5,49 MeV / 34 eV ≈ 1,6·10⁵ ion pairs, about 3,9·10³ per mm over Geiger's 4,1 cm range; visible light 1,72–3,26 eV; m_α/m_e = 7294 (text says about 7300).
- Half-value thicknesses from XCOM at 662 keV: Pb 5,50 mm, Fe 12,0, Al 34,4, concrete 39,1, water 80,9 mm; concrete ÷ lead ≈ 7. μ = ln2/d½ is derived correctly.
- Worked example: d = d½ · ln(I₀/I)/ln 2 = 23,77 mm, rounded to 24 mm; the bracket check (4 and 5 half-value thicknesses) is valid. Siirto: 5,568 % (data d½ 0,12 mm matches XCOM Pb at 60 keV, 0,122 mm); its mistake values 84,7, 94,4 and 12,0 recompute.
- Tarkistus-2 figure: R = 800·(1/2)^(d/12) on a 2 mm grid, so 400 at 12 mm, 200 at 24 mm and 50 at 48 mm.
- Figure `vaimeneminen`: lead markers at 5,5, 11 and 16,5 mm give 1/2, 1/4, 1/8; aluminium reaches 0,600 at 25 mm. Energy-axis markers sit at 12,6 eV, 60 keV and 662 keV.
- Sim model: the beta μ = 6,6 cm²/g and range 1,1 g/cm² (about 4,1 mm Al) fit an E_max of 2,28 MeV; the gamma half-value thicknesses match the table. Every model value quoted in ennuste-1, ennuste-2 and johtopäätös matches the seeded counts (590/332/175/89/57, net ratios 0,56 and 0,29, estimated d½ 5,6 mm).
- Experiments: koe-1 and koe-2 vary only the source with material and thickness locked; koe-3 varies only the lead thickness. simState exposes `pulssit`. The model box states the limits (no alpha loss in air or window, every hit counted, no dead time, no bremsstrahlung, single-emitter sources).
- Photon interactions table: the dominance ranges for water and lead and the 1,022 MeV threshold are correct.
- Every choice item has exactly one correct option, and each distractor's feedback is right. The exit ticket agrees with the theory.
- The GM tube description, the background subtraction and the claim that a GM tube cannot identify the radiation type agree across the theory, the summary, tarkistus-3 and the glossary.
