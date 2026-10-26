# Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos

> **Miksi** maapallon keskilämpötila on noin +15 °C eikä pakkasen puolella, vaikka maapallo säteilee avaruuteen yhtä paljon energiaa kuin saa Auringosta?

## Ydinajatus
Lämpö siirtyy aina itsestään lämpimämmästä kylmempään kolmella tavalla. Johtumisessa energia siirtyy aineen läpi hiukkasesta toiseen, kun nopeammin värähtelevät hiukkaset tönivät hitaampia naapureitaan. Metallit johtavat lämpöä hyvin, ilma ja villa huonosti. Konvektiossa lämmin neste tai kaasu virtaa ja kuljettaa energiaa mukanaan: lämmin ilma nousee patterin yläpuolella, koska se on laajentunut ja kevyempää kuin ympäröivä ilma. Lämpösäteilyssä kappale lähettää sähkömagneettista säteilyä, joka ei tarvitse väliainetta. Näin Auringon energia tulee Maahan tyhjän avaruuden läpi, ja näin takan hehku lämmittää kasvoja. Kaikki kappaleet säteilevät, ja mitä kuumempi kappale on, sitä enemmän ja sitä lyhytaaltoisempaa säteilyä se lähettää.

<svg data-fig="heat-transfer" viewBox="0 0 600 300" role="img" aria-label="Kolme lämmön siirtymistapaa, periaatekuva. Johtuminen: lämpö kulkee metallitangon läpi kuumasta päästä kylmään. Konvektio: lämmin vesi nousee kattilassa keskellä ja jäähtynyt vajoaa reunoilla, joten vesi kiertää. Säteily: kuuma kappale lähettää säteilyä, joka kulkee tyhjän tilan läpi." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy312-rod" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c92a2a"/><stop offset="0.35" stop-color="#f2a69c"/><stop offset="0.7" stop-color="#c4ccd4"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient><linearGradient id="fy312-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><radialGradient id="fy312-hot" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></radialGradient></defs>
  <line x1="200" y1="20" x2="200" y2="284" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="400" y1="20" x2="400" y2="284" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <rect x="14" y="130" width="172" height="36" rx="3" fill="url(#fy312-rod)" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M30,103 L146,103 L146,111 L170,96 L146,81 L146,89 L30,89 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="14" y="177.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kuuma}$</div></foreignObject>
  <foreignObject x="116" y="177.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{kylmä}$</div></foreignObject>
  <foreignObject x="33.5" y="247.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{johtuminen}$</div></foreignObject>
  <path d="M238,84 V206 Q238,222 254,222 H346 Q362,222 362,206 V84" fill="url(#fy312-water)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="236" y="84" width="128" height="3" fill="#a9d1f0"/>
  <rect x="246" y="230" width="108" height="12" rx="3" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <path d="M310,206 V138 Q310,114 311,114" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round"/>
  <path d="M311,114 Q344,114 344,138 V186" fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"/>
  <path d="M310,150 L303,164 L317,164 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M344,196 L337,182 L351,182 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M290,206 V138 Q290,114 289,114" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round"/>
  <path d="M289,114 Q256,114 256,138 V186" fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"/>
  <path d="M290,150 L283,164 L297,164 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M256,196 L249,182 L263,182 Z" fill="#ffffff" stroke-linejoin="round"/>
  <foreignObject x="240" y="247.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{konvektio}$</div></foreignObject>
  <circle cx="448" cy="150" r="30" fill="url(#fy312-hot)" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M494,104 q10,-9 20,0 t20,0 t20,0" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round"/>
  <path d="M572,104 L558,97 L558,111 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M494,150 q10,-9 20,0 t20,0 t20,0" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round"/>
  <path d="M572,150 L558,143 L558,157 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M494,196 q10,-9 20,0 t20,0 t20,0" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round"/>
  <path d="M572,196 L558,189 L558,203 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="452.5" y="247.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{säteily}$</div></foreignObject>
</svg>

