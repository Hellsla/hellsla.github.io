VERDICT: FAIL
CONTENT-HASH: 816cee5a91d7c8b5

## Blocking
- exit-ticket.json:11-12 — The micro model is the lesson's first core idea (lesson.md:6, :70) and the first meta goal. No exit-ticket question and no exercise checks it. Q3 spends the last check on the water exception, which is a detail. — Replace Q3 with: q "Teräskuula laajenee lämmetessään. Kasvavatko teräksen hiukkaset? Selitä mikromallin avulla." a "Eivät. Lämpötilan noustessa hiukkaset värähtelevät voimakkaammin. Niiden on helpompi loitota toisistaan kuin puristua yhteen, joten niiden keskimääräinen etäisyys kasvaa. Kuula laajenee, vaikka hiukkaset pysyvät samankokoisina."

## Polish
- lesson.md:6 — "Hiukkasten on helpompi loitota … kuin puristua" is the step a student will ask "miksi?" about, and the lesson gives no reason. The link to fy3-3 (temperature measures mean kinetic energy) is also left implicit. — "Lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta, joten lämmetessä värähtely voimistuu. Lähekkäin puristuvat hiukkaset hylkivät toisiaan hyvin voimakkaasti, mutta loittonevien välinen veto heikkenee vähitellen. Siksi hiukkanen heilahtaa kauemmas poispäin kuin lähemmäs naapuriaan."
- lesson.md:19 — The lesson never says what α means or why ΔL grows with L₀, yet L2-04 asks the student to compute α. The table header "α (10⁻⁶ 1/K)" is also easy to misread. — Add: "α kertoo, kuinka suuren osan pituudestaan kappale pitenee, kun lämpötila nousee 1 K. Kaksi kertaa pidempi sauva pitenee kaksi kertaa enemmän, koska sen jokainen metri pitenee yhtä paljon. Taulukon luku 12 tarkoittaa 12 · 10⁻⁶ 1/K."
- lesson.md:12, :21 — Line 12 says gases need the gas laws. Line 21 says gases use the same formula, and only the table says "vakiopaineessa". The lesson also never explains why gases expand most. — In line 21 write "kaasuilla, kun paine pysyy vakiona". At line 12 add: "Kaasun hiukkasia ei sido toisiinsa mikään. Lämmetessä ne törmäävät seinämiin kovempaa (fy3-3), ja jos paine pysyy samana, kuten ilmapallossa, kaasu laajenee."
- lesson.md:12 — The lesson goes from "tiheys suurin 4 °C:ssa" straight to "järvi jäätyy pinnalta" and leaves out the middle step. — Add: "Tihein, 4-asteinen vesi painuu pohjalle, ja kylmempi vesi jää pinnalle ja jäätyy."
- lesson.md:25 — "γ ≈ 3α, koska … kolmeen suuntaan" does not answer why the factor is 3 and not a cube. L2-02 and L3-03 depend on it. — Add: "Kuution jokainen särmä pitenee suhteessa αΔT. Kun muutokset ovat pieniä, nämä kolme suhteellista kasvua lähes vain lasketaan yhteen."

## Checked
- The hash was 816cee5a91d7c8b5 at the start and at the end. The lint reports 0 errors and 0 warnings.
- Prerequisites: the lesson uses the fact that a temperature difference is the same in K and °C (lesson.md:19, :60), which fy3-3:10 teaches.
- The motivating question (the comb joint on a bridge) is one a student would ask. Lines 8 and 64 answer it.
- Each Ydinajatus paragraph adds one idea. The only forward reference is "kaasulait" (fy3-9), and nothing depends on it.
- Levels are 5/4/3. L1 tasks use one formula. L2 tasks need a rearrangement, the γ ≈ 3α step or a conversion. L3 tasks combine two ideas.
- No exercise repeats the bridge example. L1-01 (steel, mm) comes closest, but it has no sign crossing, which is acceptable for L1.
- answers.py output matches every answer in exercises.json.
- Exit Q1 (the formula) and Q2 (the hole grows) test core ideas.
- All meta glossary terms exist in glossary.json.
