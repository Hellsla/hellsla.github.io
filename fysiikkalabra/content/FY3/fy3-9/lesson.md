# Kaasujen tilanmuutokset ja Boylen laki

> **Miksi** suljettu sipsipussi pullistuu lentokoneessa kireäksi, vaikka siihen ei ole lisätty mitään?

## Ydinajatus
Suljetun kaasumäärän tilaa kuvaavat paine p, tilavuus V ja lämpötila T. Kun yksi niistä muuttuu, muuttuu yleensä ainakin yksi muista. Tällaista muutosta sanotaan tilanmuutokseksi. Tilanmuutoksia on helpointa tutkia niin, että yksi suureista pidetään vakiona. Isotermisessä tilanmuutoksessa lämpötila on vakio, isobaarisessa paine ja isokoorisessa tilavuus.

Mikromallin mukaan kaasun paine syntyy hiukkasten törmäyksistä astian seinämiin. Jos kaasu puristetaan puoleen alkuperäisestä tilavuudesta ja lämpötila pysyy samana, hiukkaset liikkuvat yhtä nopeasti kuin ennen, mutta ne osuvat seinämiin kaksi kertaa niin usein. Paine kaksinkertaistuu.

<svg viewBox="0 0 600 300" role="img" aria-label="Mikromalli Boylen laista, kaaviokuva. Vasemmalla sylinterissä on kahdeksan kaasuhiukkasta tilavuudessa V ja paineessa p. Oikealla samat kahdeksan hiukkasta on puristettu mäntää painamalla puoleen tilavuuteen V/2 samassa lämpötilassa. Nopeusnuolet ovat yhtä pitkät, mutta männän ja pohjan osumamerkkejä on kaksi kertaa niin monta, joten paine on 2p. Kaasupatsaiden korkeudet ovat suhteessa 2 : 1." style="max-width:100%;font-family:system-ui,sans-serif;font-size:26px">
  <rect x="40" y="30" width="160" height="220" fill="currentColor" fill-opacity="0.08"/>
  <polyline points="40,14 40,250 200,250 200,14" fill="none" stroke="currentColor" stroke-width="4"/>
  <rect x="43" y="16" width="154" height="14" fill="currentColor" fill-opacity="0.55"/>
  <line x1="120" y1="6" x2="120" y2="16" stroke="currentColor" stroke-width="5"/>
  <line x1="95" y1="6" x2="145" y2="6" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>
  <circle cx="68" cy="86" r="6.5" fill="currentColor"/>
  <line x1="60.5" y1="88.7" x2="53.9" y2="91.1" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="48.3,93.2 52.4,86.9 55.4,95.4" fill="currentColor"/>
  <circle cx="115" cy="74" r="6.5" fill="currentColor"/>
  <line x1="122.5" y1="71.3" x2="129.1" y2="68.9" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="134.7,66.8 130.6,73.1 127.6,64.6" fill="currentColor"/>
  <circle cx="165" cy="90" r="6.5" fill="currentColor"/>
  <line x1="171.9" y1="94" x2="178" y2="97.5" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="183.2,100.5 175.7,101.4 180.2,93.6" fill="currentColor"/>
  <circle cx="92" cy="150" r="6.5" fill="currentColor"/>
  <line x1="90.6" y1="142.1" x2="89.4" y2="135.2" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="88.4,129.3 93.8,134.4 85,136" fill="currentColor"/>
  <circle cx="140" cy="140" r="6.5" fill="currentColor"/>
  <line x1="134.9" y1="146.1" x2="130.4" y2="151.5" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="126.5,156.1 126.9,148.6 133.8,154.4" fill="currentColor"/>
  <circle cx="185" cy="174" r="6.5" fill="currentColor"/>
  <line x1="187.7" y1="166.5" x2="190.1" y2="159.9" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="192.2,154.3 194.4,161.4 185.9,158.4" fill="currentColor"/>
  <circle cx="70" cy="206" r="6.5" fill="currentColor"/>
  <line x1="77.5" y1="208.7" x2="84.1" y2="211.1" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="89.7,213.2 82.6,215.4 85.6,206.9" fill="currentColor"/>
  <circle cx="158" cy="210" r="6.5" fill="currentColor"/>
  <line x1="165.9" y1="208.6" x2="172.8" y2="207.4" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="178.7,206.4 173.6,211.8 172,203" fill="currentColor"/>
  <polygon points="78,37 71.8,38.8 70,45 68.2,38.8 62,37 68.2,35.2 70,29 71.8,35.2" fill="currentColor"/>
  <polygon points="178,37 171.8,38.8 170,45 168.2,38.8 162,37 168.2,35.2 170,29 171.8,35.2" fill="currentColor"/>
  <polygon points="108,243 101.8,244.8 100,251 98.2,244.8 92,243 98.2,241.2 100,235 101.8,241.2" fill="currentColor"/>
  <polygon points="188,243 181.8,244.8 180,251 178.2,244.8 172,243 178.2,241.2 180,235 181.8,241.2" fill="currentColor"/>
  <rect x="330" y="140" width="160" height="110" fill="currentColor" fill-opacity="0.08"/>
  <polyline points="330,14 330,250 490,250 490,14" fill="none" stroke="currentColor" stroke-width="4"/>
  <rect x="333" y="126" width="154" height="14" fill="currentColor" fill-opacity="0.55"/>
  <line x1="410" y1="6" x2="410" y2="126" stroke="currentColor" stroke-width="5"/>
  <line x1="385" y1="6" x2="435" y2="6" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>
  <circle cx="358" cy="168" r="6.5" fill="currentColor"/>
  <line x1="350.5" y1="170.7" x2="343.9" y2="173.1" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="338.3,175.2 342.4,168.9 345.4,177.4" fill="currentColor"/>
  <circle cx="405" cy="162" r="6.5" fill="currentColor"/>
  <line x1="412.5" y1="159.3" x2="419.1" y2="156.9" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="424.7,154.8 420.6,161.1 417.6,152.6" fill="currentColor"/>
  <circle cx="455" cy="170" r="6.5" fill="currentColor"/>
  <line x1="461.9" y1="174" x2="468" y2="177.5" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="473.2,180.5 465.7,181.4 470.2,173.6" fill="currentColor"/>
  <circle cx="382" cy="200" r="6.5" fill="currentColor"/>
  <line x1="380.6" y1="192.1" x2="379.4" y2="185.2" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="378.4,179.3 383.8,184.4 375,186" fill="currentColor"/>
  <circle cx="430" cy="195" r="6.5" fill="currentColor"/>
  <line x1="424.9" y1="201.1" x2="420.4" y2="206.5" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="416.5,211.1 416.9,203.6 423.8,209.4" fill="currentColor"/>
  <circle cx="475" cy="212" r="6.5" fill="currentColor"/>
  <line x1="477.7" y1="204.5" x2="480.1" y2="197.9" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="482.2,192.3 484.4,199.4 475.9,196.4" fill="currentColor"/>
  <circle cx="360" cy="228" r="6.5" fill="currentColor"/>
  <line x1="367.5" y1="230.7" x2="374.1" y2="233.1" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="379.7,235.2 372.6,237.4 375.6,228.9" fill="currentColor"/>
  <circle cx="448" cy="230" r="6.5" fill="currentColor"/>
  <line x1="455.9" y1="228.6" x2="462.8" y2="227.4" stroke="currentColor" stroke-width="2.5"/>
  <polygon points="468.7,226.4 463.6,231.8 462,223" fill="currentColor"/>
  <polygon points="353,147 346.8,148.8 345,155 343.2,148.8 337,147 343.2,145.2 345,139 346.8,145.2" fill="currentColor"/>
  <polygon points="396,147 389.8,148.8 388,155 386.2,148.8 380,147 386.2,145.2 388,139 389.8,145.2" fill="currentColor"/>
  <polygon points="450,147 443.8,148.8 442,155 440.2,148.8 434,147 440.2,145.2 442,139 443.8,145.2" fill="currentColor"/>
  <polygon points="486,147 479.8,148.8 478,155 476.2,148.8 470,147 476.2,145.2 478,139 479.8,145.2" fill="currentColor"/>
  <polygon points="353,243 346.8,244.8 345,251 343.2,244.8 337,243 343.2,241.2 345,235 346.8,241.2" fill="currentColor"/>
  <polygon points="413,243 406.8,244.8 405,251 403.2,244.8 397,243 403.2,241.2 405,235 406.8,241.2" fill="currentColor"/>
  <polygon points="438,243 431.8,244.8 430,251 428.2,244.8 422,243 428.2,241.2 430,235 431.8,241.2" fill="currentColor"/>
  <polygon points="480,243 473.8,244.8 472,251 470.2,244.8 464,243 470.2,241.2 472,235 473.8,241.2" fill="currentColor"/>
  <polygon points="230,52 223.8,53.8 222,60 220.2,53.8 214,52 220.2,50.2 222,44 223.8,50.2" fill="currentColor"/>
  <text x="238" y="61" fill="currentColor" font-size="24">osuma</text>
  <line x1="218" y1="200" x2="300" y2="200" stroke="currentColor" stroke-width="4"/>
  <polygon points="316,200 298,190 298,210" fill="currentColor"/>
  <text x="265" y="176" text-anchor="middle" fill="currentColor" font-size="24">T vakio</text>
  <text x="120" y="288" text-anchor="middle" fill="currentColor">V ja p</text>
  <text x="410" y="288" text-anchor="middle" fill="currentColor">V/2 ja 2p</text>
