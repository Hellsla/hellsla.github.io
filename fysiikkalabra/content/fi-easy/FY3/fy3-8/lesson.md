# Lämpölaajeneminen

> **Miksi** pitkän sillan päässä on kampamainen teräsliitos, jonka yli auton renkaat kolahtavat?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: auto ajaa pitkää siltaa pitkin poispäin katsojasta. Etualalla tien poikki kulkee kampamainen teräsliitos. Sen hampaat lomittuvat. Hampaiden väliin jää rako, joka antaa sillan laajeta lämmetessään." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-8-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Lähes kaikki aineet laajenevat lämmetessään ja kutistuvat jäähtyessään. Ilmiötä sanotaan **lämpölaajenemiseksi**.

<figure class="unit-photo"><img src="pics/fy3/bridge-expansion-joint.webp" alt="Sillan kannella on metallinen sauma. Taustalla on sillan kaide."><figcaption>Kruunuvuorensillan liikuntasauma Helsingissä vuonna 2026. Sauma antaa sillalle tilaa liikkua, esimerkiksi kun lämpötila muuttuu.</figcaption></figure>

### Miksi aine laajenee?
Mikromalli (hiukkasmalli) selittää lämpölaajenemisen. Kiinteässä aineessa hiukkaset värähtelevät tasapainoasemiensa ympärillä. Kun lämpötila nousee, värähtely voimistuu.

Hiukkasten on helpompi loitota toisistaan kuin puristua lähemmäs toisiaan. Lähekkäin puristuvat hiukkaset hylkivät toisiaan voimakkaasti. Loittonevien hiukkasten välinen veto taas heikkenee vähitellen. Siksi hiukkanen heilahtaa kauemmas naapuristaan kuin lähemmäs sitä. Voimakkaammin värähtelevien hiukkasten **keskimääräinen etäisyys kasvaa**. Kun kaikki hiukkasvälit kasvavat, koko kappale laajenee.

<svg data-fig="particles" viewBox="0 0 600 316" role="img" aria-label="Sama hiukkasrivi kylmänä ja lämpimänä. Lämpimänä hiukkaset värähtelevät voimakkaammin. Niiden keskimääräinen etäisyys d on suurempi kuin kylmän rivin etäisyys d₀. Hiukkaset ovat silti yhtä suuria. Etäisyyden muutos on piirretty liioiteltuna." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-8-particles.webp" x="3.8" y="1.3" width="606.1" height="330.8" preserveAspectRatio="none"/>
  <foreignObject x="20" y="85.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kylmä}$</div></foreignObject>
  <foreignObject x="198.5" y="33.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$d_0$</div></foreignObject>
  <foreignObject x="20" y="207.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lämmin}$</div></foreignObject>
  <foreignObject x="196" y="155.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$d > d_0$</div></foreignObject>
  <foreignObject x="143" y="281.5" width="445" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{hiukkaset yhtä suuria, välit liioiteltu}$</div></foreignObject>
</svg>

```pysahdy
Hiukkaset eivät kasva, kun kappale lämpenee. Miksi kappale silti laajenee?
---
Lämmetessä hiukkasten värähtely voimistuu. Silloin niiden keskimääräinen etäisyys kasvaa. Kun kaikki hiukkasvälit kasvavat, koko kappale laajenee.
```

### Lämpölaajeneminen arjessa
Muutos on pieni mutta voimakas. Teräksinen sauva pitenee vain noin sadastuhannesosan pituudestaan jokaista kelviniä kohti. Jos sauvan päät on kiinnitetty, laajeneva teräs työntää niitä valtavalla voimalla. Siksi pitkissä rakenteissa on liikuntasaumoja eli rakoja, jotka antavat rakenteen laajeta. Sillan teräskansi on talvipakkasella lyhyempi kuin kesähelteellä. Kampamainen liitos sillan päässä antaa kannen liikkua vapaasti. Samasta syystä sähkölinjat roikkuvat helteellä alempana kuin pakkasella.

Kappale laajenee kaikkiin suuntiin samassa suhteessa kuin valokuvaa suurennettaessa. Myös reikä levyssä suurenee, kun levy lämpenee. Tätä käytetään kutistusliitoksessa. Kuumennettu teräsrengas pujotetaan akselille. Kun se jäähtyy, se puristuu tiukasti kiinni.

```pysahdy
Teräslevyssä on pyöreä reikä. Levy lämpenee. Pieneneekö vai suureneeko reikä?
---
Reikä suurenee. Kappale laajenee kaikkiin suuntiin samassa suhteessa kuin valokuvaa suurennettaessa.
```

