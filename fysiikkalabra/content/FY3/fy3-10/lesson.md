# Ideaalikaasun tilanyhtälö pV = nRT

> **Miksi** heliumpallo on paljon kevyempi kuin samankokoinen ilmapallo? Onko siinä vähemmän kaasua?

## Ydinajatus
Kaasujen tilanmuutoksia tutkittiin edellisellä oppitunnilla yksi kerrallaan: vakiolämpötilassa pV on vakio, vakiopaineessa V/T on vakio ja vakiotilavuudessa p/T on vakio. Nämä kolme kaasulakia voidaan yhdistää. Kun suljetun kaasumäärän paine, tilavuus ja lämpötila muuttuvat samanaikaisesti, suure pV/T pysyy vakiona. Tätä sanotaan yhdistetyksi kaasulaiksi.

Vakion arvo riippuu siitä, kuinka paljon kaasua on. Jos samaan paineeseen ja lämpötilaan otetaan kaksi kertaa enemmän kaasua, se vie kaksinkertaisen tilavuuden. Kaasun määrää mitataan ainemääränä n, jonka yksikkö on mooli (mol). Hiukkasia on pienessäkin kaasumäärässä valtavasti, joten ne lasketaan mooleina, kuten kemiasta voi olla tuttua. Yksi mooli on 6,022 · 10²³ hiukkasta. Avogadron vakio N_A = 6,022 · 10²³ 1/mol kertoo, kuinka monta hiukkasta on yhdessä moolissa.

Aineen moolimassa M kertoo yhden moolin massan. Heliumin moolimassa on 4,0 g/mol, ilman keskimäärin 29 g/mol ja hiilidioksidin 44 g/mol.

Mittauksissa havaitaan, että pV/(nT) on kaikille kaasuille sama luku, kun paine ei ole kovin suuri eikä lämpötila kovin matala. Se on moolinen kaasuvakio R = 8,31 J/(mol·K). Siitä saadaan ideaalikaasun tilanyhtälö pV = nRT, joka sitoo yhteen kaasun neljä tilaa kuvaavaa suuretta. Kaasun laatu ei näy yhtälössä lainkaan. Samassa paineessa ja lämpötilassa yhtä suuressa tilavuudessa on siis aina yhtä monta moolia kaasua, olipa kaasu heliumia tai ilmaa. Tämä vastaa alun kysymykseen: pallot sisältävät yhtä monta hiukkasta, mutta heliumhiukkaset ovat paljon kevyempiä.

