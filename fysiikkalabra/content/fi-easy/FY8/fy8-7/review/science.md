VERDICT: PASS
CONTENT-HASH: 77247589df7c4d0d

## Blocking

## Polish

## Checked
- Round 2 blocking items fixed: the correct option's feedback (inquiry.json:33) and the "ylemmän tason $E_2$ energia" distractor's feedback (inquiry.json:37) now both give $633\,\text{nm}$ and $1{,}96\,\text{eV}$, matching the prompt.
- hc/λ recomputed in my own script (CODATA h, c, e): 633 nm → 1,9587 eV, 632,8 nm → 1,9593 eV, so 1,96 eV with three figures. lesson-answers.py `kert-633-eV` = 1,958921 (rounded constants), the same to three figures; its comment is right.
- Prompt physics: spontaneous decay of an excited neon atom between two neon levels giving the 633 nm He-Ne line is correct, and agrees with the He-Ne photo caption (lesson.md:193) and the worked example (1,96 eV ↔ 633 nm, lesson.md:281, 324).
- Exactly one correct option: photon energy $hf = E_2 - E_1$, and the levels set the colour. The distractor "ylemmän tason energia" is wrong, and its feedback says why (the photon carries the difference, not one level's energy).
- Direction distractor: wrong, and its feedback is right (spontaneous emission goes in a random direction; "atomien itsestään lähettämä valo leviää kaikkialle").
- "Only after another photon hits" distractor: wrong, and its feedback is right (spontaneous decay in about $10^{-8}\,\text{s}$; stimulated emission is this chapter's new idea). The ms-lifetime metastable level in the theory is a separate, labelled case, so there is no contradiction.
- Other 650 nm mentions (rate graph, misconception box, worked-example check against the 650 nm graph) belong to the red-pointer contexts and are consistent with their own data (`rate-1mW-650`, `mis-650`).
- Hash 77247589df7c4d0d at start and end.
