VERDICT: PASS
CONTENT-HASH: 6afc032326200d35
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- exercises.json L2-05, L2-06, L3-04, L3-05 `text` — the translation held a literal backslash-n (`\\n\\n`) where fi has real line breaks, so the task text showed `\n\n` on the page (visible in open-exercises-L2-1280-5 and L3-1280-4 captures) and the a)/b)/c) parts ran together; replaced with real newlines (the same line breaks as fi).

## Polish
(none)

## Checked
- Captures open-exercises-L2-1280-5 and open-exercises-L3-1280-4 showed the literal `\n\n` in L2-05 and L3-04; fixed in exercises.json (they will render as paragraphs after a rebuild; the captures predate the fix).
- Data tables of L2-05 and L3-04: captions, column headers and cells equal fi (decimal point in cells as in fi); LaTeX nuclide labels intact.
- Units and numbers in prompts are LaTeX with `\,` before the unit and `\cdot` for multiplication, as in fi; display units "10¹⁰ J", "10²⁰ kg" equal fi.
- No Finnish text in en.
