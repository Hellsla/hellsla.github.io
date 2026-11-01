VERDICT: DONE

Unit fy14-quantum-tunnelling, "Waves, probability and quantum tunnelling" (FY14 chapter 1, order 4). Developer report 2026-11-01.
Content hash at hand-over: see `python3 scripts/units.py hash fy14-quantum-tunnelling`.

## Files
- `content/en/units/fy14-quantum-tunnelling/unit.json` — chapter 1, order 4, 9 sources checked 2026-11-01.
- `content/en/units/fy14-quantum-tunnelling/unit.md` — Why question; hero; *Electrons one at a time* {Slits} (figure `slits`, link to the Fotoni double-slit station), *Through the wall* {Tunnel} (figure `barrier`, model table of tunnelling chances, evidence: alpha decay, STM, flash memory), Key idea (duality, Born's probability), Formula: the de Broglie wavelength, *Tunnelling and the Sun* {Sun} (figure `sunbarrier`; link to chapter *The Energy of the Stars*), staged Worked example (electron at 100 V, 7 stages), Common misconception, optional *People in this story* {People} (Louis de Broglie), Summary.
- `content/en/units/fy14-quantum-tunnelling/inquiry.json` — 24 activities: hook (the Sun's "too cold" core), retrieval choice (closest approach, link to the atom unit), pair talk; two committed predictions (single-electron double slit → revealed by the Key idea section, after the *Slits* evidence; a too-high barrier → revealed by *Tunnelling and the Sun*, after the *Tunnel* evidence); pair task *Particle or wave?* (word bank, starters); factor task on the model table (13, two mistakes); theory; vocabulary `match`; *Tunnelling and the Sun*; reflect; optional biography; worked example; numeric proton wavelength in the Sun (779 fm, three mistakes); optional transfer choice (tennis ball); misconception; three checks; explanation for a younger student with starters; summary; French corner with `say`.
- `content/en/units/fy14-quantum-tunnelling/teacher.md` — timing, fast pairs / short of time, organisation, assessment, difficulties, extensions.
- `lessons/units/fy14-quantum-tunnelling/figures.py` — `hero` (sunrise; a lens shows two blurred protons; no text, no people), `slits` (30, 300, 3000 simulated hits from the two-slit intensity, labelled "simulated"), `barrier` (schematic wave through a barrier, labelled "schematic"), `sunbarrier` (log–log: k e²/r for two protons, k_BT = 1.35 keV, turning point 1060 fm, 720 keV at 2 fm).

## Checks run
- `units.py figures` (up to date), `units.py check` (no error for this unit), `build.py fy14-quantum-tunnelling`.
- `check_layout.py --width 360` OK, `--width 1280` OK (after moving a figure label and splitting two long formulas).
- `screenshot.py` captures inspected (hero, figures, stages, components, French corner).
- Playwright: predictions lock without feedback and reveal after Key idea / *Tunnelling and the Sun*; numeric answers accepted; explain models stay closed until text is written; match checks; no console errors, no `.katex-error`, no raw `$`.

## Facts verified (WebFetch, 2026-11-01)
- Young 1801–1803; Taylor's low-intensity experiment 1909; single-electron build-up, Merli, Missiroli and Pozzi 1974 — Wikipedia *Double-slit experiment*.
- Davisson and Germer, electron diffraction published 1927; G. P. Thomson and Reid 1927 — *Davisson–Germer experiment*.
- de Broglie: Dieppe 1892 – Louveciennes 1987, House of Broglie (noble family), history degree 1910, thesis 1924 *Recherches sur la théorie des quanta*, Nobel Prize 1929 "for his discovery of the wave nature of electrons" — *Louis de Broglie*.
- Born rule, July 1926 — *Born rule*.
- Gamow and Gurney & Condon 1928 (alpha decay); STM Binnig and Rohrer 1981, Nobel 1986; flash memory; exponential dependence on width, height and mass; tunnelling essential for stellar fusion — *Quantum tunnelling*.
- Atkinson and Houtermans 1929, first calculation of stellar fusion — *Fritz Houtermans*. Average proton waits 9 billion years; tunnelling through the Coulomb barrier — *Proton–proton chain*. Core 15.7 MK, age 4.6 billion years — *Sun*. Fotoni double-slit station with single photons — helsinki.fi.

## Numbers (Python)
- k_B · 15.7 MK = 1353 eV ("1.35 keV"); k e² = 1.440 MeV·fm; at 2 fm 0.720 MeV; ratio 532 ("more than 500"); classical turning point 1.440 MeV·fm / 1.353 keV = 1064 fm ("about 1000 fm", figure "1060 fm").
- Tunnelling model values T ≈ exp(−2κd), κ = √(2 m_e · 1 eV)/ħ = 5.123 nm⁻¹: 0.25 nm 7.72 %, 0.50 nm 0.596 %, 0.75 nm 0.0460 %, 1.00 nm 0.00355 %; step factor e^{2κ·0.25 nm} = 12.96; 0.60/0.0035 ≈ 170. Factor task 7.7 : 0.60 = 12.8 → 13; mistakes 7.1 (difference) and 0.078 (inverse).
- Worked example: Ek = 1.602e-17 J; 2mEk = 2.919e-47; p = 5.402e-24 kg·m/s; λ = 1.227e-10 m = 0.123 nm; v = 5.93e6 m/s (2 % of c).
- Proton: Ek = 2.163e-16 J; 2mEk = 7.237e-43; p = 8.507e-22; λ = 7.79e-13 m = 779 fm; mistakes 24 630 fm (eV for keV), 1102 fm (no factor 2), 33 380 fm (electron mass).
- Tennis ball λ = 6.626e-34 / (0.057 · 50) = 2.3e-34 m.

## Open questions
- The table of tunnelling chances uses the simple estimate exp(−2κd) (stated in teacher.md); it is labelled approximate model values.
- "A typical kinetic energy of the order of k_BT": the mean is 3/2 k_BT ≈ 2 keV; the text says "of the order of" on purpose.
- Photo placeholder `<!-- photo: louis-de-broglie -->`.

## Shared issues
- None new beyond those reported in fy14-classical-limits (build.py data embedding from inquiry.json; timeline strip vs check_layout; Bohr's place in timeline.json).

## Fixes after review

Content hash after the fixes: 52dad39318ce6af1.

- Science 1 (a): "within a few femtometres, where the strong nuclear force acts" (also in the sunbarrier aria-label).
- Science 1 (b) / Pedagogy 4: the Sun section now says that tunnelling only lets two protons get close; two protons alone cannot stay together, fusion needs one to turn into a neutron, p + p → d + e⁺ + ν, a slow process of the weak interaction, so an average proton waits about 9 billion years.
- Science 1 (c): check-3 correct feedback: "An average proton still waits about 9 billion years, also because the first step, p + p → d + e⁺ + ν, needs the weak interaction." check-explain model says the protons "come close enough to fuse" and "roughly 1000 fm" (Science 4).
- Science 2: "Gamow's tunnelling (1928) solved the puzzle." Science 3: "an electron biprism, which acts like two slits".
- Pedagogy 1–2: pred-tunnel stem: "The barrier is then made twice as wide. What do you predict?" Options rewritten around width (classical bounce, far rarer [correct], half as often, equally often); feedback uses 7.7 % → 0.60 % (about 13 times less).
- Pedagogy 3: proton-wave Reasonableness compares 779 fm with the turning distance of about 1000 fm.
- Pedagogy 5: check-3 correct option shortened ("… huge numbers of them.").
- Visual 1: sunbarrier: the green strip is labelled "strong force" with an arrow.
- Visual 2: the unit chain C·V = J = kg·m²/s² is its own display line after "Check the units:"; the next sentence starts with "So".
- Visual 3: kg² · m²/s² with a dot, in the worked example and the proton task. Visual 4: heading "Formula: The de Broglie wavelength".
- Visual 5: barrier figure: E at the right end of the dashed line, "barrier top" label at the top edge; sunbarrier top tick "10 000".
- Visual 6: Given equalities braced.
- French respellings in italics, with the convention sentence in the box (this unit has no *un*).
- Checks: units.py figures, units.py check, build.py, check_layout 360 and 1280 OK, browser test (all tasks, reveals, no KaTeX or console errors).
