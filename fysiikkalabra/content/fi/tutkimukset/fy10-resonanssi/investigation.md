# Äänen resonanssi putkessa

> **Tutkimuskysymys:** Millä ilmapatsaan pituuksilla putkessa syntyy resonanssi, ja kuinka suuri on äänen nopeus ilmassa resonanssikohtien perusteella?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydällä on vaakasuora läpinäkyvä putki kahden tuen varassa. Putken vasemman, avoimen pään edessä on pieni kaiutin, joka on johdoilla kytketty taajuusgeneraattoriin. Generaattorin näyttö on tyhjä. Putken sisällä on mäntä, jonka varsi tulee ulos oikeasta päästä. Putken alla kulkee mittanauha. Pöydällä on myös lämpömittari ja vihko mittaustuloksia varten." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-resonanssi-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

Pullon suulle puhallettu ääni, urkupillin sävel ja simpukankuoren kohina kuulostavat voimakkailta, koska putken tai pullon ilma alkaa värähdellä voimakkaasti tietyllä taajuudella. Tässä tutkimuksessa muutat putkessa olevan ilmapatsaan pituutta, etsit kohdat, joissa ääni voimistuu, ja määrität niiden avulla äänen nopeuden ilmassa. Mittaa, laske ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** millä ilmapatsaan pituuksilla resonanssi syntyy, kun äänilähteen taajuus pysyy samana, mikä on äänen aallonpituus usean resonanssikohdan perusteella ja kuinka suuri on äänen nopeus ilmassa epävarmuuksineen. Vertaa tulosta äänen nopeuden tunnettuun arvoon mittauslämpötilassa.

**Päätät itse (osittain ohjattu ja itsenäinen työtapa):** käytettävän taajuuden, sen, miten tunnistat resonanssikohdan (korvalla vai anturilla), kuinka monta resonanssikohtaa etsit ja kuinka monta kertaa toistat kunkin, miten määrität aallonpituuden mittaustuloksista sekä tavan, jolla arvioit tuloksen epävarmuuden. Ohjatussa työtavassa sivu kiinnittää useimmat näistä valinnoista. Osittain ohjatussa työtavassa sivu antaa resonanssin mallin ja ehdottaa käsittelytapoja ja epävarmuuden arviointitapoja, ja valitset niistä. Itsenäisessä työtavassa teet kaikki luetellut valinnat ja perustelet ne itse.

::: tuki I
**Itsenäinen työtapa.** Laajennus, mittaus usealla taajuudella, kuuluu työhösi.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Taajuus pysyy samana, ja ilmapatsasta pidennetään vähitellen ensimmäisen resonanssikohdan jälkeen. Missä kohdassa arvelet seuraavan resonanssin syntyvän, ja ovatko peräkkäiset resonanssikohdat mielestäsi tasavälein?
2. Jos taajuutta suurennetaan, siirtyvätkö resonanssikohdat lähemmäs toisiaan vai kauemmas toisistaan? Perustele.
3. Onko äänen nopeus ilmassa mielestäsi sama kaikilla taajuuksilla? Entä lämpimässä ja kylmässä huoneessa?
4. Kumpi on mielestäsi epätarkempaa: ilmapatsaan pituuden lukeminen asteikolta vai sen kohdan löytäminen, jossa ääni on voimakkain? Miten voisit pienentää tätä epävarmuutta?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Äänen nopeutta ei voi lukea suoraan mittarista. Ennen kuin luet eteenpäin, kirjaa:

1. Mistä suureista äänen nopeus voidaan laskea, ja mitkä niistä saat äänilähteestä ja mitkä mittaamalla?
2. Mitä muutat, mitä mittaat ja mitä pidät vakiona?
3. Mistä kohdasta mihin kohtaan ilmapatsaan pituus mitataan?

## Teoriaa lyhyesti

Ääni on ilmassa etenevää pitkittäistä aaltoliikettä: ilmahiukkaset värähtelevät edestakaisin aallon etenemissuunnassa, ja ilmanpaine vaihtelee tihentymien ja harvennusten mukana. Aallon etenemisnopeus $v$, taajuus $f$ ja aallonpituus $\lambda$ liittyvät toisiinsa yhtälöllä

```latex
v = f\lambda
```

Taajuuden määrää äänilähde. Äänen nopeus riippuu väliaineesta ja sen lämpötilasta: ilmassa ääni etenee sitä nopeammin, mitä lämpimämpää ilma on. Aallonpituus määräytyy taajuudesta ja nopeudesta. Aaltoliikettä ja ääntä käsitellään tarkemmin moduulissa FY5.

