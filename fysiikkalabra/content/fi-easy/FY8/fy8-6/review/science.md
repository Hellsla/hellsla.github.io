VERDICT: PASS
CONTENT-HASH: 2b8e0609a3a68cbe

## Blocking

## Polish
- lesson.md:162 — added gloss "Fotoni on valon pienin energiamäärä." reads as one universal smallest amount of light energy; the photon's energy depends on the frequency (red smaller than blue, as the next paragraph says) — "Fotoni on pienin energia-annos, jonka tietyn taajuuden valo voi luovuttaa; sen energia on $hf$." (C-level wording, not blocking; matches the fy8-1 glossary sense once the frequency is named).

## Checked
- Numbers and JSON structure (correct flags, answers, tolerances, mistakes, initial/locked/vary) identical to the passed Finnish source in lesson.md, inquiry.json, exit-ticket.json; only wording differs.
- Recomputed in one script: 1240 V nm, red 1,97 eV / blue 2,64 eV, worked example h = 6,515e-34 J s (−1,7 %), six-LED fit k = 4,054e-15 V s, b = −0,050 V, h = 6,49e-34 J s (−2,0 %), siirto 954 nm, tarkistus-2 6,675e-34 J s, exit 3,06 V.
- Sim model I = (s/R)ln(1+e^{(U−U_k)/s}): koe-1 currents 17,8 / 13,9 / 11,1 / 0,11 / 0 / 0 mA, koe-2 table and extrapolation 1,88 V (slope 55,5 mA/V) match feedback, hints and solution; sim.js uses the same s, R, U_k.
- Ennuste 1 and 2: exactly one correct option; distractor feedback (LED is not a resistor; current keeps rising above U_k) correct.
- Etsi virhe: offset (≈ −0,1 V, thermal energy and extrapolation definition) shifts intercept, not slope; λ-axis distractor correctly rejected (U_k ∝ 1/λ).
- Causality: photon energy set by the band gap, not by U; excess energy to heat; brighter, not bluer, at higher U — stated consistently in theory, misconception, tarkistus-1 and model answers.
- Spectra: lamp continuous, LED 20–40 nm band, laser diode ≈ 1 nm; laser-eye warning kept.
- Figure "ryhma" (check 2): line passes (4,6; 1,80) and (7,0; 2,80) on the shot; slope 4,17e-15 V s.
- meta.json key_concepts (valodiodi, laserdiodi, kynnysjännite, energia-aukko): physically correct and consistent with the glossary.
