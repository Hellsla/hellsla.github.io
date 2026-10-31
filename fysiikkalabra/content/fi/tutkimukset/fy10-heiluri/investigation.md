# Putoamiskiihtyvyyden määrittäminen heilurin avulla

> **Tutkimuskysymys:** Mistä heilurin jaksonaika riippuu, ja kuinka suuri on putoamiskiihtyvyys mittauspaikallasi?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydällä on statiivi, jonka varresta riippuu langan varassa metallikuula. Kuula on piirretty useaan kohtaan pienen heilahduksen aikana. Pöydällä ovat rullamitta, sekuntikello, lankarulla ja sakset." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10hh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10hh-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10hh-wall)"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy10hh-desk)"/>
  <line x1="0" y1="492" x2="1200" y2="488" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="514" x2="1200" y2="510" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="536" x2="1200" y2="532" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="558" x2="1200" y2="554" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="580" x2="1200" y2="576" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="300" y="448" width="260" height="22" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="333" y="50" width="14" height="398" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="334" y="68" width="292" height="12" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="324" y="60" width="32" height="28" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="590" y="78" width="20" height="16" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M548.5,418 A330,330 0 0 0 651.5,418" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-dasharray="6 6"/>
  <line x1="600" y1="92" x2="648.5" y2="398" stroke="#495057" stroke-width="1.5" stroke-opacity="0.25"/>
  <g opacity="0.3"><circle cx="651.5" cy="418" r="20" fill="#adb5bd" stroke="#495057" stroke-width="2.5"/><circle cx="644.5" cy="411" r="5" fill="#ffffff" fill-opacity="0.6"/></g>
  <line x1="600" y1="92" x2="642" y2="399" stroke="#495057" stroke-width="1.5" stroke-opacity="0.25"/>
  <g opacity="0.3"><circle cx="645" cy="419" r="20" fill="#adb5bd" stroke="#495057" stroke-width="2.5"/><circle cx="638" cy="412" r="5" fill="#ffffff" fill-opacity="0.6"/></g>
  <line x1="600" y1="92" x2="624.5" y2="401" stroke="#495057" stroke-width="1.5" stroke-opacity="0.25"/>
  <g opacity="0.3"><circle cx="626" cy="421" r="20" fill="#adb5bd" stroke="#495057" stroke-width="2.5"/><circle cx="619" cy="414" r="5" fill="#ffffff" fill-opacity="0.6"/></g>
  <line x1="600" y1="92" x2="600" y2="402" stroke="#495057" stroke-width="1.5" stroke-opacity="0.25"/>
  <g opacity="0.3"><circle cx="600" cy="422" r="20" fill="#adb5bd" stroke="#495057" stroke-width="2.5"/><circle cx="593" cy="415" r="5" fill="#ffffff" fill-opacity="0.6"/></g>
  <line x1="600" y1="92" x2="575.5" y2="401" stroke="#495057" stroke-width="1.5" stroke-opacity="0.25"/>
  <g opacity="0.3"><circle cx="574" cy="421" r="20" fill="#adb5bd" stroke="#495057" stroke-width="2.5"/><circle cx="567" cy="414" r="5" fill="#ffffff" fill-opacity="0.6"/></g>
  <line x1="600" y1="92" x2="558" y2="399" stroke="#495057" stroke-width="1.5" stroke-opacity="0.25"/>
  <g opacity="0.3"><circle cx="555" cy="419" r="20" fill="#adb5bd" stroke="#495057" stroke-width="2.5"/><circle cx="548" cy="412" r="5" fill="#ffffff" fill-opacity="0.6"/></g>
  <line x1="600" y1="92" x2="551.5" y2="398" stroke="#495057" stroke-width="2" stroke-opacity="1"/>
  <g opacity="1.0"><circle cx="548.5" cy="418" r="20" fill="#adb5bd" stroke="#495057" stroke-width="2.5"/><circle cx="541.5" cy="411" r="5" fill="#ffffff" fill-opacity="0.6"/></g>
  <rect x="820" y="418" width="70" height="52" rx="10" fill="#ffd43b" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="855" cy="444" r="10" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="888" y="456" width="90" height="10" fill="#ffe8a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="1064.5" y="380" width="11" height="8" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="1067.5" y="387.5" width="5" height="5" fill="#6c757d"/>
  <circle cx="1070" cy="425" r="34" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="1070" cy="425" r="27.88" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="1070" y1="402" x2="1070" y2="398.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1081.5" y1="405" x2="1083.5" y2="402" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1090" y1="413.5" x2="1093" y2="411.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1093" y1="425" x2="1096.5" y2="425" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1090" y1="436.5" x2="1093" y2="438.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1081.5" y1="445" x2="1083.5" y2="448" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1070" y1="448" x2="1070" y2="451.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1058.5" y1="445" x2="1056.5" y2="448" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1050" y1="436.5" x2="1047" y2="438.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1047" y1="425" x2="1043.5" y2="425" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1050" y1="413.5" x2="1047" y2="411.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1058.5" y1="405" x2="1056.5" y2="402" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="1070" y1="425" x2="1090.5" y2="415.5" stroke="#c92a2a" stroke-width="2.38" stroke-linecap="round"/>
  <circle cx="1070" cy="425" r="2.72" fill="#1f2933"/>
  <rect x="90" y="430" width="46" height="40" rx="4" fill="#1971c2" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="82" y="424" width="62" height="10" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="82" y="466" width="62" height="8" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <g transform="translate(190,446) rotate(-12)" fill="none" stroke="#1f2933" stroke-width="3"><circle cx="0" cy="0" r="10"/><circle cx="0" cy="26" r="10"/><line x1="9" y1="5" x2="70" y2="20"/><line x1="9" y1="21" x2="70" y2="8"/></g>