### Eri aineiden lämpölaajeneminen
Eri aineet laajenevat eri tavalla. Kaksoismetalliliuska, jossa kaksi eri metallia on liitetty toisiinsa, taipuu lämmetessään, koska toinen metalli pitenee enemmän. Sellainen liuska avaa ja sulkee virtapiirin vanhanmallisissa termostaateissa.

Nesteet laajenevat yleensä selvästi enemmän kuin kiinteät aineet, ja kaasut vielä paljon enemmän. Nesteen hiukkaset eivät pysy paikoillaan. Niiden väliset vuorovaikutukset ovat heikompia kuin kiinteässä aineessa, joten lämpötilan nousu vie niitä kauemmas toisistaan kuin kiinteässä aineessa. Kaasun hiukkaset ovat kaukana toisistaan ja lähes vapaita, joten vakiopaineessa kaasun tilavuus kasvaa paljon enemmän. Kaasun tilavuus riippuu myös paineesta. Siihen palataan luvussa *Kaasujen tilanmuutokset ja Boylen laki*. Nestelämpömittari perustuu nesteen laajenemiseen: kun lämpötila nousee, nestepatsas kohoaa ohuessa putkessa.

Vesi on poikkeus. Lämpötilojen $0\,{}^\circ\text{C}$ ja $4\,{}^\circ\text{C}$ välillä se kutistuu lämmetessään, joten sen tiheys on suurin noin $4\,{}^\circ\text{C}$:ssa. Tihein, 4-asteinen vesi painuu pohjalle. Kylmempi vesi jää pinnalle ja jäätyy. Siksi järvi jäätyy pinnalta alkaen. Pohjalla on talvellakin noin 4-asteista vettä, jossa kalat selviävät.

```pysahdy
Missä lämpötilassa vesi on tiheintä? Minne järvessä tihein vesi siksi painuu?
---
Vesi on tiheintä noin $4\,{}^\circ\text{C}$:ssa. Tihein vesi painuu järven pohjalle.
```

## Kaava: Pituuden ja tilavuuden lämpölaajeneminen
Kun kappaleen lämpötila muuttuu $\Delta T$, sen pituus on
```kaavat
pituuden lämpölaajeneminen :: l = l_0(1 + \alpha \Delta T)
```
missä $l$ on pituus lämpötilan muutoksen jälkeen (m), $l_0$ alkuperäinen pituus (m), $\alpha$ pituuden lämpötilakerroin (1/K) ja $\Delta T$ lämpötilan muutos (K). Pituuden lämpötilakerroin $\alpha$ kertoo, kuinka suuren osan pituudestaan kappale pitenee, kun sen lämpötila nousee $1\,\text{K}$. Taulukon luku 12 tarkoittaa, että $\alpha = 12 \cdot 10^{-6}\,\tfrac{1}{\text{K}}$.

Pituuden muutos saadaan, kun uudesta pituudesta vähennetään alkuperäinen pituus. Tätä muotoa käytämme tämän luvun laskuissa:
```latex
\Delta l = l - l_0 = \alpha l_0 \Delta T
```
Kaavasta näkyy, että muutos on verrannollinen alkuperäiseen pituuteen. Kaksi kertaa pidemmässä sauvassa on kaksi kertaa enemmän hiukkasvälejä, joten se pitenee kaksi kertaa enemmän. Jäähtyessä $\Delta T$ on negatiivinen, joten myös $\Delta l$ on negatiivinen eli kappale lyhenee.

Nesteiden (ja vakiopaineessa kaasujen) tilavuus lasketaan samalla tavalla:
```kaavat
tilavuuden lämpölaajeneminen :: V = V_0(1 + \gamma \Delta T)
```
missä $V$ on tilavuus lämpötilan muutoksen jälkeen (m³), $V_0$ alkuperäinen tilavuus (m³) ja $\gamma$ tilavuuden lämpötilakerroin (1/K). Tilavuuden muutos on samalla tavalla $\Delta V = V - V_0 = \gamma V_0 \Delta T$. Kiinteällä aineella $\gamma \approx 3\alpha$, koska kappale laajenee kaikkiin kolmeen suuntaan. Pituus, leveys ja korkeus kasvavat kukin suhteessa $\alpha \Delta T$. Kun muutokset ovat pieniä, tilavuuden suhteellinen kasvu on lähes näiden summa $3\alpha \Delta T$. Kaavat ovat hyviä malleja, kun lämpötilan muutos on kohtuullinen. Kiinteillä aineilla se tarkoittaa esimerkiksi enintään noin sataa kelviniä. Nesteillä, varsinkin vedellä, kerroin $\gamma$ muuttuu selvästi lämpötilan mukana. Siksi taulukon $20\,{}^\circ\text{C}$:n arvoja käytetään vain lähellä $20\,{}^\circ\text{C}$:ta.

