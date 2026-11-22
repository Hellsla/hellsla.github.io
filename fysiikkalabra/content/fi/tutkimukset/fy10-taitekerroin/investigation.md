# Taitekertoimen määrittäminen

> **Tutkimuskysymys:** Miten valon taitekulma riippuu tulokulmasta, kun valo tulee läpinäkyvästä kappaleesta ilmaan, ja kuinka suuri on kappaleen aineen taitekerroin?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöytä ylhäältä päin. Pöydällä on pyöreä kulma-asteikko, jonka päällä on puoliympyrän muotoinen läpinäkyvä kappale. Pöydän vasemmassa reunassa on laser, jonka säde kulkee asteikon nollasuuntaa pitkin kappaleen kaarevan pinnan läpi sen tasaisen pinnan keskipisteeseen ja siitä suoraan eteenpäin pieneen paperivarjostimeen. Oikealla on vihko ja lyijykynä." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-taitekerroin-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

Lasissa oleva lusikka näyttää katkenneen veden pinnan kohdalta, ja uima-altaan pohja näyttää todellista matalammalta. Molemmat johtuvat siitä, että valo muuttaa suuntaansa siirtyessään aineesta toiseen. Tässä tutkimuksessa mittaat laserin säteen avulla, miten valon suunta muuttuu, kun se tulee läpinäkyvästä kappaleesta ilmaan, ja määrität kappaleen aineelle luvun, joka kuvaa tätä ilmiötä. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** miten taitekulma riippuu tulokulmasta, kun valo tulee kappaleesta ilmaan, ja kuinka suuri kappaleen aineen taitekerroin on epävarmuuksineen.

**Päätät itse (osittain ohjattu ja itsenäinen työtapa):** käytettävät tulokulmat ja niiden määrän, toistomittaukset, sen, miten varmistat kappaleen ja asteikon asennon, kuvaajan akselit perusteluineen sekä tavan, jolla arvioit tuloksen epävarmuuden. Ohjatussa työtavassa sivu kiinnittää nämä valinnat puolestasi, osittain ohjatussa se antaa niihin tukea, ja itsenäisessä työtavassa perustelet valintasi itse.

::: tuki I
**Itsenäinen työtapa.** Laajennus, taitekertoimen määrittäminen rajakulmasta, kuuluu työhösi: vertaa lopuksi kahdella menetelmällä saatuja tuloksia.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Kun säde tulee kappaleesta ilmaan vinosti, kääntyykö se kohti pinnan normaalia vai siitä poispäin? Onko taitekulma siis tulokulmaa suurempi vai pienempi?
2. Onko taitekulma suoraan verrannollinen tulokulmaan: kaksinkertaistuuko taitekulma, kun tulokulma kaksinkertaistuu?
3. Mitä arvelet tapahtuvan taittuneelle säteelle, kun tulokulmaa kasvatetaan yhä suuremmaksi?
4. Mikä mittauksessa on todennäköisesti suurin epävarmuuden lähde?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Teoriaa lyhyesti

Valon taittumista käsitellään tarkemmin moduulissa FY7. Tässä on se, mitä tarvitset tähän työhön.

Valo etenee eri aineissa eri nopeuksilla. Aineen **taitekerroin** $n$ kertoo, kuinka monta kertaa suurempi valon nopeus $c$ tyhjiössä on kuin valon nopeus $v$ aineessa: $n = \dfrac{c}{v}$. Taitekerroin on yksikötön luku. Ilman taitekerroin on niin lähellä yhtä, noin $1{,}0003$, että tässä työssä sen voi merkitä ykköseksi.

Kun valo osuu vinosti kahden aineen rajapintaan, se muuttaa rajapinnassa suuntaansa eli **taittuu**. Kulmat mitataan aina rajapinnan **normaalista** eli rajapintaa vastaan kohtisuorasta suorasta, ei pinnasta. **Tulokulma** $\alpha$ on tulevan säteen ja normaalin välinen kulma, ja **taitekulma** $\beta$ on taittuneen säteen ja normaalin välinen kulma. Osa valosta myös heijastuu rajapinnasta, ja heijastuneen säteen kulma normaaliin on yhtä suuri kuin tulokulma.

Kulmat liittyvät toisiinsa **taittumislain** eli Snellin lain mukaan:

```latex
n_1 \sin\alpha = n_2 \sin\beta
```

missä $n_1$ on sen aineen taitekerroin, josta valo tulee, ja $n_2$ sen aineen, johon valo taittuu. Kun valo tulee kappaleesta ilmaan, $n_1$ on kappaleen aineen taitekerroin $n$ ja $n_2 = 1$. Taitekerroin riippuu hieman valon väristä, joten mittaamasi taitekerroin koskee laserin valon väriä.

