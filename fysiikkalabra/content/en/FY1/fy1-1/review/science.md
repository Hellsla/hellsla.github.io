VERDICT: PASS
CONTENT-HASH: 3aa00aef52592794

## Blocking
(none)

## Polish
- lesson.md "Types of objects, not steps" — "about four million solar masses" with an event-horizon diameter of 2.5·10^10 m: 4.0 million gives 2.4·10^10 m, and 2.5·10^10 m needs the 4.3 million that the sim box uses — say "about 4.3 million solar masses" in both, or "about 2.4–2.5·10^10 m".
- inquiry.json `tunnista`, black-hole feedback — "the known black holes formed as remnants of stars are about three solar masses or heavier" is true only for the usual picture (B, minor): add "as far as is known" or "usually", since the mass limits are not sharp (about 2.2–3 solar masses).
- lesson.md "Four fundamental interactions" — the strong interaction "reaches only a distance the size of a nucleus, about 10^-15 m": that is the range of the residual effect between nucleons (C); the sentence is placed after the residual effect, so it is acceptable, but "a few 10^-15 m" would match the lead nucleus (1.4·10^-14 m) used in L1-04.
- lesson.md "Earth's address" — "an estimated hundreds of billions of galaxies" is the conservative end (newer estimates are higher); "at least hundreds of billions" is safer.

## Checked
- Recomputed in one script: worked example (6.5·10^4, 5 steps), inquiry numbers (42 and 62 orders, midpoint -4, 12 732 km, 57 917, 6.5·10^4), every exercise answer: all agree with answers.py and exercises.json.
- Orders of magnitude by the stated rule (a below about 3 rounds down): proton -15, atom -10, hair -4, Planck -35, universe 27, Milky Way 21, Neptune's orbit 13, Proxima 10^17; the sim's `kohdeExp` = round(log10 d) gives the same values for every object the experiments visit.
- Experiment initial states (L = -9, 7.7, 27.5) make the water molecule, Earth and the universe the nearest object; the varied item is the object name only, so the setups isolate it.
- Exactly one correct option in every choice; all distractor feedbacks recomputed (10^36 for the proton pair, 26 000 ly, 109, 4 and 400-fold ratios) and correct.
- Scale-axis figure: pixel positions match log10 d (11.8 px per decade, 59 px per five); matter-ladder, cosmic-address and object-types numbers agree with the text and the sim; en numbers match fi.
- Interactions: gravity, electromagnetic, strong (residual) and weak (beta decay, K-40 in a banana, helium nucleus) are correctly assigned; guardrail wording on scale-reading uncertainty (L2-07) is followed.