</svg>

Vapaasti putoava kappale on ohi hetkessä, joten sen kiihtyvyyttä on vaikea mitata tarkasti tavallisilla välineillä. Heiluri toistaa samaa liikettä yhä uudelleen, ja sen tahti riippuu putoamiskiihtyvyydestä. Tässä tutkimuksessa selvität mittaamalla, mistä heilurin jaksonaika riippuu, ja määrität putoamiskiihtyvyyden pelkän langan, kuulan, mittanauhan ja kellon avulla. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** mistä heilurin jaksonaika riippuu, ja kuinka suuri putoamiskiihtyvyys $g$ on mittauspaikallasi epävarmuuksineen.

**Päätät itse:** itsenäisessä työtavassa päätät kaiken tämän: mitä heilurin ominaisuutta muutat ja mitkä pidät vakioina, käytettävät arvot ja mittauspisteiden määrän, toistojen määrän, tavan, jolla mittaat jaksonajan ja heilurin pituuden, miten testaat muiden ominaisuuksien vaikutuksen, kuvaajan akselit perusteluineen sekä tavan, jolla arvioit tuloksen epävarmuuden. Osittain ohjatussa työtavassa sivu antaa muuttujan, kuvaajan akselit ja kaksi tapaa arvioida epävarmuus, joista valitset toisen; pituudet, heilahdusten ja toistojen määrän, mittaustavat ja tarkistusmittauksen järjestelyn päätät itse. Ohjatussa työtavassa sivu kiinnittää kaikki nämä valinnat, ja sinä perustelet ne raportissa.

::: tuki I
**Itsenäinen työtapa.** Laajennus, heilahduskulman vaikutuksen tutkiminen, kuuluu työhösi: arvioi sen avulla, oliko päämittauksesi heilahduskulma riittävän pieni.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Vaikuttaako jaksonaikaan langan pituus, kuulan massa tai se, kuinka kauas sivulle kuula vedetään? Arvioi kunkin kohdalla, kasvaako jaksonaika, pieneneekö se vai pysyykö se samana.
2. Jos langan pituus nelinkertaistuu, mitä arvelet tapahtuvan jaksonajalle?
3. Millainen on kuvaaja, jossa pystyakselilla on jaksonaika ja vaaka-akselilla langan pituus: suora vai käyrä?
4. Kumpi on mittauksessa todennäköisesti suurempi epävarmuuden lähde, pituuden vai ajan mittaaminen? Miksi?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Putoamiskiihtyvyyttä ei voi lukea suoraan mistään mittarista. Ennen kuin luet eteenpäin, kirjaa:

