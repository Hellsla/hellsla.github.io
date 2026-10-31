# FY10-tutkimusten toteutettavuus (tarkistus 31.10.2026)

Tarkistin kaikkien 27 julkaistun tutkimuksen työohjeet ja mittausmenetelmät: välineet, sen, saadaanko tutkittava suure todella mittauksista, oletukset, menetelmien johdonmukaisuuden, systemaattiset virheet, F/E-luokituksen, ennakkovalmistelut ja sopivuuden lukioon. Kriteerit ja luokat A/B/C ovat samat kuin tiedostossa `docs/physics-guardrails.md`: **A** on fysiikan tai menetelmän virhe, **B** puuttuva ehto tai epäjohdonmukaisuus ja **C** hyväksyttävä yksinkertaistus. Tarkistus on tehty paperilla. Kokeita ei ole mitattu.

## Yhteenveto

- **A-virheitä ei löytynyt.** Jokaisen tutkimuksen analyysiketju toimii: malli, linearisointi, kulmakerroin tai pinta-ala, haettu suure, yksiköt ja epävarmuus.
- **B-havaintoja oli 18.** Korjasin niistä 13 selvää täsmennystä ja yhtenäistin työselostuksen osien nimet (alla). Viisi F/E-luokitusta jätin opettajan päätettäviksi.
- **Ei keksittyjä turvallisuusrajoja.** Kaikki välinekohtaiset rajat ovat yhä muodossa "opettajan ilmoittama raja" tai "laitteen ohjeen mukaan".
- **Kestoa ei arvioitu.** Toteutuksen keston kertovat vain kolme tutkimusta (lämmön johtuminen noin kaksi 75 minuutin tuntia, kaasu yksi pitkä tunti OO-työtavalla ja jäähtyminen "suurin osa oppitunnista"). Siksi kestoa ei käytetä tutkimuspankin suodattimena.

| Tutkimus | Toteutettavuus | F/E | Korjattu |
|---|---|---|---|
| Pudotus- ja pomppukorkeus | kyllä | ok | – |
| Lämmön johtuminen lämpökameralla | **koemittaus tarpeen** (kameran erottelukyky) | ok | 2 systemaattista virhettä lisätty |
| Leikkiauton nopeus ja lähtökorkeus | kyllä, valmistelu | ok | – |
| Liikemäärän säilyminen törmäyksissä | kyllä, valmistelu (kaksi liikeanturia vastakkain) | ok | – |
| Putoamiskiihtyvyys heilurin avulla | kyllä | ok | – |
| Jousivakion määrittäminen | kyllä | laajennus E3 → E2 (opettaja 31.10.) | vakiotermin syy lisätty; E2 |
| Hypyn tutkiminen voimalevyllä | kyllä, vaatii voimalevyn | ok | ristiriita korjattu |
| Hissin kulkema matka kiihtyvyydestä | **koemittaus tarpeen** (nollakohdan virhe) | ok | oletus "kerrokset yhtä korkeita" lisätty |
| Pallon muotokerroin | **koemittaus tarpeen** (rajanopeus kuvausalueella) | ok | – |
| Liukukitkakerroin | kyllä, valmistelu | ok | – |
| Tuulivoimala | **koemittaus tarpeen** (koulun malli) | ok | true RMS -ehto opettajalle |
| Äänen nopeus kulkuajasta | kyllä, valmistelu | laajennus E3 (opettaja 31.10.) | – |
| Uppokuumentimen hyötysuhde | kyllä, kun opettaja on antanut virtarajan | laajennus E3 → E2 | olomuodon muutoksen ehto; E2 |
| Valaistusvoimakkuus ja etäisyys | kyllä, valmistelu | ok | – |
| Kuuman veden jäähtyminen | **koemittaus tarpeen** (kaksi puoliintumisaikaa tunnissa) | ok | – |
| Kaasun tilanyhtälö | kyllä, valmistelu | ok | – |
| Vesivoimalaitoksen pienoismalli | **koemittaus tarpeen** (koulun malli) | ok | roiskeet ja true RMS |
| Äänen resonanssi putkessa | kyllä, valmistelu | laajennus E3 → E2 (opettaja 31.10.) | E2 |
| Valonnopeus mikroaaltouunilla | **koemittaus tarpeen** (uunikohtainen) | ok | – |
| Pariston kuormituskäyrä | kyllä, valmistelu | ok | pidikkeen kosketusresistanssi |
| Kondensaattorin kapasitanssi | kyllä, valmistelu | ok | välineluetteloon vaihtokytkin |
| Muuntajan tutkiminen | kyllä, valmistelu | laajennus E3 → E2 | turvallisuuslause täsmennetty; E2 |
| Sähkömagneettinen induktio | kyllä (näytteenottotaajuus kokeiltava) | oma tekijä E3 → E2 | E2 |
| Planckin vakio LEDien avulla | kyllä, valmistelu | ok | – |
| Hiuksen paksuus | kyllä | ok | – |
| Taitekerroin | kyllä | ok | – |
| Umpinaisen sylinterin hitausmomentti | **koemittaus tarpeen** (ajanoton tarkkuus) | ok | käsiajanoton epätarkkuus opettajalle |

