## fy2-s1

### a)
**Annettu:** tuulivoimalan nimellisteho $P_\text{n} = 5{,}0\,\text{MW}$, käyttöaste $k = 0{,}32$, vuoden pituus $t = 8760\,\text{h}$ ja kaupungin vuosikulutus $E = 380\,\text{GWh}$
**Kysytty:** tarvittavien tuulivoimaloiden määrä $N$
**Periaate:** Tuulivoimala ei käy koko vuotta nimellisteholla, koska tuuli vaihtelee. Käyttöaste kertoo vuoden keskitehon: $P_\text{keski} = k \cdot P_\text{n}$. Teho vaihtelee, mutta vuoden energia on keskiteho kertaa aika. Kun yhden voimalan vuosienergia tiedetään, jaetaan kulutus sillä. Näin saadaan voimaloiden määrä. Määrä on kokonaisluku. Sen on oltava vähintään laskettu arvo.
**Kaava:** $E_1 = k \cdot P_\text{n} \cdot t$ ja $N = \dfrac{E}{E_1}$
**Muunnokset:** Kun teho on megawatteina ja aika tunteina, energia on megawattitunteina. Muunnos on $1\,\text{GWh} = 1000\,\text{MWh}$.
**Sijoitus:** $E_1 = 0{,}32 \cdot 5{,}0\,\text{MW} \cdot 8760\,\text{h} = 14\,016\,\text{MWh} = 14{,}0\,\text{GWh}$ ja $N = \dfrac{380\,\text{GWh}}{14{,}0\,\text{GWh}} = 27{,}1$
**Vastaus:** Tarvitaan $28$ tuulivoimalaa. Laskettu arvo $27{,}1$ pyöristetään ylöspäin. Syy on se, että $27$ voimalaa tuottaisi vain $27 \cdot 14{,}0\,\text{GWh} = 378\,\text{GWh}$. Se on liian vähän. Määrä on kokonaisluku, joten merkitsevien numeroiden sääntö ei rajoita sitä.
**Järkevyys:** Kaupungin keskiteho on $\dfrac{380\,000\,\text{MWh}}{8760\,\text{h}} \approx 43\,\text{MW}$. Voimaloiden yhteinen nimellisteho on $28 \cdot 5{,}0\,\text{MW} = 140\,\text{MW}$. Se on noin kolminkertainen. Tämä sopii käyttöasteeseen $0{,}32 \approx \tfrac{1}{3}$.

### b)
**Annettu:** vuosikulutus $E = 380\,\text{GWh}$ ja elinkaaren päästökertoimet: kivihiili $e = 820\,\text{g/kWh}$, maakaasu $490\,\text{g/kWh}$ ja tuulivoima maalla $11\,\text{g/kWh}$
**Kysytty:** vuotuinen päästö $m$ kullakin tavalla ja päästön pieneneminen prosentteina kivihiileen verrattuna
**Periaate:** Päästökerroin kertoo, montako grammaa hiilidioksidiekvivalenttia syntyy yhtä kilowattituntia kohti. Mukana on koko elinkaari. Kun kaikki kilowattitunnit tuotetaan samalla tavalla, päästö on suoraan verrannollinen energiaan. Prosentuaalinen pieneneminen on päästöjen erotus suhteessa kivihiilen päästöön. Energia on kaikissa vaihtoehdoissa sama, joten se supistuu. Siksi suhteen voi laskea suoraan päästökertoimista.
**Kaava:** $m = e \cdot E$ ja pieneneminen $\dfrac{m_\text{hiili} - m}{m_\text{hiili}} = 1 - \dfrac{e}{e_\text{hiili}}$
**Muunnokset:** $E = 380\,\text{GWh} = 380 \cdot 10^{6}\,\text{kWh}$, koska kerroin on yksikössä $\text{g/kWh}$. Lopuksi $1\,\text{t} = 10^{6}\,\text{g}$.
**Sijoitus:** Kivihiili: $m = 820\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} = 3{,}116 \cdot 10^{11}\,\text{g} = 3{,}116 \cdot 10^{5}\,\text{t}$. Maakaasu: $m = 490\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} = 1{,}862 \cdot 10^{11}\,\text{g} = 1{,}862 \cdot 10^{5}\,\text{t}$. Tuulivoima: $m = 11\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} = 4{,}18 \cdot 10^{9}\,\text{g} = 4{,}18 \cdot 10^{3}\,\text{t}$. Pieneneminen: maakaasu $1 - \dfrac{490\,\text{g/kWh}}{820\,\text{g/kWh}} = 0{,}40$ ja tuulivoima $1 - \dfrac{11\,\text{g/kWh}}{820\,\text{g/kWh}} = 0{,}99$
**Vastaus:** Kivihiilellä $m \approx 3{,}1 \cdot 10^{5}\,\text{t}$, maakaasulla $1{,}9 \cdot 10^{5}\,\text{t}$ ja tuulivoimalla $4{,}2 \cdot 10^{3}\,\text{t}$ vuodessa. Tarkkuus on kaksi merkitsevää numeroa, kuten päästökertoimissa. Maakaasu pienentää päästöä noin $40\,\%$ ja tuulivoima noin $99\,\%$.
**Järkevyys:** Kivihiilellä syntyy vajaa kilogramma kilowattituntia kohti. Kilowattitunteja on satoja miljoonia. Siksi satoja tuhansia tonneja on oikea suuruusluokka. Prosentit täsmäävät tonneista laskettuihin: maakaasulla jää $\dfrac{1{,}862 \cdot 10^{5}\,\text{t}}{3{,}116 \cdot 10^{5}\,\text{t}} \approx 0{,}60$ kivihiilen päästöstä. Pieneneminen on siis $40\,\%$. Tuulivoimankaan päästö ei ole nolla, koska voimaloiden valmistus ja rakentaminen aiheuttavat päästöjä.

