VERDICT: PASS
CONTENT-HASH: ab4f0a6870837ccf

## Blocking
(none left)

## Fixed
- none needed

## Polish
- Terminology and decimal point consistent; no meaning changed.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): compared lesson.md, inquiry.json, exit-ticket.json, meta.json, figures.json, and the simulation labels with the Finnish source for meaning, physics terms, units, sign/causality, chapter titles, figure texts (each value translates its own key), and Selkeä suomi level without lowering the cognitive demand.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked lesson.md, inquiry.json (new check-c2 item, rewording of dilute-gas/measurement-uncertainty claims), exit-ticket.json (1 question) and figures.json (boyle-points) against the new Finnish.
- Update 2026-10-29 (sim LaTeX PR #132): sim.js lost the dial numbers and the gauge's kPa label; the reading with its unit ($p$ in kPa, one decimal) stands above the gauge and matches the readout and the graph's $p$ (kPa) axis. Every sims.fy3-9 key is present in lang/fi-easy.json with the same placeholders, units and LaTeX as the Finnish; the PR added or removed no key. Canvas captures at 390 and 1280 px: thermometer °C scale, $T$ in K, $V$ in ml, axis labels and the gauge reading render in KaTeX with no raw $ or missing keys. test_sims fy3-9 PASS in this language. No lesson text changed in the Finnish source or the translation since the last PASS.
