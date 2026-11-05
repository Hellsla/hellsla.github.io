VERDICT: PASS
CONTENT-HASH: 3b6f5d5631f07584

## Delta review (round 4)

`git diff dcad1b122 -- content/en/units/fy9-magnetismi-valo lessons/units/fy9-magnetismi-valo` shows only the concept map `kartta` change: figures.json "liike tai virta" → "motion, current" (was "motion or current") and the regenerated foreignObject in unit.md (x 221→230, width 141→132). Nothing else changed. Rebuilt with `python3 scripts/build.py fy9-magnetismi-valo` and checked preview/en/fy9-magnetismi-valo.html in Playwright (scripts/_browser.launch) at 360 and 1280 px with all details open: no page errors, 0 KaTeX errors, "motion or current" no longer present. In `kartta` the heading "forces in a field" and the grey "motion, current" no longer overlap: gap 35 px at 360 (heading right 192, label left 227) and 67 px at 1280 (390 / 457); the label is still right-aligned with the other grey labels. `check_layout.py --width 360` and `--width 1280`: OK for preview/en/fy9-magnetismi-valo (no FAIL).

Shared issue (not translation, not blocking): with every details element forced open at 360 px the section TOC strip widens the document (scrollWidth 537); the Finnish page does the same, and it does not happen with the page as loaded (scrollWidth 360). Verdict unchanged: PASS.

# fy9-magnetismi-valo (en): visual & editorial review of the translation, round 3

Rebuilt with `python3 scripts/build.py fy9-magnetismi-valo` → preview/en/fy9-magnetismi-valo.html and checked in
Playwright (scripts/_browser.launch) at 390 and 1280 px with every details element opened: no page errors, no KaTeX
errors, no raw `$`, scrollWidth 390 / 1280 (no horizontal scroll), `html lang="en"`, decimal point throughout
(only "k=0,1,2" lists use commas, correctly). Every figure screenshotted at both widths: hero, kartta, siirto,
ympyra, fy7-7 trace, fy7-2 track-sign, s3-B, s3-lin; all English and readable. No Finnish left in the page text
except the language switcher's own "Selkeä suomi" label.

## Blocking
None. Round-2 Blocking 1 FIXED: the concept map `kartta` now shows **forces in a field**, **induction**,
**light** at both widths (figlib `translate()` covers `\textbf{}`, figures redrawn, `--check` up to date).

## Polish
1. Figure `ympyra` at 390 px: the $r = mv/(qB)$ label in the top-right corner sits close to the figure's expand
   button. Same in the source; a figures.py change would fix both languages. Not a translation issue.
