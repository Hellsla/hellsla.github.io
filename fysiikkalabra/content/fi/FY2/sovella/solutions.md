## fy2-s1

### a)
**Annettu:** tuulivoimalan nimellisteho $P_\text{n} = 5{,}0\,\text{MW}$, käyttöaste $k = 0{,}32$, vuoden pituus $t = 8760\,\text{h}$ ja kaupungin vuosikulutus $E = 380\,\text{GWh}$
**Kysytty:** tarvittavien tuulivoimaloiden määrä $N$
**Periaate:** Tuulivoimala ei käy koko vuotta nimellisteholla, koska tuuli vaihtelee. Käyttöaste kertoo vuoden keskitehon: $P_\text{keski} = k \cdot P_\text{n}$. Teho vaihtelee, mutta vuoden energia on keskiteho kertaa aika. Kun yhden voimalan vuosienergia tiedetään, voimaloiden määrä on kulutus jaettuna sillä. Määrä on kokonaisluku, ja sen on oltava vähintään laskettu arvo.
**Kaava:** $E_1 = k \cdot P_\text{n} \cdot t$ ja $N = \dfrac{E}{E_1}$
**Muunnokset:** Kun teho on megawatteina ja aika tunteina, energia on megawattitunteina: $1\,\text{GWh} = 1000\,\text{MWh}$.
**Sijoitus:** $E_1 = 0{,}32 \cdot 5{,}0\,\text{MW} \cdot 8760\,\text{h} = 14\,016\,\text{MWh} = 14{,}0\,\text{GWh}$ ja $N = \dfrac{380\,\text{GWh}}{14{,}0\,\text{GWh}} = 27{,}1$
**Vastaus:** Tarvitaan $28$ tuulivoimalaa. Laskettu arvo $27{,}1$ pyöristetään ylöspäin, koska $27$ voimalaa tuottaisi vain $27 \cdot 14{,}0\,\text{GWh} = 378\,\text{GWh}$ eli liian vähän. Määrä on kokonaisluku, joten merkitsevien numeroiden sääntö ei sitä rajoita.
**Järkevyys:** Kaupungin keskiteho on $\dfrac{380\,000\,\text{MWh}}{8760\,\text{h}} \approx 43\,\text{MW}$. Voimaloiden yhteinen nimellisteho on $28 \cdot 5{,}0\,\text{MW} = 140\,\text{MW}$, noin kolminkertainen, mikä sopii käyttöasteeseen $0{,}32 \approx \tfrac{1}{3}$.

