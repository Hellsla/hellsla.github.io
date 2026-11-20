# Kaasujen tilanmuutokset ja Boylen laki

> **Miksi** suljettu sipsipussi pullistuu lentokoneessa kireäksi, vaikka siihen ei ole lisätty mitään?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: lentokoneen istuimen tarjottimella on pullistunut, kireä sipsipussi ja vesimuki. Ikkunasta näkyvät pilvet kaukana alapuolella." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-9-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Suljetun kaasumäärän tilaa kuvaavat paine $p$, tilavuus $V$ ja lämpötila $T$. Kun yksi niistä muuttuu, yleensä muuttuu myös ainakin yksi muista. Tätä muutosta sanotaan tilanmuutokseksi. Tilanmuutoksia on helpointa tutkia, kun yksi suure pidetään vakiona. Isotermisessä tilanmuutoksessa lämpötila on vakio. Isobaarisessa tilanmuutoksessa paine on vakio. Isokoorisessa tilanmuutoksessa tilavuus on vakio.

Mikromalli selittää kaasun paineen. Paine syntyy, kun hiukkaset törmäävät astian seinämiin. Oletetaan, että kaasu puristetaan puoleen alkuperäisestä tilavuudesta ja lämpötila pysyy samana. Silloin hiukkaset liikkuvat yhtä nopeasti kuin ennen. Ne osuvat seinämiin kaksi kertaa niin usein. Paine kaksinkertaistuu.

<svg data-fig="micro-boyle" viewBox="0 0 600 332" role="img" aria-label="Mikromalli Boylen laista, kaaviokuva. Vasemmalla sylinterissä on kahdeksan kaasuhiukkasta. Niiden tilavuus on V ja paine p. Oikealla samat kahdeksan hiukkasta on puristettu mäntää painamalla puoleen tilavuuteen V/2. Lämpötila on sama. Nopeusnuolet ovat yhtä pitkät. Männän ja pohjan osumamerkkejä on kuitenkin kaksi kertaa niin monta. Siksi paine on 2p. Kaasutilojen korkeudet ovat suhteessa 2 : 1." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-9-micro-boyle.webp" x="0" y="0" width="600" height="340" preserveAspectRatio="none"/>
  <foreignObject x="238" y="51.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{osuma}$</div></foreignObject>
  <foreignObject x="223.5" y="171.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T\ \text{vakio}$</div></foreignObject>
  <foreignObject x="87.5" y="289.5" width="65" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V\ \text{ja}\ p$</div></foreignObject>
  <foreignObject x="358.5" y="289.5" width="103" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V/2\ \text{ja}\ 2p$</div></foreignObject>
</svg>

Isotermisessä tilanmuutoksessa paine on siis kääntäen verrannollinen tilavuuteen. Se tarkoittaa, että kun tilavuus kaksinkertaistuu, paine puolittuu. Paineen ja tilavuuden tulo pysyy vakiona. Tätä sanotaan Boylen laiksi. Laki vastaa alun kysymykseen. Lentokoneen matkustamossa ilmanpaine laskee noin $78\,\text{kPa}$:iin. Pussin ilma laajenee, kunnes pussi on kireä. Kireässä pussissa ilman paine on yhä hieman suurempi kuin matkustamon paine. Siksi pussi tuntuu kovalta.

```pysahdy
Kaasun tilavuus pienenee kolmasosaan. Lämpötila pysyy samana. Mitä paineelle tapahtuu?
---
Paine kolminkertaistuu. Tulo $pV$ pysyy vakiona.
```

Boylen laki pätee hyvin ilmaan ja muihin kaasuihin tavallisissa paineissa ja lämpötiloissa. Kaasun määrän täytyy pysyä samana. Kaasua ei saa vuotaa pois eikä sitä saa tulla lisää. Paineena käytetään kaasun kokonaispainetta. Mittarin näyttämää ylipainetta ei käytetä.