Talon lämmitysenergiasta suuri osa kuluu siihen, että lämpö johtuu seinien, katon, ikkunoiden ja lattian läpi ulos. Rakennusosan lämmöneristävyyttä kuvaa U-arvo eli lämmönläpäisykerroin, joka kertoo, kuinka monta wattia lämpötehoa siirtyy yhden neliömetrin läpi, kun sisä- ja ulkolämpötilan ero on yksi kelvin. Mitä pienempi U-arvo, sitä paremmin rakenne eristää. Nykyaikaisen seinän U-arvo on noin 0,17 W/(m²·K), mutta hyvänkin ikkunan noin 1,0 W/(m²·K), joten pieni ikkuna päästää läpi yhtä paljon lämpöä kuin moninkertainen ala seinää. Hyvä eristys säästää energiaa ja vähentää lämmityksen päästöjä.

Kappaleen lämpötila pysyy vakiona, kun siihen tulee yhtä suuri teho kuin siitä lähtee. Tätä sanotaan energiatasapainoksi. Maapallo saa energiaa Auringon säteilynä, josta noin 30 % heijastuu suoraan takaisin avaruuteen pilvistä, jäästä ja vaaleista pinnoista. Loppu imeytyy, ja maapallo säteilee saman tehon pois pitkäaaltoisena lämpösäteilynä. Ilman ilmakehää tasapaino asettuisi noin −18 °C:n keskilämpötilaan.

Ilmakehän vesihöyry, hiilidioksidi ja metaani päästävät auringonvalon pääosin läpi, vaikka noin viidesosa siitä imeytyy ilmakehään. Ne imevät maanpinnan lähettämää lämpösäteilyä ja säteilevät osan siitä takaisin alas. Maanpinta saa siksi enemmän energiaa kuin pelkästä Auringosta, ja tasapaino asettuu noin +15 °C:een. Tätä sanotaan kasvihuoneilmiöksi, ja se vastaa alun kysymykseen.

<svg data-fig="energy-balance" viewBox="0 0 600 300" role="img" aria-label="Maapallon energiatasapaino, periaatekuva. Auringosta tuleva säteily kulkee ilmakehän läpi maanpintaan; osa siitä heijastuu takaisin avaruuteen. Maanpinta säteilee lämpösäteilyä ylöspäin, ja ilmakehän kasvihuonekaasut säteilevät osan siitä takaisin alas." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy312-ground" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#f1dfb5"/></linearGradient><linearGradient id="fy312-air" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d0e6fb"/></linearGradient><radialGradient id="fy312-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#ffc078"/></radialGradient></defs>
  <rect x="12" y="116" width="576" height="54" fill="url(#fy312-air)" stroke="#6b7480" stroke-width="2" stroke-dasharray="7 5"/>
  <rect x="12" y="236" width="576" height="52" fill="url(#fy312-ground)" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="240" y="247.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{maanpinta}$</div></foreignObject>
  <foreignObject x="246" y="128.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ilmakehä}$</div></foreignObject>
  <circle cx="50" cy="52" r="26" fill="url(#fy312-sun)" stroke="#e8590c" stroke-width="2.5"/>
  <foreignObject x="88" y="21.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Aurinko}$</div></foreignObject>
  <path d="M66.5,88.5 L117,206.5 L109,210 L132,226 L136.5,198 L128,201.5 L77.5,83.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M180,115 L220,64.5 L227.5,70 L230,44 L205.5,52.5 L212.5,58 L172,109 Z" fill="#ffc078" stroke-linejoin="round"/>
  <foreignObject x="246" y="41.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{heijastuu}$</div></foreignObject>
  <path d="M396,228 L396,58 L405,58 L390,34 L375,58 L384,58 L384,228 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="412" y="55.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lämpösäteily}$</div></foreignObject>
  <path d="M444,176 L444,204 L435,204 L450,226 L465,204 L456,204 L456,176 Z" fill="#f2a69c" stroke-linejoin="round"/>
  <foreignObject x="472" y="186.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{takaisin}$</div></foreignObject>
</svg>