### c)
**Annettu:** $N = 28$ tuulivoimalaa, yhden vuosienergia $E_1 = 14{,}0\,\text{GWh}$, talven osuus tuulivoiman vuosienergiasta $32\,\%$ ja kaupungin vuosikulutuksesta $31\,\%$, kulutus $E = 380\,\text{GWh}$, talven pituus $90\,\text{d}$, huipputeho $80\,\text{MW}$ ja tyynen jakson teho alle $5\,\%$ nimellistehosta
**Kysytty:** tuulivoimaloiden keskiteho $P_\text{t}$ joulu–helmikuussa ja riittääkö se kaupungin tarpeeseen
**Periaate:** Taulukosta saadaan, kuinka suuri osa vuoden energiasta tuotetaan ja kulutetaan talvella. Talven keskiteho on talven energia jaettuna talven tunneilla. Keskiteho kertoo vain, riittääkö energia keskimäärin. Kulutus ja tuuli vaihtelevat talvenkin aikana. Siksi tarvetta on verrattava myös huipputehoon ja tyynen jakson tehoon.
**Kaava:** $P_\text{t} = \dfrac{0{,}32 \cdot N E_1}{t}$ ja kaupungin talven keskiteho $P_\text{k} = \dfrac{0{,}31 \cdot E}{t}$
**Muunnokset:** $t = 90 \cdot 24\,\text{h} = 2160\,\text{h}$ ja $1\,\text{GWh} = 1000\,\text{MWh}$
**Sijoitus:** $N E_1 = 28 \cdot 14{,}016\,\text{GWh} = 392{,}4\,\text{GWh}$. $P_\text{t} = \dfrac{0{,}32 \cdot 392{,}4\,\text{GWh}}{2160\,\text{h}} = \dfrac{125\,600\,\text{MWh}}{2160\,\text{h}} = 58{,}1\,\text{MW}$ ja $P_\text{k} = \dfrac{0{,}31 \cdot 380\,\text{GWh}}{2160\,\text{h}} = \dfrac{117\,800\,\text{MWh}}{2160\,\text{h}} = 54{,}5\,\text{MW}$. Tyynellä jaksolla teho on $P_\text{tuuli} < 0{,}05 \cdot 28 \cdot 5{,}0\,\text{MW} = 7\,\text{MW}$. Muualta tarvitaan siis $P_\text{muualta} > 80\,\text{MW} - 7\,\text{MW} = 73\,\text{MW}$.
**Vastaus:** Tuulivoimaloiden keskiteho talvella on $P_\text{t} \approx 58\,\text{MW}$. Tarkkuus on kaksi merkitsevää numeroa, kuten taulukon prosenttiosuuksissa. Keskiteho on hieman suurempi kuin kaupungin talven keskimääräinen tarve $55\,\text{MW}$. Talven energia riittää siis keskimäärin. Tyynenä pakkasiltana tuulivoimaloiden yhteisteho voi kuitenkin jäädä alle $7\,\text{MW}$:n. Jos kaupunki tarvitsee silloin $80\,\text{MW}$, muualta tarvitaan yli $73\,\text{MW}$ sähkötehoa.
**Järkevyys:** Talvi on neljännes vuodesta. Sille osuu noin kolmannes sekä tuotannosta että kulutuksesta. Siksi talven keskitehot ovat suurempia kuin vuoden keskitehot ($45\,\text{MW}$ ja $43\,\text{MW}$), kuten kuuluukin. Kumpikin keskiteho on pienempi kuin huipputeho $80\,\text{MW}$, kuten keskiarvon pitääkin olla.