Boylen lain voi todentaa kokeella. Ruiskuun suljetaan ilmaa, ja ruisku liitetään painemittariin. Mäntää painetaan vaiheittain. Jokaisella tilavuudella luetaan paine. Mittaus tehdään hitaasti, jotta ilman lämpötila ehtii palata huoneenlämpöön. Tulokset piirretään $(V, p)$-koordinaatistoon. Pisteet asettuvat laskevalle kaarelle. Kaarelta on vaikea nähdä, onko kyse juuri kääntäen verrannollisuudesta. Siksi taulukkoon lasketaan uusi sarake $1/V$. Sitten piirretään $p$ $1/V$:n funktiona. Jos laki pätee, pisteet asettuvat mittausepävarmuuden rajoissa origon kautta kulkevalle suoralle. Suoran kulmakerroin (suoran jyrkkyys) on vakio $pV$. Kokeile simulaatiossa: tallenna mittauksia eri tilavuuksilla ja valitse ”Piirrä p 1/V:n funktiona”.

Kun kaasua lämmitetään, sen hiukkaset liikkuvat nopeammin. Oletetaan, että mäntä pääsee liikkumaan niin, että paine pysyy vakiona (isobaarinen tilanmuutos). Silloin kaasu laajenee. Kun kaasun määrä pysyy samana ja kaasu on harvaa (hiukkaset ovat kaukana toisistaan), sen tilavuus on suoraan verrannollinen kelvinlämpötilaan. Se tarkoittaa, että kun kelvinlämpötila kaksinkertaistuu, tilavuus kaksinkertaistuu. Oletetaan sitten, että tilavuus pidetään vakiona (isokoorinen tilanmuutos). Silloin paine kasvaa. Paine on suoraan verrannollinen kelvinlämpötilaan. Molemmissa tapauksissa lämpötila pitää ilmoittaa kelvineinä, koska verrannollisuus alkaa absoluuttisesta nollapisteestä.

<svg data-fig="iso-processes" viewBox="0 0 600 412" role="img" aria-label="Kaksi tilanmuutosta, kaaviokuva. Vasemmalla on isobaarinen muutos. Sylinterin mäntää kuormittaa vakiopainoinen kappale. Kaasu lämpenee lämpötilasta T₁ lämpötilaan T₂. Mäntä nousee, ja tilavuus kasvaa V₁:stä V₂:een. Hiukkasten nopeusnuolet ovat pidempiä. Oikealla on isokoorinen muutos. Jäykän, suljetun astian tilavuus V pysyy samana. Kaasu lämpenee, ja paineenmittarin viisari kääntyy suuremman paineen p₂ kohdalle." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-9-iso-processes.webp" x="0" y="0" width="600" height="420" preserveAspectRatio="none"/>
  <foreignObject x="77.5" y="11.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{isobaarinen}$</div></foreignObject>
  <foreignObject x="377.5" y="11.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{isokoorinen}$</div></foreignObject>
  <foreignObject x="65" y="209.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$m$</div></foreignObject>
  <foreignObject x="40" y="349.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_1\text{, }V_1$</div></foreignObject>
  <foreignObject x="205" y="164.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$m$</div></foreignObject>
  <foreignObject x="180" y="349.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_2\text{, }V_2$</div></foreignObject>
  <foreignObject x="136" y="303.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="355" y="349.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_1\text{, }p_1$</div></foreignObject>
  <foreignObject x="475" y="349.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_2\text{, }p_2$</div></foreignObject>
  <foreignObject x="440" y="303.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
</svg>

```pysahdy
Jäykässä, suljetussa astiassa oleva kaasu lämpenee. Mikä suure kasvaa? Miksi?
---
Paine kasvaa. Tilavuus on vakio, ja hiukkaset liikkuvat nopeammin.
```

<figure class="unit-photo"><img src="pics/fy3/barrel-balloon.webp" alt="Tutkijat täyttävät isoa läpinäkyvää palloa lumen keskellä."><figcaption>NASAn tutkimuspallon täyttö Etelämantereella. Heliumia laitetaan vain pallon yläosaan. Kaasu laajenee, kun pallo nousee ja ulkoilman paine pienenee.</figcaption></figure>

## Kaava: Boylen laki ja kaasun tilanmuutokset
Isotermisessä tilanmuutoksessa eli Boylen lain mukaan
```latex
p_1 V_1 = p_2 V_2
```
Tässä $p_1$ ja $V_1$ ovat kaasun paine (Pa) ja tilavuus (m³) alkutilassa. Suureet $p_2$ ja $V_2$ ovat paine ja tilavuus lopputilassa. Yhtälö on sama kuin $pV = \text{vakio}$. Kun yhtälö jaetaan $V$:llä, saadaan
```latex
p = \text{vakio} \cdot \frac{1}{V}
```
Paine on siis kääntäen verrannollinen tilavuuteen. Merkitään $x = 1/V$ ja $y = p$. Silloin yhtälö on muotoa $y = kx$, kuten FY1:n suoran yhtälö. Siksi $(1/V, p)$-kuvaaja on origon kautta kulkeva suora. Suoran kulmakerroin on $k = pV$.