</svg>

Isotermisessä tilanmuutoksessa paine on siis kääntäen verrannollinen tilavuuteen, ja paineen ja tilavuuden tulo pysyy vakiona. Tätä sanotaan Boylen laiksi. Se pätee hyvin ilmaan ja muihin kaasuihin tavallisissa paineissa ja lämpötiloissa, kunhan kaasun määrä pysyy samana ja paineena käytetään kaasun koko painetta eikä mittarin näyttämää ylipainetta. Tämä vastaa alun kysymykseen: lentokoneen matkustamossa ilmanpaine on noin 78 kPa, joten suljetussa pussissa oleva ilma laajenee, kunnes pussin sisäpuolinen paine on yhtä suuri kuin ulkopuolinen.

Boylen laki voidaan todentaa kokeellisesti. Ruiskuun suljetaan ilmaa, ja ruisku liitetään painemittariin. Mäntää painetaan vaiheittain, ja jokaisella tilavuudella luetaan paine. Mittaus tehdään hitaasti, jotta ilman lämpötila ehtii palata huoneenlämpöön. Kun tulokset piirretään (V, p)-koordinaatistoon, pisteet asettuvat laskevalle kaarelle, josta on vaikea nähdä, onko kyse juuri kääntäen verrannollisuudesta. Siksi taulukkoon lasketaan uusi sarake 1/V ja piirretään p 1/V:n funktiona. Jos laki pätee, pisteet ovat origon kautta kulkevalla suoralla, ja suoran kulmakerroin on vakio pV. Kokeile simulaatiossa: tallenna mittauksia eri tilavuuksilla ja valitse ”Piirrä p 1/V:n funktiona”.