<svg data-fig="volume-expansion" viewBox="0 0 600 350" role="img" aria-label="Nesteen tilavuuden lämpölaajeneminen. Kolvissa on sama määrä nestettä. Kolvin kaulana on ohut putki. Kylmänä nesteen tilavuus on V₀, ja pinta on alempana. Lämpimänä neste on laajentunut, ja pinta nousee ohuessa putkessa. Tilavuuden muutos ΔV on merkitty putkeen. Laajeneminen on piirretty liioiteltuna." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-8-volume-expansion.webp" x="0" y="-1.2" width="600" height="360" preserveAspectRatio="none"/>
  <foreignObject x="96" y="11.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{kylmä, } T_0$</div></foreignObject>
  <foreignObject x="395" y="11.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$T_0 + \Delta T$</div></foreignObject>
  <foreignObject x="39" y="243.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$V_0$</div></foreignObject>
  <foreignObject x="190" y="175.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{pinta}$</div></foreignObject>
  <foreignObject x="319" y="243.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$V_0$</div></foreignObject>
  <foreignObject x="474" y="145.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\Delta V$</div></foreignObject>
</svg>

| Aine | $\alpha$ (10⁻⁶ 1/K) |
| --- | --- |
| teräs | 12 |
| alumiini | 23 |
| kupari | 17 |
| tavallinen lasi | 9 |
| borosilikaattilasi | 3,3 |

| Aine ($20\,{}^\circ\text{C}$) | $\gamma$ (10⁻³ 1/K) |
| --- | --- |
| vesi | 0,21 |
| etanoli | 1,1 |
| bensiini | 0,95 |
| ilma (vakiopaineessa) | 3,4 |

<svg data-fig="rod-expansion" viewBox="0 0 600 300" role="img" aria-label="Sama sauva kylmänä ja lämpimänä. Lämmin sauva on pidempi. Pituuden muutos Δl on merkitty sauvan päähän. Sauva on kiinni seinässä vasemmassa päässä. Laajeneminen on piirretty liioiteltuna." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-8-rod-expansion.webp" x="5" y="5" width="597" height="309.7" preserveAspectRatio="none"/>
  <foreignObject x="66" y="23.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{kylmä, lämpötila } T_0$</div></foreignObject>
  <foreignObject x="233.5" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$l_0$</div></foreignObject>
  <foreignObject x="66" y="111.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{lämmin, lämpötila } T_0 + \Delta T$</div></foreignObject>
  <foreignObject x="250" y="153.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$l_0 + \Delta l$</div></foreignObject>
  <foreignObject x="468.5" y="221.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta l$</div></foreignObject>
  <foreignObject x="305" y="271.5" width="283" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{laajeneminen liioiteltu}$</div></foreignObject>
</svg>

## Esimerkki
Teräksisen sillan kansi on $120\,\text{m}$ pitkä. Paikkakunnalla lämpötila vaihtelee vuoden aikana $-30\,{}^\circ\text{C}$:n pakkasesta $+30\,{}^\circ\text{C}$:n helteeseen, ja teräksen pituuden lämpötilakerroin on $12 \cdot 10^{-6}\,\tfrac{1}{\text{K}}$. Kuinka paljon kannen pituus muuttuu, eli kuinka paljon liikuntasauman on vähintään annettava periksi?

<!-- vaihe -->

**Tunnetut ja kysytty.** Kannen pituus $l_0 = 120\,\text{m}$, teräksen $\alpha = 12 \cdot 10^{-6}\,\tfrac{1}{\text{K}}$ (tehtävässä annettu), pienin lämpötila $-30\,{}^\circ\text{C}$ ja suurin $+30\,{}^\circ\text{C}$.

Kysytään kannen pituuden muutosta $\Delta l$ koko vuoden aikana.

<!-- vaihe -->

**Periaate.** Kiinteän aineen hiukkasten värähtely voimistuu lämmetessä. Silloin niiden keskimääräinen etäisyys kasvaa, ja kansi pitenee. Teräs pysyy kiinteänä koko vuoden. Kansi saa laajentua vapaasti. Siksi pituuden muutos on verrannollinen alkupituuteen ja lämpötilan muutokseen (kun toinen kaksinkertaistuu, muutos kaksinkertaistuu): $\Delta l = \alpha l_0 \Delta T$.

<!-- vaihe -->

