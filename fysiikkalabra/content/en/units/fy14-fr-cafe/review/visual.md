VERDICT: PASS
CONTENT-HASH: d2bb84b94122e667

## Blocking
(none)

## Polish
1. [Minor] `unit.md` *At a French café: what happens when*: whole French phrases are set in roman inside English sentences. The pilot does the same. Optional fix: italicise the phrases in steps 1–5 so they are easier to parse.
2. [Minor] Hero: the plane-tree trunk stops above the terrace floor, and a piece of awning sticks out past the building. Fix: extend the trunk to y ≈ 600 and clip the awning at the facade.
3. [Minor] A say tip at 390 is auto-hyphenated in English ("be-fore"). This comes from the shared rule and is harmless.
4. [Minor] The new role tags ("Customer only", "Waiter only") use the shared `.opt-tag` at 11.5 px. They are readable, and the size is shared.

## Checked
- Fresh captures for this hash and the contact sheets.
- The menu table, the dialogue and the order, gapfill and match components at 390 and 1280.
- The hero at 390 and 1280.
- A word-break audit at 360, 390 and 1280: French breaks only at real hyphens, and no table is wide.
- `prior` *tu*/*vous* are now tagged.
- No console errors.
- Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Re-check 2026-11-01: photographs
- Screenshots at 360, 768 and 1280 px (details opened, image loaded); check_layout.py OK at 360 and 1280 px; figure gaps 20 px above and 24 px below, no overflow, credit on its own line and legible.
- Café terrace photo between the intro and the numbered steps fits well; the street scene is still readable on a phone.
