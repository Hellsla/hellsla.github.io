# Ideaalikaasun tilanyhtälö $pV = nRT$

> **Miksi** heliumpallo on paljon kevyempi kuin samankokoinen ilmapallo? Onko siinä vähemmän kaasua?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: huoneessa kaksi samankokoista ilmapalloa. Heliumpallo on noussut kattoon ja sen naru roikkuu alas, tavallinen ilmalla täytetty pallo lepää lattialla." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-10-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Luvun *Kaasujen tilanmuutokset ja Boylen laki* kaasulait koskivat suljettua kaasumäärää. Nyt verrataan eri kaasumääriä ja eri kaasuja. Kun $5{,}00$ litran pallo täytetään paineessa $101\,\text{kPa}$ ja lämpötilassa $20\,{}^\circ\text{C}$ vuorotellen heliumilla, typellä, ilmalla ja hiilidioksidilla, kaasujen massat ovat esimerkkipunnituksessa (keksityt arvot, joissa on punnituksen hajontaa) hyvin erilaiset: $0{,}83\,\text{g}$, $5{,}78\,\text{g}$, $6{,}02\,\text{g}$ ja $9{,}10\,\text{g}$. Kun kunkin massa jaetaan kaasun moolimassalla, tulos on kuitenkin joka kerta noin $0{,}207\,\text{mol}$. Samassa paineessa ja lämpötilassa yhtä suuressa tilavuudessa on siis yhtä paljon kaasua, olipa kaasu mitä tahansa. Heliumpallo on kevyempi, koska heliumhiukkaset ovat kevyempiä, ei siksi, että kaasua olisi vähemmän.

<svg data-fig="helium-ilma" viewBox="0 0 600 326" role="img" aria-label="Havainnekuva, hiukkaset kuvattu suurennettuina: kaksi yhtä suurta kaasupalloa samassa paineessa ja lämpötilassa. Kummassakin on yhtä monta hiukkasta ja ainemäärä n = 0,21 mol. Heliumpallon kaasun massa on m = 0,83 g ja ilmapallon m = 6,0 g, koska ilman hiukkaset ovat raskaampia. Nuolet näyttävät hiukkasten liikkeen mittakaavassa: kevyet heliumhiukkaset liikkuvat samassa lämpötilassa nopeammin, nuolen pituus on nopeuden suhde 2,7 : 1." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-10-helium-ilma.webp" x="3.7" y="-1.2" width="594.1" height="331.7" preserveAspectRatio="none"/>
  <foreignObject x="108.5" y="231.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{helium}$</div></foreignObject>
  <foreignObject x="83.5" y="263.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$n = 0{,}21\,\text{mol}$</div></foreignObject>
  <foreignObject x="96" y="295.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m = 0{,}83\,\text{g}$</div></foreignObject>
  <foreignObject x="421" y="231.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ilma}$</div></foreignObject>
  <foreignObject x="383.5" y="263.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$n = 0{,}21\,\text{mol}$</div></foreignObject>
  <foreignObject x="402.5" y="295.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m = 6{,}0\,\text{g}$</div></foreignObject>
  <foreignObject x="271" y="93.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{sama}$</div></foreignObject>
  <foreignObject x="275.5" y="123.5" width="49" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$p,\ T$</div></foreignObject>
</svg>

Hiukkasia on pienessäkin kaasumäärässä valtavasti, joten niitä ei lasketa yksitellen vaan mooleina, samaan tapaan kuin kananmunia lasketaan tusinoina. Yksi mooli on ${6{,}022 \cdot 10^{23}}$ hiukkasta, ja lukua ${N_\text{A} = 6{,}022 \cdot 10^{23}\,\text{1/mol}}$ sanotaan Avogadron vakioksi. Ainemäärä $n$ kertoo, montako moolia hiukkasia on. Yhden moolin massa on aineen moolimassa $M$: heliumilla $4{,}00\,\text{g/mol}$, ilmalla keskimäärin $29{,}0\,\text{g/mol}$ ja hiilidioksidilla $44{,}0\,\text{g/mol}$. Ainemäärä saadaan siis sekä hiukkasmäärästä että massasta:
```kaavat
ainemäärä Avogadron vakion avulla :: n = \frac{N}{N_\text{A}}
ainemäärä :: n = \frac{m}{M}
```
missä $N$ on hiukkasten lukumäärä, $m$ massa (g tai kg) ja $M$ moolimassa (g/mol tai kg/mol).

