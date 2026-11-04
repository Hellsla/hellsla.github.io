VERDICT: PASS
CONTENT-HASH: 36602805dfdc3f5a

## Blocking

## Polish
- lesson.md:569 (Tiivistelmä) and the alkuaineet figure — heavier-than-iron elements are attributed only to supernovae and neutron-star mergers; about half (e.g. Sr, Ba, Pb) come from slow neutron capture in giant (AGB) stars. Line 374 is fine for gold and uranium — consider "neutronisieppauksessa jättiläistähdissä, supernovissa ja neutronitähtien törmäyksissä".
- lessons/FY8/fy8-16/lesson-answers.py:29 — comment says fit-H0 "69,7"; the computed least-squares slope is 69,83 (sim-spec says 69,8) — fix the comment.

## Checked
- H₀ = 70 km/s/Mpc; 1/H₀ = 3,086·10¹⁹ km / 70 km/s = 4,41·10¹⁷ s = 1,40·10¹⁰ a; 1 Mpc ≈ 3,26·10⁶ ly; tarkistus-2 1/72 → 13,6·10⁹ a.
- z = Δλ/λ₀, v = cz stated for z < 0,1 in Kaava, Esimerkki (z = 0,035) and the sim's model box; sim galaxies z = 0,0060–0,0635, hubble-t figure z ≤ 0,07.
- Sim table recomputed: v = 70d + own motion, λ(Hα) 660,2–698,0 nm; least-squares slope through origin 69,83 → numeric answer 70 ± 7 % right; odd galaxies above, even below the line (solution correct); 19 030/275 = 69,2.
- Recombination wording correct: at ≈3000 K photons with ≥13,6 eV "ei enää ollut tarpeeksi" (number argument, not mean energy); stretch 3000/2,725 = 1101; Wien 1,06 mm; release light near-IR (966 nm).
- BBN: n:p = 1:7 → Y = 2/8 = 25 %; 10⁹ K at ~3 min, freeze-out ~20 min; He-4 most tightly bound light nucleus.
- Stellar fusion to Fe-56 (≈8,8 MeV, C-level vs Ni-62), triple-alpha Q = 7,274 MeV, supernova core collapse, r-process for gold (tarkistus-3 model answer and criteria).
- Dark matter (rotation curves, cluster dynamics, lensing; non-baryonic from BBN + CMB) and dark energy (1998 SNe, acceleration); Planck 2018 4,9/26,2/68,9 % → 5/26/69 %; Hubble tension stated as open.
- Hook 669,4 / 495,8 nm (z = 0,0200), spektri figure 689,1 nm, Esimerkki 10 506 km/s, 70,0 km/s/Mpc; siirto 86,0 Mpc and mistakes 84,3, 8,6·10⁴, 6020.
- Predictions, virhe, tarkistus-1: exactly one correct option, distractor feedback correct; ennuste-1 feedback numbers match the sim.
- Sim code implements λ = λ₀(1+z), z = v/c, 1/H₀ conversion; exaggerated wave stretch disclosed.
