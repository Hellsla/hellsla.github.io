# Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos

> **Miksi** maapallon keskilämpötila on noin $+15\,{}^\circ\text{C}$ eikä pakkasen puolella? Maapallo säteilee avaruuteen yhtä paljon energiaa kuin imee Auringosta.

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: Maa nähtynä avaruudesta. Maan ympärillä on ohut ilmakehä. Kuvan vasemmassa reunassa paistaa Aurinko. Mustalla taivaalla tuikkii tähtiä." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-12-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Lämpötilaero saa energiaa siirtymään itsestään. Kun siirrot lasketaan yhteen, energiaa siirtyy lämpimämmästä kappaleesta kylmempään. Näin siirtyvää energiaa sanotaan lämmöksi. Lämpö siirtyy kolmella tavalla.

Ensimmäinen tapa on johtuminen. Siinä energia siirtyy aineen läpi hiukkasesta toiseen. Nopeammin värähtelevät hiukkaset tönivät hitaampia naapureitaan. Metallit johtavat lämpöä hyvin. Niissä energiaa kuljettavat myös vapaat elektronit, ja pääosin juuri ne. Ilma ja villa johtavat lämpöä huonosti.

Toinen tapa on konvektio. Siinä lämmin neste tai kaasu virtaa ja kuljettaa energiaa mukanaan. Esimerkiksi lämmin ilma nousee patterin yläpuolella. Se on laajentunut, ja siksi se on kevyempää kuin ympäröivä ilma.

Kolmas tapa on lämpösäteily. Siinä kappale lähettää sähkömagneettista säteilyä. Säteily ei tarvitse väliainetta eli ainetta, jonka läpi se kulkisi. Näin Auringon energia tulee Maahan tyhjän avaruuden läpi. Näin myös takan hehku lämmittää kasvoja. Kaikki kappaleet säteilevät. Mitä kuumempi kappale on, sitä enemmän se säteilee. Se lähettää silloin myös lyhytaaltoisempaa säteilyä. Lämpösäteilyä lähtee molemmista kappaleista. Myös kylmempi kappale säteilee lämpimämpää kohti. Lämpimämpi kappale säteilee kuitenkin enemmän. Siksi kun siirrot lasketaan yhteen, energiaa siirtyy kylmempään kappaleeseen.

<svg data-fig="heat-transfer" viewBox="0 0 600 300" role="img" aria-label="Kolme lämmön siirtymistapaa, periaatekuva. Johtuminen: lämpö kulkee metallitangon läpi kuumasta päästä kylmään päähän. Konvektio: lämmin vesi nousee kattilassa keskellä. Jäähtynyt vesi vajoaa reunoilla. Vesi siis kiertää. Säteily: kuuma kappale lähettää säteilyä. Säteily kulkee tyhjän tilan läpi." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-12-heat-transfer.webp" x="6.2" y="7.4" width="594.1" height="308.2" preserveAspectRatio="none"/>
  <foreignObject x="14" y="177.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kuuma}$</div></foreignObject>
  <foreignObject x="116" y="177.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{kylmä}$</div></foreignObject>
  <foreignObject x="33.5" y="247.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{johtuminen}$</div></foreignObject>
  <foreignObject x="240" y="247.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{konvektio}$</div></foreignObject>
  <foreignObject x="452.5" y="247.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{säteily}$</div></foreignObject>
</svg>

```pysahdy
Auringon energia tulee Maahan tyhjän avaruuden läpi. Mikä lämmönsiirtotapa se on? Miksi se ei ole johtumista eikä konvektiota?
---
Se on lämpösäteilyä. Säteily ei tarvitse väliainetta. Johtuminen ja konvektio tarvitsevat ainetta, jonka läpi energia siirtyy.
```

### Rakennuksen lämpöhäviöt
Talon lämmitysenergiasta suuri osa kuluu siihen, että lämpö johtuu ulos. Lämpö johtuu seinien, katon, ikkunoiden ja lattian läpi. Rakennusosan lämmöneristävyyttä kuvaa U-arvo eli lämmönläpäisykerroin. U-arvo kertoo, kuinka monta wattia lämpötehoa siirtyy yhden neliömetrin läpi. Tämä pätee, kun sisä- ja ulkolämpötilan ero on yksi kelvin. Mitä pienempi U-arvo on, sitä paremmin rakenne eristää. Nykyaikaisen seinän U-arvo on noin $0{,}17\,\text{W/(m}^2\text{}\cdot\text{K)}$. Hyvänkin ikkunan U-arvo on noin $1{,}0\,\text{W/(m}^2\text{}\cdot\text{K)}$. Siksi pieni ikkuna päästää läpi yhtä paljon lämpöä kuin moninkertainen ala seinää. Hyvä eristys säästää energiaa ja vähentää lämmityksen päästöjä.

```pysahdy
Seinän U-arvo on $0{,}17\,\text{W/(m}^2\text{}\cdot\text{K)}$. Ikkunan U-arvo on $1{,}0\,\text{W/(m}^2\text{}\cdot\text{K)}$. Kumpi eristää paremmin? Miksi?
---
Seinä eristää paremmin, koska sen U-arvo on pienempi. Sen läpi siirtyy vähemmän lämpötehoa samalla pinta-alalla ja lämpötilaerolla.
```

