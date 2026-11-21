# Kaasun tekemä työ ja lämpövoimakone

> **Miksi** lämpövoimalaitos saa polttoaineen energiasta sähköksi vain alle puolet, ja minne loput energiasta menee?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: lauhdevoimalaitos järven rannalla. Voimalinjat vievät sähköä pois, jäähdytystornista nousee suuri höyrypilvi, ja lauhdevesi purkautuu järveen lämpimänä, mikä näkyy oranssina vyöhykkeenä vedessä. Suurin osa polttoaineen energiasta lähtee lämpönä ilmaan ja veteen." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-11-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Kun kaasu laajenee ja työntää mäntää, se tekee työtä. Kaasu painaa mäntää voimalla $F = pA$, missä $A$ on männän pinta-ala. Jos mäntä liikkuu matkan $s$ ja paine pysyy samana, kaasun tekemä työ on voima kertaa matka, $pAs$. Tulo $As$ on kaasun tilavuuden muutos $\Delta V$, joten kaasun tekemä työ on $W = p\,\Delta V$. ($V$, $p$)-kuvaajassa se on kuvaajan ja $V$-akselin väliin jäävä pinta-ala, samoin kuin työ ($s$, $F$)-kuvaajassa. Kun kaasua puristetaan, ympäristö tekee kaasuun puristustyön, jonka suuruus lasketaan samalla kaavalla. Työtä tekevä kaasu luovuttaa energiaa, joten sen sisäenergia kasvaa vähemmän kuin siihen tuotu lämpö.

<svg data-fig="piston-work" viewBox="0 0 600 330" role="img" aria-label="Kaasun tekemä työ männälle, periaatekuva. Sylinterin poikkipinta-ala on A. Kaasun paine p työntää mäntää voimalla F = pA, ja mäntä siirtyy matkan Δs oikealle. Kaasun tilavuus kasvaa varjostetun osan verran, ΔV = AΔs. Työ on W = FΔs = pAΔs = pΔV. Kuva ei ole mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-11-piston-work.webp" x="1.2" y="0" width="597" height="339.6" preserveAspectRatio="none"/>
  <foreignObject x="449" y="85.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$F = pA$</div></foreignObject>
  <foreignObject x="130.5" y="115.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kaasu},\ p$</div></foreignObject>
  <foreignObject x="318.5" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta V$</span></div></foreignObject>
  <foreignObject x="46" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="318.5" y="228.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta s$</div></foreignObject>
  <foreignObject x="190" y="275.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = F\,\Delta s = pA\,\Delta s = p\,\Delta V$</div></foreignObject>
</svg>

```pysahdy
Kaasun paine on $100\,\text{kPa}$, ja se laajenee tilavuuden $0{,}010\,\text{m}^3$ verran. Paine pysyy vakiona. Kuinka suuren työn kaasu tekee?
---
$W = p\,\Delta V$, joten $W = 1{,}0\,\text{kJ}$ ($100\,000\,\text{Pa} \cdot 0{,}010\,\text{m}^3$).
```

### Lämpövoimakone toistaa liikettään
Lämpövoimakone muuttaa lämpöä jatkuvasti työksi, joten sen on toistettava liikettään. Mäntä on saatava takaisin alas. Jos se painetaan alas samassa paineessa, palautus vie koko kaasun tekemän työn. Palautus vaatii vähemmän työtä, jos kaasu jäähdytetään ensin pienempään paineeseen, mutta silloin kaasu luovuttaa lämpöä kylmempään ympäristöön. Höyryvoimalaitoksessa vesi kiehuu kattilassa, kuuma höyry laajenee turbiinissa ja pyörittää generaattoria, ja turbiinista tuleva höyry tiivistyy jälleen vedeksi lauhduttimessa, jota merivesi jäähdyttää. Työaine kiertää samaa rataa yhä uudelleen, joten kierroksen lopussa sen sisäenergia on sama kuin alussa. Energia säilyy: kuumasta lähteestä tullut lämpö $Q_1$ on yhtä suuri kuin koneen tekemä työ $W$ ja kylmempään ympäristöön luovutettu lämpö $Q_2$ yhteensä.

