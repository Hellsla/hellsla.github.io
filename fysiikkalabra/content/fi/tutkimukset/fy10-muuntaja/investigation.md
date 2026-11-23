# Muuntajan tutkiminen

> **Tutkimuskysymys:** Miten muuntajan toisiojännite riippuu käämien kierroslukujen suhteesta, kuinka hyvin ideaalisen muuntajan malli kuvaa mittauksia, ja kuinka suuri on muuntajan hyötysuhde?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydällä on muuntaja. Suljetun rautasydämen kummassakin pystyhaarassa on käämi. Vasemmanpuoleinen käämi on kytketty johtimilla virtalähteeseen ja kahteen yleismittariin, oikeanpuoleinen kahteen yleismittariin ja kuormitusvastukseen. Mittarien näytöt ovat tyhjiä. Pöydällä on lisäksi kaksi irrallista käämiä ja vihko." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-muuntaja-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

Sähköverkon jakelumuuntajat, hitsauslaitteet ja monet sähkölaitteiden virtalähteet muuttavat vaihtojännitteen suuruutta muuntajalla. Muuntajassa ei ole liikkuvia osia, eikä sen kahden käämin välillä kulje sähkövirtaa, mutta silti energia siirtyy käämistä toiseen. Tässä tutkimuksessa kokoat muuntajan itse vaihdettavista käämeistä, mittaat sen jännitteet ja sähkövirrat ja vertaat tuloksia malliin. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:**

- miten toisiojännitteen ja ensiöjännitteen suhde riippuu käämien kierroslukujen suhteesta, kun toisiokäämin napoihin on kytketty vain jännitemittari (mittaukset usealla eri kierroslukujen suhteella)
- kuinka hyvin ideaalisen muuntajan malli kuvaa mittauksia, ja muuttuuko toisiojännite, kun toisiopiiriin kytketään kuormitusvastus (mittaus ainakin yhdellä käämiyhdistelmällä sekä ilman kuormaa että kuormitettuna)
- muuntajan hyötysuhde epävarmuuksineen ensiö- ja toisiopuolen sähkötehoista, ja mistä energiahäviöt johtuvat.

**Päätät itse** (osittain ohjattu ja itsenäinen työtapa): käytettävät käämiyhdistelmät ja niiden määrän opettajan hyväksymien joukosta, ensiöjännitteen opettajan antamissa rajoissa, mitä pidät vakiona ja kuinka monta kertaa toistat lukemat. Itsenäisessä työtavassa valitset lisäksi kuvaajan akselit perusteluineen ja tavan, jolla arvioit tulosten epävarmuuden. Ohjatussa työtavassa sivu kiinnittää nämä valinnat. Osittain ohjatussa työtavassa sivu antaa tueksi mallikuvaajan ja tavat arvioida epävarmuutta.

::: tuki I
**Itsenäinen työtapa.** Laajennus, hyötysuhteen mittaaminen eri kuormituksilla, kuuluu työhösi.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Ensiökäämi ja ensiöjännite pysyvät samoina. Mitä toisiojännitteelle tapahtuu, kun toisiokäämin kierrosluku kaksinkertaistetaan? Entä jos ensiökäämin kierrosluku kaksinkertaistetaan ja toisiokäämi pysyy samana?
2. Muuttuuko toisiojännite, kun toisiokäämin napoihin kytketään pelkän jännitemittarin lisäksi kuormitusvastus? Jos muuttuu, mihin suuntaan?
3. Kuinka suuri osa ensiöpuolelle tuodusta sähkötehosta arvelet saatavan toisiopuolelta? Mihin loput energiasta joutuu?
4. Mikä mittauksessa on todennäköisesti suurin epävarmuuden lähde?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Teoriaa lyhyesti

