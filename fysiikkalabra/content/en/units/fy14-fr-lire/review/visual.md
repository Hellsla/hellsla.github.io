VERDICT: PASS
CONTENT-HASH: ad7141695fb701d6

Delta review: unit.md "Why you understand more than you think", first sentence now "You can already recognise many French words, especially through English, Swedish and international scientific vocabulary." Previous PASS hash: f5bc3f119dc791ac.

## Blocking
(none)

## Polish
(Carried over from the previous report, not part of this diff: News texts can still separate a number from its unit at a line break; use a no-break space.)

## Checked
- Built preview and scripts/screenshot.py fy14-fr-lire --lang en (47 captures). Opened the paragraph at 390 px (lire-390-0): the italic French and Swedish examples (trottoar, parapluie, byrå, bureau ...) wrap between whole items, `lang="fr"` spans unchanged, no clipping, no horizontal scroll. The new sentence is accurate in tone (no longer "thousands ... without having studied them") and flows into the examples. Diff read: only this sentence changed.

## Scores
illustrations 5 · typography 5 · English 5 · accessibility 4
