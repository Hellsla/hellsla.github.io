# Kaasujen tilanmuutokset ja Boylen laki

> **Miksi** suljettu sipsipussi pullistuu lentokoneessa kireäksi, vaikka siihen ei ole lisätty mitään?

## Ydinajatus
Suljetun kaasumäärän tilaa kuvaavat paine p, tilavuus V ja lämpötila T. Kun yksi niistä muuttuu, muuttuu yleensä ainakin yksi muista. Tällaista muutosta sanotaan tilanmuutokseksi. Tilanmuutoksia on helpointa tutkia niin, että yksi suureista pidetään vakiona. Isotermisessä tilanmuutoksessa lämpötila on vakio, isobaarisessa paine ja isokoorisessa tilavuus.

Mikromallin mukaan kaasun paine syntyy hiukkasten törmäyksistä astian seinämiin. Jos kaasu puristetaan puoleen alkuperäisestä tilavuudesta ja lämpötila pysyy samana, hiukkaset liikkuvat yhtä nopeasti kuin ennen, mutta ne osuvat seinämiin kaksi kertaa niin usein. Paine kaksinkertaistuu. Isotermisessä tilanmuutoksessa paine on siis kääntäen verrannollinen tilavuuteen, ja paineen ja tilavuuden tulo pysyy vakiona. Tätä sanotaan Boylen laiksi. Se pätee hyvin ilmaan ja muihin kaasuihin tavallisissa paineissa ja lämpötiloissa.

Boylen laki voidaan todentaa kokeellisesti. Ruiskuun suljetaan ilmaa, ja ruisku liitetään painemittariin. Mäntää painetaan vaiheittain, ja jokaisella tilavuudella luetaan paine. Mittaus tehdään hitaasti, jotta ilman lämpötila ehtii palata huoneenlämpöön. Kun tulokset piirretään (V, p)-koordinaatistoon, pisteet asettuvat laskevalle kaarelle, josta on vaikea nähdä, onko kyse juuri kääntäen verrannollisuudesta. Siksi taulukkoon lasketaan uusi sarake 1/V ja piirretään p 1/V:n funktiona. Jos laki pätee, pisteet ovat origon kautta kulkevalla suoralla, ja suoran kulmakerroin on vakio pV.

Kun kaasua lämmitetään, sen hiukkaset liikkuvat nopeammin. Jos mäntä pääsee liikkumaan niin, että paine pysyy vakiona, kaasu laajenee, ja sen tilavuus on suoraan verrannollinen kelvinlämpötilaan. Jos tilavuus taas pidetään vakiona, paine kasvaa, ja se on suoraan verrannollinen kelvinlämpötilaan. Molemmissa laeissa lämpötila on ilmoitettava kelvineinä, koska verrannollisuus alkaa absoluuttisesta nollapisteestä. Tämä vastaa myös alun kysymykseen: lentokoneen matkustamossa ilmanpaine on noin 78 kPa, joten pussin sisällä oleva ilma laajenee, kunnes pussin sisäpuolinen paine on yhtä suuri kuin ulkopuolinen.

## Kaava
Isotermisessä tilanmuutoksessa eli Boylen lain mukaan
```latex
p_1 V_1 = p_2 V_2
```
missä p₁ ja V₁ ovat kaasun paine (Pa) ja tilavuus (m³) alkutilassa ja p₂ ja V₂ lopputilassa. Yhtälö on sama kuin pV = vakio, joten p on kääntäen verrannollinen V:hen. Koska yhtälön molemmilla puolilla on samat yksiköt, paineen ja tilavuuden voi ilmoittaa myös esimerkiksi kilopascaleina ja litroina, kunhan ne ovat samat molemmilla puolilla.

Isobaarisessa ja isokoorisessa tilanmuutoksessa
```latex
\frac{V_1}{T_1} = \frac{V_2}{T_2} \qquad \text{ja} \qquad \frac{p_1}{T_1} = \frac{p_2}{T_2}
```
missä T₁ ja T₂ ovat kaasun lämpötilat kelvineinä (K) alku- ja lopputilassa.

