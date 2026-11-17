# Työjono

Opettajan päättämät tulevat työt, joita ei ole vielä aloitettu. Jokainen kohta tehdään omana pull requestinaan;
valmis kohta poistetaan tästä samassa pull requestissa.

Tämä on ainoa työjono (opettaja 2026-11-13): ei GitHub Issuesia eikä erillisiä listoja. Kohdat ovat
`docs/ROADMAP.md`:n järjestyksessä. Kohdan ottava ketju katsoo ensin avoimet pull requestit, merkitsee kohtaan
ensimmäisessä commitissaan `Varattu: <haara>` ja avaa luonnos-PR:n heti, jotta muut ketjut näkevät varauksen
(repon juuren `CLAUDE.md`). Saman kurssin kohdat tehdään peräkkäin, eri kurssien yleensä enintään kolme rinnakkain; kun opettaja sanoo työn kiireelliseksi, ei ylärajaa (opettaja 2026-11-15).

## 0. Päivitystyön tehostaminen (opettaja 2026-11-17: "Laita kaikki seuraavaksi työjonoon")

Tehdään seuraavaksi, ennen uusia kurssikohtaisia läpikäyntejä. Mittaus 10.–17.11. (git-historia): 89 yhdistettyä
PR:ää, 140 mainin yhdistystä haaroihin ja noin 110 `site/`-uudelleenrakennusta; `site/` on 246 Mt ja 1282 tiedostoa.
Kulutuslokin (`review/usage.tsv`) otoksessa orkestroija on kallein rivi (yksi istunto: Opus, 296 vuoroa, 17,8 M
tokenia, 4,72 $; yksittäinen katselmointi 0,02–1 $). Osat 0a–0e ja 0g muuttavat jaettuja tiedostoja (`scripts/`,
`.claude/`, `CLAUDE.md`, `.github/workflows/`): ne tehdään yksin, yksi kerrallaan, tässä järjestyksessä, ja
yhdistetään ennen sisältö-PR:iä. Jokainen osa on oma haaransa ja luonnos-PR:nsä ja raportoi PR:ssä, mitä se säästi
(vuorot, tokenit, yhdistykset tai katselmoinnit ennen ja jälkeen). Avoimet jaetut PR:t #665 (5g) ja #666 (8m)
yhdistetään ensin.

### 0a. Katselmointikierroksen ajo yhdellä komennolla
`/lesson`, `/exercises` ja `/quality-audit` ajavat nyt ketjun `check_lesson.py` → `screenshot.py --if-stale` →
`reviews.py scope` → `reviews.py carry` → `review_packet.py` komento kerrallaan, ja jokainen komento on orkestroijan
vuoro koko kontekstilla. Yksi skripti (esim. `python scripts/round.py <id>[,<id>…] [--exercises] [--lang]`) ajaa
ketjun ja tulostaa lyhyen yhteenvedon: tarkistusten tulos (vain epäonnistuneet rivit), kunkin roolin scope, kirjatut
carryt ja pakettien polut. Erälle (`--batch`) sama. Komentotiedostot (`.claude/commands/`) lyhennetään käyttämään sitä.
Samalla selvitetään, miksi orkestrointi on ajettu Opuksella, vaikka `lesson.md` määrää Sonnetin (komennon `model:` ei
ilmeisesti vaikuta pilvi-istunnon malliin), ja kirjataan työntekijäistunnon malli koordinaattorin käynnistysohjeeseen.
Ei muuta katselmointisääntöjä. Testi: skriptin yhteenveto vastaa erikseen ajettujen komentojen tuloksia.

### 0b. Ohjetiedostot lyhyiksi
`fysiikkalabra/CLAUDE.md` latautuu jokaiseen istuntoon ja agenttiin, ja suuri osa siitä on päivättyä päätöshistoriaa
(käyttöliittymän vaiheet, Design audit, ääneenluvun toteutus). `tyojono.md` on yli 630 riviä (noin 33 k tokenia), ja
suuri osa on "tehty"-merkintöjä, opittua ja kirjattuja päätöksiä.
- `CLAUDE.md`: jäljelle voimassa olevat säännöt lyhyesti; toteutuksen kuvaus ja historia `docs/`-tiedostoihin
  (esim. `docs/decisions/`), joihin säännöstä viitataan. Yhtään sääntöä ei poisteta eikä muuteta: PR:ssä taulukko
  "sääntö → uusi paikka", jotta opettaja näkee, ettei mitään kadonnut.
- `tyojono.md`: vain avoimet kohdat. Valmiit kohdat, kurssien "tehty"-rivit ja opit `docs/tyojono-loki.md`:hen,
  kirjatut päätökset `docs/decisions/`:iin tai `NOTES.md`:hen. Tavoite alle 200 riviä.
Ajetaan yksin (kaikki ketjut muokkaavat jonoa): koordinaattori sopii hetken, jolloin muut PR:t ovat yhdistetty tai
yhdistävät mainin heti perään.

### 0c. Yksi yleinen esitystapaluokka `reviews.py`:hin
`reflow`, `md-paragraphs` ja `caption-label` on tehty kukin erikseen, ja jokainen on jättänyt tähteitä: kohteet
(Sovella, koe, yksikkö, tutkimus, TVT-ohje) tulivat mukaan vasta jälkikäteen (5f, 8c-1), ja kahden luokan yhdistelmä
samalla rivillä luokittuu lukumuutokseksi (FY5 fy5-12, fy5-2; FY4 fy4-14; FY3 fy3-5). Korjaus: yksi normalisoitu
vertailu (samat sanat, luvut, merkit, yksiköt ja kaavat samassa järjestyksessä; rivijako, kappalejako, listamerkit,
`aligned`-rakenne ja LaTeXille näkymättömät välilyönnit eivät merkitse), joka koskee samalla tavalla lukua,
tehtäväsarjaa ja jokaista kohdetyyppiä ja sallii luokkien yhdistelmät. Säännöt ennallaan: tiede ja pedagogiikka carry,
ulkoasu delta; `verify` johtaa rivit uudelleen. Testit `test_reviews.py`:hin jokaisesta yllä nimetystä tähteestä. Sen
jälkeen kurssien 5d- ja 8c-tähteet (Sovella, kokeet, yhdistelmärivit) voi tehdä ilman täysiä katselmointeja. #666:n
jälkeen; ennen kuin 8c jatkuu FY7:ään.

### 0d. CI:n selain pilvi-istuntoihin
Usea kurssi-PR jätti rivejä, jotka "vain CI:n Chromium leikkaa" (FY4, FY7, FY2), ja ne löytyivät vasta CI-kierroksella.
Pilvi-istunnossa Docker on asennettu, mutta sen palvelu ei ole käynnissä (tarkistettu 2026-11-17), joten
`ci_env.py run` ja `check_lesson.py`:n layout-tarkistus putoavat istunnon omaan Chromiumiin. Selvitä ja korjaa: joko
Docker-palvelu käyntiin ympäristön setup-skriptissä, tai `requirements-ci.txt`:n Playwright-versio, sen Chromium ja
CI-kuvan fontit asennetaan setup-skriptissä ja `ci_env.py` tunnistaa ne samaksi selaimeksi. Hyväksymisehto: fy2-3
360 px:llä antaa istunnossa saman määrän leikkautuvia kaavoja kuin CI (13, ei 3; `docs/QUALITY.md` aukko 2).
Ympäristön muutos on opettajan hyväksyttävä.

### 0e. Ulkoasun delta vain suomeksi, kun muutos on kielineutraali
Opettajan päätös 2026-11-17 (hyväksytty jonoon; sääntöteksti hyväksytään yhdistämällä PR). Kun muutos on esitystapaluokkaa
(0c) ja `check_i18n.py` toteaa saman rakenteen kaikilla kielillä, ulkoasukatselmoija katsoo vain suomenkielisen sivun;
en ja fi-easy saavat ulkoasun PASS:n carryna, jos `check_layout.py` menee niillä läpi kaikilla leveyksillä avatuin
ratkaisuin. Muu muutos (sanat, käännös, kuvat) katselmoidaan kieli kerrallaan kuten ennen. `reviews.py` RULES, `verify`,
`test_reviews.py`, `docs/QUALITY.md` ja komentotiedostot samassa PR:ssä. 0c:n jälkeen.

### 0f. Yksi läpikäynti per kurssi (työtapa, ei koodia)
Sama kurssi on käyty läpi erikseen kohdissa 5d, 8c, 8l-b, 18 ja 19, ja 8g ja 8j ovat tulossa; jokainen läpikäynti tuo
omat ulkoasukatselmointinsa kolmella kielellä, `site/`-rakennuksensa ja mainin yhdistyksensä. Tästä eteenpäin kurssin
avoimet kohdat tehdään yhdessä PR:ssä (laajennus kohdan 19 päätökseen 16.11. "jos saat yhdisteltyä PR niin tee"):
mekaaniset muutokset (8c, 8l-b:n jäännös, 5d:n tähteet) samaan PR:ään kurssin seuraavan sisältömuutoksen (8g, 8j)
kanssa, jonka katselmoinnit kattavat ne. Ei koskaan jo katselmoitavana olevaan PR:ään. Koordinaattori kirjaa jokaiselle
kurssille (FY1–FY9) yhden rivin: mitkä kohdat ovat auki ja missä PR:ssä ne tehdään. Voimaan heti; ei odota muita osia.

### 0g. `site/` pois sisältö-PR:istä (ensin suunnitelma, pysähdys opettajan hyväksyntään)
Jokainen yhdistetty PR vanhentaa kaikkien avoimien PR:ien `site/`-kopion, joten jokainen haara yhdistää mainin ja
rakentaa `site/`:n uudelleen keskimäärin 1,6 kertaa (juuren `CLAUDE.md` sääntö 4). Tavoite: sisältö-PR ei sisällä
`site/`-muutoksia; CI rakentaa sivuston ja `ruukkilabra-deploy.yml` julkaisee rakennetun version mainin ajon jälkeen.
Ensin pelkkä suunnitelma (`docs/audits/`), ei koodia: (1) miten `ci_scope.py` päättelee muuttuneet sivut ilman
committoitua `site/`-diffiä (kahden rakennuksen vertailu tai lähteistä); (2) miten "committoitu `site/` vastaa tuoretta
rakennusta" -tarkistus korvataan; (3) miten opettaja näkee PR:n vaikutuksen sivuihin ennen yhdistämistä (esikatselu
CI:n artefaktina tai `reviews.py impact`); (4) säilyykö `site/` repossa CI:n kirjoittamana vai poistuuko se kokonaan;
(5) julkaisun palautus virhetilanteessa; (6) siirtymä avoimille PR:ille. Julkaisusääntö ei muutu: sivulle pääsee vain
katselmoitu sisältö, ja yhdistäminen on opettajan julkaisupäätös. Toteutus omina PR:inään vasta hyväksynnän jälkeen.

## 3. Kaavat taulukkokirjan muotoon: valmis