Tässä työssä säde suunnataan puoliympyrän muotoisen kappaleen kaarevan pinnan läpi tasaisen pinnan keskipisteeseen. Tällöin säde kulkee kaarevan pinnan läpi ympyrän säteen suuntaisesti eli kohtisuoraan pintaa vastaan, joten se ei taitu siinä. Säde taittuu vain kerran, tasaisessa pinnassa, kun se tulee kappaleesta ilmaan. Malli edellyttää siis, että säde osuu tasaisen pinnan keskipisteeseen ja että kulmat luetaan tasaisen pinnan normaalista.

<svg data-fig="setup" viewBox="0 0 600 440" role="img" aria-label="Kaaviokuva ylhäältä päin. Puoliympyrän muotoisen kappaleen tasainen pinta on pystysuorassa kuvan keskellä, ja kaareva pinta on vasemmalla. Tasaisen pinnan keskipisteen kautta kulkee vaakasuora katkoviiva, pinnan normaali. Laserin säde tulee vasemmalta alhaalta kaarevan pinnan läpi säteen suuntaisesti tasaisen pinnan keskipisteeseen. Tulokulma alfa on kappaleen sisällä säteen ja normaalin välinen kulma. Ilmaan tullut säde jatkaa oikealle ylös, ja taitekulma beeta on sen ja normaalin välinen kulma. Osa valosta heijastuu tasaisesta pinnasta takaisin kappaleeseen ohuena katkoviivana. Kuva on piirretty mittakaavassa taitekertoimella 1,5." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-taitekerroin-setup.webp" x="0" y="0" width="600" height="445" preserveAspectRatio="none"/>
  <foreignObject x="198" y="221.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="382" y="177.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\beta$</div></foreignObject>
  <foreignObject x="202.5" y="285.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kappale}$</div></foreignObject>
  <foreignObject x="381" y="295.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{ilma}$</div></foreignObject>
  <foreignObject x="330" y="231.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{normaali}$</div></foreignObject>
  <foreignObject x="23" y="363" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{laser}$</div></foreignObject>
</svg>

::: tuki OO
**Vihje akseleihin.** Taittumislaki ei sano, että kulmat itse olisivat suoraan verrannollisia. Mitkä suureet laki sanoo suoraan verrannollisiksi, kun valo tulee kappaleesta ilmaan? Valitse niiden perusteella kuvaajan akselit niin, että kulmakerroin on taitekerroin, ja kirjaa perustelusi.
:::

::: tuki O
**Mallista suoraksi.** Kun valo tulee kappaleesta ilmaan, taittumislaki on muotoa

```latex
\sin\beta = n \cdot \sin\alpha
```

Kun pystyakselille valitaan taitekulman sini $\sin\beta$ ja vaaka-akselille tulokulman sini $\sin\alpha$, mallin kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on taitekerroin $n$. Sini ei voi olla suurempi kuin yksi, joten suora päättyy, kun $\sin\beta = 1$.

<svg data-fig="model" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja: taitekulman sini tulokulman sinin funktiona taittumislain mallin mukaan, kun valo tulee aineesta ilmaan. Kuvaaja on origon kautta kulkeva suora, joka päättyy, kun taitekulman sini on yksi. Suoralle on merkitty kaksi pistettä ja niiden välinen muutos vaaka- ja pystysuunnassa. Kulmakerroin on taitekerroin n. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="99" y1="290" x2="464" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M476,290 L463,296 L463,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="291" x2="100" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,24 L106,37 L94,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="93" y1="72" x2="100" y2="72" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="68" y="57.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="70" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="482" y="275.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\sin\alpha$</div></foreignObject>
  <foreignObject x="114" y="15.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\sin\beta$</span></div></foreignObject>
  <polyline points="100,290 333.5,72" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="100" y1="72" x2="432.5" y2="72" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="170" y1="224.5" x2="292.5" y2="224.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="292.5" y1="224.5" x2="292.5" y2="110" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="201" y="232.5" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\Delta(\sin\alpha)$</div></foreignObject>
  <foreignObject x="302.5" y="155.5" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\Delta(\sin\beta)$</div></foreignObject>
  <foreignObject x="353.5" y="213" width="95" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$n = \dfrac{\Delta(\sin\beta)}{\Delta(\sin\alpha)}$</div></foreignObject>
</svg>
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona.