### d)
**Kysytty:** kuinka paljon aurinkopuistot auttavat huippuiltana, ja mitkä tuotantotavat voisivat tuottaa tehoa tyynenä pakkasiltana, rajoituksineen
**Periaate:** Vuoden energia ei kerro, onko tehoa saatavilla juuri silloin, kun sitä tarvitaan. Huippuiltana ratkaisee teho sillä hetkellä. Sen voivat tuottaa voimalat, joiden tehoa voi säätää. Sen voivat tuottaa myös voimalat, jotka käyvät tasaisesti säästä riippumatta. Tehon säätö ja sääriippuvuus ovat ominaisuuksia, joilla on rajansa. Ne eivät ole ehdottomia luokkia.
**Mallivastaus:** Yhden aurinkopuiston vuosienergia on $0{,}11 \cdot 10\,\text{MW} \cdot 8760\,\text{h} \approx 9{,}6\,\text{GWh}$. Siksi $40$ puistoa tuottaa noin $385\,\text{GWh}$ vuodessa. Talvella siitä tulee taulukon mukaan vain $4\,\%$ eli noin $15\,\text{GWh}$. Se vastaa keskitehoa $\dfrac{15\,400\,\text{MWh}}{2160\,\text{h}} \approx 7\,\text{MW}$. Tammikuun illalla on pimeää, joten teho huipun aikaan on nolla. Aurinkosähkö tuotetaan pääosin kesällä. Silloin kulutus on pienimmillään.

Tyynenä pakkasiltana tehoa voisivat tuottaa
- *maakaasuvoimala* ($50\,\text{MW}$): tehoa voi nostaa nopeasti, mutta kaasu on tuontipolttoainetta. Päästökerroin on uusista vaihtoehdoista suurin.
- *biomassavoimala* ($40\,\text{MW}$): tehoa voi säätää, mutta voimala käynnistyy hitaammin. Polttoainetta on kuljetettava ja varastoitava.
- *vesivoimaosuus* ($20\,\text{MW}$): tehoa voi säätää nopeasti, mutta vuoden energia riippuu sateista. Siksi vettä ei voi käyttää rajattomasti.
- *pieni ydinvoimala* ($60\,\text{MW}$): se käy tasaisesti säästä riippumatta, joten se on käynnissä myös huippuiltana. Tehoa ei voi nostaa nimellistehoa suuremmaksi. Voimalaa ei myöskään ole vielä saatavilla.
- *verkosta ostettu sähkö*: sitä voi käyttää, kun muualla on tuotantoa vapaana. Koko Suomen kulutus on kuitenkin suurimmillaan samoina pakkasiltoina.

### e)
**Kysytty:** perusteltu suositus kaupungin sähköntuotannoksi laskelmineen, vastaperusteineen ja oletuksineen
**Periaate:** Hyvä suositus kattaa kaksi eri vaatimusta: vuoden energian (a- ja b-kohtien laskut) ja talven huipputehon (c- ja d-kohdat). Päästö lasketaan jokaiselle tuotantotavalle erikseen kaavalla $m = e \cdot E$. Sitten päästöt lasketaan yhteen. Valinta on arvovalinta. Päästöjen lisäksi painavat tehon säätö, polttoaine, maankäyttö, jäte ja aikataulu. Siksi yhtä oikeaa tuotantotapaa ei ole. Vastaus arvioidaan perustelujen perusteella. Alla on yksi mahdollinen suositus.
**Mallivastaus:** Suosittelen yhdistelmää: $18$ tuulivoimalaa, kaupungin osuus vesivoimalasta ja yksi biomassavoimala. Biomassavoimala käy pääasiassa silloin, kun tuuli ei riitä.