<svg viewBox="0 0 600 300" role="img" aria-label="Kaavakuva: kaksi yhtä suurta palloa samassa paineessa ja lämpötilassa. Kummassakin on yhtä monta hiukkasta ja 0,21 mol kaasua. Heliumpallon kaasun massa on 0,83 g ja ilmapallon 6,0 g, koska ilman hiukkaset ovat raskaampia." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <ellipse cx="150" cy="110" rx="100" ry="98" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="3"/>
  <polygon points="141,218 159,218 150,206" fill="currentColor"/>
  <line x1="150" y1="218" x2="150" y2="232" stroke="currentColor" stroke-width="2"/>
  <circle cx="100" cy="55" r="5" fill="currentColor" fill-opacity="0.55"/>
  <circle cx="155" cy="40" r="5" fill="currentColor" fill-opacity="0.55"/>
  <circle cx="200" cy="65" r="5" fill="currentColor" fill-opacity="0.55"/>
  <circle cx="85" cy="105" r="5" fill="currentColor" fill-opacity="0.55"/>
  <circle cx="135" cy="90" r="5" fill="currentColor" fill-opacity="0.55"/>
  <circle cx="185" cy="110" r="5" fill="currentColor" fill-opacity="0.55"/>
  <circle cx="220" cy="125" r="5" fill="currentColor" fill-opacity="0.55"/>
  <circle cx="110" cy="145" r="5" fill="currentColor" fill-opacity="0.55"/>
  <circle cx="160" cy="140" r="5" fill="currentColor" fill-opacity="0.55"/>
  <circle cx="200" cy="165" r="5" fill="currentColor" fill-opacity="0.55"/>
  <circle cx="135" cy="180" r="5" fill="currentColor" fill-opacity="0.55"/>
  <circle cx="90" cy="170" r="5" fill="currentColor" fill-opacity="0.55"/>
  <text x="150" y="260" text-anchor="middle" fill="currentColor" font-weight="bold">helium</text>
  <text x="150" y="291" text-anchor="middle" fill="currentColor">0,21 mol · 0,83 g</text>
  <ellipse cx="450" cy="110" rx="100" ry="98" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="3"/>
  <polygon points="441,218 459,218 450,206" fill="currentColor"/>
  <line x1="450" y1="218" x2="450" y2="232" stroke="currentColor" stroke-width="2"/>
  <circle cx="400" cy="55" r="9" fill="currentColor" fill-opacity="0.9"/>
  <circle cx="455" cy="40" r="9" fill="currentColor" fill-opacity="0.9"/>
  <circle cx="500" cy="65" r="9" fill="currentColor" fill-opacity="0.9"/>
  <circle cx="385" cy="105" r="9" fill="currentColor" fill-opacity="0.9"/>
  <circle cx="435" cy="90" r="9" fill="currentColor" fill-opacity="0.9"/>
  <circle cx="485" cy="110" r="9" fill="currentColor" fill-opacity="0.9"/>
  <circle cx="520" cy="125" r="9" fill="currentColor" fill-opacity="0.9"/>
  <circle cx="410" cy="145" r="9" fill="currentColor" fill-opacity="0.9"/>
  <circle cx="460" cy="140" r="9" fill="currentColor" fill-opacity="0.9"/>
  <circle cx="500" cy="165" r="9" fill="currentColor" fill-opacity="0.9"/>
  <circle cx="435" cy="180" r="9" fill="currentColor" fill-opacity="0.9"/>
  <circle cx="390" cy="170" r="9" fill="currentColor" fill-opacity="0.9"/>
  <text x="450" y="260" text-anchor="middle" fill="currentColor" font-weight="bold">ilma</text>
  <text x="450" y="291" text-anchor="middle" fill="currentColor">0,21 mol · 6,0 g</text>
</svg>

Ideaalikaasu on mikromalli. Siinä hiukkaset ajatellaan pistemäisiksi, ja ne vaikuttavat toisiinsa ja astian seinämiin vain törmätessään. Paine syntyy seinämiin osuvista törmäyksistä, ja se kasvaa, kun hiukkasia on enemmän, kun ne liikkuvat nopeammin eli lämpötila on korkeampi tai kun tilavuus on pienempi. Todelliset kaasut noudattavat mallia hyvin tavallisissa oloissa. Malli alkaa pettää suurissa paineissa ja matalissa lämpötiloissa, kun hiukkaset ovat lähellä toisiaan ja niiden välinen vetovoima tiivistää kaasun nesteeksi.

## Kaava
Ideaalikaasun tilanyhtälö on
```latex
pV = nRT
```
missä p on paine (Pa), V tilavuus (m³), n ainemäärä (mol), R = 8,31 J/(mol·K) moolinen kaasuvakio ja T lämpötila kelvineinä (K). Celsiusasteina annettu lämpötila θ muutetaan kelvineiksi lisäämällä lukuarvoon 273,15. Tilanyhtälössä paine on aina kokonaispaine pascaleina ja tilavuus kuutiometreinä, koska R:n yksikössä on joule: 1 Pa · m³ = 1 N/m² · m³ = 1 N · m = 1 J.

Ainemäärä saadaan massasta ja moolimassasta:
```latex
n = \frac{m}{M}
```
missä m on massa (kg tai g) ja M moolimassa (kg/mol tai g/mol). Hiukkasten lukumäärä saadaan ainemäärästä Avogadron vakion avulla:
```latex
N = n N_\text{A}
```
missä N on hiukkasten lukumäärä ja $N_\text{A} = 6{,}022 \cdot 10^{23}\,\text{1/mol}$ Avogadron vakio.