Kun kaasua lämmitetään, sen hiukkaset liikkuvat nopeammin. Jos mäntä pääsee liikkumaan niin, että paine pysyy vakiona (isobaarinen tilanmuutos), kaasu laajenee, ja sen tilavuus on suoraan verrannollinen kelvinlämpötilaan. Jos tilavuus taas pidetään vakiona (isokoorinen tilanmuutos), paine kasvaa, ja se on suoraan verrannollinen kelvinlämpötilaan. Molemmissa laeissa lämpötila on ilmoitettava kelvineinä, koska verrannollisuus alkaa absoluuttisesta nollapisteestä.

## Kaava
Isotermisessä tilanmuutoksessa eli Boylen lain mukaan
```latex
p_1 V_1 = p_2 V_2
```
missä p₁ ja V₁ ovat kaasun paine (Pa) ja tilavuus (m³) alkutilassa ja p₂ ja V₂ lopputilassa. Yhtälö on sama kuin pV = vakio. Kun se jaetaan V:llä, saadaan
```latex
p = \text{vakio} \cdot \frac{1}{V}
```
Paine on siis kääntäen verrannollinen tilavuuteen. Kun merkitään x = 1/V ja y = p, yhtälö on muotoa y = kx kuten FY1:n suoran yhtälö. Siksi (1/V, p)-kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on k = pV. Tulon pV yksikkö on Pa · m³ = N/m² · m³ = N · m = J, ja 1 kPa · 1 l = 1 J. Koska yhtälön p₁V₁ = p₂V₂ molemmilla puolilla on samat yksiköt, paineen ja tilavuuden voi ilmoittaa myös esimerkiksi kilopascaleina ja litroina, kunhan ne ovat samat molemmilla puolilla.

