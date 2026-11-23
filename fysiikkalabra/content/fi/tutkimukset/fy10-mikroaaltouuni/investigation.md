# Valonnopeuden määrittäminen mikroaaltouunilla

> **Tutkimuskysymys:** Miten mikroaaltouunissa syntyvästä seisovasta aallosta voidaan määrittää mikroaaltojen aallonpituus, ja kuinka suureksi valonnopeus saadaan sen ja uunin taajuuden avulla?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: mikroaaltouuni laboratorion työpöydällä. Uunin luukku on kiinni ja uuni on pois päältä. Luukun ikkunasta näkyy uunin pohjalla lautanen, jolle on levitetty tasainen kerros juustoraastetta, ja sen vieressä kuppi vettä. Pöydällä uunin vieressä on mitta-asteikko, patalappu ja kulho juustoraastetta." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-mikroaaltouuni-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

Valo kulkee sekunnissa noin seitsemän ja puoli kertaa maapallon ympäri, joten sen nopeutta ei voi mitata kellolla ja mittanauhalla. Mikroaaltouuni tarjoaa kiertotien: uunin mikroaallot ovat sähkömagneettista säteilyä kuten valo, ja niiden aallonpituuden voi selvittää juustoraasteen avulla. Tässä tutkimuksessa määrität mikroaaltojen aallonpituuden ja lasket siitä valonnopeuden. Mittaa, laske ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** mikroaaltojen aallonpituus uunissa syntyvän seisovan aallon avulla, siitä ja uunin taajuudesta laskettu valonnopeus epävarmuuksineen sekä se, onko tulos sopusoinnussa valonnopeuden tunnetun arvon kanssa.

**Päätät itse (osittain ohjattu työtapa):** miten kuumennat juustoa (tehoasetus ja yksittäisen kuumennusjakson pituus), mistä riveistä ja suunnista mittaat sulaneiden kohtien välit, kuinka monen välin yhteispituuden mittaat ja montako riviä tai toistoa teet, miten paikannat sulaneen kohdan keskikohdan sekä tavan, jolla arvioit tuloksen epävarmuuden. Kirjaa valintasi perusteluineen. Ohjatussa työtavassa sivu kiinnittää useimmat näistä valinnoista puolestasi.

Uunin valmistelee opettaja, eikä sen turvallisuudesta päätetä itse: noudata kohdan Suunnittele turvallisuusohjeita kaikissa työtavoissa.

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Millaisen kuvion arvelet syntyvän tasaiseen juustokerrokseen, kun sitä kuumennetaan hetken uunissa, jonka alusta ei pyöri? Miksi mikroaaltouunin alusta tavallisesti pyörii?
2. Jos juustoon sulaa toisistaan erillisiä kohtia, miten kahden vierekkäisen kohdan välinen etäisyys voisi liittyä mikroaaltojen aallonpituuteen?
3. Kuinka kaukana toisistaan arvelet sulaneiden kohtien olevan: millimetrejä, senttimetrejä vai kymmeniä senttimetrejä?
4. Mitä arvelet sulaneille kohdille tapahtuvan, jos juustoa kuumennetaan liian kauan, ja miten se vaikuttaisi mittaukseen?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Teoriaa lyhyesti

**Aallon nopeus.** Aallon etenemisnopeus $v$, taajuus $f$ ja aallonpituus $\lambda$ liittyvät toisiinsa aaltoyhtälöllä

```latex
v = f\lambda
```

Taajuuden yksikkö on hertsi, $1\,\text{Hz} = 1\,\tfrac{1}{\text{s}}$. Aaltoliikettä käsitellään tarkemmin moduulissa FY5.

**Mikroaallot.** Mikroaaltouunin mikroaallot ovat sähkömagneettista säteilyä, samaa ilmiötä kuin valo ja radioaallot, mutta niiden aallonpituus on paljon suurempi kuin valon. Kaikki sähkömagneettinen säteily etenee tyhjiössä samalla nopeudella, valonnopeudella $c$, ja ilmassa käytännössä yhtä nopeasti. Siksi mikroaaltojen etenemisnopeus on valonnopeus: $c = f\lambda$. Sähkömagneettista säteilyä käsitellään moduulissa FY7. Mikroaaltojen taajuus on uunin ominaisuus, ja se on merkitty uunin arvokilpeen tai käyttöohjeeseen.

**Seisova aalto.** Uunin metalliseinät heijastavat mikroaallot. Kun kaksi samantaajuista aaltoa etenee vastakkaisiin suuntiin, ne yhdistyvät seisovaksi aalloksi. Seisovassa aallossa on kohtia, joissa sähkökenttä ei värähtele lainkaan (**solmukohdat**), ja niiden puolivälissä kohtia, joissa se värähtelee voimakkaimmin (**kupukohdat**). Kuvio pysyy paikallaan. Kahden vierekkäisen kupukohdan välinen etäisyys on puolet aallonpituudesta, samoin kahden vierekkäisen solmukohdan välinen etäisyys. Seisovia aaltoja käsitellään moduulissa FY5.

