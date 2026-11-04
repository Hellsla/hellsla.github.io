VERDICT: PASS
CONTENT-HASH: f73c1faf99b28bab

Round 2 (delta review of round 1 fixes; round 1 hash 5d2b5d87bf295a65). Visual & editorial review of fy9-tasavirta, 2026-11-04.

Round 1 had no Blocking findings. Built with `python3 scripts/build.py fy9-tasavirta` and opened in Playwright at 390
and 1280 with all details opened: scroll width equals viewport, 0 .katex-error, no raw $, no console or page errors.

## Round 1 Polish, verified
- P2 repeated "keksitty esimerkki": the Tutki and s3 notes are rewritten; I also changed the other five task notes from
  "… ovat keksitty esimerkki" (ungrammatical) to "… on keksitty". The badge label "Keksitty esimerkkiaineisto" still
  echoes "keksitty" in a few notes, which is acceptable.
- P3 figure labels: developer measured 14,3 px; the `mokki` capture at 390 confirms readable labels.
- P4 `mokki`: "kylmälaukku" in full, nothing clipped at 390 or 1280; current arrows and the battery polarity agree.
- P5 theory length: only 5 words added.
- P1 source-note pill radius: shared component, still under Shared issues.

## New problems found and fixed in round 2
- s3 c model graph (`lessons/units/fy9-tasavirta/sovella/figures.py`, ik_graph): the I_k label's background box covered
  the dashed extrapolation between about 5,2 A and 6,3 A, so the line did not visibly reach the I axis. The label now sits
  above-right of the point; regenerated and checked at 390 and 1280: the line meets the red point.

## Shared issues
- The source-note badge should use a smaller border radius when the note wraps to several lines (round 1 P1).