**Muuntajan rakenne.** Muuntajassa on kaksi käämiä yhteisen rautasydämen ympärillä. **Ensiökäämi** kytketään vaihtojännitelähteeseen ja **toisiokäämi** kuormaan, esimerkiksi vastukseen. Käämit eivät ole sähköisesti yhteydessä toisiinsa: energia siirtyy niiden välillä magneettikentän välityksellä. Käämin kierrosluku $N$ kertoo, kuinka monta kertaa johdin kiertää sydämen ympäri.

**Induktio lyhyesti.** Kun ensiökäämissä kulkee vaihtovirta, se synnyttää rautasydämeen magneettikentän, jonka suuruus ja suunta muuttuvat jatkuvasti. Rautasydän ohjaa kentän kulkemaan myös toisiokäämin läpi. Kierroksen läpi kulkevaa magneettikentän ”määrää” kutsutaan **magneettivuoksi**. Kun magneettivuo muuttuu, johdinkierrokseen syntyy eli **indusoituu** jännite, joka on sitä suurempi, mitä nopeammin vuo muuttuu. Käämin kierrokset ovat peräkkäin eli sarjassa, joten niiden jännitteet laskevat yhteen. Sama tapahtuu myös ensiökäämissä itsessään: sen omiin kierroksiin indusoituva jännite vastustaa sähkövirran muutosta. Tasajännitteellä muuntaja ei toimi, koska muuttumaton magneettikenttä ei indusoi jännitettä. Induktiota ja muuntajaa käsitellään tarkemmin moduulissa FY7.

**Ideaalinen muuntaja** on malli, jossa

- kaikki magneettivuo kulkee rautasydämessä, eli sama vuo kulkee molempien käämien jokaisen kierroksen läpi
- käämien johtimilla ei ole resistanssia
- rautasydämessä ei synny energiahäviöitä.

Todellinen muuntaja ei täytä näitä ehtoja täsmälleen. Tässä työssä selvität, kuinka paljon se poikkeaa mallista.

**Vaihtojännite ja tehollinen arvo.** Vaihtojännite ja vaihtovirta muuttavat suuntaansa ja suuruuttaan jatkuvasti. Vaihtosuureiden mittari näyttää **tehollisen arvon**: se on valittu niin, että vastuksen keskimääräinen teho on $P = UI$, kun $U$ ja $I$ ovat tehollisia arvoja. Kytke siis yleismittari vaihtojännitteen ja vaihtovirran asetukselle.

**Sähköteho ja hyötysuhde.** Vastuksen teho on sen napojen välisen jännitteen ja vastuksen läpi kulkevan sähkövirran tulo, $P = UI$. Sama pätee muihinkin laitteisiin silloin, kun jännite ja sähkövirta vaihtelevat samassa tahdissa. Jännitteen yksikkö on voltti ($\text{V}$), sähkövirran ampeeri ($\text{A}$) ja tehon watti: $1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W}$. Sähkötehoa käsitellään tarkemmin moduulissa FY6. [[apua:fy2-3|Teho]] Muuntajan **hyötysuhde** on toisiopuolelta saatavan tehon $P_2$ ja ensiöpuolelle tuodun tehon $P_1$ suhde:

```latex
\eta = \frac{P_2}{P_1}
```

[[apua:fy2-4|Hyötysuhde]] Kuormitusvastukselle teho on $P_2 = U_2 I_2$. Ensiökäämille tulo $U_1 I_1$ ei kuitenkaan ole aivan sama kuin käämiin tuleva teho: osa ensiövirrasta vain magnetoi rautasydäntä, ja sen kuljettama energia palaa jännitelähteeseen saman jakson aikana. Siksi $U_1 I_1$ on vähintään yhtä suuri kuin ensiöpuolelle todella tuleva teho. Kun lasket hyötysuhteen tulosta $\eta = \dfrac{U_2 I_2}{U_1 I_1}$, saat arvon, joka ei ole todellista hyötysuhdetta suurempi.

