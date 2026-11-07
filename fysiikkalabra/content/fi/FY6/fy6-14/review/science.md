VERDICT: PASS
CONTENT-HASH: c4df2de70c91f626
Mode: light (teacher 2026-11-07, "kevyt katselmointi": the editorial-correction diff since origin/main only)

## Blocking
- none

## Polish
- glossary.json:5165 irradianssi: "Se ei ole sama kuin fotometrinen valovoima" is true, but the photometric counterpart of irradiance is valaistusvoimakkuus (lx); naming that would be more precise. Optional.

## Checked
- Irradiance G defined as radiant power per unit area, W/m², in lesson, formula legend, summary, glossary (aurinkokenno, tyhjäkäyntijännite, new irradianssi), lang/fi.json sims.fy6-14.valo, sim-spec, inquiry and figure aria-labels; no "valon voimakkuus" left in fi fy6-14 or lessons/FY6/fy6-14. η = P/(GA) unchanged.
- LED: current must be limited; series resistor in a simple constant-voltage circuit, constant-current source in other devices; same in the Miksi question, theory, summary, inquiry explain model and criterion, glossary LED.
- Recomputed: 1000 W/m² · 0,0060 m² = 6,0 W; 0,92/6,0 = 15 %; (4,5 − 2,0) V : 1 Ω = 2,5 A, 125 × 20 mA.
- Lint: no physics warnings.
