VERDICT: FAIL
CONTENT-HASH: d34eff70d761834f

## Blocking
1. [Major] `unit.md`, table *Counting to 100* (70–100), at 360 px. This is the one wide table that scrolls, and I judge it **not acceptable**. The table is 345 px wide in a 326 px box. The cut falls inside the maths column, so the student sees `60 + 1` for 70, 71 and 75 and `4 · 20 +` with no visible scroll cue. A truncated sum reads as a wrong number at the point where the lesson teaches how the numbers are built. Fix: in row 97, drop the `.nobr` around `quatre-vingt-dix-sept`. The `lang="fr"` span keeps `hyphens:manual`, so the word can break only at its own hyphen. I tested this in the browser: at 360 px the table then measures 326/326 and does not scroll. Leave the other rows as they are.

## Polish
1. [Minor] French that is not tagged `lang="fr"`. In the summary table: `*euros* in the middle`, which is auto-hyphenated *eu-ros* at 360 px, and `*centimes*`. Also check-3's title "3. Saying six euros" (its prompt is tagged) and `prior` "polite *vous*". Fix: wrap each in `<span lang="fr">` or `{fr}`.
2. [Minor] Summary table at 390: English words in the cells are auto-hyphenated ("un-der one euro"), and the "a price?" row wraps its first column. The pilot accepted this. An optional `th:first-child{width:22%}` would balance it.
3. [Minor] Hero: the seller's head sits between the price tags and partly behind them, so the seller reads as half hidden. Optional fix: move the tags 30 units up, or move the seller 40 units to the side.
4. [Minor] In the components, French number words break at their own hyphens (*quatre-vingt-/dix* in say and match titles). This is correct typography, and I am not asking for a change.

## Checked
- Contact sheets 1–7. At full size: intro-1280, selita-390-1 and -4 (both tables), the stage and fx captures through the contact sheets, and the receipt gapfill and listening match at 390 and 1280.
- The hero at 390 and 1280: no text, no faces, no answer given away.
- The 70–100 table at 360, opened, and the `.nobr` fix tested live.
- A word-break audit at 360, 390 and 1280: no French word is auto-hyphenated inside a `lang="fr"` span.
- All three model answers, opened after writing.
- No console errors, no raw `$`, no `.katex-error`.
- Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 3
