VERDICT: FAIL
CONTENT-HASH: d6a1f284318a9815

## Blocking
- content/fi-easy/FY8/fy8-7/inquiry.json:33 — (A, internal consistency) the prompt now gives the neon atom's photon as $633\,\text{nm}$, but the correct option's feedback still says "Aallonpituutta $650\,\text{nm}$ vastaa energia $\tfrac{hc}{\lambda} \approx 1{,}91\,\text{eV}$". A student checking the number against the prompt is shown the wrong wavelength and energy. — fix: "Aallonpituutta $633\,\text{nm}$ vastaa energia $\tfrac{hc}{\lambda} \approx 1{,}96\,\text{eV}$" (recomputed 1,959 eV; lesson-answers.py `kert-633-eV` = 1,958921).
- content/fi-easy/FY8/fy8-7/inquiry.json:37 — (A) same stale $650\,\text{nm}$ / $1{,}91\,\text{eV}$ in the "energia on ylemmän tason $E_2$ energia" distractor's feedback. — fix: $633\,\text{nm}$, $1{,}96\,\text{eV}$.

## Polish

## Checked
- hc/λ recomputed in my own script: 633 nm → 1,959 eV → 1,96 eV; 650 nm → 1,908 eV (old value). lesson-answers.py row `kert-633-eV` is correct and its comment right.
- Prompt physics: the 633 nm He-Ne line is a transition between two neon levels, so spontaneous emission of 633 nm from neon is correct; this matches the lesson's He-Ne photo caption (lesson.md:193) and the worked example's 633 nm check (lesson.md:324).
- Exactly one correct option (energy = $E_2 - E_1$); the other three options stay wrong and their feedback is still right (random direction in spontaneous emission; spontaneous decay needs no incoming photon).
- The reworded direction feedback ("atomien itsestään lähettämä valo leviää kaikkialle") is correct and fits the neon context better than "lampun valo".
- Other 650 nm mentions (rate graph, misconception box, tark2 check) are separate red-pointer contexts, not part of this item, and stay consistent with their own data.
- Hash d6a1f284318a9815 at start and end.