<svg viewBox="0 0 600 300" role="img" aria-label="Kaksi kuvaajaa samoista mittauksista. Vasemmalla paine tilavuuden funktiona on laskeva kaari. Oikealla paine tilavuuden käänteisluvun funktiona on origon kautta kulkeva suora." style="max-width:100%;font-family:system-ui,sans-serif;font-size:26px">
  <line x1="50" y1="250" x2="285" y2="250" stroke="currentColor" stroke-width="3"/>
  <line x1="50" y1="250" x2="50" y2="30" stroke="currentColor" stroke-width="3"/>
  <polyline points="91.8,50 94,60 96.5,70.2 99,79.4 102.3,90.2 106,100.7 109,108.3 112.7,116.7 117,125.2 122,133.9 127,141.4 133.6,150 140,157.1 147,163.8 154.5,170 165,177.3 175.4,183.3 186,188.5 200,194.3 217.2,200 238,205.5 259,210" fill="none" stroke="currentColor" stroke-width="3"/>
  <circle cx="91.8" cy="50" r="5" fill="currentColor"/><circle cx="102.3" cy="90" r="5" fill="currentColor"/><circle cx="112.7" cy="116.7" r="5" fill="currentColor"/><circle cx="133.6" cy="150" r="5" fill="currentColor"/><circle cx="154.5" cy="170" r="5" fill="currentColor"/><circle cx="175.4" cy="183.3" r="5" fill="currentColor"/><circle cx="217.2" cy="200" r="5" fill="currentColor"/><circle cx="259" cy="210" r="5" fill="currentColor"/>
  <text x="60" y="28" fill="currentColor">p</text>
  <text x="285" y="278" text-anchor="end" fill="currentColor">V</text>
  <line x1="330" y1="250" x2="580" y2="250" stroke="currentColor" stroke-width="3"/>
  <line x1="330" y1="250" x2="330" y2="30" stroke="currentColor" stroke-width="3"/>
  <line x1="330" y1="250" x2="560" y2="39" stroke="currentColor" stroke-width="3"/>
  <circle cx="373.6" cy="210" r="5" fill="currentColor"/><circle cx="384.5" cy="200" r="5" fill="currentColor"/><circle cx="402.7" cy="183.3" r="5" fill="currentColor"/><circle cx="417.2" cy="170" r="5" fill="currentColor"/><circle cx="439" cy="150" r="5" fill="currentColor"/><circle cx="475.3" cy="116.7" r="5" fill="currentColor"/><circle cx="504.4" cy="90" r="5" fill="currentColor"/><circle cx="548" cy="50" r="5" fill="currentColor"/>
  <text x="340" y="28" fill="currentColor">p</text>
  <text x="580" y="278" text-anchor="end" fill="currentColor">1/V</text>
</svg>

Isobaarisessa ja isokoorisessa tilanmuutoksessa
```latex
\frac{V_1}{T_1} = \frac{V_2}{T_2} \qquad \text{ja} \qquad \frac{p_1}{T_1} = \frac{p_2}{T_2}
```
missä T₁ ja T₂ ovat kaasun lämpötilat kelvineinä (K) alku- ja lopputilassa. Tilavuus tai paine on siis suoraan verrannollinen kelvinlämpötilaan, ja (T, V)- tai (T, p)-kuvaajan suoran jatke kulkee origon eli absoluuttisen nollapisteen 0 K kautta.

<svg viewBox="0 0 600 300" role="img" aria-label="Kaasun tilavuus vakiopaineessa tai paine vakiotilavuudessa kelvinlämpötilan funktiona, mittakaavassa. Mittauspisteet välillä 253–373 K ovat suoralla. Suoran katkoviivalla piirretty jatke kulkee origon kautta: tilavuus tai paine olisi nolla absoluuttisessa nollapisteessä 0 K eli −273 °C." style="max-width:100%;font-family:system-ui,sans-serif;font-size:26px">
  <line x1="70" y1="250" x2="560" y2="250" stroke="currentColor" stroke-width="3"/>
  <line x1="70" y1="250" x2="70" y2="30" stroke="currentColor" stroke-width="3"/>
  <line x1="397.6" y1="250" x2="397.6" y2="260" stroke="currentColor" stroke-width="3"/>
  <line x1="70" y1="250" x2="373.6" y2="114.3" stroke="currentColor" stroke-width="3" stroke-dasharray="10 8"/>
  <line x1="373.6" y1="114.3" x2="517.6" y2="50" stroke="currentColor" stroke-width="3"/>
  <circle cx="373.6" cy="114.3" r="6" fill="currentColor"/><circle cx="409.6" cy="98.3" r="6" fill="currentColor"/><circle cx="445.6" cy="82.2" r="6" fill="currentColor"/><circle cx="481.6" cy="66.1" r="6" fill="currentColor"/><circle cx="517.6" cy="50" r="6" fill="currentColor"/>
  <text x="70" y="286" text-anchor="middle" fill="currentColor">0</text>
  <text x="397.6" y="286" text-anchor="middle" fill="currentColor">273</text>
  <text x="590" y="286" text-anchor="end" fill="currentColor">T (K)</text>
  <text x="82" y="34" fill="currentColor">V tai p</text>
  <text x="190" y="160" text-anchor="middle" fill="currentColor">jatke</text>