<svg data-fig="standing" viewBox="0 0 600 360" role="img" aria-label="Kaaviokuva yksinkertaisesta mallista. Kahden metalliseinän välissä on seisova aalto. Kiinteä viiva ja katkoviiva näyttävät sähkökentän värähtelyn ääriasennot. Solmukohdissa, myös seinien kohdalla, kenttä ei värähtele. Kupukohdissa, solmukohtien puolivälissä, värähtely on suurin. Alla olevassa juustokerroksessa on sulanut kohta jokaisen kupukohdan alla. Kahden vierekkäisen kupukohdan välinen etäisyys on puolet aallonpituudesta, lambda per kaksi." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-mikroaaltouuni-standing.webp" x="0" y="0" width="600" height="367.5" preserveAspectRatio="none"/>
  <foreignObject x="182.5" y="15.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kupukohta}$</div></foreignObject>
  <foreignObject x="348.5" y="15.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{solmukohta}$</div></foreignObject>
  <foreignObject x="405" y="297" width="20" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\dfrac{\lambda}{2}$</div></foreignObject>
  <foreignObject x="70" y="297.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{juustokerros}$</div></foreignObject>
</svg>

**Miksi juusto sulaa kohdittain.** Mikroaallot lämmittävät ruokaa, koska värähtelevä sähkökenttä saa ruoan vesimolekyylit liikkeeseen, ja energia muuttuu sisäenergiaksi. Mitä voimakkaammin kenttä värähtelee, sitä nopeammin ruoka lämpenee. Kun alusta ei pyöri, ruoka lämpenee eniten kupukohdissa.

**Mallin rajat.** Yllä oleva malli on yksinkertaistettu: siinä aallot etenevät edestakaisin yhdessä suunnassa. Todellisessa uunissa mikroaallot heijastuvat kaikista seinistä, ja kuvio on usean seisovan aallon yhdistelmä. Siksi sulaneiden kohtien väli voi jossakin suunnassa poiketa puolesta aallonpituudesta, ja kuvio voi olla epäsäännöllinen. Lisäksi lämpö johtuu juustossa, joten sulaneet kohdat laajenevat ja lopulta yhtyvät, jos kuumennus jatkuu. Juustokerros, lautanen ja vesikuppi muuttavat kuviota jonkin verran, mutta niiden vaikutus aallonpituuteen ilmassa jätetään mallissa huomiotta.

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, miten saat juustoon selvästi erottuvat sulaneet kohdat, mitä mittaat ja miten luet uunin taajuuden.

**Turvallisuus.** Noudata sivun alun Turvallisuus-kohdan ohjeita koko työn ajan. Uunin käyttö ja alustan poisto kuuluvat opettajalle.

**Taajuus.** Lue mikroaaltojen taajuus uunin arvokilvestä ja kirjaa se yksikköineen. Arvokilvessä on yleensä myös sähköverkon taajuus, joka on eri asia kuin mikroaaltojen taajuus. Jos et löydä mikroaaltojen taajuutta, kysy opettajalta: se on uunin käyttöohjeessa. [[apua:fy1-2|Kerrannaisyksiköt]]

::: tuki O
**Ohjattu.** Levitä mikroaaltouuniin sopivalle tasaiselle lautaselle ohut ja tasainen kerros juustoraastetta niin, että lautasen pohja ei näy. Aseta lautanen uuniin opettajan neuvomaan kohtaan, ja kuppi vettä uunin reunalle, aina samaan kohtaan. Kuumenna opettajan kertomalla tehoasetuksella opettajan kertomissa lyhyissä jaksoissa ja katso luukun ikkunasta välillä. Lopeta, kun juustoon on sulanut selvästi erottuvia kohtia, ennen kuin ne alkavat yhtyä toisiinsa. Ota lautanen uunista patalapulla. Etsi ainakin kolme riviä, joissa on vähintään neljä sulanutta kohtaa samalla suoralla, ja mittaa jokaisesta rivistä ensimmäisen ja viimeisen kohdan keskikohtien välinen etäisyys $L$. Kirjaa myös, montako väliä $n$ etäisyyteen sisältyy.