**Mittarien kytkeminen.** Virtamittari kytketään **sarjaan** sen käämin tai vastuksen kanssa, jonka läpi kulkeva sähkövirta mitataan. Jännitemittari kytketään **rinnan** käämin kanssa, sen kahden navan väliin. Virtamittaria ei koskaan kytketä yksin käämin napoihin, sillä se oikosulkisi käämin.

<svg data-fig="setup" viewBox="0 0 600 380" role="img" aria-label="Kaaviokuva. Suljetun rautasydämen vasemmassa haarassa on ensiökäämi, jossa on N yksi kierrosta, ja oikeassa haarassa toisiokäämi, jossa on N kaksi kierrosta. Ensiökäämi on kytketty vaihtojännitelähteeseen. Ensiöpiirissä virtamittari on sarjassa käämin kanssa ja mittaa sähkövirran I yksi, ja jännitemittari on kytketty käämin napoihin ja mittaa jännitteen U yksi. Toisiopiirissä virtamittari on sarjassa kuormitusvastuksen R kanssa ja mittaa sähkövirran I kaksi, ja jännitemittari on kytketty toisiokäämin napoihin ja mittaa jännitteen U kaksi." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-muuntaja-setup.webp" x="0" y="-1.2" width="600" height="386.2" preserveAspectRatio="none"/>
  <foreignObject x="244" y="52" width="112" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{rautasydän}$</div></foreignObject>
  <foreignObject x="50" y="180.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\sim$</div></foreignObject>
  <foreignObject x="100.5" y="127" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{A}$</div></foreignObject>
  <foreignObject x="93.5" y="89.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I_1$</div></foreignObject>
  <foreignObject x="160.5" y="182" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{V}$</div></foreignObject>
  <foreignObject x="109" y="180.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U_1$</div></foreignObject>
  <foreignObject x="568" y="180.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R$</div></foreignObject>
  <foreignObject x="480.5" y="127" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{A}$</div></foreignObject>
  <foreignObject x="473.5" y="89.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I_2$</div></foreignObject>
  <foreignObject x="420.5" y="182" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{V}$</div></foreignObject>
  <foreignObject x="458" y="180.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U_2$</div></foreignObject>
  <foreignObject x="208.5" y="307.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N_1$</div></foreignObject>
  <foreignObject x="358.5" y="307.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N_2$</div></foreignObject>
  <foreignObject x="166" y="342" width="112" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{ensiökäämi}$</div></foreignObject>
  <foreignObject x="317" y="342" width="122" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{toisiokäämi}$</div></foreignObject>
</svg>

## Tutkimuskysymyksestä mitattaviksi suureiksi

Ennen kuin luet eteenpäin, kirjaa:

1. Mitä ideaalisen muuntajan malli ennustaa: miten toisiojännite $U_2$ riippuu ensiöjännitteestä $U_1$ ja kierrosluvuista $N_1$ ja $N_2$? Perustele yllä olevien periaatteiden avulla.
2. Millaisen kuvaajan piirrät, jotta mallin ennuste näkyy suorana? Mikä sen kulmakertoimen pitäisi olla, jos malli pätee?
3. Mitä muutat, mitä mittaat jokaisella käämiyhdistelmällä ja mitä pidät vakiona?
4. Mitkä suureet mittaat hyötysuhdetta varten, ja mitkä niistä on luettava samaan aikaan?

::: tuki O OO
Tarkista kirjauksesi tästä. Ideaalisessa muuntajassa sama magneettivuo kulkee jokaisen kierroksen läpi, joten jokaiseen kierrokseen indusoituu yhtä suuri jännite kummassakin käämissä. Toisiokäämin jännite on silloin $N_2$ kertaa yhden kierroksen jännite. Ensiökäämiin indusoituva jännite on vastaavasti $N_1$ kertaa sama kierroksen jännite, ja koska käämin johtimella ei mallissa ole resistanssia, se on yhtä suuri kuin käämiin kytketty jännite $U_1$. Yhden kierroksen jännite on siis $\dfrac{U_1}{N_1} = \dfrac{U_2}{N_2}$, eli