1. Mitä heilurin ominaisuutta muuttamalla voisit saada putoamiskiihtyvyyden selville, ja mitkä ominaisuudet pidät silloin vakioina?
2. Yksi heilahdus edestakaisin kestää vain sekunnin tai pari. Miten saat jaksonajan mitattua mahdollisimman tarkasti käsin otetulla ajalla?
3. Mistä kohdasta mihin kohtaan heilurin pituus mitataan?

## Teoriaa lyhyesti

Heiluri on **jaksollisessa liikkeessä**: se toistaa samaa liikettä. **Jaksonaika** $T$ on aika, jossa heiluri tekee yhden kokonaisen heilahduksen edestakaisin eli palaa samaan kohtaan liikkuen samaan suuntaan. Jaksonajan yksikkö on sekunti.

Kun kuula vedetään sivuun ja päästetään irti, sen paino vetää sitä kohti radan alinta kohtaa. Kuula ohittaa alimman kohdan suurimmalla nopeudellaan, nousee toiselle puolelle, pysähtyy hetkeksi kääntökohdassa ja palaa takaisin. Mitä suurempi putoamiskiihtyvyys on, sitä voimakkaammin paino palauttaa kuulaa kohti alinta kohtaa ja sitä lyhyempi jaksonaika on. [[apua:fy1-6|Putoamiskiihtyvyys]]

<svg data-fig="setup" viewBox="0 0 600 400" role="img" aria-label="Kaaviokuva. Kuula riippuu langan varassa ripustuskohdasta. Heilurin pituus l mitataan ripustuskohdasta kuulan keskipisteeseen. Kuula on vedetty sivuun niin, että lanka on kulmassa theta pystysuoraan nähden. Katkoviiva näyttää kuulan radan ja pystysuoran, ja haaleampi kuula on radan alimmassa kohdassa. Kulma on piirretty selvyyden vuoksi suuremmaksi kuin mittauksissa." style="max-width:100%;font-size:24px">
  <rect x="170" y="26" width="260" height="14" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="291" y="38" width="18" height="14" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M207.5,303.5 A270,270 0 0 0 392.5,303.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-dasharray="6 6"/>
  <line x1="300" y1="50" x2="300" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <g opacity="0.35"><circle cx="300" cy="320" r="22" fill="#adb5bd" stroke="#495057" stroke-width="2.5"/><circle cx="292.5" cy="312.5" r="5.5" fill="#ffffff" fill-opacity="0.6"/></g>
  <line x1="300" y1="50" x2="385" y2="283" stroke="#495057" stroke-width="2" stroke-linecap="butt"/>
  <g opacity="1.0"><circle cx="392.5" cy="303.5" r="22" fill="#adb5bd" stroke="#495057" stroke-width="2.5"/><circle cx="384.5" cy="296" r="5.5" fill="#ffffff" fill-opacity="0.6"/></g>
  <circle cx="392.5" cy="303.5" r="3.5" fill="#1f2933"/>
  <circle cx="300" cy="320" r="3.5" fill="#1f2933"/>
  <path d="M300,120 A70,70 0 0 0 324,116" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="312" y="127.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <line x1="230" y1="50" x2="230" y2="320" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="220" y1="50" x2="240" y2="50" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="220" y1="320" x2="240" y2="320" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="240" y1="320" x2="274" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <foreignObject x="198" y="170.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$l$</div></foreignObject>
  <foreignObject x="324" y="31.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{ripustuskohta}$</div></foreignObject>
  <foreignObject x="196" y="349.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kuulan keskipiste}$</div></foreignObject>
</svg>