<svg data-fig="spots" viewBox="0 0 600 380" role="img" aria-label="Kaaviokuva ylhäältä katsottuna. Lautasella on juustokerros, johon on sulanut kohtia. Neljä sulanutta kohtaa on samalla suoralla. Niiden keskikohdat on merkitty rastilla. Ensimmäisen ja viimeisen kohdan keskikohtien välinen etäisyys L kattaa kolme kohtien väliä." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-mikroaaltouuni-spots.webp" x="1.2" y="2.5" width="597" height="384.3" preserveAspectRatio="none"/>
  <foreignObject x="290" y="341.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$L$</div></foreignObject>
  <foreignObject x="425" y="315.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{3 väliä}$</div></foreignObject>
</svg>
:::

::: tuki OO
**Osittain ohjattu.** Päätä itse, miten kuumennat juustoa niin, että kohdat erottuvat mutta eivät yhdy, mistä riveistä mittaat ja montako väliä kukin mittaus kattaa. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Miksi kannattaa mitata usean välin yhteispituus eikä yhtä väliä?
- Miten paikannat sulaneen kohdan keskikohdan, kun kohta on leveä ja reunoiltaan epäselvä?
- Miten vesikuppi voi vaikuttaa kuvioon sen lähellä?
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle. Kirjaa myös uunin taajuus ja tehoasetus sekä vesikupin paikka.

::: tuki O
Voit käyttää esimerkiksi tällaista taulukkoa:

| Rivi | $n$ (välejä) | $L\ (\text{m})$ | $d = \dfrac{L}{n}\ (\text{m})$ |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

Aseta mitta lautaselle juustokerroksen viereen tai päälle vasta, kun lautanen on otettu uunista. Lue kummankin kohdan keskikohta samalla tavalla ja katso asteikkoa kohtisuoraan.
:::

Muista mittausepävarmuus: kirjaa, kuinka tarkasti pystyt paikantamaan sulaneen kohdan keskikohdan. Se on yleensä paljon epätarkempaa kuin mitan asteikko. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Merkitään kahden vierekkäisen sulaneen kohdan välistä etäisyyttä $d$. Vastaa:

1. Johda teorian avulla lauseke, jolla valonnopeus $c$ lasketaan mitatusta etäisyydestä $d$ ja taajuudesta $f$.
2. Laske jokaisesta rivistä etäisyys $d$ ja niiden keskiarvo $\bar{d}$. Laske siitä aallonpituus ja valonnopeus. Muista muuttaa taajuus perusyksikköön hertsi.
3. Olivatko eri rivien etäisyydet yhtä suuria? Jos eivät, mistä ero voi johtua?
4. Perustele, miksi usean välin yhteispituuden mittaaminen antaa tarkemman tuloksen kuin yhden välin mittaaminen.

::: tuki O
**Tarkista lausekkeesi.** Vierekkäisten kupukohtien väli on puolet aallonpituudesta, joten $\lambda = 2d$, ja valonnopeus on

```latex
c = f\lambda = 2fd
```

missä $f$ on mikroaaltojen taajuus ja $d$ vierekkäisten sulaneiden kohtien välinen etäisyys.
:::

## Epävarmuus ja luotettavuus

Ilmoita valonnopeus muodossa $c = (c \pm \Delta c)\,\text{m/s}$ ja perustele, miten arvioit epävarmuuden $\Delta c$.

::: tuki O
**Epävarmuus vaihe vaiheelta.**

- **Etäisyys $L$.** Se on kahden paikkalukeman erotus, joten sen epävarmuus on lukemien epävarmuuksien summa: $\Delta L = \Delta x_\text{alku} + \Delta x_\text{loppu}$, missä $\Delta x$ on se tarkkuus, jolla paikannat kohdan keskikohdan.
- **Etäisyys $d$.** Kun $d = \dfrac{L}{n}$, sen epävarmuus on $\Delta d = \dfrac{\Delta L}{n}$. Vertaa tätä myös siihen, kuinka paljon eri rivien tulokset vaihtelevat: käytä suurempaa näistä.
- **Taajuus $f$.** Arvokilven arvo on uunin nimellinen taajuus. Jos uunin käyttöohjeessa on valmistajan ilmoittama taajuuden toleranssi, käytä sitä epävarmuutena $\Delta f$; kysy sitä opettajalta. Kilven viimeisen numeron perusteella arvioitu epävarmuus on liian pieni, koska uunin todellinen taajuus voi poiketa kilven arvosta enemmän.
- **Valonnopeus $c$.** Tulon suhteellinen epävarmuus on tekijöiden suhteellisten epävarmuuksien summa: $\dfrac{\Delta c}{c} = \dfrac{\Delta f}{f} + \dfrac{\Delta d}{d}$. Kerroin 2 on tarkka, eikä se lisää epävarmuutta.

Pyöristä $\Delta c$ yhteen merkitsevään numeroon ja $c$ samaan tarkkuuteen.
:::