Tulon $pV$ yksikkö on $\text{Pa} \cdot \text{m}^3 = \text{N/m}^2 \cdot \text{m}^3 = \text{N} \cdot \text{m} = \text{J}$. Lisäksi $1\,\text{kPa} \cdot 1\,\textsf{l} = 1\,\text{J}$. Yhtälön $p_1 V_1 = p_2 V_2$ molemmilla puolilla on samat yksiköt. Siksi paineen ja tilavuuden voi ilmoittaa myös esimerkiksi kilopascaleina ja litroina. Yksiköiden pitää olla samat molemmilla puolilla.

<svg data-fig="boyle-graphs" viewBox="0 0 600 580" role="img" aria-label="Kaksi kuvaajaa samoista mittauksista, mittakaavassa, kun pV = 2000 kPa·ml. Ylhäällä on paine tilavuuden funktiona. Se on laskeva kaari, ja mittauspisteet V = 10, 15, 20, 30 ja 40 ml ovat kaarella. Alhaalla on paine tilavuuden käänteisluvun 1/V funktiona. Se on origon kautta kulkeva suora, jonka kulmakerroin on pV." style="max-width:100%;font-size:24px">
  <line x1="170" y1="250" x2="170" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="244.5" y1="250" x2="244.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="318.5" y1="250" x2="318.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="393" y1="250" x2="393" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="215" x2="430" y2="215" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="180.5" x2="430" y2="180.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="145.5" x2="430" y2="145.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="111" x2="430" y2="111" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="250" x2="444" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,250 L443,256 L443,244 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="251" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="170" y1="250" x2="170" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="153.5" y="259.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="244.5" y1="250" x2="244.5" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="228" y="259.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="318.5" y1="250" x2="318.5" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="302" y="259.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="393" y1="250" x2="393" y2="257" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="376.5" y="259.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="89" y1="215" x2="96" y2="215" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="200.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="180.5" x2="96" y2="180.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="166" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="145.5" x2="96" y2="145.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="131" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="89" y1="111" x2="96" y2="111" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="96.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="89" y1="76" x2="96" y2="76" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="61.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <foreignObject x="66" y="255.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="462" y="235.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{ml})$</div></foreignObject>
  <foreignObject x="86" y="19.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <polyline points="155.5,76 157,81 159,85.5 160.5,90 162,94 164,98 165.5,101.5 167.5,105.5 169,108.5 171,112 172.5,115 174.5,118 176,121 177.5,123.5 179.5,126 181,128.5 183,131 184.5,133.5 186.5,135.5 188,137.5 189.5,139.5 191.5,141.5 193,143.5 195,145.5 196.5,147.5 198.5,149 200,150.5 201.5,152.5 203.5,154 205,155.5 207,157 208.5,158 210.5,159.5 212,161 213.5,162 215.5,163.5 217,164.5 219,166 220.5,167 222.5,168 224,169.5 225.5,170.5 227.5,171.5 229,172.5 231,173.5 232.5,174.5 234.5,175.5 236,176 238,177 239.5,178 241,179 243,179.5 244.5,180.5 246.5,181.5 248,182 250,183 251.5,183.5 253,184.5 255,185 256.5,185.5 258.5,186.5 260,187 262,187.5 263.5,188.5 265,189 267,189.5 268.5,190 270.5,191 272,191.5 274,192 275.5,192.5 277,193 279,193.5 280.5,194 282.5,194.5 284,195 286,195.5 287.5,196 289.5,196.5 291,197 292.5,197.5 294.5,198 296,198.5 298,199 299.5,199 301.5,199.5 303,200 304.5,200.5 306.5,201 308,201.5 310,201.5 311.5,202 313.5,202.5 315,203 316.5,203 318.5,203.5 320,204 322,204.5 323.5,204.5 325.5,205 327,205.5 328.5,205.5 330.5,206 332,206.5 334,206.5 335.5,207 337.5,207 339,207.5 340.5,208 342.5,208 344,208.5 346,208.5 347.5,209 349.5,209 351,209.5 353,210 354.5,210 356,210.5 358,210.5 359.5,211 361.5,211 363,211.5 365,211.5 366.5,212 368,212 370,212.5 371.5,212.5 373.5,212.5 375,213 377,213 378.5,213.5 380,213.5 382,214 383.5,214 385.5,214.5 387,214.5 389,214.5 390.5,215 392,215 394,215.5 395.5,215.5 397.5,215.5 399,216 401,216 402.5,216.5 404.5,216.5 406,216.5 407.5,217 409.5,217 411,217 413,217.5 414.5,217.5 416.5,217.5 418,218 419.5,218 421.5,218.5 423,218.5 425,218.5 426.5,218.5 428.5,219 430,219" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="170" cy="111" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="207.5" cy="157" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="244.5" cy="180.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="318.5" cy="203.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="393" cy="215" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="440" y="200.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2f74b5">$\text{kaari}$</div></foreignObject>
  <line x1="207.5" y1="520" x2="207.5" y2="346" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="318.5" y1="520" x2="318.5" y2="346" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="520" x2="430" y2="346" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="485" x2="430" y2="485" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="450.5" x2="430" y2="450.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="415.5" x2="430" y2="415.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="381" x2="430" y2="381" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="346" x2="430" y2="346" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="520" x2="444" y2="520" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,520 L443,526 L443,514 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="521" x2="96" y2="332" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,320 L102,333 L90,333 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="207.5" y1="520" x2="207.5" y2="527" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="178.5" y="529.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}04$</div></foreignObject>
  <line x1="318.5" y1="520" x2="318.5" y2="527" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="289.5" y="529.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}08$</div></foreignObject>
  <line x1="430" y1="520" x2="430" y2="527" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="401" y="529.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}12$</div></foreignObject>
  <line x1="89" y1="485" x2="96" y2="485" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="470.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="450.5" x2="96" y2="450.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="436" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="415.5" x2="96" y2="415.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="401" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="89" y1="381" x2="96" y2="381" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="366.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="89" y1="346" x2="96" y2="346" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="331.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <foreignObject x="66" y="525.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="462" y="505.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1/V\ (\text{1/ml})$</div></foreignObject>
  <foreignObject x="86" y="289.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <polyline points="96,520 430,353" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="374.5" cy="381" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="281.5" cy="427" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="235" cy="450.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="189" cy="473.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="165.5" cy="485" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="440" y="360.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2f74b5">$\text{suora}$</div></foreignObject>
