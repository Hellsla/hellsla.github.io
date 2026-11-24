VERDICT: PASS
CONTENT-HASH: 32f374343d0b2f9a

## Blocking

## Polish
- lesson.md:268 (basalt caption) — "Jäähtynyt pinta on harmaa, koska se säteilee lähes vain infrapunaa" gives the wrong reason for the colour. The pattern is right, but the grey comes from reflected daylight; the infrared emission only explains why the crust does not glow — e.g. "Jäähtynyt pinta ei hehku, koska se säteilee lähes vain infrapunaa; harmaa väri on heijastunutta valoa."
- inquiry.json siirto solution — "kolme merkitsevää numeroa kuten lämpötilassa 2430 °C": the temperature the law actually uses is 2703 K. Better to name the limiting datum as "noin 2430 °C" (about ±10 °C), which gives three figures.
- lesson.md:190 / antenna figure — the figure draws the near field E parallel to and in step with the current I at the same instant. That is acceptable for a principle figure, but the caption could avoid suggesting a phase relation.

## Checked
- I recomputed every number in one script with my own formulas (analytic Planck peak x = 4,965, Simpson integral of the visible share) and compared them with lesson-answers.py. All agree: FM 3,0 m; 12 cm; 9,66 / 9,44 / 3,62 µm; 502 nm; 5773 K; 2,47 vs 3,22 µm; 1072 / 1193 nm; 1380 K → 1106,85 °C; 4,3 and 7,5 · 10¹⁴ Hz; 19-fold ratio.
- Curves figure (stated to scale): peaks 483 / 580 / 724 nm and heights 100 / 40,2 / 13,2 MW/(m²·µm). The pixel positions match the axes, and so does the visible band 380–750 nm.
- Spectrum figure: the log axis puts 97,5 px per factor 10³. Every region boundary (1 m, 1 mm, 750 nm, 380 nm, 10 nm, 0,01 nm) and the zoomed 400–700 nm ticks are placed correctly.
- Wave figure: E and B are in phase, perpendicular to each other and to the direction of travel, and E × B points along c. λ is marked between neighbouring crests.
- sim.js: Planck M_λ (exact SI constants), λ_max from a golden-section search rather than from Wien's law, visible share as ∫M_λ/σT⁴, glow from 800 K. The 1280 px capture shows 500 nm and 43,9 % at 5800 K, and the 390 px koe-2 capture shows 9659 nm and "alle 0,01 %" at 300 K. Both match my values.
- koe-1/koe-2: the range is locked and T is the only variable. All required temperatures can be set on the 100 K slider steps, and every peak falls inside its locked range. simState carries lmax in nm.
- Predictions: exactly one correct option in each, and every distractor's feedback gives the right model values and the mechanism.
- virhe, siirto, tarkistus-2: the mistakes match the real errors and the hints lead to the answer. The worked example is solved symbolically first, with 3 significant figures for a reason given and the IAU 5772 K check.
- Wien's law is stated as holding for a black body, approximately for real bodies, with T in kelvins. Stefan–Boltzmann's 16× is stated for a black body. Radiation from an accelerating charge is labelled classical, and the scope stays in FY7, with the photon left to FY8.
- Explain model answers, the exit ticket and the summary agree with the theory.
