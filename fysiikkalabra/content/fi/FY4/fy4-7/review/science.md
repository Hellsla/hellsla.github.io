VERDICT: FAIL
CONTENT-HASH: b6cbdb2316954ee3

## Blocking
- inquiry.json:516 (check-1, option "Molempiin", feedback) — **A**: "Liike-energiaa muuttavat kaikki voimat" is false: a force perpendicular to the motion (the normal force on a ramp, the tension in a swinging pendulum's string) does not change kinetic energy, and the next chapter's work concept depends on this. — Fix: "Kumpikin voima muuttaa tässä kappaleen liike-energiaa, mutta potentiaalienergia liittyy vain voimaan, joka palauttaa energian…".
- lesson.md:486 (Tiivistelmä) — **B**: "Ilman kitkaa se pysyy samana" states conservation of mechanical energy with too few conditions. Air resistance also lowers it (the lesson itself names it as non-conservative), and a push or pull raises it (for example, a cart pushed up a frictionless ramp). — Fix: "Kun kitkaa ja ilmanvastusta ei ole eikä kappaletta työnnetä tai vedetä, se pysyy samana; kitka ja ilmanvastus muuttavat osan siitä sisäenergiaksi."

## Polish
- inquiry.json:19 (hook) — "lähes 1,8 m" for 1,83 m reads as just under 1,8 m; write "noin 1,8 m", as check-3's model answer does.
- inquiry.json:328 (exp-3 distractor feedback) — "rampin ja pyörien lämpötila" names wheels, but the model uses sliding friction μN on a point cart. "Rampin ja kärryn" would match Mallin oletukset.
- lesson.md Ydinajatus, "Konservatiivinen voima": "saa korkeudelta h alas tullessaan saman nopeuden" assumes the body starts from rest (or with the same speed). Saying "levosta lähtien" would make that explicit.

## Checked
- Recomputed every number in one script: hook 0,459/1,83 m; retrieval 5,1 m and its distractors; ramp model 0,051/0,204/0,459 m; steep ramp 0,459 m, 3,00 m/s; friction case 0,378 m, 2,41 m/s, 2,91 J; ratio 9,0; 50→70 km/h gives 1,96; zero-level figure 8,8/3,9/4,9/−3,9 J; worked example 21 573 J → 22 kJ; Etsi virhe 648 kJ/50 kJ/1 296 kJ/18 kJ; transfer 9,83 m (127, 19,7); check-2 0,50 kg (0,25, 2,0); exit ticket ½. All agree.
- sim.js: an exact piecewise solution with a(up/down) = g(sin α ± μ cos α). h_max and v_paluu come out of the motion. Its simState keys (hmax, vback, Ek0, Emek) are present at the experiments' initial values, and the controlled variables isolate the varied one. Slopes 25°/50° slide back with μ = 0,10. The 0–16 J scale covers 2 kg at 4 m/s, and the drawn ramp (0,95 m) covers h_max = 0,82 m.
- Derivation of E_k from h = v²/(2g) and mgh is sound. E_p = mgh is stated with its near-surface condition, the sign below the zero level and the zero-level independence of ΔE_p.
- Conservative force: the definition, the spring and electric examples, and friction/air resistance as non-conservative all match the slot's täsmennys and the glossary.
- Predictions: exactly one correct option each; the distractor feedback is correct.
- Figures: the ramp (h vs 4h), Ek(v) for 1 kg, the ball graph points (2;1), (4;4), (6;9), and the hero's ¾-height at half speed are all correct.
- Scope is within FY4 central contents.
