VERDICT: PASS
CONTENT-HASH: 1c8e4b98816f56ec

## Blocking

## Polish
- lessons/FY8/fy8-2/sim-spec.md:1 — the absorption mode is still described as "lampun valkoinen valo kulkee kylmän vetykaasun läpi", although the sim now labels the cell cold only when n_a = 1 and hot otherwise. Write "vetykaasun läpi (kylmä, kun n_a = 1; kuuma, kun n_a > 1)" so that the spec matches sim.js:143 and the howto.
- lesson.md (Energiatilat selittävät viivat) — "osa vetyatomeista on ensimmäisessä viritystilassa" is fair (C). The fraction is tiny (about 10⁻⁸ at 5800 K), so "pieni osa" would avoid suggesting a large share.

## Checked
- Round 1 blocking items are fixed. Hero: the prism is apex-down and the fan bends toward the base, with violet (most deviated) on top on both the fan and the screen. ennuste-2 feedback now says absorption depends on which levels are occupied. The sim labels the cell "kylmä/kuuma vetykaasu" by n_a, and the howto and model say so. The greenhouse range is now 0,08–0,5 eV (CO₂ 15 µm 0,083, 4,3 µm 0,288; H₂O 6,3 µm 0,197, 2,7 µm 0,459 eV).
- Round 1 polish is done: the lamp-ID feedback has a correct "all lines of the element / no unexplained line" rule; syncNy disables n_y ≤ n_a, so the experiments never record ΔE = 0; and "voimakkaimmat näkyvät viivat" with 7→2 at 397,1 nm.
- I recomputed everything in one script, and it agrees with lesson-answers.py: Balmer 656,5/486,3/434,2/410,3 nm, gaps 170/52/24 nm, Lyman 121,6–93,8 nm (the sim's readout rounds them to 122/103/97/95/94), retrieval 1,91/3,02 eV, example 1,9375 eV, Etsi virhe 1,05·10⁻²⁵ "m" → 656 nm, siirto 0,7221 eV (mistakes 9,92/3,06/2,34/−0,722), check 2 2,2711 eV (3,64, 0,440).
- Spectra figure: 1 px/nm, and its lines sit at 410,5/434/486,5/656,5 nm. Levels figure: 22 px/eV for every level. Fluorescence figure: 55,9 px/eV, with 365 nm = 3,40 eV and 520 nm = 2,38 eV.
- Lamp figure: the lines are at Hg 405/436/546/577–579 nm. Exactly one option is correct, and every distractor's feedback is right.
- Predictions 1–2: exactly one correct option each. The experiments lock tila and n_a and vary n_y, and simState gives dE and lam.
- sim.js: E_n = −13,6/n², λ = hc/ΔE with the lesson's constants, and the region limits are 380/750 nm. Line colours are intended.
- The misconception box (exact energy, the ionisation exception, re-emission in all directions), the greenhouse mechanism (collisions, emission downward) and the fluorescence mechanism are all correct.
- Exit ticket: three lines of 1,0/2,0/3,0 eV, and 400 nm emission after 450 nm absorption is ruled out by energy. The helium 1868 model answer is correct.
- The exercise set is identical to the one reviewed in exercises/review/science.md.
