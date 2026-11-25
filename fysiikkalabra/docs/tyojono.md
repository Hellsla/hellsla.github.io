# Työjono

Opettajan päättämät tulevat työt, joita ei ole vielä aloitettu. Jokainen kohta tehdään omana pull requestinaan;
valmis kohta poistetaan tästä samassa pull requestissa ja sen lyhyt yhteenveto lisätään `tyojono-loki.md`:hen.

Tämä on ainoa työjono (opettaja 2026-11-13): ei GitHub Issuesia eikä erillisiä listoja. Kohdat ovat
`docs/ROADMAP.md`:n järjestyksessä. Kohdan ottava ketju katsoo ensin avoimet pull requestit, merkitsee kohtaan
ensimmäisessä commitissaan `Varattu: <haara>` ja avaa luonnos-PR:n heti, jotta muut ketjut näkevät varauksen
(repon juuren `CLAUDE.md`). Saman kurssin kohdat tehdään peräkkäin, eri kurssien yleensä enintään kolme rinnakkain
(opettaja 2026-11-22: "I need more usage, add more agents" → yläraja pois toistaiseksi; aiemmin kolme, 2026-11-19); kun opettaja sanoo työn kiireelliseksi, ei ylärajaa (opettaja 2026-11-15).
Jonon pitää pysyä lyhyenä (alle 200 riviä): tässä on vain se, mitä tekijä tarvitsee aloittaakseen; täysi vanha teksti,
tehdyt kurssit ja opit ovat `docs/tyojono-loki.md`:ssä ("loki §N"), kirjatut päätökset `docs/decisions/tyojono-paatokset.md`:ssä.

## 0. Päivitystyön tehostaminen (opettaja 2026-11-17: "Laita kaikki seuraavaksi työjonoon")

Tehdään ennen uusia kurssikohtaisia läpikäyntejä. Tehty: 0a (`scripts/round.py`, #670), 0b (ohjetiedostot, #673), 0c (esitystapaluokka, #677; loki §0c), 0e (ulkoasun delta vain suomeksi, kun muutos on kielineutraali; sääntöteksti odottaa opettajan hyväksyntää, PR draft; loki §0e), 0d (CI:n selain pilvi-istuntoihin; ei ympäristömuutosta, `ci_env.py` käynnistää Dockerin itse; `round.py` tarkistaa matalan kloonin ja riippuvuudet).
Osat 0e ja 0g muuttavat jaettuja tiedostoja: ne tehdään yksin, yksi kerrallaan, tässä järjestyksessä, ja yhdistetään
ennen sisältö-PR:iä. Jokainen osa raportoi PR:ssä, mitä se säästi (vuorot, tokenit, yhdistykset, katselmoinnit ennen ja jälkeen).

### 0f. Yksi läpikäynti per kurssi (työtapa, ei koodia)
Sama kurssi on käyty läpi erikseen kohdissa 5d, 8c, 8l-b, 18 ja 19, ja 8g ja 8j ovat tulossa; jokainen läpikäynti tuo
omat ulkoasukatselmointinsa kolmella kielellä, `site/`-rakennuksensa ja mainin yhdistyksensä. Tästä eteenpäin kurssin
avoimet kohdat tehdään yhdessä PR:ssä (laajennus kohdan 19 päätökseen 16.11. "jos saat yhdisteltyä PR niin tee"):
mekaaniset muutokset (8c, 8l-b:n jäännös, 5d:n tähteet) samaan PR:ään kurssin seuraavan sisältömuutoksen (8g, 8j)
kanssa, jonka katselmoinnit kattavat ne. Ei koskaan jo katselmoitavana olevaan PR:ään. Koordinaattori kirjaa jokaiselle
kurssille (FY1–FY9) yhden rivin: mitkä kohdat ovat auki ja missä PR:ssä ne tehdään. Voimaan heti; ei odota muita osia.

### 0g. `site/` pois sisältö-PR:istä (ensin suunnitelma, pysähdys opettajan hyväksyntään)
PR 1 varjo #693 ja PR 2 kytkentä #796 (+ deploy-varapolku #802) yhdistetty 2026-11-22; PR 3 poisto (#822, opettaja 2026-11-23): `fysiikkalabra/site/` ei ole enää seurattu, `scripts/site_migrate.sh` avoimille haaroille; jäljellä PR 4 (ohjeiden viimeistely, mitattu säästö). Suunnitelma: claude/0g-site-suunnitelma (#687, suunnitelma `docs/audits/2026-11-17-0g-site-suunnitelma.md`, hyväksytty). Päätökset (opettaja 2026-11-17): A `site/` poistuu kokonaan; vanhat linkit → `ruukkilab.fi` PR 3:ssa; esikatselu = CI-artefakti + muuttuneiden sivujen lista; siirtymä PR 1 varjo → PR 2 kytkentä → PR 3 poisto (ajankohta sovitaan erikseen) → PR 4 mittaus. Toteutus yksin, yksi PR kerrallaan.
Jokainen yhdistetty PR vanhentaa kaikkien avoimien PR:ien `site/`-kopion, joten jokainen haara yhdistää mainin ja
rakentaa `site/`:n uudelleen keskimäärin 1,6 kertaa (juuren `CLAUDE.md` sääntö 4). Tavoite: sisältö-PR ei sisällä
`site/`-muutoksia; CI rakentaa sivuston ja `ruukkilabra-deploy.yml` julkaisee rakennetun version mainin ajon jälkeen.
Ensin pelkkä suunnitelma (`docs/audits/`), ei koodia: (1) miten `ci_scope.py` päättelee muuttuneet sivut ilman
committoitua `site/`-diffiä (kahden rakennuksen vertailu tai lähteistä); (2) miten "committoitu `site/` vastaa tuoretta
rakennusta" -tarkistus korvataan; (3) miten opettaja näkee PR:n vaikutuksen sivuihin ennen yhdistämistä (esikatselu
CI:n artefaktina tai `reviews.py impact`); (4) säilyykö `site/` repossa CI:n kirjoittamana vai poistuuko se kokonaan;
(5) julkaisun palautus virhetilanteessa; (6) siirtymä avoimille PR:ille. Julkaisusääntö ei muutu: sivulle pääsee vain
katselmoitu sisältö, ja yhdistäminen on opettajan julkaisupäätös. Toteutus omina PR:inään vasta hyväksynnän jälkeen.