*Energia.* Tuulivoimalat tuottavat $18 \cdot 14{,}0\,\text{GWh} \approx 252\,\text{GWh}$ vuodessa. Vesivoimaosuus tuottaa $0{,}50 \cdot 20\,\text{MW} \cdot 8760\,\text{h} \approx 88\,\text{GWh}$ vuodessa. Loput $380\,\text{GWh} - 252\,\text{GWh} - 88\,\text{GWh} \approx 40\,\text{GWh}$ tuottaa biomassavoimala. Sen käyttöaste on silloin vain noin $\dfrac{40\,100\,\text{MWh}}{40\,\text{MW} \cdot 8760\,\text{h}} \approx 0{,}11$.

*Päästö.* $m = 11\,\text{g/kWh} \cdot 252 \cdot 10^{6}\,\text{kWh} + 24\,\text{g/kWh} \cdot 88 \cdot 10^{6}\,\text{kWh} + 230\,\text{g/kWh} \cdot 40 \cdot 10^{6}\,\text{kWh} \approx 2{,}8 \cdot 10^{3}\,\text{t} + 2{,}1 \cdot 10^{3}\,\text{t} + 9{,}2 \cdot 10^{3}\,\text{t} \approx 1{,}4 \cdot 10^{4}\,\text{t}$ vuodessa. Se on noin $95\,\%$ vähemmän kuin kivihiilellä ($3{,}1 \cdot 10^{5}\,\text{t}$). Se on myös selvästi vähemmän kuin pelkällä maakaasulla ($1{,}9 \cdot 10^{5}\,\text{t}$). Pelkkä tuulivoima ($4{,}2 \cdot 10^{3}\,\text{t}$) olisi vähäpäästöisempi, mutta se ei kata huippua.

*Huippu.* Tyynenä pakkasiltana biomassavoimala ($40\,\text{MW}$), vesivoima ($20\,\text{MW}$) ja tuulivoimalat (alle $0{,}05 \cdot 90\,\text{MW} \approx 4{,}5\,\text{MW}$) antavat yhteensä noin $65\,\text{MW}$. Loput noin $15\,\text{MW}$ ostetaan verkosta. Toinen tapa on siirtää osa kulutuksesta, esimerkiksi sähkölämmitys, muutamaksi tunniksi myöhemmäksi.

*Muut perusteet.* Yhdistelmä ei ole yhden polttoaineen tai yhden sään varassa. Tuulivoimalla ei ole polttoainetta, ja vesi- ja biomassavoiman tehoa voi säätää. Tuulivoimalat vievät maata ja muuttavat maisemaa. Biomassavoimala tarvitsee haketta, mutta vain noin kuudesosan siitä, mitä se tarvitsisi täydellä käyttöasteella.

*Vahvin vastaperuste* on seuraava. Biomassavoimala seisoo suuren osan vuodesta. Siksi sen rakentaminen on kallista tuotettua energiaa kohti. Lisäksi biomassan polton hiilidioksidi sitoutuu takaisin vasta vuosikymmenten kuluessa. Siksi todellinen päästö voi olla suurempi kuin laskennan oletus $230\,\text{g/kWh}$. Vastaan, että juuri tehon säädön takia voimalaa tarvitaan. Ilman sitä huippuiltana tarvittaisiin verkosta yli $50\,\text{MW}$, ja koko maan kulutus on silloin suurimmillaan. Biomassan osuus energiasta on vain noin $11\,\%$.

*Oletukset.* Oletin, että käyttöasteet ovat joka vuosi samat. Tuulisuus ja sademäärä vaihtelevat. Huonona vuonna biomassavoimala käy enemmän ja päästö kasvaa. Oletin myös, että kulutus pysyy $380\,\text{GWh}$:ssa. Jos lämmitys ja liikenne sähköistyvät, kulutus kasvaa. Silloin tuulivoimaloita tarvitaan lisää. Hinta ja sähköverkon vahvistaminen jäivät laskematta. Ne voivat kuitenkin ratkaista päätöksen.

