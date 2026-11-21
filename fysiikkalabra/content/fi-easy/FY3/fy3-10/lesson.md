# Ideaalikaasun tilanyhtälö $pV = nRT$

> **Miksi** heliumpallo on paljon kevyempi kuin samankokoinen ilmapallo? Onko siinä vähemmän kaasua?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: huoneessa on kaksi samankokoista ilmapalloa. Heliumpallo on noussut kattoon, ja sen naru roikkuu alas. Tavallinen ilmalla täytetty pallo on lattialla." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-10-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Luvussa *Kaasujen tilanmuutokset ja Boylen laki* kaasulait koskivat suljettua kaasumäärää. Nyt verrataan eri kaasumääriä ja eri kaasuja.

Täytetään $5{,}00$ litran pallo. Paine on $101\,\text{kPa}$ ja lämpötila $20\,{}^\circ\text{C}$. Täytetään pallo vuorotellen heliumilla, typellä, ilmalla ja hiilidioksidilla. Esimerkkipunnituksessa kaasujen massat ovat hyvin erilaiset: $0{,}83\,\text{g}$, $5{,}78\,\text{g}$, $6{,}02\,\text{g}$ ja $9{,}10\,\text{g}$. Arvot on keksitty, ja niissä on punnituksen hajontaa. Jaetaan sitten kunkin kaasun massa kaasun moolimassalla. Tulos on joka kerta noin $0{,}207\,\text{mol}$. Samassa paineessa ja lämpötilassa yhtä suuressa tilavuudessa on siis yhtä paljon kaasua. Kaasun laji ei vaikuta tähän. Heliumpallo on kevyempi, koska heliumhiukkaset ovat kevyempiä. Syy ei ole se, että kaasua olisi vähemmän.

<svg data-fig="helium-ilma" viewBox="0 0 600 326" role="img" aria-label="Havainnekuva, hiukkaset suurennettuina. Kaksi yhtä suurta kaasupalloa on samassa paineessa ja lämpötilassa. Kummassakin on yhtä monta hiukkasta ja ainemäärä n = 0,21 mol. Heliumpallon kaasun massa on m = 0,83 g. Ilmapallon kaasun massa on m = 6,0 g, koska ilman hiukkaset ovat raskaampia. Nuolet näyttävät hiukkasten liikkeen mittakaavassa. Kevyet heliumhiukkaset liikkuvat samassa lämpötilassa nopeammin. Nuolen pituus on nopeuden suhde 2,7 : 1." style="max-width:100%;font-size:24px">
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

Pienessäkin kaasumäärässä on valtavasti hiukkasia. Siksi niitä ei lasketa yksitellen. Ne lasketaan mooleina, samaan tapaan kuin kananmunia lasketaan tusinoina. Yksi mooli on ${6{,}022 \cdot 10^{23}}$ hiukkasta. Luku ${N_\text{A} = 6{,}022 \cdot 10^{23}\,\text{1/mol}}$ on Avogadron vakio. Ainemäärä $n$ kertoo, montako moolia hiukkasia on. Yhden moolin massa on aineen moolimassa $M$. Heliumin moolimassa on $4{,}00\,\text{g/mol}$, ilman keskimäärin $29{,}0\,\text{g/mol}$ ja hiilidioksidin $44{,}0\,\text{g/mol}$. Ainemäärän voi siis laskea kahdella tavalla: hiukkasmäärästä tai massasta.
```kaavat
ainemäärä Avogadron vakion avulla :: n = \frac{N}{N_\text{A}}
ainemäärä :: n = \frac{m}{M}
```
Tässä $N$ on hiukkasten lukumäärä, $m$ massa (g tai kg) ja $M$ moolimassa (g/mol tai kg/mol).

<svg data-fig="mole-masses" viewBox="0 0 600 316" role="img" aria-label="Havainnekuva, hiukkaset suurennettuina ja kaavamaisina. Kolme yhtä suurta astiaa on samassa paineessa ja lämpötilassa. Kussakin on yhtä monta hiukkasta eli ainemäärä n = 1,00 mol. Moolimassa on heliumilla 4,00 g/mol, ilmalla 29,0 g/mol ja hiilidioksidilla 44,0 g/mol. Jokaisen astian alla oleva palkki näyttää kaasun massan mittakaavassa. Yksi mooli painaa eri kaasuilla eri verran." style="max-width:100%;font-size:24px">
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

