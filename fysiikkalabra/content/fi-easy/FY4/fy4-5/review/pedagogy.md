VERDICT: PASS
CONTENT-HASH: 599fe97ac3218029

## Blocking
- none

## Polish
- scripts/check_i18n.py does not list `detail` (a rubric criterion's specifics) in TEXT_KEYS, so it reports the simplified check-3 criteria details as errors; the translation is right and the checker needs `detail` added (outside this review's scope; the content hash does not change when it is fixed).

## Checked
- Checked: the text is genuinely simplified (long sentences split, one idea per sentence, concepts opened in words, physics terms kept), with no step or reason removed; goals keep the -maan/-mään form; feedback, hints and solutions complete; check-3 rubric details simplified into short sentences; preview at 360 px: no overflow, sim labels in plain Finnish, drawing task reveal gated on the tick with a plain-Finnish prompt.