### Hyväksytään myös
Mikä tahansa tuotantotapa tai yhdistelmä saa täydet pisteet, kun nämä täyttyvät. Suositus kattaa vuoden energian. Suositus kattaa talven huipun tai arvioi puuttuvan tehon ja sen hoitamisen. Päästö on laskettu oikein. Rajoitukset on käsitelty. Vastaperuste ja oletukset on esitetty. Esimerkiksi:
- *Pieni ydinvoimala.* Se tuottaa $0{,}90 \cdot 60\,\text{MW} \cdot 8760\,\text{h} \approx 473\,\text{GWh}$ vuodessa. Se on enemmän kuin kaupunki tarvitsee. Koko kulutuksen päästö olisi vain $12\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} \approx 4{,}6 \cdot 10^{3}\,\text{t}$. Perustelussa on käsiteltävä kolme asiaa. Voimalaa ei vielä ole saatavilla, ja rakentaminen kestää yli kymmenen vuotta (mitä kaupunki tekee sillä välin). Huipusta puuttuu $20\,\text{MW}$. Käytetty polttoaine on loppusijoitettava.
- *Tuulivoima ja maakaasuvoimala varavoimana.* Kun kaasuvoimala käy vain tyynillä jaksoilla, päästö jää pieneksi. Perustelussa arvioidaan, kuinka suuri osa energiasta tuotetaan kaasulla. Sen päästö lasketaan.
- *Kaksi biomassavoimalaa.* Ne kattavat huipun $80\,\text{MW}$. Ne kattavat vuoden energian käyttöasteella $\dfrac{380\,000\,\text{MWh}}{80\,\text{MW} \cdot 8760\,\text{h}} \approx 0{,}54$. Päästö $230\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} \approx 8{,}7 \cdot 10^{4}\,\text{t}$ on noin $72\,\%$ pienempi kuin kivihiilellä. Perustelussa käsitellään hakkeen saatavuus, kuljetukset ja hiilen hidas sitoutuminen. Siinä todetaan myös, että kerroin $230\,\text{g/kWh}$ on laskennan oletus ja metsähakkeen todellinen kerroin voi olla toinen.
- *Tuulivoima ja sähkön osto verkosta huippujen aikana.* Perustelussa todetaan, että kaupunki on riippuvainen verkosta kylmimpinä päivinä, ja riippuvuutta arvioidaan.

Pisteitä ei anneta valitusta tuotantotavasta. Pisteet annetaan siitä, miten valinta on perusteltu.

### Yleisiä virheitä
- a-kohdassa energia lasketaan nimellisteholla ilman käyttöastetta: $5{,}0\,\text{MW} \cdot 8760\,\text{h} = 43{,}8\,\text{GWh}$. Silloin voimaloita näyttää tarvittavan vain $9$.
- a-kohdassa $27{,}1$ pyöristetään alaspäin $27$:ään. Silloin sähköä jää puuttumaan.
- b-kohdassa gigawattitunteja ei muunneta kilowattitunneiksi. Toinen virhe on, että grammat jäävät muuntamatta tonneiksi.
- c-kohdassa päätellään keskitehosta, että tuulivoima riittää talvella aina. Silloin energia ja teho sekoitetaan. Huipputeho ja tyynet jaksot ratkaisevat.
- Tuulivoimaa, aurinkovoimaa tai ydinvoimaa kutsutaan päästöttömäksi. Niidenkin elinkaaren päästökerroin on kuitenkin $11\text{–}48\,\text{g/kWh}$.
- Ydinvoimaa pidetään täysin säätämättömänä tai vesivoimaa rajattomana. Ydinvoimalan tehoa voi kuitenkin laskea, ja vesivoiman energia riippuu sateista.
- e-kohdassa esitetään vain mielipide ilman laskelmaa. Toinen virhe on, että talven huippu jätetään käsittelemättä.

## fy2-s2

