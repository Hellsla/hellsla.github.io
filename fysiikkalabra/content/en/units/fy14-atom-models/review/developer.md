VERDICT: DONE

Unit fy14-atom-models, "From Rutherford's nucleus to Bohr's atom" (FY14 chapter 1, order 3). Developer report 2026-11-01.
Content hash at hand-over: see `python3 scripts/units.py hash fy14-atom-models`.

## Files
- `content/en/units/fy14-atom-models/unit.json` — chapter 1, order 3, 10 sources checked 2026-11-01.
- `content/en/units/fy14-atom-models/unit.md` — Why question; hero; *The gold-foil evidence* {Foil} (figure `scatter`), *The spectrum of hydrogen* {Lines} (figure `lines`, link to the Fotoni spectra station), Key idea (nucleus size, classical instability), *Bohr's quantum atom* {Bohr} (figure `levels`), Formula: energy levels of hydrogen, staged Worked example (closest approach of an alpha particle to gold, 7 stages), Common misconception, optional *People in this story* {People} (Marsden, Bohr, 60–100 words, photo placeholders), Summary.
- `content/en/units/fy14-atom-models/inquiry.json` — 24 activities: hook (Thomson's model, Marsden's task; does not give the result), retrieval choice on photon energy (link to the photoelectric unit); two committed predictions (gold foil, `layout: models` → revealed by the Key idea section, after the *Foil* evidence; bigger jump → revealed by the *Bohr* section); paths-figure question; measured Balmer table (`source: measured`) with the red-line photon energy (1.889 eV, two mistakes); pair comparison of the two spectra (word bank, starters); theory; vocabulary `match`; reflect; optional biographies; worked example; numeric 5→2 jump (434 nm, three mistakes); optional find-error (one level instead of a difference); misconception; three checks; fusion explanation with starters; summary; French corner with `say`.
- `content/en/units/fy14-atom-models/teacher.md` — timing, fast pairs / short of time, organisation, assessment, difficulties, extensions.
- `lessons/units/fy14-atom-models/figures.py` — `hero` (glowing tube, grating, four lines on a screen; no text, no people), `scatter` (alpha paths integrated for a Coulomb force, to scale in fm, 50 fm bar), `lines` (measured Balmer lines on a 380–720 nm scale), `levels` (hydrogen levels to scale with Balmer and the first Lyman jump).

## Checks run
- `units.py figures` (up to date), `units.py check` (no error for this unit), `build.py fy14-atom-models`.
- `check_layout.py --width 360` OK, `--width 1280` OK (after separating the 410/434 labels).
- `screenshot.py` captures inspected; fixed the empty lower half of `scatter` (paths now on both sides), the λ label crossing the Lyman arrow in `levels`.
- Playwright: predictions lock without feedback and reveal after their theory sections (Key idea, Bohr); numeric answers accepted; explain models closed until text is written; match component checks; no console errors, no `.katex-error`, no raw `$`.

## Facts verified (WebFetch, 2026-11-01)
- Thomson's model 1904; large-angle scattering negligible in it — Wikipedia *Plum pudding model*.
- Geiger and Marsden 1909: zinc sulfide screen, microscope, darkened lab; about 1 in 8000 alpha particles turned back by a platinum reflector (>90°); Rutherford 1911; "15-inch shell … tissue paper" (1936 lecture); Rutherford's upper bound 27 fm; gold nucleus ≈ 7.3 fm; nucleus ≥ 10 000 times smaller than the atom; example speed 2e7 m/s, alpha mass 6.64e-27 kg — *Rutherford scattering experiments*.
- Marsden: born 1889 (Lancashire), 20-year-old undergraduate in 1909, Secretary of NZ DSIR from 1926, died 1970 — *Ernest Marsden*. Rutherford Manchester 1907, Cambridge 1919 — *Ernest Rutherford*.
- Bohr: July 1913 (trilogy July, September, November), Copenhagen, worked with Rutherford in Manchester 1912, institute opened 1921, Nobel Prize 1922 with its motivation, 1885–1962 — *Niels Bohr*, *Bohr model*. Levels −13.6 eV/n²; Balmer 1885, Rydberg 1888; failures for many-electron atoms; Larmor's radiating charge — *Bohr model*.
- Balmer wavelengths in air 656.279, 486.135, 434.0472, 410.1734 nm — *Balmer series*. Balmer a Swiss mathematician teaching at a girls' school in Basel — *Johann Jakob Balmer*. Gold Z = 79, atomic radius 144 pm — *Gold*. Fotoni spectra station (filament lamp and gas discharge tubes) — helsinki.fi.

