# Tasainen liike – nopeus, paikka ja kuvaajat

> **Miksi** Voyager 2 -luotaimen paikan voi laskea etukäteen mille tahansa päivälle, vaikka se on yli 20 miljardin kilometrin päässä Auringosta?

<svg data-fig="hero" data-style="house" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: vasemmalla on Aurinko ja planeettojen radat. Oikealla kaukana avaruudessa on Voyager 2 -luotain. Luotaimen takana on suora jälki. Jäljellä on merkkejä luotaimen aiemmista paikoista. Merkit ovat yhtä kaukana toisistaan, ja niiden välillä on kulunut yhtä pitkä aika. Tulevat paikat jatkuvat eteenpäin katkoviivana." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy1/fy1-5-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Tasainen liike on liikettä suoraa pitkin vakionopeudella. Kappale kulkee yhtä pitkissä ajoissa yhtä pitkät matkat. Nopeus kertoo, kuinka pitkän matkan kappale kulkee yhdessä sekunnissa. Siksi nopeuden yksikkö on metri sekunnissa (m/s). Jos kärry etenee joka sekunti kaksi metriä, sen nopeus on $2\,\text{m/s}$.

<svg data-fig="motion" data-style="house" viewBox="0 0 600 330" role="img" aria-label="Liikekuva. Samaa kärryä on piirretty viidelle peräkkäiselle hetkelle: 0 s, 1 s, 2 s, 3 s ja 4 s. Kärryjen välit ovat yhtä pitkät. Jokaisen välin alla on yhtä pitkä sulku Δs. Kuva näyttää, että tasaisessa liikkeessä kappale kulkee yhtä pitkissä ajoissa yhtä pitkät matkat. Välit on piirretty mittakaavassa. Kärryt ovat samankokoisia." style="max-width:100%;font-size:24px">
  <image href="pics/fy1/fy1-5-motion.webp" x="0" y="-1.2" width="600" height="337.5" preserveAspectRatio="none"/>
  <foreignObject x="20" y="175.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t = 0\,\text{s}$</div></foreignObject>
  <foreignObject x="155" y="175.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{s}$</div></foreignObject>
  <foreignObject x="270" y="175.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2\,\text{s}$</div></foreignObject>
  <foreignObject x="385" y="175.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3\,\text{s}$</div></foreignObject>
  <foreignObject x="500" y="175.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4\,\text{s}$</div></foreignObject>
  <foreignObject x="96" y="31.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="111" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta s$</div></foreignObject>
  <foreignObject x="226" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta s$</div></foreignObject>
  <foreignObject x="341" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta s$</div></foreignObject>
  <foreignObject x="456" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta s$</div></foreignObject>
  <foreignObject x="80" y="301.5" width="440" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{yhtä pitkissä ajoissa yhtä pitkät matkat}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy1/city-highway-light-trails.webp" alt="Moottoritie yöllä kaupungissa. Tiellä on valkoisia ja punaisia valoviivoja."><figcaption>Kun kuva otetaan pitkällä valotusajalla, autojen valot piirtävät viivoja. Valkoiset ovat ajovaloja ja punaiset takavaloja. Kuvasta näkyy liikkeen rata. Kuvasta ei näe, oliko liike tasaista.</figcaption></figure>

### Suoraan verrannollisuus
Kaksi suuretta ovat suoraan verrannollisia, jos niiden suhde eli osamäärä on aina sama. Oletetaan, että tasainen liike alkaa nollakohdasta. Silloin paikka $s$ on sama kuin kuljettu matka. Paikka ja aika $t$ ovat suoraan verrannollisia. Kaksinkertainen aika antaa kaksinkertaisen matkan. Suhde $s : t$ on nopeus $v$. $(t, s)$-kuvaajassa tämä näkyy suorana, joka kulkee origon kautta.

```pysahdy
Kärry lähtee nollakohdasta. Se kulkee $3\,\text{s}$:ssa $6\,\text{m}$. Kuinka pitkän matkan se kulkee $9\,\text{s}$:ssa samalla nopeudella?
---
Aika on kolme kertaa pidempi. Siksi myös matka on kolme kertaa pidempi: $18\,\text{m}$. Matka on suoraan verrannollinen aikaan.
```