<svg data-fig="mole-masses" viewBox="0 0 600 316" role="img" aria-label="Havainnekuva, hiukkaset suurennettuina ja kaavamaisina: kolme yhtä suurta astiaa samassa paineessa ja lämpötilassa, kussakin yhtä monta hiukkasta eli ainemäärä n = 1,00 mol. Moolimassa on heliumilla 4,00 g/mol, ilmalla 29,0 g/mol ja hiilidioksidilla 44,0 g/mol. Palkki jokaisen astian alla on kaasun massa mittakaavassa: yksi mooli painaa eri kaasuilla eri verran." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-10-mole-masses.webp" x="0" y="0" width="603" height="325.4" preserveAspectRatio="none"/>
  <foreignObject x="14" y="153.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{helium}$</div></foreignObject>
  <foreignObject x="14" y="183.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M = 4{,}00\,\text{g/mol}$</div></foreignObject>
  <foreignObject x="14" y="243.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 4{,}00\,\text{g}$</div></foreignObject>
  <foreignObject x="214" y="153.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ilma}$</div></foreignObject>
  <foreignObject x="214" y="183.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M = 29{,}0\,\text{g/mol}$</div></foreignObject>
  <foreignObject x="214" y="243.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 29{,}0\,\text{g}$</div></foreignObject>
  <foreignObject x="414" y="153.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{hiilidioksidi}$</div></foreignObject>
  <foreignObject x="414" y="183.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M = 44{,}0\,\text{g/mol}$</div></foreignObject>
  <foreignObject x="414" y="243.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 44{,}0\,\text{g}$</div></foreignObject>
  <foreignObject x="20" y="281.5" width="560" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kussakin astiassa }n = 1{,}00\,\text{mol},\ \text{sama }p, T$</div></foreignObject>
</svg>

```pysahdy
Heliumin moolimassa on $4{,}00\,\text{g/mol}$. Kuinka monta moolia on $8{,}0\,\text{g}$ heliumia?
---
Ainemäärä on $n = m/M$, joten $n = 8{,}0\,\text{g}/4{,}00\,\text{g/mol} = 2{,}0\,\text{mol}$.
```

Ideaalikaasu on mikromalli. Siinä hiukkaset ajatellaan pistemäisiksi, ja ne vaikuttavat toisiinsa ja astian seinämiin vain törmätessään. Siksi hiukkasten välisten vuorovaikutusten energia on mallissa merkityksetön, ja kelvinlämpötila on suoraan verrannollinen hiukkasten keskimääräiseen liike-energiaan. Paine syntyy seinämiin osuvista törmäyksistä, ja se kasvaa, kun hiukkasia on enemmän, kun ne liikkuvat nopeammin eli lämpötila on korkeampi tai kun tilavuus on pienempi. Todelliset kaasut noudattavat mallia hyvin tavallisissa oloissa. Malli alkaa pettää suurissa paineissa ja matalissa lämpötiloissa, kun hiukkaset ovat lähellä toisiaan ja niiden välinen vetovoima tiivistää kaasun nesteeksi.