::: tuki OO
Mieti, mistä lukemista etäisyyden $L$ epävarmuus muodostuu, miten se jakautuu välien kesken, ja miten etäisyyden ja taajuuden epävarmuudet yhdistyvät valonnopeuden epävarmuudeksi. Valitse menetelmä ja perustele se.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet tulosta? Ota huomioon myös mallin rajat: noudattiko kuvio yksinkertaista mallia, jossa kohtien väli on puolet aallonpituudesta? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Vertaa tulostasi valonnopeuden tunnettuun arvoon $c = 2{,}998 \cdot 10^8\,\text{m/s}$: onko tunnettu arvo epävarmuusvälisi sisällä? Jos on, tulos on sopusoinnussa tunnetun arvon kanssa, mutta se ei todista mallia oikeaksi. Jos ei ole, mikä systemaattinen virhe tai mallin oletus voisi selittää eron? Vertaa tulosta ennusteisiisi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** seisova aalto, miksi juusto sulaa kupukohdissa ja miten lauseke valonnopeudelle saadaan.
- **Koejärjestely ja menetelmä:** kuva järjestelystä, miten kuumensit juuston ja mittasit kohtien välit sekä työturvallisuus (vesikuppi, ei metallia, alusta ei pyöri: poistettu käyttöohjeen mukaan).
- **Mittaustulokset:** alkuperäiset etäisyydet ja välien määrät omissa sarakkeissaan, uunin taajuus ja sen lähde.
- **Tulos:** $c = (c \pm \Delta c)\,\text{m/s}$ oikein pyöristettynä.
- **Luotettavuus:** kohtien paikantamisen epätarkkuus, taajuuden epävarmuus ja mallin rajat sekä niiden vaikutuksen suunta.

## Laajennus: kohtien paikat kuvaajana kahdessa suunnassa

Yksinkertainen malli olettaa, että sulaneiden kohtien väli on sama joka suunnassa. Testaa oletusta. Valitse kaksi toisiaan vastaan kohtisuoraa suuntaa, esimerkiksi uunin leveyden ja syvyyden suunnat, ja mittaa kummastakin suunnasta rivin jokaisen sulaneen kohdan keskikohdan paikka $x_k$ mitan asteikolta. Numeroi kohdat järjestyksessä $k = 1, 2, 3, \ldots$

Jos kohdat ovat tasavälein, paikka järjestysnumeron funktiona on suora, jonka kulmakerroin on vierekkäisten kohtien välinen etäisyys $d$. Vakiotermi riippuu vain siitä, mihin mitan nollakohta asetettiin.

<svg data-fig="model" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja: sulaneen kohdan keskikohdan paikka x k järjestysnumeron k funktiona mallin mukaan. Kuvaaja on suora, jonka kulmakerroin on vierekkäisten kohtien välinen etäisyys d, joka on mallin mukaan lambda per kaksi. Suora ei kulje origon kautta, koska ensimmäisen kohdan paikka riippuu siitä, mihin mitan nollakohta asetetaan. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="300" x2="474" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M486,300 L473,306 L473,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="301" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="157.5" y1="300" x2="157.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="147.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="224.5" y1="300" x2="224.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="214.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="292" y1="300" x2="292" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="282" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="359" y1="300" x2="359" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="349" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="426.5" y1="300" x2="426.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="416.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <foreignObject x="60" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="492" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$k$</div></foreignObject>
  <foreignObject x="104" y="15.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$x_k$</span></div></foreignObject>
  <polyline points="123.5,250 440,62" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="224.5" y1="190" x2="292" y2="190" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="292" y1="190" x2="292" y2="150" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="302" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$d$</div></foreignObject>
  <foreignObject x="248" y="193.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1$</div></foreignObject>
  <foreignObject x="117" y="46" width="195" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kulmakerroin } d = \dfrac{\lambda}{2}$</div></foreignObject>
</svg>

Piirrä kummastakin suunnasta kuvaaja ja sovita pisteisiin suora. Ovatko pisteet suoralla? Ovatko kahden suunnan kulmakertoimet sopusoinnussa keskenään ja päämittauksen tuloksen kanssa? Päällekkäiset epävarmuusvälit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi. Mitä mahdollinen ero kertoo yksinkertaisen mallin pätevyydestä? [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

::: tuki O OO
**Vihjeitä.** Pidä mitta paikallaan koko rivin lukemisen ajan, jotta kaikki paikat luetaan samasta nollakohdasta. Kulmakerroin ei riipu nollakohdasta. Sovitusohjelman ilmoittama kulmakertoimen keskivirhe käy kulmakertoimen epävarmuudeksi. Kuvaajan sovitukseen käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi mittaustuloksiin vai siihen, mitä odotit tunnetun arvon perusteella?
- Mitä tekisit toisin, jos aloittaisit alusta?
