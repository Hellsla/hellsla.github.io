VERDICT: PASS
CONTENT-HASH: 13accd741d1267f9
## Blocking

## Polish
- [Minor] Pysähdy ja mieti, kolmas lohko: the changed wording ("Sen vaakasuora kenttä ... kohtisuorassa Maan kentän vaakakomponenttia vastaan. Kuinka suuri on vaakasuora kokonaiskenttä?") is unambiguous and consistent with the section's use of "vaakakomponentti"; situation first, question last. No change needed.

## Checked
- Round 4 delta (scope: only the changed compass ```pysahdy block, teacher 2026-11-20). Hash at start and end: 13accd741d1267f9.
- Read the block in lesson.md: question and Vastaus both say "vaakasuora" consistently; quantities remain inline LaTeX with upright units and thin space.
- Opened review/shots/fy7-1-stage-selita-390-6.png (390 px): the block renders inside the reading column, label, question and Vastaus summary intact, no katex-error, no overflow; the surrounding formula display, the compass paragraph and the figure after it survived.
- Vastaus chain is unchanged apart from the added lead-in words; it was seen set as rows in earlier rounds.
- Deterministic checks in the packet (layout 360/390/768/1280, latex, lint) all ok.

## Vanhan sisällön löydökset
- [Minor] glossary.json "kenttäviiva" defines the term via electric field and charges only; for a magnetic chapter it does not fit (magnetic field lines are closed loops). Old content, not blocking.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5
