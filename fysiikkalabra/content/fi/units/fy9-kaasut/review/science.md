VERDICT: PASS
CONTENT-HASH: 8e65be516f1f6a85
SCOPE: delta re-review after FAIL at 9aa2efef9e81542c (commit e5a3f7ab3a). Diff of the unit's content from e5a3f7ab3a to the working tree touches only unit.md: (1) the second pysahdy box question reworded (commit 693d2f77fa); (2) during this review the same box was moved (uncommitted) from before $T = \theta + 273{,}15$ K to after the paragraph ending "…tiivistyy nesteeksi ennen sitä.". Hash was 3c6710f77b96877f at start and 8e65be516f1f6a85 after the move; review redone on 8e65be516f1f6a85, identical at the end. tasks.json, solutions.md, answers.py, inquiry.json, teacher.md and unit.json unchanged. Language: fi.

## Blocking
None.

## Polish
- Optionally add "Absoluuttinen nollapiste on silti todellinen alin mahdollinen lämpötila." to the box answer, so the box says this outright.
- Carried over: the third box repeats the next sentence; s5 b) "noin 5–7 %" → "noin 5 %" (recomputed 4.6 % and 5.0 %).

## Checked
- Previous Blocking 1 (A, definition): fixed. The question now reads "Miksi suoran jatkaminen nollapaineeseen on vain kaasumallin ennuste?". It names the extrapolation, not absolute zero, as the model prediction, and it matches the box answer (real gas condenses first). Nothing now says absolute zero itself is hypothetical.
- The move fixes the earlier Polish item. "Kelvinlämpötila on" now runs straight into the formula. The box follows the paragraph that introduces the extrapolation ("Se on mallin ennuste: …"), so the paragraph's "se" (the extrapolated zero) and the box agree. The (θ, p) line in the question matches the text's "(θ, p)- tai (θ, V)-suoraa" and s3. The box text is byte-identical to the committed version.
- Nothing else changed: the diff of content/fi/units/fy9-kaasut, with review/ files left out, is only these two edits. So the previous full check still holds: every number in s1–s9, inquiry.json and teacher.md recomputed against answers.py, choice items, rubrics, force diagrams, scope and figure scale.
