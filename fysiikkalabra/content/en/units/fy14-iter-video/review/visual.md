VERDICT: PASS
CONTENT-HASH: dc30a3e24eb0b99d

## Blocking
(none)

## Polish
1. [Minor] The table *The video checked against verified facts* (`unit.md` Checked; captures `stage-tutki-390-3/4`). At 390 the three columns squeeze the middle one to about 120 px. Its cells run to 8–10 lines with many hyphenations ("mil-lion", "opera-tion", "tar-get", "fu-sion en-ergy", "out-dated"). It is readable, but it is the unit's central evidence. Fix: shorten the middle cells, for example "€20 billion+ (ITER); US $65 billion estimate disputed; +€5 billion in 2024". Alternatively use one-word verdicts and move the explanations into the text below the table.
2. [Minor] Units in the table and the text are plain text ("23,000 t", "104 km", "150 million °C against about 15 million °C"). The sister units use LaTeX for these (`$150$ million $^\circ\text{C}$`). Fix: write quantities with symbols in LaTeX, `$23\,000\ \text{t}$`, `$104\ \text{km}$`. Quantities spelled out in words can stay as they are.
3. [Minor] `check-2`, the correct option: "The 2022 plan said 2025". This is the imprecision the unit itself warns against: the plan valid in 2022 was the 2016 baseline. Fix: "The plan valid in 2022 (2016 baseline) said 2025; the 2024 baseline says 2034." Keep the length within ±30 % of the other options.
4. [Minor] Frames 1–2: the four questions (a)–(d) run on in one paragraph, which is hard to follow while watching. Fix: put them in a short list (`<ol type="a">` or a Markdown list), one question per line.

## Checked
- Fresh build and captures for this hash: top and intro at 390 and 1280, every stage at 390 and 1280, contact sheets 1–5, credits, sources and teacher notes.
- Both `video` components: before loading, and after "Load the video" over HTTP. The iframe is youtube-nocookie, 358 × 201 px at 390 and 656 × 369 px at 1280, and its title is set. The video itself cannot play in the sandbox, so I could not check the spoken content.
- The two match components, say, the four note frames and the claims table at both widths.
- The hero (laptop, notebook, magnifier) has no text or people. Its magnifier is slightly cut off at the left edge, which is decorative.
- No `.katex-error` and no overflow. The only raw `$` are currency signs in the source titles, which is correct.
- English editing of every text. French tips: consistent respelling, *u* compared with the Finnish *y*.

## Shared issues
(none new)

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4