### b)
**Annettu:** vuosikulutus $E = 380\,\text{GWh}$ ja elinkaaren päästökertoimet: kivihiili $e = 820\,\text{g/kWh}$, maakaasu $490\,\text{g/kWh}$ ja tuulivoima maalla $11\,\text{g/kWh}$
**Kysytty:** vuotuinen päästö $m$ kullakin tavalla ja päästön pieneneminen prosentteina kivihiileen verrattuna
**Periaate:** Päästökerroin kertoo, montako grammaa hiilidioksidiekvivalenttia syntyy kilowattituntia kohti, kun mukaan lasketaan koko elinkaari. Kun kaikki kilowattitunnit tuotetaan samalla tavalla, päästö on suoraan verrannollinen energiaan. Prosentuaalinen pieneneminen on päästöjen erotus suhteessa kivihiilen päästöön. Energia on kaikissa vaihtoehdoissa sama, joten se supistuu, ja suhteen voi laskea suoraan päästökertoimista.
**Kaava:** $m = e \cdot E$ ja pieneneminen $\dfrac{m_\text{hiili} - m}{m_\text{hiili}} = 1 - \dfrac{e}{e_\text{hiili}}$
**Muunnokset:** $E = 380\,\text{GWh} = 380 \cdot 10^{6}\,\text{kWh}$, koska kerroin on yksikössä $\text{g/kWh}$. Lopuksi $1\,\text{t} = 10^{6}\,\text{g}$.
**Sijoitus:** Kivihiili: $m = 820\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} = 3{,}116 \cdot 10^{11}\,\text{g} = 3{,}116 \cdot 10^{5}\,\text{t}$. Maakaasu: $m = 490\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} = 1{,}862 \cdot 10^{11}\,\text{g} = 1{,}862 \cdot 10^{5}\,\text{t}$. Tuulivoima: $m = 11\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} = 4{,}18 \cdot 10^{9}\,\text{g} = 4{,}18 \cdot 10^{3}\,\text{t}$. Pieneneminen: maakaasu $1 - \dfrac{490\,\text{g/kWh}}{820\,\text{g/kWh}} = 0{,}40$ ja tuulivoima $1 - \dfrac{11\,\text{g/kWh}}{820\,\text{g/kWh}} = 0{,}99$
**Vastaus:** Kivihiilellä $m \approx 3{,}1 \cdot 10^{5}\,\text{t}$, maakaasulla $1{,}9 \cdot 10^{5}\,\text{t}$ ja tuulivoimalla $4{,}2 \cdot 10^{3}\,\text{t}$ vuodessa, kahden merkitsevän numeron tarkkuudella kuten päästökertoimissa. Maakaasu pienentää päästöä noin $40\,\%$, tuulivoima noin $99\,\%$.
**Järkevyys:** Kivihiilellä syntyy vajaa kilogramma kilowattituntia kohti, ja kilowattitunteja on satoja miljoonia, joten satoja tuhansia tonneja on oikea suuruusluokka. Prosentit täsmäävät tonneista laskettuihin: maakaasulla jää $\dfrac{1{,}862 \cdot 10^{5}\,\text{t}}{3{,}116 \cdot 10^{5}\,\text{t}} \approx 0{,}60$ kivihiilen päästöstä eli pieneneminen on $40\,\%$. Tuulivoimankaan päästö ei ole nolla, koska voimaloiden valmistus ja rakentaminen aiheuttavat päästöjä.

### c)
**Annettu:** $N = 28$ tuulivoimalaa, yhden vuosienergia $E_1 = 14{,}0\,\text{GWh}$, talven osuus tuulivoiman vuosienergiasta $32\,\%$ ja kaupungin vuosikulutuksesta $31\,\%$, kulutus $E = 380\,\text{GWh}$, talven pituus $90\,\text{d}$, huipputeho $80\,\text{MW}$ ja tyynen jakson teho alle $5\,\%$ nimellistehosta
**Kysytty:** tuulivoimaloiden keskiteho $P_\text{t}$ joulu–helmikuussa ja riittääkö se kaupungin tarpeeseen
**Periaate:** Taulukosta saadaan, kuinka suuri osa vuoden energiasta tuotetaan ja kulutetaan talvella. Talven keskiteho on talven energia jaettuna talven tunneilla. Keskiteho kertoo vain, riittääkö energia keskimäärin: kulutus ja tuuli vaihtelevat talvenkin aikana, joten tarvetta on verrattava myös huipputehoon ja tyynen jakson tehoon.
**Kaava:** $P_\text{t} = \dfrac{0{,}32 \cdot N E_1}{t}$ ja kaupungin talven keskiteho $P_\text{k} = \dfrac{0{,}31 \cdot E}{t}$
**Muunnokset:** $t = 90 \cdot 24\,\text{h} = 2160\,\text{h}$ ja $1\,\text{GWh} = 1000\,\text{MWh}$
**Sijoitus:** $N E_1 = 28 \cdot 14{,}016\,\text{GWh} = 392{,}4\,\text{GWh}$. $P_\text{t} = \dfrac{0{,}32 \cdot 392{,}4\,\text{GWh}}{2160\,\text{h}} = \dfrac{125\,600\,\text{MWh}}{2160\,\text{h}} = 58{,}1\,\text{MW}$ ja $P_\text{k} = \dfrac{0{,}31 \cdot 380\,\text{GWh}}{2160\,\text{h}} = \dfrac{117\,800\,\text{MWh}}{2160\,\text{h}} = 54{,}5\,\text{MW}$. Tyynellä jaksolla teho on alle $0{,}05 \cdot 28 \cdot 5{,}0\,\text{MW} = 7\,\text{MW}$.
**Vastaus:** Tuulivoimaloiden keskiteho talvella on $P_\text{t} \approx 58\,\text{MW}$, kahden merkitsevän numeron tarkkuudella kuten taulukon prosenttiosuuksissa. Se on hieman suurempi kuin kaupungin talven keskimääräinen tarve $55\,\text{MW}$, joten talven energia riittää keskimäärin. Tyynenä pakkasiltana tuulivoimaloista saa kuitenkin vain noin $7\,\text{MW}$, kun tarve on $80\,\text{MW}$. Silloin noin $73\,\text{MW}$ on saatava muualta.
**Järkevyys:** Talvi on neljännes vuodesta, ja sille osuu noin kolmannes sekä tuotannosta että kulutuksesta, joten talven keskitehot ovat vuoden keskitehoja ($45\,\text{MW}$ ja $43\,\text{MW}$) suurempia, kuten kuuluukin. Kumpikin keskiteho on huipputehoa $80\,\text{MW}$ pienempi, kuten keskiarvon pitääkin olla.

