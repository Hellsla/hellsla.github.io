VERDICT: FAIL
CONTENT-HASH: 816cee5a91d7c8b5

## Blocking
- exit-ticket.json:11-12 — The micro model is the core idea of the lesson (lesson.md:6, :70) and its first goal. No exit-ticket question or exercise checks it. Q3 tests the water exception instead, which is a detail. — Replace Q3. q: "Teräskuula laajenee lämmetessään. Kasvavatko teräksen hiukkaset? Selitä mikromallin avulla." a: "Eivät. Lämmetessä hiukkaset värähtelevät voimakkaammin, ja koska niiden on helpompi loitota toisistaan kuin puristua yhteen, niiden keskimääräinen etäisyys kasvaa. Hiukkaset pysyvät samankokoisina."

## Polish
- lesson.md:6 — The lesson does not say why "helpompi loitota kuin puristua" holds, and it does not link to the fy3-3 idea that temperature measures mean kinetic energy. — Add: "Lähekkäin puristuvat hiukkaset hylkivät toisiaan voimakkaasti, mutta loittonevien välinen veto heikkenee vähitellen, joten hiukkanen heilahtaa kauemmas poispäin kuin lähemmäs naapuriaan."
- lesson.md:19 — The lesson never says what α means or why ΔL ∝ L₀, yet L2-04 asks for α. — Add: "α kertoo, kuinka suuren osan pituudestaan kappale pitenee 1 K:n lämpenemisessä. Kaksi kertaa pidempi sauva pitenee kaksi kertaa enemmän. Taulukon 12 tarkoittaa 12 · 10⁻⁶ 1/K."
- lesson.md:12, :21 — Line 12 sends gases to the gas laws, but line 21 applies the same formula to them, and the lesson never says why gases expand most. — In line 21 write "kaasuilla, kun paine pysyy vakiona". In line 12 add: "Lämmetessä kaasun hiukkaset törmäävät seinämiin kovempaa (fy3-3); jos paine pysyy samana, kuten ilmapallossa, kaasu laajenee."
- lesson.md:12 — The lesson goes from the density maximum straight to the lake freezing from the top. — Add: "Tihein, 4-asteinen vesi painuu pohjalle, ja kylmempi vesi jää pinnalle ja jäätyy."
- lesson.md:25 — The lesson does not explain why γ ≈ 3α rather than a cube, and L2-02 and L3-03 use the relation. — Add: "Kuution kolme särmää pitenevät kukin suhteessa αΔT; pienillä muutoksilla nämä suhteelliset kasvut lähes lasketaan yhteen."

## Checked
- Hash unchanged; lint clean.
- The ΔT in K and in °C (lesson.md:19, :60) is covered by fy3-3:10.
- Lines 8 and 64 answer the motivating question about the bridge joint.
- Each paragraph in Ydinajatus adds one idea, and none depends on the gas laws.
- The levels follow the rubric with 5/4/3 tasks.
- No exercise repeats the example. L1-01 is the closest, but it has no sign crossing, which is acceptable for L1.
- answers.py matches exercises.json.
- Exit Q1 and Q2 test core ideas.
- Glossary terms all exist.
