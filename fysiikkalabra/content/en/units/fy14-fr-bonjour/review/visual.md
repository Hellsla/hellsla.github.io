VERDICT: FAIL
CONTENT-HASH: 61ad9554da6ac05b

## Blocking
1. [Major] Opening illustration (`lessons/units/fy14-fr-bonjour/figures.py` line 26, `size=32` in a 1200-wide viewBox; captures `top-390`, `intro-390`). The speech-bubble text "Bonjour ! Bienvenue !" / "Bonjour, madame !" renders at about 9–10 px on a phone. That is unreadable, and the bubbles carry the scene's point. NOTES §3 also says an opening illustration has no text. Fix: either remove the text and leave empty bubbles (the aria-label and the dialogue carry the words), or set `size=48` (about 14 px at 390) and widen the bubbles to about 540 and 480 units.
2. [Major] Automatic hyphenation inside French words (`templates/site.css` line 126 and line 326, `hyphens:auto`; captures `stage-selita-390-3`, `fx-1-390-2`). The summary table shows "Comment vous appe-lez-vous ?", and a tip shows "A woman writes *En-chantée*". In a unit that teaches beginners to spell these words, a soft hyphen next to the real hyphen of *appelez-vous* misleads. Fix (shared, `assets/units/fy14/units.css`): `[lang|="fr"]{hyphens:manual;-webkit-hyphens:manual}`.

## Polish
3. [Minor] Respelling notation is inconsistent (`unit.md` §Sounds, the `say` tips). It is italic in the theory and roman in the tips. Stress is shown with capitals (*sa-LY*, *par-LE*) in some places and accents in others (*vu-za-plé*, *bõ-jour*). Nasals are written with *n* (*fin-lan-DÈ*, *fray-KAHNSS*) right after "do not say the n". The respellings also carry `lang="fr"`, so a screen reader reads them as French. Fix: pick one convention: italic, the stressed syllable in capitals, a nasal written `õ/ã/ẽ`, and no `lang="fr"` on respellings.
4. [Minor] Language details. In the `gapfill` feedback "You live *{fr}in{/fr}* a town", the English word is tagged as French; write `*in*`. The Why question nests `<span lang="fr">` twice; keep one. "*il* is said like Finnish *il*": write "*il* is said as it is written in Finnish: *il*". In check-2, "written with a small letter": write "with a lower-case letter".
5. [Minor] The opening paragraph touches the bottom of the hero at 390 and 1280 (`templates/site.css` line 397, `.intro-media>p{margin:0}`). Give it `margin-top:.8rem`.
6. [Minor] Gapfill "Comment vous [▾] -vous ?" (`fx-5-390`): the hyphen detaches from the gap and wraps. In `gapfill.js`, keep the select and the text directly after it (up to the next space) in one `white-space:nowrap` span.
7. [Minor] Summary table at 390: "Je m'appelle …" wraps the ellipsis onto its own line. Use a no-break space before "…".

## Checked
top-390/1280, intro-390/1280, every stage at 390 and 1280, all eight components (fx-1…8) at both widths (say, dialogue in Read mode, order, gapfill, match), sources, teacher; the hero zoomed at 390. Built-page check: French no-break spaces before `! ? : ;` and inside « » are present everywhere except inside the KaTeX hero labels (harmless). French and English read against the sources; the dialogue, order, gapfill and checks are idiomatic and correct. Hash unchanged at the end.

## Scores
illustrations 3 · typography 4 · English/French 4 · accessibility 4
