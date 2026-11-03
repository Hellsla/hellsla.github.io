VERDICT: PASS
CONTENT-HASH: a39da44d46850279

## Blocking

## Polish
1. lesson.md:1129 (Yleinen virhekäsitys, 1. kappale) — "Lasketaan yhtä monta osumaa yhteensä." jää irralliseksi käskyksi. Parempi: "Verrataan tilanteita, joissa osumia on yhteensä yhtä monta. Kuulamallissa osumien osuus $n : N$ tietyssä kohdassa pysyisi samana kuin yhden raon kanssa, koska kuulat antaisivat kahden yhden raon kuvion summan."
2. inquiry.json `ennuste-1` (prompt) — "matkaero on tässä kohdassa puolikas aallonpituus" vihjaa aaltomallin vastauksen; harkitse pelkkää kohtaa $x_0$ (sama huomio kuin lähdeversiossa, ei käännöksen vika).
3. inquiry.json `koe-2` (intro) — kerro, että mittauksen kytkeminen tyhjentää varjostimen: "Kytke sitten mittaus päälle (varjostin tyhjenee), paina *+1000 osumaa* ja kirjaa."
4. inquiry.json `simulaatio` (model) — "Haalea aalto näyttää todennäköisyysaallon" kuulostaa siltä, että kuva olisi itse aalto; "Haalea aalto havainnollistaa todennäköisyysaaltoa." on yhtä selkeä.

## Checked
- Kierroksen 1 esto korjattu: `kertaus` määrittelee intensiteetin "teho pinta-alaa kohti … energiaa sekunnissa yhtä pinta-alayksikköä kohti", sama kuin `siirto`-tehtävässä; tunti ei enää ole ristiriidassa itsensä kanssa.
- Kierroksen 1 hiomisehdotukset tehty: avauskappale jaettu kahtia ja "puolitoista aallonpituutta" poistettu; Compton-vaihtoehto "Mitä suurempi sirontakulma on, sitä enemmän se luovuttaa" on selkeä ja vastaa taulukkoa.
- Polku 17-vuotiaalle: koukku (Tonomura 1989), kertaus, kaksi ennustetta, simulaatio, kaksi lukittua koetta, johtopäätös, Compton-data, teoria, pohdinta, esimerkki, virheenetsintä, aurinkopurje, harjoitukset, kolme tarkistusta, lähtölippu. Yhden tunnin työmäärä, alun kysymykseen vastataan, de Broglie rajattu pois.
- Ennusteet voi kumota: 43 → 3 osumaa tuhannesta, reitin mittaus palauttaa 43; väärien vaihtoehtojen palaute korjaa virhekäsityksen eikä vain toista vastausta.
- Selkeä suomi: lyhyet virkkeet, lisäselitykset (matkaero, kvanttiolio, diffraktio, lepomassa, sironnut säteily, intensiteetti) oikeissa kohdissa; sanaston termit ja taivutukset ($520\,\text{nm}$:n, $1000$:sta, $4{,}3\,\%$:sta, $1\,\text{mW}$:n) oikein.
- Esimerkki porrastettu seitsemään vaiheeseen (#13–#14), yksi askel kerrallaan, kaavat 390 px:ssä luettavia.
- Kuvat #4, #7, #9, #11 luettavia 390 px:ssä; väri ei kanna merkitystä yksin; alt-tekstit (luvut sanoina) antavat saman tiedon paljastamatta ennusteiden vastauksia.
- Simulaatio 390 ja 1280 px (#2, #40, #41): ohjaimet ja lukemat ymmärrettäviä, ohje/oletukset/selitys nimetyissä laatikoissa; kokeiden alkutila, vakiot ja muuttuja näkyvät (#37–#38).
- Lähtölippu testaa ydinideaa (aalto- vs. hiukkasilmiö; $p = \tfrac{h}{\lambda}$); `tarkistus-3`:n kriteerit ovat havaittavia.
- 1280 px: teoria ja kuvat vierekkäin (#43, #45–#47), ei tekstiseinää.