</svg>

Isobaarisessa ja isokoorisessa tilanmuutoksessa
```latex
\frac{V_1}{T_1} = \frac{V_2}{T_2} \qquad \text{ja} \qquad \frac{p_1}{T_1} = \frac{p_2}{T_2}
```
Tässä $T_1$ ja $T_2$ ovat kaasun lämpötilat kelvineinä (K) alku- ja lopputilassa. Suljetun, harvan kaasun tilavuus tai paine on siis suoraan verrannollinen kelvinlämpötilaan. $(T, V)$- tai $(T, p)$-kuvaajan suoran jatke kulkee origon kautta. Origo on absoluuttinen nollapiste $0\,\text{K}$. Jatke on mallin ennuste. Todellinen kaasu tiivistyy nesteeksi ennen kuin $0\,\text{K}$ saavutetaan.

Kelvinlämpötilan saa celsiuslämpötilasta $\theta$ lisäämällä 273,15:
```latex
T = \theta + 273{,}15\,\text{K}
```
Tässä $\theta$ on lämpötila celsiusasteina lukuarvona. Laskuissa riittää $273\,\text{K}$.

<svg data-fig="absolute-zero" viewBox="0 0 600 640" role="img" aria-label="Kuvaajat mittakaavassa, kun T on 0–400 K. Ylhäällä on kaasun tilavuus vakiopaineessa. Alhaalla on kaasun paine vakiotilavuudessa. Molemmat ovat kelvinlämpötilan funktioita. Mittauspisteet välillä 253–373 K ovat suoralla. Suoran jatke on piirretty katkoviivalla, ja se kulkee origon kautta. Tilavuus tai paine olisi nolla absoluuttisessa nollapisteessä 0 K eli −273 °C." style="max-width:100%;font-size:24px">
  <line x1="179.5" y1="240" x2="179.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263" y1="240" x2="263" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="346.5" y1="240" x2="346.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="240" x2="430" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="189" x2="430" y2="189" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="137.5" x2="430" y2="137.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="86" x2="430" y2="86" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="240" x2="444" y2="240" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,240 L443,246 L443,234 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="241" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="179.5" y1="240" x2="179.5" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="157" y="249.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="263" y1="240" x2="263" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="240.5" y="249.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="346.5" y1="240" x2="346.5" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="324" y="249.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="430" y1="240" x2="430" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="407.5" y="249.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="89" y1="189" x2="96" y2="189" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="174" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="137.5" x2="96" y2="137.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="123" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="86" x2="96" y2="86" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="72" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <foreignObject x="462" y="225.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ (\text{K})$</div></foreignObject>
  <foreignObject x="86" y="19.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\textsf{l})$</div></foreignObject>
  <foreignObject x="86" y="249.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="61" y="283.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$-273^\circ\text{C}$</div></foreignObject>
  <polyline points="96,240 307.5,145" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 8"/>
  <polyline points="307.5,145 407.5,100" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="307.5" cy="145" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="134" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="357.5" cy="122.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="382.5" cy="111.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="407.5" cy="100" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="148.5" y="162" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{jatke}$</span></div></foreignObject>
  <line x1="179.5" y1="556" x2="179.5" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263" y1="556" x2="263" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="346.5" y1="556" x2="346.5" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="556" x2="430" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="506" x2="430" y2="506" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="456" x2="430" y2="456" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="406" x2="430" y2="406" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="556" x2="444" y2="556" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,556 L443,562 L443,550 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="557" x2="96" y2="382" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,370 L102,383 L90,383 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="179.5" y1="556" x2="179.5" y2="563" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="157" y="565.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="263" y1="556" x2="263" y2="563" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="240.5" y="565.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="346.5" y1="556" x2="346.5" y2="563" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="324" y="565.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="430" y1="556" x2="430" y2="563" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="407.5" y="565.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="89" y1="506" x2="96" y2="506" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="491.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="456" x2="96" y2="456" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="441.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="406" x2="96" y2="406" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="391.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <foreignObject x="462" y="541.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ (\text{K})$</div></foreignObject>
  <foreignObject x="86" y="339.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <foreignObject x="86" y="565.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="61" y="599.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$-273^\circ\text{C}$</div></foreignObject>
  <polyline points="96,556 307.5,462.5" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 8"/>
  <polyline points="307.5,462.5 407.5,418" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="307.5" cy="462.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="451.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="357.5" cy="440.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="382.5" cy="429" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="407.5" cy="418" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="148.5" y="478.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{jatke}$</span></div></foreignObject>
