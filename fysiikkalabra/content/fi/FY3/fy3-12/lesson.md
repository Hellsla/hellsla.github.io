# Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos

> **Miksi** maapallon keskilämpötila on noin $+15\,{}^\circ\text{C}$ eikä pakkasen puolella, vaikka maapallo säteilee avaruuteen yhtä paljon energiaa kuin imee Auringosta?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: Maa avaruudesta nähtynä, ympärillään ohut ilmakehä. Kuvan vasemmassa reunassa paistaa Aurinko, ja tähdet tuikkivat mustalla taivaalla." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-12-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Lämpötilaeron vuoksi energiaa siirtyy itsestään nettomääräisesti lämpimämmästä kappaleesta kylmempään. Näin siirtyvää energiaa sanotaan lämmöksi, ja se siirtyy kolmella tavalla. Johtumisessa energia siirtyy aineen läpi hiukkasesta toiseen, kun nopeammin värähtelevät hiukkaset tönivät hitaampia naapureitaan. Metallit johtavat lämpöä hyvin, koska niissä energiaa kuljettavat lisäksi ja pääosin vapaat elektronit; ilma ja villa johtavat huonosti. Konvektiossa lämmin neste tai kaasu virtaa ja kuljettaa energiaa mukanaan: lämmin ilma nousee patterin yläpuolella, koska se on laajentunut ja kevyempää kuin ympäröivä ilma.

Lämpösäteilyssä kappale lähettää sähkömagneettista säteilyä, joka ei tarvitse väliainetta. Näin Auringon energia tulee Maahan tyhjän avaruuden läpi, ja näin takan hehku lämmittää kasvoja. Kaikki kappaleet säteilevät, ja mitä kuumempi kappale on, sitä enemmän ja sitä lyhytaaltoisempaa säteilyä se lähettää. Lämpösäteilyä lähtee siis molemmista kappaleista, joten myös kylmempi kappale säteilee lämpimämpää kohti. Lämpimämpi säteilee kuitenkin enemmän, joten energiaa siirtyy nettona kylmempään.

<svg data-fig="heat-transfer" viewBox="0 0 600 300" role="img" aria-label="Kolme lämmön siirtymistapaa, periaatekuva. Johtuminen: lämpö kulkee metallitangon läpi kuumasta päästä kylmään. Konvektio: lämmin vesi nousee kattilassa keskellä ja jäähtynyt vajoaa reunoilla, joten vesi kiertää. Säteily: kuuma kappale lähettää säteilyä, joka kulkee tyhjän tilan läpi." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-12-heat-transfer.webp" x="6.2" y="7.4" width="594.1" height="308.2" preserveAspectRatio="none"/>
  <foreignObject x="14" y="177.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kuuma}$</div></foreignObject>
  <foreignObject x="116" y="177.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{kylmä}$</div></foreignObject>
  <foreignObject x="33.5" y="247.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{johtuminen}$</div></foreignObject>
  <foreignObject x="240" y="247.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{konvektio}$</div></foreignObject>
  <foreignObject x="452.5" y="247.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{säteily}$</div></foreignObject>
</svg>

```pysahdy
Auringon energia tulee Maahan tyhjän avaruuden läpi. Mikä lämmönsiirtotapa se on, ja miksi se ei ole johtumista eikä konvektiota?
---
Se on lämpösäteilyä. Säteily ei tarvitse väliainetta, mutta johtuminen ja konvektio tarvitsevat ainetta, jonka läpi energia siirtyy.
```

### Rakennuksen lämpöhäviöt
Talon lämmitysenergiasta suuri osa kuluu siihen, että lämpö johtuu seinien, katon, ikkunoiden ja lattian läpi ulos. Rakennusosan lämmöneristävyyttä kuvaa U-arvo eli lämmönläpäisykerroin, joka kertoo, kuinka monta wattia lämpötehoa siirtyy yhden neliömetrin läpi, kun sisä- ja ulkolämpötilan ero on yksi kelvin. Mitä pienempi U-arvo, sitä paremmin rakenne eristää. Nykyaikaisen seinän U-arvo on noin $0{,}17\,\text{W/(m}^2\text{}\cdot\text{K)}$, mutta hyvänkin ikkunan noin $1{,}0\,\text{W/(m}^2\text{}\cdot\text{K)}$, joten pieni ikkuna päästää läpi yhtä paljon lämpöä kuin moninkertainen ala seinää. Hyvä eristys säästää energiaa ja vähentää lämmityksen päästöjä.