Kun tilanyhtälö ratkaistaan paineen suhteen, nähdään, että paine kaksinkertaistuu, kun hiukkasten lukumäärä tai kelvinlämpötila kaksinkertaistuu tai kun tilavuus puolittuu. Paine on siis suoraan verrannollinen hiukkasten lukumäärään ja kelvinlämpötilaan ja kääntäen verrannollinen tilavuuteen, eli $p \propto NT/V$.

<svg viewBox="0 0 600 300" role="img" aria-label="Kaavakuva neljästä kaasuastiasta. Vasemmalta: lähtötila, jossa paine on p. Kun hiukkasia on kaksi kertaa enemmän, kun kelvinlämpötila on kaksinkertainen eli hiukkaset liikkuvat nopeammin tai kun tilavuus on puolet, paine on 2p." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <rect x="15" y="20" width="120" height="155" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="3"/>
  <line x1="40" y1="50" x2="53" y2="56" stroke="currentColor" stroke-width="2"/>
  <circle cx="40" cy="50" r="6" fill="currentColor"/>
  <line x1="97" y1="60" x2="84" y2="65" stroke="currentColor" stroke-width="2"/>
  <circle cx="97" cy="60" r="6" fill="currentColor"/>
  <line x1="63" y1="100" x2="68" y2="87" stroke="currentColor" stroke-width="2"/>
  <circle cx="63" cy="100" r="6" fill="currentColor"/>
  <line x1="110" y1="120" x2="102" y2="109" stroke="currentColor" stroke-width="2"/>
  <circle cx="110" cy="120" r="6" fill="currentColor"/>
  <line x1="43" y1="142" x2="56" y2="136" stroke="currentColor" stroke-width="2"/>
  <circle cx="43" cy="142" r="6" fill="currentColor"/>
  <line x1="87" y1="148" x2="83" y2="135" stroke="currentColor" stroke-width="2"/>
  <circle cx="87" cy="148" r="6" fill="currentColor"/>
  <text x="75" y="215" text-anchor="middle" fill="currentColor">alku</text>
  <text x="75" y="262" text-anchor="middle" fill="currentColor" font-weight="bold">p</text>
  <rect x="165" y="20" width="120" height="155" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="3"/>
  <line x1="190" y1="50" x2="203" y2="56" stroke="currentColor" stroke-width="2"/>
  <circle cx="190" cy="50" r="6" fill="currentColor"/>
  <line x1="247" y1="60" x2="234" y2="65" stroke="currentColor" stroke-width="2"/>
  <circle cx="247" cy="60" r="6" fill="currentColor"/>
  <line x1="213" y1="100" x2="218" y2="87" stroke="currentColor" stroke-width="2"/>
  <circle cx="213" cy="100" r="6" fill="currentColor"/>
  <line x1="260" y1="120" x2="252" y2="109" stroke="currentColor" stroke-width="2"/>
  <circle cx="260" cy="120" r="6" fill="currentColor"/>
  <line x1="193" y1="142" x2="206" y2="136" stroke="currentColor" stroke-width="2"/>
  <circle cx="193" cy="142" r="6" fill="currentColor"/>
  <line x1="237" y1="148" x2="233" y2="135" stroke="currentColor" stroke-width="2"/>
  <circle cx="237" cy="148" r="6" fill="currentColor"/>
  <line x1="225" y1="38" x2="236" y2="46" stroke="currentColor" stroke-width="2"/>
  <circle cx="225" cy="38" r="6" fill="currentColor"/>
  <line x1="265" y1="82" x2="259" y2="95" stroke="currentColor" stroke-width="2"/>
  <circle cx="265" cy="82" r="6" fill="currentColor"/>
  <line x1="183" y1="90" x2="196" y2="86" stroke="currentColor" stroke-width="2"/>
  <circle cx="183" cy="90" r="6" fill="currentColor"/>
  <line x1="227" y1="128" x2="241" y2="131" stroke="currentColor" stroke-width="2"/>
  <circle cx="227" cy="128" r="6" fill="currentColor"/>
  <line x1="265" y1="158" x2="252" y2="153" stroke="currentColor" stroke-width="2"/>
  <circle cx="265" cy="158" r="6" fill="currentColor"/>
  <line x1="205" y1="165" x2="213" y2="153" stroke="currentColor" stroke-width="2"/>
  <circle cx="205" cy="165" r="6" fill="currentColor"/>
  <text x="225" y="215" text-anchor="middle" fill="currentColor">2N</text>
  <text x="225" y="262" text-anchor="middle" fill="currentColor" font-weight="bold">2p</text>
  <rect x="315" y="20" width="120" height="155" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="3"/>
  <line x1="340" y1="50" x2="358" y2="59" stroke="currentColor" stroke-width="2"/>
  <circle cx="340" cy="50" r="6" fill="currentColor"/>
  <line x1="397" y1="60" x2="378" y2="67" stroke="currentColor" stroke-width="2"/>
  <circle cx="397" cy="60" r="6" fill="currentColor"/>
  <line x1="363" y1="100" x2="370" y2="81" stroke="currentColor" stroke-width="2"/>
  <circle cx="363" cy="100" r="6" fill="currentColor"/>
  <line x1="410" y1="120" x2="398" y2="104" stroke="currentColor" stroke-width="2"/>
  <circle cx="410" cy="120" r="6" fill="currentColor"/>
  <line x1="343" y1="142" x2="361" y2="134" stroke="currentColor" stroke-width="2"/>
  <circle cx="343" cy="142" r="6" fill="currentColor"/>
  <line x1="387" y1="148" x2="381" y2="129" stroke="currentColor" stroke-width="2"/>
  <circle cx="387" cy="148" r="6" fill="currentColor"/>
  <text x="375" y="215" text-anchor="middle" fill="currentColor">2T</text>
  <text x="375" y="262" text-anchor="middle" fill="currentColor" font-weight="bold">2p</text>
  <rect x="465" y="20" width="120" height="155" fill="none" stroke="currentColor" stroke-opacity="0.4" stroke-dasharray="6 5"/>
  <rect x="465" y="97" width="120" height="78" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="3"/>
  <line x1="490" y1="112" x2="499" y2="117" stroke="currentColor" stroke-width="2"/>
  <circle cx="490" cy="112" r="6" fill="currentColor"/>
  <line x1="547" y1="117" x2="538" y2="121" stroke="currentColor" stroke-width="2"/>
  <circle cx="547" cy="117" r="6" fill="currentColor"/>
  <line x1="513" y1="137" x2="517" y2="128" stroke="currentColor" stroke-width="2"/>
  <circle cx="513" cy="137" r="6" fill="currentColor"/>
  <line x1="560" y1="147" x2="554" y2="139" stroke="currentColor" stroke-width="2"/>
  <circle cx="560" cy="147" r="6" fill="currentColor"/>
  <line x1="493" y1="158" x2="502" y2="154" stroke="currentColor" stroke-width="2"/>
  <circle cx="493" cy="158" r="6" fill="currentColor"/>
  <line x1="537" y1="161" x2="534" y2="152" stroke="currentColor" stroke-width="2"/>
  <circle cx="537" cy="161" r="6" fill="currentColor"/>
  <text x="525" y="215" text-anchor="middle" fill="currentColor">V/2</text>
  <text x="525" y="262" text-anchor="middle" fill="currentColor" font-weight="bold">2p</text>