## Kaava: Ideaalikaasun tilanyhtälö
Esimerkkipunnituksesta saadaan luku, joka on kaikille kaasuille sama: paine kerrottuna tilavuudella ja jaettuna ainemäärällä ja kelvinlämpötilalla. Neljän kaasun keskimääräisellä ainemäärällä $0{,}2071\,\text{mol}$ se on
```latex
\begin{aligned}
R &= \frac{pV}{nT} \\
&= \frac{101\,000\,\text{Pa} \cdot 0{,}00500\,\text{m}^3}{0{,}2071\,\text{mol} \cdot 293{,}15\,\text{K}} \\
&\approx 8{,}3\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}
\end{aligned}
```
Tarkat mittaukset antavat kaikille kaasuille arvon $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$, kun paine ei ole kovin suuri eikä lämpötila kovin matala. Lukua sanotaan mooliseksi kaasuvakioksi. Siitä saadaan ideaalikaasun tilanyhtälö
```kaavat
ideaalikaasun tilanyhtälö :: pV = nRT
```
missä $p$ on kaasun absoluuttinen paine, $V$ tilavuus, $n$ ainemäärä, $R$ moolinen kaasuvakio ja $T$ kelvinlämpötila. Kaasun laatu ei näy yhtälössä lainkaan. Celsiusasteina annettu lämpötila $\theta$ muutetaan kelvineiksi lisäämällä lukuarvoon $273{,}15$.

```pysahdy
Kaksi samankokoista palloa on samassa paineessa ja lämpötilassa, toisessa heliumia ja toisessa ilmaa. Onko niissä yhtä paljon kaasua?
---
On. Kaasun laatu ei näy yhtälössä $pV = nRT$, joten sama $p$, $V$ ja $T$ tarkoittavat samaa ainemäärää $n$. Massat eroavat, koska moolimassat eroavat.
```

Kun käytetään kaasuvakion arvoa
```latex
R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}
```
tulon $pV$ yksikön on oltava joule. Tavallisesti paine muunnetaan pascaleiksi ja tilavuus kuutiometreiksi, jolloin
```latex
1\,\text{Pa} \cdot \text{m}^3 = 1\,\tfrac{\text{N}}{\text{m}^2} \cdot \text{m}^3 = 1\,\text{N} \cdot \text{m} = 1\,\text{J}
```
Myös kilopascalien ja litrojen yhdistelmä on mahdollinen, sillä
```latex
1\,\text{kPa} \cdot \textsf{l} = 1000\,\text{Pa} \cdot 0{,}001\,\text{m}^3 = 1\,\text{J}
```
Tärkeintä on käsitellä yksiköt johdonmukaisesti koko laskun ajan.

Kun tilanyhtälö ratkaistaan paineen suhteen, nähdään, että paine kaksinkertaistuu, kun hiukkasten lukumäärä tai kelvinlämpötila kaksinkertaistuu tai kun tilavuus puolittuu. Paine on siis suoraan verrannollinen hiukkasten lukumäärään ja kelvinlämpötilaan ja kääntäen verrannollinen tilavuuteen, eli $p \propto NT/V$.

<svg data-fig="paine-ja-tekijat" viewBox="0 0 600 300" role="img" aria-label="Kaavakuva neljästä männällä suljetusta kaasusylinteristä, hiukkaset suurennettuina. Vasemmalta oikealle: lähtötilassa hiukkasmäärä N, lämpötila T ja tilavuus V, ja paine on p. Paine on 2p, kun hiukkasia on kaksi kertaa enemmän (2N), kun kelvinlämpötila on kaksinkertainen (2T) eli hiukkaset liikkuvat nopeammin, tai kun mäntä on painettu puoleen tilavuuteen (V/2). Nuolten pituus kuvaa hiukkasten nopeutta." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-10-paine-ja-tekijat.webp" x="1.2" y="0" width="597" height="307.2" preserveAspectRatio="none"/>
  <foreignObject x="36" y="211.5" width="78" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N,\ T,\ V$</div></foreignObject>
  <foreignObject x="65" y="251.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p$</div></foreignObject>
  <foreignObject x="180" y="211.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2N,\ T,\ V$</div></foreignObject>
  <foreignObject x="208.5" y="251.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2p$</div></foreignObject>
  <foreignObject x="330" y="211.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N,\ 2T,\ V$</div></foreignObject>
  <foreignObject x="358.5" y="251.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2p$</div></foreignObject>
  <foreignObject x="473.5" y="211.5" width="103" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N,\ T,\ V/2$</div></foreignObject>
  <foreignObject x="508.5" y="251.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2p$</div></foreignObject>
</svg>

