# Planckin vakio LEDien avulla

> **Tutkimuskysymys:** Miten LEDin kynnysjännite riippuu sen lähettämän valon aallonpituudesta, ja kuinka suuri Planckin vakio on tämän perusteella?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydällä on pienjännitelähde, säädettävä liukuvastus ja kaksi yleismittaria, joiden näytöissä ei ole lukemia. Johdot kulkevat kytkentäalustalle, jossa yksi LED loistaa himmeästi. Pöydällä on rasia, jossa on erivärisiä sammuneita LEDejä, sekä LEDien tietolehti ja vihko." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-planck-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

Planckin vakio on yksi luonnon perusvakioista: se kertoo, kuinka suuri energia valon pienimmällä osalla, fotonilla, on. Vakion voi määrittää koulun laboratoriossa tavallisilla LEDeillä ja kahdella yleismittarilla. Tässä tutkimuksessa mittaat usean erivärisen LEDin sähköisiä ominaisuuksia ja päättelet niistä Planckin vakion. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** kuinka suuri kynnysjännite on usealla erivärisellä LEDillä, miten se riippuu LEDin valon aallonpituudesta ja kuinka suuri Planckin vakio on tämän perusteella epävarmuuksineen. Vertaa tulosta Planckin vakion tunnettuun arvoon.

**Päätät itse** (osittain ohjattu ja itsenäinen työtapa): kuinka monta LEDiä ja mittauspistettä käytät ja millä jännitealueella mittaat opettajan ilmoittaman virtarajan sisällä, miten määrität kynnysjännitteen, kuvaajan akselit perusteluineen sekä tavan, jolla arvioit tuloksen epävarmuuden. Ohjatussa työtavassa sivu kiinnittää nämä valinnat. Osittain ohjatussa työtavassa sivu antaa vaihtoehdot kynnysjännitteen määrittämiseen ja epävarmuuden arvioimiseen, ja valitset niistä perustellen. Itsenäisessä työtavassa valitset ja perustelet kaiken itse.

::: tuki I
**Itsenäinen työtapa.** Jos koulussa on hila tai spektrometri, laajennus kuuluu työhösi: mittaa ainakin yhden LEDin aallonpituus itse ja vertaa sitä tietolehden arvoon.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Kun LEDin jännitettä kasvatetaan nollasta alkaen, miten arvelet sen läpi kulkevan sähkövirran muuttuvan? Alkaako LED loistaa heti?
2. Kummalla arvelet olevan suuremman kynnysjännitteen, punaisella vai sinisellä LEDillä?
3. Jos LEDin valon aallonpituus olisi kaksi kertaa niin suuri, mitä arvelet tapahtuvan kynnysjännitteelle?
4. Kuinka lähelle tunnettua arvoa arvelet pääseväsi, ja mikä mittauksessa on todennäköisesti suurin epävarmuuden lähde?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Teoriaa lyhyesti

Tämän työn fysiikkaa käsitellään tarkemmin moduuleissa FY6–FY8, joita ei ole vielä julkaistu Ruukkilabrassa. Tässä on se, mitä tutkimuksessa tarvitset.

**Fotoni.** Valo siirtää energiaa pieninä paloina, fotoneina. Fotonin energia on

```latex
E = hf
```

missä $E$ on fotonin energia, $f$ valon taajuus ja $h$ **Planckin vakio**, jonka yksikkö on $\text{J}\cdot\text{s}$. Valon taajuus ja aallonpituus $\lambda$ liittyvät toisiinsa yhtälöllä $c = f\lambda$, missä $c$ on valon nopeus tyhjiössä. Kun aallonpituus tunnetaan, taajuus on $f = \dfrac{c}{\lambda}$.

**Varaus ja jännite.** Kun varattu hiukkanen siirtyy jännitteen $U$ yli, sen energia muuttuu määrällä $qU$. Elektronin varauksen suuruus on alkeisvaraus $e$, joten elektronin energia muuttuu määrällä $eU$.