Opiskelija valitsee itse kysymyksen ja lähteet. Siksi vastaukset ovat erilaisia. Alla on mallivastauksen rakenne ja yksi esimerkki. Esimerkin kysymys on tuulivoiman kasvihuonekaasupäästö tuotettua sähköä kohti. Lähde 1 on todellinen. Se on IPCC:n viidennen arviointiraportin (AR5, 2014) työryhmän III liite III. Sen elinkaaripäästöjen mediaania käytetään myös tehtävässä fy2-s1. Mediaani on keskimmäinen arvo, kun tutkimusten tulokset laitetaan suuruusjärjestykseen. Lähde 2 on keksitty. Se on esimerkki tavallisesta julkaisutyypistä, energiayhtiön verkkosivusta. Sitä ei ole olemassa.

### a)
**Kysytty:** kysymys, kahden lähteen lähdemerkinnät sekä kummankin tekijä, julkaisija ja tarkoitus
**Periaate:** Lähdemerkinnän avulla lukija löytää julkaisun itse. Tekijä ja julkaisija kertovat, kuka luvusta vastaa. Tarkoitus kertoo, miksi julkaisu on tehty. Tarkoitus ei tee luvusta väärää. Tarkoitus voi kuitenkin vaikuttaa siihen, mitkä luvut julkaisu valitsee ja miten se ne esittää. Siksi lähdettä ei hylätä julkaisijan takia. Sen sijaan tarkoitus otetaan huomioon, kun lukua tulkitaan.
**Mallivastaus:** *Rakenne.* Kirjoita kysymys yhdellä virkkeellä. Kirjoita kummastakin lähteestä nämä: lähdemerkintä, tekijä tai julkaisija, julkaisutyyppi ja tarkoitus. Kirjoita lisäksi yksi tai kaksi virkettä siitä, miten tarkoitus voi näkyä luvuissa.

*Esimerkki.* Kysymykseni on, kuinka suuri on tuulivoiman kasvihuonekaasupäästö tuotettua sähköä kohti.

Lähdemerkinnät:

- Lähde 1: Schlömer, S. ym. (2014). Annex III: Technology-specific cost and performance parameters. Teoksessa *Climate Change 2014: Mitigation of Climate Change. Contribution of Working Group III to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change*. Cambridge University Press. Luettu (lukupäivä).
- Lähde 2 (keksitty esimerkki): Esimerkkienergia Oy. Tuulivoima – puhdasta sähköä. Verkkosivu, päivitetty (vuosi). (verkko-osoite). Luettu (lukupäivä).

Lähde 1 on hallitustenvälisen ilmastopaneelin IPCC:n arviointiraportin liite. Siihen on koottu tuotantotapojen päästöjä monista tutkimuksista. Sen tekijät ovat tutkijoita. Sen tarkoitus on koota tutkimustieto päätöksenteon pohjaksi. Raportti esittää vaihteluvälin ja mediaanin. Se ei suosittele mitään tuotantotapaa.

Lähde 2 on energiayhtiön verkkosivu. Sillä yhtiö esittelee tuulipuistojaan. Sivun tarkoitus on kertoa asiakkaille yhtiön tuotannosta ja markkinoida sitä. Siksi sivu kertoo tuulivoiman eduista. Se ei välttämättä kerro, miten luku on laskettu.

### b)
**Kysytty:** lähteiden julkaisuaika, aineiston ajanjakso sekä luvut suureineen ja yksiköineen samassa yksikössä
**Periaate:** Julkaisuaika ja aineiston ajanjakso ovat eri asioita. Uusi julkaisu voi käyttää vanhaa aineistoa. Tuotantotavat ja niiden laitteet muuttuvat. Siksi eri vuosien luvut voivat erota toisistaan. Lukuja voi verrata vain, kun ne ovat samaa suuretta ja samassa yksikössä. Päästökertoimen yksikkö muunnetaan näin: muunnetaan sekä massan etuliite että energian etuliite.
**Mallivastaus:** *Rakenne.* Kirjoita kummastakin lähteestä julkaisuvuosi ja aineiston vuodet. Kirjoita luku, sen suure ja yksikkö. Muunna luku tarvittaessa samaan yksikköön.

