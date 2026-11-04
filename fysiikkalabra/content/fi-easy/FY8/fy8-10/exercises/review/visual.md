VERDICT: PASS
CONTENT-HASH: 128fe4045df341c6
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- exercises.json L2-05, L2-06, L3-04, L3-05 `text` — the translation held a literal backslash-n (`\\n\\n`) where fi has real line breaks, so the task text showed `\n\n` on the page (visible in open-exercises-L2-1280-5 and L3-1280-4 captures) and the a)/b)/c) parts ran together; replaced with real newlines (the same line breaks as fi).

## Polish
(none)

## Checked
- Captures of fi-easy L2/L3 exercises showed the same literal `\n\n` (L2-05, L2-06, L3-04, L3-05); fixed in exercises.json, captures predate the fix.
- Data tables of L2-05 and L3-04: captions, headers and cells equal fi; LaTeX intact.
- Units and numbers are LaTeX with decimal comma `{,}` as in fi; display units equal fi.
- Paragraph breaks in the a)–d) parts now match fi.