</svg>

```pysahdy
Kaasun lämpötila nousee vakiotilavuudessa $20\,{}^\circ\text{C}$:sta $40\,{}^\circ\text{C}$:een. Kaksinkertaistuuko paine?
---
Ei kaksinkertaistu. Kelvineinä lämpötila nousee $293\,\text{K}$:sta $313\,\text{K}$:iin. Paine kasvaa vain tekijällä $313/293 \approx 1{,}07$.
```

## Esimerkki
Sipsipussissa on lentokentällä $0{,}80\,\textsf{l}$ ilmaa $101\,\text{kPa}$:n paineessa. Lennon aikana matkustamon paine on $78\,\text{kPa}$. Kuinka suuri on pussissa olevan ilman tilavuus lennolla? Lämpötila pysyy samana, ja pussi pääsee laajenemaan vapaasti.

<!-- vaihe -->

**Tunnetut ja kysytty.** Tunnetaan $p_1 = 101\,\text{kPa}$, $V_1 = 0{,}80\,\textsf{l}$ ja $p_2 = 78\,\text{kPa}$. Lämpötila on sama.

Kysytään lopputilavuutta $V_2$ litroina.

<!-- vaihe -->

**Periaate.** Pussi on suljettu, joten ilman määrä ei muutu. Lämpötila pysyy samana. Tilanmuutos on siis isoterminen ja Boylen laki pätee. Tulo $pV$ pysyy vakiona. Pussi laajenee vapaasti. Siksi sen sisällä on aina sama paine kuin matkustamossa.