Putkeen kulkeva ääni heijastuu putken päästä, sekä suljetusta että avoimesta. Putkeen menevä ja heijastunut aalto kulkevat päällekkäin ja summautuvat. Tietyillä ilmapatsaan pituuksilla ne vahvistavat toisiaan niin, että putkeen syntyy **seisova aalto**: aaltokuvio ei etene, vaan ilma värähtelee jokaisessa kohdassa paikallaan, eri kohdissa eri amplitudilla. Kohtia, joissa ilma ei värähtele lainkaan, kutsutaan **solmuiksi**, ja kohtia, joissa se värähtelee voimakkaimmin, **kuvuiksi**. Vierekkäisten solmujen etäisyys on $\dfrac{\lambda}{2}$, ja solmun ja sen viereisen kuvun etäisyys on $\dfrac{\lambda}{4}$.

Suljetussa päässä, esimerkiksi männän tai vedenpinnan kohdalla, ilma ei pääse liikkumaan, joten siinä on solmu. Avoimessa päässä ilma pääsee liikkumaan vapaasti, joten siellä on kupu. Kupu ei ole tarkalleen putken suulla vaan hieman sen ulkopuolella; tämän siirtymän suuruus riippuu putken halkaisijasta. Kun ilmapatsaan pituus on sellainen, että seisova aalto syntyy, ilmapatsas värähtelee voimakkaasti äänilähteen tahdissa ja ääni voimistuu selvästi. Tätä kutsutaan **resonanssiksi**.

<svg data-fig="standing" viewBox="0 0 600 300" role="img" aria-label="Kaaviokuva seisovasta aallosta putkessa, jonka vasen pää on avoin ja oikea pää suljettu männällä. Vihreä alue näyttää, kuinka suurella amplitudilla ilma värähtelee eri kohdissa putkea. Männän pinnassa ilma ei värähtele: siinä on solmu. Toinen solmu on puolikkaan aallonpituuden päässä männästä. Avoimen pään lähellä, hieman putken ulkopuolella, ja solmujen puolivälissä on kupu, jossa ilma värähtelee voimakkaimmin. Vierekkäisten solmujen etäisyys on puolikas aallonpituutta." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-resonanssi-standing.webp" x="28.6" y="3.6" width="571.4" height="294" preserveAspectRatio="none"/>
  <foreignObject x="165" y="51.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{solmu}$</div></foreignObject>
  <foreignObject x="443" y="51.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{solmu}$</div></foreignObject>
  <foreignObject x="315" y="51.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kupu}$</div></foreignObject>
  <foreignObject x="64" y="51.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kupu}$</div></foreignObject>
  <foreignObject x="334" y="223" width="20" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\dfrac{\lambda}{2}$</div></foreignObject>
</svg>

::: tuki O OO
**Tarkista kirjauksesi tästä.** Äänen nopeus lasketaan yhtälöstä $v = f\lambda$. Taajuus $f$ luetaan äänilähteestä, ja aallonpituus $\lambda$ määritetään resonanssikohdista. Muutat ilmapatsaan pituutta $L$, mittaat ne pituudet, joilla resonanssi syntyy, ja pidät taajuuden samana koko mittaussarjan ajan. Pituus $L$ mitataan putken avoimesta päästä männän pintaan (tai vedenpintaan).

<svg data-fig="setup" viewBox="0 0 600 300" role="img" aria-label="Kaaviokuva. Vaakasuoran putken vasen pää on avoin, ja sen edessä on kaiutin, joka on kytketty taajuusgeneraattoriin. Generaattori antaa taajuuden f. Putken sisällä on mäntä, jota voi siirtää varresta. Ilmapatsaan pituus L mitataan putken avoimesta päästä männän pintaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-resonanssi-setup.webp" x="7.5" y="10" width="597" height="306" preserveAspectRatio="none"/>
  <foreignObject x="52.5" y="35.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kaiutin}$</div></foreignObject>
  <foreignObject x="95" y="230.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$f$</div></foreignObject>
  <foreignObject x="196" y="230.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{taajuusgeneraattori}$</div></foreignObject>
  <foreignObject x="375" y="35.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{mäntä}$</div></foreignObject>
  <foreignObject x="255" y="177.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$L$</div></foreignObject>
</svg>

