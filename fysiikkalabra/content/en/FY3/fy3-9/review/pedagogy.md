VERDICT: PASS
CONTENT-HASH: 0f725d6d6618ffb0

## Blocking
(none left)

## Fixed
- inquiry.json exp-1 and exp-2 `names.mode` "tilanmuutos" left untranslated → "change of state".

## Polish
- Reads naturally; step labels and sim labels match the lang file.
- Sim readout and gauge use the Finnish decimal comma ("100,0 kPa", "50,0 ml") on the English page, as the shared sim.js does in every language; a language-aware decimal in the sims would be better (not a translation file).
- Experiment set-up lines show the raw sim values ("change of state: isoterminen/isobaarinen"): the Finnish word appears because check_i18n does not allow a `values` map in the translation.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): compared lesson.md, inquiry.json, exit-ticket.json, meta.json, figures.json, and the simulation labels with the Finnish source for meaning, physics terms, units, sign/causality, chapter titles, figure texts (each value translates its own key), and English naturalness.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked lesson.md, inquiry.json (new check-c2 item, rewording of dilute-gas/measurement-uncertainty claims), exit-ticket.json (1 question) and figures.json (boyle-points) against the new Finnish.
- Update 2026-10-29 (sim LaTeX PR #132): built preview/en/fy3-9.html and looked at the simulation at 390 px: the gauge has no dial numbers, the reading with its unit (100,0 kPa) stands above it, KaTeX labels (T, p axis, V, thermometer scale, readout) are legible with no overlap; all texts match the Finnish and nothing is missing.
