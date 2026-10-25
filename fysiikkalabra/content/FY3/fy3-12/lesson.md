# Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos

> **Miksi** maapallon keskilämpötila on noin +15 °C eikä pakkasen puolella, vaikka maapallo säteilee avaruuteen yhtä paljon energiaa kuin saa Auringosta?

## Ydinajatus
Lämpö siirtyy aina itsestään lämpimämmästä kylmempään kolmella tavalla. Johtumisessa energia siirtyy aineen läpi hiukkasesta toiseen, kun nopeammin värähtelevät hiukkaset tönivät hitaampia naapureitaan. Metallit johtavat lämpöä hyvin, ilma ja villa huonosti. Konvektiossa lämmin neste tai kaasu virtaa ja kuljettaa energiaa mukanaan: lämmin ilma nousee patterin yläpuolella, koska se on laajentunut ja kevyempää kuin ympäröivä ilma. Lämpösäteilyssä kappale lähettää sähkömagneettista säteilyä, joka ei tarvitse väliainetta. Näin Auringon energia tulee Maahan tyhjän avaruuden läpi, ja näin takan hehku lämmittää kasvoja. Kaikki kappaleet säteilevät, ja mitä kuumempi kappale on, sitä enemmän ja sitä lyhytaaltoisempaa säteilyä se lähettää.

Talon lämmitysenergiasta suuri osa kuluu siihen, että lämpö johtuu seinien, katon, ikkunoiden ja lattian läpi ulos. Rakennusosan lämmöneristävyyttä kuvaa U-arvo eli lämmönläpäisykerroin, joka kertoo, kuinka monta wattia lämpötehoa siirtyy yhden neliömetrin läpi, kun sisä- ja ulkolämpötilan ero on yksi kelvin. Mitä pienempi U-arvo, sitä paremmin rakenne eristää. Nykyaikaisen seinän U-arvo on noin 0,17 W/(m²·K), mutta hyvänkin ikkunan noin 1,0 W/(m²·K), joten pieni ikkuna päästää läpi yhtä paljon lämpöä kuin moninkertainen ala seinää. Hyvä eristys säästää energiaa ja vähentää lämmityksen päästöjä.

Kappaleen lämpötila pysyy vakiona, kun siihen tulee yhtä suuri teho kuin siitä lähtee. Tätä sanotaan energiatasapainoksi. Maapallo saa energiaa Auringon säteilynä, josta noin 30 % heijastuu suoraan takaisin avaruuteen pilvistä, jäästä ja vaaleista pinnoista. Loput imeytyy, ja maapallo säteilee saman tehon pois pitkäaaltoisena lämpösäteilynä. Ilman ilmakehää tasapaino asettuisi noin −18 °C:n keskilämpötilaan. Ilmakehän vesihöyry, hiilidioksidi ja metaani kuitenkin päästävät auringonvalon lähes esteettä läpi mutta imevät maanpinnan lähettämää lämpösäteilyä ja säteilevät osan siitä takaisin alas. Maanpinta saa siksi enemmän energiaa kuin pelkästä Auringosta, ja tasapaino asettuu noin +15 °C:een. Tätä sanotaan kasvihuoneilmiöksi, ja se vastaa alun kysymykseen.

Fossiilisten polttoaineiden käyttö on nostanut ilmakehän hiilidioksidipitoisuuden noin 280 miljoonasosasta yli 420 miljoonasosaan. Kun kasvihuonekaasuja lisätään, avaruuteen pääsee hetkellisesti vähemmän energiaa kuin Auringosta tulee. Ero on nykyään noin 1 W jokaista maapallon neliömetriä kohti. Ylimääräinen energia lämmittää valtameriä, maata ja ilmaa, kunnes uusi tasapaino asettuu korkeampaan lämpötilaan. Tätä on ilmastonmuutos. Pieneltä näyttävä tehoero on koko maapallon alalla valtava, ja suurin osa siitä varastoituu meriin, joiden suuri lämpökapasiteetti hidastaa lämpenemistä mutta myös pitää sen käynnissä pitkään. Energiaratkaisut, kuten eristäminen, lämpöpumput ja päästöttömät voimalaitokset, ovat siksi myös eettisiä valintoja, jotka vaikuttavat tuleviin sukupolviin.

## Kaava
Rakennusosan läpi johtuva lämpöteho on
```latex
P = U A \Delta T
```
missä P on lämpöteho (W), U rakennusosan U-arvo (W/(m²·K)), A pinta-ala (m²) ja ΔT sisä- ja ulkolämpötilan erotus (K). Energiatasapainossa kappaleeseen tuleva ja siitä lähtevä teho ovat yhtä suuret, ja lämpötila pysyy vakiona.

<svg viewBox="0 0 600 300" role="img" aria-label="Maapallon energiatasapaino: Auringosta tuleva säteily, josta osa heijastuu takaisin ja osa imeytyy maanpintaan. Maanpinta säteilee lämpösäteilyä ylöspäin, ja ilmakehän kasvihuonekaasut säteilevät osan siitä takaisin alas." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <rect x="20" y="230" width="560" height="50" fill="currentColor" fill-opacity="0.25"/>
  <rect x="20" y="110" width="560" height="50" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-dasharray="6 5"/>
  <text x="300" y="268" text-anchor="middle" fill="currentColor">maanpinta</text>
  <text x="560" y="142" text-anchor="end" fill="currentColor">ilmakehä</text>
  <line x1="90" y1="20" x2="150" y2="222" stroke="currentColor" stroke-width="5"/>
  <polygon points="152,230 140,210 158,208" fill="currentColor"/>
  <text x="40" y="50" fill="currentColor">Aurinko</text>
  <line x1="190" y1="104" x2="230" y2="28" stroke="currentColor" stroke-width="3"/>
  <polygon points="234,20 220,34 236,38" fill="currentColor"/>
  <text x="240" y="44" fill="currentColor">heijastuu</text>
  <line x1="400" y1="226" x2="400" y2="40" stroke="currentColor" stroke-width="5" stroke-dasharray="10 6"/>
  <polygon points="400,28 390,48 410,48" fill="currentColor"/>
  <text x="414" y="60" fill="currentColor">lämpösäteily</text>
  <line x1="470" y1="164" x2="470" y2="218" stroke="currentColor" stroke-width="4" stroke-dasharray="10 6"/>
  <polygon points="470,228 460,208 480,208" fill="currentColor"/>
  <text x="484" y="206" fill="currentColor">takaisin</text>
</svg>

## Esimerkki
Omakotitalon seinien pinta-ala on 120 m² ja U-arvo 0,17 W/(m²·K), ja ikkunoiden pinta-ala on 20 m² ja U-arvo 1,0 W/(m²·K). Sisällä on 21 °C ja ulkona −15 °C. Kuinka suuri lämpöteho johtuu seinien ja ikkunoiden läpi, ja kuinka paljon energiaa se on vuorokaudessa?

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
P_\text{seinä} &= 0{,}17\,\tfrac{\text{W}}{\text{m}^2\text{K}} \cdot 120\,\text{m}^2 \cdot 36\,\text{K} \\
&\approx 730\,\text{W} \\
P_\text{ikkuna} &= 1{,}0\,\tfrac{\text{W}}{\text{m}^2\text{K}} \cdot 20\,\text{m}^2 \cdot 36\,\text{K} \\
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