```latex
\frac{U_2}{U_1} = \frac{N_2}{N_1}
```

Jännitteiden suhde on mallin mukaan sama kuin kierroslukujen suhde. Kuvaaja, jossa pystyakselilla on $\dfrac{U_2}{U_1}$ ja vaaka-akselilla $\dfrac{N_2}{N_1}$, on silloin origon kautta kulkeva suora, jonka kulmakerroin on $1$. Koska akseleilla on suhteita, pienet ensiöjännitteen vaihtelut mittausten välillä eivät hajota pisteitä.

<svg data-fig="model" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja: jännitteiden suhde U kaksi per U yksi kierroslukujen suhteen N kaksi per N yksi funktiona ideaalisen muuntajan mallin mukaan. Akseleilla on sama mittakaava, ja kummallekin on merkitty arvot yksi ja kaksi. Kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on yksi. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="182" y1="280" x2="182" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="274" y1="280" x2="274" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="188" x2="320" y2="188" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="96" x2="320" y2="96" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="280" x2="334" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M346,280 L333,286 L333,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="182" y1="280" x2="182" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="172" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="274" y1="280" x2="274" y2="287" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="264" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="83" y1="188" x2="90" y2="188" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="173.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="83" y1="96" x2="90" y2="96" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="81.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="352" y="265.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N_2/N_1$</div></foreignObject>
  <foreignObject x="104" y="15.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$U_2/U_1$</span></div></foreignObject>
  <polyline points="90,280 311,59" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="228" y="182.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{kulmakerroin } 1$</span></div></foreignObject>
</svg>

Hyötysuhdetta varten tarvitset samalla käämiyhdistelmällä ja samalla kuormalla ensiöjännitteen $U_1$, ensiövirran $I_1$, toisiojännitteen $U_2$ ja toisiovirran $I_2$, kaikki luettuina samaan aikaan, koska ne voivat muuttua, kun kuormitusta muutetaan. Mallin ehdot eivät ole itsestään selviä, ja mittaus näyttää, pysyvätkö pisteet mallin suoralla.
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona. Piirrä kytkentäkaavio ja näytä kytkentä opettajalle ennen kuin kytket virran.

::: tuki O
**Ohjattu.** Kokoa muuntaja niin, että rautasydän on suljettu. Tee mittaukset kahdessa osassa.

- **Osa A, jännitteiden suhde.** Kytke toisiokäämin napoihin vain jännitemittari. Kytke ensiökäämiin opettajan ilmoittama jännite ja mittaa ensiöjännite $U_1$ ja toisiojännite $U_2$. Toista mittaus kaikilla opettajan hyväksymillä käämiyhdistelmillä, ja vaihda myös käämien rooleja niin, että sama käämi on vuorollaan ensiö- ja toisiokäämi. Tavoite on vähintään viisi eri kierroslukujen suhdetta, sekä ykköstä pienempiä että suurempia. Kirjaa jokaisella kerralla molemmat kierrosluvut. Lue kullakin yhdistelmällä lukemat kerran: toistoja ei tarvita, koska kuvaajan useat pisteet tasoittavat yksittäisten lukemien satunnaisia virheitä.
- **Osa B, hyötysuhde.** Valitse opettajan neuvoma käämiyhdistelmä. Mittaa ensin toisiojännite ilman kuormaa. Kytke sitten toisiopiiriin kuormitusvastus ja sen kanssa sarjaan virtamittari sekä ensiöpiiriin virtamittari. Lue kaikki neljä mittaria $U_1$, $I_1$, $U_2$ ja $I_2$ samalla kuormituksella. Katkaise virta, kytke se uudelleen ja lue lukemat vielä kahdesti, niin että saat kolme lukemasarjaa.