### d)
**Kysytty:** kuinka paljon aurinkopuistot auttavat huippuiltana, ja mitkä tuotantotavat voisivat tuottaa tehoa tyynenä pakkasiltana rajoituksineen
**Periaate:** Vuoden energia ei kerro, onko tehoa saatavilla juuri silloin, kun sitä tarvitaan. Huippuiltana ratkaisee teho sillä hetkellä. Sen voivat tuottaa voimalat, joiden tehoa voi säätää tai jotka käyvät tasaisesti säästä riippumatta. Säädettävyys ja sääriippuvuus ovat ominaisuuksia, joilla on rajansa, eivät ehdottomia luokkia.
**Mallivastaus:** Yhden aurinkopuiston vuosienergia on $0{,}11 \cdot 10\,\text{MW} \cdot 8760\,\text{h} \approx 9{,}6\,\text{GWh}$, joten $40$ puistoa tuottaa noin $385\,\text{GWh}$ vuodessa. Talvella siitä tulee taulukon mukaan vain $4\,\%$ eli noin $15\,\text{GWh}$, mikä vastaa keskitehoa $\dfrac{15\,400\,\text{MWh}}{2160\,\text{h}} \approx 7\,\text{MW}$. Tammikuun iltana on pimeää, joten teho huipun aikaan on nolla. Aurinkosähkö tuotetaan pääosin kesällä, jolloin kulutus on pienimmillään.

Tyynenä pakkasiltana tehoa voisivat tuottaa
- *maakaasuvoimala* ($50\,\text{MW}$): tehoa voi nostaa nopeasti, mutta kaasu on tuontipolttoainetta ja päästökerroin on uusista vaihtoehdoista suurin
- *biomassavoimala* ($40\,\text{MW}$): säädettävä, mutta käynnistyy hitaammin, ja polttoainetta on kuljetettava ja varastoitava
- *vesivoimaosuus* ($20\,\text{MW}$): tehoa voi säätää nopeasti, mutta vuoden energia riippuu sateista, joten vettä ei voi käyttää rajattomasti
- *pieni ydinvoimala* ($60\,\text{MW}$): käy tasaisesti säästä riippumatta ja on siksi käynnissä myös huippuiltana, mutta tehoa ei voi nostaa nimellistehoa suuremmaksi, eikä voimalaa ole vielä saatavilla
- *verkosta ostettu sähkö*: käytettävissä, kun muualla on tuotantoa vapaana, mutta koko Suomen kulutus on suurimmillaan samoina pakkasiltoina.

