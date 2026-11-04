VERDICT: DONE

Fix round 1 for fy7-15 *Valon polarisaatio*.

## Blocking
- science, lesson.md "Yleinen virhekäsitys" — the third misconception now reads "Kolmas virhe on kuvitella, että lisäkalvo voi vain vähentää läpi tulevaa valoa." The rest of the paragraph is unchanged.

## Polish applied
- pedagogy + visual, Esimerkki "Järkevyys" — "Lähtevästä valosta" is now "Alkuperäisestä valosta ($840\,\text{W/m}^2$) läpi pääsee noin kolmannes."
- pedagogy, inquiry.json "mittaus" — the task text no longer gives the slope $A = 360{,}7\,\text{lx}$. It gives only $\Delta A$ and $B$, so the student reads the slope from the fitted line in `fy7-15/fit`. The solution's Annettu line now matches, and its graph-reading step says the exact value comes from the program. The answer 360,7 and its 2 % tolerance are unchanged; a graph reading of about 360 lx passes.
- visual, sim-1280 — the slider label `sims.fy7-15.p2_pois` in lang/fi.json is shortened to "$\text{P}_2$ (pois): θ₂ = …°" so it fits on one line.

## Not done (teacher's call or optional)
- Malus scope beyond "kvalitatiivisesti"; making "pohdi" required; the ennuste-yksi gloss; exit-ticket Q1 medium; glare-figure tint; "voi näkyä mustana".

`python3 scripts/check_lesson.py fy7-15`: all ok.
