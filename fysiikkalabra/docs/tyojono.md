# Työjono

Opettajan päättämät tulevat työt, joita ei ole vielä aloitettu. Jokainen kohta tehdään omana pull requestinaan;
valmis kohta poistetaan tästä samassa pull requestissa.

Tämä on ainoa työjono (opettaja 2026-11-13): ei GitHub Issuesia eikä erillisiä listoja. Kohdat ovat
`docs/ROADMAP.md`:n järjestyksessä. Kohdan ottava ketju katsoo ensin avoimet pull requestit, merkitsee kohtaan
ensimmäisessä commitissaan `Varattu: <haara>` ja avaa luonnos-PR:n heti, jotta muut ketjut näkevät varauksen
(repon juuren `CLAUDE.md`). Saman kurssin kohdat tehdään peräkkäin, eri kurssien enintään kolme rinnakkain.

## 3. Kaavat taulukkokirjan muotoon: valmis

FY1–FY9 on tehty (#501, #522, #527, #529, #572, #576, #578, #580, #583); FY7:n neljä `\\[Npt]`-kaavaa nimettiin kohdassa 3b (#589; nimet tarkistettu MAFY:n raakadatasta, koordinaattori 15.11: `curl https://mafytaulukot.fi/data/latestversion` antaa sivujen id:t ja versiot, sisältö `https://mafytaulukot.fi/<id>/fi/<versio>/theory.html`). FY10:ssä ja FY14:ssä ei ole nimettäviä
kaavoja (opettaja 14.11: "ei tarvitse"). FY5:ssä F pysyy gravitaatiolaissa (opettaja 14.11). Keskinopeuden tunnus on
kaikkialla $v_\text{k}$, ei $v_\text{ka}$ (opettaja 2026-11-13). Kohta 3 on valmis; FY8:n kuusi `\\[Npt]`-lohkoa ovat Sijoitus-laskuketjuja ja jäävät nimeämättä (koordinaattorin päätös 14.11).

## 4. FY10:n tutkimusten ja TVT-ohjeiden korjaukset (opettaja 2026-11-13)

Tehty (#549, erät 2–4): fy10-liukukitka, fy10-jousivakio, fy10-induktio (kuva osin, ks. PR), tvt-kuvaaja ja tvt-tyoselostus; fy10-hiuksen-paksuuden löydös ei pitänyt kuvasta (ei muutettu). Jäljellä: erä 1 (jaetut komponentit), Minor-erä ja yhteinen kuvasääntö.

Auditointi on tehty (#536: 28 PASS, 8 FAIL, ei Critical-löydöksiä, 159 Minor). Korjataan `/quality-audit <id> --fix`
#536:n kuvauksen järjestyksessä: ensin Major-löydökset tvt-epavarmuus, tvt-kuvaaja, tvt-tyoselostus, fy10-jousivakio,
fy10-induktio, fy10-lammonjohtuminen, fy10-liukukitka ja fy10-hiuksen-paksuus. fy10-liukukitkan kallistusvirhe
("0,02 asteen kallistusta kohti", noin 50-kertainen ero) tiedekatselmoinnilla ennen korjausta. Jokainen Major-löydös
tarkistetaan ensin kuvista (fy10-hiuksen-paksuus antoi kahdella ajolla eri tuloksen). Minor-löydökset ja yhteinen
kuvasääntö erillisenä eränä opettajan päätöksellä; jaettujen komponenttien muutokset (`templates/`, `screenshot.py`:n
tyhjät 28×28 px kaappaukset) tehdään yksin. Voi kulkea rinnakkain kohdan 2 kanssa.

## 5. CI:n toistettavuus (2026-11-13)

Tapa ajaa selaintarkistukset CI:n kontissa (`mcr.microsoft.com/playwright/python:v1.65.0-noble`) paikallisesti, ja
layout-testien virheilmoitukset nimeämään ylivuotava elementti (`docs/QUALITY.md` aukot 1–2). Jaettuja tiedostoja:
tehdään yksin ja yhdistetään ennen muita.
Löydös (2026-11-15, #590): `check_lesson.py` layout-tarkistus (360 px, ratkaisu auki) ei havainnut fy8-1-L2-08:n
sijoitusketjun ylivuotoa en-versiossa (oikea reuna 372 px vs. laatikko 330 px, yksikkö Hz leikkautui; ulkoasukatselmoija
löysi sen); lisää `check_layout.py`:hin tarkistus, joka mittaa ratkaisun kaavaketjun ylivuodon avoimessa tilassa
kaikilla kielillä 360 ja 390 px:llä.

## 5b. Leikkautuva kaava: tarkistus ja rivijako-carry (opettaja 2026-11-15)

Kohta 6 pysähtyi (fy8-1 #590, fy8-2 #593): ulkoasukatselmointi hylkäsi kahdessa erässä peräkkäin ratkaisujen
kaavaketjut, jotka leikkautuvat 360 px:llä (esim. "m/s" → "m/"). `check_layout.py` ei havaitse leikkautumista, ja jokainen
rivijakokorjaus vanhentaa kaikki katselmoinnit (fy8-2: noin 650 k ennen kolmatta kierrosta). Opettaja 2026-11-15 hyväksyi
molemmat:
1. `check_layout.py` havaitsee KaTeX-kaavan, joka leikkautuu tai ylittää laatikkonsa (myös inline-kaava ja avattu
   ratkaisu, kaikilla kolmella kielellä), jotta kehittäjä korjaa sen ennen katselmointeja. Testi löydöksillä fy8-2 L2-09
   ja L3-06 (#593:n kuvaus) ja fy8-1 L2-08 (#590).
2. Uusi carry-kategoria: kaavaketjun pelkkä rivijako (samat luvut, merkit ja yksiköt samassa järjestyksessä, vain
   rivinvaihdot ja `=`-rivien jako muuttuvat) siirtää tiede- ja pedagogiikkakatselmoinnit muutoksen yli. Ulkoasu
   katselmoidaan aina uudelleen. `reviews.py scope` tunnistaa ja `verify` johtaa sen uudelleen CI:ssä (kuten `formula-names`);
   mikä tahansa muu muutos samassa tehtävässä katselmoidaan normaalisti.
Jaettu muutos, ajetaan yksin, ennen kohtia 6 ja 8l. Sen jälkeen #593 (fy8-2) jatkaa kolmannella korjauksella.

## 6. Kuvatehtävät ja taulukkotehtävät FY8 ja FY9 (opettaja 2026-11-13, 2026-11-14 ja 2026-11-15)

Opettaja 2026-11-15: kaksi kuvatehtävää per luku on hyväksytty kustannuksesta huolimatta (noin 300 k per luku);
FY10:een ja FY14:ään ei tehdä kuvatehtäviä eikä taulukkotehtäviä.

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

## 8b. Itsearvion tasot väreissä jo ennen valintaa ja tiiviimpi kortti (opettaja 2026-11-13)

"Arvioi, mitä opit" -kortin tasosirut (Harjoittelen vielä, Osaan osittain, Osaan, Osaan opettaa, Ei vielä) näkyvät nyt
harmaina, kunnes yksi valitaan (P0-2, 2026-11-10: "quiet until chosen"). Opettaja: tekstien lisäksi samat värit kuin
moduulisivun itsearvioinnin yhteenvedossa (sormenjälki) jo ennen valintaa; valittu erottuu edelleen selvästi (esim.
täysi väri ja rasti, muut vaaleampina). Sama kortti FY1–FY8:ssa ja FY9:ssä. Lisäksi "Ei vielä" -siru rivittyy nyt
omalle rivilleen: mahdutetaan samalle riville leveällä näytöllä. Sivupohjan muutos (templates, site.css), ei
lukujen tekstejä; korjaa CLAUDE.md:n P0-2-kuvaus samassa PR:ssä. Kontrasti WCAG AA molemmissa teemoissa.

Samaan (opettaja 2026-11-13, "eikö tässä saisi tiivistettyä s.e. ei olisi noin paljon tyhjää"): kortti on nyt hyvin
väljä, kun jokaisen tavoitteen alle jää "Ei vielä" omalle rivilleen ja tavoitteiden väliin iso tyhjä tila
katkoviivoineen. Tiivistetään: kaikki viisi tasoa yhdelle riville leveällä näytöllä (sirut kapeammiksi tai "Ei vielä"
pieneksi linkiksi rivin perään), pienempi pystyväli tavoitteiden välillä ja kortin alalaidassa; puhelimella saa
rivittyä. Nappien vähimmäiskorkeus 40 px säilyy.

## 8c. Kappalejako esimerkkien ja ratkaisujen vaiheisiin (opettaja 2026-11-13)

Esimerkkien vaiheet (esim. fy3-13, vaihe 1/7 "Tunnetut ja kysytty") ovat yksi tiivis kappale, jossa on luettuja
pisteitä, huomautus ja kysymys peräkkäin: vaikea lukea. Opettaja: "näissä teksteissä saisi kappalejakoa olla …
esim. 'Lämpötila'-alkuinen virke voisi olla jo omalla rivillään." Sääntö: yksi asia per kappale; tunnetut (lista tai
oma kappale), huomautukset omaksi kappaleekseen, kysytty viimeiseksi omaksi rivikseen (CLAUDE.md Readability:
"the question last as its own sentence"). Kirjataan sääntö NOTES.md §3:een ja lintiin varoitukseksi (vaiheen
kappale yli ~60 sanaa tai useita virkkeitä eri asioista), sitten korjataan kurssi kerrallaan (`/quality-audit
--fix`, 116 lukua, joissa "Tunnetut ja kysytty"); sisältömuutos, joten katselmoinnit scope-säännön mukaan
(typografia/kappalejako: odotettavasti visual delta, muut carry). Ensin pilotti yhdellä luvulla (fy3-13) opettajan
nähtäväksi.

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

## 8i. FY2: energialajit taulukoksi (opettaja 2026-11-13)

fy2-1:n "Seitsemän energialajia" on luettelo pitkiä kohtia; opettaja: "tässäkin toimisi taulukko" (CLAUDE.md: "A table
when the content is a table"). Taulukko, esim. sarakkeet Energialaji (ja tunnus) | Mihin liittyy | Esimerkki;
käsitekorttien alleviivaukset säilyvät. Lämpöenergian kohdan selitys lämmön ja lämpöenergian erosta ei mahdu soluun:
se jää taulukon alle omaksi kappaleekseen. Kaikki kielet (fi, en, fi-easy). Sisältömuutos: katselmoinnit
`reviews.py scope fy2-1` mukaan (opettaja pyysi muutosta itse). Pieni oma PR.

## 8j. Pohdinnan kertaustehtävä liittyy pohdinnan ilmiöön (opettaja 2026-11-13)

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

## 8l. Taulukoiden otsikoista pois "(esimerkkiaineisto)" (opettaja 2026-11-15)

Opettaja 2026-11-15: "Voisiko taulukoista ottaa pois tuon (esimerkkiaineisto)". Tehtävien taulukko-otsikoissa (`"caption"`
`exercises.json`:issa) on merkintä noin 930 kertaa: fi 312, en 292 ("(example data)"), fi-easy 325, kursseilla FY2–FY8.
Poistetaan vain otsikoista. Jos sulkeissa on muutakin, se jää (esim. "(esimerkkiaineisto, energiat NNDC NuDat 3)" →
"(energiat NNDC NuDat 3)"). Tehtävätekstin maininnat (noin 18) ja taulukon alla oleva lähderivi eivät muutu. Tehdään
kohdan 8k `teacher-text`-kategorialla (opettajan nimenomainen hyväksyntä tälle mekaaniselle muutokselle), jotta
katselmoinnit kulkevat muutoksen yli. Jaettu muutos (`scripts/reviews.py` ja kaikki kurssit), ajetaan yksin, sim PR 3:n (#591) jälkeen.

## 9b. FY7:n kokeen jälkityöt (PR #586, koordinaattori 2026-11-14)

FY7:n esimerkkikoe on valmis (#586); sen katselmointien Minor-huomioita ei korjattu siinä, ettei katselmoinnit vanhene.
1. Jaettu, ajetaan yksin: `lang/fi.json` `koe.max` sitovilla välilyönneillä, jotta "120 p:n" ja "70 p." eivät katkea riviltä.
2. FY7-kokeen Minor-korjaukset (uusi katselmointi tai kevyt kuljetus): k7 c:n Sijoitukseen yksikkö luvulle 50 (`· 50 €/MWh`) ja tulos; k4 c:ssä 2789 (ei 2788) tai 12,374 V ketjussa; k5 b:n keskiarvomurtoluku isompana (`\tfrac` tai oma rivi); k6 d:n "noin yhdeksässä vuodessa" → "noin 9–10 vuodessa"; k2 c:n rivi B²k tiukka 390 px:llä; k7 b nimeää Wienin vakion, harkitse. Pedagogiikan huomio: k3 ja k4 valittaessa ei kuvaaja- tai epävarmuusosaa, harkitse lyhyttä osaa toiseen.

## 10. Simulaatioiden käyttöliittymä (opettaja 2026-11-14)

Mittaus, päätökset ja rajaukset: `docs/audits/2026-11-14-simulaatioiden-kayttoliittyma.md`. Matalalla kannettavalla
(1366×650) simulaation kuva kapenee 384 px:iin ja sen tekstit noin 7 px:iin; puhelimella kuva vierii pois säätimiä
käytettäessä. Osat tässä järjestyksessä, kukin oma pull requestinsa. PR 1–PR 5 muuttavat jaettuja tiedostoja
(`templates/`, `scripts/`): ne tehdään yksin, yksi kerrallaan, ja yhdistetään ennen sisältömuutoksia. Pilotit (PR 2,
PR 4) pysähtyvät opettajan hyväksyntään ennen yleistystä. Yksikään osa ei muuta sim.js-tiedostoja, simulaatioiden
lang-tekstejä tai fysiikkaa.

- **PR 1 (tehty, #563)** kuvan todellinen leveys tekstikoon perustaksi (`sim-embed.js`) ja selaintesti 1366×650 (kuvan tekstit
  vähintään 10 px) omina CI-jobeinaan.
- **PR 2: Varattu: claude/sim-ui-pr2-pilotti-fy4-1** pilotti fy4-1: lukemat kuvan alle, toistorivi yhdelle riville, `.lab-side .sim-canvas`-säännön 25 rem:n
  varaus pienemmäksi, kuvausteksti pois kokeiden vierestä.
- **PR 3: Varattu: claude/sim-ui-pr3-asettelu** sama asettelu tyypeille A–C (aikaohjatut, jatkuvat, staattiset); tyyppi D, fy1-2, fy1-4 ja poikkeavat
  jäävät nykyiselleen.
- **PR 4:** tarttuva kuva puhelimella, pilotti fy4-1 ja yksi staattinen simulaatio.
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

## 13. Englanninkieliset käsitekortit FY6 ja FY8 (opettaja 2026-11-13: tehdään myöhemmin)

`kortit/en/` ei sisällä tiedostoja `fy6.json` ja `fy8.json`, joten englanninkielisillä FY6- ja FY8-sivuilla ei ole
käsitekortteja eikä alleviivauksia.

## 14. Ahjo ja LUMA-tutor yhteiseen jaksopohjaan (opettaja 2026-11-13; järjestys 2026-11-14)

Kilparobotiikka on kirjoitettu jaksopohjan lohkoina (#516–#517, `scripts/jaksot.py`); Ahjo ja LUMA-tutor piirtyvät
vielä osin omilla moduuleillaan (`ahjo.py`, `lumatutor.py`). Siirretään ne samaan pohjaan niin, että sivut pysyvät
tavulleen samoina kuten Kilparobotiikassa, ja puuttuvat lohkot lisätään yhteiseen lohkokirjastoon. Jaettuja
tiedostoja: tehdään yksin.

## 15. Kustannustoimituksellinen lopputarkistus FY1–FY8 (opettaja 2026-11-14)

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
- Kaikki FY1–FY8-oppitunnit järjestelmällisesti, kurssi kerrallaan.
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

## 16. Vihkot FY1–FY8 nykyisellä tiiviillä asettelulla (opettaja 2026-11-13; jonon viimeinen 2026-11-14)

Tulostettavat A5-vihkot (`python scripts/print_book.py <C> --lang fi|en --publish`, README "Printed A5 book") kaikille
kursseille FY1–FY8 sivuja säästävällä tiiviillä asettelulla (#393). FY1–FY4:llä vihko on (7.11.), mutta sisältö on
muuttunut sen jälkeen (kaavat taulukkokirjan muotoon, käsitteet, korjaukset), joten ne tehdään uudelleen; FY5–FY8 ovat uusia. Kurssin
vihko tehdään vasta, kun sen kohdan 3 kaavat taulukkokirjan muodossa on yhdistetty, ettei sitä tarvitse tehdä kahdesti. Rakenna sivusto
vihkojen jälkeen (Vihkot-sivu).

## Kirjattu päätös: teorian taitto, vaihtoehto B (opettaja 2026-11-14)

Opettaja vertasi kolmea vaihtoehtoa 14.11. ja valitsi B:n: nykyinen 38 rem:n palsta säilyy, ja asettelu korjataan
kohdan 8e mukaan (kohta 11, U3). Entinen kohta 7 (keskitetty tekstiraita ja marginaaliraita) poistettiin jonosta.
Perustelu: marginaaliin mahtuva kuva olisi noin neljänneksen pienempi, ja Teoria olisi ainoa keskitetty vaihe.

## Kirjattu päätös: luvut ilman käsitekortteja (opettaja 2026-11-13)

Luvut fy3-13, fy3-14, fy3-16 ja fy4-16 jäävät ilman omia kortteja ja alleviivauksia (#526:n siirtojen jälkeen).
Kortteja ei lisätä niihin.
