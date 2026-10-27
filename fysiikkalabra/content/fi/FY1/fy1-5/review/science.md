VERDICT: FAIL
CONTENT-HASH: 36c74c0fc49138ad

## Blocking
- lesson.md:172 and inquiry.json:382 (conclusion `model`) — new sentence "JPL:n luku on luotaimen etäisyys Maasta, ja Maa on … jopa 1 AU lähempänä tai kauempana kuin Aurinko" is unsupported and wrong in effect. The teacher's brief gives 143,05 AU as the figure matching the heliocentric model, and the lesson compares it with the distance from the Sun. If it were the Earth distance, the comparison would be wrong, not explained: in mid-February the Earth is on the far side of the Sun from Voyager 2 (λ ≈ 289°, β ≈ −38°; Earth at heliocentric λ ≈ 146°), so the Earth–probe distance is about 0,6 AU *greater* than the Sun–probe distance. The heliocentric value would then be about 142,4 AU and the gap about 0,8 AU, not 0,2 AU. The bound is also overstated: along this direction the Earth's offset is at most cos 38° ≈ 0,8 AU, not 1 AU. — Delete the Earth-distance clause in both places. Keep the honest causes, e.g. "Ero johtuu osin siitä, että Auringon vetovoima hidastaa luotainta hieman ja alkuetäisyys on annettu vain kymmenesosan tarkkuudella." Keep "Malli on tarkka murto-osan prosentista".

## Polish

## Checked
- Hash 36c74c0fc49138ad at start and end. answers.py, exercises.json and exit-ticket.json are unchanged since round 1, so their recomputed answers still stand.
- lesson.md:129 unit rule now reads "yhteensopiviin yksiköihin (yleensä SI)", consistent with the AU/vrk worked example.
- solutions.md L3-01: 0,2 AU / 0,0088602 AU/vrk = 22,6 vrk, so "noin 20 vuorokauden virhe" is right.
- solutions.md L3-02: 30 km/s · 1,497·10⁵ s = 0,030 AU = 0,020 % of 150 AU, so the Earth's motion is correctly negligible (an upper bound, since part of it is transverse).
- solutions.md L1-02: 8,0 m/s = 50 s per 400 m, a top-runner pace, so the claim is acceptable.
- inquiry.json siirto: s₀ = 120 m at t = 0, 21,6 km/h = 6,0 m/s, 120 + 6,0·45 = 390 m, matching `answer`.
- koe-1/koe-2 intros: "t > 0" fixes the undefined s/t at t = 0. The setups, locked parameters and initial states are unchanged.
- Model value at 2026-02-15 recomputed: 143,26 AU, so "143,3 AU" and "noin 0,2 AU" are right.
