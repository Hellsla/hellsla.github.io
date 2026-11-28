VERDICT: PASS
CONTENT-HASH: fd4df10b9ccf9625

## Blocking
(none)

## Polish
- [Minor] guide.json learn, 2nd item — "tallentamaan vastauksesi ja päättämään koe ja harjoittelemaan kokeen työkaluilla" has two "ja" and mixes three skills; split: "tallentamaan vastauksesi, päättämään kokeen ja harjoittelemaan kokeen työkaluilla".
- [Minor] guide.md, Mihin tarvitset tätä — the paragraph is about 90 words but has seven sentences in a row, two of them explaining words ("vastauskenttä", "päivittyy eli muuttuu uudemmaksi"); fine for S2, but the final sentence could be moved to its own short paragraph.
- [Minor] Table (step 2) — soft hyphens break "digi-taulukot" and "koodil-laan" at 1280 px even though there is room; the cells are narrow because the first column is wide. Not blocking, and it is a shared table component.

## Checked
- No fi-easy captures exist (content/fi-easy/.../review/ has no shots). I used the Finnish captures from content/fi/tvt/tvt-abitti2/review/shots: page-390-1, page-390-2, page-1280-1. These were stamped for the Finnish page, not this hash.
- fi-easy differs from the Finnish text: sentences are split and words are explained. Checked by diffing the sources and by checking preview/fi-easy/tvt-abitti2.html: one table, no katex-error, nothing to render as red source (the single maths item $60\,\text{min}$ is rendered in the browser).
- Not opened: page-390-3/-4, page-1280-2/-3, top captures and contact sheet. The unseen lower parts (steps 6–7, errors, sources) are plain lists and text with no figures, so I judged them from the source.
- The guide has no figures, so there is nothing to judge under illustrations.

## Scores
illustrations 5 (no figures) · typography 5 · Finnish 4 · accessibility 4
