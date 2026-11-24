VERDICT: PASS
CONTENT-HASH: 4612c17ebdb6e5fc

## Blocking

## Polish
- lesson.md:168 — The basalt caption says the solid surface "näyttää harmaalta, koska se säteilee lähes pelkästään infrapunaa". It looks grey because it reflects daylight. Its emission being almost all infrared only explains why it does not glow. — Write "ei hehku, koska se säteilee lähes pelkästään infrapunaa".
- inquiry.json:110 (`calc`), :330 (tarkistus-2 Kaava step) — "$t = T - 273{,}15\,\text{K}$ celsiusasteina" mixes units: the result is in kelvins, not °C. — Write the numeric relation, e.g. "$t$ celsiusasteina on $T$ kelvineinä miinus $273{,}15$", or keep it as in tarkistus-2's Sijoitus step, $t = (1380 - 273{,}15)\,{}^\circ\text{C}$.
- inquiry.json:276 (siirto Vastaus) — "kolme merkitsevää numeroa kuten lämpötilassa $2430\,{}^\circ\text{C}$": under the house rule (P7) the trailing zero counts, so 2430 has four significant figures. The real reason for three is the task's "noin". — Give "noin" as the reason for three figures.

## Checked
- Recomputed in one script with my own formulas and printed beside lesson-answers.py: FM $3{,}0\,\text{m}$, microwave $12\,\text{cm}$; Wien peaks at 300, 307, 800, 2900 and 5772 K; worked example $5773\,\text{K} \to 5{,}77 \cdot 10^3\,\text{K}$; virhe 2,47/3,22 µm and 2,61 m; siirto 1072 nm with both mistake values (1192,59 and 1,07208); tarkistus-2 1380 K → 1107 °C with mistakes 1380 and 1653,15; kertaus 4,3/7,5 · 10¹⁴ Hz. All agree.
- Peaks by the Wien root x = 4,965: 300 K 9659 nm, 3000 K 966 nm, 6000 K 483 nm, so λT = 2,898 · 10⁻³ m·K. These match the option feedback and the conclusion's model answer. The visible share at 300 K is about 10⁻²¹ %, so "alle 0,01 %" holds.
- Curves figure (stated to scale): peaks at 483, 580 and 724 nm with heights 100, 40,2 and 13,2 MW/(m²·µm). Spot values at 1000 nm match Planck within 1 %, and the visible band sits at 380–750 nm.
- Spectrum figure: log scale and region boundaries placed correctly; the visible inset is linear, red at 750 nm.
- Wave figure: E and B in phase, both perpendicular to the propagation direction, with E×B along +x; λ is marked between two peaks. Antenna figure: the field reverses every half wavelength.
- Simulation: Planck M_λ with exact constants, a golden-section peak search over 50 nm–50 µm that covers the slider's 200–10 000 K, visible share as the 380–750 nm integral divided by σT⁴, and the vertical scale following the highest point inside the range. Its boxes state the model and its limits, and it calls its numbers model values.
- Experiments: koe-1 (lyhyt range, T 3000/4500/6000) and koe-2 (pitkä range, 300 K and 600–900 K) lock the range, vary only T, and simState gives `lmax`. Every peak falls inside its range.
- Exactly one correct option in each choice item; the distractor feedback is right.
- The hehkulamppu reasonableness check is valid: 25 % of black-body power lies below λ_max, so a peak above 750 nm means most of the power is infrared.
- Scope: Stefan–Boltzmann appears only qualitatively; the photon is left to FY8; the classical source model is labelled as classical.