</svg>

Simulaatiossa voit tutkia tätä hiukkasten tasolla: muuta hiukkasten määrää, lämpötilaa ja tilavuutta ja vertaa seinämistä mitattua painetta ennusteeseen. Hiukkasten keskinäiset törmäykset eivät muuta painetta, joten ne on jätetty simulaatiosta pois.

Kun kaasun määrä ei muutu, tilanyhtälöstä seuraa yhdistetty kaasulaki
```latex
\frac{p_1 V_1}{T_1} = \frac{p_2 V_2}{T_2}
```
missä alaindeksit 1 ja 2 tarkoittavat alku- ja lopputilaa. Siitä saadaan jokainen edellisen oppitunnin kaasulaki, kun yksi suure pidetään vakiona.

## Esimerkki
Juhlapallo täytetään heliumilla, kunnes sen tilavuus on 5,0 l. Pallossa paine on 101 kPa ja lämpötila 20 °C. Kuinka monta moolia heliumia pallossa on, ja mikä on heliumin massa? Heliumin moolimassa on 4,0 g/mol.

<!-- vaihe -->
**Tunnetut ja kysytty.** Muutetaan yksiköt perusyksiköiksi:

- tilavuus $V = 5{,}0\,\textsf{l} = 0{,}0050\,\text{m}^3$
- paine $p = 101\,\text{kPa}$, eli $p = 101\,000\,\text{Pa}$
- lämpötila $T = (20 + 273{,}15)\,\text{K}$, eli $T = 293{,}15\,\text{K}$
- moolimassa $M = 4{,}0\,\text{g/mol}$