**LED.** LED eli hohtodiodi on puolijohdekomponentti, joka johtaa sähkövirtaa hyvin vain yhteen suuntaan, päästösuuntaan. Kun virta kulkee LEDin läpi päästösuuntaan, elektronit menettävät puolijohteessa energiaa, ja energia voi vapautua fotonina. Fotonin energia ja siten valon väri määräytyvät LEDin puolijohdemateriaalista: fotonin energia on suunnilleen yhtä suuri kuin materiaalin energia-aukko eli energiaero, jonka elektroni menettää, ja kynnysjännitteestä laskettu energia $eU_\text{k}$ on vain likiarvo sille. LED alkaa johtaa sähkövirtaa ja lähettää valoa vasta, kun sen jännite on riittävän suuri. Jännitettä, jolla tämä alkaa, kutsutaan tässä työssä **kynnysjännitteeksi** $U_\text{k}$.

**Periaate.** Elektroni voi tuottaa fotonin vain, jos sillä on vähintään fotonin energia. Siksi LED alkaa loistaa suunnilleen silloin, kun yhden elektronin energia $eU_\text{k}$ on yhtä suuri kuin yhden fotonin energia:

```latex
eU_\text{k} \approx hf
```

Yhteys on vain likimääräinen, ja sen ehdot kannattaa pitää mielessä koko työn ajan: LED ei lähetä yhtä ainoaa aallonpituutta vaan kapean aallonpituusalueen, kynnysjännitteen arvo riippuu siitä, miten se määritetään, osa LEDin jännitteestä kuluu sen sisäiseen resistanssiin, ja LEDin lämpeneminen muuttaa sen ominaisuuksia. Vakiot $e = 1{,}602\,176\,634\cdot10^{-19}\,\text{C}$ ja $c = 2{,}997\,924\,58\cdot10^{8}\,\text{m/s}$ ovat tarkkoja määriteltyjä arvoja.

::: tuki O
**Malli kuvaajaksi.** Kun periaatteeseen sijoitetaan $f = \dfrac{c}{\lambda}$ ja ratkaistaan kynnysjännite, saadaan

```latex
U_\text{k} = \frac{hc}{e}\cdot\frac{1}{\lambda}
```

Kynnysjännite on siis mallin mukaan suoraan verrannollinen aallonpituuden käänteislukuun $\dfrac{1}{\lambda}$. Kuvaaja $U_\text{k}$ suureen $\dfrac{1}{\lambda}$ funktiona on suora, jonka kulmakerroin on $k = \dfrac{hc}{e}$. Planckin vakio saadaan kulmakertoimesta:

```latex
h = \frac{ek}{c}
```

<svg data-fig="model" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja: kynnysjännite U k aallonpituuden käänteisluvun yksi per lambda funktiona mallin mukaan. Kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on h kertaa c jaettuna e:llä. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="280" x2="484" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,280 L483,286 L483,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="251" width="20" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\dfrac{1}{\lambda}$</div></foreignObject>
  <foreignObject x="104" y="15.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$U_\text{k}$</span></div></foreignObject>
  <polyline points="90,280 451,83.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="127.5" y="76" width="183" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kulmakerroin } \dfrac{hc}{e}$</div></foreignObject>
</svg>

Jos kaikkien LEDien kynnysjännitteissä on suunnilleen sama lisäosa, esimerkiksi määritystavasta johtuen, suora siirtyy ylös tai alas eikä kulje origon kautta, mutta kulmakerroin ei muutu. Siksi Planckin vakio kannattaa määrittää kulmakertoimesta eikä yksittäisen LEDin tuloksesta. Eri puolijohdemateriaaleista tehdyillä LEDeillä lisäosa voi kuitenkin olla erisuuruinen, ja silloin se muuttaa myös kulmakerrointa. Mittaamalla selviää, kuinka hyvin malli pätee.
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona. Piirrä kytkentäkaavio ja näytä kytkentä opettajalle ennen kuin kytket virran. LEDin kanssa sarjassa on aina oltava vastus, joka rajoittaa sähkövirtaa. Jos säädettävän vastuksen voi säätää nollaan, kytke sen lisäksi sarjaan kiinteä suojavastus, jonka opettaja antaa. Kirjaa myös, mistä saat LEDien aallonpituudet: ne luetaan LEDien tietolehdistä, tai mittaat ne itse spektrometrillä tai hilalla, jos sellainen on käytettävissä (katso laajennus). Älä arvaa aallonpituutta värin perusteella.

