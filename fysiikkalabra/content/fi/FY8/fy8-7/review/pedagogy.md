VERDICT: FAIL
CONTENT-HASH: a099757b3027bdc5
## Blocking
- inquiry.json:33 — the "kertaus" stem was changed to 633 nm (He-Ne), but the correct option's feedback still says "aallonpituutta $650\,\text{nm}$ ... $\approx 1{,}91\,\text{eV}$"; the student sees a different wavelength and energy than the question gave, and answers.py now holds 1,96 eV (633 nm) — fix: write $633\,\text{nm}$ and $\approx 1{,}96\,\text{eV}$.
- inquiry.json:37 — same stale values in the "Ei tasojen erotus" distractor feedback ($650\,\text{nm}$, $1{,}91\,\text{eV}$) — fix: $633\,\text{nm}$, $1{,}96\,\text{eV}$.
## Polish
- none
## Checked
- Stem now helium-neon laser, 633 nm: matches lesson.md caption (line 193) and the worked example's sanity check (line 324); the physical setting is better than the earlier unnamed "laserosoitin" medium (my earlier polish note resolved).
- Option 3 feedback "atomien itsestään lähettämä valo leviää kaikkialle" repairs the direction misconception without the lamp comparison; fine.
- Hash unchanged at end of review.