### e)
**Kysytty:** perusteltu suositus kaupungin sähköntuotannoksi laskelmineen, vastaperusteineen ja oletuksineen
**Periaate:** Hyvä suositus kattaa kaksi eri vaatimusta: vuoden energian (a- ja b-kohtien laskut) ja talven huipputehon (c- ja d-kohdat). Päästö lasketaan jokaiselle tuotantotavalle erikseen kaavalla $m = e \cdot E$ ja lasketaan yhteen. Valinta on arvovalinta, jossa päästöjen lisäksi painavat säädettävyys, polttoaine, maankäyttö, jäte ja aikataulu. Siksi yhtä oikeaa tuotantotapaa ei ole, vaan vastaus arvioidaan perustelujen perusteella. Alla on yksi mahdollinen suositus.
**Mallivastaus:** Suosittelen yhdistelmää: $18$ tuulivoimalaa, kaupungin osuus vesivoimalasta ja yksi biomassavoimala, joka käy pääasiassa silloin, kun tuuli ei riitä.

*Energia.* Tuulivoimalat tuottavat $18 \cdot 14{,}0\,\text{GWh} \approx 252\,\text{GWh}$ ja vesivoimaosuus $0{,}50 \cdot 20\,\text{MW} \cdot 8760\,\text{h} \approx 88\,\text{GWh}$ vuodessa. Loput $380\,\text{GWh} - 252\,\text{GWh} - 88\,\text{GWh} \approx 40\,\text{GWh}$ tuottaa biomassavoimala, jonka käyttöaste on silloin vain noin $\dfrac{40\,100\,\text{MWh}}{40\,\text{MW} \cdot 8760\,\text{h}} \approx 0{,}11$.

*Päästö.* $m = 11\,\text{g/kWh} \cdot 252 \cdot 10^{6}\,\text{kWh} + 24\,\text{g/kWh} \cdot 88 \cdot 10^{6}\,\text{kWh} + 230\,\text{g/kWh} \cdot 40 \cdot 10^{6}\,\text{kWh} \approx 2{,}8 \cdot 10^{3}\,\text{t} + 2{,}1 \cdot 10^{3}\,\text{t} + 9{,}2 \cdot 10^{3}\,\text{t} \approx 1{,}4 \cdot 10^{4}\,\text{t}$ vuodessa. Se on noin $95\,\%$ vähemmän kuin kivihiilellä ($3{,}1 \cdot 10^{5}\,\text{t}$) ja selvästi vähemmän kuin pelkällä maakaasulla ($1{,}9 \cdot 10^{5}\,\text{t}$). Pelkkä tuulivoima ($4{,}2 \cdot 10^{3}\,\text{t}$) olisi vähäpäästöisempi, mutta se ei kata huippua.

*Huippu.* Tyynenä pakkasiltana biomassavoimala ($40\,\text{MW}$), vesivoima ($20\,\text{MW}$) ja tuulivoimalat (alle $0{,}05 \cdot 90\,\text{MW} \approx 4{,}5\,\text{MW}$) antavat yhteensä noin $65\,\text{MW}$. Loput noin $15\,\text{MW}$ ostetaan verkosta, tai osa kulutuksesta, kuten sähkölämmitys, siirretään muutamaksi tunniksi myöhemmäksi.

*Muut perusteet.* Yhdistelmä ei ole yhden polttoaineen tai yhden sään varassa: tuulivoimalla ei ole polttoainetta, ja vesi- ja biomassavoiman tehoa voi säätää. Tuulivoimalat vievät maata ja muuttavat maisemaa. Biomassavoimala tarvitsee haketta, mutta vain noin kuudesosan siitä, mitä se tarvitsisi täydellä käyttöasteella.

*Vahvin vastaperuste* on, että biomassavoimala seisoo suuren osan vuodesta, joten sen rakentaminen on kallista tuotettua energiaa kohti, ja biomassan polton hiilidioksidi sitoutuu takaisin vasta vuosikymmenten kuluessa. Vastaan, että juuri säädettävyyden takia voimalaa tarvitaan: ilman sitä huippuiltana tarvittaisiin verkosta yli $50\,\text{MW}$, ja koko maan kulutus on silloin suurimmillaan. Biomassan osuus energiasta on vain noin $11\,\%$.