Kysytään ainemäärää n ja massaa m.

<!-- vaihe -->
**Kaava ratkaistuna.** Ratkaistaan tilanyhtälöstä ainemäärä ja yhtälöstä $n = m/M$ massa:
```latex
\begin{aligned}
n &= \frac{pV}{RT} \\
m &= nM
\end{aligned}
```

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
Pallossa on 0,21 mol heliumia, ja sen massa on 0,83 g.

<!-- vaihe -->
**Järkevyys.** Kemiasta tuttu moolitilavuus on huoneenlämmössä noin 24 l/mol, joten 5,0 litrassa on noin 5,0/24 ≈ 0,21 mol kaasua. Samankokoisessa ilmapallossa on yhtä monta moolia ilmaa, mutta sen massa on noin 0,2073 mol · 29 g/mol ≈ 6,0 g. Heliumpallo on kevyempi, koska heliumhiukkaset ovat kevyempiä, ei siksi, että kaasua olisi vähemmän.

## Yleinen virhekäsitys
Tilanyhtälön laskuissa toistuu kolme virhettä:

- **Celsiusasteet.** Lämpötila on tilanyhtälössä aina kelvineinä. Esimerkiksi 0 °C antaisi paineeksi nollan, mutta kaasulla on paine myös jäätymispisteessä.
- **Sekoitetut yksiköt.** Jos paine on kilopascaleina mutta tilavuus kuutiometreinä tai paine pascaleina mutta tilavuus litroina, tulos on tuhatkertaisesti väärä. Varminta on muuttaa kaikki suureet perusyksiköiksi: paine pascaleiksi, tilavuus kuutiometreiksi ja lämpötila kelvineiksi.
- **Raskas kaasu.** Moni ajattelee, että raskaampaa kaasua mahtuu samaan tilavuuteen vähemmän moolia. Ainemäärä riippuu kuitenkin vain paineesta, tilavuudesta ja lämpötilasta, ei kaasun laadusta. Massa sen sijaan riippuu moolimassasta.

## Tiivistelmä
- Ideaalikaasun tilanyhtälö on $pV = nRT$, missä $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$ ja T on kelvineinä.
- Ainemäärä n kertoo kaasun määrän mooleina, ja $n = m/M$. Hiukkasten lukumäärä on $N = nN_\text{A}$.
- Paine on verrannollinen lausekkeeseen NT/V: kaksinkertainen hiukkasmäärä tai kelvinlämpötila tai puolet pienempi tilavuus kaksinkertaistaa paineen.
- Kun kaasun määrä pysyy samana, $p_1V_1/T_1 = p_2V_2/T_2$, ja siitä saadaan erilliset kaasulait.
- Samassa paineessa, lämpötilassa ja tilavuudessa on aina yhtä monta moolia kaasua, kaasun laadusta riippumatta.
- Ideaalikaasumalli toimii hyvin tavallisissa oloissa ja pettää suurissa paineissa ja matalissa lämpötiloissa.
