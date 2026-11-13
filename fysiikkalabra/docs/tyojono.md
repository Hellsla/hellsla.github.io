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

Varattu: claude/fy10-tvt-major-korjaukset (erät 2–4: liukukitka, hiuksen-paksuus, induktio, jousivakio, tvt-kuvaaja, tvt-tyoselostus)

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

## 6. Kuva- ja MAFY-taulukkotehtävät FY8, FY9, FY10 ja FY14 (opettaja 2026-11-13)

Sama tahti kuin FY4:stä alkaen: jokaisessa luvussa vähintään kaksi kuvatehtävää ja MAFY-taulukkotehtävä noin joka
kolmannessa luvussa (#521, #528). Arvot vain `docs/mafy-arvot.tsv`:stä, uudet rivit lähde-URL:n kanssa. Aloitetaan,
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

## Kirjattu päätös: luvut ilman käsitekortteja (opettaja 2026-11-13)

Luvut fy3-13, fy3-14, fy3-16 ja fy4-16 jäävät ilman omia kortteja ja alleviivauksia (#526:n siirtojen jälkeen).
Kortteja ei lisätä niihin.
