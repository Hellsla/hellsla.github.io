VERDICT: PASS
CONTENT-HASH: 2c430903c1515a25

## Blocking

## Polish
- exercises/review/packet-science.md:57 — the "Exercise brief" block is empty in the en packet (the generator looks for the Finnish section names Kaava, Esimerkki …, which the English lesson does not use) — a tooling fix in review_packet.py, not in the exercise set.

## Checked
- Numbers, answers, units and tolerances identical to the Finnish set; only the wording is translated.
- Recomputed every answer in one script: L1 5.04→5.0 mWb, 3.0 V, 0.20 V, 0.36 mWb, 0.50 m/s; L2 48 mV, 2.0 V (steepest part 0.50–0.60 s), 0.30 A, 75 mV; L3 4.23→4.2 mV, 50 µT (ΔΦ = 2BA), 0.060 mWb (triangle area = NΔΦ).
- answers.py computes the same physics as the solutions; no answer depends only on agreeing with its own solution.
- Conditions stated: field perpendicular to the loop, rod/velocity/field mutually perpendicular; L3-01 uses only the vertical component with a correct reason.
- Solutions complete (symbolic first, conversions, sig. figs from the limiting datum, real reasonableness checks).
- Figure flux-task (0→4.0 mWb in 0.20 s, flat to 0.50 s, →0 at 0.60 s) gives every value the task needs and its English description matches.
