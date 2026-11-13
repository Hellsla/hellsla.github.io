VERDICT: PASS
CONTENT-HASH: a71711e7c0c92d0d

## Blocking

## Polish
- lesson.md:522 — "lääketieteessä käytetty gamma-, röntgen- ja elektronisäteily … Sen energia ei riitä muuttamaan ytimiä" is true for imaging, Co-60 and sterilisation beams (under about 10 MeV). It is not quite true for 15–18 MV radiotherapy beams, which cause slight photonuclear activation. Holds as a fair simplification (C). A tighter version: "röntgenkuvauksessa ja steriloinnissa käytetty".
- inquiry.json:64 (ennuste-1) and koe-2 — in the model values, the alpha source behind 5 mm of aluminium gives 9 pulses, against a background mean of 4 (P(N ≥ 9) ≈ 2 %) and 5 behind paper. "Satunnaisvaihtelun rajoissa" is defensible, but a student may read it as alpha getting through the aluminium. A different seed term for this one setting would remove the doubt, but it is not needed.
- inquiry.json:329 (siirto) — the task uses one half-value thickness for a dental X-ray spectrum, and the solution says "jokaisella fotonilla … sama todennäköisyys". That is strictly true only for one photon energy. Fair at this level because the task gives d½ "tälle säteilylle" and a narrow beam. An optional half-sentence would cover it: "oleta, että puoliintumispaksuus pysyy samana".

## Checked
- One script recomputed every number of the lesson and the inquiry with my own formulas, and every number agrees:
  - ionisation: W = 34 eV, Am-241 5,49 MeV → 1,6·10⁵ ion pairs, ≈ 3,9·10³ per mm, range 4,1 cm in air;
  - photon energies: visible 1,72–3,26 eV, water 12,6 eV;
  - the worked example: 23,77 → 24 mm, with checks of 6,25 % and 3,1 %;
  - siirto: 5,57 %, and its mistake values 84,7, 94,4 and 12,0;
  - tarkistus-2: 12 mm, 24 mm and 50 pulses per minute at 48 mm, read off the figure.
- Half-value thicknesses at 662 keV come from XCOM μ/ρ: Pb 5,50, Fe 11,99, Al 34,4, concrete 39,1 and water 80,9 mm. The concrete-to-lead ratio is ≈ 7. Lead at 60 keV gives 0,122 mm.
- The ranges where each photon interaction dominates are right: water < 0,03 MeV and 0,03–25 MeV; lead < 0,5 MeV and 0,5–5 MeV. The pair-production threshold is 1,022 MeV.
- The sim model is right:
  - beta: μ/ρ = 6,6 cm²/g and range 1,1 g/cm² (Katz–Penfold for 2,28 MeV), so ≈ 4 mm of Al;
  - gamma follows the narrow-beam law, and alpha has T = 0 behind any absorber;
  - the limits are stated in the Mallin oletukset box (no energy loss in air or the window, single-species sources, no bremsstrahlung, ideal GM tube, no dead time).
- sim.js `trans`, its seeding and the slot loop are the same as the Python port in lesson-answers.py. Every model value quoted in the feedback, the model answer and sim-spec matches the k = 1 counts: 5/550/577, 9/4/535, and 590, 332, 175, 89, 57; nets 586, 328, 171 and the ratio 0,29.
- Experiments: koe-1 and koe-2 lock the absorber and n and vary the source; koe-3 locks the source and the absorber and varies n. `simState.pulssit` exists, and changing a control aborts the count and resets k, so the first count is reproducible.
- Figures, checked against their coordinates: `energia` (log axis at 50 px per decade, markers at 12,6 eV, 60 keV and 662 keV) and `vaimeneminen` (Pb points at 5,5, 11 and 16,5 mm; Al 0,60 and Pb 0,043 at 25 mm). Both are to scale as their labels claim.
- Every choice item has exactly one correct option, and each distractor's feedback repairs its misconception correctly. Checked: kertaus, ennuste-1, ennuste-2, virhe, tarkistus-1.
- GM tube physics (avalanche, pulses of the same size, background, identifying the type with absorbers under a stated condition) is consistent across the theory, tarkistus-3, the summary and the glossary.
- The biological effects are explained through ionisation (direct effect, radicals, double-strand breaks, internal versus external sources). The total-risk caveats are stated, and the content is within FY8's central contents.
- The exit ticket agrees with the theory: photon energy versus brightness, and sterilisation does not activate.