```pysahdy
Kaasun kelvinlämpötila kaksinkertaistuu ja tilavuus kaksinkertaistuu. Hiukkasmäärä pysyy samana. Mitä paineelle tapahtuu?
---
Paine ei muutu, koska $p \propto NT/V$ ja kaksi tekijää 2 supistuu pois.
```

Simulaatiossa voit tutkia tätä hiukkasten tasolla: muuta hiukkasten määrää, lämpötilaa ja tilavuutta ja vertaa seinämistä mitattua painetta tilanyhtälön ennusteeseen, jonka lasket itse. Hiukkasten keskinäiset törmäykset eivät muuta painetta keskimäärin, joten ne on jätetty simulaatiosta pois. Simulaatiossa paine näytetään suhteessa vertailutilaan ($p/p_\text{ref}$), ei pascaleina. Vertailutila on $N = 100$ hiukkasta, $T = 300\,\text{K}$ ja koko tilavuus ($V = 100\,\%$); siinä $p/p_\text{ref} = 1$, ja arvo 2 tarkoittaa kaksinkertaista vertailupaineeseen verrattuna. Hiukkasmäärä $N$ kuvaa kaasun määrää.

<!-- sim -->

<figure class="unit-photo"><img src="pics/fy3/hot-air-balloon-burner.webp" alt="Kuumailmapallon punaisen kuvun sisään suuntautuu kirkas keltainen liekki. Etualalla ovat korin kiinnitysketjut ja vaijerit."><figcaption>Kuumailmapallon poltin lämmittää pallon sisällä olevaa ilmaa. Pallon suu on alhaalta auki, joten sisäilman paine pysyy lähes ulkoilman paineena.</figcaption></figure>

Kun kaasun määrä ei muutu, $nR$ on vakio, ja tilanyhtälöstä seuraa yhdistetty kaasulaki $p_1V_1/T_1 = p_2V_2/T_2$ (alaindeksit 1 ja 2 ovat alku- ja lopputila). Siitä saadaan jokainen luvun *Kaasujen tilanmuutokset ja Boylen laki* kaasulaki, kun yksi suure pidetään vakiona.

## Esimerkki
Juhlapallo täytetään heliumilla, kunnes sen tilavuus on $5{,}0\,\textsf{l}$. Pallossa paine on $101\,\text{kPa}$ ja lämpötila $20\,{}^\circ\text{C}$. Kuinka monta moolia heliumia pallossa on, ja mikä on heliumin massa? Heliumin moolimassa on $4{,}0\,\text{g/mol}$.

<!-- vaihe -->

**Tunnetut ja kysytty.** Pallon tilavuus $V = 5{,}0\,\textsf{l}$, paine $p = 101\,\text{kPa}$, lämpötila $\theta = 20\,{}^\circ\text{C}$ ja heliumin moolimassa $M = 4{,}0\,\text{g/mol}$.

Kysytään ainemäärää $n$ ja massaa $m$.

<!-- vaihe -->

**Periaate.** Pallossa on tietty määrä heliumia tietyssä tilavuudessa, paineessa ja lämpötilassa, ja helium käyttäytyy tavallisessa paineessa ja huoneenlämmössä ideaalikaasuna. Siksi tilanyhtälö $pV = nRT$ antaa ainemäärän, ja moolimassa muuttaa ainemäärän massaksi.

<!-- vaihe -->