### Lineaarinen malli
Tasainen liike on malli, ei todellisuus. Pyöräilijä polkee epätasaisesti. Voyager 2 hidastuu hieman Auringon vetovoiman takia. Malli on silti hyvä, kun nopeus muuttuu tarkasteltavana aikana vain vähän. Mallin kuvaaja on suora. Suoraa kuvaa lineaarinen malli: paikka muuttuu yhtä paljon jokaista sekuntia kohti. Mallilla lasketut arvot ovat mallin arvoja. Niitä verrataan mittauksiin.

## Kaava: Tasainen liike
Oletetaan, että kappale on tarkastelun alussa ($t = 0$) paikassa $s_0$. Kappale liikkuu suoraa pitkin vakionopeudella $v$. Sen paikka hetkellä $t$ on
```latex
s = s_0 + v t
```
missä $s$ on paikka (m) valitusta nollakohdasta mitattuna, $s_0$ alkupaikka (m), $v$ nopeus (m/s) ja $t$ aika alusta (s). Kappaleen kulkema matka on $\Delta s = s - s_0 = vt$. Tämän luvun esimerkeissä kappale liikkuu positiiviseen suuntaan. Siksi nopeus on positiivinen.

### Nopeus kuvaajasta
$(t, s)$-kuvaaja on suora. Suoran kulmakerroin on nopeus:
```kaavat
keskivauhti :: v = \frac{\Delta s}{\Delta t}
```
missä $\Delta s$ on paikan muutos (m) ja $\Delta t$ sen aikaväli (s). Suora leikkaa $s$-akselin alkupaikan $s_0$ kohdalla. Jos $s_0 = 0$, paikka on suoraan verrannollinen aikaan: $s = vt$. Jos $s_0 \neq 0$, suora on yhtä jyrkkä kuin samalla nopeudella origosta alkava suora. Se on kuitenkin siirtynyt ylös tai alas. Silloin vain matka $\Delta s$ on suoraan verrannollinen aikaan. Paikka $s$ ei ole.

<svg data-fig="graph" data-style="house" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja on mittakaavassa. Siinä on kaksi tasaista liikettä, joiden nopeus on 3 m/s. Liikkeet näkyvät (t, s)-koordinaatistossa suorina. Alempi suora kulkee origon kautta, eli alkupaikka on 0. Ylempi suora alkaa paikasta s₀ = 5 m. Suorat ovat yhdensuuntaiset. Alemmalle suoralle on piirretty kulmakolmio. Ajassa 2 s paikka kasvaa 6 m. Siksi kulmakerroin on 3 m/s. Se on nopeus." style="max-width:100%;font-size:24px">
  <line x1="165" y1="300" x2="165" y2="60" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="233.5" y1="300" x2="233.5" y2="60" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="302.5" y1="300" x2="302.5" y2="60" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="371" y1="300" x2="371" y2="60" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="440" y1="300" x2="440" y2="60" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="96" y1="204" x2="440" y2="204" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="96" y1="108" x2="440" y2="108" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="95" y1="300" x2="458" y2="300" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M466,300 L454.5,305 L458,300 L454.5,295 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="301" x2="96" y2="42" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M96,34 L101,45.5 L96,42 L91,45.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="165" y1="300" x2="165" y2="307" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="155" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="233.5" y1="300" x2="233.5" y2="307" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="223.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="302.5" y1="300" x2="302.5" y2="307" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="292.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="371" y1="300" x2="371" y2="307" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="361" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="440" y1="300" x2="440" y2="307" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="430" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="89" y1="204" x2="96" y2="204" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="51" y="189.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="108" x2="96" y2="108" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="51" y="93.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <foreignObject x="66" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="472" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s\ (\text{m})$</div></foreignObject>
  <polyline points="96,300 440,156" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,252 440,108" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="89" y1="252" x2="96" y2="252" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="51" y="237.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$s_0$</div></foreignObject>
  <circle cx="96" cy="252" r="5.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="233.5" y1="242.5" x2="371" y2="242.5" stroke="#6b7480" stroke-width="1.25" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="371" y1="242.5" x2="371" y2="185" stroke="#6b7480" stroke-width="1.25" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="233.5" cy="242.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="371" cy="185" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="237.5" y="252" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t = 2\,\text{s}$</div></foreignObject>
  <foreignObject x="383" y="199" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta s = 6\,\text{m}$</span></div></foreignObject>
  <foreignObject x="448" y="141.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$s = vt$</div></foreignObject>
  <foreignObject x="448" y="93.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s = s_0 + vt$</div></foreignObject>
