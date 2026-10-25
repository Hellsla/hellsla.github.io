VERDICT: PASS
CONTENT-HASH: 1a6cce6e4e6be1dc

## Blocking
(none)

## Polish
- lesson.md:67 — "siksi jää kelluu" gives the 0–4 °C anomaly as the reason ice floats (ice floats because it is less dense than water); wording only, hand to the physics reviewer.
- exit-ticket.json:12 — "4-asteista" in the question, "Neljäasteinen" in the answer; use one form.
- sim.js:100 — canvas label "välit +0,240 %" is terse; "hiukkasväli …" would be clearer (not in diff, code string).
- solutions.md:84 — "Fe" for steel: steel is an alloy; "teräs" would be clearer (not in diff).
- glossary.json — liikuntasauma and kaksoismetalli(liuska) are used but not listed; add if wanted.

## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -7,7 +7,7 @@
 
 Muutos on pieni mutta voimakas. Teräksinen sauva pitenee vain noin sadastuhannesosan pituudestaan jokaista kelviniä kohti, mutta jos sauvan päät on kiinnitetty, laajeneva teräs työntää niitä valtavalla voimalla. Siksi pitkissä rakenteissa on liikuntasaumoja. Sillan teräskansi on talvipakkasella lyhyempi kuin kesähelteellä, ja kampamainen liitos sillan päässä antaa kannen liikkua vapaasti. Samasta syystä sähkölinjat roikkuvat helteellä alempana kuin pakkasella.
 
-Kappale laajenee kaikkiin suuntiin samassa suhteessa, kuin valokuvaa suurennettaessa. Myös reikä levyssä suurenee, kun levy lämpenee. Tätä käytetään kutistusliitoksessa: kuumennettu teräsrengas pujotetaan akselille, ja jäähtyessään se puristuu tiukasti kiinni. Eri aineet laajenevat eri tavalla. Kaksoismetalliliuska, jossa kaksi eri metallia on liitetty toisiinsa, taipuu lämmetessään, koska toinen metalli pitenee enemmän. Sellainen liuska avaa ja sulkee virtapiirin vanhanmallisissa termostaateissa.
+Kappale laajenee kaikkiin suuntiin samassa suhteessa kuin valokuvaa suurennettaessa. Myös reikä levyssä suurenee, kun levy lämpenee. Tätä käytetään kutistusliitoksessa: kuumennettu teräsrengas pujotetaan akselille, ja jäähtyessään se puristuu tiukasti kiinni. Eri aineet laajenevat eri tavalla. Kaksoismetalliliuska, jossa kaksi eri metallia on liitetty toisiinsa, taipuu lämmetessään, koska toinen metalli pitenee enemmän. Sellainen liuska avaa ja sulkee virtapiirin vanhanmallisissa termostaateissa.
 
 Nesteet laajenevat yleensä selvästi enemmän kuin kiinteät aineet, ja kaasut vielä paljon enemmän. Nestelämpömittari perustuu nesteen laajenemiseen: kun lämpötila nousee, nestepatsas kohoaa ohuessa putkessa. Kaasun tilavuus riippuu lisäksi paineesta, ja kaasuja tarkastellaan kaasulakien avulla. Vesi on poikkeus: 0 °C:n ja 4 °C:n välillä se kutistuu lämmetessään, joten sen tiheys on suurin noin 4 °C:ssa. Siksi järvi jäätyy pinnalta alkaen, ja pohjalla on talvellakin noin 4-asteista vettä, jossa kalat selviävät.
 
@@ -64,7 +64,7 @@
 Kansi pitenee kesään mennessä lähes yhdeksän senttimetriä. Se on vain 0,07 % kannen pituudesta, mutta ilman liikuntasaumaa laajeneva teräs työntäisi sillan päitä niin suurella voimalla, että rakenteet vaurioituisivat. Siksi sillan päässä on kampamainen liitos, jonka hampaat liukuvat toistensa lomassa.
 
 ## Yleinen virhekäsitys
-Moni ajattelee, että lämmetessä hiukkaset itse kasvavat. Mikromallissa hiukkaset pysyvät samankokoisina, ja vain niiden keskimääräiset etäisyydet kasvavat. Toinen virhe on luulla, että levyn reikä pienenee, kun levy laajenee ”reiän sisään päin”. Reikä suurenee samassa suhteessa kuin levy muutenkin. Kolmas virhe on olettaa, että kaikki aineet laajenevat aina lämmetessään: vesi kutistuu 0 °C:n ja 4 °C:n välillä, ja siksi jää kelluu ja järvet jäätyvät pinnalta.
+Moni ajattelee, että lämmetessä hiukkaset itse kasvavat. Mikromallissa hiukkaset pysyvät samankokoisina, ja vain niiden keskimääräiset etäisyydet kasvavat. Toinen virhe on luulla, että levyn reikä pienenee, kun levy laajenee ”reiän sisäänpäin”. Reikä suurenee samassa suhteessa kuin levy muutenkin. Kolmas virhe on olettaa, että kaikki aineet laajenevat aina lämmetessään: vesi kutistuu 0 °C:n ja 4 °C:n välillä, ja siksi jää kelluu ja järvet jäätyvät pinnalta.
 
 ## Tiivistelmä
 - Lämmetessä hiukkasten värähtely voimistuu ja niiden keskimääräinen etäisyys kasvaa, joten aine laajenee.