**Kaava ratkaistuna.** Kysytty suure on jo yksin kaavan vasemmalla puolella, joten kaavaa ei tarvitse muokata:
```latex
\begin{aligned}
&\Delta l = \alpha l_0 \Delta T \\
&\Delta T = T_\text{max} - T_\text{min}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Lämpötilan muutos on sama celsiusasteina ja kelvineinä. Siksi $$\begin{aligned} &\Delta T \\ &= 30\,{}^\circ\text{C} - (-30\,{}^\circ\text{C}) \\ &= 60\,\text{K} \end{aligned}$$. Pituudet ovat metreinä, joten $\Delta l$ tulee metreinä. Lopuksi muutetaan tulos millimetreiksi: $1\,\text{m} = 1000\,\text{mm}$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan arvot yksiköineen:
```latex
\begin{aligned}
\Delta l &= \alpha l_0 \Delta T \\
&= 12 \cdot 10^{-6}\,\tfrac{1}{\text{K}} \cdot 120\,\text{m} \cdot 60\,\text{K} \\
&= 0{,}0864\,\text{m} \\
&= 86{,}4\,\text{mm}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kannen pituus muuttuu vuoden aikana noin $86\,\text{mm}$. Liikuntasauman on siis annettava periksi vähintään $87\,\text{mm}$. Kun kysytään pienintä riittävää arvoa, luku pyöristetään ylöspäin: $86{,}4\,\text{mm}$ → $87\,\text{mm}$. Silloin sauma riittää varmasti. Tulos ilmoitetaan kahdella merkitsevällä numerolla (merkitsevät numerot kertovat, kuinka tarkka luku on). Tulosta rajoittavat kerroin $12 \cdot 10^{-6}\,\tfrac{1}{\text{K}}$ ja kokonaisasteiden erotus $\Delta T = 60\,\text{K}$. Kummassakin on kaksi numeroa. Pituudessa $120\,\text{m}$ on vähintään kaksi numeroa, joten se ei rajoita tulosta.

<!-- vaihe -->

**Järkevyys.** Karkea arvio: $10^{-5}\,\tfrac{1}{\text{K}} \cdot 100\,\text{m} \cdot 60\,\text{K} = 60\,\text{mm}$, joten tulos on oikeaa suuruusluokkaa. Kansi pitenee kesään mennessä lähes yhdeksän senttimetriä, koska lämpötila nousee. Se on vain $\alpha \Delta T = 0{,}072\,\%$ kannen pituudesta. Ilman liikuntasaumaa laajeneva teräs kuitenkin työntäisi sillan päitä suurella voimalla. Silloin rakenteet vaurioituisivat. Siksi sillan päässä on kampamainen liitos. Sen hampaat liukuvat toistensa lomassa.

## Yleinen virhekäsitys
Moni ajattelee, että lämmetessä hiukkaset itse kasvavat. Mikromallissa hiukkaset pysyvät samankokoisina, ja vain niiden keskimääräiset etäisyydet kasvavat. Toinen virhe on luulla, että levyn reikä pienenee. Silloin ajatellaan, että levy laajenee reunoiltaan reiän puolelle. Näin ei käy. Reikä suurenee samassa suhteessa kuin levy muutenkin. Kolmas virhe on olettaa, että kaikki aineet laajenevat aina lämmetessään. Vesi kutistuu $0\,{}^\circ\text{C}$:n ja $4\,{}^\circ\text{C}$:n välillä, ja jäätyessään se laajenee. Siksi jää kelluu ja järvet jäätyvät pinnalta.

## Tiivistelmä
- Lämmetessä hiukkasten värähtely voimistuu ja niiden keskimääräinen etäisyys kasvaa, joten aine laajenee.
- Lämpötilan muutoksen jälkeen pituus on $l = l_0(1 + \alpha \Delta T)$ ja tilavuus $V = V_0(1 + \gamma \Delta T)$. Pituuden muutos on siis $\Delta l = \alpha l_0 \Delta T$ ja tilavuuden muutos $\Delta V = \gamma V_0 \Delta T$. Kiinteällä aineella $\gamma \approx 3\alpha$.
- Nesteet laajenevat enemmän kuin kiinteät aineet ja kaasut paljon enemmän kuin nesteet.
- Kappale laajenee kaikkiin suuntiin samassa suhteessa, joten myös reiät suurenevat.
- Vesi on poikkeus: sen tiheys on suurin noin $4\,{}^\circ\text{C}$:ssa.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: rautatiekiskot helteellä. Kiskojen yllä väreilee kuumuus. Kahden kiskon jatkoskohdassa on pieni rako, joka antaa kiskojen laajeta lämmetessään." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-8-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
