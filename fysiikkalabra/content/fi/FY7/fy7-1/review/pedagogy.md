VERDICT: PASS
CONTENT-HASH: bd1fbbb2ff520dfa

## Blocking

## Polish
- lesson.md:325 — "laboratoriomagneetti | noin $45\,\text{T}$" reads fine, but the sentence below says "noin $45\,\text{T}$:n jatkuvia kenttiä"; "noin" twice in one passage is harmless. Optional: "ennätys noin $45\,\text{T}$" in the table.
- The earlier Polish items (Suomessa-"etelässä" wording, 52 / 52–53 µT, "kymmenen senttimetrin päässä", check-2 inference, inclination workload, optional L2 tasks) are not touched by this diff and remain as previously reported.

## Checked
- inquiry.json table column "magneetin kenttä B_m (µT)": the 390 px capture (#48/#49) renders it as typeset B with subscript m, matching the theory and worked-example notation; no literal underscore visible.
- "B_m" now separates the magnet's field from the total B and Earth's field in the experiment table; it helps the vector-sum step.
- lesson.md table and paragraph: "yli 45 T" changed to "noin 45 T" in both places; consistent, case "noin $45\,\text{T}$:n" correct.
- lesson-answers.py comment and exit-ticket change (5 mT, 5000 µT, ratio ≈ 96) fit the earlier-approved exit ticket; comments only, no student-visible effect.
