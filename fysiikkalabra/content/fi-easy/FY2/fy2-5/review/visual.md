VERDICT: FAIL
CONTENT-HASH: 40fdc2a8fe139053

## Blocking
- [Major] inquiry.json (prior, line 13; feedback, line 324) — the chapter references "(luku *Teho P = ΔE/Δt*)" were not updated to the new title "Teho: $P = \Delta E/\Delta t$" (fy2-3); in the intro-1280 capture the Pohjatiedot item shows it as plain italic text, without the link and without maths, while every other reference is a link — a stale reference that no longer resolves and breaks the formula-as-LaTeX rule — write "(luku *Teho $P = \\Delta E/\\Delta t$*)" in JSON (as the title in fy2-3 meta.json), in both places.

## Polish
- none

## Checked
batch delta review: intro-1280 (title "$E = Hm$" renders in KaTeX, no wrap problem), fig-row-1280; figures unchanged by the diff.