<figure class="unit-photo"><img src="pics/fy3/steam-locomotive-wheel.webp" alt="Punaisen höyryveturin suuri vetopyörä ja siihen liitetty kiertokanki läheltä."><figcaption>Höyryveturissa laajeneva höyry työntää mäntää, ja kiertokanki muuttaa männän edestakaisen liikkeen pyörien pyörimiseksi.</figcaption></figure>

Kokemus osoittaa, ettei lämpövoimakone voi muuttaa kaikkea saamaansa lämpöä työksi, vaan osa on aina luovutettava kylmempään ympäristöön. Tämä on termodynamiikan toisen pääsäännön sisältö. Mitä suurempi on kuuman lähteen ja kylmän ympäristön lämpötilaero kuuman lähteen lämpötilaan nähden, sitä suuremman osan lämmöstä kone voi muuttaa työksi. Kiertoprosesseja ei tällä kurssilla lasketa; simulaatio näyttää vain, miksi lämpöä $Q_2$ ei voi välttää.

<svg data-fig="heat-engine" viewBox="0 0 600 340" role="img" aria-label="Lämpövoimakoneen energiavirrat nuolina, joiden leveys kuvaa energiavirtaa eli tehoa: kuumasta lähteestä, jonka lämpötila on T_1, tulee koneeseen lämpö Q_1. Kone tekee työn W, joka on 40 prosenttia Q_1:stä, ja luovuttaa loput, lämmön Q_2, kylmään ympäristöön, jonka lämpötila on T_2. Nuolten leveydet ovat mittakaavassa: Q_1 60, W 24 ja Q_2 36 yksikköä, joten Q_1-nuoli on yhtä leveä kuin W- ja Q_2-nuolet yhteensä." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-11-heat-engine.webp" x="1.2" y="0" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="215" y="23.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kuuma lähde}\quad T_1$</div></foreignObject>
  <foreignObject x="190" y="287.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kylmä ympäristö}\quad T_2$</div></foreignObject>
  <foreignObject x="271" y="152.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kone}$</div></foreignObject>
  <foreignObject x="354" y="77.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_1$</div></foreignObject>
  <foreignObject x="342" y="229.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_2$</div></foreignObject>
  <foreignObject x="460" y="119.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W$</div></foreignObject>
  <foreignObject x="16" y="137.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{nuolen leveys}$</div></foreignObject>
  <foreignObject x="16" y="167.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kuvaa tehoa}$</div></foreignObject>
</svg>

```pysahdy
Voiko lämpövoimakone muuttaa kaiken saamansa lämmön työksi?
---
Ei voi. Osa lämmöstä on aina luovutettava kylmempään ympäristöön.
```

### Hyötysuhde
Hyötysuhde kertoo, kuinka suuri osa koneeseen tuodusta energiasta saadaan hyödyksi, joten sen arvo riippuu siitä, mikä lasketaan hyödyksi. Voimalaitoksen sähköntuotannon hyötysuhteessa hyötyä on vain sähkö. Suomalainen lauhdevoimalaitos, joka tuottaa vain sähköä, saa polttoaineen energiasta sähköksi noin $40\,\%$, ja ydinvoimalaitos noin $35\,\%$. Suurin osa lopusta siirtyy lauhduttimen kautta mereen, ja polttoainetta käyttävästä laitoksesta osa poistuu myös savukaasujen mukana ilmaan. Automoottorin hyötysuhde on noin $30\,\%$, ja loput energiasta poistuu pakokaasujen ja jäähdyttimen mukana.

Sähkön ja lämmön yhteistuotannossa lauhduttimen lämpö $Q_2$ otetaan talteen: se lämmittää kaukolämpöverkon vettä, joka vie sen kaupungin taloihin. Lämpövoimakone luovuttaa siis edelleen lämpöä kylmempään, mutta tämä lämpö käytetään hyödyksi. Kokonaishyötysuhteessa hyödyksi lasketaan sähkö ja kaukolämpö yhteensä, ja se on 85–$90\,\%$. Sähköntuotannon hyötysuhde ei siis nouse, vaan on yleensä pienempi kuin pelkkää sähköä tuotettaessa. Tämä vastaa alun kysymykseen: sähköksi saadaan alle puolet, mutta loput eivät katoa, vaan siirtyvät lämpönä ympäristöön tai kaukolämpöverkkoon.

