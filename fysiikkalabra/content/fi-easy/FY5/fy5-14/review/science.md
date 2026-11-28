VERDICT: PASS
CONTENT-HASH: 224e52aa680148ae

## Blocking

## Polish
- content/fi-easy/FY5/fy5-14/lesson.md:223 — the "pitkittainen" figure's label still reads $\text{harvennus}$ (figures.json:5 maps "harvennus" to "harvennus"), but the text, its alt text and the summary now say "harventuma". The physics is the same, but an S2 reader meets two words for one concept. Fix: relabel `\text{harventuma}` in lessons/FY5/fy5-14/figures.py:67 and in figures.json (the figure needs the teacher's approval again).
- content/fi-easy/FY5/fy5-14/lesson.md:571 — (unchanged from the last round) the Doppler answer gives a reason only for the front.

## Checked
- Scope: the diff only, at lesson.md:12 and :531, plus the alt text of the "pitkittainen" figure (lesson.md:14, figures.json:3). No numbers, symbols or formulas changed.
- Definition: a harventuma is the low-pressure region between compressions (p < p0). This is correct and matches the glossary term "ääni".
- Inflection: harventuma / harventumat / harventumia is used in the same way in the text, the alt text and the summary.
- The fi-easy text says the same as the Finnish version.
- Cross-chapter: fy5-10 was also moved to "harventuma" in the same change.
- Hash run at the start and at the end: 224e52aa680148ae, unchanged.

## Vanhan sisällön löydökset
- none
