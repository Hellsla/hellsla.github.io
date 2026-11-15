VERDICT: FAIL
CONTENT-HASH: 3ccad76c26d15915

## Blocking
- [Major] inquiry.json, exit-ticket.json (prompts of Prediction 1, Prediction 2, "q") — the edited sentences now typeset $100\,\text{kPa}$ but keep "50 ml", "25 ml", "40 ml" in plain text; in open-ennusta-1280-1 the two sit side by side in different typefaces and "25 / ml" breaks across a line — teacher rule 2026-11-01 (a plain number with unit in edited text) — typeset the ml values in every edited line, preferably all 32 in inquiry.json and exit-ticket.json, as `$25\,\text{ml}$`.

## Polish
- [Minor] lesson.md — the edited paragraph and worked example are correct; no other findings.

## Checked
- Diff: kPa, cm², N, Pa and kPa·ml typeset in inquiry.json, exit-ticket.json and lesson.md. Opened fy3-9-open-ennusta-1280-1 (kPa choices render upright, thin space, aligned; the plain ml defect above). Source-checked the other changed lines.

## Scores
illustrations 5 · typography 3 · Finnish 5 · accessibility 4