Ideaalikaasu on mikromalli. Mallissa hiukkaset ovat pistemäisiä. Ne vaikuttavat toisiinsa ja astian seinämiin vain törmätessään. Siksi mallissa ei tarvitse ottaa huomioon hiukkasten välisten vuorovaikutusten energiaa. Kelvinlämpötila on suoraan verrannollinen hiukkasten keskimääräiseen liike-energiaan. Paine syntyy, kun hiukkaset osuvat seinämiin. Paine kasvaa kolmella tavalla:

- Hiukkasia on enemmän.
- Hiukkaset liikkuvat nopeammin. Silloin lämpötila on korkeampi.
- Tilavuus on pienempi.

Todelliset kaasut noudattavat mallia hyvin tavallisissa oloissa. Malli ei toimi hyvin suurissa paineissa eikä matalissa lämpötiloissa. Silloin hiukkaset ovat lähellä toisiaan. Niiden välinen vetovoima tiivistää kaasun nesteeksi.

## Kaava: Ideaalikaasun tilanyhtälö
Esimerkkipunnituksesta saadaan luku, joka on kaikille kaasuille sama. Se lasketaan näin: paine kerrotaan tilavuudella, ja tulo jaetaan ainemäärällä ja kelvinlämpötilalla. Neljän kaasun keskimääräinen ainemäärä on $0{,}2071\,\text{mol}$. Sillä luku on
```latex
\begin{aligned}
R &= \frac{pV}{nT} \\
&= \frac{101\,000\,\text{Pa} \cdot 0{,}00500\,\text{m}^3}{0{,}2071\,\text{mol} \cdot 293{,}15\,\text{K}} \\
&\approx 8{,}3\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}
\end{aligned}
```
Tarkat mittaukset antavat kaikille kaasuille arvon $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$. Tämä pätee, kun paine ei ole kovin suuri eikä lämpötila kovin matala. Luku on moolinen kaasuvakio. Siitä saadaan ideaalikaasun tilanyhtälö
```kaavat
ideaalikaasun tilanyhtälö :: pV = nRT
```
Tässä $p$ on kaasun absoluuttinen paine, $V$ tilavuus, $n$ ainemäärä, $R$ moolinen kaasuvakio ja $T$ kelvinlämpötila. Kaasun laatu ei näy yhtälössä lainkaan.

```pysahdy
Kaksi samankokoista palloa on samassa paineessa ja lämpötilassa. Toisessa on heliumia ja toisessa ilmaa. Onko niissä yhtä paljon kaasua?
---
On. Kaasun laatu ei näy yhtälössä $pV = nRT$. Sama $p$, $V$ ja $T$ tarkoittavat siis samaa ainemäärää $n$. Massat ovat erilaiset, koska moolimassat ovat erilaiset.
```

Lämpötila $\theta$ voi olla annettu celsiusasteina. Muuta se kelvineiksi lisäämällä lukuarvoon $273{,}15$.

Käytä kaasuvakion arvoa
```latex
R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}
```
Silloin tulon $pV$ yksikön pitää olla joule. Tavallisesti paine muutetaan pascaleiksi ja tilavuus kuutiometreiksi. Silloin
```latex
1\,\text{Pa} \cdot \text{m}^3 = 1\,\tfrac{\text{N}}{\text{m}^2} \cdot \text{m}^3 = 1\,\text{N} \cdot \text{m} = 1\,\text{J}
```
Myös kilopascalit ja litrat sopivat yhdessä, koska
```latex
1\,\text{kPa} \cdot \textsf{l} = 1000\,\text{Pa} \cdot 0{,}001\,\text{m}^3 = 1\,\text{J}
```
Tärkeintä on käyttää yksiköitä samalla tavalla koko laskun ajan.

Ratkaise tilanyhtälö paineen suhteen. Silloin näet, että paine kaksinkertaistuu kolmessa tapauksessa:

