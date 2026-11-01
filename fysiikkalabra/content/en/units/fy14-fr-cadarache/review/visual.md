VERDICT: PASS
CONTENT-HASH: dfd86936dde13656

## Blocking
(none) The earlier blocking finding is resolved. The plan's labels are now 32 units, which renders at 14.3 px at 390 px (measured). *le couloir* is now in ink, and every label fits its room.

## Polish
1. [Minor] *Role-play* word bank: the list "Je peux vous aider ?, Voici votre badge., C'est au premier étage., …" stacks punctuation (`?,` `.,`). Fix: separate the phrases with " / " or put them in a list.
2. [Minor] The summary table at 390: the shared `td{hyphens:auto}` rule hyphenates the English "sim-ple" and "under-stood". This is harmless.

## Checked
- Map at 390 and 1280. *le Rhône* now sits beside its line, *l'étang de Berre* is labelled and is in the aria-label, the labels measure 14.6 px, and the scale is unchanged and correct.
- Plan at 390 and 1280.
- The hero.
- The new role cards: four folds, each opened at 390, readable, with the roles named in the tag and the title.
- Directions table, dialogue, order and gapfills.
- A word-break audit at 360, 390 and 1280: no auto-hyphenated French, and no table is wide.
- No console errors.
- Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Re-check 2026-11-01: photographs
- Screenshots at 360, 768 and 1280 px (details opened, image loaded); check_layout.py OK at 360 and 1280 px; figure gaps 20 px above and 24 px below, no overflow, credit on its own line and legible.
- Distant ITER view fits; on a phone the buildings are a thin strip on the horizon under a large sky (a tighter crop would help, not blocking).