*Oletukset.* Oletin, että käyttöasteet ovat joka vuosi samat. Tuulisuus ja sademäärä vaihtelevat, joten huonona vuonna biomassavoimala käy enemmän ja päästö kasvaa. Oletin myös, että kulutus pysyy $380\,\text{GWh}$:ssa. Jos lämmitys ja liikenne sähköistyvät, kulutus kasvaa ja tuulivoimaloita tarvitaan lisää. Hinta ja sähköverkon vahvistaminen jäivät laskematta, vaikka ne voivat ratkaista päätöksen.

### Hyväksytään myös
Mikä tahansa tuotantotapa tai yhdistelmä saa täydet pisteet, kun suositus kattaa vuoden energian ja kattaa talven huipun tai arvioi puuttuvan tehon ja sen hoitamisen, päästö on laskettu oikein, rajoitukset on käsitelty ja vastaperuste ja oletukset on esitetty. Esimerkiksi:
- *Pieni ydinvoimala.* Se tuottaa $0{,}90 \cdot 60\,\text{MW} \cdot 8760\,\text{h} \approx 473\,\text{GWh}$ vuodessa eli enemmän kuin kaupunki tarvitsee, ja koko kulutuksen päästö olisi vain $12\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} \approx 4{,}6 \cdot 10^{3}\,\text{t}$. Perustelussa on käsiteltävä, että voimalaa ei vielä ole saatavilla ja rakentaminen kestää yli kymmenen vuotta (mitä kaupunki tekee sillä välin), että huipusta puuttuu $20\,\text{MW}$ ja että käytetty polttoaine on loppusijoitettava.
- *Tuulivoima ja maakaasuvoimala varavoimana.* Kun kaasuvoimala käy vain tyynillä jaksoilla, päästö jää pieneksi. Perustelussa arvioidaan, kuinka suuri osa energiasta tuotetaan kaasulla, ja lasketaan sen päästö.
- *Kaksi biomassavoimalaa.* Ne kattavat huipun $80\,\text{MW}$ ja vuoden energian käyttöasteella $\dfrac{380\,000\,\text{MWh}}{80\,\text{MW} \cdot 8760\,\text{h}} \approx 0{,}54$. Päästö $230\,\text{g/kWh} \cdot 380 \cdot 10^{6}\,\text{kWh} \approx 8{,}7 \cdot 10^{4}\,\text{t}$ on noin $72\,\%$ pienempi kuin kivihiilellä. Perustelussa käsitellään hakkeen saatavuus, kuljetukset ja hiilen hidas sitoutuminen.
- *Tuulivoima ja sähkön osto verkosta huippujen aikana*, kun riippuvuus verkosta kylmimpinä päivinä todetaan ja sitä arvioidaan.

Pisteitä ei anneta valitusta tuotantotavasta vaan siitä, miten valinta on perusteltu.

### Yleisiä virheitä
- a-kohdassa energia lasketaan nimellisteholla ilman käyttöastetta: $5{,}0\,\text{MW} \cdot 8760\,\text{h} = 43{,}8\,\text{GWh}$, jolloin voimaloita näyttää tarvittavan vain $9$.
- a-kohdassa $27{,}1$ pyöristetään alaspäin $27$:ään, jolloin sähköä jää puuttumaan.
- b-kohdassa gigawattitunteja ei muunneta kilowattitunneiksi, tai grammat jäävät muuntamatta tonneiksi.
- c-kohdassa päätellään keskitehosta, että tuulivoima riittää talvella aina, vaikka huipputeho ja tyynet jaksot ratkaisevat. Energia ja teho sekoitetaan.
- Tuulivoimaa, aurinkovoimaa tai ydinvoimaa kutsutaan päästöttömäksi, vaikka niidenkin elinkaaren päästökerroin on $11\text{–}48\,\text{g/kWh}$.
- Ydinvoimaa pidetään täysin säätämättömänä tai vesivoimaa rajattomana: ydinvoimalan tehoa voi laskea, ja vesivoiman energia riippuu sateista.
- e-kohdassa esitetään vain mielipide ilman laskelmaa tai jätetään talven huippu käsittelemättä.