<!-- vaihe -->

**Kaava ratkaistuna.** Ratkaistaan Boylen laista $V_2$. Molemmat puolet jaetaan paineella $p_2$:
```latex
\begin{aligned}
p_1 V_1 &= p_2 V_2 \\
V_2 &= \frac{p_1 V_1}{p_2}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Yksikköjä ei tarvitse muuntaa. Molemmat paineet ovat kilopascaleina, joten ne supistuvat osamäärässä. Tilavuus tulee suoraan litroina.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan arvot yksiköineen:
```latex
\begin{aligned}
V_2 &= \frac{p_1 V_1}{p_2} \\
&= \frac{101\,\text{kPa} \cdot 0{,}80\,\textsf{l}}{78\,\text{kPa}} \\
&= 1{,}036\,\textsf{l}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Ilman tilavuus on $V_2 \approx 1{,}0\,\textsf{l}$. Tulos on annettu kahdella merkitsevällä numerolla, kuten lähtötiedot $0{,}80\,\textsf{l}$ ja $78\,\text{kPa}$. Tilavuus kasvaa noin $30\,\%$. Jos pussi on valmiiksi lähes täynnä, se pullistuu kireäksi.

<!-- vaihe -->

**Järkevyys.** Paine pienenee, joten tilavuuden täytyy kasvaa. Kasvukerroin on painesuhde $101/78 \approx 1{,}3$. Lasketaan: $0{,}80\,\textsf{l} \cdot 1{,}3 \approx 1{,}0\,\textsf{l}$. Tulo $pV$ on lopussa $78\,\text{kPa} \cdot 1{,}036\,\textsf{l} \approx 80{,}8\,\text{kPa}\cdot\textsf{l}$. Se on sama kuin alussa: $101\,\text{kPa} \cdot 0{,}80\,\textsf{l} = 80{,}8\,\text{kPa}\cdot\textsf{l}$.

## Yleinen virhekäsitys
Nämä kolme virhettä toistuvat usein:

- **Kääntäen verrannollisuus ei ole laskeva suora.** Kun tilavuus kaksinkertaistuu, paine puolittuu. Siksi $(V, p)$-kuvaaja on kaari. Kaari lähestyy akseleita, mutta ei koskaan kohtaa niitä. Suora syntyy vasta, kun $p$ piirretään $1/V$:n funktiona.
- **Celsiusasteet eivät kelpaa lämpötilojen suhteeseen.** Oletetaan, että $1{,}00\,\textsf{l}$ ilmaa lämpenee vakiopaineessa $10\,{}^\circ\text{C}$:sta $20\,{}^\circ\text{C}$:seen. Sen tilavuus ei kaksinkertaistu. Kelvineinä laskettuna $$\begin{aligned} V_2 &= V_1 T_2 / T_1 \\ &= 1{,}00\,\textsf{l} \cdot 293\,\text{K} / 283\,\text{K} \\ &\approx 1{,}04\,\textsf{l} \end{aligned}$$. Tilavuus kasvaa siis vain noin $3{,}5\,\%$.
- **Suljetun astian kaasun paine ei johdu kaasun painosta.** Pienessä astiassa kaasun paino on mitätön. Paine syntyy hiukkasten törmäyksistä. Siksi paine on yhtä suuri kaikkialla astiassa.

## Tiivistelmä
- Tilanmuutoksessa kaasun paine, tilavuus ja lämpötila muuttuvat. Isotermisessä muutoksessa $T$ on vakio, isobaarisessa $p$ ja isokoorisessa $V$.
- Boylen laki: isotermisessä tilanmuutoksessa $p_1 V_1 = p_2 V_2$. Paine on siis kääntäen verrannollinen tilavuuteen.
- Kääntäen verrannollisuus todennetaan näin: taulukkoon lasketaan sarake $1/V$ ja $p$ piirretään $1/V$:n funktiona. Pisteiden pitää asettua mittausepävarmuuden rajoissa origon kautta kulkevalle suoralle.
- Kun kaasun määrä pysyy samana, harvan kaasun tilavuus vakiopaineessa on suoraan verrannollinen kelvinlämpötilaan. Vakiotilavuudessa paine on suoraan verrannollinen kelvinlämpötilaan. Näissä laskuissa lämpötilat ilmoitetaan aina kelvineinä.