### Jäähdytyskone ja lämpöpumppu
Jäähdytyskone ja lämpöpumppu toimivat päinvastoin kuin lämpövoimakone: ne käyttävät sähköenergiaa ja siirtävät sen avulla lämpöä kylmästä paikasta lämpimään. Jääkaappi siirtää lämpöä kaapin sisältä huoneeseen, ja ilmalämpöpumppu ulkoilmasta sisälle. Sisälle luovutettu lämpö on ulkoa otetun lämmön ja käytetyn sähkön summa, joten pumppu voi lämmittää taloa esimerkiksi kolminkertaisella teholla käyttämäänsä sähkötehoon verrattuna. Tätä lämpötehon ja sähkötehon suhdetta sanotaan lämpökertoimeksi. Lämpökerroin ei ole hyötysuhde: se voi olla yli 1, koska osa sisälle tulevasta lämmöstä siirretään ulkoilmasta eikä tule sähköstä. Pumppu ei luo energiaa, vaan siirtää sitä.

<svg data-fig="heat-pump" viewBox="0 0 600 340" role="img" aria-label="Lämpöpumpun energiavirrat nuolina, joiden leveys kuvaa tehoa: sähköenergia W ja ulkoilmasta otettu lämpö Q_2 tulevat pumppuun, ja pumppu luovuttaa sisälle lämmön Q_1, joka on niiden summa. Nuolten leveydet ovat mittakaavassa: W 20, Q_2 40 ja Q_1 60 yksikköä, joten sisälle lähtevä nuoli on yhtä leveä kuin kaksi tulevaa nuolta yhteensä ja kolme kertaa niin leveä kuin sähkön nuoli." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-11-heat-pump.webp" x="1.2" y="0" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="215" y="23.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kylmä ulkoilma}$</div></foreignObject>
  <foreignObject x="208.5" y="287.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämmin sisätila}$</div></foreignObject>
  <foreignObject x="258.5" y="152.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pumppu}$</div></foreignObject>
  <foreignObject x="344" y="77.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_2$</div></foreignObject>
  <foreignObject x="78.5" y="119.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sähkö}\ W$</div></foreignObject>
  <foreignObject x="354" y="230.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_1$</div></foreignObject>
  <foreignObject x="426" y="137.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{nuolen leveys}$</div></foreignObject>
  <foreignObject x="451" y="167.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{kuvaa tehoa}$</div></foreignObject>
</svg>

```pysahdy
Lämpöpumpun lämpökerroin on 3. Kuinka paljon lämpöä se luovuttaa sisälle $1\,\text{kWh}$:lla sähköä, ja mistä loppu lämpö tulee?
---
Sisälle tulee $3\,\text{kWh}$ lämpöä. Sähköä on $1\,\text{kWh}$, ja loput $2\,\text{kWh}$ siirretään ulkoilmasta.
```

## Kaava: Kaasun työ ja hyötysuhde
Kun kaasun paine pysyy vakiona, kaasun tekemä laajenemistyö on
```kaavat
kaasun tekemä laajenemistyö / kaasuun tehty puristustyö :: W = p\,\Delta V
```
missä $W$ on kaasun tekemä työ (J), $p$ kaasun paine (Pa) ja $\Delta V$ kaasun tilavuuden muutos (m³). Kun kaasua puristetaan, sama kaava antaa ympäristön kaasuun tekemän puristustyön suuruuden. Kaasun sisäenergian muutoksen antaa lämpöopin ensimmäinen pääsääntö
```kaavat
lämpöopin 1. pääsääntö :: \Delta U = Q + W
```
missä $Q$ on kaasuun siirtynyt lämpö (J) ja $W$ kaasuun tehty työ (J), kuten luvussa *Sisäenergia, lämpömäärä ja energian säilyminen*. Pääsäännössä $W$ on siis kaasuun tehty työ: kun kaasu laajenee ja tekee työn $p\,\Delta V$, siihen tehty työ on $W = -p\,\Delta V$, joten $\Delta U = Q - p\,\Delta V$.