**Heilurin pituus** $l$ on etäisyys ripustuskohdasta kuulan keskipisteeseen, ja **heilahduskulma** $\theta$ on langan suurin kulma pystysuoraan nähden. Värähtelyliikettä käsitellään tarkemmin moduulissa FY5. Siellä osoitetaan, että heilurin jaksonaika on

```latex
T = 2\pi\sqrt{\frac{l}{g}}
```

missä $T$ on jaksonaika, $l$ heilurin pituus ja $g$ putoamiskiihtyvyys. Malli pätee, kun

- heilahduskulma on pieni, korkeintaan noin kymmenen astetta,
- kuula on pieni verrattuna langan pituuteen, joten sen voi ajatella pisteeksi langan päässä,
- langan massa on pieni verrattuna kuulan massaan eikä lanka veny,
- ilmanvastus on pieni ja kuula heilahtaa yhdessä tasossa eikä kiertele soikealla radalla.

Malli kertoo myös, mistä jaksonaika sen mukaan ei riipu. Älä luota siihen pelkän kaavan perusteella, vaan testaa se: tarkistusmittaus kuuluu tähän työhön kaikissa työtavoissa.

Kun malli tunnetaan, putoamiskiihtyvyys voidaan päätellä mittaamalla jaksonaika ja pituus. Yksittäisestä mittauksesta saatu arvo ei kuitenkaan kerro, päteekö malli. Siksi $g$ kannattaa määrittää kuvaajasta, jossa on mittauksia usealla pituudella.

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona. Suunnittele myös tarkistusmittaus, jolla testaat ennusteesi 1: vaikuttavatko kuulan massa ja heilahduskulma jaksonaikaan?

::: tuki O
**Ohjattu.** Muutat heilurin pituutta $l$ ja mittaat jokaisella pituudella jaksonajan $T$. Vakiona pidät kuulan, langan ja pienen heilahduskulman: vedä kuula sivuun enintään noin kymmenesosa heilurin pituudesta. Käytä ainakin kuutta pituutta mahdollisimman tasaisin välein, lyhimmästä noin $0{,}20\ \text{m}$:stä niin pitkään kuin statiivi sallii. Mittaa jokaisella pituudella kymmenen kokonaisen heilahduksen aika kolme kertaa.
:::

::: tuki OO
**Osittain ohjattu.** Muuttuja on heilurin pituus. Päätä itse, mitä pituuksia käytät, kuinka monen heilahduksen ajan mittaat kerralla, montako toistoa teet ja miten pidät heilahduskulman pienenä. Suunnittele lisäksi tarkistusmittaus: millä pituudella, millä toisella kuulalla ja millä heilahduskulmilla testaat massan ja kulman vaikutuksen niin, että kulma pysyy pienten kulmien alueella. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Miten kiinnität langan niin, että ripustuskohta pysyy paikallaan eikä lanka liu'u koukussa heilahdusten aikana?
- Mistä kohdasta kuulaa mittaat pituuden, ja miten mittaat sen samalla tavalla jokaisella pituudella?
- Miksi pituudet kannattaa valita mahdollisimman laajalta väliltä?
- Missä radan kohdassa kuula on helpointa havaita tarkasti, kun käynnistät ja pysäytät kellon?
:::

::: tuki O
**Vihje ajanottoon.** Käynnistä kello, kun kuula ohittaa radan alimman kohdan, ja laske "nolla". Laske jokainen kerta, kun kuula ohittaa saman kohdan samaan suuntaan, ja pysäytä kello lukuun "kymmenen". Alimmassa kohdassa kuula liikkuu nopeimmin, joten ohitushetki näkyy terävämmin kuin kääntökohdassa, jossa kuula on hetken lähes paikallaan. Päästä kuula irti ilman vauhtia ja odota pari heilahdusta ennen kuin aloitat ajanoton.
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana: jokainen toisto omaan sarakkeeseensa ja niistä lasketut suureet mitattujen oikealle puolelle.