### 0h. Generoidut tiedostot CI:lle (opettaja 2026-11-17, 0g:n jälkeen)
`docs/figures/catalog.json`, `docs/assessment/<COURSE>.md` ja `docs/coverage/<COURSE>.md` aiheuttavat saman mainin yhdistys -ristiriidan kuin `site/`. CI generoi ne ja tarkistaa vastaavuuden; `figcat.py find` generoi katalogin tarvittaessa paikallisesti. Ensin suunnitelma, kuten 0g (`docs/audits/2026-11-17-0g-site-suunnitelma.md` osa 9). Jaettu muutos: yksin, 0g:n jälkeen.
Tehty ja poistettu jonosta: 8q (#690), 8r (#694), kuvan .side-arvio (#775); kohta 22 (#751); kohta 8 (virhekäsityslaatikot #713, sisältö kaikilla kursseilla FY1–FY8, tarkistettu 2026-11-23); kohta 8f (animaatiot FY3 #757, FY4 #761). Muut opettajan päätökset 2026-11-23: fy7-5-simulaation Nopeus-valikon nimi ennallaan; hellsla.github.io:n sitemap.xml:stä poistettu ruukkilab.fi-osoitteet (ruukkilab.fi:llä oma sivukartta).

## 4. FY10:n tutkimusten ja TVT-ohjeiden korjaukset (opettaja 2026-11-13)
Taulukko-otsakkeet 390 px tehty (#731). Auditointi tehty (#536), Major-korjaukset ja sisältöosa tehty (#549, #645; loki §4). Erä 1 (jaetut komponentit) tehty (PR #709: apulinkit, listojen numerointi, laskurivit listoissa, tyhjät taulukkorivit, 28×28-kaappaukset; loki §4). Jäljellä, opettajan päätettävä: Minor-erä ja yhteinen kuvasääntö (nimiöt vähintään noin 12 px 390 px:ssä,
mallikuvaajan akseleilla suure ja yksikkö, kaaviokuvan kuvateksti sanoo sen kaaviokuvaksi, malliksi merkitty luonnoskuvaaja).
Kuviin ei kosketa: opettaja piirtää ne itse.
Kuvasääntöraportti tehty (`docs/audits/2026-11-23-fy10-kuvasaanto.md`, PR #819); opettajan päätökset (2026-11-23 koordinaattorin chatissa): nimiöt 11 px ja yli kelpaavat; yksikköä ei vaadita mallikuvaajan akselille; kuvateksti riittää malli- ja kaaviokuvamerkinnäksi, puuttuvat sanat lisätty 5 kuvan kuvatekstiin (PR #819); liikemaara/model: science-löydös (`docs/audits/2026-11-23-fy10-liikemaara-science-loydos.md`) korjattu (vastakkaisen törmäyksen ehto poikkeaman suuntaan, investigation.md ja teacher.md) ja kuvateksti merkitsee mallin (Mallikuvaaja / mallin mukaan; kuvaa ei muutettu); katselmoinnit PASS (opettaja 2026-11-23). **Myöhempi kohta:** alle 11 px:n nimiöt (24 kuvaa, raportin kohta 1; pienin hyppy/model 9,2 px) jätetty ennalleen; uusi piirros vaatii opettajan hyväksynnän.
Minor-erä tehty PR:ssä #819 (opettaja 2026-11-23 koordinaattorin kautta): ohuet välit yksiköissä (32 kohtaa 8 tutkimuksessa) ja yksi lainausmerkki, katselmoinnit normaalisti. Muut auditoinnin Minor-löydökset oli jo korjattu tai koskevat kuvia.

## 5b. Leikkautuva kaava: avoimet päätökset (opettaja päättää)
Tarkistus ja `reflow`-carry tehty (#594). Auki: (1) lasketaanko vierityslinjalle jäävä inline-kaava leikkautuneeksi (nyt
kyllä), ja korjataanko vanha lista jaetulla komponentilla vai sivu kerrallaan; (2) tehdäänkö täysi CI-pohjainen lista
(koko sivuston ajo, noin 20 ydintuntia). Lista: `docs/clipped-formulas/<kurssi>.tsv` (rivejä vain poistetaan).

## 5c. ElevenLabs-ääneenluku FY1 ja FY2 (opettaja 2026-11-15)
Ei tekijää: #598 suljettu yhdistämättä. Ääni Oskari - Finnish; mp3-tiedostot repoon Hellsla/ruukkilabra-audio, päärepossa vain manifestit. FY1:n luvut fy1-1…fy1-8
äänitetty; FY2 odottaa opettajan päätöstä. Sääntö: `CLAUDE.md` "Parts specified…", `docs/decisions/oppituntisivun-osat.md`. Tarkka toimeksianto: loki §5c.

## 5d. Leikkautuvat kaavat omalle rivilleen (opettaja 2026-11-15)
Tehty kaikille kursseille FY1–FY9 (loki §5d: kurssikohtaiset luvut, opit ja listalle jääneet rivit). Jäljellä vain
`docs/clipped-formulas/`:n tähderivit; ne tehdään 0c:n jälkeen ilman täysiä katselmointeja. Menetelmä: loki §5d "Opit".
FY1 tehty (#724). FY2 tehty (#749): jäljellä 14 riviä (lainatut opiskelijan laskut exercises.json:ssa fy2-3, fy2-8; fy2-6:n ja fy2-8:n Järkevyys-ketjujen jatkorivit). FY3: 20 riviä jää (fy3-15:n kolme rivinvaihtoa tehty; lainatut
opiskelijan laskut ja lauseen sisäiset ketjut fy3-4, fy3-5, fy3-12 sekä fy3-10:n `\dfrac`-rivi, jonka rivittäminen vaatisi sisältömuutoksen; ei tehtävissä pelkällä rivityksellä, koska `$$` irrottaa lauseen sisältä välimerkin ja päätteen, esim. "…kg:n massan").

## 6. Kuvatehtävät ja taulukkotehtävät FY9 (opettaja 2026-11-13…15)
FY9 A tehty (claude/fy9-a-kuvatehtavat, #714): fy9-voimat s7–s8, fy9-ympyraliike s8–s9, fy9-sailymislait s7–s8, fy9-energia s8–s9; FY9 B on toisen työntekijän.
FY9 C tehty (PR #717, claude/fy9-c-kuvatehtavat): fy9-sahkokentta s7–s8, fy9-magnetismi-valo s8–s9, fy9-moderni s8–s9, fy9-mittaaminen s7–s8, fy9-kokeellisuus s7–s8 (loki §6 FY9 C); koordinaattori kirjaa rivin yhteen kohtaan A:n ja B:n kanssa.
Kaksi kuvatehtävää per luku hyväksytty kustannuksesta huolimatta (noin 300 k per luku); FY10:een ja FY14:ään ei. Jokaisessa
luvussa vähintään kaksi kuvatehtävää ja taulukkotehtävä noin joka kolmannessa; arvot vain `docs/mafy-arvot.tsv`:stä, uudet rivit
lähde-URL:n kanssa. FY8 on valmis (kaikissa luvuissa 1–16 vähintään kaksi kuvatehtävää; taulukkotehtävä fy8-1:ssä ja fy8-4:ssä, muissa ei
VERIFIED-riviä; historia loki §6). Jäljellä FY9 (units): malli fy9-liike tehty ja hyväksytty (#708; opettaja 2026-11-18 koordinaattorin ilmoituksen mukaan, loki §6 FY9; s7 ja s8 unitin Sovella-sarjaan, ei jaettua muutosta, uusia kuvia ei; kierros: `python scripts/round.py fy9-<id>` ja `--finish` (0j; unitin Sovella-sarja on `figcat`-omistaja `<unit>-sovella`, joten uusi unit-kuva kelpaa)); loput 13 kokonaisuutta samalla mallilla. Kehittäjä jakaa pitkät sijoitusketjut (hc omaksi
vaiheekseen, energia jouleina ennen eV-muunnosta) jo ensimmäisessä versiossa. Tämä kohta jää, kunnes FY9 on tehty.
FY9 B (lämpö, kaasut, aallot, tasavirta) tehty: kaksi kuvatehtävää kuhunkin (PR #715; loki §6 FY9 B).

## 8e. Kuvien asettelu (opettaja 2026-11-13) — toteutetaan kohdan 11 U3:n osana
Turha pystyväli kuvan vierellä, kuva ja pieni taulukko tai kaksi pientä taulukkoa vierekkäin, kuva aina selittämänsä kappaleen
viereen, valokuva kuvateksteineen oikealle palstalle (`build.py fig_rows`, site.css, `check_layout.py`). Ennen/jälkeen-kuvat: fy3-8, fy4-3, fy1-1 (1280, 1440, 1920 px). Täysi kuvaus: loki §8e.

## 8g. Mallivastaukset perusperiaatteesta (opettaja 2026-11-13)
Tehty: FY4 (#727, 2026-11-18; 5d FY4: FY4.tsv:n rivit jäivät, CI-selain näkee 4–6 px:n leikkaukset). FY7 tehty (PR #726, loki §8g FY7). FY8 tehty (PR #823, loki §8g FY8). FY1 tehty (PR #813: kaikki 8 lukua, Sovella ja koe, kolme kieltä; loki §8g FY1). FY2 tehty (PR #817: kaikki 8 lukua, Sovella ja koe, kolme kieltä; Sovella fi, en ja fi-easy, koe vain fi). FY5 tehty (PR #814: kaikki 17 lukua, Sovella ja koe, kolme kieltä; Sovella fi, en ja fi-easy, koe vain fi; loki §8g FY5). FY6 tehty (PR #815: kaikki 16 lukua, Sovella ja koe; kohta 15 fy6-5 ja kohta 20 FY6 Sovella samassa PR:ssä; loki §8g FY6). FY3 tehty (PR #849: kaikki 16 lukua, Sovella ja koe, kolme kieltä; Sovella fi, en ja fi-easy, koe vain fi; loki §8g FY3). Kurssit FY1–FY8 tehty.
Tehtävien, Sovellan ja kokeiden mallivastausten Kaava-vaihe alkaa perusyhtälöistä ($\eta = E_\text{hyöty}/E$, $E = Pt$, $Q = rm$, energiatase),
sitten johdettu kaava, symbolinen sievennys loppuun, vasta sitten sijoitus. Kurssi kerrallaan `/exercises`- ja `/practice`-putkella; yhdistetään saman kurssin
kesken olevaan tehtäväkatselmointiin (FY5, FY6, FY7), ei rinnakkain.

## 8j. Pohdinnan kertaustehtävä liittyy pohdinnan ilmiöön (opettaja 2026-11-13)
Tehty: FY4 (#647), FY5 (#661 ja 0f-PR #671: fy5-7, fy5-11, fy5-17; `docs/audits/2026-11-17-8j-FY5.md`), FY1 (0f-PR #679: fy1-2, -5, -6, -7; `docs/audits/2026-11-17-8j-FY1.md`), FY6 (0f-PR #675: fy6-2…14; `docs/audits/2026-11-17-8j-FY6.md`), FY3 (0f-PR claude/fy3-8j-0f: fy3-1, -3, -4, -5, -6, -7, -9, -10, -12; `docs/audits/2026-11-17-8j-FY3.md`).
FY2 tehty paitsi fy2-1 (ei kertaustehtävää; kysymys opettajalle, `docs/audits/2026-11-17-8j-FY2.md`; PR #676).
FY7 tehty (0f-PR 2: fy7-1, 3–10, 12–14; `docs/audits/2026-11-17-8j-FY7.md`).
FY8 tehty (0f-PR claude/fy8-0f: fy8-1, 2, 4–16; `docs/audits/2026-11-18-8j-FY8.md`).
Jäljellä FY1:n fy1-1 ja fy1-8 (kertaus paljastaisi Ennusta-vastauksen; kysymys opettajalle, FY1-audit) ja fy2-1. Sääntö: `herata`-vaiheen retrieval-`choice` kysyy pohjatietoa saman ilmiön kautta. Lopuksi sivupohjan muutos:
Pohdinnan järjestys ilmiö → kertaustehtävä → pohdintakysymys (`inquiry.py`/js; kirjataan `docs/inquiry.md`:hen).

## 8l-b. "Esimerkkiaineisto" pois otsikoista (opettaja 2026-11-16)
`caption-label` tunnistaa kaikki muodot (#658); poistettu FY1, FY2, FY4, FY6, FY7, FY8 (fy8-2, fi, fi-easy, en; 0f-PR claude/fy8-0f). FY5 tehty (0f-PR #671). FY3: tehtävien text-kentät tehty (PR #742). Jäljellä muut kurssit:
otsikot `reviews.caption_label_free`-funktiolla ja `reviews.py carry <id> --exercises [--lang]`; tehdään kurssin muiden töiden mukana (0f).
Tehty (PR #852, 2026-11-24): tehtävätekstien ja tutkimusvaiheen alkuetuliite "Esimerkkiaineisto:" / "Example data:" pois fi, fi-easy ja en: fy1-6 (tutkimusvaihe), fy4-16, fy5-10, fy6-1, fy6-5, fy6-11, fy8-4, fy8-5, fy8-7, fy8-16 (tehtävät); delta-katselmoinnit PASS. Ei carry-reittiä: jäljellä ei ollut `caption`-kenttiä.
Jäljellä: FY3 (#849:n yhteydessä); fy2-1:n tutkimusvaiheen otsikko "Esimerkkiaineisto: pomppiva pallo" (kaikissa kielissä; täysi katselmointi, joten tehdään fy2-1:n seuraavan sisältömuutoksen mukana); en-yksikön `units/fy14-fotoni/inquiry.json` kehote "Example data: …" (yksikön katselmointi); fy6-11:n `solutions.md`:n Annettu-rivin pieni alkukirjain "esimerkkiaineisto: levyjen etäisyys …" (visual Polish, ei uutta kierrosta). Leipätekstin "esimerkkiaineistossa" ja palautteiden "Esimerkkiaineisto kumoaa/tukee tätä" jäävät tarkoituksella.

## 10. Simulaatioiden käyttöliittymä (opettaja 2026-11-14)
Mittaus ja päätökset `docs/audits/2026-11-14-simulaatioiden-kayttoliittyma.md`. PR 1–4b tehty (#563, #588, #591, #648, #652), PR 5 tehty (#711: canvasin nimi ja kuvaus, 40 px:n valintaruudut, näkyvä kohdistus). Myöhemmin kurssi kerrallaan luvun seuraavan
sisältömuutoksen yhteydessä: tyyppi D (fy6-5, fy6-6, fy6-9, fy6-12, fy6-13, fy6-14), fy1-2:n säätimien ryhmittely, näppäinvaihtoehto raahaukselle,
nimien yhtenäistäminen (Toisto / Tauko / Alusta), toistuvien seliterivien poisto. 1366×650:n lisähuomiot: loki §10.
FY1 tehty (#842): fy1-2:n säätimet kolmelle riville, toistuvat seliterivit pois fy1-1…fy1-6:sta, nopeusvalinnan nimi "Nopeus" fy1-1:ssä ja fy1-3:ssa; näppäinvaihtoehto raahaukselle jo olemassa (fy1-1, fy1-2). Opettajalle: "Käynnistä" → "Toisto" (ratkaistu: pysyy "Käynnistä", opettaja 24.11) ja fy1-5:n ("Toistonopeus") ja fy1-6:n ("Nopeus (toisto)") toistovalinnan nimi, koska kuvassa on jo "nopeus v".
**Opettaja 2026-11-24 klo 00.4x (koordinaattorin chatissa, "I agree on 1-4")**: (1) jatkotyöt aloitetaan nyt erillisinä PR:inä kursseille FY1, FY4 ja FY7 (kurssi kerrallaan; jaettu simulaatiokoodi yksin; uudet painikenimet opettajan hyväksyttäviksi tekijäsessioon); (2) Pysähdy ja mieti laajennetaan FY14:ään (ei FY10:een: tutkimuksissa omat pohdintavaiheet); (3) FY7:n 8g-polish tehdään (kohta 15); (4) FY9 tasavirta s7/s8 (16 p ja 18 p) skaalataan 15 pisteeseen.
**Opettaja 2026-11-24 klo 04.0x (koordinaattorin chatissa, "Ok ok ok ok ok", koordinaattorin suositukset 1–5)**: (1) FY5 "harvennus" → "harventuma" omana PR:nään: tekstit ja kuvien alt-tekstit, täydet katselmoinnit, opettajan approve-figures tekijäsessioon; piirrosten sisäiset nimiöt uudelleen piirrettävien listalle; (2) simulaatioiden aloituspainike pysyy "Käynnistä" (ei "Toisto"); (3) toistonopeuden nimi yhtenäistetään "Nopeus" (ei "Toistonopeus"); (4) fy2-7: fi "sisäenergia" ja en "thermal energy" saavat erota; (5) kolmen katselmointikierroksen raja on ehdoton: neljäs kierros vain opettajan luvalla etukäteen.
FY4 tehty (#844: "Nopeus (toisto)" → "Nopeus" fy4-1, fy4-12; toistuva seliterivi pois fy4-1; fy4-12 exp-2 Järkevyys-virke korjattu; raahattavaa ei ole; fy4-2 pois, ks. kohta 24 Avoimet). Avoin jaettu vika: toistonopeuden label-span kutistuu 1 px:ään 1280 px:n leveydellä (fy4-1, fy4-3; `site.css`/`sim-embed.js`), korjataan jaettuna yksin. FY1: fy1-5:n ja fy1-6:n toistovalinta pidetään nimellä "Toistonopeus"/"Nopeus (toisto)", koska simulaatiossa näkyy nopeus v (ulkoasukatselmoinnin Major); opettajalle tiedoksi poikkeuksena "Nopeus"-päätökseen.
FY7 tehty (PR #848): "Animaation nopeus" → "Nopeus" fy7-2, fy7-6 ja fy7-7:ssä; toistuvat seliterivit pois fy7-4, 6, 9, 10 ja 11:stä; "Käynnistä" ja fy7-5:n "Nopeus" ennallaan; raahaus vain fy7-1:ssä, jossa r- ja φ-liukusäätimet ovat näppäinvaihtoehto (koodia ei lisätty). fy7-10 `tarkistus-3`:n tehtävänanto korjattu ("veden pinnan läpi", koordinaattorin lupa, kierros 2). Jäljellä: fy7-8:n seliterivi (lesson.md:46 kuva monokromaattinen, lint ERROR; korjaus = uusi piirros, opettajan päätös) ja fy7-1:n seliterivi (ei toistu Käyttöohjeessa).

## 11. Tehtävänäkymä ja teorian taitto (opettaja 2026-11-14, UI/UX-auditointi)
Yleislinja (CLAUDE.md "General UI line"): käyttöliittymään ei lisätä tekstiä. U4 (#561) ja U5 (#582) tehty. U1–U3 jaettuja (`templates/`, `scripts/`, `site.css`, `lang/`):
yksin, järjestyksessä U1, U2, U3, kohdan 10 PR 5:n jälkeen; ennen/jälkeen-kuvat PR:ään ja pysähdys opettajan hyväksyntään. Fysiikkaan, vastauksiin,
toleransseihin, tallennusavaimiin ja palautustiedostoon ei kosketa. Täysi määrittely: loki §11.
- **U2 Tehtäväkortin järjestys** (U1 #723 ja U2 #733 tehty): numero ja merkit; tilanne ja kysymys; kuva; vastauskenttä + Tarkista (täytetty päänappi) + Kirjoita ratkaisu; palaute; erotinviivan alla Vihjeet, Vastaus, Näytä ratkaisu, lukko. Ei uusia tekstejä.
- **U3 Teorian taitto, vaihtoehto B** (kohta 8e): 38 rem:n palsta säilyy; teksti kuvarivin yläreunaan, valokuva viereen, kaksi pientä taulukkoa vierekkäin, korkea kuva alle tai seuraava kappale viereen.
- Ei tehdä: Aloita-riviä, "Näytä kaikki tehtävät" -toimintoa, etusivun ryhmäotsikoita, marginaalipalstaa tai keskitettyä lukupalstaa, yhden luvun julkaistua pilottia.

## 11b. FY9: adaptiivinen YO-valmentaja (opettaja 2026-11-14)
Suunnitelma `docs/FY9_ADAPTIVE_PLAN.md` (#566), hyväksytty P1–P12. PR 1 (YTL/Abitti-tietojen tarkistus, sisältö) voi alkaa heti; PR 2–8 jaettuja, yksin, kohdan 10 PR 5:n ja U1:n jälkeen;
PR 9 Abitti 2 -ohje; PR 10 kielimallin selvitys. Ei palvelinta, ei tekoälyrajapintaa; jokainen uusi käyttöliittymäteksti hyväksytään PR kerrallaan. Arvio 2,5–3,5 M tokenia.
PR 1 tehty (e2c7f5c, YTL/Abitti-tiedot). PR 2 tehty (#824: tehtäväindeksi `valmentaja/fy9.json`, `kertaus/FY9.json`, `valmentaja.py`; R9 tarkistettu, harmiton). Minikoesarjat ja diagnostisten tehtävien jaksokartoitus (`kertaus/FY9.json`, ehdotus P8) **hyväksytty: opettaja 2026-11-23 ("ok")**. Jaetun kaistan järjestys (opettaja 2026-11-23): 17b → 0g PR 3 → 11b PR 2–8 → 11 U3. PR 3 tehty (#826, näytön kirjaus).
PR 4 tehty (#830): uudet käyttöliittymätekstit, tietosuojalause, kuvat ja laattakuva `coach.svg` hyväksytty: opettaja 2026-11-23 tekijäsessioon ("Hyväksyn tekstit ja kuvat").
PR 4b (seuraavaksi, ennen PR 5:tä): tavoite L–E / M–C / B–A ja käydyt kurssit, suunnitelman P13 ja PR 4b; **opettaja 2026-11-23 ("yes, go with the recommendations")**; uudet tekstit hyväksytään tekijäsessioon.
Varattu: claude/11b-pr4b-tavoite (PR 4b tavoite L–E / M–C / B–A ja käydyt kurssit, P13; #834)
PR 4b (#834): uudet käyttöliittymätekstit ja kuvat hyväksytty: opettaja 2026-11-23 tekijäsessioon ("hyväksyn tekstit ja kuvat").
PR 5 (#836, vaikea ratkaisuvaihe ja toistuvat virheet): uudet käyttöliittymätekstit ja kuvat hyväksytty: opettaja 2026-11-24 tekijäsessioon ("Hyväksyn tekstit ja kuvat"). Jäljellä: PR 6–8.
Varattu: claude/11b-pr6-koetila (PR 6 koetila ja minikokeet 30/60 min, harjoituskokeen koetila)
PR 6 (#847, koetila ja minikokeet): uudet käyttöliittymätekstit ja kuvat hyväksytty: opettaja 2026-11-24 tekijäsessioon ("Hyväksyn tekstit ja kuvat").
Varattu: claude/11b-pr7-kertauspolku (PR 7 kertauspolku 2/4 viikkoa, 14/28 vrk, 3–7 pv/vko, 20/40/60 min)
PR 7 (#851, kertauspolku): uudet käyttöliittymätekstit ja kuvat hyväksytty: opettaja 2026-11-25 tekijäsessioon ("I approve texts and images").
PR 7b (jaettu, PR 7:n jälkeen, ennen PR 8:aa): valmentajan "Aloita diagnoosilla" vie nyt `fy9-koe.html`:n alkuun; linkin pitää viedä suoraan 24 kohdan diagnoosiin (osio 5 Esimerkit, `testi-1`). Muutos `valmentaja.py`:n `data-diag`-arvoon (ankkuri), ei uutta tekstiä. **Opettaja 2026-11-24 ("go with your recommendations")**.

## 17. Kehitys ilman kirjautumista (opettaja 2026-11-15)
17a PR 1 (#720) ja PR 2 (#741, manifesti ja pysyvä tallennus) sekä 17b PR 1 (#818, koko työ yhteen tiedostoon; tekstit opettaja 2026-11-23) tehty; webkit.org sallittu ympäristöön 2026-11-19, opettajan luvalla.
Ohjeet ja päätökset K1–K9: `docs/audits/2026-11-15-kehitys-ilman-kirjautumista.md`. Jokainen osa oma PR, yksin; uudet käyttöliittymätekstit PR:n kuvauksessa. Tallennusavaimia, tiedostomuotoja ja korttien id:itä ei muuteta.
Osat: 17a verkoton käyttö (service worker, manifesti, moduuli laitteelle), 17b koko työ yhteen tiedostoon, 17c yleisvirheiden tunnistus, 17d ajoitettu kertaus, 17e luokan yhteenveto, 17f hakemistot ja haku.
Järjestys: 17a PR 1–2, 17b PR 1, 17f PR 1–2, 17c PR 1, 17e, 17d PR 1, sitten 17f PR 3, 17a PR 3, 17b PR 2. Osien sisältö: loki §17.

## 19. 45 soveltavaa aineistotehtävää FY1–FY9: tehty (loki §19)
Kaikki 45 tehty (FY1–FY9, A1–A5). Avoin vain: opettaja avaa Tukesin kaksi linkkiä (FY6 A3, A4) selaimessa ennen yhdistämistä. Poistetaan, kun se on tehty.

## 15. Kustannustoimituksellinen lopputarkistus FY1–FY8 (opettaja 2026-11-14, kevennetty 2026-11-16)
Toiseksi viimeinen: kohtien 17, 18, 13 jälkeen, sen jälkeen 14 ja viimeisenä 16. Ensin pelkkä raportti (`docs/audits/`), korjaukset vasta opettajan luettua. Kevennetty:
(1) automaattiset läpikäynnit (concepts.py, coverage.py --all, physics_phrases, check_a11y; yksi raportti); (2) otos: täysi tarkistus yhdelle luvulle per kurssi, raportti opettajalle;
(3) laajennus vain, jos otos löytää kriittisiä virheitä. LOPS 2019 vertailuperusta; julkaistuja oppikirjoja ei käytetä; virheitä ei oleteta; tunnisteita, vastauksia ja tallennusmuotoja
ei muuteta ilman todettua virhettä; lähdekoodia ei muokata. Raportin rakenne ja kahdeksan tarkistuskohtaa: loki §15.
Raportti tehty (#721, `docs/audits/2026-11-18-lopputarkistus-FY1-FY8.md`). **Hyväksytty: opettaja 2026-11-18 klo 18.33** (koordinaattorin chatissa, "mennään ehdotustesi mukaisesti"): korjataan kaikki raportin löydökset, kurssi kerrallaan omissa PR:issään saman kurssin keskeneräisen PR:n jälkeen:
- FY2: fy2-4 M1, M2, M3 tehty ja katselmoitu (PR #738, 9 katselmointia PASS).
- FY6: fy6-5 kirjoitusvirhe "sisäenergiakseen": ei löytynyt enää mistään kielestä (tarkistettu PR #815:ssä), ei korjattavaa.
- FY8: fy8-9 tehty (PR #823: "säteilykvanteista", 97,65 → 97,6 MBq, Geiger-kuvateksti; muut löydökset kuvaan, tehtäväkäytäntöön tai ohjelmakuvaukseen liittyvinä jäävät: kuva 14 apuviiva, "Graphical Analysis Prossa", $A=\lambda N$ valinnaisessa tehtävässä, kriteeri 4, tehtävien 9–14 taulukon kuvateksti).

## 20. Opettajan päätökset 2026-11-18 klo 18.33 (koordinaattorin chatissa, "mennään ehdotustesi mukaisesti")
Jokainen kohta tehdään omana työnään saman kurssin keskeneräisen PR:n jälkeen; tämä rivi on hyväksynnän kirjaus (sääntö 5).
- Pysähdy ja mieti tehty FY1–FY8 (#760, #765, #766 ja #772, #745, #770, #777, #779, #783) ja FY14 (29 yksikköä, 56 laatikkoa, vain en, kolme katselmointia jokaiselle; FY10 ei, opettaja 2026-11-24 "I agree on 1-4") ja FY9 (#825: 14 yksikköä, fi täysi katselmointi, en ja fi-easy vain tiede; en- ja fi-easy-yksikkösivut draft, kunnes pedagogia ja ulkoasu on tehty), kaikki kielet, katselmoitu; FY5:stä alkaen rajattu laajuus, vanhan sisällön löydökset PR:ien kuvauksissa. **Opettaja 2026-11-19 aamulla ("kaikki ok"): laajennetaan muihin kursseihin**; seuraavaksi FY9 ja muut kurssit, kurssi kerrallaan.
- Pysähdy ja mieti FY9 (#825): **opettaja 2026-11-23 (tekijän sessiossa, "Vain fi täysi, en/fi-easy kevyesti")**: fi:lle tiede, pedagogia ja ulkoasu, en:lle ja fi-easylle vain tiede (70 katselmointia 126:n sijaan); en- ja fi-easy-sivut jäävät draftiksi, kunnes kaikki kolme katselmointia ovat voimassa.
- 8j: fy1-1, fy1-8 ja fy2-1 ohitetaan (ei kertaustehtävää).
- 5d: FY5:n 16 ja FY6:n 25 jäljellä olevaa riviä jäävät listalle (myös fy5-7 `x = A \sin(…)`).
- Pysähdy ja mieti FY2 (#765): **opettaja 2026-11-19 klo 22.3x ("1 yes"): fy2-4:lle sallitaan neljäs, rajattu katselmointikierros** (tiede ja pedagogia delta, en full) kolmannen kierroksen esteen (johtopäätöksen kriteeri 3) korjauksen vahvistamiseksi; poikkeus lesson.md:n kolmen kierroksen rajaan vain tähän.
- Pysähdy ja mieti FY3 (#766): **opettaja 2026-11-20 klo 14.2x ("I allow recommendations")**: (1) visuaalikatselmoija kirjoittaa uudet `review/visual.md`-raportit vanhojen tilalle (normaali menettely); (2) fy3-4 jätetään pois tästä PR:stä (palautetaan mainin tilaan), muut 15 lukua yhdistetään. fy3-4:n simulaation lukema (näyttää heti ρg = 9,81 kPa/m ja 1,97-kertaisen paineen, joten kokeen 1 numerotehtävä vastataan ilman mittausta) korjataan omana jaettuna työnään (sim/`lang/`, yksin), ja fy3-4:n Pysähdy ja mieti tehdään sen jälkeen samassa yhteydessä.
- fy3-4 (#772): **opettaja 2026-11-20 klo 17.3x ("yes")**: (1) kaavarivi "hydrostaattinen paine :: p = p_0 + ρgh" pidetään (opettajan päätös 2026-11-12, docs/fy3/kaavanimet.tsv rivi 37); opettajan hyväksymä poikkeus, katselmoijat eivät merkitse estettä. (2) Esimerkin ikkunavoima 1,77 kN ja kolmen merkitsevän numeron perustelu (P7).
- Pysähdy ja mieti FY5 ja eteenpäin: **opettaja 2026-11-20 klo 01.0x ("Ok do it")**: rajattu laajuus. Katselmoijien löydökset vanhasta sisällöstä kirjataan PR:n kuvaukseen (osio "Vanhan sisällön löydökset") erillistä korjausta varten; tässä PR:ssä korjataan vain uuden Pysähdy ja mieti -sisällön esteet ja vanhan sisällön kohdat, jotka estävät uuden sisällön toimimisen. (FY2 maksoi n. 31 USD / 100 katselmointia.)
- 23 prosessisivu (#764): opettaja 2026-11-19 klo 22.3x ("2, yes"): sisältö hyväksytty; **klo 22.4x: "the workflow should look like an office"**: työnkulun animaatio piirretään toimistona (kuten hellsla.github.io/agent-office: huoneet ja työpöydät, hahmot kuljettavat paketteja pöydältä toiselle ja CI-koneille). **Toimistoversio hyväksytty: opettaja 2026-11-19 klo 22.5x ("ok dont put more effort into this")**; ei lisätyötä, viimeistellään ja yhdistetään.
- FY6 Sovella: tehty PR #815:ssä (s1 a/b/d, s2 d, s3 a, s4 d uudelleen sanottu; ajautumisnopeus ja ryömintä erotettu; ei uusia tehtävätyyppejä).
- Pienet: header-raja 72 rem hyväksytty (jaettu, site.css; tehty jo f19810c, 2026-11-17); kirjavinkeissä suorat Finna-teoslinkit ja "Tiede – luovaa leikkiä" -kirjan suomenkielinen painos, jos löytyy; podcasteille YouTube-linkit sallittu; FY10:n taulukko-otsakkeet 390 px:ssä lyhennetty (#731).
- 0g PR 2 aloitetaan, kun päivän PR-jono on tyhjä. 8k (teacher-text) toteutetaan.
- Podcastien YouTube-linkit jätetään pois toistaiseksi (opettaja 2026-11-18 klo 22.00).
- 11 U2: opettaja 2026-11-18 klo 22.00: toimintarivin järjestys Kirjoita ratkaisu → vastauskenttä → Tarkista ("ensin kirjoitetaan ratkaisu, vasta sitten tarkistetaan"); uudet kuvat opettajalle ennen yhdistämistä. **Kuvat hyväksytty: opettaja 2026-11-19 aamulla ("kaikki ok").** Lisäys (opettaja 2026-11-19 klo 07.15, kuvakaappaus): monivalintatehtävissä Kirjoita ratkaisu ja Vastaa samalle riville (Kirjoita ratkaisu ensin); uudet kuvat opettajalle. **Lisäyksen kuvat hyväksytty: opettaja 2026-11-19 klo 12.4x ("hyväksyn kuvat").**
- Podcastit-sivun (fi) muu kieli -laatikon teksti (opettaja 2026-11-18 klo 19.00, "käy"): lead "Haluatko kuulla fysiikkaa myös englanniksi?"; text "Tutustu englanninkielisiin fysiikan podcasteihin, dokumentteihin ja opetusvideoihin. Tutut ilmiöt avautuvat uudesta näkökulmasta, ja samalla opit fysiikan sanastoa englanniksi."; link ennallaan.
- Opettajan päätökset 2026-11-19 aamulla (koordinaattorin chatissa, "Kaikki ok"): FY3 FY3 fy3-8 sanamuoto ja fy3-11:n 480 kW:n tehtävän ratkaisun perustelu (loppunolla on merkitsevä, ei pyöristysohjetta; P7-sääntöä ei muutettu) tehty (FY3-paketti); jaetut yksi kerrallaan: header 72 rem → CI-tarkistus site/-sivujen poistolle → 0g PR 2; rinnalla 5d FY2 (37) ja FY3 (23) riviä.
- Kirjavinkkien Finna-tietuelinkit ja podcastien YouTube-linkit odottavat: Finna estää koneellisen haun (Cloudflare), YouTube-linkki vaatisi jaetun muutoksen (`media_tips.py`) ja opettajan päätöksen.
- Pysähdy ja mieti FY7 (#779): **opettaja 2026-11-21 klo 16.4x ("hyväksyn", koordinaattorin suositus 1)**: fy7-1:lle neljäs, rajattu katselmointikierros (tiede en/fi/fi-easy delta ja pedagogia delta), vain tähän lukuun; PASS, yhdistetty.
- Pysähdy ja mieti FY8 (#783): **opettaja 2026-11-22 klo 03.2x ("Hyväksyn suosituksesi", koordinaattorin suositus 1)**: fy8-4:lle, fy8-15:lle ja fy8-16:lle neljäs, rajattu katselmointikierros (tiede ja pedagogia delta, kaikki kielet; visual delta vanhentuneen tilan vuoksi), vain näihin lukuihin; PASS.
- Mahdollinen myöhempi sisältötyö: FY3/5/6:n käsin jaetut Pysähdy-ketjut (fy3-4, fy5-3, fy5-9, fy6-4, fy6-6…8, fy6-11…16) yhdeksi ketjuksi `mathlayout.display_chains`in (#782) varaan; sanamuoto muuttuu, joten katselmointi.

## 24. Uudet kuvat sivustolle (opettaja 2026-11-19; kuvat hyväksytty 15.–18.11.)
Osa 1 (kuvapohja, `scripts/figimage.py`, NOTES.md §3) ja FY2-pilotti (#768) **hyväksytty: opettaja 2026-11-20 klo 01.4x ("I approve")**.
Lähde ja säännöt: 662 Codexin piirtämää, opettajan hyväksymää kuvaa FY1–FY10 ja FY14, haara `claude/dazzling-pasteur-kws2vo`, `uudet_kuvat/<MODUULI>-hyvaksytyt-kuvat.zip` (`kuvat/`, `merkinnoin/`, `ASETTELU.tsv`, `PAATOS.txt`; `VAIHDETTAVUUS.tsv`). **Haaraa ei yhdistetä mainiin; PNG:t eivät mene mainiin**; mainin `downloads/`-zippejä ei käytetä. Vaihdetaan vain `kuvat/`-kuvat; ennalleen kuvaajat, ohitetut ja "pidä alkuperäinen" (`PAATOS.txt`); vuorovaikutteisen elementin osaa ei korvata (opettaja 17.11.); monivalinnan vaihtoehtokuvat koko tehtävä kerrallaan; `fy2-4/grid` ja `fy7-2/track-sign` FY9:ssä omistajamoduulin versiolla. Piirroksia ei muuteta; jos kuva ei toimi sivulla, opettajalle (uusi piirros = uusi hyväksyntä). `PAATOS.txt`:n mittasuhde- ja yksityiskohtahuomiot hyväksytty sellaisinaan.
Kulku (osat 2–11, moduuli kerrallaan, oma luonnos-PR): kuvat lukuihin sekä koe- ja Sovella-sivuille kaikilla kielillä; ennen/jälkeen-kuvat `docs/audits/img24-<moduuli>/`; opettaja hyväksyy suoraan tekijäsessioon; `approve-figures` (myös koe/Sovella, #793), carry, build, tarkistukset; viewBox-ylitysten tyhjää reunaa ei rajata (opettaja 2026-11-22 klo 17.12); jos ylitys kaataa check_layoutin (kuva yli 3 px kehyksen sivun yli), pelkkää taustaa oleva kaista rajataan WebP:stä ja ASETTELUsta ja rajattu kuva hyväksytetään opettajalla suoraan tekijäsessioon (opettaja 2026-11-23 klo 02.3x: "Etene suositusten mukaisesti"); muu tyhjän reunan rajaus vain opettajan luvalla; koordinaattori yhdistää moduulihyväksynnän jälkeen (opettaja 2026-11-19).
Tehty ja yhdistetty: FY1 #771 (36 kuvaa; **opettaja 2026-11-20 klo 17.5x "hyväksytty"**; tehtäväsarjojen carry #792), FY2 #768, FY3 #776 (61; **opettaja 2026-11-21 "Hyväksyn FY3-kuvat"**; water-column ja earth-flows rajattu, **"On ok" 2026-11-21 klo 11.0x**; wall-temperature samalla perusteella), FY4 #780 (72; **opettaja 2026-11-21 "Hyväksyn"**; strobe-otsikko siirretty, virhe rajattu, fy4-7/hero sellaisenaan "On ok") ja koe/Sovella #786 (3; **opettaja 2026-11-22**), FY5 #785 (87/94; **opettaja 2026-11-21**, karuselli ja muutos rajattu) ja koe/Sovella #788 (5; **opettaja 2026-11-22**), FY6 #794 (79; **opettaja 2026-11-22**), FY7 #798 (89; **opettaja 2026-11-22**), FY3:n 7 käsin liimattua SVG:tä (fy3-13…fy3-16; PR #816, **opettaja 2026-11-23 "Hyväksyn kuvat"**; kuvatekstit 24 px, piirrokset figures.py:ssä; neljälle luvulle täysi katselmointikierros, koska vanhan SVG:n poisto ei kulje carryna), FY10 #797 (62, vain fi; **opettaja 2026-11-22**; fy10-liikemaara/setup tekstilaatikko kavennettu, **opettaja hyväksyi 2026-11-22**). Jaetut korjaukset: #782 (`figimage.code_of`), #787 (`practice.figures`), #789 (`build.py` kopioi koe/Sovella-kuvat), #791 (`mathlayout.list_chains`, tvt-kulmakerroin), #793 (`approve-figures` ja `ci_scope` koe/Sovella), #801/#804/#805/#806/#807/#808/#809/#810 (figimage FY9/FY14-yksiköille ja FY10-tutkimuksille, carry, testit). Lisäksi yhdistetty 2026-11-23: FY8 #799, FY9 #800 (30 kuvaa), FY14 #803 (43 kuvaa, vain en); niiden rajatut kuvat (fy8-11/ketju, fy8-15/valittaja, fy9-harjoituskoe-s2-fbd, fy14-confinement-concepts/aspect) **opettaja hyväksyi 2026-11-23 suoraan tekijäsessioihin**.
Avoimet: **Varattu: claude/fy5-harventuma** — FY5 `fy5-10/types` "harvennus" → "harventuma" kaikkialla (opettaja 2026-11-19 klo 19.12; lähde ja `glossary.json` vanhalla sanalla) — odottaa opettajaa: alt-tekstit (approve-figures) ja piirrosten nimiöt (**uudelleen piirrettävät: fy5-10/types 2 nimiötä, fy5-14/pitkittainen 1**, `docs/audits/fy5-harventuma/`); tehdään omana PR:nään, tekstit + alt-tekstit, full-katselmoinnit (koordinaattori 2026-11-23); FY5 `fy5-9/heiluri`, `fy5-17/maapallo` ja FY7 `fy7-1/cut-magnet` ennallaan (PAATOS); FY6 `fy6-15/luokat` III-numero puuttuu vinoneliöstä (PAATOS, opettajalle); FY4 `fy4-4/valitse_d`-kuvan toinen virhe piirretään myöhemmin uudelleen (opettaja 2026-11-23 "ok"); FY10-kuvien alle 11 px nimiöt (esim. hyppy/model 9,2 px) piirretään myöhemmin uudelleen (opettaja 2026-11-23; raportti `docs/audits/2026-11-23-fy10-kuvasaanto.md`); FY4 `fy4-2` lesson.md:5 kuva monokromaattinen (currentColor), lint ERROR; korjaus = uusi piirros, opettajan päätös (kohdan 10 FY4-PR:ssä fy4-2 jätettiin tämän takia pois: "Nopeus (toisto)" ja seliterivi jäivät); FY8 `{"union": true}` -avain pois `fy8-11/ketju`, `fy8-16/laajeneminen` (convert ei tue); `figimage.py convert` ei luo `lessons/<MODUULI>/`-kansiota; FY8 suurennettu kuvankäsittelyllä (pienentämättömät korvaavat, jos opettaja toimittaa); FY9 11 voimakuviota kuvauksesta (`nimeton-N`); FY14 sivut englanniksi.

## 26. Opettajan päätökset 2026-11-25 (koordinaattorin chatissa, "Yes yes")
(a) Kohdan 11c jatko: pitkien tehtävien laskukohtiin vastauksen tarkistus ja yleisen virheen palaute (muuttaa mallivastauksen lukkoa, tehty-laskuria ja valmentajan näyttölokia). Jaettu, oma PR, vasta 11b PR 8:n ja 11c:n vihjeyksiköiden jälkeen; uudet käyttöliittymätekstit hyväksytään tekijäsessioon.
(b) Fysiklabbet- ja Mafy-vertailun ehdotukset (sessio "Fysillabbet vs ruukkilabra", 2026-11-25) jonoon. Kustakin ensin lyhyt ehdotus opettajalle (mitä muuttuu, kuva ennen/jälkeen, kustannus), toteutus vasta päätöksen jälkeen:
  1. esitystila oppitunneille; 2. hyppyrivi luvun alkuun; 3. teoriakappaleiden 60 sanan raja (233/1593 kappaletta yli); 4. kaavalaatikon tunnusluettelo;
  5. MAOL/Mafy-taulukoiden käyttö fy9-koe-yksikössä ja hakutehtävät; 6. Mafy-kartta; 7. taulukoiden versiovahti CI:hin; 8. toinen harjoituskoe.

## 14. Ahjo ja LUMA-tutor yhteiseen jaksopohjaan (opettaja 2026-11-13; juuri ennen vihkoja)
Siirretään `ahjo.py` ja `lumatutor.py` jaksopohjan lohkoiksi niin, että sivut pysyvät tavulleen samoina kuten Kilparobotiikassa; puuttuvat lohkot yhteiseen kirjastoon. Jaettu: yksin.

## 16. Vihkot FY1–FY8 (opettaja 2026-11-13; jonon viimeinen)
A5-vihkot kaikille kursseille tiiviillä asettelulla (`python scripts/print_book.py <C> --lang fi|en --publish`); FY1–FY4 tehdään uudelleen, FY5–FY8 uusia. Vasta kohtien 3, 17 ja 18
jälkeen; rakenna sivusto vihkojen jälkeen (Vihkot-sivu).

## 25. Yksilöllinen oppimispolku, pilotti FY1 (opettaja 2026-11-20 klo 17.5x "laita se vikaksi"; jonon viimeinen, vihkojen jälkeen)
Versio 1 kokonaan selaimessa: luvun alussa 3–5 kysymyksen lähtötesti tyypillisistä virhekäsityksistä, jonka perusteella sivu suosittelee polun (kertaa ensin / ydintehtävät / haasteet); väärä vastaus ohjaa esimerkkiin tai simulaatioon; osaamiskartta oppilaan selaimeen. Ei palvelinta, ei tunnuksia, ei oppilastietojen keruuta (fysiikkalabra/CLAUDE.md "Never"). Suunnitelma tehdään ensin Claude-projektissa, ja opettaja hyväksyy sen ennen toteutusta; uusi käyttöliittymäteksti vaatii opettajan luvan. Versio 2 (opettajanäkymä, palvelin, kirjautuminen, tietosuoja) on erillinen hanke, joka vaatisi "Never"-säännön muuttamista opettajan päätöksellä.
