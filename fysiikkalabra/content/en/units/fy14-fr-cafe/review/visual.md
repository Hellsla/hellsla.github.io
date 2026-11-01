VERDICT: PASS
CONTENT-HASH: a5933b8c1ec948d3

## Blocking
(none)

## Polish
1. [Minor] `unit.md` *At a French café: what happens when*: whole French phrases are set in roman inside English sentences, so a line such as "Call a waiter with S'il vous plaît ! or Excusez-moi !, never with Garçon !" is hard to parse. The pilot does the same, but this list has far more phrases. Optional fix: italicise the phrases in steps 1–5, as the Coffee words paragraph already does.
2. [Minor] Untagged French: `prior` "Greetings, *tu* and *vous*", and the feedback text "Café noisette: …". Fix: `{fr}` / `<span lang="fr">`.
3. [Minor] Hero: the plane-tree trunk ends above the terrace floor, and a short piece of awning sticks out past the building's right edge. Fix: extend the trunk down to y ≈ 600, and clip the awning at the facade.
4. [Minor] The say tips are auto-hyphenated in English at 390 ("be-fore a consonant"), and the summary table's first column hyphenates. This comes from the shared `td{hyphens:auto}` rule. It is harmless.

## Checked
- Contact sheets 1–6. At full size: intro, tutki-390-1 (the menu table), the order component at 390, selita-1280-1, the dialogue at 390 and 1280, and the gapfill and match.
- The hero at 390 and 1280: no text, no faces.
- A word-break audit at 360, 390 and 1280: French breaks only at real hyphens (*croque-/monsieur*). There is no auto-hyphenation in `lang="fr"`, and no table scrolls.
- All three model answers, opened after writing.
- No console errors, no raw `$`, no `.katex-error`.
- Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4