::: tuki O
Voit käyttää esimerkiksi tällaista taulukkoa. Siinä $t_{10}$ on kymmenen heilahduksen aika.

| $l\ (\text{m})$ | $t_{10}\ (\text{s})$, 1. | $t_{10}\ (\text{s})$, 2. | $t_{10}\ (\text{s})$, 3. | $\bar{t}_{10}\ (\text{s})$ | $T = \dfrac{\bar{t}_{10}}{10}\ (\text{s})$ | $T^2\ (\text{s}^2)$ |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |

Mittaa pituus ripustuskohdasta kuulan keskipisteeseen. Keskipistettä on vaikea osua mittanauhalla, joten voit mitata langan pituuden ripustuskohdasta kuulan yläpintaan ja lisätä siihen kuulan säteen. Tee kaikki pituudet samalla tavalla.
:::

**Tarkistusmittaus.** Mittaa yhdellä pituudella jaksonaika myös kuulalla, jonka massa on selvästi erilainen, ja tavallista suuremmalla heilahduskulmalla, joka on kuitenkin vielä pienten kulmien alueella. Kirjaa nämäkin tulokset toistoineen.

::: tuki O
Tee tarkistusmittaus päämittauksesi pisimmällä pituudella, jolta sinulla on jo tulos tavallisella kuulalla ja pienellä kulmalla. Mittaa samalla pituudella kymmenen heilahduksen aika kolme kertaa

- toisella kuulalla, jonka massa on selvästi erilainen, kun vedät sen sivuun enintään noin kymmenesosan heilurin pituudesta
- tavallisella kuulalla, kun vedät sen sivuun noin kuudesosan heilurin pituudesta, jolloin kulma on noin kymmenen astetta.

Punnitse molemmat kuulat. Jos toinen kuula on eri kokoinen, säädä langan pituutta niin, että pituus kuulan keskipisteeseen pysyy samana. Kirjaa tulokset samanlaiseen taulukkoon, jossa ensimmäisessä sarakkeessa on pituuden sijasta kuula ja kulma.
:::

Muista mittausepävarmuus: arvioi, kuinka tarkasti mittaat pituuden ja ajan, ja kirjaa arviot ylös. Toistomittausten hajonta kertoo, kuinka paljon ajanotto vaihtelee. [[apua:fy1-3|Toistomittausten keskiarvo ja epävarmuus]]

## Käsittele tulokset