- hiukkasten lukumäärä kaksinkertaistuu
- kelvinlämpötila kaksinkertaistuu
- tilavuus puolittuu.

Paine on siis suoraan verrannollinen hiukkasten lukumäärään ja kelvinlämpötilaan. Se on kääntäen verrannollinen tilavuuteen. Tämä kirjoitetaan $p \propto NT/V$.

<svg data-fig="paine-ja-tekijat" viewBox="0 0 600 300" role="img" aria-label="Kaavakuva neljästä männällä suljetusta kaasusylinteristä. Hiukkaset on suurennettu. Vasemmalta oikealle: lähtötilassa hiukkasmäärä on N, lämpötila T ja tilavuus V, ja paine on p. Paine on 2p kolmessa tapauksessa. Ensimmäinen: hiukkasia on kaksi kertaa enemmän (2N). Toinen: kelvinlämpötila on kaksinkertainen (2T), eli hiukkaset liikkuvat nopeammin. Kolmas: mäntä on painettu puoleen tilavuuteen (V/2). Nuolten pituus kuvaa hiukkasten nopeutta." style="max-width:100%;font-size:24px">
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
Kaasun kelvinlämpötila kaksinkertaistuu. Tilavuus kaksinkertaistuu. Hiukkasmäärä pysyy samana. Mitä paineelle tapahtuu?
---
Paine ei muutu. Koska $p \propto NT/V$, kaksi tekijää 2 supistuu pois.
```

Simulaatiossa voit tutkia tätä hiukkasten tasolla. Muuta hiukkasten määrää, lämpötilaa ja tilavuutta. Vertaa seinämistä mitattua painetta tilanyhtälön ennusteeseen. Laske ennuste itse. Hiukkasten keskinäiset törmäykset eivät muuta painetta keskimäärin. Siksi ne on jätetty simulaatiosta pois.

Simulaatiossa paine näytetään suhteessa vertailutilaan ($p/p_\text{ref}$). Sitä ei näytetä pascaleina. Vertailutila on $N = 100$ hiukkasta, $T = 300\,\text{K}$ ja koko tilavuus ($V = 100\,\%$). Siinä $p/p_\text{ref} = 1$. Arvo 2 tarkoittaa kaksinkertaista painetta vertailupaineeseen verrattuna. Hiukkasmäärä $N$ kuvaa kaasun määrää.

<!-- sim -->

<figure class="unit-photo"><img src="pics/fy3/hot-air-balloon-burner.webp" alt="Kirkas liekki nousee kuumailmapallon punaisen kuvun sisään."><figcaption>Poltin lämmittää pallon sisällä olevaa ilmaa. Pallo on alhaalta auki. Siksi sisäilman paine on lähes sama kuin ulkoilman paine.</figcaption></figure>

Joskus kaasun määrä ei muutu. Silloin $nR$ on vakio, ja tilanyhtälöstä seuraa yhdistetty kaasulaki $p_1V_1/T_1 = p_2V_2/T_2$. Alaindeksit 1 ja 2 ovat alku- ja lopputila. Yhdistetystä kaasulaista saat jokaisen luvun *Kaasujen tilanmuutokset ja Boylen laki* kaasulain. Pidä yksi suure vakiona.

## Esimerkki
Juhlapallo täytetään heliumilla, kunnes sen tilavuus on $5{,}0\,\textsf{l}$. Pallossa paine on $101\,\text{kPa}$ ja lämpötila $20\,{}^\circ\text{C}$. Kuinka monta moolia heliumia pallossa on? Mikä on heliumin massa? Heliumin moolimassa on $4{,}0\,\text{g/mol}$.

<!-- vaihe -->

**Tunnetut ja kysytty.** Pallon tilavuus $V = 5{,}0\,\textsf{l}$, paine $p = 101\,\text{kPa}$, lämpötila $\theta = 20\,{}^\circ\text{C}$ ja heliumin moolimassa $M = 4{,}0\,\text{g/mol}$.

Kysytään ainemäärää $n$ ja massaa $m$.

<!-- vaihe -->

**Periaate.** Pallossa on tietty määrä heliumia. Tilavuus, paine ja lämpötila tunnetaan. Helium käyttäytyy tavallisessa paineessa ja huoneenlämmössä ideaalikaasuna. Siksi tilanyhtälö $pV = nRT$ antaa ainemäärän. Moolimassa muuttaa ainemäärän massaksi.

<!-- vaihe -->

**Kaava ratkaistuna.** Ratkaistaan ainemäärä tilanyhtälöstä. Massa ratkaistaan yhtälöstä $n = m/M$:
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
Pallossa on $0{,}21\,\text{mol}$ heliumia, ja sen massa on $0{,}83\,\text{g}$. Tilavuus $5{,}0\,\textsf{l}$ rajoittaa ainemäärää. Massaa rajoittaa myös moolimassa $4{,}0\,\text{g/mol}$. Kummassakin on kaksi numeroa, joten tulokset annetaan kahdella merkitsevällä numerolla. Paine $101\,\text{kPa}$ ja lämpötila $293\,\text{K}$ ovat kolmen numeron arvoja. Ne eivät rajoita tulosta.

<!-- vaihe -->

**Järkevyys.** Yksi mooli kaasua vie huoneenlämmössä ja normaalipaineessa noin $24\,\textsf{l}$. Siksi tilavuudessa $5{,}0\,\textsf{l}$ on noin $5{,}0\,\textsf{l} : 24\,\textsf{l/mol} \approx 0{,}21\,\text{mol}$ kaasua. Samankokoisessa ilmapallossa on yhtä monta moolia ilmaa. Sen massa on noin $0{,}2073\,\text{mol} \cdot 29\,\text{g/mol} \approx 6{,}0\,\text{g}$. Heliumpallo on kevyempi, koska heliumhiukkaset ovat kevyempiä. Syy ei ole se, että kaasua olisi vähemmän.

## Yleinen virhekäsitys
Tilanyhtälön laskuissa toistuu kolme virhettä:

- **Celsiusasteet.** Lämpötila on tilanyhtälössä aina kelvineinä. Esimerkiksi $0\,{}^\circ\text{C}$ antaisi paineeksi nollan. Kaasulla on kuitenkin paine myös jäätymispisteessä.
- **Sekoitetut yksiköt.** Paine voi olla kilopascaleina ja tilavuus kuutiometreinä. Tai paine voi olla pascaleina ja tilavuus litroina. Silloin tulos on tuhatkertaisesti väärä. Varminta on muuttaa kaikki suureet perusyksiköiksi: paine pascaleiksi, tilavuus kuutiometreiksi ja lämpötila kelvineiksi.
- **Raskas kaasu.** Moni ajattelee, että raskasta kaasua mahtuu samaan tilavuuteen vähemmän moolia. Ainemäärä riippuu kuitenkin vain paineesta, tilavuudesta ja lämpötilasta. Se ei riipu kaasun laadusta. Massa sen sijaan riippuu moolimassasta.

## Tiivistelmä
- Ideaalikaasun tilanyhtälö on $pV = nRT$. Tässä $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$ ja $T$ on kelvineinä.
- Ainemäärä $n$ kertoo kaasun määrän mooleina: $n = N/{N_\text{A}} = m/M$.
- Paine on verrannollinen lausekkeeseen $NT/V$. Paine kaksinkertaistuu, kun hiukkasmäärä tai kelvinlämpötila kaksinkertaistuu. Se kaksinkertaistuu myös, kun tilavuus puolittuu.
- Kun kaasun määrä pysyy samana, $p_1V_1/T_1 = p_2V_2/T_2$. Tästä saadaan erilliset kaasulait.
- Samassa paineessa, lämpötilassa ja tilavuudessa on aina yhtä monta moolia kaasua. Kaasun laji ei vaikuta. Punnitus antaa kaikille kaasuille saman $m/M$.
- Ideaalikaasumalli toimii hyvin tavallisissa oloissa. Se ei toimi hyvin suurissa paineissa eikä matalissa lämpötiloissa.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: kuumailmapallo leijuu järven yllä. Korin yläpuolella palava liekki lämmittää pallon sisällä olevaa ilmaa." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-10-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