```pysahdy
Seinän U-arvo on $0{,}17\,\text{W/(m}^2\text{}\cdot\text{K)}$ ja ikkunan $1{,}0\,\text{W/(m}^2\text{}\cdot\text{K)}$. Kumpi eristää paremmin, ja miksi?
---
Seinä eristää paremmin, koska sen U-arvo on pienempi. Sen läpi siirtyy vähemmän lämpötehoa samalla pinta-alalla ja lämpötilaerolla.
```

### Energiatasapaino
Kappaleen lämpötila pysyy vakiona, kun siihen tulee yhtä suuri teho kuin siitä lähtee. Tätä sanotaan energiatasapainoksi. Maapallo saa energiaa Auringon säteilynä, josta noin $30\,\%$ heijastuu suoraan takaisin avaruuteen pilvistä, jäästä ja vaaleista pinnoista. Loppu imeytyy, ja maapallo säteilee saman tehon pois pitkäaaltoisena lämpösäteilynä. Ilman ilmakehää tasapaino asettuisi noin $-18\,{}^\circ\text{C}$:n keskilämpötilaan.

### Kasvihuoneilmiö
Ilmakehän vesihöyry, hiilidioksidi ja metaani päästävät auringonvalon pääosin läpi, vaikka noin viidesosa siitä imeytyy ilmakehään. Ne imevät maanpinnan lähettämää lämpösäteilyä ja säteilevät osan siitä takaisin alas. Maanpinta saa siksi enemmän energiaa kuin pelkästä Auringosta, ja tasapaino asettuu noin $+15\,{}^\circ\text{C}$:een. Tätä sanotaan kasvihuoneilmiöksi, ja se vastaa alun kysymykseen.

<svg data-fig="energy-balance" viewBox="0 0 600 340" role="img" aria-label="Maapallon energiatasapaino, periaatekuva. Auringosta tuleva säteily kulkee ilmakehän läpi maanpintaan; osa siitä heijastuu takaisin avaruuteen. Maanpinta säteilee lämpösäteilyä ylöspäin, ja ilmakehän kasvihuonekaasut säteilevät osan siitä takaisin alas." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-12-energy-balance.webp" x="-2.5" y="-2.5" width="603" height="353" preserveAspectRatio="none"/>
  <foreignObject x="230" y="289.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{maanpinta}$</div></foreignObject>
  <foreignObject x="24" y="231.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ilmakehä}$</div></foreignObject>
  <foreignObject x="122" y="35.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Aurinko}$</div></foreignObject>
  <foreignObject x="302" y="37.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{heijastuu}$</div></foreignObject>
  <foreignObject x="370" y="235.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lämpösäteily}$</div></foreignObject>
  <foreignObject x="427.5" y="63.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{CO}_2$</div></foreignObject>
  <foreignObject x="396" y="177.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{takaisin}$</div></foreignObject>
</svg>

```pysahdy
Kasvihuonekaasut päästävät auringonvalon pääosin läpi. Miksi ne silti nostavat maanpinnan lämpötilaa?
---
Ne imevät maanpinnan lähettämää lämpösäteilyä ja säteilevät osan siitä takaisin alas. Maanpinta saa siksi enemmän energiaa kuin pelkästä Auringosta.
```

### Ilmastonmuutos
Ihmisen toiminta, pääosin fossiilisten polttoaineiden käyttö, on nostanut ilmakehän hiilidioksidipitoisuuden noin 280 miljoonasosasta yli 420 miljoonasosaan. Kun kasvihuonekaasuja lisätään, avaruuteen pääsee hetkellisesti vähemmän energiaa kuin Auringosta tulee. Ero on nykyään noin $1\,\text{W}$ jokaista maapallon neliömetriä kohti. Ylimääräinen energia lämmittää valtameriä, maata ja ilmaa, kunnes uusi tasapaino asettuu korkeampaan lämpötilaan. Tätä sanotaan ilmastonmuutokseksi. Pieneltä näyttävä tehoero on koko maapallon alalla valtava, ja suurin osa siitä varastoituu meriin, joiden suuri lämpökapasiteetti hidastaa lämpenemistä mutta myös pitää sen käynnissä pitkään. Energiaratkaisut, kuten eristäminen, lämpöpumput ja päästöttömät voimalaitokset, ovat siksi myös eettisiä valintoja, jotka vaikuttavat tuleviin sukupolviin.

