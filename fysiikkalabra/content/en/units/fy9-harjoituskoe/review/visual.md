VERDICT: FAIL
CONTENT-HASH: 1e30cf3d05232256

Visual & editorial review (round 2) of the English translation of fy9-harjoituskoe.

## Blocking
1. [Major, not fixed] inquiry.json activities 2–11 `"fold": "Osa I"`: the preview (preview/en/fy9-harjoituskoe.html, 390 and 1280) still shows the Finnish tag "OSA I" on all ten Part I items. The translation cannot fix it: I tried "Part I", and check_i18n.py fails ("'Part I' differs from Finnish 'Osa I' (only texts are translated)"), so I reverted it. `fold` is still missing from scripts/check_i18n.py TEXT_KEYS. Fix (Shared issues): add `fold` to TEXT_KEYS, then set the ten values to "Part I" here.

## Polish
1. [Minor] The Finnish-derived subscripts ($m_\text{j}$, $F_\text{v}$, $R_\text{l}$, $c_\text{k}$) stay because the formulas must match the source. They are acceptable because each is defined in words.

## Round-1 fixes verified
- Blocking 2 (s7 b grammar): fixed, "What percentage of the mechanical energy …".
- Polish 1–4 (s8 figure description "between 1.1 and 6.5 m²/s² and between 12 and 71 mN", s3 c "a relative change of", s10 a, s5 b "angles of incidence"): all fixed. I also changed s3 c to "by what percentage has it changed?".

## Shared issues
- scripts/check_i18n.py `TEXT_KEYS` (and so translate_kit) lacks inquiry.json `fold`. Every translated unit that uses folds shows Finnish there.

## Checked
- I built with `python3 scripts/build.py fy9-harjoituskoe` and opened preview/en/fy9-harjoituskoe.html in Playwright at 390 and 1280 with every details element open. There is no horizontal scroll (scrollWidth 390 / 1280), no KaTeX errors, no raw `$`, no comma decimals and no console errors. The figures are 298–358 px wide at 390 and 569–608 px at 1280, and their text is English.
- check_i18n.py: en 0 errors.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4
