# Sähkömagneettisen induktion tutkiminen

> **Tutkimuskysymys:** Miten käämiin indusoituva jännite riippuu valitsemastasi tekijästä, esimerkiksi magneetin nopeudesta tai käämin kierrosluvusta?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydällä on kaksi samankokoista käämiä, sauvamagneetti ja pieni lieriömagneetti. Toisen käämin päät on kytketty johtimilla jänniteanturiin, ja anturi on kytketty kannettavaan tietokoneeseen. Tietokoneen näyttö on tyhjä. Pöydällä on myös viivain ja vihko." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-induktio-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

Kun magneetti liikkuu käämin lähellä, käämin päiden välille syntyy jännite, vaikka piirissä ei ole paristoa eikä virtalähdettä. Samaan ilmiöön perustuvat generaattorit, polkupyörän dynamo ja langaton lataus. Tässä tutkimuksessa valitset yhden tekijän, jonka vaikutusta jännitteeseen tutkit, ja selvität riippuvuuden mittaamalla. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** miten valitsemasi tekijä vaikuttaa jännitepulssiin, joka syntyy, kun magneetti kulkee käämin läpi. Määritä jokaisesta kokeesta pulssin **huippuarvo** $U_\text{max}$ ja ensimmäisen pulssin **pinta-ala** $S$ eli jännitteen ja ajan kuvaajan ja aika-akselin väliin jäävä pinta-ala, ja selvitä, miten kumpikin riippuu tutkimastasi tekijästä.

**Päätät itse (osittain ohjattu ja itsenäinen työtapa):** tutkittavan tekijän ja sen arvot, sen, miten pidät muut tekijät vakioina, toistojen määrän, kuvaajien akselit perusteluineen sekä tavan, jolla arvioit tulosten epävarmuuden. Osittain ohjatussa työtavassa valitset tekijän kahdesta vaihtoehdosta ja sivu antaa tukea, itsenäisessä työtavassa valitset ja perustelet kaiken itse. Ohjatussa työtavassa sivu kiinnittää nämä valinnat.

::: tuki I
**Itsenäinen työtapa.** Laajennus kuuluu työhösi: tutki laajennuksessa jotakin toista tekijää kuin päämittauksessa ja vertaa, miten huippuarvo ja pinta-ala riippuvat kummastakin.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Luonnostele, millainen on käämin jännite ajan funktiona, kun magneetti tulee käämiin, kulkee sen läpi ja jatkaa toiselle puolelle. Onko jännite koko ajan samanmerkkinen?
2. Miten jännitteen huippuarvo muuttuu, kun tutkimasi tekijä kaksinkertaistuu? Ohjatussa työtavassa tekijä on magneetin nopeus.
3. Riippuuko jännitepulssin pinta-ala tutkimastasi tekijästä samalla tavalla kuin huippuarvo?
4. Mikä mittauksessa on todennäköisesti vaikeinta, ja mikä on suurin epävarmuuden lähde?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Magneetin liikkuessa jännite muuttuu koko ajan, joten ”jännitteen suuruus” täytyy ensin muuttaa mitattaviksi luvuiksi. Ennen kuin luet eteenpäin, kirjaa:

1. Miten luet yhden kokeen jännitekuvaajasta huippuarvon $U_\text{max}$ ja pinta-alan $S$, ja millä laitteella jännite kannattaa mitata, jotta lyhyt pulssi näkyy kokonaan?
2. Mitä muutat, mitä mittaat ja mitkä tekijät pidät vakioina?
3. Miten saat tutkimasi tekijän arvon selville luvuksi? Jos tutkit nopeutta, miten saat magneetin kulkemaan käämin läpi joka kerta tunnetulla ja toistettavalla nopeudella?

## Teoriaa lyhyesti

Sähkömagneettista induktiota käsitellään tarkemmin moduulissa FY7, jonka sivut eivät ole vielä valmiina. Tätä tutkimusta varten tarvitset vain seuraavat asiat.

**Magneettivuo** $\Phi$ kuvaa, kuinka paljon magneettikenttää kulkee käämin yhden kierroksen läpi. Kun tasainen magneettikenttä $B$ on kohtisuorassa kierroksen tasoa vastaan, $\Phi = BA$, missä $A$ on kierroksen pinta-ala. Vuon yksikkö on weber, $1\ \text{Wb} = 1\ \text{T} \cdot \text{m}^2$. Kun magneetti lähestyy käämiä, yhä enemmän sen kenttää kulkee kierrosten läpi, joten vuo kasvaa.

<svg data-fig="flux" viewBox="0 0 600 330" role="img" aria-label="Kaaviokuva. Vasemmalla on sauvamagneetti, joka liikkuu nopeudella v oikealle kohti käämiä. Magneetin punaisesta päästä lähtee vihreitä kenttäviivoja, joiden suunta on merkitty nuolenkärjin. Neljä tummempaa kenttäviivaa kulkee käämin kierrosten läpi, vaaleammat kaartuvat käämin ohi takaisin magneetin siniseen päähän. Käämissä on N kierrosta, ja sen päiden välille syntyvä jännite U mitataan jännitemittarilla." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-induktio-flux.webp" x="13.5" y="4.9" width="588.2" height="330.9" preserveAspectRatio="none"/>
  <foreignObject x="417" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="494" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="206" y="97.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="90" y="207.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{magneetti}$</span></div></foreignObject>
  <foreignObject x="323" y="19.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{käämi, } N \text{ kierrosta}$</div></foreignObject>
