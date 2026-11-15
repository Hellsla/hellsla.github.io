VERDICT: FAIL
CONTENT-HASH: bc9cdc28a007fde8
Review of the recognition chart (queue 9c) and the term change against the version passed at add641812b74c0f3; full on the chart, delta on the rest.

## Blocking
- The row "kaarre tasaisella tiellä -> kitka kaartaa -> F_μ = mv²/r" uses F_μ, which in this course is the sliding friction (F_μ = μN, liukukitka). In a curve the friction is static (the unit says so: "kitka on lepokitkaa", at most μ0 N), so the chart contradicts the unit's own terms and teaches a student to use μN. Fix: "kitka kaartaa" -> "F = mv²/r" with the text "lepokitka", and the same in the aria-label.

## Polish
- B: teacher.md still says "jokainen haara"; the chart has rows.
- B: "mikä voima kaartaa rataa?" is a question, not a sign in the task; use "kappale kulkee ympyrärataa, voimat tunnetaan".

## Checked
- 8 rows read; the wide pills on their own line are legible; the gravitation rows each follow from the sign (satellite: γMm/r² = mv²/r).
- Chart as a recognition chart: start box, then one card per sign with the choice and a dark-green pill; no formula list; 360 px capture readable, no clipped label.
- Placement after Ydinajatus (after Ydinajatus); aria-label read against every row: same rows, same order, same physics, spoken symbols in words, so usable for a screen reader.
- Changed term lines (liikekitka -> liukukitka) in the diff: consistent, physics unchanged.
- teacher.md sentence read against the chart.
- Not looked at: fi-easy and en versions (this report is fi only).