**Resonanssin ehto.** Kun putken toinen pää on suljettu, ilmapatsaaseen täytyy mahtua solmusta kupuun matka $\dfrac{\lambda}{4}$, $\dfrac{3\lambda}{4}$, $\dfrac{5\lambda}{4}$ ja niin edelleen. Koska kupu on matkan $e$ verran putken suun ulkopuolella, resonanssipituudet ovat

```latex
L_n + e = (2n - 1)\cdot\frac{\lambda}{4}
```

missä $n = 1, 2, 3, \ldots$ on resonanssin järjestysluku, $L_n$ on $n$:s resonanssipituus lyhyimmästä alkaen ja $e$ kuvun etäisyys putken suulta, tavallisesti suunnilleen 0,6 kertaa putken säde. Samalla taajuudella putken suu käyttäytyy joka resonanssissa samoin, joten $e$ on kaikissa resonansseissa sama. Siirtymää $e$ ei kuitenkaan tunneta tarkasti.

<svg data-fig="resonances" viewBox="0 0 600 390" role="img" aria-label="Kaaviokuva kolmesta peräkkäisestä resonanssista samalla taajuudella. Kolme päällekkäistä putkea, joiden vasen pää on avoin. Ylimmässä mäntä on lähimpänä avointa päätä, ja ilmapatsaan pituus on L yksi; seuraavissa mäntä on kauempana, pituudet L kaksi ja L kolme. Kupu on matkan e verran putken suun ulkopuolella. Katkoviivat näyttävät männän paikat." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-resonanssi-resonances.webp" x="2.5" y="1.2" width="594.1" height="392.3" preserveAspectRatio="none"/>
  <foreignObject x="14" y="55.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n = 1$</div></foreignObject>
  <foreignObject x="197" y="99.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$L_1$</div></foreignObject>
  <foreignObject x="14" y="175.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n = 2$</div></foreignObject>
  <foreignObject x="347" y="219.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$L_2$</div></foreignObject>
  <foreignObject x="14" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n = 3$</div></foreignObject>
  <foreignObject x="497" y="339.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$L_3$</div></foreignObject>
  <foreignObject x="124" y="9.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$e$</div></foreignObject>
</svg>

Jos putken molemmat päät ovat avoimia ja pituutta muutetaan esimerkiksi sisäkkäisillä putkilla, molemmissa päissä on kupu, ja ehto on $L_n + 2e = n\cdot\dfrac{\lambda}{2}$. Selvitä, kummanlainen putki sinulla on.
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona, kuinka monta resonanssikohtaa etsit ja miten tunnistat resonanssin.

::: tuki O
**Ohjattu.** Käytä opettajan ehdottamaa taajuutta tai valitse taajuus, jolla putkeen mahtuu ainakin kolme resonanssikohtaa: kokeile ensin liikuttamalla mäntää koko putken matkan. Jos kohtia on vähemmän kuin kolme, suurenna taajuutta. Kirjaa taajuus generaattorin näytöltä ja pidä se samana koko sarjan ajan. Aseta kaiutin putken avoimen pään eteen lähelle suuta mutta ei tiiviisti kiinni. Etsi kukin resonanssikohta kaksi kertaa: kerran ilmapatsasta pidentäen ja kerran lyhentäen. Mittaa myös huoneen lämpötila.
:::

::: tuki OO
**Osittain ohjattu.** Muutat ilmapatsaan pituutta samalla taajuudella. Päätä itse taajuus, resonanssikohtien määrä, toistojen määrä ja se, tunnistatko resonanssin korvalla vai anturilla. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Miten varmistat, ettet ohita lyhyintä resonanssikohtaa?
- Mistä tiedät, että taajuus pysyy samana koko sarjan ajan?
- Jos käytät mikrofonia tai anturia, missä se on, ja pysyykö se samassa kohdassa koko sarjan ajan?
- Miksi resonanssikohta kannattaa etsiä sekä pidentäen että lyhentäen?
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana. Kirjaa myös taajuus ja huoneen lämpötila. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle.

::: tuki O
Voit käyttää esimerkiksi tällaista taulukkoa. Lisää rivejä, jos putkeen mahtuu useampia resonanssikohtia. Alaindeksi $\text{pit}$ tarkoittaa ilmapatsaan pidentämistä ja $\text{lyh}$ sen lyhentämistä.

| $n$ | $L_\text{pit}\ (\text{m})$ | $L_\text{lyh}\ (\text{m})$ | $\bar{L}_n\ (\text{m})$ |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

Liikuta mäntää hitaasti ja pysähdy kohtaan, jossa ääni on voimakkain. Lue pituus putken suulta männän pintaan ja katso asteikkoa kohtisuoraan. Tarkista, että peräkkäisten kohtien välit ovat suunnilleen yhtä suuret: jos jokin väli on noin kaksi kertaa muita suurempi, olet ohittanut yhden resonanssin.
:::