## Korjatut kohdat

1. **Pariston kuormituskäyrä.** Jännitemittari kytketään pariston napoihin, koska pidikkeen kosketusresistanssi näkyisi muuten osana sisäistä resistanssia.
2. **Kondensaattori.** Kytkentä tarvitsee vaihtokytkimen (asennot A ja B). Välineluettelossa luki vain "kytkin".
3. **Muuntaja, opettajalle.** Teksti "toisiojännite pysyy pienjännitteenä" ei sano, mitä tarkoitetaan, koska sähköalan pienjännite kattaa myös verkkojännitteen. Nyt teksti sanoo: kosketusvaaraton, opettajan ilmoittaman rajan alapuolella. Lukua ei annettu.
4. **Hitausmomentti, opettajalle.** Käsin otettu aika on yleensä liian epätarkka. Hitausmomentti saadaan erotuksesta, jossa ajan suhteellinen virhe moninkertaistuu.
5. **Tuulivoimala ja vesivoima, opettajalle.** Vaihtojännitteen tehollisarvo luetaan oikein vain true RMS -mittarilla tai, kun jännite on sinimuotoinen, mittarin taajuusalueella.
6. **Uppokuumennin.** Yhtälö $Q = cm\Delta T$ pätee vain, kun olomuoto ei muutu.
7. **Vesivoima.** Jos vettä roiskuu keräysastian ohi, $\Delta m$ jää liian pieneksi ja hyötysuhde tulee liian suureksi.
8. **Lämmön johtuminen.** Kaksi uutta virhelähdettä: kappale näkyy kuvassa vain muutaman kuvapisteen levyisenä, ja kannen yläpuolinen lämmin ilma lämmittää kappaleita.
9. **Jousivakio.** Tiiviisti kierretyn jousen suora ei kulje origon kautta, mutta kulmakerroin on silti jousivakio.
10. **Hyppy.** Lause "Mittausohjelma laskee …" oli ristiriidassa sivun oman vihjeen kanssa, koska ohjelmat integroivat aika-akseliin asti.
11. **Hissi.** Kulmakerroin on kerroskorkeus vain, jos kaikki kerrokset ovat yhtä korkeita.
12. **Työselostuksen osien nimet.** Raportoi-osioissa 14 tutkimusta käytti otsikkoa "Työn suunnitelma" ja pariston tutkimus otsikkoa "Tulokset". Nyt nimet ovat samat kuin FY10:n työselostuspohjassa (`local-courses.json`): "Koejärjestely ja menetelmä" ja "Tulos".
13. **F/E-luokitus.** Muuntajan laajennus, induktion "oma tekijä" ja uppokuumentimen laajennus muutettiin E3:sta E2:ksi. Opettajan päätöksellä (31.10.2026) myös jousivakion laajennus (värähtely, sama menetelmä kuin heilurissa) ja resonanssin laajennus (sama mittaus usealla taajuudella) ovat E2. Äänen nopeuden laajennus jää E3:ksi, koska opiskelija suunnittelee siinä toisen, oman menetelmänsä. Ne toistavat perusosan menetelmän. Lisävaativuus on tulkinnassa tai työtavassa, ei kokeen teknisessä vaativuudessa.

Muutetut tutkimukset kävivät uudelleen läpi fysiikan ja pedagogiikan katselmoinnin ennen julkaisua.

## Opettajan päätettävät

- **Koemittaus ennen käyttöä:** lämmön johtuminen, hissi, muotokerroin, tuulivoimala, vesivoima, jäähtyminen, mikroaaltouuni ja hitausmomentti. Näiden toteutettavuus riippuu koulun omista välineistä. Paperilla tehty tarkistus ei voi vahvistaa sitä.
- **Laserluokka** (liikemäärä, hiuksen paksuus, taitekerroin) ja **uppokuumentimen virtaraja** ovat yhä opettajan vahvistettavia. Ne on merkitty sivuille, eikä niille ole keksitty arvoja.
- **Erityisvälineet**, joita kaikilla kouluilla ei ole: lämpökamera, kaksi optista liikeanturia, voimalevy, hissi (lupa), 0,1 g:n vaaka ja videoanalyysi.
