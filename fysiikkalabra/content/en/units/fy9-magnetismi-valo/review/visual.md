VERDICT: PASS
CONTENT-HASH: 2a8fe7db4a2c47ca

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