Fossiilisten polttoaineiden käyttö on nostanut ilmakehän hiilidioksidipitoisuuden noin 280 miljoonasosasta yli 420 miljoonasosaan. Kun kasvihuonekaasuja lisätään, avaruuteen pääsee hetkellisesti vähemmän energiaa kuin Auringosta tulee. Ero on nykyään noin 1 W jokaista maapallon neliömetriä kohti. Ylimääräinen energia lämmittää valtameriä, maata ja ilmaa, kunnes uusi tasapaino asettuu korkeampaan lämpötilaan. Tätä sanotaan ilmastonmuutokseksi. Pieneltä näyttävä tehoero on koko maapallon alalla valtava, ja suurin osa siitä varastoituu meriin, joiden suuri lämpökapasiteetti hidastaa lämpenemistä mutta myös pitää sen käynnissä pitkään. Energiaratkaisut, kuten eristäminen, lämpöpumput ja päästöttömät voimalaitokset, ovat siksi myös eettisiä valintoja, jotka vaikuttavat tuleviin sukupolviin.

## Kaava: Lämpöteho ja U-arvo
Rakennusosan läpi johtuva lämpöteho on
```latex
P = U A \Delta T
```
missä $P$ on lämpöteho (W), $U$ rakennusosan U-arvo (W/(m²·K)), $A$ pinta-ala (m²) ja $\Delta T$ sisä- ja ulkolämpötilan erotus (K). Kaava pätee, kun lämpötilat rakennusosan molemmilla puolilla pysyvät vakioina. Energiatasapainossa kappaleeseen tuleva ja siitä lähtevä teho ovat yhtä suuret, ja lämpötila pysyy vakiona.

<svg data-fig="wall-temperature" viewBox="0 0 600 300" role="img" aria-label="Seinän poikkileikkaus ja lämpötilan kulku, periaatekuva. Seinässä on ohut sisälevy, paksu eristekerros ja ohut ulkoverhous. Lämpötila laskee sisältä 21 asteesta ulos miinus 15 asteeseen eli 36 kelviniä, ja suurin osa laskusta tapahtuu eristeessä. Lämpöteho P kulkee seinän läpi sisältä ulos." style="max-width:100%;font-size:24px">
  <defs><pattern id="fy312-wool" width="14" height="14" patternUnits="userSpaceOnUse"><path d="M1,4 q4,-5 6,0 t6,0 M1,11 q4,-5 6,0 t6,0" fill="none" stroke="#a97a35" stroke-width="1.5"/></pattern></defs>
  <line x1="40" y1="64" x2="570" y2="64" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="40" y1="222" x2="570" y2="222" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <rect x="220" y="40" width="36" height="200" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="256" y="40" width="124" height="200" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="256" y="40" width="124" height="200" fill="url(#fy312-wool)"/>
  <rect x="380" y="40" width="28" height="200" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="302" y="85" width="68" height="30" rx="4" fill="#ffffff" fill-opacity="0.85"/>
  <foreignObject x="294.5" y="85.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{eriste}$</div></foreignObject>
  <path d="M40,64 H220 L256,72 L380,214 L408,222 H570" fill="none" stroke="#c92a2a" stroke-width="4" stroke-linejoin="round"/>
  <foreignObject x="101" y="25.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$21\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="82.5" y="85.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sisällä}$</div></foreignObject>
  <foreignObject x="465" y="181.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-15\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="458.5" y="135.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ulkona}$</div></foreignObject>
  <path d="M30,64 H24 V222 H30" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="36" y="128.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta T = 36\,\text{K}$</span></div></foreignObject>
  <path d="M120,278 L444,278 L444,288 L470,272 L444,256 L444,266 L120,266 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="484" y="257.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$P$</div></foreignObject>
</svg>


## Esimerkki
Omakotitalon seinien pinta-ala on 120 m² ja U-arvo 0,17 W/(m²·K), ja ikkunoiden pinta-ala on 20 m² ja U-arvo 1,0 W/(m²·K). Sisällä on 21 °C ja ulkona −15 °C. Kuinka suuri lämpöteho johtuu seinien ja ikkunoiden läpi, ja kuinka paljon energiaa se siirtää vuorokaudessa?