--- a/solutions.md
+++ b/solutions.md
@@ -4,7 +4,7 @@
 **Kaava:** ΔL = α L₀ ΔT
 **Sijoitus:** ΔT = 55 °C − 15 °C = 40 K. ΔL = 12 · 10⁻⁶ 1/K · 6,0 m · 40 K = 0,00288 m = 2,88 mm ≈ 2,9 mm
 **Vastaus:** 2,9 mm
-**Järkevyys:** Kouru pitenee vain muutaman millimetrin, mutta siksi pitkien kourujen kiinnikkeet päästävät kourun liukumaan. Yksiköt: 1/K · m · K = m.
+**Järkevyys:** Kouru pitenee vain muutaman millimetrin, mutta pitkien kourujen kiinnikkeiden täytyy silti päästää kouru liukumaan. Yksiköt: 1/K · m · K = m.
 
 ## fy3-8-L1-02
 **Annettu:** alumiinijohto L₀ = 50,0 m, α = 23 · 10⁻⁶ 1/K, T₀ = 18 °C, T = −27 °C
@@ -60,7 +60,7 @@
 **Kaava:** ΔL = α L₀ ΔT, josta ΔT = ΔL / (α L₀), ja T = T₀ + ΔT
 **Sijoitus:** ΔT = 0,0072 m / (12 · 10⁻⁶ 1/K · 25,0 m) = 24 K. T = 12 °C + 24 K = 36 °C
 **Vastaus:** 36 °C
-**Järkevyys:** Auringonpaisteessa tumma kisko lämpenee helposti yli 36 °C:seen. Silloin raot ovat kiinni ja kiskot työntävät toisiaan, joten raon täytyy olla riittävän leveä. Kelvinin ja celsiusasteen lämpötilaero on yhtä suuri, joten 24 K lisätään suoraan 12 °C:seen.
+**Järkevyys:** Auringonpaisteessa tumma kisko lämpenee helposti yli 36 °C:seen. Silloin raot ovat kiinni ja kiskot työntävät toisiaan, joten raon täytyy olla riittävän leveä. Lämpötilaero on sama kelvineinä ja celsiusasteina, joten 24 K lisätään suoraan 12 °C:seen.
 
 ## fy3-8-L2-04
 **Annettu:** L₀ = 3,00 m, ΔL = 2,07 mm = 0,00207 m, T₀ = 12 °C, T = 42 °C
@@ -76,7 +76,7 @@
 **Kaava:** Reikä suurenee samassa suhteessa kuin muu kappale: Δd = α d₀ ΔT, josta ΔT = Δd / (α d₀)
 **Sijoitus:** Δd = 75,09 mm − 75,00 mm = 0,09 mm. ΔT = 0,09 mm / (12 · 10⁻⁶ 1/K · 75,00 mm) = 100 K. T = 20 °C + 100 K = 120 °C
 **Vastaus:** 120 °C
-**Järkevyys:** Lämmetessä kaikki pyörän mitat kasvavat kuin valokuvaa suurennettaessa, myös reiän halkaisija. Käytännössä pyörä lämmitetään hieman kuumemmaksi, jotta jää välys. Jäähtyessään reikä pyrkii takaisin 75,00 mm:iin, mutta akseli on tiellä, joten pyörä puristuu tiukasti kiinni.
+**Järkevyys:** Lämmetessä kaikki pyörän mitat kasvavat kuin valokuvaa suurennettaessa, myös reiän halkaisija. Käytännössä pyörä lämmitetään hieman kuumemmaksi, jotta reiän ja akselin väliin jää välys. Jäähtyessään reikä pyrkii takaisin 75,00 mm:iin, mutta akseli on tiellä, joten pyörä puristuu tiukasti kiinni.
 
 ## fy3-8-L3-02
 **Annettu:** L₀ = 50,0 mm, kupari α = 17 · 10⁻⁶ 1/K, teräs α = 12 · 10⁻⁶ 1/K, T₀ = 20 °C, T = 100 °C
