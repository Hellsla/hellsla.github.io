VERDICT: PASS
CONTENT-HASH: 1bb1eedd78f766c7

## Blocking

## Polish
- lesson.md:276 figure label "source on line" — the theory, ennuste-1 and the sim say "line segment", and the point is that the source lies between the two detectors. "source on segment" would match; the dashed segment in the figure makes the meaning clear, so not an error.
- lesson.md:58 "for tungsten they are at about 59 keV" — K lines at about 59 (Kα) and 67 keV (Kβ). Write "at about 59 and 67 keV". Carried over.
- lesson.md:178 "the calcium atoms in it have many electrons" — the main cause is the larger atomic number (photoabsorption rises steeply with Z). Carried over.

## Checked
- inquiry.json koe-1: names "patient", "detection", "coincidences N" and values "one tumour", "coincidence" now match the sim's lang keys (kohde_1, ilmaisu_1); initial values, locked keys (kohde, ilmaisu), vary N and the measured key virhe are unchanged, so the experiment still isolates N.
- lang/en.json fy8-14 legend "Orange dot: annihilation photon. Line: segment between the detectors hit at the same time." is correct; ei_kuvaa_kanvas "no image" appears only in single-photon mode, where the readout correctly says only the detector is known.
- Figures (captures 6, 8, 12): the moved "bone" and "control" labels point at the right parts; the PET figure keeps 511 keV, 180° and e⁺ + e⁻ → γ + γ.
- Hash unchanged between start and end; no number changed in this diff.
