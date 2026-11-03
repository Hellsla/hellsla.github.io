VERDICT: PASS
CONTENT-HASH: e0c6a4f464dbb877

## Blocking
(none)

## Polish
- lesson.md Kaava: γ kept for the gravitational constant with the note "(many English books write it as *G*)", as in fy5-5 en; G is weight elsewhere in the course, so the note is the right call. Said once; correct.
- lesson.md: "the orbit is not a circle but an ellipse" for the Finnish "soikea": correct physics (bound orbits under an inverse-square force are ellipses) and fits the cannon figure.

## Checked
- Delta (coordinator fix, hash 74bd28343cb1ef34 -> e0c6a4f464dbb877): the only change is inquiry.json reveal.pending (after teoria-paino), Finnish "Palaute avautuu, kun olet lukenut kohdan Painottomuus." -> "Feedback opens when you have read the section Weightlessness."; rebuilt preview/en/fy5-6.html shows it, and it matches the theory heading "Weightlessness" on the page. No other file changed.
- Every file of content/en/FY5/fy5-6 against the Finnish: lesson.md, inquiry.json (every option, correct flag, feedback, hint, mistake, criterion, model answer and solution), exit-ticket.json, meta.json, figures.json; sims.fy5-6 in lang/en.json (26 keys, same placeholders).
- Numbers and formulas identical apart from the decimal point: 7659.7 m/s, 5570.6 s, 92.8/92.9 min, 8.6 m/s², 88 %, 605/687 N, 31 km/s, 1.023/1.018 km/s, 1/81; inquiry 7.60/7.67/7.70 km/s, 155/396/432/1700 km, 92.4 min, 8.69 N/kN, 3.65 MN, GPS 3.8738 km/s, Hubble 544 km, Phobos 6.428·10²³ kg (recomputed: 4π²r³/(γT²) = 3.2539·10²² / 5.0619·10⁻² = 6.43·10²³ kg).
- Mars task: the prompt's "5.00e23" is only the input format example, as in the Finnish; the solution and the displayed answer are LaTeX powers of ten ($6.43 \cdot 10^{23}\,\text{kg}$; capture open-tarkista-1280-2).
- Data and sources: Earth 147.1–152.1 million km, Moon 363 300–405 500 km, Halley 88–5250 million km, ISS 92.9 min, GPS 26 560 km / 11 h 58 min, geostationary 42 164 km / 23 h 56 min, Mars 6.42·10²³ kg, Phobos 9376 km / 7 h 39 min agree with NASA/GPS.gov values; source notes translated faithfully.
- Terms: centripetal acceleration, net force, support force, weightlessness (apparent weightlessness), free fall, centrifugal force rejected; British spelling (centre, metres, aeroplane, lift).
- Fixed here: astronaut/student pronouns made neutral (he/him -> they/the astronaut) in lesson.md, exit-ticket.json, inquiry.json; "aeroplane whose engines are adjusted so that it flies along the path of a projectile" (meaning of the Finnish kept).
- The later sim change (axis label key akseli_kulma only) does not touch the model; hash at the start c9745cc2a1ff934e, final above.