Muista mittausepävarmuus: kirjaa, kuinka tarkasti voit lukea pituuden ja kuinka tarkasti löydät resonanssikohdan. Kirjaa myös, kuinka tarkasti taajuus tunnetaan; sen kertoo laitteen ohje tai opettaja. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Määritä aallonpituus useasta resonanssikohdasta, ei yhdestä, ja laske siitä äänen nopeus. Vastaa:

1. Ovatko mittaamasi resonanssikohdat tasavälein? Perustele seisovan aallon solmujen ja kupujen avulla, kuinka suuri peräkkäisten resonanssikohtien etäisyys on aallonpituuteen verrattuna.
2. Miksi aallonpituus kannattaa määrittää resonanssikohtien erotuksista eikä yhdestä resonanssipituudesta? Perustele putken suun ja kuvun avulla.
3. Miksi monen resonanssikohdan käyttäminen parantaa tulosta verrattuna kahteen vierekkäiseen kohtaan?

::: tuki O OO
**Kaksi tapaa käsitellä tuloksia.** Kirjoita resonanssin ehto kahdelle peräkkäiselle resonanssille ja vähennä yhtälöt toisistaan: mitä tapahtuu siirtymälle $e$? Sen jälkeen voit käyttää jompaakumpaa tapaa:

- **Erotus kauimmaisista kohdista.** Kun olet löytänyt $N$ resonanssikohtaa, ensimmäisen ja viimeisen välissä on $N - 1$ puolikasta aallonpituutta:

```latex
\frac{\lambda}{2} = \frac{\bar{L}_N - \bar{L}_1}{N - 1}
```

- **Kuvaaja.** Piirrä resonanssipituus $\bar{L}_n$ järjestysluvun $n$ funktiona ja sovita pisteisiin suora. Mallin mukaan kulmakerroin on $\dfrac{\lambda}{2}$. [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

<svg data-fig="model" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja: resonanssipituus L järjestysluvun n funktiona mallin mukaan, kun taajuus pysyy samana. Kuvaaja on suora, jonka kulmakerroin on puolikas aallonpituutta. Kun n kasvaa yhdellä, L kasvaa puolikkaan aallonpituuden verran. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="280" x2="484" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,280 L483,286 L483,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="172.5" y1="280" x2="172.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="162.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="255" y1="280" x2="255" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="245" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="338" y1="280" x2="338" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="328" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="420.5" y1="280" x2="420.5" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="410.5" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n$</div></foreignObject>
  <foreignObject x="104" y="15.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$L$</span></div></foreignObject>
  <polyline points="148,274.5 445,92.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="255" y1="208.5" x2="338" y2="208.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="338" y1="208.5" x2="338" y2="158" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="286.5" y="216" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1$</div></foreignObject>
  <foreignObject x="348" y="154.5" width="20" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\dfrac{\lambda}{2}$</div></foreignObject>
  <foreignObject x="112.5" y="62.5" width="170" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kulmakerroin } \dfrac{\lambda}{2}$</div></foreignObject>
</svg>

Mitä suoran vakiotermi kertoo? Vihje: sijoita resonanssin ehtoon $n = 0$. Kuvaajan sovitukseen käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].
:::

::: tuki O
**Ohjattu.** Laske aallonpituus kauimmaisten resonanssikohtien erotuksesta. Jos käytössäsi on sovitusohjelma, tarkista tulos lisäksi kuvaajasta. Laske lopuksi äänen nopeus yhtälöstä $v = f\lambda$.
:::

## Epävarmuus ja luotettavuus

Ilmoita äänen nopeus muodossa lukuarvo $\pm$ epävarmuus yksikköineen, esimerkiksi $v = (\ldots \pm \ldots)\,\text{m/s}$, ja perustele, miten arvioit epävarmuuden $\Delta v$.

::: tuki O OO
**Resonanssikohdan epävarmuus.** Kun olet etsinyt saman kohdan useamman kerran, esimerkiksi pidentäen ja lyhentäen, voit arvioida sen epävarmuuden lukemien vaihteluvälin puolikkaana. Jos se on pienempi kuin asteikon lukemisen tarkkuus, käytä lukemisen tarkkuutta.

**Aallonpituuden epävarmuus.** Erotuksen epävarmuus on erotettavien epävarmuuksien summa, joten kauimmaisista kohdista laskettaessa