Piirrä mittaustuloksista kuvaaja, jonka kulmakertoimesta saat putoamiskiihtyvyyden. Mieti ensin, mitkä suureet akseleille on valittava, jotta mallin mukainen kuvaaja on suora. Merkitse akseleille suureet ja yksiköt. Piirrä mittauspisteet, älä yhdistä niitä murtoviivalla, ja sovita pisteisiin suora. [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

::: tuki O
Valitse pystyakselille jaksonajan neliö $T^2$ ja vaaka-akselille heilurin pituus $l$.
:::

Kirjoita sovitetun suoran yhtälö ja vastaa:

1. Perustele, miksi valitsemillasi akseleilla mallin mukainen kuvaaja on suora. Mikä suure kulmakerroin on, ja mikä on sen yksikkö?
2. Miten putoamiskiihtyvyys saadaan kulmakertoimesta? Laske $g$.
3. Ovatko pisteet suoralla? Kulkeeko suora origon kautta? Jos ei, mistä vakiotermi voi johtua?

::: tuki O OO
**Miksi juuri nämä akselit?** Kuvaaja jaksonajasta $T$ pituuden $l$ funktiona on käyrä, koska $T$ riippuu pituuden neliöjuuresta. Kun mallin molemmat puolet korotetaan toiseen, saadaan

```latex
T^2 = \frac{4\pi^2}{g}\cdot l
```

joten jaksonajan neliö pituuden funktiona on origon kautta kulkeva suora, jonka kulmakerroin on $a = \dfrac{4\pi^2}{g}$. Kulmakertoimen yksikkö on $\text{s}^2/\text{m}$, ja putoamiskiihtyvyys on $g = \dfrac{4\pi^2}{a}$.

<svg data-fig="model" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja: jaksonajan neliö T toiseen heilurin pituuden l funktiona mallin mukaan. Kuvaaja on origon kautta kulkeva suora. Suoralle on merkitty kaksi pistettä ja niiden välinen muutos: vaakasuunnassa delta l ja pystysuunnassa delta T toiseen. Kulmakerroin on delta T toiseen jaettuna delta l:llä, ja se on neljä pii toiseen jaettuna g:llä. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="280" x2="484" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,280 L483,286 L483,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$l$</div></foreignObject>
  <foreignObject x="80" y="-6.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T^2$</div></foreignObject>
  <polyline points="90,280 451,83.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="204" y1="218" x2="394" y2="218" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="394" y1="218" x2="394" y2="114.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="282.5" y="223.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\Delta l$</div></foreignObject>
  <foreignObject x="404" y="151.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\Delta (T^2)$</div></foreignObject>
  <foreignObject x="105" y="53" width="120" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\dfrac{\Delta (T^2)}{\Delta l} = \dfrac{4\pi^2}{g}$</div></foreignObject>
</svg>

Jos pituus on mitattu joka kerta samasta väärästä kohdasta, esimerkiksi kuulan yläpintaan keskipisteen sijasta, jokaisesta pituudesta puuttuu sama matka. Silloin suora siirtyy, ja kuvaajaan tulee vakiotermi, mutta kulmakerroin ja siitä laskettu $g$ eivät muutu. Tämä on kuvaajasta määrittämisen etu verrattuna yksittäiseen laskuun $g = \dfrac{4\pi^2 l}{T^2}$.
:::

Kuvaajan sovitukseen ja jaksonajan neliön laskemiseen voit käyttää esimerkiksi Graphical Analysis -ohjelmaa tai taulukkolaskentaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukkolaskenta]].

## Epävarmuus ja luotettavuus

Ilmoita putoamiskiihtyvyys muodossa $g = (g \pm \Delta g)\ \text{m/s}^2$ ja perustele, miten arvioit epävarmuuden $\Delta g$. Kerro myös, kuinka suuri ajanoton epävarmuus oli ja miten se vaikutti jaksonajan epävarmuuteen.

::: tuki O OO
**Jaksonajan epävarmuus.** Jos mittaat $N$ heilahduksen ajan ja ajanoton epävarmuus on $\Delta t$, jaksonajan epävarmuus on $\Delta T = \dfrac{\Delta t}{N}$: lähtö- ja pysäytyshetken epävarmuus jakautuu kaikille heilahduksille. Ajanoton epävarmuuden voit arvioida toistojen hajonnasta, esimerkiksi suurimpana poikkeamana keskiarvosta. Kun jaksonaika korotetaan toiseen, suhteellinen epävarmuus kaksinkertaistuu: $\dfrac{\Delta (T^2)}{T^2} = 2\cdot\dfrac{\Delta T}{T}$.

**Kulmakertoimen epävarmuus.** Ohjatussa työtavassa käytä jyrkimmän ja loivimman suoran menetelmää. Osittain ohjatussa työtavassa valitse jompikumpi tapa:

- **Sovitusohjelman keskivirhe.** Monet ohjelmat ilmoittavat kulmakertoimen keskivirheen. Käytä sitä epävarmuutena $\Delta a$.
- **Jyrkin ja loivin suora.** Piirrä jyrkin ja loivin suora, jotka vielä sopivat pisteisiin niiden epävarmuuksien rajoissa. Määritä niiden kulmakertoimet $a_\text{max}$ ja $a_\text{min}$ ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta a = \dfrac{a_\text{max} - a_\text{min}}{2}$.

Koska $g = \dfrac{4\pi^2}{a}$, putoamiskiihtyvyyden suhteellinen epävarmuus on sama kuin kulmakertoimen: $\dfrac{\Delta g}{g} = \dfrac{\Delta a}{a}$. Pyöristä $\Delta g$ yhteen merkitsevään numeroon ja $g$ samaan desimaaliin.
:::

