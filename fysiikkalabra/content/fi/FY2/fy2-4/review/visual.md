VERDICT: PASS
CONTENT-HASH: 893ac0f1037abe61
Mode: light (teacher 2026-11-07, "kevyt katselmointi"): the FY2 targeted-fix diff (git diff origin/main...HEAD) only

## Blocking
- none

## Polish
- [Minor] inquiry.json, sim "model" and koe-1 "model" — the sim text now says losses become "pääosin lämpöenergiaksi", the experiment model says "häviöitä, pääosin lämpöä"; both are correct and readable, optionally use one form in both (e.g. "pääosin lämmöksi" / "pääosin lämpöä") for a single voice.

## Checked
- Diff of content/fi/FY2/fy2-4/inquiry.json read in full surrounding paragraph (sim model, koe-1 discussion model).
- New loss sentences: natural Finnish, no AI phrasing, "määriteltyyn hyötyyn" is clear; reflection now described as "osa tulevasta säteilyenergiasta myös heijastuu ympäristöön", not as heat.
- "Loput $75\,\%$ oli häviöitä, pääosin lämpöä." reads naturally; LaTeX intact; no new plain numbers or units.
- Substance agrees with en and fi-easy versions of the same two passages.
- Content hash recomputed at start and end: 893ac0f1037abe61 (matches brief).