*Esimerkki.* Lähde 1 on julkaistu vuonna 2014. Se kokoaa tutkimuksia, jotka on julkaistu ennen sitä. Lähde 2 on päivitetty viime vuonna. Se ei kuitenkaan kerro, miltä vuodelta luku on. Lähteen 1 mukaan maatuulivoiman elinkaaren kasvihuonekaasupäästöjen mediaani on $11\,\tfrac{\text{g}}{\text{kWh}}$ hiilidioksidiekvivalenttina. Kasvihuonekaasuja on monia, esimerkiksi hiilidioksidi ja metaani. Hiilidioksidiekvivalentti tarkoittaa, että kaikkien kasvihuonekaasujen yhteisvaikutus on muunnettu hiilidioksidin määräksi. Lähde 2 sanoo, että tuulivoima tuottaa sähköä ilman hiilidioksidipäästöjä. Sen luku on siis $0\,\tfrac{\text{g}}{\text{kWh}}$. Luku koskee vain hiilidioksidia. Toinen lähde voisi ilmoittaa päästön yksikössä $\tfrac{\text{t}}{\text{GWh}}$. Silloin muunnos olisi $11\,\tfrac{\text{g}}{\text{kWh}} = \tfrac{11 \cdot 10^{-6}\,\text{t}}{10^{-6}\,\text{GWh}} = 11\,\tfrac{\text{t}}{\text{GWh}}$. Luku pysyy siis samana.

### c)
**Kysytty:** kummankin lähteen tarkasteluraja, oletukset ja epävarmuus
**Periaate:** Tarkasteluraja kertoo, mitä luku sisältää. Sähkö on vain osa kaikesta energiasta. Energiaa käytetään myös lämmitykseen, liikenteeseen ja teollisuuteen. Käytönaikaiset päästöt syntyvät silloin, kun voimala tuottaa energiaa. Elinkaaren päästöihin lasketaan lisäksi voimalan rakentaminen, polttoaineen hankinta, huolto ja purkaminen. Siksi tuotantotapa voi aiheuttaa elinkaaren päästöjä, vaikka sillä ei ole käytönaikaisia päästöjä. Oletukset muuttavat lukua. Oletus voi koskea esimerkiksi voimalan tyyppiä, aluetta tai käyttöastetta. Epävarmuus näkyy vaihteluvälinä. Vaihteluväli kertoo pienimmän ja suurimman arvon.
**Mallivastaus:** *Rakenne.* Kirjoita kummastakin lähteestä nämä asiat. Koskeeko luku sähköä vai kaikkea energiaa? Onko päästö käytönaikainen vai elinkaaren päästö? Muussa kysymyksessä kerro vastaava rajaus. Kerro tärkeimmät oletukset ja epävarmuus. Jos lähde ei kerro jotakin, totea se.

*Esimerkki.* Molemmat lähteet koskevat sähköä. Lähde 1 laskee elinkaaren päästöt. Siinä ovat siis mukana voimaloiden valmistus, rakentaminen ja purkaminen. Lähde 2 tarkoittaa käytönaikaisia päästöjä. Pyörivä tuulivoimala ei polta mitään. Lähde 1 olettaa voimaloiden käyttöasteet ja käyttöiät. Ne on saatu sen tutkimuksista. Tulos riippuu niistä. Kun käyttöikä on pidempi, rakentamisen päästöt jakautuvat suuremmalle energiamäärälle. Lähde 1 ilmoittaa mediaanin lisäksi tutkimusten vaihteluvälin. Maatuulivoimalle se on $7\text{–}56\,\tfrac{\text{g}}{\text{kWh}}$. Siksi sen epävarmuus näkyy. Lähde 2 ei kerro epävarmuutta. Käytönaikainen päästö on kuitenkin nolla jo määritelmän mukaan.

### d)
**Kysytty:** lähteiden vertailukelpoisuus ja perusteltu johtopäätös
**Periaate:** Luvut ovat vertailukelpoisia, kun nämä ehdot täyttyvät. Luvut ovat samaa suuretta samassa yksikössä. Ne ovat samalta ajanjaksolta. Toinen mahdollisuus on, että asia ei ole ehtinyt muuttua ajanjaksojen välillä. Luvuilla on sama tarkasteluraja ja samat tärkeät oletukset. Jos jokin näistä eroaa, se voi selittää lukujen eron. Johtopäätöksessä erotetaan kaksi asiaa: mitä lähteet sanovat ja mitä niistä voi päätellä.
**Mallivastaus:** *Rakenne.* Arvioi vertailukelpoisuus kohta kohdalta. Selitä lukujen ero. Kirjoita johtopäätös, joka vastaa kysymykseen. Toinen mahdollisuus on perustella, miksi lähteet eivät riitä vastaukseen.