</svg>

```pysahdy
Kaksi kappaletta liikkuu samalla nopeudella. Toinen lähtee nollakohdasta ja toinen paikasta $5\,\text{m}$. Miten niiden $(t, s)$-suorat eroavat toisistaan?
---
Suorat ovat yhdensuuntaiset, koska kulmakerroin eli nopeus on sama. Toinen suora leikkaa $s$-akselin kohdassa $5\,\text{m}$. Se on siirtynyt ylös.
```

### Yksiköt
Muunna ensin yksiköt yhteensopiviksi, yleensä SI-yksiköiksi. Tee muunnos sijoittamalla yksikön paikalle sen arvo. Esimerkiksi $1\,\text{km} = 1000\,\text{m}$ ja $1\,\text{h} = 3600\,\text{s}$. Siksi $72\,\text{km/h} = \tfrac{72\cdot1000\,\text{m}}{3600\,\text{s}} = 20\,\text{m/s}$. Samoin $1\,\text{min} = 60\,\text{s}$. Aurinkokunnan etäisyyksiä ilmoitetaan usein tähtitieteellisinä yksikköinä. Yksikkö $1\,\text{AU} = 149\,597\,870{,}7\,\text{km}$ on suunnilleen Maan ja Auringon keskietäisyys.

```pysahdy
Auto ajaa nopeudella $90\,\text{km/h}$. Kuinka monta metriä se kulkee sekunnissa?
---
Sijoitetaan $1\,\text{km} = 1000\,\text{m}$ ja $1\,\text{h} = 3600\,\text{s}$. Silloin $90\,\text{km/h} = \tfrac{90\cdot1000\,\text{m}}{3600\,\text{s}} = 25\,\text{m/s}$. Auto kulkee sekunnissa $25\,\text{m}$.
```

## Esimerkki
Voyager 2 -luotain ylitti heliopaussin 5. marraskuuta 2018. Silloin sen etäisyys Auringosta oli $s_0 = 119{,}0\,\text{AU}$ (Burlaga ym. 2019, Nature Astronomy). Luotaimen nopeus Aurinkoon nähden oli silloin $v = 15{,}341\,\text{km/s}$ (NASA/JPL). Oletetaan nopeus vakioksi. Kuinka kaukana Auringosta luotain on mallin mukaan 5. marraskuuta 2026?

<!-- vaihe -->

**Tunnetut ja kysytty.**

- $s_0 = 119{,}0\,\text{AU}$ hetkellä $t = 0$ (5. marraskuuta 2018),
- $v = 15{,}341\,\text{km/s}$ ja
- $1\,\text{AU} = 149\,597\,870{,}7\,\text{km}$.

Aikaväli 5. marraskuuta 2018 – 5. marraskuuta 2026 on 8 vuotta. Siinä on karkauspäivät 2020 ja 2024: $8 \cdot 365 + 2 = 2922$ vuorokautta.

Kysytään etäisyyttä $s$ Auringosta.

<!-- vaihe -->