::: tuki O
**Ohjattu.** Muutat tulokulmaa $\alpha$ kääntämällä alustaa ja mittaat jokaisella tulokulmalla taitekulman $\beta$. Vakiona pidät kappaleen paikan alustalla ja laserin paikan pöydällä. Aloita tulokulmasta $5^\circ$ ja kasvata sitä $5^\circ$ kerrallaan, kunnes taittunut säde katoaa. Mittaa jokainen tulokulma normaalin kummallakin puolella, eli käännä alustaa ensin yhteen ja sitten toiseen suuntaan.
:::

::: tuki OO
**Osittain ohjattu.** Muuttuja on tulokulma. Päätä itse, mitä tulokulmia käytät, montako mittausta teet ja miten varmistat, että kulmat luetaan oikein normaalista. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Miten asetat kappaleen alustalle niin, että tasaisen pinnan keskipiste on asteikon keskipisteessä ja asteikon nollasuunta on tasaisen pinnan normaali? Mitä säteelle pitäisi tapahtua, kun tulokulma on nolla?
- Miten voit käyttää tasaisesta pinnasta heijastuvaa heikkoa sädettä kohdistuksen tarkistamiseen?
- Miksi kannattaa mitata samat tulokulmat normaalin kummallakin puolella?
- Ulottuvatko tulokulmasi koko alueelle, jolla taittunut säde näkyy, myös suurimpiin kulmiin?
- Mistä kohdasta asteikkoa luet kulman, kun säde on muutaman millimetrin levyinen?
:::

## Mittaa

Kirjaa alkuperäiset lukemat taulukkoon heti mittauksen aikana. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle. Kirjaa myös, mitä havaitset taittuneesta ja heijastuneesta säteestä, kun tulokulma kasvaa suureksi.

::: tuki O
Voit käyttää esimerkiksi tällaista taulukkoa. Kirjaa kulmat suuruuksina, ilman etumerkkiä.

| $\alpha\ (^\circ)$ | $\beta_1\ (^\circ)$ | $\beta_2\ (^\circ)$ | $\bar{\beta}\ (^\circ)$ | $\sin\alpha$ | $\sin\bar{\beta}$ |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

Tässä $\beta_1$ ja $\beta_2$ ovat taitekulmat normaalin eri puolilla ja $\bar{\beta}$ niiden keskiarvo. Lue kulma säteen keskeltä ja katso asteikkoa suoraan ylhäältä. Tarkista ennen sarjaa, että tulokulmalla nolla säde kulkee kappaleen läpi suoraan ja heijastunut säde palaa laseria kohti. Laske sinit laskimella, joka on asteissa, tai ohjelmalla, jolle annat kulmat oikeassa yksikössä.
:::

