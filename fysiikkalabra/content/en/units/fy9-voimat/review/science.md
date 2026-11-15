VERDICT: FAIL
CONTENT-HASH: 27420fa4cd4b32b8
Round 2 (fix round after queue 9c round 1): delta against the version round 1 reviewed (65a72267ecdbb241).

## Blocking
- **Term, round-1 Blocking not fixed: unit.md line 239 (Formula section) still says "In free-body diagrams $\overline{F}_\mu$ stands for either kind of friction, static or kinetic."** The chart, the same paragraph and the glossary say sliding friction; the brief lists this as fixed but the file is unchanged. Fix: "static or sliding".

## Polish
- C: "lepokitka → F ≤ F_μ0": F is the static friction (round 1, stands).

## Checked
- Round-1 Blocking fixed (fi): row 3 "tanko tai vipu pysyy paikallaan → ΣM = 0" (equilibrium stated); row 9 "putoaa, ilmanvastus, nopeus tasaantuu → F_v = G" (vertical fall stated; buoyancy neglected, fine). Both in the chart (rendered 360 px) and the aria-label.
- The friction rows (liukukitka F_μ = μN, lepokitka F ≤ F_μ0, lähtökitka F_μ0 = μ_0N) unchanged and correct.
- grep: no other "kinetic friction" in en FY9 units.
- Hash taken at the start and the end (27420fa4cd4b32b8).