Lämpövoimakoneen yhden kierroksen aikana tekemä työ ja hyötysuhde ovat
```latex
W = Q_1 - Q_2
```
```kaavat
lämpövoimakoneen hyötysuhde :: \eta = \frac{W}{Q_1} = \frac{Q_1 - Q_2}{Q_1}
```
missä $Q_1$ on kuumasta lähteestä koneeseen siirtynyt lämpö (J), $Q_2$ kylmempään ympäristöön luovutettu lämpö (J), $W$ koneen kierroksen aikana tekemä työ (J) ja $\eta$ hyötysuhde, joka ilmoitetaan usein prosentteina. Hyötysuhde voidaan laskea samalla tavalla tehoista, esimerkiksi sähköteho jaettuna polttoaineteholla.

<svg data-fig="pv-work" viewBox="0 0 600 330" role="img" aria-label="(V, p)-kuvaaja vakiopaineessa laajenevasta kaasusta: paine p pysyy vakiona, kun tilavuus kasvaa arvosta V_1 arvoon V_2, joten kuvaaja on vaakasuora jana, jonka nuoli osoittaa laajenemisen suuntaa. Janan ja V-akselin väliin jäävä varjostettu suorakulmio, jonka leveys on tilavuuden muutos ΔV ja korkeus p, on kaasun tekemä työ W = p ΔV. Kaaviokuva." style="max-width:100%;font-size:24px">
  <line x1="203" y1="270" x2="203" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="363" y1="270" x2="363" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="112.5" x2="470" y2="112.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="270" x2="484" y2="270" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,270 L483,276 L483,264 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="271" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="203" y1="270" x2="203" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="186.5" y="279.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V_1$</div></foreignObject>
  <line x1="363" y1="270" x2="363" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="346.5" y="279.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V_2$</div></foreignObject>
  <line x1="89" y1="112.5" x2="96" y2="112.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="98" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$p$</div></foreignObject>
  <foreignObject x="66" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="255.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{m}^3)$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{Pa})$</div></foreignObject>
  <polygon points="203,270 363,270 363,112.5 203,112.5" fill="#e8590c" fill-opacity="0.35"/>
  <polyline points="203,112.5 363,112.5" fill="none" stroke="#1f2933" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="203" y1="112.5" x2="203" y2="270" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="363" y1="112.5" x2="363" y2="270" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="269" y1="112.5" x2="278" y2="112.5" stroke="#1f2933" stroke-width="4.5" stroke-linecap="butt"/>
  <path d="M297,112.5 L277,121.5 L277,103.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="198" y="72" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kaasu laajenee}$</div></foreignObject>
  <foreignObject x="241.5" y="156" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = p\,\Delta V$</div></foreignObject>
  <line x1="257" y1="228" x2="218" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M206,228 L219,222 L219,234 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="309" y1="228" x2="348" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M360,228 L347,234 L347,222 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="266.5" y="213.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta V$</div></foreignObject>
</svg>

Lämpöpumppu luovuttaa sisälle lämmön $Q_1$, joka on ulkoilmasta otetun lämmön $Q_2$ ja pumpun käyttämän sähköenergian $W$ summa. Energia säilyy, joten pumpun käyttämä sähköenergia on $W = Q_1 - Q_2$. Lämpökerroin kertoo, kuinka moninkertaisen lämmön pumppu luovuttaa sisälle käyttämäänsä sähköenergiaan verrattuna:
```kaavat
lämpöpumpun suorituskyky :: \varepsilon = \frac{Q_1}{W} = \frac{Q_1}{Q_1 - Q_2}
```
missä $Q_1$ on lämpimälle puolelle eli sisälle luovutettu lämpö (J), $Q_2$ kylmältä puolelta eli ulkoilmasta otettu lämpö (J), $W$ pumpun käyttämä sähköenergia eli työ (J) ja $\varepsilon$ lämpökerroin. Lämpökerroin voidaan laskea samalla tavalla tehoista.