::: tuki O
**Ohjattu.** Mittaat jokaisesta LEDistä sarjan, jossa muutat LEDin jännitettä $U$ säätämällä virtalähdettä tai säädettävää vastusta ja luet joka kerta jännitteen $U$ ja sähkövirran $I$. Kynnysjännitteen määrität myöhemmin näistä mittauksista. Käytä kaikkia opettajan antamia erivärisiä LEDejä, joiden aallonpituus tiedetään, mieluiten ainakin neljää. Mittaa jokaisesta LEDistä ainakin kahdeksan pistettä: muutama jännitteillä, joilla virtaa ei juuri kulje, ja ainakin viisi alueelta, jolla virta kasvaa jyrkästi. Vakiona pidät kytkennän, mittarit ja niiden mittausalueet sekä tavan, jolla mittaat.
:::

::: tuki OO
**Osittain ohjattu.** Muuttuja on LEDin väri eli aallonpituus, ja jokaisesta LEDistä mittaat jännitteen ja sähkövirran. Päätä itse, kuinka monta LEDiä ja mittauspistettä käytät ja millä jännitealueella mittaat. Valitse kynnysjännitteen määritystapa kohdassa Käsittele tulokset annetuista vaihtoehdoista. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Tarkista kytkentäsi tästä:

<svg data-fig="setup" viewBox="0 0 600 400" role="img" aria-label="Kytkentäkaavio. Tasajännitelähteen plusnavasta virta kulkee kiinteän suojavastuksen R s ja säädettävän vastuksen R kautta LEDiin ja siitä virtamittarin kautta takaisin miinusnapaan. LED on kytketty päästösuuntaan. Vastukset rajoittavat virtaa, ja virtamittari on sarjassa LEDin kanssa ja mittaa sähkövirran I. Jännitemittari on kytketty suoraan LEDin napoihin eli rinnan LEDin kanssa, ja se mittaa LEDin jännitteen U." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-planck-setup.webp" x="1.2" y="0" width="597" height="404.2" preserveAspectRatio="none"/>
  <foreignObject x="65" y="158" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{tasa-}$</div></foreignObject>
  <foreignObject x="49.5" y="184" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{jännite-}$</div></foreignObject>
  <foreignObject x="65" y="210" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{lähde}$</div></foreignObject>
  <foreignObject x="111" y="91" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:22px">$+$</div></foreignObject>
  <foreignObject x="111" y="283" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:22px">$-$</div></foreignObject>
  <foreignObject x="208.5" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <foreignObject x="345" y="19.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <foreignObject x="280" y="347.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I$</div></foreignObject>
  <foreignObject x="280.5" y="307" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{A}$</div></foreignObject>
  <foreignObject x="520.5" y="187" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{V}$</div></foreignObject>
  <foreignObject x="562" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="333" y="188" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px;color:#6b7480">$\text{LED}$</div></foreignObject>
</svg>

Mieti ainakin näitä:

- Miksi jännitemittari kytketään suoraan LEDin napoihin eikä virtalähteen napoihin?
- Kumpi LEDin jaloista kytketään plusnapaan päin? Yleensä pidempi jalka on plusnapaan kytkettävä anodi, mutta tarkista asia opettajalta tai tietolehdestä.
- Miten varmistat, että virta pysyy opettajan ilmoittaman rajan alapuolella, vaikka säädät vastusta?
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana: jokaiselle LEDille oma mittaussarja, ja lisäksi jokaisen LEDin väri ja aallonpituus sekä tieto siitä, mistä aallonpituus on peräisin. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle.

Pidä virta koko ajan opettajan ilmoittaman rajan alapuolella, äläkä katso suoraan kirkkaasti loistavaan LEDiin. UV- ja infrapuna-LEDiin ei katsota koskaan suoraan, ja UV-LEDin kanssa käytetään opettajan antamia silmäsuojaimia.