## fy2-s2

Lähteet ja kysymys ovat opiskelijan omia, joten vastaukset ovat erilaisia. Alla on mallivastauksen rakenne ja yksi esimerkki. Esimerkin kysymys on tuulivoiman kasvihuonekaasupäästö tuotettua sähköä kohti. Lähde 1 on todellinen: IPCC:n viidennen arviointiraportin (AR5, 2014) työryhmän III liite III, jonka elinkaaripäästöjen mediaania käytetään myös tehtävässä fy2-s1. Lähde 2 on keksitty esimerkki tavallisesta julkaisutyypistä, energiayhtiön verkkosivusta, eikä sitä ole olemassa.

### a)
**Kysytty:** kysymys, kahden lähteen lähdemerkinnät sekä kummankin tekijä, julkaisija ja tarkoitus
**Periaate:** Lähdemerkinnästä lukija löytää julkaisun itse. Tekijä ja julkaisija kertovat, kuka luvusta vastaa, ja tarkoitus kertoo, miksi julkaisu on tehty. Tarkoitus ei tee luvusta väärää, mutta se voi vaikuttaa siihen, mitkä luvut julkaisu valitsee ja miten se ne esittää. Siksi lähdettä ei hylätä julkaisijan takia, vaan sen tarkoitus otetaan huomioon tulkinnassa.
**Mallivastaus:** *Rakenne.* Kysymys yhdellä virkkeellä. Kummastakin lähteestä lähdemerkintä, tekijä tai julkaisija, julkaisutyyppi ja tarkoitus sekä yksi tai kaksi virkettä siitä, miten tarkoitus voi näkyä luvuissa.

*Esimerkki.* Kysymykseni on, kuinka suuri on tuulivoiman kasvihuonekaasupäästö tuotettua sähköä kohti.

Lähdemerkinnät:

- Lähde 1: Schlömer, S. ym. (2014). Annex III: Technology-specific cost and performance parameters. Teoksessa *Climate Change 2014: Mitigation of Climate Change. Contribution of Working Group III to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change*. Cambridge University Press. Luettu (lukupäivä).
- Lähde 2 (keksitty esimerkki): Esimerkkienergia Oy. Tuulivoima – puhdasta sähköä. Verkkosivu, päivitetty (vuosi). (verkko-osoite). Luettu (lukupäivä).

Lähde 1 on hallitustenvälisen ilmastopaneelin IPCC:n arviointiraportin liite, jossa on koottu tuotantotapojen päästöjä monista tutkimuksista. Sen tekijät ovat tutkijoita, ja sen tarkoitus on koota tutkimustieto päätöksenteon pohjaksi. Raportti esittää vaihteluvälin ja mediaanin eikä suosittele mitään tuotantotapaa.

Lähde 2 on energiayhtiön verkkosivu, jolla yhtiö esittelee tuulipuistojaan. Sen tarkoitus on kertoa asiakkaille yhtiön tuotannosta ja markkinoida sitä. Siksi sivu kertoo tuulivoiman eduista eikä välttämättä kerro, miten luku on laskettu.

### b)
**Kysytty:** lähteiden julkaisuaika, aineiston ajanjakso sekä luvut suureineen ja yksiköineen samassa yksikössä
**Periaate:** Julkaisuaika ja aineiston ajanjakso ovat eri asioita: uusi julkaisu voi käyttää vanhaa aineistoa. Tuotantotavat ja niiden laitteet muuttuvat, joten eri vuosien luvut voivat erota jo siksi. Lukuja voi verrata vain, kun ne ovat samaa suuretta ja samassa yksikössä. Päästökertoimen yksiköt muunnetaan toisikseen, kun sekä massan että energian etuliitteet muunnetaan.
**Mallivastaus:** *Rakenne.* Kummastakin lähteestä julkaisuvuosi ja aineiston vuodet, luku suureineen ja yksiköineen ja tarvittaessa muunnos samaan yksikköön.