<!-- vaihe -->
**Lämpötilaero.** Lämpötilaero on sama kelvineinä ja celsiusasteina:
```latex
\begin{aligned}
\Delta T &= T_\text{sisä} - T_\text{ulko} \\
&= 21\,{}^\circ\text{C} - (-15\,{}^\circ\text{C}) \\
&= 36\,\text{K}
\end{aligned}
```

<!-- vaihe -->
**Kaava ratkaistuna.** Seinät ja ikkunat johtavat lämpöä rinnakkain, joten tehot lasketaan yhteen:
```latex
\begin{aligned}
P &= P_\text{seinä} + P_\text{ikkuna} \\
&= (U_\text{s} A_\text{s} + U_\text{i} A_\text{i})\,\Delta T
\end{aligned}
```

<!-- vaihe -->
**Sijoitus.** Sijoitetaan arvot yksiköineen:
```latex
\begin{aligned}
P_\text{seinä} &= U_\text{s} A_\text{s}\,\Delta T \\
&= 0{,}17\,\tfrac{\text{W}}{\text{m}^2\text{K}} \cdot 120\,\text{m}^2 \cdot 36\,\text{K} \\
&\approx 730\,\text{W} \\
P_\text{ikkuna} &= U_\text{i} A_\text{i}\,\Delta T \\
&= 1{,}0\,\tfrac{\text{W}}{\text{m}^2\text{K}} \cdot 20\,\text{m}^2 \cdot 36\,\text{K} \\
&= 720\,\text{W}
\end{aligned}
```
Yhteensä $P \approx 1450\,\text{W} \approx 1{,}5\,\text{kW}$.

<!-- vaihe -->
**Energia vuorokaudessa.** Energia on teho kertaa aika, $E = Pt$:
```latex
\begin{aligned}
E &= P t \\
&= 1{,}45\,\text{kW} \cdot 24\,\text{h} \\
&\approx 35\,\text{kWh}
\end{aligned}
```

<!-- vaihe -->
**Järkevyys.** Ikkunoiden ala on vain kuudesosa seinien alasta, mutta niiden läpi menee yhtä paljon lämpöä, koska niiden U-arvo on lähes kuusinkertainen. Talon lämmitys korvaa tämän tehon, ja katto, lattia ja ilmanvaihto lisäävät tarvetta vielä.

## Yleinen virhekäsitys
Moni sekoittaa kasvihuoneilmiön ja otsonikadon, vaikka ne ovat eri asioita: otsonikato päästää läpi enemmän ultraviolettisäteilyä, mutta ei juuri lämmitä maapalloa. Toinen virhe on ajatella, että kasvihuoneilmiö on kokonaan haitallinen. Luonnollinen kasvihuoneilmiö pitää Maan elinkelpoisena, ja ongelma on sen voimistuminen ihmisen päästöjen vuoksi. Kolmas virhe on luulla, että villapaita tuottaa lämpöä. Se vain hidastaa lämmön johtumista ja konvektiota kehosta, samoin kuin seinän eriste hidastaa lämmön karkaamista talosta.

## Tiivistelmä
- Lämpö siirtyy johtumalla, konvektiolla ja lämpösäteilynä aina lämpimämmästä kylmempään.
- Rakennusosan läpi johtuva lämpöteho on $P = UA\Delta T$. Pieni U-arvo tarkoittaa hyvää lämmöneristystä.
- Energiatasapainossa tuleva ja lähtevä teho ovat yhtä suuret, ja lämpötila pysyy vakiona.
- Kasvihuonekaasut imevät maanpinnan lämpösäteilyä ja säteilevät osan takaisin, mikä nostaa maanpinnan tasapainolämpötilan noin −18 °C:sta noin +15 °C:een.
- Kasvihuonekaasujen lisääntyminen rikkoo tasapainon hetkellisesti, ja maapallo lämpenee, kunnes uusi tasapaino asettuu korkeampaan lämpötilaan.
