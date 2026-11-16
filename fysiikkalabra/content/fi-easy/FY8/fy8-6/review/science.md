VERDICT: PASS
CONTENT-HASH: 295325ec5f0a88cc
Mode: delta (round 1)

## Blocking
- none

## Polish
- inquiry.json:359 — the feedback stops at "muuttuu LEDissä sisäenergiaksi", while lesson.md:208 adds "joka siirtyy lämpönä ympäristöön" — the two are consistent; the same wording in both would follow the guardrails' "one explanation, same words" (not blocking).

## Checked
- lesson.md:208: "lämmöksi" → "sisäenergiaksi, joka siirtyy lämpönä ympäristöön": correct and in line with the guardrails (a body has internal energy; heat is energy in transfer). Causal chain unchanged: the energy gap fixes the photon energy, a larger voltage gives a larger current and more photons, not bluer light.
- inquiry.json:359: distractor "valo muuttuu sinisemmäksi" is still wrong, and its feedback states the right reason; the correct option is untouched.
- No "lämmöksi" wording is left in lesson.md, inquiry.json or exit-ticket.json, so theory and feedback agree.
- exit-ticket.json: chains only re-broken; recomputed hc = 1,9865e-25 J m, eλ = 6,488e-26 C m, U_k = hc/(eλ) = 3,06 V for 405 nm; numbers, units and order unchanged.
- Hash identical at the start and the end of the review.