### Energiatasapaino
Kappaleen lämpötila pysyy vakiona, kun siihen tulee yhtä suuri teho kuin siitä lähtee. Tätä sanotaan energiatasapainoksi. Maapallo saa energiaa Auringon säteilynä. Noin $30\,\%$ siitä heijastuu suoraan takaisin avaruuteen. Heijastajia ovat pilvet, jää ja vaaleat pinnat. Loppu säteilystä imeytyy. Maapallo säteilee saman tehon pois pitkäaaltoisena lämpösäteilynä. Ilman ilmakehää tasapaino asettuisi noin $-18\,{}^\circ\text{C}$:n keskilämpötilaan.

### Kasvihuoneilmiö
Ilmakehässä on vesihöyryä, hiilidioksidia ja metaania. Ne päästävät auringonvalon pääosin läpi. Noin viidesosa valosta kuitenkin imeytyy ilmakehään. Samat kaasut imevät maanpinnan lähettämää lämpösäteilyä. Ne säteilevät osan siitä takaisin alas. Maanpinta saa siksi enemmän energiaa kuin pelkästä Auringosta. Tasapaino asettuu noin $+15\,{}^\circ\text{C}$:een. Tätä sanotaan kasvihuoneilmiöksi. Se vastaa alun kysymykseen.