FY1–FY9 on tehty (#501, #522, #527, #529, #572, #576, #578, #580, #583); FY7:n neljä `\\[Npt]`-kaavaa nimettiin kohdassa 3b (#589; nimet tarkistettu MAFY:n raakadatasta, koordinaattori 15.11: `curl https://mafytaulukot.fi/data/latestversion` antaa sivujen id:t ja versiot, sisältö `https://mafytaulukot.fi/<id>/fi/<versio>/theory.html`). FY10:ssä ja FY14:ssä ei ole nimettäviä
kaavoja (opettaja 14.11: "ei tarvitse"). FY5:ssä F pysyy gravitaatiolaissa (opettaja 14.11). Keskinopeuden tunnus on
kaikkialla $v_\text{k}$, ei $v_\text{ka}$ (opettaja 2026-11-13). Kohta 3 on valmis; FY8:n kuusi `\\[Npt]`-lohkoa ovat Sijoitus-laskuketjuja ja jäävät nimeämättä (koordinaattorin päätös 14.11).

## 4. FY10:n tutkimusten ja TVT-ohjeiden korjaukset (opettaja 2026-11-13)

Varattu: claude/fy10-minor-sisalto (vain sisältöosa: tutkimusten ja TVT-ohjeiden omat Minor-löydökset ja fy10-induktion kenttäviivat; jaetut komponentit eivät kuulu siihen).

Sisältöosa (PR #645): tekstin ja LaTeXin Minorit korjataan. Kuviin ei kosketa (opettaja 16.11: "älä tee näille kuville mitään, piirrän ne uudelleen ChatGPT:llä"); jokainen kuvalöydös, myös fy10-induktion kenttäviivat, on PR #645:n avoimissa kohdissa opettajan piirtämistä varten.

Ehdotus yhteiseksi kuvasäännöksi (koordinaattori 16.11; opettajan päätettäväksi): toistuvat kuvalöydökset kirjataan yhtenä sääntönä, ei kuva kerrallaan: (1) nimikkeet luettavia 390 px:ssä (vähintään noin 12 px, ei vaaleanharmaata ohutta tekstiä); (2) mallikuvaajan akseleilla suure ja yksikkö, tai kuvaus sanoo, että kuva on kaavio ilman mittakaavaa; (3) kaaviokuvan aria-label tai kuvateksti sanoo sen kaaviokuvaksi ("ei mittakaavassa", "havainnollistava, ei mitattu"); (4) malli- tai luonnoskuvaaja merkitsee itsensä malliksi kuvan sisällä. Jaettu osa (taulukoiden otsakkeet ja tyhjät rivit 390 px:ssä, listojen numerointi, laskurivit listoissa, apulinkit, tyhjät 28×28 px:n kaappaukset) kuuluu erään 1.

Tehty (#549, erät 2–4): fy10-liukukitka, fy10-jousivakio, fy10-induktio (kuva osin, ks. PR), tvt-kuvaaja ja tvt-tyoselostus; fy10-hiuksen-paksuuden löydös ei pitänyt kuvasta (ei muutettu). Jäljellä: erä 1 (jaetut komponentit), Minor-erä ja yhteinen kuvasääntö.

Auditointi on tehty (#536: 28 PASS, 8 FAIL, ei Critical-löydöksiä, 159 Minor). Korjataan `/quality-audit <id> --fix`
#536:n kuvauksen järjestyksessä: ensin Major-löydökset tvt-epavarmuus, tvt-kuvaaja, tvt-tyoselostus, fy10-jousivakio,
fy10-induktio, fy10-lammonjohtuminen, fy10-liukukitka ja fy10-hiuksen-paksuus. fy10-liukukitkan kallistusvirhe
("0,02 asteen kallistusta kohti", noin 50-kertainen ero) tiedekatselmoinnilla ennen korjausta. Jokainen Major-löydös
tarkistetaan ensin kuvista (fy10-hiuksen-paksuus antoi kahdella ajolla eri tuloksen). Minor-löydökset ja yhteinen
kuvasääntö erillisenä eränä opettajan päätöksellä; jaettujen komponenttien muutokset (`templates/`, `screenshot.py`:n
tyhjät 28×28 px kaappaukset) tehdään yksin. Voi kulkea rinnakkain kohdan 2 kanssa.

## 5b. Leikkautuva kaava: tarkistus ja rivijako-carry: tehty (PR #594, opettaja 2026-11-15)

Tehty: `check_layout.py` havaitsee leikkautuvan kaavan (360 ja 390 px, avattu ratkaisu, kolme kieltä), `reviews.py` tuntee
kategorian `reflow` (science ja pedagogy none, visual delta), kehittäjäohjeessa on rivi. Mainissa jo olevat leikkautuvat
kaavat ovat `docs/clipped-formulas/<kurssi>.tsv`:ssä (rivejä vain poistetaan). Auki, opettajan päätettävä:
1. lasketaanko vierityslinjalle jäävä inline-kaava leikkautuneeksi (nyt kyllä), ja korjataanko vanha lista jaetulla
   komponentilla vai sivu kerrallaan;
2. tehdäänkö täysi CI-pohjainen lista (koko sivuston ajo, noin 20 ydintuntia): lista on tehty paikallisella Chromiumilla, ja
   CI voi löytää sivuilta uusia rivejä, jotka lisätään CI:n lokista.
Kohdat 6 ja 8l voivat jatkua; #593 (fy8-2) yhdistää mainin ja ajaa `check_layout.py fy8-2 --width 360`.

## 5c. ElevenLabs-ääneenluku FY1 ja FY2 (opettaja 2026-11-15)

Varattu: claude/elevenlabs-readaloud

Tilanne 2026-11-15 (PR #598 suljettu, jatkuu uudessa PR:ssä haarasta claude/readaloud-recorded): ääneksi valittu Oskari - Finnish;
`flSpeech.blocks()` lukee käsitekortin termin; FY1:n luvut fy1-1…fy1-8 on äänitetty. Opettajan päätös: mp3-tiedostot eivät kuulu
päärepoon vaan repoon Hellsla/ruukkilabra-audio (kuten mallit); päärepossa on vain manifestit. FY2 odottaa opettajan päätöstä.

Suomenkielisten FY1- ja FY2-lukujen Kuuntele-nappi soittaa etukäteen tehdyn ElevenLabs-äänitteen; muut kielet ja kurssit
jatkavat Supertonic-äänellä. Jaettu muutos (scripts/, readaloud.js, CLAUDE.md, testit): ajetaan yksin, 5b:n (#594) jälkeen.
- Äänitteet tehdään skriptillä (`scripts/`), ei koskaan oppilaan selaimesta. API-avain on ympäristön network secret
  osoitteelle api.elevenlabs.io (otsake `xi-api-key`; tallennettu ympäristöön hellsla.github.io 2026-11-15); avainta ei
  kirjoiteta repoon.
- Skripti avaa rakennetun sivun Playwrightilla ja ottaa `readaloud.js`:ltä samat lohkot ja saman puhetekstin kuin
  Kuuntele-nappi lukee (Pohdinta ja Teoria; ei tehtäviä, vihjeitä eikä ratkaisuja). Kaavat sanoiksi `lang/fi.json`
  "speech"-säännöillä, luvut ja yksittäiset tunnukset kirjoitettuna auki.
- Yksi mp3 ja aikaleimat per lohko, sidottuna lohkon puhetekstin tiivisteeseen. Muuttunut lohko luetaan Supertonicilla,
  kunnes se generoidaan uudelleen. Lauseen ja sanan korostus säilyy.
- Ensin ääninäytteet: sama fy1-1:n kappale kolmella suomenkielisellä kirjastoäänellä opettajan valittavaksi. Pysähdys valintaan.
- Sitten pilotti: vain fy1-1. PR:ään lista fy1-1:n kaavoista muodossa "TeX → puheteksti", äänitiedostojen yhteiskoko ja
  käytetty merkkimäärä. Pysähdys opettajan kuunteluun.
- `CLAUDE.md`:n Ääneenluku-kappale ja `test_readaloud.py` päivitetään samassa PR:ssä. Lukujen tekstejä ei muuteta, joten
  katselmoinnit eivät vanhene.

## 5d. Leikkautuvat kaavat omalle rivilleen ja align-muotoon (opettaja 2026-11-15)

FY5 tehty (PR #638): 332 riviä pois listalta (luvut, tehtävät, Sovella ja Esimerkkikoe kolmella kielellä); 16 jää. Viisi kaavaa kolmella kielellä, joiden sulkeiden, murtoluvun tai kymmenpotenssitulon sisältö on yksinään ruutua leveämpi, eikä riviä katkaista suureen tai sulkeiden sisältä: fy5-1 $\Sigma M = g\,(\ldots)$, fy5-4 $1200\,\text{kg}\cdot\left(\ldots\right)$, fy5-6 $\gamma M = 6{,}674 \cdot 10^{-11} \cdot 5{,}97 \cdot 10^{24}\ldots$, fy5-8 $\tfrac{1}{2}\cdot 150\,\tfrac{\text{N}}{\text{m}}\cdot\left(\ldots\right)$ ja kokeen $F = 6{,}674 \cdot 10^{-11} \cdot \dfrac{\ldots}{\ldots}$ (vain fi). Lisäksi fy5-12:n Tutki-summa $3{,}20\,\text{m} + 2{,}40\,\text{m} = 5{,}60\,\text{m}$: luvun tiedekatselmointi on vanhemmasta versiosta, ja reviews.py luokittelee rivityksen yhdessä välillä tehtyjen muutosten kanssa lukumuutokseksi. Opittua: kertomerkin kohdalta katkaistaan vain kokonaisten suureiden välistä, ja jatkorivin (&− tai &·) jälkeisen relaatiorivin loppuun tulee &, koska mathlayout.join_wide liittäisi sen muuten jatkoriviin leveällä näytöllä (= kesken riviä); jaettu korjaus join_wideen on ehdotettu koordinaattorille.

FY4 tehty (PR #637): 584 riviä pois listalta; 89 jää (17 lyhyttä muuttamatonta kaavaa, jotka leikkautuvat vain CI:n selaimessa 4–6 px (fy4-4, fy4-8, fy4-9, fy4-13, fy4-16; listalta poistetaan vain rivi, jonka kaava ei enää ole tekstin sisällä), liian leveät yksittäiset `\dfrac`- ja `\sqrt`-kaavat (fy4-6, fy4-8, fy4-10, fy4-11, fy4-15), paljaiden kertoimien tulot, joita ei saa katkaista (fy4-15), välilyönnittömät `\cdot`-ketjut, joissa rivi voisi katketa vain kertomerkin jälkeen ja katko sen edellä muuttaisi `chain_view`n (fy4-6, fy4-16; ulkoasukatselmointi hylkäsi kertomerkkiin päättyvän rivin), sulkeissa olevat kaavat (fy4-8, fy4-10:n `p_\text{kok}`), lainattu opiskelijan lasku (fy4-7, fy4-9) sekä fy4-14:n kaksi inquiry-kaavaa: niiden rivitys osui riveille, joita aiemmat siirrot koskivat, ja olisi vaatinut tiede- ja pedagogiikkakatselmoinnin). Rivijako mitattiin selaimessa (KaTeX) ja on kaikilla kielillä sama.

FY6 tehty (PR #627): 565 riviä pois listalta; 29 jää (sulkeiden tai lainausmerkkien sisällä olevat kaavat, liian leveät yksittäiset `\dfrac`- ja `\sqrt`-kaavat ja fy6-2:n taulukon mittarin tarkkuusmerkinnät). Rivi alkaa vain relaatiosta, plus- tai miinusmerkistä tai kokonaisten suureiden välistä.

FY9 tehty (PR #611): 1001 riviä pois listalta; 84 jää (16 liian leveää yksittäistä `\dfrac`- tai `\sqrt`-kaavaa ja 12 sulkeiden, lainausmerkkien tai sijapäätteen sisällä olevaa kaavaa, jotka jäävät tekstin sisään).

FY1 tehty (PR #619): 199 riviä pois listalta; 3 jää (fy1-3:n keskiarvon `\dfrac`, jonka osoittajan summa on yksinään ruutua leveämpi).

FY7 tehty (PR #633, kohdan 19 FY7:n kanssa): luvut 1–16 ja esimerkkikoe kolmella kielellä; 439 riviä pois listalta (tarkistettu site/:stä 352, 360 ja 390 px:llä ja CI:ssä); 56 jää (Sovella-sarjan 18 riviä: sarja palautettiin mainin muotoon, koska sen juurikaava `\sqrt{\dfrac{…}{…}}` ei jakaudu riveiksi ilman sisältömuutosta; fy7-2:n leveä `\dfrac`; fy7-14:n kaksi vihjeen kaavaa, jotka CI:n Chromium leikkaa 360 px:llä mutta paikallinen ei edes 352 px:llä; sekä ne en- ja fi-easy-tehtäväsarjojen rivit, joiden sivulla näkyy yhä vanhempi katselmoitu versio, koska niiden tiedekatselmointi oli vanhentunut jo mainissa: en fy7-4, fy7-6, fy7-10, fy7-12, fy7-16, fi-easy fy7-6, fy7-12). Uudet huomiot: tehtävätekstissä (`p.task`) display-kaavan perässä oleva välimerkki ei siirry kaavaan, joten lainauksen tai sulkeiden sisäinen ketju jaetaan relaation kohdalta peräkkäisiksi tekstin sisäisiksi kaavoiksi (`$a = b$ $= c$`, reflow); jo mainissa `aligned`-muotoisia monen yhtälön lohkoja ei saa yhdistää.

FY2 tehty (PR #610): 399 riviä pois listalta (luvut, Sovella ja Esimerkkikoe kolmella kielellä); 53 jää (47 vanhaa inline-kaavaa, jotka CI löysi 360 px:llä, ja kahden tehtävätekstin opiskelijan laskun 6 riviä, koska tehtävätekstissä välimerkki jäisi display-kaavan jälkeen yksin).

FY3 tehty (PR #628): 876 riviä pois listalta; 23 jää (fy3-10:n vihjeen liian leveä `\dfrac`, fy3-4:n sulkeissa oleva kaava, fy3-5:n ja fy3-12:n lainattu opiskelijan lasku, fy3-5:n kolme inquiry-kaavaa, joiden rivitys olisi vaatinut täyden tiedekatselmoinnin, sekä fy3-15:n kertausvalinnan palautteen kaava: `test_inquiry.py` vertaa palautteen alkua lähteeseen eikä tunnista näyttökaavaan siirtyvää välimerkkiä).

Kohdan 5b tarkistus löysi mainista noin 4 800 kaavaa, jotka leikkautuvat puhelimella (`docs/clipped-formulas/`).
Esimerkki: fy2-3, Esimerkki 2, jossa tekstin sisällä oleva $E = 1500 \cdot 3{,}0\,\text{kWh} = 4500\,\text{kWh}$
näkyy 360 px:llä muodossa "4500 kW". Opettaja 2026-11-15:
- Tekstin sisällä oleva pitkä kaava nostetaan omaksi kaavarivikseen, ja pitkä ketju jaetaan `aligned`-ympäristöön
  yhtäsuuruusmerkit tasattuina (`E &= 1500 \cdot 3{,}0\,\text{kWh} \\ &= 4500\,\text{kWh}`).
- Pelkkä tällainen muutos (samat luvut, merkit ja yksiköt samassa järjestyksessä) katselmoidaan vain ulkoasun osalta:
  `reflow`-carry (5b) siirtää tiede- ja pedagogiikkakatselmoinnit.
Tehdään kurssi kerrallaan, yksi PR per kurssi, alkaen kursseista, joilla rivejä on eniten (FY8, FY9, FY2); jokainen
korjattu kaava poistaa rivinsä listalta. Ei muita sisältömuutoksia samassa PR:ssä.
Opit FY8:sta (#601, 15.11): (1) inline-`$$` samalla rivillä ilman tyhjiä rivejä pitää tekstin välit ennallaan, jolloin
reviews.py:n rivipohjainen luokitus ei anna `numbers`-luokkaa sekatiedostoissa (esim. inquiry.json). (2) lint_lesson:
lessonin Esimerkki-`$$`-lohkon ensimmäisellä rivillä ei lukuja ja yksiköitä (vasen puoli omalle riville); solutions.md:n
Kaava-rivin ensimmäisellä rivillä `=` (`$$\begin{aligned}` ja ensimmäinen rivi samalla rivillä). (3) check_i18n vaatii
saman kaavarakenteen kaikilla kielillä: rivijako päätetään kielineutraalisti. (4) CI:n Chromium on noin 4 px tiukempi
kuin paikallinen: aja check_layout myös 352 px:llä. (5) Rakenna site/ vasta, kun kaikki katselmoinnit ovat voimassa.

## 5e. Välimerkki display-kaavan perään (koordinaattori 2026-11-15)

Varattu: claude/display-kaavan-valimerkki

Kohdan 5d PR #601: kun tekstin sisällä oleva kaava nostetaan display-kaavaksi (`$$…$$` tai `aligned`) ja lause jatkuu
välimerkillä ("… $$kaava$$." tai "$$kaava$$, joten …"), välimerkki jää yksin seuraavan rivin alkuun. Sisältöä ei muuteta
(reflow-carry ei muuten kulje). Jaettu muutos (`scripts/`, testit): ajetaan yksin, merkitään ensin.
1. Rakennus (`scripts/build.py`/`scripts/mathlayout.py`, palvelinpuolella): display-kaavan välittömästi seuraava
   välimerkki (. , ; : ! ?) siirretään renderöityyn kaavaan viimeisen rivin loppuun (`\text{.}`; `aligned`: viimeinen rivi).
   Muu teksti jatkuu seuraavassa kappaleessa ilman välimerkkiä.
2. Toimii kaikkialla, missä kaavoja renderöidään (lesson.md, inquiry.json, exercises, solutions, koe, sovella, units),
   kolmella kielellä; ääneenluku ei muutu oudoksi.
3. Testi: `$$a = b$$.` → piste kaavassa; `$$a=b$$, joten c` → pilkku kaavassa, "joten c" jatkuu; inline-kaava ei muutu.
4. `site/` muuttuu vain display-kaava + välimerkki -kohdista; `check_layout.py` SMOKE-sivuille; `reviews.py verify`
   (rakennusmuutos, mikään katselmointi ei vanhene).


## 5f. Reflow-carry yksiköille, Sovella-sarjoille ja esimerkkikokeille (koordinaattori 2026-11-15)

Varattu: claude/item-reflow-carry

Kohdan 5d FY9-PR #611: FY9:n sisältö on yksiköitä (`content/*/units/fy9-*`), ja `carry-item` siirsi vain opettajan
hyväksymät kuvat, kaavanimet ja MAFY-tunnukset. Pelkkä rivijako vanhensi siis yksikön kaikki kolme katselmointia; sama
koskee FY8:n (#601) Sovella-sarjoja ja esimerkkikoetta. Jaettu muutos (`scripts/reviews.py`, `test_reviews.py`): ajetaan
yksin, 8l:n (#607) jälkeen ja ennen 8m:ää.
1. `carry-item` vertaa tekstejä myös `chain_view`-muodossa (sama kuin luvun `reflow`-luokka): kun ero on pelkkä
   rivijako, tiede ja pedagogiikka siirtyvät luokalla `reflow`, ja ulkoasu tarvitsee delta-katselmoinnin (RULES).
2. `verify` johtaa reflow-rivit uudelleen eikä hyväksy reflow-riviä ulkoasukatselmoinnille.
3. Testi (`test_reviews.py` 8n): yksikön kaava nostettuna `aligned`-muotoon siirtää tieteen ja pedagogiikan, ei ulkoasua;
   muuttunut luku, merkki tai sana ei siirrä mitään.
## 6. Kuvatehtävät ja taulukkotehtävät FY8 ja FY9 (opettaja 2026-11-13, 2026-11-14 ja 2026-11-15)

Opettaja 2026-11-15: kaksi kuvatehtävää per luku on hyväksytty kustannuksesta huolimatta (noin 300 k per luku);
FY10:een ja FY14:ään ei tehdä kuvatehtäviä eikä taulukkotehtäviä.
Varattu: claude/exercises-fy8-6 (fy8-6)
Havainto (koordinaattori 2026-11-15, fy8-2): kahdessa erässä peräkkäin ulkoasu on hylännyt ratkaisujen kaavaketjut,
jotka eivät katkea 360 px:llä (`check_layout.py` ei havainnut niitä). Seuraavien erien kehittäjän pitää jakaa pitkät
sijoitusketjut (hc omaksi vaiheekseen, energia jouleina ennen eV-muunnosta, yksikkö- ja vertailuketjut omille riveilleen)
jo ensimmäisessä versiossa. Parannusehdotus (koordinaattori, opettajan päätettäväksi): pelkkä kaavaketjun rivijako ilman
lukujen tai merkityksen muutosta voisi kulkea carryna samoin kuin presentation-only, mutta vain jaetulla muutoksella ja
opettajan päätöksellä; nyt se vaatii kolmen roolin uudet katselmoinnit (fy8-2: noin 280 k).

FY8 yksi luku per PR erästä 2 alkaen (koordinaattori 2026-11-15). Erä 1 (#590) valmistui osittain: fy8-1 on tehty ja
katselmoitu (+3 tehtävää: L1-10 MAFY kalsiumin irrotustyö 3,20 eV, L2-08 ja L2-09 kuvatehtävät; tiede, pedagogiikka ja
ulkoasu PASS fi, en, fi-easy). fy8-3:ssa on jo kaksi kuvatehtävää (L2-03, L2-06), ei muutosta. fy8-2 palautettiin mainin
tilaan ja jää erään 2: lisää kaksi kuvatehtävää kuvalla `fy8-2/lamp-spectrum`, esim. L2-09 (sinisen viivan 436 nm
fotonin energia, 2,84 eV) ja L3-06 (405 nm ja 546 nm viivat; tiedekatselmointi hylkäsi version, jossa viivat tulivat
kahdelta ylätasolta samalle alatasolle: kuvan elohopeassa ne tulevat yhdeltä ylätasolta 7³S₁ kahdelle eri alatasolle,
joten b) kysyy alatasojen eroa 5,461 − 4,667 = 0,79 eV ja c) selittää, miksi eroa ei saa laskea yhteen; korjaa tehtävä,
ratkaisu, mallivastaus ja 1570 nm infrapunahuomautus tämän mukaan). Seuraavat: fy8-4, fy8-5, ..., fy8-16 (MAFY-taulukkotehtävä
noin joka kolmanteen: ehdotus fy8-4, 7, 10, 13 ja 16, arvot `docs/mafy-arvot.tsv`:ään lähde-URL:lla).
Kulutus (mitattu, erä 1): noin 300 k per luku katselmointeineen (kehittäjä 90–105 k, täydet delta-katselmoinnit kolmella
kielellä 150–200 k, korjauskierros 35 k + uusintakatselmoinnit 160 k); erän 1 kokonaiskulutus noin 955 k ja koordinaattori
hyväksyi ylityksen jälkikäteen (alkuperäinen katto 350 k, sitten 500 k, 650 k ja 1 000 k). Mitoita erät sen mukaan: yksi
luku per PR, ja ota katselmoijat per rooli yhdellä ajolla kolmelle kielelle (en/fi-easy-tiede ei kulje fi:n PASS:n
mukana, jos käännöksessä on ennestään eroja: `reviews.py` `translation_differs` fy8-1:ssä L3-02 en, L3-01 fi-easy).
Polish-kohdat (ei estä, ei korjattu, jotta fy8-1:n hash ei muutu): `lessons/FY8/fy8-1/answers.py`:n kommentti
"387,6 nm -> 388 nm" pitäisi olla "387,5 nm -> 387 nm"; L2-08:n ratkaisussa 5,56 on tarkempi kuin kuvasta luettava 5,6;
L2-09:n ratkaisun "±1 %" löysä (7,0 ± 0,1 antaa ±1,5 %) ja merkitsevien numeroiden perustelu epäselvä; L2-08 on kevyt
tasolle 2; kuva on pieni tehtäväkortissa (jakoarvot noin 8 px, sama kaikilla kuvatehtävillä).
Tämä kohta jää, kunnes FY8 ja FY9 on tehty.

Sama tahti kuin FY4:stä alkaen: jokaisessa luvussa vähintään kaksi kuvatehtävää ja taulukkotehtävä noin joka
kolmannessa luvussa (#521, #528). Arvot vain `docs/mafy-arvot.tsv`:stä, uudet rivit lähde-URL:n kanssa. Aloitetaan,
kun kohdan 2 katselmoinnit on tehty, jotta katselmoimattomien sarjojen jono ei kasva.

## 8. Virhekäsitys omana komponenttinaan; virhekäsitys ja tiivistelmä avattaviin laatikoihin (opettaja 2026-11-13)

Toistuva osa Teoria-vaiheeseen: väite yhdellä lauseella, sitten miksi se ei päde
(`docs/audits/2026-11-10-vaiheiden-kayttoliittyma.md` kohta 5.2). Komponentti kerran, sitten sisältötyö luku
kerrallaan: lukujen sisältö muuttuu, joten jokainen luku tarvitsee tiede-, pedagogiikka- ja ulkoasukatselmoinnin.

Opettaja 2026-11-13: "Yleinen virhekäsitys" omassa laatikossaan avattavana (suljettu `<details>`, näppäimistöllä
avattava, kuten Mallin oletukset ja Laskennan selitys). Samoin Tiivistelmä omaan avattavaan laatikkoonsa. Tämä osa
on sivupohjan muutos (build, ei lukujen tekstejä), joten sen voi tehdä ennen virhekäsitysten sisältötyötä; tarkista,
että käsitekorttien alleviivaus ja sirut Tiivistelmän perässä toimivat laatikon sisällä (test_home.py).

## 8c. Kappalejako esimerkkien ja ratkaisujen vaiheisiin (opettaja 2026-11-13)

FY1 tehty: fy1-1…fy1-8 esimerkit ja ratkaisut kolmella kielellä (#650); Sovella (fi, en, fi-easy), esimerkkikoe ja en
fy1-1:n harjoitusten kolme askelta (claude/fy1-kappalejako-2, 8c-1:n #657 jälkeen). Jäljellä FY1:ssä vain numeroitu lista
Sovellan mallivastauksessa "Mitkä tahansa neljä seuraavista", jonka lint lukee yhdeksi kappaleeksi (lista, ei kappale; ei muutettu).

Opettaja 2026-11-16: laajennetaan myös FY9:ään ja FY10:een. Järjestys FY1 → FY2 → FY4 → FY5 → FY6 → FY7 → FY8 →
FY3 loput → FY9 → FY10.

Pilotti fy3-13 tehty (#643; koordinaattorin välittämänä opettaja hyväksyi 2026-11-16 sekä pilotin, "huomattavasti
parempi luettavuus", että uuden katselmointiluokan `md-paragraphs`: kappalejako ja listamerkit, sanat samat ja samassa
järjestyksessä, tiede ja pedagogiikka carry, visual delta). Sääntö on NOTES.md §3:ssa ("Paragraphs in stages and
steps") ja `lint_lesson.py` varoittaa (2026-11-16: 512 pitkää kappaletta ja 112 kesken kappaleen olevaa kysyttyä
muissa luvuissa). Jatko kurssi kerrallaan (`/quality-audit --fix`), kaikki kielet, fy3-13:n mallin mukaan.

FY4 tehty (claude/fy4-kappalejako, #654): fy4-1…fy4-16 esimerkit ja ratkaisut kolmella kielellä; tiede ja pedagogiikka
carry (`md-paragraphs`), ulkoasu delta PASS jokaiselle osalle omista kaappauksistaan. Lintin 8c-varoituksia jää fi 16, en 34,
fi-easy 18: pitkät **Vastaus:**-askeleet (vastausluku pysyy ensimmäisessä kappaleessa) sekä fy4-7:n ja fy4-11:n kohdat, joissa
järkevää katkoa ei ole (kaksoispisteeseen päättyvä Sijoitus ennen display-kaavaa, pitkät Annettu-rivit). Ulkoasun Polish-huomiot
(vain kirjattu): fi-easy fy4-10 "(2) Heilahdus." / "(2) Törmäys." jäävät edellisen kappaleen loppuun; L2-10:n osat c)–e) fy4-7:ssä
ja fy4-8:ssa ilman kappaleväliä; muutama yhden virkkeen kappale, joka vain päättää edellisen ajatuksen. FY4:n Sovella ja
esimerkkikoe odottavat samaa reviews.py-muutosta kuin FY1:n ja FY2:n.

FY5 tehty (claude/fy5-kappalejako): fy5-1…fy5-17 esimerkit ja ratkaisut kolmella kielellä, tiede ja pedagogiikka carry
(`md-paragraphs`), ulkoasu delta PASS. fy5-2:n tehtävissä aiemman reflow'n rivit jäivät jakamatta (jako niissä antaisi
tieteen ja pedagogiikan delta-katselmoinnin). Ratkaisuaskeleet, joiden vastausluku on b)-kohdassa (fy5-2 L2-06,
fy5-3 L3-05, fy5-14 L3-05), ja fy5-2 L2-03:n Kaava-vaihe (check_solutions) jäivät yhdeksi kappaleeksi; FY5:n Sovella ja
esimerkkikoe odottavat samaa reviews.py:n item-carrya kuin FY1 ja FY2.

FY2 tehty (#651): fy2-1…fy2-8 kolmella kielellä, tiede ja pedagogiikka carry, ulkoasu delta PASS. FY2:n Sovella ja
esimerkkikoe jäivät: kohteen siirto (`item_status`, `carry-item`) ei tunne luokkaa `md-paragraphs`, joten niiden
kappalejako vaatisi täydet tiede- ja pedagogiikkakatselmoinnit; ensin jaetun tiedoston muutos `reviews.py`:hin.

Esimerkkien vaiheet (esim. fy3-13, vaihe 1/7 "Tunnetut ja kysytty") ovat yksi tiivis kappale, jossa on luettuja
pisteitä, huomautus ja kysymys peräkkäin: vaikea lukea. Opettaja: "näissä teksteissä saisi kappalejakoa olla …
esim. 'Lämpötila'-alkuinen virke voisi olla jo omalla rivillään." Sääntö: yksi asia per kappale; tunnetut (lista tai
oma kappale), huomautukset omaksi kappaleekseen, kysytty viimeiseksi omaksi rivikseen (CLAUDE.md Readability:
"the question last as its own sentence"). Kirjataan sääntö NOTES.md §3:een ja lintiin varoitukseksi (vaiheen
kappale yli ~60 sanaa tai useita virkkeitä eri asioista), sitten korjataan kurssi kerrallaan (`/quality-audit
--fix`, 116 lukua, joissa "Tunnetut ja kysytty"); sisältömuutos, joten katselmoinnit scope-säännön mukaan
(typografia/kappalejako: odotettavasti visual delta, muut carry). Ensin pilotti yhdellä luvulla (fy3-13) opettajan
nähtäväksi.

### 8c-1. md-paragraphs myös Sovellaan, kokeisiin, yksiköihin ja tutkimuksiin (jaettu, koordinaattori 2026-11-16)

FY1:n työssä (#650) kaksi aukkoa `reviews.py`:ssä. (1) `carry-item` ei tuntenut luokkaa `md-paragraphs`: Sovellan,
esimerkkikokeen, yksikön, tutkimuksen tai TVT-ohjeen kappalejako kantoi vain väärällä nimellä "reflow" (sen näkymä
yhdistää välilyönnit), ja `- `-listamerkit eivät kantaneet lainkaan. (2) Kun sama rivi oli aiemmin reflow'ttu
(inline-kaava aligned-lohkoksi) ja nyt jaetaan kappaleisiin, `_md_paragraphs` näki kaavan sisällä yhden välilyönnin eron
(`d_\text{A} \approx` / `d_\text{A}\approx`) eikä luokitellut muutosta (en fy1-1:n harjoitukset). Korjaus: `para_view`
(listamerkit pois, välilyönnit yhdeksi) `item_view`n vaihtoehdoksi, `carry-item` ja `verify` tuntevat `md-paragraphs`-
rivit, ja `_md_paragraphs` jättää pois kaavan sisäiset välilyönnit, joita LaTeX ei näe (ei kahden kirjaimen välistä).
Testit `test_reviews.py`:ssä. Säännöt ennallaan: tiede ja pedagogiikka carry, ulkoasu delta. Sen jälkeen FY1:n Sovella,
esimerkkikoe ja en fy1-1:n harjoitusten kolme askelta.

## 8d. Käsitekorttien pitkät otsikot katkeavat keskeltä sanaa (opettaja 2026-11-13)

Kertaa luvun käsitteet -kortissa "Ominaislämpökapasiteet|ti" katkeaa ilman tavuviivaa (kortin otsikko piirretään
`templates/kortit.js`:ssä, `overflow-wrap` katkaisee mistä vain). Korjaus kerran kaikille korteille: sama
tavutus kuin taulukoissa (build.py:n pehmeät tavuviivat pitkiin yhdyssanoihin, tai `hyphens:auto` + `lang`), ja
tarvittaessa pienempi otsikkokoko pitkälle sanalle, niin että katkos osuu tavurajalle ja näkyy viivana
("Ominaislämpö-kapasiteetti"). Koskee myös kasitteet.html:ää, Kertauspakkaa ja Varmista käsitteet -osiota;
test_home.py:hin tapaus 360 ja 1280 px. Sivupohjan muutos, ei katselmointeja.

## 8e. Kuvien asettelu: turha pystyväli kuvan vierellä; kuva ja taulukko vierekkäin (opettaja 2026-11-13)

Teoriassa kappale, jonka viereen kuva asettuu (esim. höyrystymisen luvussa faasikaavio kappaleen "Kiehumispiste
riippuu paineesta" vieressä), saa ylä- ja alapuolelleen ison tyhjän välin: rivin korkeus tulee kuvasta ja teksti
keskittyy pystysuunnassa, joten edellinen kappale ja seuraava väliotsikko jäävät kauas. Korjaus kerran
(`build.py fig_rows`, site.css): teksti rivin yläreunaan, ja jos kuva on selvästi kappaletta korkeampi, joko
seuraava kappale virtaa kuvan viereen tai kuva siirtyy kappaleen alle (CLAUDE.md Lesson page 1: vierekkäin vain kun
ovat suunnilleen yhtä korkeita). Tarkista samalla, ettei kuva leikkaudu oikeasta reunasta. check_layoutiin
tarkistus tyhjälle pystyvälille kuvan vierellä 1280 ja 1920 px. Sivupohjan muutos, ei katselmointeja.

Samaan erään (opettaja 2026-11-13, kuvakaappaus FY3:n jään sulamisesta): kun kuvaa seuraa heti pieni taulukko tai
toinen kuva (esim. pylväskuva ja sen alla kolmen rivin arvotaulukko "Suure / Arvo"), ne asettuvat leveällä näytöllä
vierekkäin, toinen oikealle palstalle, eikä päällekkäin pitkäksi pinoksi. Sama `fig_rows`-päätös: vierekkäin, kun
molemmat mahtuvat ja ovat suunnilleen yhtä korkeita; puhelimella allekkain.

Lisäksi (opettaja 2026-11-13, fy3-8 leveällä näytöllä, "asettelu järkevämmäksi"): kaksi pientä taulukkoa (α kiinteille,
γ nesteille) pinoutuu vasempaan palstaan ja oikealle jää tyhjää, kun taas kuvat (tilavuuslaajeneminen, sauvan
pituuden kasvu) osuvat sattumanvaraisten kappaleiden ja taulukoiden viereen eivätkä sen tekstin viereen, jota ne
selittävät. Korjaa: peräkkäiset pienet taulukot vierekkäin samalle riville, kun mahtuvat; kuva aina sen kappaleen
viereen tai alle, jota se selittää (CLAUDE.md Readability: "Figures right after the paragraph, table or list they
explain"); ei tyhjää oikeaa palstaa taulukkopinon vieressä. Testaa fy3-8 1280, 1440 ja 1920 px ja ota ennen/jälkeen
-kuvat PR:ään.

Myös valokuvat (opettaja 2026-11-13, lämpövoimakoneen luku: höyryveturin kuva pitkän kappaleen alla vasemmassa
palstassa, oikea palsta tyhjä, "oikealle kuva"): kuvateksteineen valokuva asettuu leveällä näytöllä selittämänsä
kappaleen viereen oikeaan palstaan samalla säännöllä kuin SVG-kuvat. Kyseinen kappale (~130 sanaa) ylittää myös
120 sanan rajan: kirjataan kohtaan 8c (kappalejako) lukuun liittyväksi löydökseksi.


Ennen/jälkeen-kuviin myös FY1 (opettaja 2026-11-13): fy1-1 "Aine koostuu sisäkkäisistä rakenteista" (väli väliotsikon
ja kappaleen välissä, vieressä rakennekuva) ja "Atomi on ydintään kymmeniätuhansia kertoja suurempi" (väli kappaleen
ylä- ja alapuolella).
Toteutetaan kohdan 11 osana U3 (opettaja 2026-11-14).

## 8f. Animoitu kuva: hiukkasten värähtely ja lämpölaajeneminen (opettaja 2026-11-13, pilotti fy3-8)

Pilotti fy3-8 tehty (PR #649, yhteinen komponentti figlib `Fig(anim=True)` / `vibrate()`, site.css "Animated figures", lesson.js osa 7b); odottaa opettajan hyväksyntää (`reviews.py approve-figures fy3-8` vasta sen jälkeen). Muut luvut hyväksynnän jälkeen omina kohtinaan.

Opettaja kysyi, sopisiko looppaava animaatio fy3-8:n kuvan "kylmä / lämmin, d₀ / d > d₀" tilalle. Sopii, kun se
näyttää ilmiön, jota still-kuva ei näytä: lämpimässä hiukkaset värähtelevät laajemmin ja niiden keskimääräinen väli
kasvaa (hiukkaset eivät kasva). Toteutus yhteisenä komponenttina, jota muutkin luvut voivat käyttää:
- figures.py piirtää SVG:n kuten nyt; liike CSS/SMIL-animaationa, ei JavaScript-silmukkaa eikä canvasta.
- Animaatio pyörii loopilla vain näkyvissä ollessaan, kuvassa ▶/❚❚-painike (WCAG 2.2.2: yli 5 s liike pysäytettävissä),
  ja `prefers-reduced-motion` näyttää nykyisen still-kuvan. Tulosteessa ja vihkoissa still-kuva.
- Fysiikka: värähtelyn amplitudi kasvaa lämpötilan mukana ja tasapainoväli d > d₀ (epäsymmetrinen potentiaali);
  hiukkasten koko pysyy samana; "välit liioiteltu" -merkintä säilyy.
- Kuva on opettajan hyväksymä (`docs/teacher-figures.tsv`): uusi piirros vaatii uuden hyväksynnän ja tiedekatselmoinnin.
Ensin pilotti fy3-8:ssa opettajan nähtäväksi; muihin lukuihin (esim. kaasun paine, faasimuutokset) vasta sen jälkeen.

## 8g. Mallivastaukset perusperiaatteesta: kaava johdetaan (opettaja 2026-11-13)

Tehtävien, Sovella itsenäisesti -tehtävien ja esimerkkikokeiden mallivastausten Kaava-vaihe alkaa usein suoraan
yhdistetystä yhtälöstä (esim. "ηPt = rm, josta m = ηPt/r"). Opettaja: "näissäkin pitää lähteä perusperiaatteesta
liikkeelle ja johtaa kaava." Sääntö (NOTES.md §3, kirjataan energiatase-PR:ssä): ensin perusyhtälöt ($\eta =
E_\text{hyöty}/E$, $E = Pt$, $Q = rm$, energiatase), sitten johdettu kaava, sievennys symbolisesti loppuun ja vasta
sitten sijoitus. Korjataan kurssi kerrallaan `/exercises`- ja `/practice`-putkella (sisältömuutos, katselmoinnit
scope-säännön mukaan); järjestys kuten kohta 2. Ei rinnakkain saman kurssin tehtäväkatselmoinnin kanssa: yhdistetään
samaan ketjuun, kun kurssin katselmointi on vielä kesken (FY5, FY6, FY7).

## 8j. Pohdinnan kertaustehtävä liittyy pohdinnan ilmiöön (opettaja 2026-11-13)

Varattu: claude/fy4-pohdinta-kertaus (FY4)

fy4-1:n Pohdinnassa ilmiö on pyöräilijän matka kauppaan ja takaisin (matkamittari 4,0 km, siirtymä 0 m) ja kysymys
paikka–aika-kuvaajasta, mutta sen alla oleva "Kertaa yläkoulusta" -monivalinta kysyy juoksijan nopeutta (150 m,
20 s). Opettaja: "tämä ei tunnu loogiselta, tuo monivalinta ei liity tuohon pohdintaan." Sääntö (CLAUDE.md, FY3/FY1
-osio): Pohdinnan kertaustehtävä (`herata`-vaiheen retrieval-`choice`, docs/inquiry.md) kysyy pohjatietoa saman
ilmiön kautta, esim. tässä pyöräilijän keskivauhti tai matkan ja siirtymän ero. Korjaus: ensin fy4-1 (fi, en,
fi-easy), sitten kaikkien lukujen kertaustehtävät tarkistetaan pedagogisesti (`/quality-audit <id> --audit-only`
vain tämän kohdan osalta tai skripti, joka listaa kertaustehtävän ja ilmiön rinnakkain opettajalle) ja korjataan
kurssi kerrallaan. Sisältömuutos: pedagogy-katselmointi delta, science delta (uusi luku/arvo).

Järjestys (opettaja 2026-11-13, "joo hyvä"): Pohdinta-vaihe näytetään järjestyksessä ilmiön kuvaus → kertaustehtävä
samasta tilanteesta → pohdintakysymys (nyt kysymys on ennen kertaustehtävää). Sivupohjan muutos (inquiry.py/js),
kerran kaikkiin lukuihin; tehdään vasta, kun kertaustehtävät on korjattu liittymään ilmiöihinsä, ja kirjataan
CLAUDE.md:hen ja docs/inquiry.md:hen samassa PR:ssä.

## 8k. Opettajan hyväksymä tekstimuutos ohittaa katselmoinnin (opettaja 2026-11-13)

Nyt vain opettajan hyväksymät kuvat (`teacher-figure`) ja puhtaasti visuaaliset simulaatiomuutokset
(`presentation-only`) voivat siirtää katselmoinnit muutoksen yli. Kun opettaja on itse lukenut ja hyväksynyt
tekstimuutoksen (esim. fy1-1:n suuruusluokka-kappaleen lyhennys 13.11.), julkaisusääntö vaatii silti täyden
tiedekatselmoinnin, jos poistetuissa riveissä on kaavoja tai lukuja (#551). Uusi kategoria `teacher-text`, joka toimii
kuten `teacher-figure`: `reviews.py approve-text <id> [--lang]` kirjaa hyväksytyn muutoksen tarkan diffin tiedostoon
(esim. `docs/teacher-text.tsv`, ei käsin), `scope` antaa sille none/carry, `verify` johtaa sen uudelleen CI:ssä.
Rivi kirjataan vain opettajan nimenomaisesta hyväksynnästä; mikä tahansa muu muutos samassa luvussa katselmoidaan
normaalisti. Jaettuja tiedostoja (`scripts/reviews.py` ja testit): tehdään yksin.

## 8l-b. "Esimerkkiaineisto" myös ilman sulkeita pois otsikoista (opettaja 2026-11-16)

**Tila 2026-11-17 (#658):** `caption-label` tunnistaa nyt myös muodot "…, esimerkkiaineisto", "Esimerkkiaineisto: …"
(seuraava kirjain isoksi), "(…, esimerkkiaineisto)" ja "(keksitty esimerkkiaineisto[, ei mittaustulos])" sekä en
"example data" vastaavasti (`reviews.caption_label_free`). Merkintä on poistettu FY1-, FY2-, FY6- ja FY7-otsikoista
(fi, fi-easy, en). **Jäljellä FY4, FY5 ja FY8** (fy4-2, fy5-11, fy5-14, fy8-2, fy8-11; fi, fi-easy, en): niillä oli
kurssi-PR:t kesken samoissa tiedostoissa, joten ne tehdään kurssi kerrallaan, kun luokka on mainissa: otsikot
`caption_label_free`-funktiolla ja `reviews.py carry <id> --exercises [--lang]` (fi ensin, sitten fi-easy ja en).

Opettaja 16.11: "joo poistetaan". Kohta 8l (#607) poisti vain sulkeissa olevan merkinnän; noin 110 otsikkoa on muotoa
"…, esimerkkiaineisto" tai "Esimerkkiaineisto: …" (fi, en "example data", fi-easy). Jaettu: `reviews.py`:n
`caption-label`-luokka laajennetaan tunnistamaan nämäkin muodot (testit `test_reviews.py`:hin), ja merkintä poistetaan
kaikista `exercises.json`-otsikoista. Tehdään kohdan 8m jälkeen, kun kohdan 18/19 kurssi-PR:t eivät ole kesken samoissa
tiedostoissa, tai kurssi kerrallaan niiden mukana, jos luokka on jo mainissa.

## 10. Simulaatioiden käyttöliittymä (opettaja 2026-11-14)

Mittaus, päätökset ja rajaukset: `docs/audits/2026-11-14-simulaatioiden-kayttoliittyma.md`. Matalalla kannettavalla
(1366×650) simulaation kuva kapenee 384 px:iin ja sen tekstit noin 7 px:iin; puhelimella kuva vierii pois säätimiä
käytettäessä. Osat tässä järjestyksessä, kukin oma pull requestinsa. PR 1–PR 5 muuttavat jaettuja tiedostoja
(`templates/`, `scripts/`): ne tehdään yksin, yksi kerrallaan, ja yhdistetään ennen sisältömuutoksia. Pilotit (PR 2,
PR 4) pysähtyvät opettajan hyväksyntään ennen yleistystä. Yksikään osa ei muuta sim.js-tiedostoja, simulaatioiden
lang-tekstejä tai fysiikkaa.

- **PR 1 (tehty, #563)** kuvan todellinen leveys tekstikoon perustaksi (`sim-embed.js`) ja selaintesti 1366×650 (kuvan tekstit
  vähintään 10 px) omina CI-jobeinaan.
- **PR 2 (tehty, #588)** pilotti fy4-1: lukemat kuvan alle, toistorivi yhdelle riville, `.lab-side .sim-canvas`-säännön 25 rem:n
  varaus pienemmäksi, kuvausteksti pois kokeiden vierestä.
- **PR 3 (tehty, #591)** sama asettelu tyypeille A–C (aikaohjatut, jatkuvat, staattiset); tyyppi D, fy1-2, fy1-4 ja poikkeavat
  jäävät nykyiselleen.
- **PR 4 (pilotti tehty, #648; opettaja hyväksyi 2026-11-16 "Hyväksyn" ennen/jälkeen-kuvista 390 px:llä)** tarttuva kuva
  puhelimella, pilotit fy4-1 ja fy2-2 (`inquiry.SIM_STICK_PILOT`, `docs/audits/2026-11-16-sim-pr4-tarttuva-kuvat/`).
- **PR 4b: yleistys** tarttuva kuva kaikille `sim-card2`-korteille omana pull requestinaan (jaettu muutos); korkeille
  kuville raja (esimerkiksi fy7-4:n kuva on puhelimella 551 px: tarttuu vain, jos kuva vie enintään noin puolet
  ikkunasta, tai jää pois).
- **PR 5:** canvasin nimi ja kuvaus, valintaruudut 40 px:n kohteiksi, näkyvä kohdistus.

Myöhemmin kurssi kerrallaan, kunkin luvun seuraavan sisältömuutoksen yhteydessä katselmointeineen: tyyppi D (fy6-5,
fy6-6, fy6-9, fy6-12, fy6-13, fy6-14), fy1-2:n säätimien ryhmittely, näppäinvaihtoehto raahaukselle, nimien
yhtenäistäminen (Toisto / Tauko / Alusta) ja toistuvien seliterivien poisto.
PR 1:n mittauksesta (1366×650, koordinaattori 14.11): fy3-1 ja fy3-9 kutistavat tekstinsä itse sim.js:ssä (9 px,
fy3-9 jättää nimiöitä pois), ja fy3-6, fy3-8, fy4-5, fy6-11, fy7-14, fy8-10 ja fy8-16 saavat päällekkäisiä nimiöitä
384 px:n kuvassa (PR 1 nostaa tekstit vähintään 10 px:iin muuttamatta asettelua); korjataan sim.js:ssä, jos PR 2–3:n
leveämpi kuva ei riitä.

## 11. Tehtävänäkymä ja teorian taitto (opettaja 2026-11-14, UI/UX-auditoinnin tulos)

**Yleislinja** (opettaja 2026-11-14; kirjataan `CLAUDE.md`:hen U1:n PR:ssä): käyttöliittymään ei lisätä tekstiä, ja
käyttöliittymätekstejä poistetaan aina kun mahdollista. Uusi otsikko, ohjerivi, laskuri tai selite vaatii opettajan
luvan.

Jokainen osa U1–U4 on oma työntekijäketjunsa, haaransa ja luonnos-PR:nsä; ensimmäinen commit merkitsee osan
`Varattu: <haara>`. Kaikki muuttavat jaettuja tiedostoja (`templates/`, `scripts/`, `site.css`, `lang/`), joten ne
tehdään yksin, yksi kerrallaan, ja yhdistetään ennen sisältö-PR:iä. U4 on tehty (#561), U5 on tehty (#582). Järjestys: U1, U2, U3. U1–U3 aloitetaan vasta, kun kohdan 10 (simulaatioiden
käyttöliittymä) PR 1–PR 5 on yhdistetty, koska ne muuttavat samoja tiedostoja (`site.css`, `lesson.js`). Kohdat 8b, 8h
ja 8 (avattavat Virhekäsitys ja Tiivistelmä) pysyvät ennallaan ja mahtuvat väleihin. Fysiikan sisältöön, vastauksiin,
toleransseihin, tallennusavaimiin ja palautustiedoston muotoon ei kosketa. Mergen jälkeen katsotaan mainin CI-ajo.

### U1. Ydintehtävät auki Tehtävät-vaiheen alkuun
Nyt vaihe on kolme suljettua tasolaatikkoa, eikä yhtään tehtävää näy. Tason ohje sanoo "Ydintehtävät ensin", mutta ne
eivät ole ensin (FY4 luku 4: 4-4, 4-6, 4-13, 4-16).
- Luvun ydintehtävät näkyvät auki heti otsikon "6 Tehtävät" alla, allekkain, yhdessä kortissa, tehtävänantoineen ja
  vastaustoimintoineen. Tasoa ei tarvitse avata.
- Ei uutta otsikkoa, laskuria ("Ydintehtävät 2/4 tehty" ei palaa; opettaja poisti sen 13.11. ja vahvisti 14.11.),
  ohjeriviä eikä väliotsikkoa. Ydintehtävän tunnistaa nykyisestä Ydintehtävä-merkistä.
- Ydintehtävät ovat eri tasoisia: tasoilta 1 ja 2, kuten nyt (`build.py core_ids`: oletuksena kahden tason kaksi
  ensimmäistä tai `"core": true`; 14.11. 112/113 luvussa molemmilta tasoilta, yhdessä vain tasolta 1, tasolta 3 ei
  missään). Taso 3 ei tule ydintehtäviin (opettaja 14.11: "Riittää tasot 1 ja 2"). Järjestys: tason 1 ydintehtävät
  ensin, sitten tason 2. Luku, jonka ydintehtävät ovat yhdeltä tasolta, raportoidaan PR:ssä (sisältöpäätös, ei
  korjata tässä).
- Ydintehtävän merkin vieressä näkyy sen taso, **Perus** tai **Soveltava** (opettaja 14.11: "Voisi näkyä perus /
  soveltava"; tämä on hyväksytty käyttöliittymäteksti, lang-avaimet fi, en ja fi-easy, tasojen nykyisistä nimistä).
- Niiden alla nykyiset kolme tasoa suljettuina; tasossa näkyvät vain sen muut tehtävät. Tasojen otsikot ja
  "N/M tehty" toimivat kuten nyt, omilla määrillään.
- Lause "Ydintehtävät ensin, loput lisäharjoitusta." poistetaan (lang `level_lead_1` ja `level_lead_2`, kaikki kielet).
- Tallenna työ tiedostoon, Palauta ja Avaa tehtävät teorian viereen siirtyvät tasojen alle.
- Ehdottomat ehdot:
  - Tehtävä on DOM:ssa vain kerran (ei kopiota). Tunniste (`id`), numero (`data-num`), tarkistus, toleranssit,
    vihjeet, ratkaisut ja Yritä ensin -lukitus eivät muutu. Tallennetut vastaukset ja tehty-tiedot säilyvät.
  - `scripts/palautus_tasks.py` päättelee tehtävän tason ympäröivästä `details.level`-laatikosta (rivi ~131), joten
    ydintehtävä menettäisi tasonsa opettajan arviointinäkymässä: `<li>` saa oman tasotiedon (esim. `data-level`), ja
    se luetaan sieltä.
  - `templates/lesson.js`: tasokohtainen tehty-laskuri (~rivi 69), pakollisten vastausten sääntö (~240), tehtävät
    teorian vieressä (~845–875) ja koko näytön tila (~996) olettavat tehtävien olevan tasolaatikoissa; ne
    päivitetään. Rivinumerot ovat 14.11. tilanteesta.
  - Annetut tehtävät (`annetut.json`), Syventävä-merkki, tulostus ja vihkot toimivat.
  - Toimii ilman JavaScriptiä: rakenne tulee `build.py`:stä, ei skriptin siirtämänä.
  - fi, en ja fi-easy; FY1–FY8, FY9 ja FY14.
- Tiedostot: `scripts/build.py` (tehtäväosion kokoaminen), `templates/lesson.js`, `scripts/palautus_tasks.py`,
  `site.css`, `lang/*.json`.
- Testit: `test_progress`, `test_palautus`, `test_tehty`, `test_writepad`, `test_koko`, `check_layout` (kaikki
  leveydet, avoimet tilat), `palautus_tasks.py --check`, `check_a11y`. Jaettu muutos: selaintestit koko sivustolle
  käsin ennen yhdistämistä.
- Samassa PR:ssä `CLAUDE.md`: "Tehtävät last" korjataan (sivulla Tehtävät on vaihe 6 ja Testaa ja arvioi vaihe 7),
  uusi rakenne kuvataan, ja yleislinja kirjataan.
- Ei julkaistua pilottia: ennen/jälkeen-kuvat PR:ään (FY4 luku 4, 390 ja 1280 px, suljettuna ja yksi tehtävä
  tarkistettuna), ja työ pysähtyy opettajan hyväksyntään.

### U2. Tehtäväkortin ohjainten järjestys (U1:n jälkeen)
Nyt Vastaus ja Näytä ratkaisu ovat otsikkorivillä ennen tehtävänantoa; täytetty päänappi on Kirjoita ratkaisu ja
Tarkista on ääriviivanappi; puhelimella otsikkorivi rivittyy kahdelle riville ja lukko jää irralleen. Järjestys
kortissa:
1. numero, merkit (Ydintehtävä, Annettu, Syventävä) ja Avaa isoksi;
2. tilanne ja kysymys;
3. kuva tai taulukko;
4. vastauskenttä, yksikkö ja Tarkista (täytetty päänappi); Kirjoita ratkaisu samalla rivillä ääriviivanappina
   (puhelimella omalla rivillään Tarkista-rivin alla);
5. palaute heti kentän alla;
6. erotinviivan alla Vihjeet, Vastaus, Näytä ratkaisu ja lukko.

Ei uusia tekstejä (lukon selite pysyy nykyisenä title- ja ruudunlukijatekstinä). Sama järjestys monivalinta- ja
kirjoitustehtävissä. Lukituksen aria-kytkennät säilyvät. Kaikki, mitä skripti lisää korttiin, kirjataan
`palautus_tasks.py`:n siivouslistaan. Tiedostot: `templates/lesson.js` (otsikkorivin kokoaminen, ~rivi 338),
`site.css`. Testit: samat kuin U1 ja `check_a11y`. Ennen/jälkeen-kuvat 390 ja 1280 px.

### U3. Teorian taitto: vaihtoehto B (korvaa entisen kohdan 7)
Nykyinen 38 rem:n palsta säilyy, ja asettelu korjataan kohdan 8e mukaan:
- teksti kuvarivin yläreunaan, ei tyhjää väliä kappaleen ylä- ja alapuolella;
- valokuva kuvateksteineen selittämänsä kappaleen viereen oikealle;
- kaksi pientä taulukkoa vierekkäin, kun mahtuvat;
- jos kuva on selvästi kappaletta korkeampi, seuraava kappale sen viereen tai kuva alle.

Tiedostot: `build.py` `fig_rows`, `site.css`, `check_layout.py` (tarkistus tyhjälle pystyvälille). Ennen/jälkeen-kuvat:
fy3-8 ja fy4-3 leveyksillä 1280, 1440 ja 1920 px sekä fy1-1. Luonnoksessa Teoria-vaihe lyheni noin 8 % (fy3-8:
4082 → 3775 px, fy4-3: 3703 → 3380 px leveydellä 1280 px).

### Ei tehdä (opettaja 2026-11-14)
- Ei Aloita-riviä moduulisivulle; Jatka-rivi pysyy ennallaan.
- Ei "Näytä kaikki tehtävät" -toimintoa.
- Ei etusivun uusia ryhmäotsikoita.
- Ei marginaalipalstaa eikä keskitettyä lukupalstaa.
- Ei yhden luvun julkaistua pilottia: esikatselukuvat riittävät.

## 11b. FY9: adaptiivinen YO-valmentaja (opettaja 2026-11-14)


Suunnitelma: `docs/FY9_ADAPTIVE_PLAN.md` (#566). Opettaja hyväksyi 14.11 suunnitelman ja kaikki sen suositukset
P1–P12: osaamisalueet ovat kuusi osaamista (`competencies.json`); tilojen sanat hyväksytään PR 4:ssä; oma
valmentajasivu; FY9-sivulle rivi "Tänään: 3 tehtävää" Jatka-rivin tilalle; jokainen uusi käyttöliittymäteksti
hyväksytään PR kerrallaan; näyttöloki vain varmuuskopioon, ei palautukseen; minikoekoosteet agentti ehdottaa ja
opettaja hyväksyy; mitoitus 3 min/piste; laajennus muiden moduulien Sovella-tehtäviin myöhemmin; Abitti 2 omana
TVT-ohjeena; paikallinen kielimalli vain selvityksenä myöhemmin. Ei palvelinta, ei tekoälyrajapintaa, ei kustannuksia
opiskelijalle.

Järjestys (suunnitelman kohdat 8–9, hyväksymiskriteerit ja testit siellä): PR 1 YTL/Abitti-tietojen tarkistus
(sisältö, delta) voi alkaa heti; PR 2–8 (tehtäväindeksi, näytön kirjaus, osaamisnäkymä ja suositukset, vaikea vaihe,
koetila ja minikokeet, kertauspolku, kielten tarkistus) muuttavat jaettuja tiedostoja, joten ne tehdään yksin, yksi
kerrallaan, kohdan 10 PR 1–PR 5:n ja kohdan 11 U1:n jälkeen; PR 9 Abitti 2 -ohje (sisältö); PR 10 kielimallin
selvitys (dokumentti). Arvio noin 2,5–3,5 M tokenia.

## 17. Kehitys ilman kirjautumista (opettaja 2026-11-15)

Ohjeet, nykytila, testit ja päätökset K1–K9: `docs/audits/2026-11-15-kehitys-ilman-kirjautumista.md`.
Jokainen osa on oma ketjunsa, haaransa ja luonnos-PR:nsä; lähes kaikki muuttavat jaettuja tiedostoja, joten ne
tehdään yksin, yksi kerrallaan. Uusien käyttöliittymätekstien sanamuodot luetellaan PR:n kuvauksessa, ja opettaja
hyväksyy ne yhdistämällä. Tallennusavaimia, tiedostomuotoja ja korttien id:itä ei muuteta.

- **17a Verkoton käyttö ja asennus:** PR 1 service worker (käydyt sivut toimivat verkotta), PR 2 manifesti ja
  pysyvä tallennus, PR 3 moduuli laitteelle (pilotti FY3, pysähtyy hyväksyntään).
- **17b Koko työ yhteen tiedostoon:** PR 1 varmuuskopio `ruukkilabra-kaikki` v1 (myös korttipakka), PR 2 jakovalikko
  puhelimessa.
- **17c Yleisvirheiden tunnistus:** PR 1 yleinen tunnistus (etumerkki, kertaluokka, aika, kelvin) `lesson.js`:ään,
  kohdan 10 PR 2–PR 5:n ja kohdan 11 U1–U3:n jälkeen; PR 2 tehtäväkohtaiset virheet kurssi kerrallaan
  sisältömuutosten yhteydessä.
- **17d Ajoitettu kertaus:** PR 1 kortit palaavat pakkaan 5, 10 ja 20 vrk:n päästä; PR 2 sekoitettu kertaus
  FY1–FY8:lle FY9-valmentajan laajennuksena, kohdan 11b PR 4:n jälkeen.
- **17e Luokan yhteenveto arviointisivulle:** tehtävittäin ja tavoitteittain, ilman nimiä; 17c PR 1:n jälkeen.
- **17f Hakemistot ja haku:** PR 1 kaavahakemisto, PR 2 simulaatiogalleria, PR 3 koko sivuston haku.

Järjestys: 17a PR 1–2, 17b PR 1, 17f PR 1–2, 17c PR 1, 17e, 17d PR 1, sitten 17f PR 3, 17a PR 3, 17b PR 2.

## 18. Oikoluvun korjaukset FY1–FY9 (opettaja 2026-11-15)

Tehty: FY6 (PR #615). FY3 tehty: claude/oikoluku-fy3 (PR #613). FY7 tehty (PR #617, claude/fy7-oikoluku). P6 (fy7-8:n kaavanimi) ja fy7-8:n simulaation selite (lang/fi.json, lang/fi-easy.json "lämmöksi") tehdään kohdassa 8m.

Ohjeet ja päätökset P1–P9: `docs/audits/2026-11-15-oikoluku.md` kohdat 4–11 ja 13. Kaikki luvut, kurssi kerrallaan,
ilman pilottipysähdystä (opettaja: "kaikki luvut vaan, ei ongelma jos tokeneita menee"); kulutus raportoidaan, mutta
budjetti ei pysäytä työtä. Katselmointi on delta-katselmointi vain muuttuneista kohdista; jos `reviews.py scope` vaatii
täyden katselmoinnin, työntekijä kertoo koordinaattorille ennen ajoa. Kurssin kaikki korjaukset (väitteet,
merkitsevät numerot, termit, "lämmöksi", likiarvorivit, kieli) samalla kierroksella (P2), myös tehtävänannot,
inquiry.json, kuvien tekstit ja käännökset. Kurssi aloitetaan, kun kohta 8m on yhdistetty ja kurssin kohdan 5d
leikkautuvat kaavat ovat mainissa (FY8 odottaa #601:tä). Avoin kohta 12 ratkesi päätöksellä P9: pieniä arvoeroja ei
muuteta. Yksi kurssi = yksi haara ja yksi PR; rinnakkaisuus kuten jonon alussa (kiireellä ei ylärajaa).
Päätös (opettaja 2026-11-15): raja-arvotehtävien tarkistus hyväksyy jatkossakin poikkeaman molempiin suuntiin
(esim. fy6-16 L2-05: 10,4 ja 10,5 kW), eikä yksipuolista tarkistusta tehdä. P7c koskee vain mallivastauksen pyöristystä.
FY1 tehty: claude/fy1-oikoluku (PR #614).
FY5 tehty: claude/fy5-oikoluku-aineisto (PR #624); samassa PR:ssä kohdan 19 aineistotehtävät FY5-A1…A5.
FY8 tehty: claude/fy8-oikoluku (PR #621); samalla kokeen ja Sovellan leikkautuvat kaavat (5d).
Kohta 8m (#618) lisäsi `physics_phrases.py`:hen säännöt heat-into (P1) ja liikekitka: kurssin "lämmöksi"-virkkeet ovat
`docs/physics-phrases-known/<kurssi>.tsv`:ssä (vain fi; samat virkkeet fi-easy- ja en-versioissa korjataan samalla), ja korjaus poistaa
kurssin rivit. FY9:n lepokitkan nimitykset ("suurin lepokitka") yhtenäistetään 9c:ssä (#602).
Kitkan ja energian konseptikatselmoinnin löydökset (8m:ää vanhempia): `docs/audits/2026-11-15-kitka-konseptikatselmointi.md`.
FY9 tehty: claude/fy9-oikoluku-aineisto (PR #626); samassa PR:ssä kohdan 19 aineistotehtävät FY9-A1…A5 (fy9-ympyraliike-s7, fy9-magnetismi-valo-s7, fy9-moderni-s7, fy9-energia-s7, fy9-kaasut-s7).
FY4 tehty: claude/fy4-oikoluku-aineisto (PR #625); samassa PR:ssä kohdan 19 aineistotehtävät FY4-A1…A5. Lähteestä tarkistamatta: fy4-5 les:316 (YTL) ja fy4-11 les:290 (OTI).
FY2 tehty: claude/fy2-oikoluku-aineisto (PR #632); samassa PR:ssä kohdan 19 aineistotehtävät FY2-A1…A5. Kaikki kurssit tehty; jäljellä vain `docs/physics-phrases-known/`:n rivit (FY5, FY6, FY9).

## 19. 45 soveltavaa aineistotehtävää FY1–FY9 (opettaja 2026-11-16)

Toimeksianto sanatarkasti: `docs/audits/2026-11-16-aineistotehtavat.md` (viisi tehtävää per kurssi, tunnisteet FY1-A1 …
FY9-A5, lähdelinkit tarkistetaan, malliratkaisut, kolme kieltä). Tehtävät lisätään nykyiseen tehtävärakenteeseen sopivan
luvun soveltaviksi (taso 2–3, `kind` aineisto), FY9:ssä kertauskokonaisuuteen tai yksiköihin. Lähteiden palvelimet ovat
ympäristön sallituissa (16.11).
FY8 tehty: FY8-A1…A5 (PR #635, oma PR): fy8-3-L2-09, fy8-13-L2-09, fy8-12-L2-08, fy8-9-L2-08, fy8-1-L2-10. PhET Photoelectric (A5) toimii selaimessa CheerpJ:llä; sen arvot luettiin simulaation omasta ohjelmasta (photoelectric_all.jar), koska CheerpJ:n palvelin ei ole ympäristön sallituissa.
PR:ien yhdistäminen (opettaja 2026-11-16: "jos saat yhdisteltyä PR niin tee, jos vaarana että homma sotkeutuu älä tee"):
kohta 19 tehdään samassa PR:ssä saman kurssin vielä aloittamattoman työn kanssa (FY4, FY5, FY9 ja FY2: kohta 18; FY3, FY6
ja FY7: kohta 5d), ei koskaan jo katselmoitavana olevaan PR:ään; FY1 ja FY8 omana PR:nään kurssin nykyisen PR:n jälkeen.
FY5 tehty: FY5-A1…A5 (PR #624, kohdan 18 FY5:n kanssa): fy5-6-L2-09, fy5-12-L2-10, fy5-14-L2-09, fy5-17-L2-10, fy5-16-L2-10.
FY9 tehty: FY9-A1…A5 (PR #626, kohdan 18 FY9:n kanssa).
FY6 tehty: FY6-A1…A5 (PR #627, kohdan 5d FY6:n kanssa): fy6-3-L2-08, fy6-7-L2-09, fy6-15-L2-09, fy6-9-L2-09, fy6-13-L2-09. Opettaja avaa Tukesin kaksi linkkiä (A3, A4) selaimessa ennen yhdistämistä: sivusto ei vastaa automaattisiin hakuihin.
FY4 tehty: FY4-A1…A5 (PR #625, kohdan 18 FY4:n kanssa): fy4-11-L2-10, fy4-7-L2-10, fy4-9-L2-09, fy4-10-L2-10, fy4-8-L2-10.
FY2 tehty: FY2-A1…A5 (PR #632, kohdan 18 FY2:n kanssa): fy2-8-L2-10 (A1), fy2-7-L2-10 (A2), fy2-8-L3-06 (A3), fy2-3-L2-09 (A4), fy2-8-L2-11 (A5). Electricity Maps korvattu OWID:lla ja Fingridillä (`docs/audits/2026-11-16-fy2-aineistot.md`).
FY3 tehty: FY3-A1…A5 (PR #628, kohdan 5d FY3:n kanssa): fy3-9-L2-10, fy3-8-L2-10, fy3-11-L2-10, fy3-6-L2-10, fy3-7-L2-10.
FY1 tehty: FY1-A1…A5 (PR #634, oma PR): fy1-7-L2-09, fy1-4-L2-09, fy1-3-L2-09, fy1-2-L2-08, fy1-7-L2-10. A2:n Ilmatieteen laitoksen avoin rajapinta (opendata.fmi.fi) ei ole ympäristön sallituissa: tehtävä ohjaa hakemaan oman aineiston, ja varalla on merkitty keksitty esimerkkitaulukko.
FY7 tehty: FY7-A1…A5 (PR #633, kohdan 5d FY7:n kanssa): fy7-8-L2-10 (A1), fy7-9-L2-10 (A2), fy7-9-L2-11 (A3), fy7-7-L2-08 (A4), fy7-2-L2-10 (A5). Lähteet tarkistettu 16.11.; A5:n avaruussäädiagrammi piirretään JavaScriptillä eikä sen arvoja voinut lukea, joten tehtävässä on merkitty esimerkkitaulukko; A1:n aineisto ei kerro, miksi jännitteet ovat korkeita, joten a) kysyy vain sen, mitä sivulla on.

## 13. Englanninkieliset käsitekortit FY6 ja FY8 (opettaja 2026-11-13: tehdään myöhemmin)

`kortit/en/` ei sisällä tiedostoja `fy6.json` ja `fy8.json`, joten englanninkielisillä FY6- ja FY8-sivuilla ei ole
käsitekortteja eikä alleviivauksia.
Järjestys (opettaja 2026-11-15): kohdan 18 jälkeen ja ennen lopputarkistusta (15), jotta tarkistus kattaa myös kortit.

## 15. Kustannustoimituksellinen lopputarkistus FY1–FY8 (opettaja 2026-11-14) (kevennetty, opettaja 2026-11-16)

Tavoite: FY1–FY8-oppimateriaali kaupallisen kustantajan julkaisuvalmiutta vastaavalle laatutasolle. Tarkistaja toimii
kokeneena lukion fysiikan kustannustoimittajana, fysiikan didaktiikan asiantuntijana ja ohjelmistojen
laadunvarmistajana. Pedagoginen perusrakenne on jo toimiva, eikä sitä uudisteta ilman todettua tarvetta: tämä on
tarkistus- ja viimeistelyprojekti, ei uudelleensuunnitteluprojekti. **Ensin pelkkä raportti; korjaukset vasta, kun
raportti on valmis ja opettaja on lukenut sen.**

Tarkistetaan jokaisesta oppitunnista:
1. fysiikan teorian, käsitteiden ja kaavojen oikeellisuus;
2. esimerkkilaskujen, tehtävien ja malliratkaisujen oikeellisuus;
3. simulaatioiden fysikaaliset mallit, laskenta, parametrit ja tehtävänannot;
4. kuvitusten fysikaalinen oikeellisuus, visuaalinen selkeys ja yhdenmukaisuus;
5. tehtävien pedagoginen monipuolisuus suhteessa oppitunnin tavoitteisiin;
6. oppimistavoitteiden ja itsearvioinnin vastaavuus;
7. suomen kielen täsmällisyys, käsitteiden yhdenmukaisuus ja kielitietoisuus;
8. käyttöliittymän, saavutettavuuden ja tallennustoimintojen toimivuus.

Työskentelytapa:
- Kevennetty (opettaja 2026-11-16, 'ota se kevyt 15'): kohdat 1–8 on jo katettu jokaisen luvun kolmella katselmoinnilla, oikoluvulla (18) ja CI:n tarkistuksilla. (1) Automaattiset läpikäynnit kaikista kursseista: concepts.py (käsitteiden, merkintöjen ja selitysten yhdenmukaisuus kurssien välillä), coverage.py --all, physics_phrases, check_a11y; yksi raportti. (2) Otos: täysi kustannustoimituksellinen tarkistus yhdelle luvulle per kurssi (8 lukua), raportti opettajalle ensin. (3) Laajennus vain, jos otos löytää kriittisiä virheitä, ja silloin vain sille kurssille.
- LOPS 2019 (`docs/lops2019/`) on opetussuunnitelmallinen vertailuperusta.
- Julkaistuja oppikirjoja ei käytetä eikä mainita vertailuaineistona (opettaja 2026-11-14).
- Virheitä ei oleteta. Muutosta ei ehdoteta vain siksi, että asian voisi ilmaista toisin.
- Tehtävien tunnisteita, oikeita vastausarvoja tai opiskelijan tallennusmuotoja ei muuteta ilman todettua virhettä.
- Uusia tehtäviä tai simulaatioita ei lisätä ilman perusteltua pedagogista puutetta.
- Lähdekoodia ei muokata tässä vaiheessa.

Raportti (`docs/audits/`, kurssi kerrallaan) ilmoittaa jokaisesta todetusta ongelmasta: moduuli ja oppitunti,
tiedosto ja yksilöitävä kohta, nykyinen toteutus, todettu ongelma ja sen perustelu, täsmällinen korjausehdotus,
prioriteetti (kriittinen, merkittävä tai pieni) ja tarvittava tarkistus korjauksen jälkeen. Raportti erottaa
varmennetut virheet, mahdolliset ongelmat ja vapaaehtoiset parannusehdotukset. Oppitunti, jolla ei ole korjattavaa,
merkitään hyväksytyksi.

**Toiseksi viimeinen kohta** (opettaja 2026-11-14): aloitetaan vasta, kun kaikki muut jonon kohdat paitsi vihkot
(kohta 16) on tehty. Työ on laaja
(113 lukua), joten se tehdään kurssi kerrallaan omissa ketjuissaan (`/quality-audit <id> --audit-only`, budjetit
`.claude/commands/lesson.md`).
Järjestys (opettaja 2026-11-15): kohtien 17, 18 ja 13 jälkeen; sen jälkeen 14 ja viimeisenä 16.

## 14. Ahjo ja LUMA-tutor yhteiseen jaksopohjaan (opettaja 2026-11-13; järjestys 2026-11-14)

Kilparobotiikka on kirjoitettu jaksopohjan lohkoina (#516–#517, `scripts/jaksot.py`); Ahjo ja LUMA-tutor piirtyvät
vielä osin omilla moduuleillaan (`ahjo.py`, `lumatutor.py`). Siirretään ne samaan pohjaan niin, että sivut pysyvät
tavulleen samoina kuten Kilparobotiikassa, ja puuttuvat lohkot lisätään yhteiseen lohkokirjastoon. Jaettuja
tiedostoja: tehdään yksin.
Järjestys (opettaja 2026-11-15): juuri ennen vihkoja (16).

## 16. Vihkot FY1–FY8 nykyisellä tiiviillä asettelulla (opettaja 2026-11-13; jonon viimeinen 2026-11-14 ja 2026-11-15)

Tulostettavat A5-vihkot (`python scripts/print_book.py <C> --lang fi|en --publish`, README "Printed A5 book") kaikille
kursseille FY1–FY8 sivuja säästävällä tiiviillä asettelulla (#393). FY1–FY4:llä vihko on (7.11.), mutta sisältö on
muuttunut sen jälkeen (kaavat taulukkokirjan muotoon, käsitteet, korjaukset), joten ne tehdään uudelleen; FY5–FY8 ovat uusia. Kurssin
vihko tehdään vasta, kun sen kohdan 3 kaavat taulukkokirjan muodossa on yhdistetty, ettei sitä tarvitse tehdä kahdesti. Rakenna sivusto
vihkojen jälkeen (Vihkot-sivu).
Opettaja 2026-11-15: vihkot vasta kohtien 17 ja 18 jälkeen, koska oikolukua ei kannata tehdä vihkon jälkeen.

## Kirjattu päätös: teorian taitto, vaihtoehto B (opettaja 2026-11-14)

Opettaja vertasi kolmea vaihtoehtoa 14.11. ja valitsi B:n: nykyinen 38 rem:n palsta säilyy, ja asettelu korjataan
kohdan 8e mukaan (kohta 11, U3). Entinen kohta 7 (keskitetty tekstiraita ja marginaaliraita) poistettiin jonosta.
Perustelu: marginaaliin mahtuva kuva olisi noin neljänneksen pienempi, ja Teoria olisi ainoa keskitetty vaihe.

## Kirjattu päätös: luvut ilman käsitekortteja (opettaja 2026-11-13)

Luvut fy3-13, fy3-14, fy3-16 ja fy4-16 jäävät ilman omia kortteja ja alleviivauksia (#526:n siirtojen jälkeen).
Kortteja ei lisätä niihin.

## Kirjattu päätös: mallit takaisin alkuperäisiin (opettaja 2026-11-16)

Opettaja 16.11: "Palaa alkuperäiseen" (tokenit loppumassa). #620 (kaikki roolit Fable, 15.11) on peruttu: agentit ja
komennot ajetaan taas `/lesson`-komennon mallitaulukon mukaan (Sonnet, tiedekatselmointi Opus), ja Fable vaatii
opettajan sanan.

## Kirjattu päätös: kevyempi katselmointi, viisi rinnakkain (opettaja 2026-11-16)

Opettaja 16.11 (tokenien säästämiseksi): "jos pyöristyskorjaus niin ei tarvitse täyttä katselmointia", "Rajoitetaan
rinnakkaisuus viiteen", "Ei uusia täysiä kierroksia hiontahuomioista".
- Muuttunut luku, kaava, symboli, yksikkö, vastaus, toleranssi tai `answers.py` vaatii tiedekatselmoijalta deltan, ei
  täyttä katselmointia (`reviews.py` RULES `numbers`, `answers`): se katsoo muuttuneet rivit asiayhteydessään ja
  tarkistaa niiden laskut. Uusi tehtävä tai uusi sisältö ja simulaation koodi katselmoidaan kuten ennen.
- Rinnakkain enintään viisi työntekijää (juuren `CLAUDE.md` sääntö 3).
- Polish-huomioista ei ajeta uutta katselmointikierrosta: ne kirjataan PR:ään, ja vain Blocking- ja Major-huomiot
  korjataan ja katselmoidaan uudelleen.