Vertaa tulostasi taulukkokirjan arvoon, joka on annettu paikkakunnallesi tai lähimmälle paikkakunnalle: mahtuuko taulukkoarvo epävarmuusvälisi sisään? Jos mahtuu, tulos on sopusoinnussa taulukkoarvon kanssa. Jos ei mahdu, etsi syy mittauksistasi.

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet tulosta? Toteutuivatko mallin ehdot mittauksessasi? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Miten jaksonaika riippuu heilurin pituudesta, ja kuinka suuri putoamiskiihtyvyys on epävarmuuksineen? Viittaa kuvaajaan, esimerkiksi "kuvaajasta 1 nähdään, että …". Vaikuttivatko kuulan massa ja heilahduskulma pienillä kulmilla jaksonaikaan tarkistusmittauksesi perusteella, eli erosivatko jaksonajat toisistaan enemmän kuin niiden epävarmuus? Vertaa tätä ennusteeseesi 1. Perustele tarkistusmittauksen tuloksen avulla, miksi muutit juuri sitä suuretta, jota muutit, ja miksi pidit muut vakioina. Vertaa tulosta muihin ennusteisiisi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** heilurin jaksonajan malli ehtoineen ja miksi valitsemillasi akseleilla kuvaaja on suora.
- **Koejärjestely ja menetelmä:** mitä muutit, mitä mittasit ja mitä pidit vakiona, miten mittasit pituuden ja miten jaksonajan sekä miten testasit massan ja heilahduskulman vaikutuksen.
- **Mittaustulokset:** jokainen toisto omassa sarakkeessaan ja lasketut suureet niiden oikealla puolella.
- **Tulos:** $g = (g \pm \Delta g)\ \text{m/s}^2$ oikein pyöristettynä ja vertailu taulukkoarvoon.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet, niiden vaikutuksen suunta ja mallin ehtojen toteutuminen.

## Laajennus: suuret heilahduskulmat

Pienten kulmien malli on likimääräinen: todellisuudessa jaksonaika kasvaa hieman, kun heilahduskulma kasvaa. Tutki, kuinka suuri heilahduskulma voi olla ennen kuin ero näkyy mittauksissasi, ja arvioi, oliko päämittauksesi heilahduskulma riittävän pieni.

Pidä heilurin pituus vakiona ja mittaa jaksonaika usealla heilahduskulmalla, pienestä kulmasta noin $45^\circ$:een. Kohtalaisilla kulmilla jaksonaikaa kuvaa hyvin malli

```latex
T = T_0\left(1 + \frac{\theta^2}{16}\right)
```

missä $T_0 = 2\pi\sqrt{\dfrac{l}{g}}$ on pienten kulmien mallin jaksonaika ja heilahduskulma $\theta$ on radiaaneina. Piirrä kuvaaja, joka on mallin mukaan suora, ja tarkista, noudattavatko mittauksesi mallia. Millä heilahduskulmalla jaksonajan kasvu ylittää jaksonajan epävarmuuden?

::: tuki O OO
**Vihjeitä.** Valitse pystyakselille jaksonaika $T$ ja vaaka-akselille heilahduskulman neliö $\theta^2$. Mallin mukaan kuvaaja on suora, jonka vakiotermi on $T_0$ ja kulmakerroin $\dfrac{T_0}{16}$. Muunna asteet radiaaneiksi: $\theta\ (\text{rad}) = \dfrac{\pi}{180^\circ}\cdot\theta\ (^\circ)$. Kulman voit mitata kulmamittarilla ripustuskohdasta tai laskea kuulan vaakasuorasta siirtymästä $x$: $\sin\theta = \dfrac{x}{l}$. Suurilla kulmilla heilahdus pienenee ilmanvastuksen takia nopeammin, joten mittaa harvempien heilahdusten aika ja kirjaa, kuinka paljon kulma pieneni mittauksen aikana.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