<svg data-fig="energy-balance" viewBox="0 0 600 340" role="img" aria-label="Maapallon energiatasapaino, periaatekuva. Auringosta tuleva säteily kulkee ilmakehän läpi maanpintaan. Osa säteilystä heijastuu takaisin avaruuteen. Maanpinta säteilee lämpösäteilyä ylöspäin. Ilmakehän kasvihuonekaasut säteilevät osan siitä takaisin alas." style="max-width:100%;font-size:24px">
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
Ne imevät maanpinnan lähettämää lämpösäteilyä. Ne säteilevät osan siitä takaisin alas. Maanpinta saa siksi enemmän energiaa kuin pelkästä Auringosta.
```

### Ilmastonmuutos
Ihmisen toiminta on nostanut ilmakehän hiilidioksidipitoisuutta. Pääosin syy on fossiilisten polttoaineiden käyttö. Aiemmin pitoisuus oli noin 280 miljoonasosaa. Nyt se on yli 420 miljoonasosaa. Kun kasvihuonekaasuja lisätään, avaruuteen pääsee hetkellisesti vähemmän energiaa kuin Auringosta tulee. Ero on nykyään noin $1\,\text{W}$ jokaista maapallon neliömetriä kohti. Ylimääräinen energia lämmittää valtameriä, maata ja ilmaa. Lämpeneminen jatkuu, kunnes uusi tasapaino asettuu korkeampaan lämpötilaan. Tätä sanotaan ilmastonmuutokseksi.

Tehoero näyttää pieneltä. Koko maapallon alalla se on kuitenkin valtava. Suurin osa energiasta varastoituu meriin. Merien lämpökapasiteetti on suuri. Siksi lämpeneminen on hidasta, mutta se myös jatkuu pitkään. Energiaratkaisut ovat siksi myös eettisiä valintoja, jotka vaikuttavat tuleviin sukupolviin. Tällaisia ratkaisuja ovat eristäminen, lämpöpumput ja päästöttömät voimalaitokset.

## Kaava: Lämpöteho ja U-arvo
Rakennusosan läpi siirtyvä lämpöteho on
```latex
P = U A \Delta T
```
Tässä $P$ on lämpöteho (W). Suure $U$ on rakennusosan U-arvo (W/(m²·K)). Suure $A$ on pinta-ala (m²). Suure $\Delta T$ on sisä- ja ulkolämpötilan erotus (K). Kaava pätee, kun lämpötilat rakennusosan molemmilla puolilla pysyvät vakioina. Energiatasapainossa kappaleeseen tuleva ja siitä lähtevä teho ovat yhtä suuret. Silloin lämpötila pysyy vakiona.

<svg data-fig="wall-temperature" viewBox="0 0 600 300" role="img" aria-label="Seinän poikkileikkaus ja lämpötilan kulku, periaatekuva. Seinässä on ohut sisälevy, paksu eristekerros ja ohut ulkoverhous. Lämpötila laskee sisällä olevasta 21 asteesta ulkona olevaan miinus 15 asteeseen. Lasku on 36 kelviniä. Suurin osa laskusta tapahtuu eristeessä. Lämpöteho P kulkee seinän läpi sisältä ulos." style="max-width:100%;font-size:24px">
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
Omakotitalon seinien pinta-ala on $120\,\text{m}^2$ ja U-arvo $0{,}17\,\text{W/(m}^2\text{}\cdot\text{K)}$. Ikkunoiden pinta-ala on $20{,}0\,\text{m}^2$ ja U-arvo $1{,}0\,\text{W/(m}^2\text{}\cdot\text{K)}$. Sisällä on $21\,{}^\circ\text{C}$ ja ulkona $-15\,{}^\circ\text{C}$. Kuinka suuri lämpöteho johtuu seinien ja ikkunoiden läpi? Kuinka paljon energiaa se siirtää vuorokaudessa?

<!-- vaihe -->

**Tunnetut ja kysytty.** Seinät: $A_\text{s} = 120\,\text{m}^2$, $U_\text{s} = 0{,}17\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$. Ikkunat: $A_\text{i} = 20{,}0\,\text{m}^2$, $U_\text{i} = 1{,}0\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$. Lämpötilat ovat $T_\text{sisä} = 21\,{}^\circ\text{C}$ ja $T_\text{ulko} = -15\,{}^\circ\text{C}$.

Kysytään lämpötehoa $P$ ja energiaa $E$ vuorokaudessa.

<!-- vaihe -->

**Periaate.** Lämpö johtuu rakenteen läpi lämpimästä kylmään. Kun lämpötilat pysyvät vakioina, teho on verrannollinen pinta-alaan ja lämpötilaeroon: $P = UA\Delta T$. Seinät ja ikkunat johtavat lämpöä rinnakkain. Siksi niiden tehot lasketaan yhteen. Teho on vakio, joten energia on teho kerrottuna ajalla.

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

**Yksikkömuunnokset.** Lämpötilaero on sama kelvineinä ja celsiusasteina: $\Delta T = 21\,{}^\circ\text{C} - (-15\,{}^\circ\text{C}) = 36\,\text{K}$. Aika on $t = 24\,\text{h}$. Teho muutetaan kilowateiksi, jotta energia tulee kilowattitunteina.

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

**Tulos.** Seinien ja ikkunoiden läpi johtuu teho $P \approx 1{,}5\,\text{kW}$. Vuorokaudessa se siirtää energian $E \approx 35\,\text{kWh}$. Tulos annetaan kahdella merkitsevällä numerolla. Rajoittavat tiedot ovat U-arvot $0{,}17$ ja $1{,}0$ sekä lämpötilaero $36\,\text{K}$ (kokonaisasteiden erotus). Kaikissa niissä on kaksi numeroa. Pinta-alat $120\,\text{m}^2$ ja $20{,}0\,\text{m}^2$ ovat tarkempia.

<!-- vaihe -->

**Järkevyys.** Ikkunoiden ala on vain kuudesosa seinien alasta. Silti niiden läpi menee yhtä paljon lämpöä ($20{,}0\,\text{W/K}$ ja $20{,}4\,\text{W/K}$). Syy on se, että ikkunoiden U-arvo on lähes kuusinkertainen. Pyöristetyillä luvuilla $40\,\text{W/K} \cdot 36\,\text{K} \approx 1{,}4\,\text{kW}$ ja $1{,}4\,\text{kW} \cdot 24\,\text{h} \approx 34\,\text{kWh}$. Talon lämmitys korvaa tämän tehon. Katto, lattia ja ilmanvaihto lisäävät lämmöntarvetta vielä.

## Yleinen virhekäsitys
Moni sekoittaa kasvihuoneilmiön ja otsonikadon. Ne ovat eri asioita. Otsonikato päästää läpi enemmän ultraviolettisäteilyä, mutta se ei juuri lämmitä maapalloa.

Toinen virhe on ajatella, että kasvihuoneilmiö on kokonaan haitallinen. Luonnollinen kasvihuoneilmiö pitää Maan elinkelpoisena. Ongelma on sen voimistuminen ihmisen päästöjen vuoksi.

Kolmas virhe on luulla, että villapaita tuottaa lämpöä. Se vain hidastaa lämmön johtumista ja konvektiota kehosta pois. Samoin seinän eriste hidastaa lämmön karkaamista talosta.

## Tiivistelmä
- Lämpö siirtyy johtumalla, konvektiolla ja lämpösäteilynä. Lämpötilaeron vuoksi energiaa siirtyy lämpimämmästä kappaleesta kylmempään. Kaikki kappaleet lähettävät lämpösäteilyä, myös kylmempi.
- Rakennusosan läpi siirtyvä lämpöteho on $P = UA\Delta T$. Pieni U-arvo tarkoittaa hyvää lämmöneristystä.
- Energiatasapainossa tuleva ja lähtevä teho ovat yhtä suuret. Silloin lämpötila pysyy vakiona.
- Kasvihuonekaasut imevät maanpinnan lämpösäteilyä ja säteilevät osan takaisin. Siksi maanpinnan tasapainolämpötila nousee noin $-18\,{}^\circ\text{C}$:sta noin $+15\,{}^\circ\text{C}$:een.
- Kasvihuonekaasujen lisääntyminen rikkoo tasapainon hetkellisesti. Maapallo lämpenee, kunnes uusi tasapaino asettuu korkeampaan lämpötilaan.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: omakotitalo talviyönä. Lämpöä karkaa ulos ikkunoiden ja katon kautta. Oranssit nuolet näyttävät sen. Maassa on lunta." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-12-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