*Esimerkki.* Lähde 1 on julkaistu vuonna 2014, ja se kokoaa sitä ennen julkaistuja tutkimuksia. Lähde 2 on päivitetty viime vuonna, mutta se ei kerro, miltä vuodelta luku on. Lähde 1 ilmoittaa maatuulivoiman elinkaaren kasvihuonekaasupäästöjen mediaaniksi $11\,\tfrac{\text{g}}{\text{kWh}}$ hiilidioksidiekvivalenttina. Suure on siis kaikkien kasvihuonekaasujen yhteisvaikutus muunnettuna hiilidioksidin määräksi. Lähde 2 sanoo, että tuulivoima tuottaa sähköä ilman hiilidioksidipäästöjä, eli sen luku on $0\,\tfrac{\text{g}}{\text{kWh}}$, ja se koskee vain hiilidioksidia. Jos toinen lähde ilmoittaisi päästön yksikössä $\tfrac{\text{t}}{\text{GWh}}$, muunnos olisi $11\,\tfrac{\text{g}}{\text{kWh}} = \tfrac{11 \cdot 10^{-6}\,\text{t}}{10^{-6}\,\text{GWh}} = 11\,\tfrac{\text{t}}{\text{GWh}}$, eli luku pysyy samana.

### c)
**Kysytty:** kummankin lähteen tarkasteluraja, oletukset ja epävarmuus
**Periaate:** Tarkasteluraja kertoo, mitä luku sisältää. Sähkö on vain osa kaikesta energiasta, sillä energiaa käytetään myös lämmitykseen, liikenteeseen ja teollisuuteen. Käytönaikaiset päästöt syntyvät, kun voimala tuottaa energiaa. Elinkaaren päästöihin lasketaan lisäksi voimalan rakentaminen, polttoaineen hankinta, huolto ja purkaminen. Siksi tuotantotapa, jolla ei ole käytönaikaisia päästöjä, voi silti aiheuttaa elinkaaren päästöjä. Oletukset, kuten laitostyyppi, alue ja käyttöaste, muuttavat lukua, ja epävarmuus näkyy vaihteluvälinä.
**Mallivastaus:** *Rakenne.* Kummastakin lähteestä: sähkö vai kokonaisenergia, käytönaikainen vai elinkaaren päästö (tai muun kysymyksen vastaava rajaus), tärkeimmät oletukset ja epävarmuus. Jos lähde ei kerro jotakin, se todetaan.

*Esimerkki.* Molemmat lähteet koskevat sähköä. Lähde 1 laskee elinkaaren päästöt, eli siinä ovat mukana voimaloiden valmistus, rakentaminen ja purkaminen. Lähde 2 tarkoittaa käytönaikaisia päästöjä: pyörivä tuulivoimala ei polta mitään. Lähde 1 olettaa tutkimuksistaan saadut käyttöasteet ja voimaloiden käyttöiät, ja tulos riippuu niistä: pidempi käyttöikä jakaa rakentamisen päästöt suuremmalle energiamäärälle. Lähde 1 ilmoittaa mediaanin lisäksi tutkimusten vaihteluvälin, maatuulivoimalle $7\text{–}56\,\tfrac{\text{g}}{\text{kWh}}$, joten sen epävarmuus näkyy. Lähde 2 ei kerro epävarmuutta, mutta käytönaikainen päästö on nolla jo määritelmän mukaan.

### d)
**Kysytty:** lähteiden vertailukelpoisuus ja perusteltu johtopäätös
**Periaate:** Luvut ovat vertailukelpoisia, kun ne ovat samaa suuretta samassa yksikössä, samalta ajanjaksolta tai ainakin ajanjaksolta, jolla asia ei ole ehtinyt muuttua, ja samalla tarkastelurajalla ja samoilla keskeisillä oletuksilla. Jos jokin näistä eroaa, ero voi selittää lukujen eron. Johtopäätös erottaa sen, mitä lähteet sanovat, siitä, mitä niistä voi päätellä.
**Mallivastaus:** *Rakenne.* Vertailukelpoisuus kohta kohdalta, lukujen eron selitys ja johtopäätös, joka vastaa kysymykseen tai perustelee, miksi lähteet eivät riitä siihen.

