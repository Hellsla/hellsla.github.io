VERDICT: PASS
CONTENT-HASH: a6beba555e576d2c

## Blocking
(none left; list what you fixed under Fixed)

## Fixed
- lang/en.json sims.fy2-4.otettu_teho, tehot, energiat — readouts used $P_\text{in}$, $P_\text{use}$, $P_\text{loss}$ (and E_…) while the lesson, the canvas labels and the experiment questions use $_\text{o}$, $_\text{a}$, $_\text{h}$ → now o/a/h, so the readout matches $E_\text{h} : E_\text{o}$ in Experiment 1

## Polish
- inquiry.json activities[5]/[6] `values.laite` ("auton bensiinimoottori", "hehkulamppu") still show Finnish in the en "Initial state" line; check_i18n rejects translating `values` (not a text key) — needs `values` added to check_i18n.TEXT_KEYS, then translate.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md (all prose, worked example steps, misconception, summary; decimals, \cdot, chapter reference *Power P = ΔE/Δt*), figures.json, meta.json, exit-ticket.json, inquiry.json (all activities incl. experiment intros/names, hints, feedback, solutions) and the sim's en labels; physics, signs, ratios and numbers match the Finnish.
- Update 2026-10-28: experiment option words (`values`) translated to match the English sim labels; re-hashed.
