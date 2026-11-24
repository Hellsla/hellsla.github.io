VERDICT: PASS
CONTENT-HASH: 2577e76ae63ebf14

## Blocking

## Polish
- content/fi/FY5/fy5-14/lesson.md:223 — the "pitkittainen" figure's label still reads $\text{harvennus}$, but the paragraph above it, its alt text and the summary now say "harventuma". The physics is the same, so this is not an error, but students see two words for one concept. Fix: relabel `\text{harventuma}` in lessons/FY5/fy5-14/figures.py:67 (the figure needs the teacher's approval again).
- content/fi/FY5/fy5-14/lesson.md:464 — (unchanged from the last round) "mikä sen äänenkorkeus?" asks for a value, but the answer gives only what pitch depends on.

## Checked
- Scope: the diff only, at lesson.md:12 and :531, plus the alt text of the "pitkittainen" figure (lesson.md:14, figures.py:44). No numbers, symbols or formulas changed.
- Definition: in a sound wave a harventuma is the low-pressure region between compressions, p < p0. The text says so correctly and matches the glossary term "ääni" ("tihentymät ja harventumat").
- Inflection: harventuma / harventumat / harventumia is used in the same way in the text, the alt text and the summary.
- The theory paragraph, the summary and the alt text now agree with each other. Only the drawn label differs (Polish above).
- Cross-chapter: fy5-10 (*Aaltojen synty ja eteneminen*) was also moved to "harventuma" in the same change, so the chapters stay consistent.
- Hash run at the start and at the end: 2577e76ae63ebf14, unchanged.

## Vanhan sisällön löydökset
- none