</svg>

**Induktiolaki:** kun käämin kierrosten läpi kulkeva magneettivuo muuttuu, käämin päiden välille indusoituu jännite

```latex
e = -N\frac{\Delta\Phi}{\Delta t}
```

missä $e$ on indusoitunut jännite, $N$ käämin kierrosluku ja $\dfrac{\Delta\Phi}{\Delta t}$ yhden kierroksen läpi kulkevan vuon muutosnopeus. Jos vuo ei muutu, jännitettä ei synny, vaikka magneetti olisi käämin sisällä. Kun vuo kasvaa, $\Delta\Phi$ on positiivinen, ja kun vuo pienenee, negatiivinen. Siksi jännitteen etumerkki on eri silloin, kun vuo kasvaa, kuin silloin, kun se pienenee. Miinusmerkki kertoo jännitteen suunnan **Lenzin lain** mukaan: indusoitunut jännite pyrkii synnyttämään virran, joka vastustaa vuon muutosta.

Jännitemittarin ja jänniteanturin resistanssi on hyvin suuri, tyypillisesti megaohmeja, eli paljon suurempi kuin käämin resistanssi. Siksi ne ottavat piiristä hyvin pientä virtaa. Silloin mittari näyttää käytännössä indusoituneen jännitteen, ja käämin virta ei juuri jarruta magneettia.

::: tuki O OO
Tarkista kirjauksesi tästä. Jännitepulssin **huippuarvo** $U_\text{max}$ on ensimmäisen pulssin eli magneetin käämiin tulon aikaisen jännitteen suurin itseisarvo. Lue se aina ensimmäisestä pulssista, oli se positiivinen tai negatiivinen. Ensimmäisen pulssin **pinta-ala** $S$ on jännitteen ja ajan kuvaajan ja aika-akselin väliin jäävä pinta-ala ensimmäisen pulssin alusta siihen hetkeen, jolloin jännite on taas nolla. Sen yksikkö on $\text{V} \cdot \text{s}$. Lyhyen pulssin mittaamiseen tarvitaan anturi ja tiedonkeruuohjelma, joka tallentaa jännitteen tiheästi. Tavallinen yleismittari päivittää lukemaansa liian harvoin.

Jos tutkit magneetin **nopeutta**, voit pudottaa magneetin levosta käämin yläpuolelta tunnetulta korkeudelta $h$. Kun ilmanvastus ja kitka ovat pieniä, mekaaninen energia säilyy, ja magneetin nopeus käämin kohdalla on

```latex
v = \sqrt{2gh}
```

Kun sama magneetti kulkee samojen kohtien ohi nopeammin, sama vuon muutos tapahtuu lyhyemmässä ajassa. Jos magneetin nopeus muuttuu vain vähän sinä aikana, kun se tulee käämiin, vuon muutosnopeus on suoraan verrannollinen nopeuteen, ja yksinkertaisin malli on

```latex
U_\text{max} = c\,v
```

missä $c$ on vakio, joka riippuu magneetista ja käämistä. Malli olettaa, että magneetti, sen asento ja käämi pysyvät samoina, magneetti lähtee levosta, ilmanvastus ja kitka ovat pieniä ja piirissä kulkee hyvin pieni virta. Pätevätkö malli ja sen oletukset, selviää vasta mittaamalla.

Jos tutkit **kierroslukua**, induktiolaki antaa saman vuon muutoksen jokaiselle kierrokselle, kun magneetti ja sen nopeus pysyvät samoina ja käämit ovat samankokoisia. Mieti itse, mitä laki silloin ennustaa huippuarvolle.
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona.

::: tuki O
**Ohjattu.** Tutkit magneetin nopeutta. Pudotat magneetin levosta pystysuoran muoviputken läpi, joka kulkee käämin läpi, ja muutat pudotuskorkeutta $h$. Mittaat korkeuden magneetin keskikohdasta käämin yläreunaan. Vakiona pidät magneetin, sen asennon (sama napa alaspäin), käämin ja putken. Käytä ainakin kuutta pudotuskorkeutta, esimerkiksi välillä $0{,}10\ \text{m}$ – $0{,}80\ \text{m}$, jos teline riittää, ja pudota magneetti jokaiselta korkeudelta kolme kertaa.
:::

::: tuki OO
**Osittain ohjattu.** Valitse tutkittavaksi tekijäksi joko magneetin nopeus tai käämin kierrosluku. Päätä itse, millä arvoilla mittaat, montako toistoa teet ja miten pidät muut tekijät vakioina. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
<svg data-fig="setup" viewBox="0 0 600 470" role="img" aria-label="Kaaviokuva yhdestä mahdollisesta järjestelystä. Pystysuora muoviputki kulkee käämin läpi, ja putken alapään alla on pehmeä alusta. Magneetti on putken yläosassa levossa. Pudotuskorkeus h on mitattu magneetin keskikohdasta käämin yläreunaan. Käämin päät on kytketty jänniteanturiin, joka on yhteydessä tietokoneeseen." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-induktio-setup.webp" x="1.2" y="1.2" width="597" height="471.4" preserveAspectRatio="none"/>
  <foreignObject x="302" y="182.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="395" y="297.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{jänniteanturi}$</div></foreignObject>
  <foreignObject x="74" y="320.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{käämi}$</div></foreignObject>
  <foreignObject x="50" y="80.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{magneetti}$</div></foreignObject>
  <foreignObject x="100" y="205.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{putki}$</div></foreignObject>
