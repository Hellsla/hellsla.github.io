VERDICT: PASS
CONTENT-HASH: 302f1baa0ebd6ce9

## Blocking

## Polish
- lessons/FY8/fy8-2/lesson-answers.py:33 — the comment says 3,1037e-19 J, but h·c/640 nm = 3,1039e-19 J, which is what the worked example shows. Correct the comment so that the generator matches the lesson.

## Checked
- Round 2 polish is done. sim-spec.md now says the gas is cold when n_a = 1 and hot when n_a > 1, which matches sim.js and the howto. The lesson now says "pieni osa vetyatomeista" for the solar atmosphere.
- I recomputed everything in one script, and it agrees with lesson-answers.py. Balmer lines: 656,5/486,3/434,2/410,3 nm, gaps 170/52/24 nm, 7→2 at 397,1 nm. Lyman lines: 121,6–93,8 nm (10,2–13,22 eV). Retrieval: 1,91/3,02 eV. Example: 3,1039·10⁻¹⁹ J = 1,9375 eV. Etsi virhe: 1,05·10⁻²⁵ "m", and 656 nm once converted. Siirto: 0,7221 eV, with mistakes 9,92/3,06/2,34/−0,722. Check 2: 2,2711 eV, with mistakes 3,64 and 0,440.
- Figures, measured from the SVG coordinates. Spectra: 1 px/nm, and every line sits at its Balmer wavelength in both emission and absorption. Levels: 21,99 px/eV, so every level is to scale. Fluorescence: 55,9 px/eV, with 365 nm = 3,40 eV and 520 nm = 2,38 eV. Lamp figure: Hg 405/436/546/577/579 nm. Hero: the prism is apex-down, so violet is deviated most and appears at the top. The real line colours are intended.
- Greenhouse box: CO₂ 15 µm = 0,083 eV, 4,3 µm = 0,288 eV; H₂O 6,3 µm = 0,198 eV, 2,7 µm = 0,459 eV. These fit the 0,08–0,5 eV range. The mechanism (absorption, transfer by collisions, emission in all directions) is correct.
- Absorption physics: the lesson says absorption needs an occupied lower level. Cold H absorbs only in the UV, and hot stellar atmospheres populate n = 2, which gives the dark 656 nm line. Theory, ennuste-2, the sim labels and the model answer all agree.
- Misconception box: a photon must have exactly the energy difference unless it ionises the atom, and re-emission in all directions leaves the line darker but not black. Both are correct (C).
- Predictions 1–2, kertaus, lamp ID, Etsi virhe and tarkistus-1 each have exactly one correct option, and every distractor's feedback is physically right.
- Experiments: koe-1 locks tila = emissio and n_a = 2; koe-2 locks absorptio and n_a = 1. Each varies only n_y, and simState gives dE and lam. syncNy prevents ΔE = 0.
- sim.js: E_n = −13,6/n² and λ = hc/ΔE with the lesson's constants. The visible band is 380–750 nm. The 80–900 nm strip holds all Lyman lines, and lines above 900 nm (Paschen 1094/1875 nm) show as an edge arrow. The model box states the simplifications (no brightness, one atom).
- Exit ticket: the three lines are 1,0/2,0/3,0 eV, and 400 nm emission after 450 nm absorption is correctly ruled out. The helium 1868 model answer is correct. Scope: E = hf, the eV conversion is shown, and the H levels are given as data.