## Esimerkki
Biovoimalaitoksen kattilaan syötetään puuhakkeen energiaa teholla $500\,\text{MW}$. Kun laitos tuottaa pelkkää sähköä, sähköteho on $190\,\text{MW}$. Talvella sama laitos toimii yhteistuotantovoimalaitoksena: se tuottaa $150\,\text{MW}$ sähköä ja $290\,\text{MW}$ kaukolämpöä. Mikä on hyötysuhde kummassakin tapauksessa, ja kuinka suuri teho siirtyy ympäristöön hukkalämpönä?

<!-- vaihe -->

**Tunnetut ja kysytty.** Polttoaineteho $P_1 = 500\,\text{MW}$. Pelkkää sähköä tuotettaessa sähköteho $P_\text{s} = 190\,\text{MW}$; yhteistuotannossa $P_\text{s} = 150\,\text{MW}$ ja kaukolämpöteho $P_\text{k} = 290\,\text{MW}$.

Kysytään hyötysuhteita $\eta$ ja hukkalämmön tehoa $P_2$ kummassakin tapauksessa.

<!-- vaihe -->

**Periaate.** Hyötysuhde on hyödyksi saatu teho jaettuna syötetyllä teholla; se lasketaan tehoista samoin kuin energioista, koska molemmat ovat energiaa samassa ajassa. Energia säilyy, joten polttoaineteho jakautuu hyödyksi saatuun tehoon ja hukkalämpöön. Hyödyksi tulee pelkässä sähköntuotannossa vain sähkö, yhteistuotannossa sähkö ja kaukolämpö.

<!-- vaihe -->

**Kaava ratkaistuna.** Ratkaistaan kysytyt suureet symboleilla ennen lukuja:
```latex
\begin{aligned}
\eta &= \frac{P_\text{a}}{P_1} \\
P_2 &= P_1 - P_\text{a}
\end{aligned}
```
Hyödyksi saatu teho eli antoteho on $P_\text{a}$: pelkälle sähkölle $P_\text{a} = P_\text{s}$ ja yhteistuotannolle $P_\text{a} = P_\text{s} + P_\text{k}$.

<!-- vaihe -->

**Yksikkömuunnokset.** Kaikki tehot on annettu megawatteina, joten muunnoksia ei tarvita: hyötysuhteessa yksikkö supistuu, ja hukkalämpö saadaan megawatteina. Desimaaliluku muutetaan prosenteiksi kertomalla sadalla.

<!-- vaihe -->