**Periaate.** Nopeus oletetaan vakioksi. Silloin luotain liikkuu tasaisesti ja paikka noudattaa lineaarista mallia. Tulos on mallin arvo, ei mittaus. Auringon vetovoima hidastaa luotainta hieman. Vuosina 2018–2026 nopeus pienenee vain noin $0{,}1\,\text{km/s}$, joten sen voi tässä jättää huomiotta.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
s = s_0 + v t
```

<!-- vaihe -->

**Yksikkömuunnokset.** Aika on valmiiksi vuorokausina, $t = 2922\,\text{vrk}$. Siksi nopeus muunnetaan yksikköön AU/vrk. Yksiköiden paikalle sijoitetaan $1\,\text{km} = \tfrac{1}{149\,597\,870{,}7}\,\text{AU}$ ja $1\,\text{s} = \tfrac{1}{86\,400}\,\text{vrk}$. Saadaan $v = 15{,}341\,\tfrac{\text{km}}{\text{s}} = 15{,}341 \cdot \tfrac{1}{149\,597\,870{,}7}\,\text{AU} : \left(\tfrac{1}{86\,400}\,\text{vrk}\right) = 0{,}0088602\,\tfrac{\text{AU}}{\text{vrk}}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
s &= s_0 + v t \\
&= 119{,}0\,\text{AU} \\
&\quad + 0{,}0088602\,\tfrac{\text{AU}}{\text{vrk}} \cdot 2922\,\text{vrk} \\
&= 119{,}0\,\text{AU} + 25{,}89\,\text{AU} \\
&= 144{,}89\,\text{AU}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Luotain on mallin mukaan $s \approx 144{,}9\,\text{AU}$ Auringosta, noin $2{,}17 \cdot 10^{10}\,\text{km}$. Alkuetäisyys on annettu kymmenesosan tarkkuudella. Siksi tulos pyöristetään kymmenesosiin.

<!-- vaihe -->

**Järkevyys.** Nopeus $15\,\text{km/s}$ vie vuodessa noin $15\,\text{km/s} \cdot 3{,}16 \cdot 10^{7}\,\text{s} \approx 4{,}7 \cdot 10^{8}\,\text{km} \approx 3{,}2\,\text{AU}$. Kahdeksassa vuodessa luotain etenee siis noin $26\,\text{AU}$, ja $119{,}0\,\text{AU} + 26\,\text{AU} \approx 145\,\text{AU}$.

Sama malli antaa 15. helmikuuta 2026 etäisyydeksi Auringosta $142{,}6\,\text{AU}$. NASA/JPL:n Voyager-tilannesivu ilmoitti helmikuussa 2026 luotaimen etäisyydeksi Maasta $143{,}05\,\text{AU}$.

Maa kiertää Aurinkoa. Siksi luotaimen etäisyys Maasta poikkeaa sen etäisyydestä Auringosta vuoden mittaan jopa noin $1\,\text{AU}$.

Ero $0{,}5\,\text{AU}$ on tätä pienempi. Malli ja havainto täsmäävät siis noin $1\,\text{AU}$:n tarkkuudella. Tarkemmin tämä vertailu ei mallia testaa. Ero on alle prosentti etäisyydestä, joten vakionopeusmalli sopii muutaman vuoden ennusteisiin.

## Yleinen virhekäsitys
Moni ajattelee, että tasaisessa liikkeessä paikka kaksinkertaistuu, kun aika kaksinkertaistuu. Näin käy vain, jos liike alkaa nollakohdasta. Kärry on alussa kohdassa $s_0 = 6\,\text{m}$ ja etenee nopeudella $2{,}0\,\text{m/s}$. Hetkellä $2{,}0\,\text{s}$ se on paikassa $10\,\text{m}$ ja hetkellä $4{,}0\,\text{s}$ paikassa $14\,\text{m}$. Se ei ole $20\,\text{m}$:ssä. Matka sen sijaan kaksinkertaistuu: $4{,}0\,\text{m}$ muuttuu $8{,}0\,\text{m}$:ksi. Toinen virhe on laskea nopeus paikan ja ajan osamääränä $s : t$. Nopeus on kuitenkin paikan muutoksen ja aikavälin osamäärä. Kun $s_0 \neq 0$, nopeus on $\Delta s : \Delta t$, ei $s : t$.

## Tiivistelmä
- Tasaisessa liikkeessä nopeus on vakio. Kappale kulkee yhtä pitkissä ajoissa yhtä pitkät matkat: $s = s_0 + vt$.
- Kuljettu matka $\Delta s = vt$ on suoraan verrannollinen aikaan. Paikka $s$ on verrannollinen aikaan vain, kun $s_0 = 0$.
- $(t, s)$-kuvaaja on suora. Suoran kulmakerroin $\Delta s : \Delta t$ on nopeus. Suoran ja $s$-akselin leikkauskohta on alkupaikka $s_0$.
- Muunna yksiköt ennen laskemista sijoittamalla, esimerkiksi $1\,\text{km} = 1000\,\text{m}$ ja $1\,\text{h} = 3600\,\text{s}$.
- Tasainen liike on lineaarinen malli. Sen antamat arvot ovat mallin arvoja. Niitä voi verrata mittauksiin, kuten Voyager 2 -luotaimen etäisyyttä.
