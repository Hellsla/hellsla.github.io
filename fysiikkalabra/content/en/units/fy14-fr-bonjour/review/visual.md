VERDICT: PASS
CONTENT-HASH: edd56ca7362d855c

## Blocking
(none) Both earlier blocking findings are resolved:
- The opening illustration has no text: empty bubbles with three dots, and the aria-label is updated.
- French is no longer hyphenated: the summary table shows "appelez-vous" and "venez-vous" unbroken at 390.

## Polish
1. [Minor] Reflection list (`back-to-predictions`, `stage-selita-390-4`). The quoted predictions end with the meta instruction "Commit now; the theory summary will show you.", which reads oddly once the theory has been shown. Fix: move that sentence out of the prompt into the predictions' lead, or have the shared component quote only `.ask`.
2. [Minor] Summary table at 390: the English column wraps to three lines in several rows ("I come / from / Finland."). Acceptable; an optional `th:first-child{width:30%}` would balance it.

## Checked
Fresh build and captures for this hash: top-390/1280 and intro-390/1280. The hero has no words, and the paragraph below it now has a gap. Every stage at 390 and 1280, all eight components (say, dialogue, order, gapfill, match, classmate say and gapfill), sources, teacher. The respelling convention in *Sounds for Finnish speakers* and the tips: italic, capitals for stress, õ/ã/ẽ for nasals, explained once. The gapfill gap is now `appelez-vous` with no detached hyphen. "Je m'appelle …" keeps its ellipsis together. Check-1 is the new group *vous* transfer. French no-break spaces are intact. Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4