</svg>

Mieti ainakin näitä:

- Mitä tapahtuu jännitteen etumerkille, jos magneetti käännetään toisin päin? Miksi asennon täytyy olla joka kerta sama?
- Miten varmistat, että magneetti lähtee levosta eikä osu käämiin tai jää kiinni putkeen?
- Pudotuskorkeus mitataan käämin yläreunaan, mutta jännite on suurimmillaan suunnilleen silloin, kun magneetti tulee käämiin. Miksi pudotuskorkeuksien kannattaa olla selvästi suurempia kuin käämin ja magneetin pituus?
- Kuinka tiheästi anturin täytyy mitata, jotta lyhyimmänkin pulssin huippu tallentuu? Kokeile suurimmalla pudotuskorkeudella, jolla pulssi on lyhyin.
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle. Tallenna jokaisen kokeen jännitekuvaaja, jotta voit tarkistaa lukemat myöhemmin.

::: tuki O
Voit käyttää esimerkiksi kahta tällaista taulukkoa, toista huippuarvoille ja toista pinta-aloille. Jokaiselle pudotuskorkeudelle tulee kumpaankin yksi rivi, jossa on kolmen pudotuksen tulokset.

| $h\ (\text{m})$ | $U_{\text{max},1}\ (\text{V})$ | $U_{\text{max},2}\ (\text{V})$ | $U_{\text{max},3}\ (\text{V})$ |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| $h\ (\text{m})$ | $S_1\ (\text{V} \cdot \text{s})$ | $S_2\ (\text{V} \cdot \text{s})$ | $S_3\ (\text{V} \cdot \text{s})$ |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

Laske keskiarvot $\bar{U}_\text{max}$ ja $\bar{S}$ sekä nopeus $v = \sqrt{2gh}$ omiin sarakkeisiinsa mitattujen oikealle puolelle.

Säädä näytteenottotaajuus niin suureksi, että yksi pulssi koostuu ainakin kymmenistä mittauspisteistä. Lue huippuarvo ensimmäisestä pulssista itseisarvona ohjelman lukutyökalulla tai datataulukosta. Jos käämi on kytketty toisin päin, ensimmäinen pulssi on negatiivinen, ja ohjelman suurimman arvon työkalu löytää silloin toisen pulssin huipun, joka riippuu magneetin nopeudesta käämistä lähtiessä. Pinta-alan saat Graphical Analysis Prossa, kun valitset kuvaajasta välin ensimmäisen pulssin alusta siihen kohtaan, jossa jännite vaihtaa merkkiä, ja näytät valitun välin pinta-alan eli integraalin. Kirjaa pinta-ala itseisarvona.
:::