*Esimerkki.* Luvut ovat samassa yksikössä. Molemmat koskevat sähköä. Suure on lähes sama. Lähde 1 laskee kaikki kasvihuonekaasut hiilidioksidiekvivalenttina. Lähde 2 laskee vain hiilidioksidin. Luvut eivät silti ole suoraan vertailukelpoisia, koska tarkasteluraja on eri. Lähde 1 antaa elinkaaren päästön. Lähde 2 antaa käytönaikaisen päästön. Tämä selittää eron $11\,\tfrac{\text{g}}{\text{kWh}}$ ja $0\,\tfrac{\text{g}}{\text{kWh}}$. Kumpikaan lähde ei ole väärässä. Johtopäätökseni on tämä. Tuulivoimalla ei ole käytönaikaisia hiilidioksidipäästöjä. Sen elinkaaren kasvihuonekaasupäästö on lähteen 1 mukaan noin $11\,\tfrac{\text{g}}{\text{kWh}}$ hiilidioksidiekvivalenttina. Kun vertailen tuotantotapoja, käytän elinkaaren päästöjä. Niissä kaikki tuotantotavat lasketaan samalla rajauksella. Väite, että tuulivoima on päästötöntä, pitää paikkansa vain käytön aikana.

Toinen yhtä hyvä johtopäätös olisi esimerkiksi tämä. Lähteet eivät ole vertailukelpoisia. Syy on se, että lähde 2 ei kerro rajaustaan eikä vuottaan. Vastaukseen tarvitaan lähde, joka ilmoittaa elinkaaren päästön samalla rajauksella kuin lähde 1.

### Hyväksytään myös
- Mikä tahansa energiantuotannon kysymys, johon vastataan luvulla. Lähteiksi käyvät mitkä tahansa kaksi julkaisua, joilla on eri julkaisija. Pisteet tulevat arvioinnista. Ne eivät tule lähteiden valinnasta.
- Perusteltu johtopäätös, että lukuja ei voi verrata. Syy voi olla esimerkiksi se, että toinen luku koskee sähköä ja toinen kaikkea energiaa. Syy voi olla myös se, että aineistot ovat eri vuosikymmeniltä. Silloin d-kohdassa kerrotaan, millainen lähde tarvittaisiin vertailuun.
- Johtopäätös, että lähteet ovat vertailukelpoisia ja tukevat toisiaan. Johtopäätös on perusteltu kohta kohdalta.
- Eri johtopäätökset samoista lähteistä. Johtopäätökset on perusteltu lähteiden tiedoilla. Ne eivät väitä enempää kuin lähteet tukevat.

### Yleisiä virheitä
- Lähteenä on hakukoneen tulossivu, tekoälyn vastaus tai sivuston etusivu, josta lukua ei löydy. Lähdemerkinnästä puuttuu julkaisija, vuosi tai lukupäivä.
- Lähteillä on sama julkaisija. Esimerkiksi lähteet ovat saman yhtiön kaksi sivua. Toinen esimerkki on uutinen, joka vain toistaa toisen lähteen luvun.
- Lähde hylätään vain julkaisijan takia, esimerkiksi koska se on yrityksen sivu. Sen luku voi kuitenkin pitää paikkansa omalla rajauksellaan.
- Julkaisuaika ja aineiston ajanjakso sekoitetaan.
- Lukuja verrataan eri yksiköissä. Toinen virhe on, että muunnoksessa muunnetaan vain massan etuliite tai vain energian etuliite.
- Sähköä ja kaikkea energiaa verrataan keskenään. Tai käytönaikaisia ja elinkaaren päästöjä verrataan keskenään. Rajauksen eroa ei huomata.
- Johtopäätös valitsee toisen lähteen oikeaksi ilman perusteluja. Toinen virhe on, että johtopäätös väittää enemmän kuin lähteissä sanotaan.