Muista mittausepävarmuus: kirjaa, kuinka tarkasti voit lukea kulmat asteikolta, ja merkitse se taulukkoon. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Piirrä ensin taitekulma tulokulman funktiona. Piirrä sitten mittaustuloksista kuvaaja, josta taitekerroin saadaan kulmakertoimena. Merkitse akseleille suureet ja yksiköt, piirrä mittauspisteet, älä yhdistä niitä murtoviivalla, ja sovita pisteisiin suora. [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

::: tuki O
Valitse toisen kuvaajan pystyakselille $\sin\bar{\beta}$ ja vaaka-akselille $\sin\alpha$. Sinit ovat yksiköttömiä.
:::

::: tuki O OO
Arvioi kysymyksessä 1 verrannollisuutta koko mittausalueella, myös suurimmilla tulokulmilla, äläkä vain pienten kulmien pisteiden perusteella.
:::

Kirjoita sovitetun suoran yhtälö ja vastaa:

1. Onko taitekulma suoraan verrannollinen tulokulmaan? Perustele ensimmäisen kuvaajan avulla.
2. Perustele taittumislain avulla, miksi toisen kuvaajan akseleiksi sopivat juuri nämä suureet.
3. Ovatko pisteet suoralla? Kulkeeko suora origon kautta? Jos ei, mistä poikkeama voi johtua?
4. Mikä suure on kulmakerroin, ja mikä on sen yksikkö?

Kuvaajan sovitukseen käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Ilmoita taitekerroin muodossa $n \pm \Delta n$ ja perustele, miten arvioit epävarmuuden $\Delta n$.

::: tuki O OO
**Sinien epävarmuus.** Kummallakin sinillä, $\sin\alpha$ ja $\sin\beta$, on epävarmuus, koska kumpikin kulma luetaan asteikolta. Jos kulman $\beta$ epävarmuus on $\Delta\beta$, laske $\sin(\beta + \Delta\beta)$ ja $\sin(\beta - \Delta\beta)$; jos $\beta + \Delta\beta$ on yli $90^\circ$, käytä ylärajana arvoa $\sin 90^\circ = 1$. Sinin epävarmuus on niiden erotuksen puolikas. Laske tulokulman sinin epävarmuus samalla tavalla kulman $\alpha$ epävarmuudesta $\Delta\alpha$. Huomaa, että sama kulman epävarmuus vaikuttaa siniin eri kulmilla eri verran.

**Kulmakertoimen epävarmuus** jommallakummalla tavalla:

- **Sovitusohjelman keskivirhe.** Monet ohjelmat ilmoittavat kulmakertoimen keskivirheen. Käytä sitä epävarmuutena $\Delta n$.
- **Jyrkin ja loivin suora.** Piirrä jyrkin ja loivin suora, jotka vielä sopivat pisteisiin niiden epävarmuuksien rajoissa. Määritä niiden kulmakertoimet $n_\text{max}$ ja $n_\text{min}$ ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta n = \dfrac{n_\text{max} - n_\text{min}}{2}$.

Pyöristä $\Delta n$ yhteen merkitsevään numeroon ja $n$ samaan desimaaliin.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet tulosta? Miten tulokseen vaikuttaisi, jos säde ei osuisi tarkasti tasaisen pinnan keskipisteeseen tai jos asteikon nollasuunta ei olisi tasaisen pinnan normaalin suuntainen? Millä tulokulmilla kulmat oli vaikein lukea? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Mitä tapahtui, kun tulokulma kasvoi suureksi? Viittaa kuvaajiin, esimerkiksi "kuvaajasta 2 nähdään, että …". Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei? Jos opettaja kertoo, mitä ainetta kappale on, vertaa tulostasi myös aineen taulukkoarvoon epävarmuuksineen.

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** taittumislaki, mistä kulmat mitataan ja miksi säde suunnattiin tasaisen pinnan keskipisteeseen.
- **Koejärjestely ja menetelmä:** mitä muutit, mitä mittasit ja mitä pidit vakiona, myös miten tarkistit kappaleen ja asteikon asennon.
- **Mittaustulokset:** alkuperäiset kulmalukemat omissa sarakkeissaan ja sinit niiden oikealla puolella, sekä havaintosi suurilla tulokulmilla.
- **Tulos:** taitekerroin muodossa $n \pm \Delta n$ oikein pyöristettynä ja perustelu kuvaajan akseleille.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet ja niiden vaikutuksen suunta.

## Laajennus: taitekerroin rajakulmasta

Kun valo tulee aineesta, jonka taitekerroin on suurempi, aineeseen, jonka taitekerroin on pienempi, taitekulma on tulokulmaa suurempi. Kun tulokulmaa kasvatetaan, taitekulma kasvaa lopulta $90^\circ$:een, jolloin taittunut säde kulkee pintaa pitkin. Tätä tulokulmaa kutsutaan **rajakulmaksi** $\alpha_\text{r}$. Kun tulokulma on rajakulmaa suurempi, taittunutta sädettä ei synny, vaan kaikki valo heijastuu takaisin kappaleeseen. Ilmiö on **kokonaisheijastus**, ja sitä käsitellään tarkemmin moduulissa FY7. Kun taittumislakiin sijoitetaan $\beta = 90^\circ$ ja $\sin 90^\circ = 1$, saadaan

```latex
n \sin\alpha_\text{r} = 1 \quad\Rightarrow\quad n = \frac{1}{\sin\alpha_\text{r}}
```

Määritä kappaleen rajakulma mittaamalla ja laske siitä taitekerroin epävarmuuksineen. Vertaa kahdella menetelmällä saatuja taitekertoimia: mahtuvatko ne toistensa epävarmuusväleihin? Päällekkäiset välit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi. Kumpi menetelmä vaikutti luotettavammalta, ja miksi?

::: tuki O OO
**Vihjeitä.** Taittunut säde himmenee vähitellen, kun tulokulma lähestyy rajakulmaa, ja heijastunut säde kirkastuu. Etsi rajakulma lähestymällä sitä hitaasti kummastakin suunnasta ja normaalin kummallakin puolella. Epävarmuuden voit arvioida laskemalla taitekertoimen kulmilla $\alpha_\text{r} - \Delta\alpha_\text{r}$ ja $\alpha_\text{r} + \Delta\alpha_\text{r}$: epävarmuus on tulosten erotuksen puolikas.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