Muista mittausepävarmuus: kirjaa, kuinka tarkasti luet tutkimasi tekijän arvon ja miten paljon huippuarvo ja pinta-ala vaihtelevat toistojen välillä. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Piirrä mittaustuloksistasi kuvaaja, joka näyttää, miten huippuarvo riippuu tutkimastasi tekijästä, ja toinen kuvaaja pinta-alasta saman tekijän funktiona. Merkitse akseleille suureet ja yksiköt. Piirrä mittauspisteet, älä yhdistä niitä murtoviivalla, ja sovita pisteisiin malli, jonka voit perustella. [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

::: tuki O
Valitse ensimmäiseen kuvaajaan pystyakselille huippuarvon keskiarvo $\bar{U}_\text{max}$ ja vaaka-akselille nopeus $v$, ja toiseen kuvaajaan pystyakselille pinta-alan keskiarvo $\bar{S}$ ja vaaka-akselille taas $v$.
:::

Vastaa ja perustele vastauksesi induktiolain avulla:

1. Kuvaile yhden kokeen jännitekuvaaja: mitä etumerkkiä jännite on, kun magneetti tulee käämiin, ja mitä, kun se lähtee? Kumpi pulssi on suurempi, ja miksi?
2. Millainen riippuvuus huippuarvon ja tutkimasi tekijän välillä näkyy?
3. Miten pinta-ala muuttuu tutkimasi tekijän mukana? Miksi se käyttäytyy samoin tai eri tavalla kuin huippuarvo?

::: tuki O OO
Vastaa lisäksi: asettuvatko huippuarvon pisteet suoralle? Kulkeeko suora origon kautta? Mikä on kulmakertoimen fysikaalinen merkitys ja yksikkö?
:::

::: tuki O OO
Tarkista vastauksesi tästä. Alla on mallikuvaaja, joka on laskettu magneetille, joka putoaa vapaasti lyhyen käämin läpi. Se ei ole mittaus.

<svg data-fig="pulse" viewBox="0 0 600 360" role="img" aria-label="Mallikuvaaja: indusoitunut jännite U ajan t funktiona, kun magneetti putoaa käämin läpi. Ensin jännite kasvaa huippuarvoon U max ja palaa nollaan, kun magneetti tulee käämiin. Sitten jännite vaihtaa merkkiä, kun magneetti lähtee käämistä, ja tämä toinen pulssi on korkeampi ja kapeampi. Ensimmäisen pulssin ja aika-akselin väliin jäävä pinta-ala on merkitty kirjaimella S. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="200" x2="484" y2="200" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,200 L483,206 L483,194 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="201" x2="90" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,44 L96,57 L84,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="502" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="80" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <line x1="90" y1="200" x2="90" y2="340" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <polygon points="90,200 90.5,200 91,200 91.5,200 92,200 92.5,200 93,200 93,200 93.5,200 94,200 94.5,200 95,200 95.5,200 96,200 96.5,200 97,200 97.5,200 98,200 98.5,200 99,200 99,200 99.5,200 100,200 100.5,200 101,200 101.5,200 102,200 102.5,200 103,200 103.5,200 104,200 104.5,200 105,200 105,200 105.5,200 106,200 106.5,200 107,200 107.5,200 108,200 108.5,200 109,200 109.5,200 110,200 110.5,200 111,200 111,200 111.5,200 112,200 112.5,200 113,200 113.5,200 114,200 114.5,200 115,200 115.5,200 116,200 116.5,200 117,200 117,200 117.5,200 118,200 118.5,200 119,200 119.5,200 120,200 120.5,200 121,200 121.5,200 122,200 122.5,200 123,200 123,200 123.5,200 124,199.5 124.5,199.5 125,199.5 125.5,199.5 126,199.5 126.5,199.5 127,199.5 127.5,199.5 128,199.5 128.5,199.5 129,199.5 129,199.5 129.5,199.5 130,199.5 130.5,199.5 131,199.5 131.5,199.5 132,199.5 132.5,199.5 133,199.5 133.5,199.5 134,199.5 134.5,199.5 135,199.5 135,199.5 135.5,199.5 136,199.5 136.5,199.5 137,199.5 137.5,199.5 138,199.5 138.5,199.5 139,199.5 139.5,199.5 140,199.5 140.5,199.5 141,199.5 141.5,199.5 141.5,199.5 142,199.5 142.5,199.5 143,199.5 143.5,199.5 144,199.5 144.5,199.5 145,199.5 145.5,199.5 146,199.5 146.5,199.5 147,199.5 147.5,199.5 147.5,199.5 148,199.5 148.5,199.5 149,199.5 149.5,199.5 150,199.5 150.5,199.5 151,199.5 151.5,199.5 152,199.5 152.5,199.5 153,199.5 153.5,199.5 153.5,199.5 154,199.5 154.5,199.5 155,199.5 155.5,199.5 156,199.5 156.5,199.5 157,199.5 157.5,199.5 158,199.5 158.5,199.5 159,199.5 159.5,199.5 159.5,199.5 160,199.5 160.5,199.5 161,199.5 161.5,199.5 162,199.5 162.5,199.5 163,199.5 163.5,199.5 164,199.5 164.5,199.5 165,199.5 165.5,199.5 165.5,199.5 166,199.5 166.5,199.5 167,199.5 167.5,199.5 168,199.5 168.5,199.5 169,199.5 169.5,199.5 170,199.5 170.5,199.5 171,199.5 171.5,199.5 171.5,199.5 172,199.5 172.5,199.5 173,199.5 173.5,199.5 174,199 174.5,199 175,199 175.5,199 176,199 176.5,199 177,199 177.5,199 177.5,199 178,199 178.5,199 179,199 179.5,199 180,199 180.5,199 181,199 181.5,199 182,199 182.5,199 183,199 183.5,199 183.5,199 184,199 184.5,199 185,199 185.5,199 186,199 186.5,199 187,199 187.5,199 188,199 188.5,199 189,199 189.5,199 189.5,199 190,199 190.5,199 191,199 191.5,199 192,199 192.5,198.5 193,198.5 193.5,198.5 194,198.5 194.5,198.5 195,198.5 195.5,198.5 195.5,198.5 196,198.5 196.5,198.5 197,198.5 197.5,198.5 198,198.5 198.5,198.5 199,198.5 199.5,198.5 200,198.5 200.5,198.5 201,198.5 201.5,198.5 201.5,198.5 202,198.5 202.5,198.5 203,198 203.5,198 204,198 204.5,198 205,198 205.5,198 206,198 206.5,198 207,198 207.5,198 207.5,198 208,198 208.5,198 209,198 209.5,198 210,198 210.5,197.5 211,197.5 211.5,197.5 212,197.5 212.5,197.5 213,197.5 213.5,197.5 213.5,197.5 214,197.5 214.5,197.5 215,197.5 215.5,197.5 216,197.5 216.5,197 217,197 217.5,197 218,197 218.5,197 219,197 219.5,197 219.5,197 220,197 220.5,196.5 221,196.5 221.5,196.5 222,196.5 222.5,196.5 223,196.5 223.5,196.5 224,196.5 224.5,196 225,196 225.5,196 225.5,196 226,196 226.5,196 227,196 227.5,195.5 228,195.5 228.5,195.5 229,195.5 229.5,195.5 230,195.5 230.5,195 231,195 231.5,195 231.5,195 232,195 232.5,194.5 233,194.5 233.5,194.5 234,194.5 234.5,194.5 235,194 235.5,194 236,194 236.5,194 237,193.5 237.5,193.5 238,193.5 238,193 238.5,193 239,193 239.5,193 240,192.5 240.5,192.5 241,192.5 241.5,192 242,192 242.5,192 243,191.5 243.5,191.5 244,191.5 244,191 244.5,191 245,190.5 245.5,190.5 246,190 246.5,190 247,190 247.5,189.5 248,189.5 248.5,189 249,189 249.5,188.5 250,188 250,188 250.5,187.5 251,187.5 251.5,187 252,186.5 252.5,186.5 253,186 253.5,185.5 254,185.5 254.5,185 255,184.5 255.5,184 256,184 256,183.5 256.5,183 257,182.5 257.5,182 258,181.5 258.5,181 259,180.5 259.5,180 260,179.5 260.5,179 261,178.5 261.5,178 262,177.5 262,177 262.5,176 263,175.5 263.5,175 264,174 264.5,173.5 265,173 265.5,172 266,171.5 266.5,170.5 267,169.5 267.5,169 268,168 268,167 268.5,166 269,165 269.5,164.5 270,163.5 270.5,162.5 271,161 271.5,160 272,159 272.5,158 273,157 273.5,155.5 274,154.5 274,153 274.5,152 275,150.5 275.5,149 276,148 276.5,146.5 277,145 277.5,143.5 278,142 278.5,140.5 279,139 279.5,137.5 280,135.5 280,134 280.5,132.5 281,130.5 281.5,129 282,127.5 282.5,125.5 283,124 283.5,122 284,120.5 284.5,118.5 285,117 285.5,115 286,113.5 286,111.5 286.5,110 287,108.5 287.5,106.5 288,105 288.5,103.5 289,102 289.5,100.5 290,99 290.5,98 291,96.5 291.5,95.5 292,94 292,93 292.5,92.5 293,91.5 293.5,91 294,90 294.5,89.5 295,89.5 295.5,89 296,89 296.5,89 297,89.5 297.5,89.5 298,90 298,91 298.5,91.5 299,92.5 299.5,93.5 300,95 300.5,96.5 301,98 301.5,99.5 302,101.5 302.5,103.5 303,105.5 303.5,107.5 304,110 304,112.5 304.5,115 305,118 305.5,120.5 306,123.5 306.5,126.5 307,129.5 307.5,133 308,136 308.5,139.5 309,143 309.5,146.5 310,150 310,153.5 310.5,157 311,161 311.5,164.5 312,168.5 312.5,172 313,176 313.5,180 314,184 314.5,188 315,191.5 315.5,195.5 316,199.5 316,203.5 316,200 90,200" fill="#2b8a3e" fill-opacity="0.25"/>
  <polyline points="90,200 90.5,200 91,200 91.5,200 92,200 92.5,200 93,200 93,200 93.5,200 94,200 94.5,200 95,200 95.5,200 96,200 96.5,200 97,200 97.5,200 98,200 98.5,200 99,200 99,200 99.5,200 100,200 100.5,200 101,200 101.5,200 102,200 102.5,200 103,200 103.5,200 104,200 104.5,200 105,200 105,200 105.5,200 106,200 106.5,200 107,200 107.5,200 108,200 108.5,200 109,200 109.5,200 110,200 110.5,200 111,200 111,200 111.5,200 112,200 112.5,200 113,200 113.5,200 114,200 114.5,200 115,200 115.5,200 116,200 116.5,200 117,200 117,200 117.5,200 118,200 118.5,200 119,200 119.5,200 120,200 120.5,200 121,200 121.5,200 122,200 122.5,200 123,200 123,200 123.5,200 124,199.5 124.5,199.5 125,199.5 125.5,199.5 126,199.5 126.5,199.5 127,199.5 127.5,199.5 128,199.5 128.5,199.5 129,199.5 129,199.5 129.5,199.5 130,199.5 130.5,199.5 131,199.5 131.5,199.5 132,199.5 132.5,199.5 133,199.5 133.5,199.5 134,199.5 134.5,199.5 135,199.5 135,199.5 135.5,199.5 136,199.5 136.5,199.5 137,199.5 137.5,199.5 138,199.5 138.5,199.5 139,199.5 139.5,199.5 140,199.5 140.5,199.5 141,199.5 141.5,199.5 141.5,199.5 142,199.5 142.5,199.5 143,199.5 143.5,199.5 144,199.5 144.5,199.5 145,199.5 145.5,199.5 146,199.5 146.5,199.5 147,199.5 147.5,199.5 147.5,199.5 148,199.5 148.5,199.5 149,199.5 149.5,199.5 150,199.5 150.5,199.5 151,199.5 151.5,199.5 152,199.5 152.5,199.5 153,199.5 153.5,199.5 153.5,199.5 154,199.5 154.5,199.5 155,199.5 155.5,199.5 156,199.5 156.5,199.5 157,199.5 157.5,199.5 158,199.5 158.5,199.5 159,199.5 159.5,199.5 159.5,199.5 160,199.5 160.5,199.5 161,199.5 161.5,199.5 162,199.5 162.5,199.5 163,199.5 163.5,199.5 164,199.5 164.5,199.5 165,199.5 165.5,199.5 165.5,199.5 166,199.5 166.5,199.5 167,199.5 167.5,199.5 168,199.5 168.5,199.5 169,199.5 169.5,199.5 170,199.5 170.5,199.5 171,199.5 171.5,199.5 171.5,199.5 172,199.5 172.5,199.5 173,199.5 173.5,199.5 174,199 174.5,199 175,199 175.5,199 176,199 176.5,199 177,199 177.5,199 177.5,199 178,199 178.5,199 179,199 179.5,199 180,199 180.5,199 181,199 181.5,199 182,199 182.5,199 183,199 183.5,199 183.5,199 184,199 184.5,199 185,199 185.5,199 186,199 186.5,199 187,199 187.5,199 188,199 188.5,199 189,199 189.5,199 189.5,199 190,199 190.5,199 191,199 191.5,199 192,199 192.5,198.5 193,198.5 193.5,198.5 194,198.5 194.5,198.5 195,198.5 195.5,198.5 195.5,198.5 196,198.5 196.5,198.5 197,198.5 197.5,198.5 198,198.5 198.5,198.5 199,198.5 199.5,198.5 200,198.5 200.5,198.5 201,198.5 201.5,198.5 201.5,198.5 202,198.5 202.5,198.5 203,198 203.5,198 204,198 204.5,198 205,198 205.5,198 206,198 206.5,198 207,198 207.5,198 207.5,198 208,198 208.5,198 209,198 209.5,198 210,198 210.5,197.5 211,197.5 211.5,197.5 212,197.5 212.5,197.5 213,197.5 213.5,197.5 213.5,197.5 214,197.5 214.5,197.5 215,197.5 215.5,197.5 216,197.5 216.5,197 217,197 217.5,197 218,197 218.5,197 219,197 219.5,197 219.5,197 220,197 220.5,196.5 221,196.5 221.5,196.5 222,196.5 222.5,196.5 223,196.5 223.5,196.5 224,196.5 224.5,196 225,196 225.5,196 225.5,196 226,196 226.5,196 227,196 227.5,195.5 228,195.5 228.5,195.5 229,195.5 229.5,195.5 230,195.5 230.5,195 231,195 231.5,195 231.5,195 232,195 232.5,194.5 233,194.5 233.5,194.5 234,194.5 234.5,194.5 235,194 235.5,194 236,194 236.5,194 237,193.5 237.5,193.5 238,193.5 238,193 238.5,193 239,193 239.5,193 240,192.5 240.5,192.5 241,192.5 241.5,192 242,192 242.5,192 243,191.5 243.5,191.5 244,191.5 244,191 244.5,191 245,190.5 245.5,190.5 246,190 246.5,190 247,190 247.5,189.5 248,189.5 248.5,189 249,189 249.5,188.5 250,188 250,188 250.5,187.5 251,187.5 251.5,187 252,186.5 252.5,186.5 253,186 253.5,185.5 254,185.5 254.5,185 255,184.5 255.5,184 256,184 256,183.5 256.5,183 257,182.5 257.5,182 258,181.5 258.5,181 259,180.5 259.5,180 260,179.5 260.5,179 261,178.5 261.5,178 262,177.5 262,177 262.5,176 263,175.5 263.5,175 264,174 264.5,173.5 265,173 265.5,172 266,171.5 266.5,170.5 267,169.5 267.5,169 268,168 268,167 268.5,166 269,165 269.5,164.5 270,163.5 270.5,162.5 271,161 271.5,160 272,159 272.5,158 273,157 273.5,155.5 274,154.5 274,153 274.5,152 275,150.5 275.5,149 276,148 276.5,146.5 277,145 277.5,143.5 278,142 278.5,140.5 279,139 279.5,137.5 280,135.5 280,134 280.5,132.5 281,130.5 281.5,129 282,127.5 282.5,125.5 283,124 283.5,122 284,120.5 284.5,118.5 285,117 285.5,115 286,113.5 286,111.5 286.5,110 287,108.5 287.5,106.5 288,105 288.5,103.5 289,102 289.5,100.5 290,99 290.5,98 291,96.5 291.5,95.5 292,94 292,93 292.5,92.5 293,91.5 293.5,91 294,90 294.5,89.5 295,89.5 295.5,89 296,89 296.5,89 297,89.5 297.5,89.5 298,90 298,91 298.5,91.5 299,92.5 299.5,93.5 300,95 300.5,96.5 301,98 301.5,99.5 302,101.5 302.5,103.5 303,105.5 303.5,107.5 304,110 304,112.5 304.5,115 305,118 305.5,120.5 306,123.5 306.5,126.5 307,129.5 307.5,133 308,136 308.5,139.5 309,143 309.5,146.5 310,150 310,153.5 310.5,157 311,161 311.5,164.5 312,168.5 312.5,172 313,176 313.5,180 314,184 314.5,188 315,191.5 315.5,195.5 316,199.5 316,203.5 316.5,207.5 317,211.5 317.5,215.5 318,219.5 318.5,223.5 319,227.5 319.5,231.5 320,235.5 320.5,239.5 321,243.5 321.5,247.5 322,251.5 322,255 322.5,259 323,262.5 323.5,266 324,270 324.5,273.5 325,277 325.5,280 326,283.5 326.5,286.5 327,289.5 327.5,292.5 328,295.5 328.5,298 328.5,300.5 329,303 329.5,305.5 330,307.5 330.5,309.5 331,311 331.5,313 332,314.5 332.5,315.5 333,316.5 333.5,317.5 334,318.5 334.5,319 334.5,319.5 335,319.5 335.5,319.5 336,319.5 336.5,319 337,319 337.5,318 338,317.5 338.5,316.5 339,315.5 339.5,314.5 340,313 340.5,312 340.5,310.5 341,309 341.5,307 342,305.5 342.5,303.5 343,302 343.5,300 344,298 344.5,296 345,294 345.5,292 346,290 346.5,288 346.5,286 347,284 347.5,282 348,280 348.5,278 349,275.5 349.5,274 350,272 350.5,270 351,268 351.5,266 352,264 352.5,262.5 352.5,260.5 353,259 353.5,257 354,255.5 354.5,254 355,252.5 355.5,251 356,249.5 356.5,248 357,246.5 357.5,245 358,243.5 358.5,242.5 358.5,241 359,240 359.5,238.5 360,237.5 360.5,236.5 361,235.5 361.5,234 362,233 362.5,232 363,231 363.5,230.5 364,229.5 364.5,228.5 364.5,227.5 365,227 365.5,226 366,225.5 366.5,224.5 367,224 367.5,223 368,222.5 368.5,222 369,221 369.5,220.5 370,220 370.5,219.5 370.5,219 371,218.5 371.5,218 372,217.5 372.5,217 373,216.5 373.5,216 374,215.5 374.5,215 375,214.5 375.5,214 376,214 376.5,213.5 376.5,213 377,212.5 377.5,212.5 378,212 378.5,211.5 379,211.5 379.5,211 380,211 380.5,210.5 381,210.5 381.5,210 382,209.5 382.5,209.5 382.5,209.5 383,209 383.5,209 384,208.5 384.5,208.5 385,208 385.5,208 386,208 386.5,207.5 387,207.5 387.5,207 388,207 388.5,207 388.5,206.5 389,206.5 389.5,206.5 390,206 390.5,206 391,206 391.5,206 392,205.5 392.5,205.5 393,205.5 393.5,205.5 394,205 394.5,205 394.5,205 395,205 395.5,204.5 396,204.5 396.5,204.5 397,204.5 397.5,204.5 398,204 398.5,204 399,204 399.5,204 400,204 400.5,204 400.5,203.5 401,203.5 401.5,203.5 402,203.5 402.5,203.5 403,203.5 403.5,203.5 404,203 404.5,203 405,203 405.5,203 406,203 406.5,203 406.5,203 407,203 407.5,202.5 408,202.5 408.5,202.5 409,202.5 409.5,202.5 410,202.5 410.5,202.5 411,202.5 411.5,202.5 412,202.5 412.5,202 412.5,202 413,202 413.5,202 414,202 414.5,202 415,202 415.5,202 416,202 416.5,202 417,202 417.5,202 418,202 418.5,201.5 418.5,201.5 419,201.5 419.5,201.5 420,201.5 420.5,201.5 421,201.5 421.5,201.5 422,201.5 422.5,201.5 423,201.5 423.5,201.5 424,201.5 424.5,201.5 425,201.5 425,201.5 425.5,201.5 426,201.5 426.5,201.5 427,201 427.5,201 428,201 428.5,201 429,201 429.5,201 430,201 430.5,201 431,201 431,201 431.5,201 432,201 432.5,201 433,201 433.5,201 434,201 434.5,201 435,201 435.5,201 436,201 436.5,201 437,201 437,201 437.5,201 438,201 438.5,201 439,201 439.5,201 440,201 440.5,201 441,201 441.5,201 442,200.5 442.5,200.5 443,200.5 443,200.5 443.5,200.5 444,200.5 444.5,200.5 445,200.5 445.5,200.5 446,200.5 446.5,200.5 447,200.5 447.5,200.5 448,200.5 448.5,200.5 449,200.5 449,200.5 449.5,200.5 450,200.5 450.5,200.5 451,200.5 451.5,200.5 452,200.5 452.5,200.5 453,200.5 453.5,200.5 454,200.5 454.5,200.5 455,200.5 455,200.5 455.5,200.5 456,200.5 456.5,200.5 457,200.5 457.5,200.5 458,200.5 458.5,200.5 459,200.5 459.5,200.5 460,200.5 460.5,200.5 461,200.5 461,200.5 461.5,200.5 462,200.5 462.5,200.5 463,200.5 463.5,200.5 464,200.5 464.5,200.5 465,200.5 465.5,200.5 466,200.5 466.5,200.5 467,200.5 467,200.5 467.5,200.5 468,200.5 468.5,200.5 469,200.5 469.5,200.5 470,200.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="90" y1="89" x2="296" y2="89" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="26" y="74.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U_\text{max}$</div></foreignObject>
  <foreignObject x="187" y="146.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$S$</div></foreignObject>
  <foreignObject x="359.5" y="307" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{toinen pulssi}$</div></foreignObject>
  <foreignObject x="322" y="72.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{ensimmäinen pulssi}$</div></foreignObject>
</svg>

Kun magneetti tulee käämiin, vuo kasvaa, ja kun se lähtee, vuo pienenee. Siksi pulssit ovat erimerkkiset. Putoava magneetti on käämistä lähtiessään nopeampi kuin tullessaan, joten sama vuon muutos tapahtuu lyhyemmässä ajassa.

Induktiolaista seuraa, että pulssin pinta-ala on $S = N\Delta\Phi$, missä $\Delta\Phi$ on vuon kokonaismuutos koko pulssin aikana, keskimäärin yhtä kierrosta kohti. Pinta-ala kertoo siis, kuinka paljon vuo muuttuu, ja huippuarvo, kuinka nopeasti se muuttuu. Vertaa tätä omiin kuvaajiisi. Jos tuloksesi poikkeavat, mieti, mitkä mallin oletukset eivät mittauksessasi täyttyneet.
:::

Kuvaajan sovitukseen ja pulssin pinta-alan laskemiseen käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Ilmoita jokaisen mittauspisteen huippuarvo ja pinta-ala epävarmuuksineen, ja ilmoita sovituksen tulos, esimerkiksi kulmakerroin, epävarmuuksineen ja yksikköineen. Perustele, miten arvioit epävarmuudet.

::: tuki O OO
Epävarmuudet voit arvioida esimerkiksi näin:

- **Toistot.** Laske kunkin korkeuden huippuarvoista keskiarvo $\bar{U}_\text{max}$ ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta U_\text{max} = \dfrac{U_\text{suurin} - U_\text{pienin}}{2}$. Pinta-alalle samoin.
- **Nopeus.** Kun $v = \sqrt{2gh}$, nopeuden suhteellinen epävarmuus on puolet korkeuden suhteellisesta epävarmuudesta: $\dfrac{\Delta v}{v} = \dfrac{1}{2} \cdot \dfrac{\Delta h}{h}$.
- **Kulmakerroin.** Käytä sovitusohjelman ilmoittamaa kulmakertoimen keskivirhettä tai piirrä jyrkin ja loivin pisteisiin sopiva suora ja ota epävarmuudeksi niiden kulmakertoimien erotuksen puolikas.

Pyöristä epävarmuus yhteen merkitsevään numeroon ja tulos samaan desimaaliin.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet tulosta? Pohdi erityisesti, tallentuiko pulssin huippu kokonaan ja pysyivätkö vakioina pidettävät tekijät todella samoina. Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella: miten huippuarvo ja pinta-ala riippuvat tutkimastasi tekijästä? Viittaa kuvaajiin, esimerkiksi ”kuvaajasta 1 nähdään, että …”. Perustele induktiolain avulla, miksi huippuarvo ja pinta-ala käyttäytyvät niin kuin mittasit. Vertaa tuloksia ennusteisiisi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tutkimuskysymys ja tausta:** mikä tekijä valittiin ja miksi, induktiolaki ja mitä huippuarvo ja pinta-ala kertovat vuon muutoksesta.
- **Koejärjestely ja menetelmä:** kuva järjestelystä, mitä muutit, mitä mittasit ja mitä pidit vakiona, sekä näytteenottotaajuus.
- **Mittaustulokset:** alkuperäiset lukemat omissa sarakkeissaan ja ainakin yksi tallennettu jännitekuvaaja.
- **Tulosten käsittely:** molemmat kuvaajat, sovitetut mallit ja niiden perustelut.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet ja niiden vaikutuksen suunta.

## Laajennus: käämin kierrosluku

Tutki, miten huippuarvo ja pinta-ala riippuvat käämin kierrosluvusta $N$. Ennusta ensin riippuvuudet, mittaa ne usealla käämillä ja esitä tulokset kuvaajina. Vahvistavatko tulokset ennusteesi?

Pohdi lopuksi: käämeissä, joissa on paljon kierroksia, on yleensä ohuempaa lankaa ja suurempi resistanssi. Vaikuttaako resistanssi mittaamaasi jännitteeseen, kun käytät jänniteanturia? Miksi muuntajissa käämien kierroslukujen suhde ratkaisee jännitteen muutoksen?

::: tuki OO I
Jos tutkit päämittauksessa kierroslukua, tutki laajennuksessa magneetin nopeutta tai magneetin voimakkuutta.
:::

::: tuki O OO
**Vihjeitä.** Pidä magneetti ja sen nopeus samoina ja vaihda vain käämiä. Käytä käämejä, joissa on eri kierrosluvut mutta mahdollisimman samanlainen koko ja muoto. Pudota magneetti joka käämillä samalta korkeudelta ja samassa asennossa. Kirjaa käämien kierrosluvut niiden kyljestä tai opettajalta. Jos käämit ovat erikokoisia, kierroksia läpäisevä vuo voi olla eri suuri, mikä näkyy poikkeamana mallista.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajiin ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