<svg viewBox="0 0 600 300" role="img" aria-label="Kaksi kuvaajaa samoista mittauksista. Vasemmalla paine tilavuuden funktiona on laskeva kaari. Oikealla paine tilavuuden käänteisluvun funktiona on origon kautta kulkeva suora." style="max-width:100%;font-family:system-ui,sans-serif;font-size:20px">
  <line x1="50" y1="250" x2="285" y2="250" stroke="currentColor" stroke-width="3"/>
  <line x1="50" y1="250" x2="50" y2="30" stroke="currentColor" stroke-width="3"/>
  <path d="M 91.8 50 Q 105 120 133.6 150 T 259 210" fill="none" stroke="currentColor" stroke-width="3"/>
  <circle cx="91.8" cy="50" r="5" fill="currentColor"/><circle cx="102.3" cy="90" r="5" fill="currentColor"/><circle cx="112.7" cy="116.7" r="5" fill="currentColor"/><circle cx="133.6" cy="150" r="5" fill="currentColor"/><circle cx="154.5" cy="170" r="5" fill="currentColor"/><circle cx="175.4" cy="183.3" r="5" fill="currentColor"/><circle cx="217.2" cy="200" r="5" fill="currentColor"/><circle cx="259" cy="210" r="5" fill="currentColor"/>
  <text x="60" y="28" fill="currentColor">p</text>
  <text x="285" y="278" text-anchor="end" fill="currentColor">V</text>
  <line x1="330" y1="250" x2="580" y2="250" stroke="currentColor" stroke-width="3"/>
  <line x1="330" y1="250" x2="330" y2="30" stroke="currentColor" stroke-width="3"/>
  <line x1="330" y1="250" x2="560" y2="39" stroke="currentColor" stroke-width="3"/>
  <circle cx="373.6" cy="210" r="5" fill="currentColor"/><circle cx="384.5" cy="200" r="5" fill="currentColor"/><circle cx="402.7" cy="183.3" r="5" fill="currentColor"/><circle cx="439" cy="150" r="5" fill="currentColor"/><circle cx="475.3" cy="116.7" r="5" fill="currentColor"/><circle cx="548" cy="50" r="5" fill="currentColor"/>
  <text x="340" y="28" fill="currentColor">p</text>
  <text x="580" y="278" text-anchor="end" fill="currentColor">1/V</text>
</svg>

## Esimerkki
Sipsipussissa on lentokentällä 0,80 l ilmaa 101 kPa:n paineessa. Lennon aikana matkustamon paine on 78 kPa. Kuinka suuri on pussissa olevan ilman tilavuus lennolla, kun lämpötila pysyy samana ja pussi pääsee laajenemaan vapaasti?

Lämpötila on vakio, joten tilanmuutos on isoterminen ja Boylen laki pätee. Ratkaistaan lopputilavuus:
```latex
\begin{aligned}
V_2 &= \frac{p_1 V_1}{p_2} = \frac{101\,\text{kPa} \cdot 0{,}80\,\text{l}}{78\,\text{kPa}} \\
&\approx 1{,}0\,\text{l}
\end{aligned}
```
Ilman tilavuus kasvaa noin kolmanneksella (tarkemmin 1,04 l). Jos pussi on valmiiksi lähes täynnä, se pullistuu kireäksi. Tulos on järkevä: paine pienenee, joten tilavuuden täytyy kasvaa, ja kasvukerroin on painesuhde 101/78 ≈ 1,3.

## Yleinen virhekäsitys
Moni ajattelee, että kääntäen verrannollisuus tarkoittaa laskevaa suoraa. Kun tilavuus kaksinkertaistuu, paine puolittuu, joten (V, p)-kuvaaja on kaari, joka lähestyy akseleita mutta ei koskaan kohtaa niitä. Suora syntyy vasta, kun p piirretään 1/V:n funktiona. Toinen virhe on käyttää celsiusasteita kaavoissa, joissa on lämpötilojen suhde. Kun ilma lämpenee 10 °C:sta 20 °C:seen, sen tilavuus ei kaksinkertaistu, vaan kasvaa kertoimella 293 K / 283 K eli vain noin 3,5 %. Kolmas virhe on ajatella, että kaasun paine johtuu kaasun painosta. Suljetussa astiassa paine syntyy hiukkasten törmäyksistä, ja se on yhtä suuri kaikkialla astiassa.

## Tiivistelmä
- Tilanmuutoksessa kaasun paine, tilavuus ja lämpötila muuttuvat. Isotermisessä muutoksessa T on vakio, isobaarisessa p ja isokoorisessa V.
- Boylen laki: isotermisessä tilanmuutoksessa $p_1 V_1 = p_2 V_2$, joten paine on kääntäen verrannollinen tilavuuteen.
- Kääntäen verrannollisuus todennetaan laskemalla taulukkoon sarake 1/V ja piirtämällä p 1/V:n funktiona: pisteiden pitää olla origon kautta kulkevalla suoralla.
- Vakiopaineessa tilavuus ja vakiotilavuudessa paine ovat suoraan verrannollisia kelvinlämpötilaan. Lämpötilat ilmoitetaan näissä laskuissa aina kelvineinä.