## Kaava: Lämpöteho ja U-arvo
Rakennusosan läpi siirtyvä lämpöteho on
```latex
P = U A \Delta T
```
missä $P$ on lämpöteho (W), $U$ rakennusosan U-arvo (W/(m²·K)), $A$ pinta-ala (m²) ja $\Delta T$ sisä- ja ulkolämpötilan erotus (K). Kaava pätee, kun lämpötilat rakennusosan molemmilla puolilla pysyvät vakioina. Energiatasapainossa kappaleeseen tuleva ja siitä lähtevä teho ovat yhtä suuret, ja lämpötila pysyy vakiona.

<svg data-fig="wall-temperature" viewBox="0 0 600 300" role="img" aria-label="Seinän poikkileikkaus ja lämpötilan kulku, periaatekuva. Seinässä on ohut sisälevy, paksu eristekerros ja ohut ulkoverhous. Lämpötila laskee sisältä 21 asteesta ulos miinus 15 asteeseen eli 36 kelviniä, ja suurin osa laskusta tapahtuu eristeessä. Lämpöteho P kulkee seinän läpi sisältä ulos." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-12-wall-temperature.webp" x="0" y="3.8" width="600" height="296.2" preserveAspectRatio="none"/>
  <foreignObject x="294.5" y="85.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{eriste}$</div></foreignObject>
  <foreignObject x="101" y="25.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$21\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="82.5" y="85.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sisällä}$</div></foreignObject>
  <foreignObject x="465" y="181.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-15\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="458.5" y="135.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ulkona}$</div></foreignObject>
  <foreignObject x="36" y="128.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Delta T = 36\,\text{K}$</div></foreignObject>
  <foreignObject x="484" y="257.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$P$</div></foreignObject>
</svg>


## Esimerkki
Omakotitalon seinien pinta-ala on $120\,\text{m}^2$ ja U-arvo $0{,}17\,\text{W/(m}^2\text{}\cdot\text{K)}$, ja ikkunoiden pinta-ala on $20{,}0\,\text{m}^2$ ja U-arvo $1{,}0\,\text{W/(m}^2\text{}\cdot\text{K)}$. Sisällä on $21\,{}^\circ\text{C}$ ja ulkona $-15\,{}^\circ\text{C}$. Kuinka suuri lämpöteho johtuu seinien ja ikkunoiden läpi, ja kuinka paljon energiaa se siirtää vuorokaudessa?

<!-- vaihe -->

**Tunnetut ja kysytty.** Seinät: $A_\text{s} = 120\,\text{m}^2$, $U_\text{s} = 0{,}17\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$. Ikkunat: $A_\text{i} = 20{,}0\,\text{m}^2$, $U_\text{i} = 1{,}0\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$. Lämpötilat $T_\text{sisä} = 21\,{}^\circ\text{C}$ ja $T_\text{ulko} = -15\,{}^\circ\text{C}$.

Kysytään lämpötehoa $P$ ja energiaa $E$ vuorokaudessa.

<!-- vaihe -->

**Periaate.** Lämpö johtuu rakenteen läpi lämpimästä kylmään, ja kun lämpötilat pysyvät vakioina, teho on verrannollinen pinta-alaan ja lämpötilaeroon: $P = UA\Delta T$. Seinät ja ikkunat johtavat lämpöä rinnakkain, joten niiden tehot lasketaan yhteen. Teho on vakio, joten energia on teho kerrottuna ajalla.

<!-- vaihe -->

