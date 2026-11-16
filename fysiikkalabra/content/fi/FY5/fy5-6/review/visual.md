VERDICT: FAIL
CONTENT-HASH: ec56a40218450984

## Blocking
- [Major] inquiry.json, GPS example solution, Järkevyys — the re-broken ratio sits as a display block inside parentheses: "kuin ISS (", a boxed two-row block, then "), ja sen nopeus…". The sentence is torn apart, the parentheses are orphaned on separate lines at 360 px and 1280 px, and the one-row ratio is split in two for nothing — recompose the source so the chain is not inside brackets: "…kuin ISS: $26\,560\,\text{km} : 6790\,\text{km} \approx 3{,}9$. Sen nopeus on noin puolet…" (or give the ratio its own paragraph) and let mathlayout break it.

## Polish
- (none)

## Checked
- Own 360 px and 1280 px renders with every box open: the Järkevyys paragraph of the GPS solution (the only re-broken chain in inquiry.json; no horizontal overflow, page scrollWidth 360/1280). lesson.md change is teacher-approved figures only; not re-judged.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
