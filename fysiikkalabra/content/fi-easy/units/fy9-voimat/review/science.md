VERDICT: PASS
CONTENT-HASH: 37ee21db139040ce

Science review of the Selkeä suomi translation of fy9-voimat against the reviewed Finnish source
(`content/fi/units/fy9-voimat/`, three reviews PASS). `check_i18n.py`: fi-easy 0 errors; `practice.py check`:
fi-easy/units/fy9-voimat 6 tasks, 95 points (same as the source); `units.py check` ok.

Faithfulness was checked mechanically and by reading: for all 312 strings of the JSON files and for unit.md,
teacher.md and sovella/solutions.md, every `$…$` formula and every number of the source is present in the
translation and none is lost (the only added numbers are the 1–5 of the new numbered list in *Ydinajatus*). All
eight `voimakuvio` code blocks and both `latex` blocks are byte-identical; headings and section ids are the same.
Correct options, tolerances and points are unchanged (check_i18n).

Every number of the unit was recomputed in one Python call with my own formulas: jumpers 981 N / 588,6 N; crane
6766,5 N → 6,8 kN (weight 6376,5 N); angled pull 54,38 N, N = 151,22 N, μ = 0,3596 (0,31 with N = mg); slope
a = 3,306 m/s² (g sin 28° = 4,6); volleyball 12,03 m/s²; boxes A–B a = 0,9285 m/s², P = 48,0 N; sled friction 23,0 N
(8,4 N and 24,5 N distractors); Atwood T = 23,5 N between 19,6 and 29,4 N (sum 49,1 N); exit ticket 85,0 N;
s1 T = 1330,8 N, 664,5 / 666,3 / 932,8 N, α₀ = 19,29°; s2 T₂ = 118,48 N, T₁ = 296,2 N, ratio 0,40; s3 least-squares
k = 1,175 1/kg, F₀ = 0,239 N, m = 0,851 kg, μ = 0,029, 0,74 1/kg, new intercept ≈ 0,38 N, extra mass 0,12 kg in
teacher.md; s4 a_max = 7,8 and 0,98 m/s²; s5 tan 21°–24° = 0,38–0,45, mean 22,5° → 0,41, sin 33° = 0,54; s6
a₁ = 1,272 m/s², v = 10,09 m/s, s₂ = 64,8 m, 12,8 m/s without friction. All agree with the translation.

## Blocking
None.

## Polish
1. **Added explanations are physically correct.** "kohdistuu eli osuu", "mukautuu eli muuttuu tilanteen mukaan",
   "yläraja eli suurin mahdollinen arvo", "massa supistuu eli häviää yhtälöstä", "verrannollisia massaan eli
   kasvavat samassa suhteessa", "systeeminä eli kokonaisuutena", "pätevät eli ovat voimassa", vaijeri = teräsköysi,
   vinssi = kone, joka kelaa vaijeria: none changes a condition of a law. The split of *Kytketyt kappaleet* into
   "Lanka voi olla kevyt … Silloin …" (unit.md) keeps the condition before the consequence. No change needed.
2. `unit.md` *Paino, kitka ja rinne*: "Joskus pintaa vastaan kohtisuorassa vaikuttavat vain paino ja tukivoima.
   Silloin $N = mg\cos\alpha$." is faithful to the source's "Kun …" condition; "Joskus" slightly weakens the cue
   that the student must check this. Optional: "Tarkista, vaikuttavatko … vain paino ja tukivoima. Jos vaikuttavat,
   $N = mg\cos\alpha$."
3. `sovella/solutions.md` s1 *Yleisiä virheitä*, third bullet: "Kitka piirretään luiskaa ylös. Vene kuitenkin
   liukuu ylös, ja liikekitka vastustaa liukumista." is correct but the conclusion is implicit. Optional: add
   "Siksi kitka osoittaa luiskaa alas."

## Shared issues
None found.