## Numbers (Python; rounded constants as printed)
- Worked example: Ek = ½ · 6.64e-27 · (2.0e7)² = 1.328e-12 J (8.29 MeV); q1 = 3.204e-19 C, q2 = 1.266e-17 C; kq1q2 = 3.645e-26 J·m; d = 2.74e-14 m = 27 fm (exact constants 27.4 fm); atom/d = 1.44e-10/2.74e-14 ≈ 5250 ("about 5000"); 144 pm / 7.3 fm ≈ 19 700 ("about 20 000").
- Hydrogen (hc = 1240 eV·nm): 3→2 1.889 eV, 656.5 nm; 4→2 2.55 eV, 486.3 nm; 5→2 2.856 eV, 434.2 nm; 6→2 3.022 eV, 410.3 nm; 2→1 10.2 eV, 121.6 nm; 3→1 12.09 eV, 102.6 nm; 4→3 0.661 eV, 1876 nm. Red line 1240/656.3 = 1.889 eV (3.03e-19 J). Mistakes: E5 alone 2279 nm, E2 alone 365 nm, without squares 304 nm.
- Electron/alpha mass ratio 7290 ("about 7000").

## Open questions
- The "one in 8000" count was measured with a platinum reflector in 1909; the hook says the foils included gold, and the text says platinum for the number. The common textbook phrase "gold foil experiment" is kept as the section name.
- "The electron should … spiral into the nucleus" is given without a time (no source with a number was found in the sandbox).
- Photos: `<!-- photo: ernest-marsden -->`, `<!-- photo: niels-bohr -->`.

## Shared issues
- `assets/units/fy14/data/timeline.json` `bohr-model-1913` gives Manchester as the place of Bohr's 1913 model; it was Copenhagen (see the report of fy14-classical-limits, Shared issues 3).

## Fixes after review

Content hash after the fixes: 9aa351a8af4c0779.

- Science 1 / Pedagogy B1: pred-gold now asks "In 1909 Thomson's model was the best picture of the atom. What do you think Geiger and Marsden actually saw …?" The Thomson option's feedback opens "That is what Thomson's model predicts, … and it is what everyone expected. The experiment showed something else".
- Science 2: scatter aria-label: the atom is "about 600 times wider than this drawing".
- Science 3: Key idea says "a continuous spectrum" instead of "a smear of all wavelengths".
- Science 4 / Visual 5: worked example Reasonableness: "about 8.3 MeV (1.328·10⁻¹² J divided by 1.602·10⁻¹⁹ J/eV). This is within the range of alpha particles from radioactive decay, about 4–9 MeV." No long inline formula mid-sentence.
- Pedagogy B2: the photon-energy `review` task moved to Investigate, just before red-line. Think about it now has a pair talk (find out what is in a closed box by throwing marbles in), with neutral starters.
- Pedagogy P1: compare-spectra model uses *whereas* correctly.
- Pedagogy P2: back-to-predictions asks students to check that E₃ − E₂ gives their 1.89 eV.
- Pedagogy P3: teacher.md points weaker students to the hints and solution of the 5 → 2 task.
- Pedagogy P4: correct options of pred-gold, find-error and check-3 shortened; none is the longest.
- Visual 1: hero grating: four lines on each side of a dim central image, offset ∝ λ, so violet is nearest the centre and red farthest.
- Visual 2: levels: n = 3 and n = 4 labels nudged 5 units apart from each other with short leader lines to their own levels; n = 1 is "−13.6 eV".
- Visual 3: French *un* is *ẽ* (*ẽ-na-TOM*, *ẽ-ne-lek-TRÕ*); respellings in italics; convention sentence in the box.
- Visual 4: lines figure: ticks numbered 400–700, wavelengths above their lines.
- Visual 6: heading "Formula: Energy levels of hydrogen". Visual 7: b bracket in scatter has end ticks and sits clear of the paths.
- Given line equalities braced.
- Checks: units.py figures, units.py check, build.py, check_layout 360 and 1280 OK, browser test (all tasks, reveals, no KaTeX or console errors).