*Esimerkki.* Luvut ovat samassa yksikössä, ja molemmat koskevat sähköä. Suure on lähes sama: lähde 1 laskee kaikki kasvihuonekaasut hiilidioksidiekvivalenttina ja lähde 2 vain hiilidioksidin. Luvut eivät silti ole suoraan vertailukelpoisia, koska tarkasteluraja on eri: lähde 1 antaa elinkaaren päästön ja lähde 2 käytönaikaisen. Ero $11\,\tfrac{\text{g}}{\text{kWh}}$ ja $0\,\tfrac{\text{g}}{\text{kWh}}$ selittyy tällä, eikä kumpikaan lähde ole väärässä. Johtopäätökseni on, että tuulivoimalla ei ole käytönaikaisia hiilidioksidipäästöjä ja että sen elinkaaren kasvihuonekaasupäästö on lähteen 1 mukaan noin $11\,\tfrac{\text{g}}{\text{kWh}}$ hiilidioksidiekvivalenttina. Tuotantotapoja vertaillessa käytän elinkaaren päästöjä, koska niissä kaikki tuotantotavat lasketaan samalla rajauksella. Väite, että tuulivoima on päästötöntä, pitää paikkansa vain käytön aikana.

Toinen yhtä hyvä johtopäätös olisi esimerkiksi tämä: lähteet eivät ole vertailukelpoisia, koska lähde 2 ei kerro rajaustaan eikä vuottaan, ja vastaukseen tarvitaan lähde, joka ilmoittaa elinkaaren päästön samalla rajauksella kuin lähde 1.

### Hyväksytään myös
- Mikä tahansa energiantuotannon kysymys, johon vastataan luvulla, ja mitkä tahansa kaksi julkaisua, joilla on eri julkaisija. Pisteet tulevat arvioinnista, ei lähteiden valinnasta.
- Perusteltu johtopäätös, että luvut eivät ole vertailukelpoisia, esimerkiksi koska toinen koskee sähköä ja toinen kaikkea energiaa tai koska aineistot ovat eri vuosikymmeniltä. Silloin d-kohdassa kerrotaan, millainen lähde tarvittaisiin vertailuun.
- Johtopäätös, että lähteet ovat vertailukelpoisia ja tukevat toisiaan, kun se on perusteltu kohta kohdalta.
- Eri johtopäätökset samoista lähteistä, kun ne on perusteltu lähteiden tiedoilla eivätkä väitä enempää kuin lähteet tukevat.

### Yleisiä virheitä
- Lähteenä on hakukoneen tulossivu, tekoälyn vastaus tai sivuston etusivu, josta lukua ei löydy. Lähdemerkinnästä puuttuu julkaisija, vuosi tai lukupäivä.
- Lähteellä on sama julkaisija, esimerkiksi saman yhtiön kaksi sivua tai uutinen, joka vain toistaa toisen lähteen luvun.
- Lähde hylätään pelkän julkaisijan perusteella, esimerkiksi koska se on yrityksen sivu, vaikka sen luku voi pitää paikkansa omalla rajauksellaan.
- Julkaisuaika ja aineiston ajanjakso sekoitetaan.
- Lukuja verrataan eri yksiköissä, tai muunnoksessa muunnetaan vain massan tai vain energian etuliite.
- Sähköä ja kokonaisenergiaa tai käytönaikaisia ja elinkaaren päästöjä verrataan keskenään huomaamatta rajauksen eroa.
- Johtopäätös valitsee lähteistä toisen oikeaksi perustelematta, tai se väittää lähteiden perusteella enemmän kuin niissä sanotaan.