**Sijoitus.** Pelkälle sähkölle ja yhteistuotannolle erikseen:
```latex
\begin{aligned}
\eta_1 &= \frac{P_\text{s}}{P_1} \\
&= \frac{190\,\text{MW}}{500\,\text{MW}} \\
&= 0{,}380 \\
P_{2,1} &= P_1 - P_\text{s} \\
&= 500\,\text{MW} - 190\,\text{MW} \\
&= 310\,\text{MW} \\[6pt]
\eta_2 &= \frac{P_\text{s} + P_\text{k}}{P_1} \\
&= \frac{150\,\text{MW} + 290\,\text{MW}}{500\,\text{MW}} \\
&= 0{,}880 \\
P_{2,2} &= P_1 - (P_\text{s} + P_\text{k}) \\
&= 500\,\text{MW} - 440\,\text{MW} \\
&= 60\,\text{MW}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Pelkällä sähköntuotannolla hyötysuhde on $\eta_1 = 0{,}380 = 38{,}0\,\%$ ja hukkalämpöä siirtyy ympäristöön $310\,\text{MW}$, suurin osa lauhduttimen kautta mereen. Yhteistuotannossa kokonaishyötysuhde on $\eta_2 = 0{,}880 = 88{,}0\,\%$ ja hukkalämpöä on vain $60\,\text{MW}$. Tehot on annettu täysinä megawatteina, joten erotukset $310\,\text{MW}$ ja $60\,\text{MW}$ tunnetaan megawatin tarkkuudella.

Hyötysuhteet ovat osamääriä, joten niissä on yhtä monta numeroa kuin epätarkimmassa tehossa: $190\,\text{MW}$, $150\,\text{MW}$, $290\,\text{MW}$ ja $500\,\text{MW}$ ovat kaikki kolmen numeron arvoja, joten hyötysuhteet annetaan kolmella numerolla.

<!-- vaihe -->

**Järkevyys.** Energia säilyy: $190\,\text{MW} + 310\,\text{MW} = 500\,\text{MW}$ ja $$\begin{aligned} &150\,\text{MW} + 290\,\text{MW} + 60\,\text{MW} \\ &= 500\,\text{MW} \end{aligned}$$. Sähköntuotannon hyötysuhde jää selvästi alle $100\,\%$:n, koska lämpövoimakoneen on luovutettava osa lämmöstä kylmempään. Kokonaishyötysuhdekaan ei ole $100\,\%$, koska osa lämmöstä poistuu savukaasujen ja muiden häviöiden mukana. Sähköä saadaan yhteistuotannossa vähemmän, koska höyry lauhdutetaan korkeammassa lämpötilassa, jotta sen lämpö kelpaa kaukolämmöksi. Polttoaineen energia käytetään silti paljon paremmin hyödyksi.

## Yleinen virhekäsitys
Moni ajattelee, että parempi tekniikka voisi tehdä lämpövoimakoneesta lähes täydellisen, niin että kaikki lämpö muuttuisi työksi. Kitkan ja muiden häviöiden vähentäminen auttaa, mutta osa lämmöstä on aina luovutettava kylmempään ympäristöön, joten lämpövoimakoneen hyötysuhde jää selvästi alle $100\,\%$:n. Simulaation kitkaton mäntä näyttää syyn: jotta mäntä saadaan alas pienemmällä työllä kuin se nousi, kaasua on jäähdytettävä, ja jäähdytyksessä lämpöä siirtyy kylmään veteen. Raja koskee lämpöä työksi muuttavaa konetta, ei kaikkia laitteita: esimerkiksi sähkölämmittimessä käytännössä kaikki sähköenergia kasvattaa vastuksen sisäenergiaa ja siirtyy lämpönä huoneeseen.

Toinen virhe on pitää lämpöpumppua ikiliikkujana, koska se luovuttaa enemmän lämpöä kuin käyttää sähköä. Ylimääräinen lämpö tulee ulkoilmasta, eikä energiaa synny tyhjästä. Kolmas virhe on ajatella, että paineistettu kaasu tekee työtä jo sillä, että sen paine on suuri. Työtä tehdään vain, kun tilavuus muuttuu ja mäntä liikkuu.

## Tiivistelmä
- Vakiopaineessa laajeneva kaasu tekee työn $W = p\,\Delta V$, joka on ($V$, $p$)-kuvaajan alle jäävä pinta-ala. Ensimmäisessä pääsäännössä $\Delta U = Q + W$ työ $W$ on kaasuun tehty työ, joten laajenevalle kaasulle $\Delta U = Q - p\,\Delta V$.
- Mäntäkone voi toistaa työnsä vain, jos kaasu jäähdytetään ennen kuin mäntä palautetaan; silloin lämpöä siirtyy kylmempään.
- Lämpövoimakone ottaa lämpöä $Q_1$ kuumasta lähteestä, tekee työn $W$ ja luovuttaa lämmön $Q_2$ kylmempään ympäristöön: $W = Q_1 - Q_2$.
- Hyötysuhde on $\eta = W/Q_1 = (Q_1 - Q_2)/Q_1$. Lämpövoimakone ei voi muuttaa kaikkea lämpöä työksi.
- Lauhdevoimalaitoksen sähköntuotannon hyötysuhde on noin $40\,\%$. Sähkön ja lämmön yhteistuotannossa lauhduttimen lämpö käytetään kaukolämpönä, joten kokonaishyötysuhde, jossa hyödyksi lasketaan sähkö ja lämpö, on 85–$90\,\%$.
- Jäähdytyskone ja lämpöpumppu siirtävät työn avulla lämpöä kylmästä lämpimään. Ne eivät luo energiaa. Lämpöpumpun lämpökerroin $\varepsilon = Q_1/(Q_1 - Q_2)$, jossa $Q_1$ on sisälle luovutettu ja $Q_2$ ulkoilmasta otettu lämpö, ei ole hyötysuhde, ja se voi olla yli 1, koska osa lämmöstä tulee ulkoilmasta.