```latex
\Delta\!\left(\frac{\lambda}{2}\right) = \frac{\Delta L_N + \Delta L_1}{N - 1}
```

ja $\Delta\lambda$ on tämän kaksinkertainen. Kuvaajaa käytettäessä kulmakertoimen epävarmuuden saat sovitusohjelman keskivirheestä tai jyrkimmän ja loivimman pisteisiin sopivan suoran kulmakertoimista.

**Nopeuden epävarmuus.** Tulon suhteellinen epävarmuus on tekijöiden suhteellisten epävarmuuksien summa:

```latex
\frac{\Delta v}{v} = \frac{\Delta f}{f} + \frac{\Delta \lambda}{\lambda}
```

Pyöristä $\Delta v$ yhteen merkitsevään numeroon ja $v$ samaan desimaaliin.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet tulosta? Vaikuttaako resonanssikohtien määrä tuloksen epävarmuuteen? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Vertaa saamaasi äänen nopeutta tunnettuun arvoon mittauslämpötilassa ja kerro, mistä lähteestä tunnettu arvo on: onko tunnettu arvo tuloksesi epävarmuusvälillä? Päällekkäisyys tarkoittaa, että tulokset ovat sopusoinnussa, ei sitä, että ne on todistettu samoiksi. Jos ero on epävarmuutta suurempi, mikä sen voisi selittää? Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

::: tuki O OO
**Tunnettu arvo.** Kuivassa ilmassa äänen nopeus riippuu lämpötilasta likimain yhtälön

```latex
v = 331{,}3\,\text{m/s}\cdot\sqrt{\frac{T}{273{,}15\,\text{K}}}
```

mukaan, missä $T$ on ilman lämpötila kelvineinä: $T = \left(\dfrac{\theta}{{}^\circ\text{C}} + 273{,}15\right)\,\text{K}$, missä $\theta$ on celsiuslämpötila. Ilman kosteus suurentaa äänen nopeutta hieman.
:::

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** seisova aalto putkessa, resonanssin ehto ja yhtälö $v = f\lambda$.
- **Koejärjestely ja menetelmä:** mitä muutit, mitä mittasit ja mitä pidit vakiona, mistä mihin pituus mitattiin ja miten tunnistit resonanssin.
- **Mittaustulokset:** jokainen resonanssikohdan lukema omassa sarakkeessaan, keskiarvot niiden oikealla puolella sekä taajuus ja lämpötila.
- **Tulos:** äänen nopeus muodossa lukuarvo $\pm$ epävarmuus yksikköineen oikein pyöristettynä ja vertailu tunnettuun arvoon lähteineen.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet ja niiden vaikutuksen suunta sekä perustelu sille, miksi käytit useaa resonanssikohtaa.

## Laajennus: riippuuko äänen nopeus taajuudesta?

Toista mittaus usealla eri taajuudella ja määritä aallonpituus jokaisella. Jos äänen nopeus ei riipu taajuudesta, yhtälöstä $v = f\lambda$ saadaan

```latex
\lambda = v\cdot\frac{1}{f}
```

joten aallonpituus taajuuden käänteisluvun funktiona on origon kautta kulkeva suora, jonka kulmakerroin on äänen nopeus $v$.

<svg data-fig="frequency" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja: aallonpituus lambda taajuuden käänteisluvun yksi per f funktiona mallin mukaan, jos äänen nopeus ei riipu taajuudesta. Kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on äänen nopeus v. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="280" x2="484" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,280 L483,286 L483,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="251" width="20" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\dfrac{1}{f}$</div></foreignObject>
  <foreignObject x="104" y="15.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\lambda$</span></div></foreignObject>
  <polyline points="90,280 451,83.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="134" y="86" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kulmakerroin } v$</div></foreignObject>
</svg>

Määritä äänen nopeus tästä kuvaajasta ja vertaa sitä yhdellä taajuudella saamaasi tulokseen epävarmuuksineen. Ovatko pisteet suoralla, ja kulkeeko suora origon kautta? Mitä tuloksesi kertoo ennusteestasi 3?

::: tuki O OO
**Vihjeitä.** Valitse taajuudet niin, että jokaisella löydät putkesta ainakin kaksi resonanssikohtaa. Mittaa huoneen lämpötila jokaisen sarjan alussa, ettei lämpötilan muutos sekoitu taajuuden vaikutukseen.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi mittaustuloksiin vai siihen, mitä odotit tunnetun arvon olevan?
- Mitä tekisit toisin, jos aloittaisit alusta?
