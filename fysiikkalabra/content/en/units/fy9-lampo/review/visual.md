VERDICT: FAIL
CONTENT-HASH: 88ad3230c0476ed6

Visual & editorial review, round 2, of the English translation of fy9-lampo. Preview built with `python3 scripts/build.py fy9-lampo` (preview/en/fy9-lampo.html) and checked in Playwright at 390 and 1280 px with every details element opened: no console errors, no KaTeX errors, no raw `$` in text, no horizontal page scroll (scrollWidth 390 / 1280), tables fit at 390 px. Hero, melting curve, kayra and s3 graph remain readable at 390 px with English labels and the decimal point. LaTeX rules kept; English natural. Round-1 Polish 1 and 2 (s6 b wording, teacher.md "duration") are fixed.

## Blocking
1. NOT FIXED from round 1. unit.md, figure `kartta` (concept map): the four branch headings still render in Finnish at both widths: **lämpeneminen**, **olomuodon muutos**, **lämpölaajeneminen**, **lämmön siirtyminen** (unit.md lines 122, 130, 138, 146: `$\textbf{lämpeneminen}$` etc.). The translations were added to figures.json ("heating", "change of state", "thermal expansion", "heat transfer"), but they have no effect: scripts/figlib.py `translate()` (line 56) still only rewrites `\text{}`, `\mathrm{}` and `\textsf{}`, not `\textbf{}`, which lessons/units/fy9-lampo/figures.py line 112 uses. A hand edit of unit.md is not possible: check_i18n then fails with "figures differ from figures.py" (tested and reverted). Fix (shared, outside this reviewer's scope): add `textbf` to the regex in figlib.translate (and to translate_kit's figure-text extraction), then redraw with `python3 scripts/units.py figures fy9-lampo --lang en`. No change to the en files is needed after that.

## Polish
1. s3 d) "about 13 %" vs tasks.json s3 d criterion "about 12 %" (source mismatch; fix in fi first).

## Shared issues
- scripts/figlib.py `translate()` skips `\textbf{}`; check_i18n.py does not report untranslated `\textbf` words (figlib.MISSING never sees them). This affects every en/fi-easy translation of a unit whose figures.py uses `\textbf` (fy9-aallot, fy9-energia, fy9-kaasut, fy9-lampo, fy9-magnetismi-valo, fy9-moderni, fy9-sahkokentta, fy9-sailymislait, fy9-tasavirta, fy14-fusion-reactions).