Pidä sähkövirrat opettajan ilmoittamien rajojen alapuolella.
:::

::: tuki OO
**Osittain ohjattu.** Päätä itse, mitä käämiyhdistelmiä käytät ja kuinka monta, millä ensiöjännitteellä mittaat ja montako kertaa toistat lukemat. Hyötysuhdetta varten tarvitset kuormitusvastuksen ja virtamittarin kumpaankin piiriin. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Pysyykö ensiöjännite samana, kun vaihdat käämejä? Kannattaako se mitata joka kerta vai luottaa virtalähteen asetukseen?
- Miten saat samoista käämeistä sekä ykköstä pienempiä että suurempia kierroslukujen suhteita?
- Mitä tapahtuu, jos rautasydän ei ole kunnolla suljettu, esimerkiksi jos sen osien väliin jää rako?
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle. Mittaa toisiojännite jokaisella käämiyhdistelmällä ilman kuormaa, ja ainakin yhdellä yhdistelmällä myös kuormitettuna.

::: tuki O
Voit käyttää esimerkiksi tällaisia taulukoita:

**Osa A.**

| $N_1$ | $N_2$ | $U_1\ (\text{V})$ | $U_2\ (\text{V})$ | $N_2/N_1$ | $U_2/U_1$ |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

**Osa B.** Kirjaa taulukon yläpuolelle käämien kierrosluvut ja toisiojännite ilman kuormaa.

| $U_1\ (\text{V})$ | $I_1\ (\text{A})$ | $U_2\ (\text{V})$ | $I_2\ (\text{A})$ | $P_1 = U_1 I_1\ (\text{W})$ | $P_2 = U_2 I_2\ (\text{W})$ | $\eta = P_2/P_1$ |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |

Jos mittarissa on usea mittausalue, aloita suurimmalta ja vaihda pienemmälle vasta, kun tiedät, että lukema mahtuu siihen.
:::

