VERDICT: PASS
CONTENT-HASH: 2bb981571ee01f3d

## Blocking

## Polish
- inquiry.json:343 (siirto, mistake 6378): the feedback now speaks of the force but reasons "koska $g \propto \tfrac{1}{r^2}$". It is true, but it leans on the extension quantity. Fix: "koska $F \propto \tfrac{1}{r^2}$".
- inquiry.json:359 (tarkistus-1, a required check): the feedback of the correct option and of the third option explains weight by "kentän voimakkuus" and $g = \gamma \tfrac{M}{R^2}$. The question can be answered on the core path (mass does not change, weight is $G = mg$), so this is not blocking. It could say "Kuun putoamiskiihtyvyys $1{,}62\,\text{m/s}^2$".
- lesson.md:685 (Yleinen virhekäsitys, from round 1, unchanged): "kentän voimakkuus on vielä noin $8{,}9\,\text{m/s}^2$" is still the only core-path sentence that gives a field strength. Fix: "putoamiskiihtyvyys", or "voima on noin 90 % pinnan arvosta".

## Checked
- The hash was the same at the start and at the end. Round 2 judged only `git diff 09d57eb5ac..HEAD` of lesson.md, inquiry.json, exit-ticket.json and lesson-answers.py. Unchanged content rests on the round-1 full and delta reviews.
- The round-1 Blocking item is fixed. learn goal 2 is now about the force only, and the field-strength skill is in `deepen`. The optional *Etsi virhe* is titled *Syventävä:*. Tiivistelmä has $G = mg$ as a core item, separate from the *Syventävä* field line. The note "Ydinpolulle riittävät …" now holds: the only other required activity that mentions the field is tarkistus-1, which can be answered without it (see Polish).
- Transfer task: γMm/(R+h)² = ½·γMm/R² gives h = (√2 − 1)R = 2641,9 km, answer 2640 km. The check (6378/9020)² = 0,49998 is right, and the mistake values 6378 and 9020 km are right. The hints, Periaate (both masses cancel) and Järkevyys say force throughout and are correct physics. "jonka massa on $m$" makes the symbol in the hints defined.
- lesson.md:285: "kurssin" instead of "moduulin" changes no physics.
- exit-ticket.json: the chain was re-broken into rows with the same numbers, units and order. γ·1·1/1² = 6,7·10⁻¹¹ N.
- lesson-answers.py: only a comment changed. The force and g halve at the same r, so the comment is correct.