**Kaava ratkaistuna.** Ratkaistaan ensin teho ja sitten energia:
```latex
\begin{aligned}
&P = (U_\text{s} A_\text{s} \\
&\quad + U_\text{i} A_\text{i})\,\Delta T \\[6pt]
&E = Pt
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Lämpötilaero on sama kelvineinä ja celsiusasteina: $\Delta T = 21\,{}^\circ\text{C} - (-15\,{}^\circ\text{C}) = 36\,\text{K}$. Aika on $t = 24\,\text{h}$, ja teho muutetaan kilowateiksi, jotta energia tulee kilowattitunteina.

<!-- vaihe -->

**Sijoitus.** Lasketaan teho ja sen jälkeen energia:
```latex
\begin{aligned}
&P = (0{,}17 \cdot 120 \\
&\quad + 1{,}0 \cdot 20{,}0)\,\tfrac{\text{W}}{\text{K}} \cdot 36\,\text{K} \\
&= (20{,}4 + 20{,}0)\,\tfrac{\text{W}}{\text{K}} \cdot 36\,\text{K} \\
&= 1454{,}4\,\text{W} \\
&E = 1{,}4544\,\text{kW} \cdot 24\,\text{h} \\
&= 34{,}9\,\text{kWh}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Seinien ja ikkunoiden läpi johtuu teho $P \approx 1{,}5\,\text{kW}$, ja vuorokaudessa se siirtää energian $E \approx 35\,\text{kWh}$. Tulos annetaan kahdella merkitsevällä numerolla. Rajoittavat tiedot ovat U-arvot $0{,}17$ ja $1{,}0$ sekä lämpötilaero $36\,\text{K}$ (kokonaisasteiden erotus), kaikki kaksi numeroa; pinta-alat $120\,\text{m}^2$ ja $20{,}0\,\text{m}^2$ ovat tarkempia.

<!-- vaihe -->

**Järkevyys.** Ikkunoiden ala on vain kuudesosa seinien alasta, mutta niiden läpi menee yhtä paljon lämpöä ($20{,}0\,\text{W/K}$ ja $20{,}4\,\text{W/K}$), koska niiden U-arvo on lähes kuusinkertainen. Pyöristetyillä luvuilla $40\,\text{W/K} \cdot 36\,\text{K} \approx 1{,}4\,\text{kW}$ ja $1{,}4\,\text{kW} \cdot 24\,\text{h} \approx 34\,\text{kWh}$. Talon lämmitys korvaa tämän tehon, ja katto, lattia ja ilmanvaihto lisäävät tarvetta vielä.

## Yleinen virhekäsitys
Moni sekoittaa kasvihuoneilmiön ja otsonikadon, vaikka ne ovat eri asioita: otsonikato päästää läpi enemmän ultraviolettisäteilyä, mutta ei juuri lämmitä maapalloa. Toinen virhe on ajatella, että kasvihuoneilmiö on kokonaan haitallinen. Luonnollinen kasvihuoneilmiö pitää Maan elinkelpoisena, ja ongelma on sen voimistuminen ihmisen päästöjen vuoksi. Kolmas virhe on luulla, että villapaita tuottaa lämpöä. Se vain hidastaa lämmön johtumista ja konvektiota kehosta, samoin kuin seinän eriste hidastaa lämmön karkaamista talosta.

## Tiivistelmä
- Lämpö siirtyy johtumalla, konvektiolla ja lämpösäteilynä, ja lämpötilaeron vuoksi energiaa siirtyy nettomääräisesti lämpimämmästä kylmempään. Lämpösäteilyä lähettävät kaikki kappaleet, myös kylmempi.
- Rakennusosan läpi siirtyvä lämpöteho on $P = UA\Delta T$. Pieni U-arvo tarkoittaa hyvää lämmöneristystä.
- Energiatasapainossa tuleva ja lähtevä teho ovat yhtä suuret, ja lämpötila pysyy vakiona.
- Kasvihuonekaasut imevät maanpinnan lämpösäteilyä ja säteilevät osan takaisin, mikä nostaa maanpinnan tasapainolämpötilan noin $-18\,{}^\circ\text{C}$:sta noin $+15\,{}^\circ\text{C}$:een.
- Kasvihuonekaasujen lisääntyminen rikkoo tasapainon hetkellisesti, ja maapallo lämpenee, kunnes uusi tasapaino asettuu korkeampaan lämpötilaan.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: omakotitalo talviyönä. Lämpöä karkaa ulos ikkunoiden ja katon kautta, mitä kuvaavat oranssit nuolet. Maassa on lunta." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-12-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