@@ -92,4 +92,4 @@
 **Kaava:** ΔV = γ V₀ ΔT bensiinille ja kanisterille, kanisterille γ ≈ 3α
 **Sijoitus:** ΔT = 25 K. Bensiini: 0,95 · 10⁻³ 1/K · 20 000 cm³ · 25 K = 475 cm³. Kanisteri: 3 · 12 · 10⁻⁶ 1/K · 20 000 cm³ · 25 K = 18 cm³. Ero 475 cm³ − 18 cm³ = 457 cm³ ≈ 460 cm³
 **Vastaus:** 460 cm³
-**Järkevyys:** Kanisteri laajenee, mutta bensiinin γ on yli 25-kertainen teräkseen verrattuna, joten lähes puoli litraa ei mahdu. Siksi kanisteriin jätetään ilmatilaa.
+**Järkevyys:** Kanisteri laajenee, mutta bensiinin γ on yli 25 kertaa suurempi kuin teräksen γ, joten lähes puoli litraa ei mahdu. Siksi kanisteriin jätetään ilmatilaa.
--- a/sim-spec.md
+++ b/sim-spec.md
@@ -1 +1 @@
-Lämpölaajeneminen kahdella tasolla. Säätimet: aine valikosta (teräs 12, alumiini 23, kupari 17, tavallinen lasi 9 ja borosilikaattilasi 3,3, kaikki ·10⁻⁶ 1/K), sauvan alkupituus L₀ 1–100 m (pituus mitataan 20 °C:ssa) ja lämpötila −40…+120 °C. Vasemmalla mikromalli: pieni hila hiukkasia, jotka värähtelevät sitä voimakkaammin, mitä korkeampi lämpötila on, ja joiden keskimääräinen etäisyys kasvaa lämpötilan mukana; etäisyyden muutos on liioiteltu näkyväksi, ja kankaalla lukee liioittelukerroin. Oikealla sauva, jonka pituus piirretään liioiteltuna samalla kertoimella, ja sen alla (T, ΔL)-kuvaaja, jossa kaikkien viiden aineen suorat näkyvät ohuina ja valittu aine paksuna, ja nykyinen piste merkittynä. Tekstinä kankaan alla: aine ja α, lämpötilan muutos ΔT = T − 20 °C, pituuden muutos ΔL = αL₀ΔT millimetreinä etumerkin kanssa ja uusi pituus L = L₀ + ΔL metreinä riittävällä tarkkuudella. simState sisältää material, alpha, L0, T, dT, dL ja L. Värähtelyn vaihe on deterministinen (ei satunnaisuutta).
+Lämpölaajeneminen kahdella tasolla. Säätimet: aine valikosta (teräs 12, alumiini 23, kupari 17, tavallinen lasi 9 ja borosilikaattilasi 3,3, kaikki · 10⁻⁶ 1/K), sauvan alkupituus L₀ 1–100 m (pituus mitataan 20 °C:ssa) ja lämpötila −40…+120 °C. Vasemmalla mikromalli: pieni hila hiukkasia, jotka värähtelevät sitä voimakkaammin, mitä korkeampi lämpötila on, ja joiden keskimääräinen etäisyys kasvaa lämpötilan mukana; etäisyyden muutos on liioiteltu näkyväksi, ja kankaalla lukee liioittelukerroin. Oikealla sauva, jonka pituus piirretään liioiteltuna samalla kertoimella, ja sen alla (T, ΔL)-kuvaaja, jossa kaikkien viiden aineen suorat näkyvät ohuina ja valittu aine paksuna, ja nykyinen piste merkittynä. Tekstinä kankaan alla: aine ja α, lämpötilan muutos ΔT = T − 20 °C, pituuden muutos ΔL = αL₀ΔT millimetreinä etumerkin kanssa ja uusi pituus L = L₀ + ΔL metreinä riittävällä tarkkuudella. simState sisältää material, alpha, L0, T, dT, dL ja L. Värähtelyn vaihe on deterministinen (ei satunnaisuutta).
```

## Checked
- Lint clean (0 errors, 0 warnings); diff verified with `patch -p1 --dry-run`.
- Terms match glossary: lämpölaajeneminen, pituuden/tilavuuden lämpötilakerroin, kelvin, lämpötila.
- Case endings after number plus unit (°C:ssa, °C:seen, mm:n, mm:iin, m pitkä) in all files.
- Decimal comma in Finnish text, decimal point in JSON; minus sign is U+2212 everywhere; unit spacing matches the gold lesson.
- Finnish quotation marks ”…” in lesson.md; no hyphen-minus used as minus.
- exercises.json texts, units (µm, cm³, mm) and sim.js UI strings and readout: no errors.
- exit-ticket.json and sim-spec.md read: no errors beyond the polish items.
- Hash changed mid-review (sim.js: only the order of two createDiv lines, no Finnish string); re-checked sim.js strings, hash now 1a6cce6e4e6be1dc.