::: tuki O
Voit käyttää jokaiselle LEDille esimerkiksi tällaista taulukkoa:

| $U\ (\text{V})$ | $I\ (\text{mA})$ |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |

Kokoa lopuksi kaikkien LEDien tulokset yhteen taulukkoon:

| LED | $\lambda\ (\text{nm})$ | $\dfrac{1}{\lambda}\ \left(\dfrac{1}{\text{m}}\right)$ | $U_\text{k}\ (\text{V})$ |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

Aloita jännitteestä nolla ja kasvata sitä pienin askelin. Kun virta alkaa kasvaa, pienennä askelia. Lopeta sarja, kun virta lähestyy opettajan ilmoittamaa rajaa. Lue mittarit vasta, kun lukemat ovat asettuneet, ja mittaa sarja ripeästi, ettei LED ehdi lämmetä. Katkaise virta aina, kun vaihdat LEDiä.
:::

Muista mittausepävarmuus: kirjaa mittareiden lukematarkkuus ja aallonpituuden epävarmuus, eli tietolehden ilmoittama vaihteluväli tai oma arviosi. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Käsittele tulokset kahdessa vaiheessa. Merkitse kaikkien kuvaajien akseleille suureet ja yksiköt, piirrä mittauspisteet, älä yhdistä niitä murtoviivalla, ja sovita suora vain niihin pisteisiin, joihin se mallin mukaan kuuluu. [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

1. Piirrä jokaisen LEDin mittauksista virta–jännite-kuvaaja ja määritä siitä LEDin kynnysjännite. Kirjaa, miten määritit sen, ja perustele, miksi juuri tämä tapa kuvaa jännitettä, jolla LED alkaa lähettää fotoneja.
2. Muunna aallonpituudet metreiksi. Piirrä kaikkien LEDien tuloksista kuvaaja, josta Planckin vakio saadaan kulmakertoimen avulla, ja perustele, miksi valitsit juuri nämä akselit.
3. Millainen riippuvuus pisteistä näkyy? Jos sovitit pisteisiin suoran, kirjoita sen yhtälö ja pohdi, mistä mahdollinen vakiotermi voi johtua.
4. Mikä on kulmakertoimen yksikkö? Laske Planckin vakio kulmakertoimesta ja tarkista, että yksiköksi tulee $\text{J}\cdot\text{s}$.

::: tuki O OO
**Kynnysjännitteen määrittäminen.** LEDin virta–jännite-kuvaaja on mallin mukaan tämän muotoinen:

<svg data-fig="iu" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja: LEDin sähkövirta I jännitteen U funktiona mallin mukaan. Pienillä jännitteillä virta on lähes nolla. Tietyn jännitteen jälkeen virta kasvaa jyrkästi ja lähes suoraviivaisesti. Jyrkän osan suora on jatkettu katkoviivalla vaaka-akselille, ja leikkauskohta on merkitty kynnysjännitteeksi U k. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="280" x2="484" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,280 L483,286 L483,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="104" y="15.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$I$</span></div></foreignObject>
  <polyline points="90,280 92.5,280 95.5,280 98,280 100.5,280 103.5,280 106,280 108.5,280 111.5,280 114,280 116.5,280 119.5,280 122,280 124.5,280 127,280 130,280 132.5,280 135,280 138,280 140.5,280 143,280 146,280 148.5,280 151,280 154,280 156.5,280 159,280 162,280 164.5,280 167,280 170,280 172.5,280 175,280 178,280 180.5,280 183,280 186,280 188.5,280 191,280 193.5,280 196.5,280 199,280 201.5,280 204.5,280 207,280 209.5,280 212.5,280 215,280 217.5,280 220.5,280 223,280 225.5,280 228.5,280 231,280 233.5,280 236.5,280 239,279.5 241.5,279.5 244.5,279.5 247,279.5 249.5,279.5 252.5,279 255,279 257.5,279 260,278.5 263,278.5 265.5,278 268,277.5 271,277 273.5,276.5 276,275.5 279,275 281.5,274 284,272.5 287,271.5 289.5,269.5 292,268 295,266 297.5,263.5 300,261 303,258 305.5,255 308,252 311,248.5 313.5,244.5 316,240.5 319,236.5 321.5,232 324,228 326.5,223.5 329.5,218.5 332,214 334.5,209 337.5,204.5 340,199.5 342.5,194.5 345.5,189.5 348,184.5 350.5,179.5 353.5,174.5 356,169 358.5,164 361.5,159 364,154 366.5,149 369.5,143.5 372,138.5 374.5,133.5 377.5,128.5 380,123 382.5,118 385.5,113 388,107.5 390.5,102.5 393,97.5 396,92.5 398.5,87 401,82 404,77 406.5,71.5 409,66.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="299,280 417,52" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="7 5"/>
  <line x1="299" y1="272" x2="299" y2="288" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="282.5" y="289.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U_\text{k}$</div></foreignObject>
  <foreignObject x="101" y="102.5" width="164" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px;color:#6b7480">$\text{jyrkän osan suora}$</div></foreignObject>
  <line x1="268.5" y1="119" x2="363.5" y2="151" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
</svg>

Kynnysjännitteen voi määrittää esimerkiksi näillä tavoilla:

- **Jyrkän osan suora.** Sovita suora virta–jännite-kuvaajan jyrkästi nousevaan, lähes suoraan osaan ja jatka sitä vaaka-akselille. Leikkauskohdan jännite on kynnysjännite. Tapa käyttää monta mittauspistettä, joten yksittäisen lukeman virhe vaikuttaa vähemmän.
- **Valon syttyminen.** Kasvata jännitettä hämärässä huoneessa hitaasti ja kirjaa jännite, jolla LEDistä näkyy ensimmäinen heikko valo. Tapa on nopea, mutta tulos riippuu katsojan silmästä ja huoneen valaistuksesta. Tapa sopii vain näkyvää valoa lähettäville LEDeille: infrapuna-LEDin valoa ei näe lainkaan, eikä UV- tai infrapuna-LEDiin katsota koskaan suoraan.
- **Pieni sovittu virta.** Kirjaa jännite, jolla virta saavuttaa saman pienen arvon jokaisella LEDillä. Tapa on johdonmukainen, mutta tulos riippuu valitusta virrasta.

Käytä samaa tapaa kaikilla LEDeillä.
:::

::: tuki O
Määritä kynnysjännite jyrkän osan suoran avulla. Valitse virta–jännite-kuvaajassa pystyakselille virta $I$ ja vaaka-akselille jännite $U$. Valitse yhteisessä kuvaajassa pystyakselille kynnysjännite $U_\text{k}$ ja vaaka-akselille $\dfrac{1}{\lambda}$.
:::

::: tuki O OO
**Tarkista vastauksesi tästä: miksi juuri nämä akselit?** Kun periaatteeseen $eU_\text{k} \approx hf$ sijoitetaan $f = \dfrac{c}{\lambda}$ ja ratkaistaan kynnysjännite, saadaan

```latex
U_\text{k} = \frac{hc}{e}\cdot\frac{1}{\lambda}
```

Tämä on suoran yhtälö $y = kx$, kun pystyakselille valitaan $U_\text{k}$ ja vaaka-akselille $\dfrac{1}{\lambda}$. Silloin kulmakerroin on $k = \dfrac{hc}{e}$, sen yksikkö on $\text{V}\cdot\text{m}$, ja Planckin vakio on $h = \dfrac{ek}{c}$. Jos vaaka-akselille valittaisiin aallonpituus $\lambda$, pisteet asettuisivat käyrälle eikä suoralle. Toinen hyvä valinta on pystyakselille fotonin energia $eU_\text{k}$ ja vaaka-akselille taajuus $f = \dfrac{c}{\lambda}$: silloin kulmakerroin on suoraan $h$. Aallonpituus muunnetaan metreiksi ennen käänteisluvun laskemista: $1\,\text{nm} = 10^{-9}\,\text{m}$.

Tarkista vielä kuvaajastasi: ovatko pisteet suoralla, ja kulkeeko suora origon kautta? Jos kaikkien LEDien kynnysjännitteissä on sama lisäosa, suora siirtyy ylös tai alas, mutta kulmakerroin ei muutu. Eri materiaaleista tehdyillä LEDeillä lisäosa voi olla erisuuruinen, ja silloin se muuttaa myös kulmakerrointa.
:::

Kuvaajien piirtämiseen ja sovitukseen käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Ilmoita Planckin vakio muodossa $h = (h \pm \Delta h)\,\text{J}\cdot\text{s}$ ja perustele, miten arvioit epävarmuuden $\Delta h$.

::: tuki O OO
Koska $e$ ja $c$ ovat tarkkoja arvoja, Planckin vakion suhteellinen epävarmuus on sama kuin kulmakertoimen: $\dfrac{\Delta h}{h} = \dfrac{\Delta k}{k}$. Kulmakertoimen epävarmuuden voit arvioida jommallakummalla tavalla:

- **Sovitusohjelman keskivirhe.** Monet ohjelmat ilmoittavat kulmakertoimen keskivirheen. Käytä sitä epävarmuutena $\Delta k$.
- **Jyrkin ja loivin suora.** Piirrä jyrkin ja loivin suora, jotka vielä sopivat pisteisiin niiden epävarmuuksien rajoissa. Määritä niiden kulmakertoimet $k_\text{max}$ ja $k_\text{min}$ ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta k = \dfrac{k_\text{max} - k_\text{min}}{2}$.

Pisteiden epävarmuudet saat näin. Kynnysjännitteen epävarmuuden voit arvioida sovittamalla jyrkkään osaan jyrkimmän ja loivimman sopivan suoran ja katsomalla, kuinka paljon niiden leikkauskohdat eroavat. Suureen $\dfrac{1}{\lambda}$ suhteellinen epävarmuus on sama kuin aallonpituuden: $\dfrac{\Delta(1/\lambda)}{1/\lambda} = \dfrac{\Delta\lambda}{\lambda}$.

Pyöristä $\Delta h$ yhteen merkitsevään numeroon ja $h$ samaan tarkkuuteen.
:::

::: tuki O
Ohjatussa työtavassa käytä kulmakertoimen epävarmuutena jyrkimmän ja loivimman suoran menetelmää.
:::

Vertaa tulosta Planckin vakion tunnettuun arvoon $h = 6{,}626\,070\,15\cdot10^{-34}\,\text{J}\cdot\text{s}$. Laske, kuinka monta prosenttia tuloksesi poikkeaa siitä, ja tarkista, mahtuuko tunnettu arvo epävarmuusvälisi sisään.

Pohdi sitten luotettavuutta konkreettisesti: mitkä tekijät aiheuttivat mittausepävarmuutta, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan systemaattiset virheet olisivat muuttaneet tulosta? Jos tunnettu arvo jää epävarmuusvälisi ulkopuolelle, ero ei selity pelkillä lukematarkkuuksilla: mieti, mitkä Teoriaa lyhyesti -kohdan mallin ehdoista eivät ehkä täyttyneet. Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Viittaa kuvaajiin, esimerkiksi "kuvaajasta 2 nähdään, että …". Vastaa lisäksi:

- Millä perusteella LEDin kynnysjännite voidaan määrittää, ja olisiko toinen määritystapa voinut muuttaa tulosta?
- Kuinka hyvin LEDin lähettämän fotonin energiaa voidaan arvioida kynnysjännitteen avulla? Laske jokaiselle LEDille fotonin energia $\dfrac{hc}{\lambda}$ Planckin vakion tunnetulla arvolla ja vertaa sitä energiaan $eU_\text{k}$.
- Onko ero tuloksesi ja tunnetun arvon välillä mittausepävarmuuden rajoissa, vai viittaako se mallin likimääräisyyteen?

Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** fotonin energia, periaate $eU_\text{k} \approx hf$ ehtoineen ja perustelu kuvaajan akseleille.
- **Koejärjestely ja menetelmä:** kytkentäkaavio, mistä LEDien aallonpituudet ovat peräisin ja miten määritit kynnysjännitteen.
- **Mittaustulokset:** jokaisen LEDin mittaussarja omana taulukkonaan ja yhteenvetotaulukko, jossa johdetut suureet ovat mitattujen oikealla puolella.
- **Tulos:** $h = (h \pm \Delta h)\,\text{J}\cdot\text{s}$ oikein pyöristettynä ja poikkeama tunnetusta arvosta.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet, niiden vaikutuksen suunta ja mallin rajat.

## Laajennus: aallonpituudet itse hilalla

Tietolehden aallonpituuden sijasta voit mitata LEDin aallonpituuden itse. Spektrometri näyttää valon aallonpituusjakauman suoraan, jos koulussa on sellainen. Hilassa on tiheässä hyvin kapeita rakoja, ja se taivuttaa eri aallonpituuksia eri suuntiin. Lähin sivukuva eli ensimmäisen kertaluvun kuva syntyy kulmaan $\theta$, jolle pätee

```latex
d\sin\theta = \lambda
```

missä $d$ on hilan kahden vierekkäisen raon välimatka eli hilavakio ja $\lambda$ valon aallonpituus. Jos hilaan on merkitty rakojen määrä millimetrillä $N$, hilavakio on $d = \dfrac{1\,\text{mm}}{N}$. Hilaa ja valon diffraktiota käsitellään tarkemmin moduulissa FY7.

<svg data-fig="grating" viewBox="0 0 600 360" role="img" aria-label="Kaaviokuva ylhäältä. Vasemmalla on kapea rako, jonka takana on LED, ja raon kohdalla poikittainen mitta-asteikko. Oikealla etäisyydellä L asteikosta on hila ja sen takana silmä. Valo kulkee raosta suoraan hilaan. Silmä näkee raon värillisen kuvan asteikolla etäisyydellä x raosta, suunnassa, joka poikkeaa kulman theta verran raon suunnasta." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-planck-grating.webp" x="0" y="-1.2" width="600" height="366.2" preserveAspectRatio="none"/>
  <foreignObject x="4" y="239" width="36" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:18px;color:#6b7480">$\text{LED}$</div></foreignObject>
  <foreignObject x="480" y="134" width="50" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{hila}$</div></foreignObject>
  <foreignObject x="510" y="282" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{silmä}$</div></foreignObject>
  <foreignObject x="366" y="213.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <foreignObject x="280" y="327.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$L$</div></foreignObject>
  <foreignObject x="48" y="160.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$x$</div></foreignObject>
</svg>

Kun katsot raon takana loistavaa LEDiä hilan läpi, näet raon sivulla värillisen kuvan. Mittaa etäisyys $L$ asteikosta hilaan ja kuvan etäisyys $x$ raosta asteikolla. Silloin $\tan\theta = \dfrac{x}{L}$, josta saat kulman $\theta$ ja edelleen aallonpituuden. Vertaa mittaamaasi aallonpituutta tietolehden arvoon epävarmuuksineen: ovatko ne sopusoinnussa? Päällekkäiset epävarmuusvälit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi. Miten aallonpituuden epävarmuus vaikuttaa Planckin vakion epävarmuuteen?

Katso hilan läpi vain sellaista näkyvää valoa lähettävää LEDiä, jonka opettaja on hyväksynyt tähän, ja pidä virta niin pienenä, että LED loistaa himmeästi. UV- ja infrapuna-LEDejä ei katsota hilan läpi.

::: tuki O OO
**Vihjeitä.** Pimennä huone ja pidä hila kohtisuorassa raosta tulevaan valoon nähden. Mittaa kuva raon molemmilta puolilta ja käytä etäisyyksien keskiarvoa: silloin hilan pieni vinous kumoutuu. Mitä suurempi $L$, sitä pienempi on etäisyyksien lukemisen suhteellinen epävarmuus, kunhan kuva vielä erottuu. LED lähettää kapean aallonpituusalueen, joten kuva on hieman leveä: lue sen keskikohta.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajiin ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
