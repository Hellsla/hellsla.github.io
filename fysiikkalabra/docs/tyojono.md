# Työjono

Opettajan päättämät tulevat työt, joita ei ole vielä aloitettu. Jokainen kohta tehdään omana pull requestinaan;
valmis kohta poistetaan tästä samassa pull requestissa.

Tämä on ainoa työjono (opettaja 2026-11-13): ei GitHub Issuesia eikä erillisiä listoja. Kohdat ovat
`docs/ROADMAP.md`:n järjestyksessä. Kohdan ottava ketju katsoo ensin avoimet pull requestit, merkitsee kohtaan
ensimmäisessä commitissaan `Varattu: <haara>` ja avaa luonnos-PR:n heti, jotta muut ketjut näkevät varauksen
(repon juuren `CLAUDE.md`). Saman kurssin kohdat tehdään peräkkäin, eri kurssien enintään kolme rinnakkain.

## 2. Tehtäväsarjojen katselmoinnit: FY1, fy4-8, FY5, FY6, FY7 (opettaja 2026-11-13: tässä järjestyksessä)

Sarjat ovat luonnoksina eivätkä näy opiskelijoille (`python scripts/reviews.py status`): FY1 8, fy4-8 1, FY5 13,
FY6 15, FY7 14, kukin fi, en ja fi-easy. Katselmointi `/exercises`-putken vaiheilla (`reviews.py scope <id>
--exercises`, kolme katselmoijaa) kuten FY4:ssä (#531). Yksi kurssi per PR; kurssin MAFY-kaavat (kohta 3) samassa
ketjussa tai heti perään, ei rinnakkain.

## 3. Kaavat MAFY-muotoon FY5–FY8, FY10 ja FY14

FY1–FY4 ja FY9 on tehty (#501, #522, #527, #529). Keskinopeuden tunnus on kaikkialla $v_\text{k}$, ei $v_\text{ka}$
(opettaja 2026-11-13).

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

## 6. Kuvatehtävät FY8, FY9, FY10 ja FY14, MAFY-taulukkotehtävät FY8 ja FY9 (opettaja 2026-11-13 ja 2026-11-14)

Sama tahti kuin FY4:stä alkaen: jokaisessa luvussa vähintään kaksi kuvatehtävää ja MAFY-taulukkotehtävä noin joka
kolmannessa luvussa (#521, #528). FY10:een ja FY14:ään ei lisätä MAFY-taulukkotehtäviä, vain kuvatehtävät (opettaja
2026-11-14). Arvot vain `docs/mafy-arvot.tsv`:stä, uudet rivit lähde-URL:n kanssa. Aloitetaan,
kun kohdan 2 katselmoinnit on tehty, jotta katselmoimattomien sarjojen jono ei kasva.

## 7. Työpöytäasettelu: keskitetty tekstiraita ja marginaaliraita (opettaja 2026-11-13)

Isoin jäljellä oleva rakenteellinen UI-muutos. Työpöydällä lukupalsta keskitetään, ja sen viereen tulee
marginaaliraita (kuvat, kaavat, huomautukset). Jaettuja tiedostoja (`templates/`, `site.css`, `check_layout.py`):
tehdään yksin ja yhdistetään ennen muita. Ennen toteutusta vaiheittainen arvio ja vertailukuvat opettajalle
(CLAUDE.md "Where direction B goes": ei laajaa uudistusta yhdellä kertaa).

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

## 8h. Ensimmäinen ennuste näkyy aina (opettaja 2026-11-13)

Ennusta-vaihe on nyt yksi suljettu laatikko "Tee ennusteet ennen tutkimista · N kysymystä" (CLAUDE.md Lesson page 3,
2026-10-26), joten vaihe näyttää tyhjältä. Opettaja: "ehkä ensimmäinen ennuste pitäisi aina näkyä. Nyt jää muuten
turhan tyhjäksi tuo ennuste-kohta." Muutos: ensimmäinen ennustekysymys näkyy auki vaiheen alussa, muut (jos on)
laatikossa "Lisää ennusteita · N kysymystä"; yhden ennusteen luvussa ei laatikkoa lainkaan. Sitoutuminen ennen
vastausta (gating), tallennus ja Palaa ennusteisiisi -yhteenveto ennallaan. Sivupohjan muutos (inquiry.py/js,
site.css), ei lukujen tekstejä; korjaa CLAUDE.md:n Lesson page 3 samassa PR:ssä; test_inquiry ja test_progress.
Yhdistetään #546:n jälkeen (sama Ennusta-alue).

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

## 9. Esimerkkikokeet FY7 ja FY8 (opettaja 2026-11-13)

FY1–FY6:lla on esimerkkikoe (`content/fi/<COURSE>/koe/`), FY7:llä ja FY8:lla ei. `/exam FY7` ja `/exam FY8`
(`docs/exam-guidelines.md`), kumpikin omana PR:nään ja kolmella katselmoinnilla. FY8:n tehtävät on katselmoitu, joten
sen koe voi alkaa heti; FY7:n koe kohdan 2 FY7-katselmointien jälkeen, ettei sama kurssi ole kahdessa ketjussa.

## 10. Englanninkieliset käsitekortit FY6 ja FY8 (opettaja 2026-11-13: tehdään myöhemmin)

`kortit/en/` ei sisällä tiedostoja `fy6.json` ja `fy8.json`, joten englanninkielisillä FY6- ja FY8-sivuilla ei ole
käsitekortteja eikä alleviivauksia.

## 11. Ahjo ja LUMA-tutor yhteiseen jaksopohjaan (opettaja 2026-11-13: viimeisenä)

Kilparobotiikka on kirjoitettu jaksopohjan lohkoina (#516–#517, `scripts/jaksot.py`); Ahjo ja LUMA-tutor piirtyvät
vielä osin omilla moduuleillaan (`ahjo.py`, `lumatutor.py`). Siirretään ne samaan pohjaan niin, että sivut pysyvät
tavulleen samoina kuten Kilparobotiikassa, ja puuttuvat lohkot lisätään yhteiseen lohkokirjastoon. Jaettuja
tiedostoja: tehdään yksin.

## 12. Vihkot FY1–FY8 nykyisellä tiiviillä asettelulla (opettaja 2026-11-13)

Tulostettavat A5-vihkot (`python scripts/print_book.py <C> --lang fi|en --publish`, README "Printed A5 book") kaikille
kursseille FY1–FY8 sivuja säästävällä tiiviillä asettelulla (#393). FY1–FY4:llä vihko on (7.11.), mutta sisältö on
muuttunut sen jälkeen (MAFY-kaavat, käsitteet, korjaukset), joten ne tehdään uudelleen; FY5–FY8 ovat uusia. Kurssin
vihko tehdään vasta, kun sen kohdan 3 MAFY-kaavat on yhdistetty, ettei sitä tarvitse tehdä kahdesti. Rakenna sivusto
vihkojen jälkeen (Vihkot-sivu).

## 13. Simulaatioiden käyttöliittymä (opettaja 2026-11-14)

Mittaus, päätökset ja rajaukset: `docs/audits/2026-11-14-simulaatioiden-kayttoliittyma.md`. Matalalla kannettavalla
(1366×650) simulaation kuva kapenee 384 px:iin ja sen tekstit noin 7 px:iin; puhelimella kuva vierii pois säätimiä
käytettäessä. Osat tässä järjestyksessä, kukin oma pull requestinsa. PR 1–PR 5 muuttavat jaettuja tiedostoja
(`templates/`, `scripts/`): ne tehdään yksin, yksi kerrallaan, ja yhdistetään ennen sisältömuutoksia. Pilotit (PR 2,
PR 4) pysähtyvät opettajan hyväksyntään ennen yleistystä. Yksikään osa ei muuta sim.js-tiedostoja, simulaatioiden
lang-tekstejä tai fysiikkaa.

- **PR 1:** kuvan todellinen leveys tekstikoon perustaksi (`sim-embed.js`) ja selaintesti 1366×650 (kuvan tekstit
  vähintään 10 px) omina CI-jobeinaan.
- **PR 2:** pilotti fy4-1: lukemat kuvan alle, toistorivi yhdelle riville, `.lab-side .sim-canvas`-säännön 25 rem:n
  varaus pienemmäksi, kuvausteksti pois kokeiden vierestä.
- **PR 3:** sama asettelu tyypeille A–C (aikaohjatut, jatkuvat, staattiset); tyyppi D, fy1-2, fy1-4 ja poikkeavat
  jäävät nykyiselleen.
- **PR 4:** tarttuva kuva puhelimella, pilotti fy4-1 ja yksi staattinen simulaatio.
- **PR 5:** canvasin nimi ja kuvaus, valintaruudut 40 px:n kohteiksi, näkyvä kohdistus.

Myöhemmin kurssi kerrallaan, kunkin luvun seuraavan sisältömuutoksen yhteydessä katselmointeineen: tyyppi D (fy6-5,
fy6-6, fy6-9, fy6-12, fy6-13, fy6-14), fy1-2:n säätimien ryhmittely, näppäinvaihtoehto raahaukselle, nimien
yhtenäistäminen (Toisto / Tauko / Alusta) ja toistuvien seliterivien poisto.

## Kirjattu päätös: luvut ilman käsitekortteja (opettaja 2026-11-13)

Luvut fy3-13, fy3-14, fy3-16 ja fy4-16 jäävät ilman omia kortteja ja alleviivauksia (#526:n siirtojen jälkeen).
Kortteja ei lisätä niihin.