**Kaava ratkaistuna.** Ratkaistaan tilanyhtälöstä ainemäärä ja yhtälöstä $n = m/M$ massa:
```latex
\begin{aligned}
n &= \frac{pV}{RT} \\
m &= nM
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Tilanyhtälö vaatii perusyksiköt:

- tilavuus $V = 5{,}0\,\textsf{l} = 0{,}0050\,\text{m}^3$
- paine $p = 101\,\text{kPa} = 101\,000\,\text{Pa}$
- lämpötila $T = (20 + 273{,}15)\,\text{K} = 293{,}15\,\text{K}$
- moolimassa jää arvoon $M = 4{,}0\,\text{g/mol}$, jolloin massa tulee grammoina

<!-- vaihe -->

**Sijoitus.** Sijoitetaan arvot yksiköineen:
```latex
\begin{aligned}
n &= \frac{pV}{RT} \\
&= \frac{101\,000\,\text{Pa} \cdot 0{,}0050\,\text{m}^3}{8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}} \cdot 293{,}15\,\text{K}} \\
&= 0{,}2073\,\text{mol} \approx 0{,}21\,\text{mol}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Heliumin massa lasketaan tarkemmalla ainemäärällä:
```latex
\begin{aligned}
m &= nM \\
&= 0{,}2073\,\text{mol} \cdot 4{,}0\,\text{g/mol} \\
&\approx 0{,}83\,\text{g}
\end{aligned}
```
Pallossa on $0{,}21\,\text{mol}$ heliumia, ja sen massa on $0{,}83\,\text{g}$. Ainemäärän tarkkuutta rajoittaa tilavuus $5{,}0\,\textsf{l}$, ja massan tarkkuutta rajoittaa lisäksi moolimassa $4{,}0\,\text{g/mol}$; kumpikin on annettu kahdella numerolla, joten tulokset annetaan kahdella merkitsevällä numerolla. Paine $101\,\text{kPa}$ ja lämpötila $293\,\text{K}$ ovat kolmen numeron arvoja eivätkä rajoita.

<!-- vaihe -->

**Järkevyys.** Yksi mooli kaasua vie huoneenlämmössä ja normaalipaineessa noin $24\,\textsf{l}$, joten $5{,}0\,\textsf{l}$ tilavuudessa on noin $5{,}0\,\textsf{l} : 24\,\textsf{l/mol} \approx 0{,}21\,\text{mol}$ kaasua. Samankokoisessa ilmapallossa on yhtä monta moolia ilmaa, mutta sen massa on noin $0{,}2073\,\text{mol} \cdot 29\,\text{g/mol} \approx 6{,}0\,\text{g}$. Heliumpallo on kevyempi, koska heliumhiukkaset ovat kevyempiä, ei siksi, että kaasua olisi vähemmän.

## Yleinen virhekäsitys
Tilanyhtälön laskuissa toistuu kolme virhettä:

- **Celsiusasteet.** Lämpötila on tilanyhtälössä aina kelvineinä. Esimerkiksi $0\,{}^\circ\text{C}$ antaisi paineeksi nollan, mutta kaasulla on paine myös jäätymispisteessä.
- **Sekoitetut yksiköt.** Jos paine on kilopascaleina mutta tilavuus kuutiometreinä tai paine pascaleina mutta tilavuus litroina, tulos on tuhatkertaisesti väärä. Varminta on muuttaa kaikki suureet perusyksiköiksi: paine pascaleiksi, tilavuus kuutiometreiksi ja lämpötila kelvineiksi.
- **Raskas kaasu.** Moni ajattelee, että raskaampaa kaasua mahtuu samaan tilavuuteen vähemmän moolia. Ainemäärä riippuu kuitenkin vain paineesta, tilavuudesta ja lämpötilasta, ei kaasun laadusta. Massa sen sijaan riippuu moolimassasta.

## Tiivistelmä
- Ideaalikaasun tilanyhtälö on $pV = nRT$, missä $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$ ja $T$ on kelvineinä.
- Ainemäärä $n$ kertoo kaasun määrän mooleina: $n = N/{N_\text{A}} = m/M$.
- Paine on verrannollinen lausekkeeseen $NT/V$: paine kaksinkertaistuu, kun hiukkasmäärä tai kelvinlämpötila kaksinkertaistuu tai kun tilavuus puolittuu.
- Kun kaasun määrä pysyy samana, $p_1V_1/T_1 = p_2V_2/T_2$, ja siitä saadaan erilliset kaasulait.
- Samassa paineessa, lämpötilassa ja tilavuudessa on aina yhtä monta moolia kaasua, kaasun laadusta riippumatta; punnitus antaa kaikille kaasuille saman $m/M$.
- Ideaalikaasumalli toimii hyvin tavallisissa oloissa ja pettää suurissa paineissa ja matalissa lämpötiloissa.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: kuumailmapallo leijuu järven yllä. Korin yläpuolella palava liekki lämmittää pallon sisällä olevaa ilmaa." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-10-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
