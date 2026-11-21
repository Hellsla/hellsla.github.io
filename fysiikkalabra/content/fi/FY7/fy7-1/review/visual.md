VERDICT: PASS
CONTENT-HASH: 6d81563af5140bc9
## Blocking

## Polish
- [Minor] Pysähdy ja mieti, kolmas lohko: the new wording ("Paikassa, jossa ... kompassin lähellä on magneetti. Sen kenttä on ...") reads fluently and sets the situation first and the question last; no change needed.

## Checked
- Round 3 delta (scope: only the ```pysahdy blocks, teacher 2026-11-20). Hash at start and end: 6d81563af5140bc9.
- Opened review/shots/fy7-1-stage-selita-390-6.png (390 px): the changed block "Pysähdy ja mieti" (Paikassa, jossa Maan magneettikentän vaakakomponentti on 30 µT ...) renders inside the reading column, label, question and Vastaus summary intact, no katex-error, no overflow, quantities as inline LaTeX with upright units and thin space, case endings fine.
- Opened fy7-1-stage-selita-390-5.png and contact-3.png: surrounding page (formula display, tan theta, figure after the paragraph) survived, figure beside the compass paragraph is unaffected.
- Answer (Pythagoras chain, 50 µT) is unchanged since round 2, where it was seen open and set as aligned rows; the diff only touches the question text.
- The two other pysahdy blocks (magnet cut in two, compass at north pole) are unchanged and were passed in round 2.
- Deterministic checks in the packet (layout 360/390/768/1280, latex, lint) all ok.

## Vanhan sisällön löydökset
- [Minor] glossary.json "kenttäviiva" defines the term via electric field and charges only ("lähtevät positiivisista ... varauksiin"); for a magnetic chapter the definition does not fit (magnetic field lines are closed loops). Old content, not blocking, not fixed in this PR.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5