Muista mittausepävarmuus: selvitä mittarien tarkkuus mittarin ohjeesta tai opettajalta, ja kirjaa se taulukkoon. Kirjaa myös, ovatko käämeihin merkityt kierrosluvut tarkkoja vai likimääräisiä, jos tieto on saatavilla. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Piirrä jännitteiden mittaustuloksista kuvaaja, jonka avulla voit verrata mittauksia ideaalisen muuntajan malliin. Merkitse akseleille suureet ja yksiköt, jos niillä on yksikkö. Piirrä mittauspisteet, älä yhdistä niitä murtoviivalla, ja sovita pisteisiin mallin mukainen käyrä (suora, jos valitsit akselit niin, että malli on suora). [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

::: tuki O
Valitse pystyakselille jännitteiden suhde $U_2/U_1$ ja vaaka-akselille kierroslukujen suhde $N_2/N_1$.
:::

Kirjoita sovitetun suoran yhtälö ja vastaa:

1. Miksi valitsit juuri nämä akselit? Mitä mallin mukaan pitäisi näkyä kuvaajassa?
2. Ovatko pisteet suoralla koko mittausalueella? Jos eivät, millä kierroslukujen suhteilla ne poikkeavat?
3. Mikä on suoran kulmakerroin, ja poikkeaako se mallin arvosta enemmän kuin epävarmuus selittää? Kulkeeko suora origon kautta?
4. Muuttuiko toisiojännite, kun kytkit kuormitusvastuksen? Jos muuttui, kuinka paljon, suhteessa mittarin tarkkuuteen?
5. Laske hyötysuhde $\eta = \dfrac{U_2 I_2}{U_1 I_1}$ jokaisesta lukemasarjasta ja niiden keskiarvo $\bar{\eta}$.

::: tuki O OO
Tarkista vastauksesi tästä.

**Miksi juuri nämä akselit?** Kun pystyakselilla on $U_2/U_1$ ja vaaka-akselilla $N_2/N_1$, ideaalisen muuntajan malli on suora $y = x$. Silloin mallin testaaminen on yksinkertaista: kulmakertoimen pitäisi olla $1$ ja suoran kulkea origon kautta. Jos piirtäisit pelkän toisiojännitteen $U_2$ kierroslukujen suhteen funktiona, kulmakerroin olisi ensiöjännite, ja vaihteleva ensiöjännite hajottaisi pisteitä.
:::

Kuvaajan sovitukseen käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Ilmoita kuvaajan kulmakerroin muodossa $a \pm \Delta a$ ja hyötysuhde muodossa $\eta \pm \Delta\eta$, ja perustele, miten arvioit epävarmuudet.

::: tuki O OO
**Kulmakertoimen epävarmuuden** $\Delta a$ voit arvioida jommallakummalla tavalla:

- **Sovitusohjelman keskivirhe.** Monet ohjelmat ilmoittavat kulmakertoimen keskivirheen. Käytä sitä epävarmuutena $\Delta a$.
- **Jyrkin ja loivin suora.** Piirrä jyrkin ja loivin suora, jotka vielä sopivat pisteisiin niiden epävarmuuksien rajoissa. Määritä niiden kulmakertoimet $a_\text{max}$ ja $a_\text{min}$ ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta a = \dfrac{a_\text{max} - a_\text{min}}{2}$.

Yksittäisen pisteen epävarmuuden pystysuunnassa saat jännitemittarien tarkkuudesta: osamäärän suhteellinen epävarmuus on osoittajan ja nimittäjän suhteellisten epävarmuuksien summa, $\dfrac{\Delta(U_2/U_1)}{U_2/U_1} \approx \dfrac{\Delta U_1}{U_1} + \dfrac{\Delta U_2}{U_2}$.

**Hyötysuhteen epävarmuus.** Hyötysuhde lasketaan neljän lukeman tulosta ja osamäärästä, joten sen suhteellinen epävarmuus on niiden suhteellisten epävarmuuksien summa:

```latex
\begin{aligned}
\frac{\Delta \eta}{\eta} \approx {} & \frac{\Delta U_1}{U_1} + \frac{\Delta I_1}{I_1} \\
& + \frac{\Delta U_2}{U_2} + \frac{\Delta I_2}{I_2}
\end{aligned}
```

Vertaa tätä lukemasarjojen hajontaan (esimerkiksi puolet suurimman ja pienimmän arvon erotuksesta), ja käytä epävarmuutena suurempaa. Muista lisäksi, että tulo $U_1 I_1$ on vähintään yhtä suuri kuin ensiöpuolelle todella tuleva teho: tämä systemaattinen virhe voi vain pienentää laskemaasi hyötysuhdetta, ei kasvattaa sitä.

Pyöristä epävarmuus yhteen merkitsevään numeroon ja tulos samaan desimaaliin.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet tuloksia? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Viittaa kuvaajaan, esimerkiksi ”kuvaajasta 1 nähdään, että …”, ja vastaa ainakin näihin:

- Kuinka hyvin ideaalisen muuntajan malli kuvaa mittauksiasi? Mikä mallin ehdoista täyttyi todennäköisesti huonoiten, ja mihin mittaustulokseen perustat päätelmäsi?
- Mistä muuntajan energiahäviöt johtuvat? Perustele sillä, mitä mittasit, esimerkiksi hyötysuhteella ja toisiojännitteen muutoksella kuormitettaessa.
- Mitä hyötysuhteesi kertoo juuri tästä muuntajasta ja tästä kuormituksesta, ja mitä se ei kerro muuntajista yleensä?

Vertaa tuloksia ennusteisiisi: mikä osui oikeaan ja mikä ei?

::: tuki O OO
Tarkista vastauksesi tästä, kun olet kirjoittanut ne.

**Jos tulos poikkeaa mallista.** Mieti, mikä ideaalisen mallin ehdoista ei täyty. Jos osa magneettivuosta kulkee ilmassa eikä toisiokäämin läpi, toisiokäämiin indusoituu vähemmän jännitettä kuin malli ennustaa. Ensiökäämin johtimen resistanssi vie osan ensiöjännitteestä, joten käämiin indusoituva jännite on hieman pienempi kuin $U_1$. Kun toisiopiirissä kulkee sähkövirta, myös toisiokäämin oma resistanssi vie osan indusoituneesta jännitteestä ennen kuin se ehtii kuormaan.

**Mihin energia häviää?** Käämien johtimet lämpenevät, kun niissä kulkee sähkövirta. Rautasydämeen indusoituu pyörrevirtoja, jotka lämmittävät sitä, ja sydämen magnetoinnin suunnan jatkuva kääntäminen kuluttaa energiaa.
:::

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** ideaalisen muuntajan malli ja sen ehdot, miksi kuvaajan akselit valittiin niin kuin valittiin, sekä miten hyötysuhde lasketaan.
- **Koejärjestely ja menetelmä:** kytkentäkaavio, jossa näkyy, miten mittarit on kytketty kumpaankin piiriin, sekä työturvallisuus.
- **Mittaustulokset:** kierrosluvut ja alkuperäiset lukemat omissa sarakkeissaan ja lasketut suhteet ja tehot niiden oikealla puolella.
- **Tulos:** kulmakerroin $a \pm \Delta a$ ja hyötysuhde $\eta \pm \Delta\eta$ oikein pyöristettyinä, sekä kuormituksen vaikutus toisiojännitteeseen.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet ja niiden vaikutuksen suunta, myös se, miksi tulosta $U_1 I_1$ käyttämällä saatu hyötysuhde ei voi olla todellista suurempi.

## Laajennus: hyötysuhde eri kuormituksilla

Muuntajan hyötysuhde ei välttämättä ole sama kaikilla kuormituksilla. Tutki samalla käämiyhdistelmällä, miten hyötysuhde riippuu siitä, kuinka paljon tehoa toisiopuolelta otetaan: vaihda kuormitusvastusta opettajan antamien vastusten joukosta ja määritä jokaisella kuormalla $U_1$, $I_1$, $U_2$ ja $I_2$. Pidä sähkövirrat koko ajan opettajan ilmoittamien rajojen alapuolella.

Piirrä hyötysuhde toisiopuolen tehon $P_2$ funktiona ja vastaa:

1. Millä kuormituksella hyötysuhde oli suurin ja millä pienin?
2. Miten toisiojännite muuttui, kun toisiovirta kasvoi?
3. Miten selität havaitsemasi muutokset muuntajan energiahäviöillä?

::: tuki O OO
**Vihjeitä.** Muuta vain kuormaa: pidä käämiyhdistelmä ja virtalähteen asetus samoina, ja anna käämien jäähtyä mittausten välillä, jos ne lämpenevät. Mieti vastatessasi, mitkä häviöt ovat suunnilleen samat kuormasta riippumatta (rautasydämen magnetointi) ja mitkä kasvavat sähkövirran kasvaessa (käämien johtimien lämpeneminen). Muista myös, että tulo $U_1 I_1$ yliarvioi ensiöpuolen tehoa eniten silloin, kun kuormitus on pieni.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?

**Sovella:** Sähköenergia siirretään voimalaitoksilta pitkiä matkoja suurjännitteellä, ja muuntajat laskevat jännitteen ennen kuin sähkö tulee koteihin. Pohdi tehon $P = UI$ avulla, miksi sama teho kannattaa siirtää suurella jännitteellä: miten se vaikuttaa siirtojohtojen sähkövirtaan ja johtojen lämpenemiseen? Pohdi tätä ajatuksen tasolla: verkkojännitteeseen kytkettyjä laitteita ja muuntajia ei tutkita itse.