</svg>

## Esimerkki
Sipsipussissa on lentokentällä 0,80 l ilmaa 101 kPa:n paineessa. Lennon aikana matkustamon paine on 78 kPa. Kuinka suuri on pussissa olevan ilman tilavuus lennolla, kun lämpötila pysyy samana ja pussi pääsee laajenemaan vapaasti?

<!-- vaihe -->

**Tunnetut ja kysytty.** Lämpötila on vakio, joten tilanmuutos on isoterminen ja Boylen laki pätee. Tunnetaan $p_1 = 101\,\text{kPa}$, $V_1 = 0{,}80\,\textsf{l}$ ja $p_2 = 78\,\text{kPa}$. Kysytään lopputilavuutta $V_2$.

<!-- vaihe -->

**Kaava ratkaistuna.** Ratkaistaan Boylen laista $V_2$ jakamalla molemmat puolet paineella $p_2$:
```latex
\begin{aligned}
p_1 V_1 &= p_2 V_2 \\
V_2 &= \frac{p_1 V_1}{p_2}
\end{aligned}
```

<!-- vaihe -->

**Sijoitus.** Sijoitetaan arvot yksiköineen. Kilopascalit supistuvat, joten tilavuus tulee litroina eikä yksiköitä tarvitse muuntaa:
```latex
\begin{aligned}
V_2 &= \frac{p_1 V_1}{p_2} \\
&= \frac{101\,\text{kPa} \cdot 0{,}80\,\textsf{l}}{78\,\text{kPa}}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Laskin antaa $V_2 = 1{,}036\ldots\,\textsf{l} \approx 1{,}0\,\textsf{l}$, kahden merkitsevän numeron tarkkuudella kuten lähtötiedot. Ilman tilavuus kasvaa noin 30 %. Jos pussi on valmiiksi lähes täynnä, se pullistuu kireäksi.

<!-- vaihe -->

**Järkevyys.** Paine pienenee, joten tilavuuden täytyy kasvaa. Kasvukerroin on painesuhde 101/78 ≈ 1,3, ja 0,80 l · 1,3 ≈ 1,0 l.

## Yleinen virhekäsitys
Kolme virhettä toistuu usein:

- **Kääntäen verrannollisuus ei ole laskeva suora.** Kun tilavuus kaksinkertaistuu, paine puolittuu, joten (V, p)-kuvaaja on kaari, joka lähestyy akseleita mutta ei koskaan kohtaa niitä. Suora syntyy vasta, kun p piirretään 1/V:n funktiona.
- **Celsiusasteet eivät kelpaa lämpötilojen suhteeseen.** Kun 1,00 l ilmaa lämpenee vakiopaineessa 10 °C:sta 20 °C:seen, sen tilavuus ei kaksinkertaistu. Kelvineinä laskettuna V₂ = V₁T₂/T₁ = 1,00 l · 293 K / 283 K ≈ 1,04 l, joten tilavuus kasvaa vain noin 3,5 %.
- **Suljetun astian kaasun paine ei johdu kaasun painosta.** Pienessä astiassa kaasun paino on mitätön, ja paine syntyy hiukkasten törmäyksistä, joten se on yhtä suuri kaikkialla astiassa.

## Tiivistelmä
- Tilanmuutoksessa kaasun paine, tilavuus ja lämpötila muuttuvat. Isotermisessä muutoksessa T on vakio, isobaarisessa p ja isokoorisessa V.
- Boylen laki: isotermisessä tilanmuutoksessa $p_1 V_1 = p_2 V_2$, joten paine on kääntäen verrannollinen tilavuuteen.
- Kääntäen verrannollisuus todennetaan laskemalla taulukkoon sarake 1/V ja piirtämällä p 1/V:n funktiona: pisteiden pitää olla origon kautta kulkevalla suoralla.
- Vakiopaineessa tilavuus ja vakiotilavuudessa paine ovat suoraan verrannollisia kelvinlämpötilaan. Lämpötilat ilmoitetaan näissä laskuissa aina kelvineinä.
