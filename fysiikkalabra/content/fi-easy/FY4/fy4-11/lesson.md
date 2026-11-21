# Liikenneturvallisuus: jarrutus, turvavyö ja turvatyyny

> **Miksi** auton pysähtymismatka on $100\,\text{km/h}$:n nopeudella lähes kolme kertaa niin pitkä kuin $50\,\text{km/h}$:n nopeudella? Ja miksi turvavyö suojaa, kun auto ei ehdi pysähtyä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: syysilta maantiellä kuusimetsän keskellä. Vasemmalta tulee henkilöauto ajovalot päällä. Tien oikealla puolella on hirvivaroitusmerkki, ja sen takana hirvi astuu metsän reunasta tielle auton eteen. Auton ja hirven välinen matka on lyhyt. Auto tarvitsisi pysähtymiseen paljon pidemmän matkan." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-11-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Pysähtyminen alkaa reaktiosta
Kun kuljettaja huomaa vaaran, auto ei hidasta heti. Kuljettajan täytyy ensin huomata vaara. Sitten hän päättää jarruttaa ja siirtää jalan jarrupolkimelle. Tähän kuluu **reaktioaika** $t_\text{r}$. Se on aika vaaran huomaamisesta jarrutuksen alkuun. Tavallisesti se on noin sekunti. Esimerkiksi Liikenneturvan törmäysnopeuslaskuri olettaa reaktioajaksi $1\,\text{s}$. Väsymys, alkoholi ja puhelimen vilkaisu pidentävät reaktioaikaa. Reaktioajan auto kulkee yhä samalla nopeudella kuin ennen. Matkaa, jonka auto kulkee tänä aikana, sanotaan **reaktiomatkaksi** $s_\text{r}$. Vasta sen jälkeen jarrut alkavat hidastaa autoa. Auto kulkee **jarrutusmatkan** $s_\text{j}$ ennen kuin se pysähtyy. Reaktiomatka ja jarrutusmatka ovat yhteensä **pysähtymismatka** $s_\text{p}$.

### Tie pysäyttää auton kitkalla
Jarrut hidastavat pyörien pyörimistä, mutta autoa hidastaa tie. Vaakasuoralla tiellä renkaiden ja tien välinen kitka on ainoa vaakasuora voima, kun ilmanvastus jätetään huomiotta. Kitka osoittaa taaksepäin. Newtonin toisen lain mukaan myös kiihtyvyys osoittaa silloin taaksepäin, ja auto hidastuu. Jarrutuksessa kiihtyvyyden suuruutta sanotaan **hidastuvuudeksi** $a$.

<svg data-fig="jarrutus" viewBox="0 0 600 330" role="img" aria-label="Vasemmalla on tilannekuva: auto jarruttaa vaakasuoralla tiellä, ja jarruvalot palavat. Auton yllä sininen nopeusnuoli osoittaa eteenpäin oikealle ja oranssi kiihtyvyysnuoli taaksepäin vasemmalle. Oikealla on auton voimakuvio. Auto on piirretty suorakulmiona. Paino G osoittaa keskipisteestä alas. Tien tukivoima N osoittaa alapinnasta ylös ja on yhtä pitkä kuin paino. Tien kitkavoima F mu osoittaa alapinnan takakulmasta taaksepäin, ja se on lähes painon pituinen. Kitka on ainoa vaakasuora voima." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-11-jarrutus.webp" x="1.2" y="1.2" width="597" height="338.3" preserveAspectRatio="none"/>
  <foreignObject x="77.5" y="9.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="205.5" y="91.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="97.5" y="47.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="383.5" y="9.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <foreignObject x="475.5" y="230" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="503.5" y="107" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="312" y="203.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
</svg>

Kitka voi kasvaa vain tiettyyn ylärajaan asti. Yläraja riippuu renkaista ja tien pinnasta. Kuivalla asfaltilla hidastuvuus voi olla noin $9\,\text{m/s}^2$, ja Liikenneturvan laskuri käyttää samaa arvoa. Märällä, lumisella ja jäisellä tiellä kitka on pienempi, joten myös hidastuvuus on pienempi. Jäällä hidastuvuus on vain pieni osa kuivan tien arvosta. Lukkiutumattomat jarrut (ABS) estävät pyöriä lukkiutumasta. Pyörivän renkaan pinta ei liu'u tien suhteen, joten renkaaseen vaikuttaa lepokitka. Lepokitka voi olla suurempi kuin liukuvan renkaan liukukitka, ja auto pysyy ohjattavana.

```pysahdy
Miksi jarrutusmatka on jäisellä tiellä pidempi kuin kuivalla asfaltilla, vaikka jarrupoljinta painetaan täysillä?
---
Jäällä kitka on pienempi, joten hidastuvuus on pienempi. Auton pysäyttäminen kestää kauemmin, ja auto kulkee pidemmän matkan.
```

### Nopeus kasvattaa jarrutusmatkaa jyrkästi
Reaktiomatka on suoraan verrannollinen nopeuteen. Kun nopeus on kaksinkertainen, auto kulkee reaktioajassa kaksinkertaisen matkan. Jarrutusmatka kasvaa jyrkemmin. Kun hidastuvuus on sama, kaksinkertaisen nopeuden pysäyttäminen kestää kaksi kertaa kauemmin. Koko tämän ajan auto liikkuu kaksi kertaa nopeammin. Jarrutusmatka on siksi neljä kertaa pidempi. Kuvassa reaktioaika on $1{,}0\,\text{s}$ ja hidastuvuus $9{,}0\,\text{m/s}^2$ kummallakin nopeudella.

<svg data-fig="pysahtyminen" viewBox="0 0 600 400" role="img" aria-label="Kaksi tietä päällekkäin. Matkat ovat mittakaavassa, autot eivät. Kummassakin kuljettaja huomaa vaaran katkoviivan kohdalla. Ylhäällä nopeus on 50 kilometriä tunnissa. Vihreä reaktiomatka on 13,9 metriä ja ruskea jarrutusmatka 10,7 metriä, yhteensä 24,6 metriä. Alhaalla nopeus on 100 kilometriä tunnissa. Reaktiomatka on kaksi kertaa pidempi, 27,8 metriä, ja jarrutusmatka neljä kertaa pidempi, 42,9 metriä. Yhteensä matka on 70,6 metriä. Reaktioaika on 1,0 sekuntia ja hidastuvuus 9,0 metriä sekunnin neliölle. Alla on mittanauha metreinä." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy411-p50" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient><linearGradient id="fy411-p100" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient></defs>
  <foreignObject x="16" y="11.5" width="261" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v_0 = 50\,\text{km/h}:\ s_\text{p} = 24{,}6\,\text{m}$</div></foreignObject>
  <rect x="16" y="90" width="568" height="24" fill="#6c757d"/>
  <line x1="16" y1="90" x2="584" y2="90" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="16" y1="114" x2="584" y2="114" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <g transform="translate(147.5,90) scale(0.32)">
  <path d="M2,-15 Q0,-41 24,-45 L62,-49 Q82,-77 112,-79 H156 Q178,-77 192,-51 L212,-45 Q226,-41 224,-15 Z" fill="url(#fy411-p50)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M72,-51 Q88,-71 110,-72 H128 V-51 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M136,-72 H154 Q170,-69 180,-51 H136 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="208" y="-39" width="14" height="8" rx="2" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="2" y="-40" width="9" height="9" rx="2" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="6" cy="-36" r="14" fill="#f2a69c"/>
  <rect x="2" y="-40" width="9" height="9" rx="2" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="48" cy="-15" r="15" fill="#1f2933"/>
  <circle cx="48" cy="-15" r="7" fill="#c4ccd4"/>
  <circle cx="178" cy="-15" r="15" fill="#1f2933"/>
  <circle cx="178" cy="-15" r="7" fill="#c4ccd4"/>
  </g>
  <line x1="60" y1="48" x2="60" y2="146" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <rect x="60" y="124" width="90.5" height="12" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="150.5" y="124" width="69.5" height="12" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="88.5" y="139.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$s_\text{r}$</div></foreignObject>
  <foreignObject x="168.5" y="139.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#b8622d">$s_\text{j}$</div></foreignObject>
  <foreignObject x="16" y="181.5" width="274" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v_0 = 100\,\text{km/h}:\ s_\text{p} = 70{,}6\,\text{m}$</div></foreignObject>
  <rect x="16" y="260" width="568" height="24" fill="#6c757d"/>
  <line x1="16" y1="260" x2="584" y2="260" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="16" y1="284" x2="584" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <g transform="translate(447,260) scale(0.32)">
  <path d="M2,-15 Q0,-41 24,-45 L62,-49 Q82,-77 112,-79 H156 Q178,-77 192,-51 L212,-45 Q226,-41 224,-15 Z" fill="url(#fy411-p100)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M72,-51 Q88,-71 110,-72 H128 V-51 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M136,-72 H154 Q170,-69 180,-51 H136 Z" fill="#eef5f9" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="208" y="-39" width="14" height="8" rx="2" fill="#ffc078" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="2" y="-40" width="9" height="9" rx="2" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="6" cy="-36" r="14" fill="#f2a69c"/>
  <rect x="2" y="-40" width="9" height="9" rx="2" fill="#c92a2a" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="48" cy="-15" r="15" fill="#1f2933"/>
  <circle cx="48" cy="-15" r="7" fill="#c4ccd4"/>
  <circle cx="178" cy="-15" r="15" fill="#1f2933"/>
  <circle cx="178" cy="-15" r="7" fill="#c4ccd4"/>
  </g>
  <line x1="60" y1="218" x2="60" y2="316" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <rect x="60" y="294" width="180.5" height="12" fill="#2b8a3e" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="240.5" y="294" width="278.5" height="12" fill="#b8622d" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="134" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$s_\text{r}$</div></foreignObject>
  <foreignObject x="363.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#b8622d">$s_\text{j}$</div></foreignObject>
  <line x1="60" y1="364" x2="547.5" y2="364" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="60" y1="364" x2="60" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="50" y="367.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
  <line x1="125" y1="364" x2="125" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="108.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10$</div></foreignObject>
  <line x1="190" y1="364" x2="190" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="173.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$20$</div></foreignObject>
  <line x1="255" y1="364" x2="255" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="238.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$30$</div></foreignObject>
  <line x1="320" y1="364" x2="320" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="303.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$40$</div></foreignObject>
  <line x1="385" y1="364" x2="385" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="368.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$50$</div></foreignObject>
  <line x1="450" y1="364" x2="450" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="433.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$60$</div></foreignObject>
  <line x1="515" y1="364" x2="515" y2="356" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="498.5" y="367.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$70$</div></foreignObject>
  <foreignObject x="555.5" y="367.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{m}$</div></foreignObject>
</svg>

Tästä saadaan vastaus alun kysymyksen ensimmäiseen osaan. Nopeus kaksinkertaistuu $50\,\text{km/h}$:sta $100\,\text{km/h}$:iin. Silloin reaktiomatka kaksinkertaistuu $13{,}9\,\text{m}$:stä $27{,}8\,\text{m}$:iin, mutta jarrutusmatka nelinkertaistuu $10{,}7\,\text{m}$:stä $42{,}9\,\text{m}$:iin. Pysähtymismatka kasvaa siksi $24{,}6\,\text{m}$:stä $70{,}6\,\text{m}$:iin, lähes kolminkertaiseksi.

```pysahdy
Kuljettaja jarruttaa pysähdyksiin nopeudesta $40\,\text{km/h}$ eikä nopeudesta $80\,\text{km/h}$. Miten jarrutusmatka muuttuu, kun hidastuvuus on sama?
---
Se lyhenee neljäsosaan. Pysäyttäminen kestää vain puolet ajasta, ja auto liikkuu koko ajan puolta hitaammin.
```

### Sama liikemäärän muutos, eri törmäysaika
Jos este on lähempänä kuin pysähtymismatka, auto törmää. Nokkakolarissa auton keula rypistyy, ja auto pysähtyy noin sekunnin kymmenesosassa. Kun matkustaja pysähtyy auton mukana, hänen liikemääränsä $p = mv$ muuttuu arvosta $mv$ nollaan. Oletetaan, että matkustajan massa on sama ja hän pysähtyy samasta alkunopeudesta samaan loppunopeuteen. Silloin liikemäärän muutos on sama turvavyön kanssa ja ilman. Alku- ja loppunopeus määräävät liikemäärän muutoksen. Oikeassa onnettomuudessa turvavyöttömän matkustajan liike ei kuitenkaan aina lopu, kun auto pysähtyy. Hän voi esimerkiksi lentää tuulilasin läpi. Kun liikemäärän muutos on sama, vain **törmäysaikaa** $\Delta t$ voidaan muuttaa. Törmäysaika on aika, jossa matkustaja pysähtyy. Luvussa *Liikemäärä ja impulssi* opit, että liikemäärän muutos on yhtä suuri kuin impulssi $\overline{I} = \overline{F}\,\Delta t$. Mitä pidempi törmäysaika on, sitä pienempi voima riittää samaan liikemäärän muutokseen.

<svg data-fig="tormays" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva, pyöristetyt esimerkkiarvot: matkustajan nopeus nokkakolarissa, kun auton nopeus on 50 kilometriä tunnissa. Vaaka-akselilla on aika 0–0,12 sekuntia ja pystyakselilla nopeus 0–16 metriä sekunnissa. Sininen viiva: vyöhön kiinnitetty matkustaja hidastuu tasaisesti auton mukana 13,9 metristä sekunnissa nollaan 0,10 sekunnissa. Ruskea viiva: ilman vyötä matkustaja jatkaa nopeudella 13,9 metriä sekunnissa 0,090 sekuntiin asti. Sitten hän osuu auton sisustaan ja pysähtyy 0,010 sekunnissa. Nopeuden muutos on molemmissa sama." style="max-width:100%;font-size:24px">
  <line x1="145" y1="290" x2="145" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="210" y1="290" x2="210" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275" y1="290" x2="275" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="340" y1="290" x2="340" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="405" y1="290" x2="405" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="232.5" x2="470" y2="232.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="175" x2="470" y2="175" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="117.5" x2="470" y2="117.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="60" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="79" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="291" x2="80" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,34 L86,47 L74,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="145" y1="290" x2="145" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="116" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}02$</div></foreignObject>
  <line x1="210" y1="290" x2="210" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="181" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}04$</div></foreignObject>
  <line x1="275" y1="290" x2="275" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="246" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}06$</div></foreignObject>
  <line x1="340" y1="290" x2="340" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="311" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}08$</div></foreignObject>
  <line x1="405" y1="290" x2="405" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="382.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}1$</div></foreignObject>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="441" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}12$</div></foreignObject>
  <line x1="73" y1="232.5" x2="80" y2="232.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="218" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="73" y1="175" x2="80" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="160.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="73" y1="117.5" x2="80" y2="117.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="103" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="73" y1="60" x2="80" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$16$</div></foreignObject>
  <foreignObject x="50" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="70" y="3.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\text{m/s})$</div></foreignObject>
  <polyline points="80,90.5 405,290" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="80,90.5 372.5,90.5 405,290" fill="none" stroke="#b8622d" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="96" y="55.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#b8622d"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{ilman vyötä: }\Delta t = 0{,}010\,\text{s}$</span></div></foreignObject>
  <foreignObject x="119" y="241" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{vyössä: }\Delta t = 0{,}10\,\text{s}$</span></div></foreignObject>
</svg>

Ilman turvavyötä matkustaja jatkaa liikettään lähes samalla nopeudella, kun auto hidastuu hänen ympärillään. Newtonin ensimmäisen lain mukaan mikään voima ei vielä hidasta häntä. Hän osuu ohjauspyörään, kojelautaan tai tuulilasiin ja pysähtyy sekunnin sadasosissa. **Turvavyö** kiinnittää matkustajan autoon, joten hän hidastuu auton rypistyvän keulan mukana. Vyö myös venyy hieman. Se jakaa voiman lantion, rintakehän ja olkapään vahvoille luille. Turvatyyny täyttyy sekunnin sadasosissa ja ottaa vastaan pään ja ylävartalon. Se pidentää pysähtymisaikaa ja jakaa voiman suurelle alalle, joten paine kehoon on pienempi. Turvatyyny on tehty toimimaan yhdessä turvavyön kanssa, ei sen sijasta.

```pysahdy
Auto pysähtyy törmäyksessä. Miksi vyötön matkustaja jatkaa eteenpäin, vaikka mikään ei työnnä häntä?
---
Mikään voima ei hidasta häntä. Newtonin ensimmäisen lain mukaan hän jatkaa liikettä entisellä nopeudella, kun auto pysähtyy hänen ympärillään.
```

<figure class="unit-photo"><img src="pics/fy4/side-impact-crash-test.webp" alt="Keltainen auto testihallissa. Auton kylki on painunut sisään."><figcaption>Auto törmäystestin jälkeen Yhdysvalloissa. Auton kylki on painunut sisään.</figcaption></figure>

Tämä on vastaus alun kysymyksen toiseen osaan. Ero näkyy myös onnettomuustilastoissa. Onnettomuustietoinstituutti on koonnut tiedot kuolemaan johtaneista onnettomuuksista vuosina 2017–2021. Tutkijalautakunnat tutkivat nämä onnettomuudet. Henkilö- ja pakettiautoissa kuoli 278 ihmistä, joilla oli turvavyö, ja 198 ihmistä ilman turvavyötä. Lautakuntien arvion mukaan 114 vyötöntä olisi voinut selvitä, jos vyö olisi ollut kiinni. Liikenneturvan seurannan mukaan lähes kaikki etupenkillä istuvat käyttävät vyötä.

## Kaava: Pysähtymismatka ja törmäyksen voima

### Reaktiomatka ja jarrutusmatka
Reaktioajan auto liikkuu tasaisella nopeudella $v_0$, joten reaktiomatka on
```latex
s_\text{r} = v_0\,t_\text{r}
```
missä $s_\text{r}$ on reaktiomatka ($\text{m}$), $v_0$ auton nopeus ennen jarrutusta ($\text{m/s}$) ja $t_\text{r}$ reaktioaika ($\text{s}$). Jarrutuksessa hidastuvuus oletetaan vakioksi. Silloin nopeus pienenee $(t,v)$-kuvaajassa suoraviivaisesti nollaan. Kuten luvussa *Kiihtyvyys ja tasaisesti kiihtyvä liike*, kuljettu matka on kuvaajan ja aika-akselin väliin jäävä pinta-ala.

<svg data-fig="tv" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva (t, v)-kuvaajasta, ei lukuarvoja. Nopeus pysyy reaktioajan t_r ajan arvossa v_0, joten kuvaaja on vaakasuora. Sen alle jää vihreä suorakulmio, jonka pinta-ala on reaktiomatka s_r = v_0 t_r. Sitten nopeus pienenee suoraviivaisesti nollaan jarrutusajassa t_j. Kuvaajan alle jää ruskea kolmio, jonka pinta-ala on jarrutusmatka s_j = puolet v_0 t_j:stä. Suoran kulmakertoimen suuruus on hidastuvuus a." style="max-width:100%;font-size:24px">
  <line x1="196.5" y1="290" x2="196.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="453.5" y1="290" x2="453.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="121" x2="500" y2="121" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="79" y1="290" x2="514" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,290 L513,296 L513,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="291" x2="80" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,44 L86,57 L74,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="196.5" y1="290" x2="196.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="180" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{r}$</div></foreignObject>
  <line x1="453.5" y1="290" x2="453.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="418.5" y="299.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{r} + t_\text{j}$</div></foreignObject>
  <line x1="73" y1="121" x2="80" y2="121" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="106.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_0$</div></foreignObject>
  <foreignObject x="50" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="532" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="70" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polygon points="80,290 80,121 196.5,121 196.5,290" fill="#2b8a3e" fill-opacity="0.35"/>
  <polygon points="196.5,290 196.5,121 453.5,290" fill="#b8622d" fill-opacity="0.35"/>
  <polyline points="80,121 196.5,121 453.5,290" fill="none" stroke="#1971c2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="122" y="199.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s_\text{r}$</div></foreignObject>
  <foreignObject x="265.5" y="224.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s_\text{j}$</div></foreignObject>
  <foreignObject x="348" y="170.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{kulmakerroin } {-a}$</div></foreignObject>
</svg>

Nopeus pienenee arvosta $v_0$ nollaan, ja hidastuvuus on $a$. Jarrutusaika on siksi
```latex
t_\text{j} = \frac{v_0}{a}
```
missä $t_\text{j}$ on jarrutusaika ($\text{s}$) ja $a$ hidastuvuus eli kiihtyvyyden suuruus ($\text{m/s}^2$). Jarrutusmatka on kolmion pinta-ala $\tfrac{1}{2}\,v_0\,t_\text{j}$. Sijoitetaan siihen jarrutusaika. Saadaan
```latex
s_\text{j} = \frac{v_0^2}{2a}
```
missä $s_\text{j}$ on jarrutusmatka ($\text{m}$). Pysähtymismatka on näiden summa:
```latex
s_\text{p} = v_0\,t_\text{r} + \frac{v_0^2}{2a}
```
missä $s_\text{p}$ on pysähtymismatka ($\text{m}$). Malli olettaa kolme asiaa: tie on vaakasuora, hidastuvuus on jarrutuksen ajan vakio ja ilmanvastus jätetään huomiotta. Nopeus sijoitetaan yksikössä $\text{m/s}$.

### Hidastuvuus kitkasta
Vaakasuoralla tiellä auto ei kiihdy pystysuunnassa, joten tukivoima on yhtä suuri kuin paino, $N = mg$. Kun jarrutetaan niin lujaa kuin pito sallii, kitka on $F_\mu = \mu N$. Tässä $\mu$ on renkaiden ja tien välinen kitkakerroin. Newtonin toisen lain mukaan $\mu mg = ma$, ja massa supistuu:
```latex
a = \mu g
```
missä $\mu$ on kitkakerroin (ei yksikköä) ja $g = 9{,}81\,\text{m/s}^2$. Kuivan asfaltin $9{,}0\,\text{m/s}^2$ vastaa kitkakerrointa $0{,}92$. Tässä mallissa jarrutusmatka ei riipu auton massasta. Raskaan kuorma-auton jarrutusmatka on silti usein pidempi. Sen jarrut ja renkaat eivät aina pysty käyttämään koko pitoa.

### Törmäyksen keskimääräinen voima
Matkustajan nopeus muuttuu törmäyksessä määrän $\Delta v$ ajassa $\Delta t$. Impulssiperiaate on $\overline{F}_\text{ka}\,\Delta t = \Delta\overline{p}$. Siitä saadaan matkustajaan vaikuttavan keskimääräisen voiman suuruus:
```latex
F_\text{ka} = \frac{m\,\Delta v}{\Delta t}
```
missä $F_\text{ka}$ on keskimääräinen voima ($\text{N}$), $m$ matkustajan massa ($\text{kg}$), $\Delta v$ nopeuden muutoksen suuruus ($\text{m/s}$) ja $\Delta t$ törmäysaika ($\text{s}$). Esimerkiksi $75\,\text{kg}$:n matkustaja pysähtyy $50\,\text{km/h}$:n nopeudesta. Liikemäärän muutos on noin $1040\,\text{kg}\cdot\text{m/s}$. Vyössä muutos kestää noin $0{,}10\,\text{s}$, ja keskimääräinen voima on noin $10\,\text{kN}$. Ilman vyötä aika on noin $0{,}010\,\text{s}$ ja voima kymmenkertainen.

<svg data-fig="tF" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja mittakaavassa, pyöristetyt esimerkkiarvot 75 kilogramman matkustajalle, kun nopeus on 50 kilometriä tunnissa. Vaaka-akselilla on aika 0–0,12 sekuntia ja pystyakselilla keskimääräinen voima 0–120 kilonewtonia. Matala sininen suorakulmio: vyössä voima on noin 10 kilonewtonia 0,10 sekunnin ajan. Kapea ja korkea ruskea suorakulmio: ilman vyötä voima on noin 100 kilonewtonia 0,010 sekunnin ajan. Suorakulmioiden pinta-alat ovat yhtä suuret." style="max-width:100%;font-size:24px">
  <line x1="145" y1="310" x2="145" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="210" y1="310" x2="210" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="275" y1="310" x2="275" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="340" y1="310" x2="340" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="405" y1="310" x2="405" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="310" x2="470" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="270" x2="470" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="230" x2="470" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="190" x2="470" y2="190" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="150" x2="470" y2="150" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="110" x2="470" y2="110" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="70" x2="470" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="79" y1="310" x2="484" y2="310" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,310 L483,316 L483,304 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="311" x2="80" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,44 L86,57 L74,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="145" y1="310" x2="145" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="116" y="319.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}02$</div></foreignObject>
  <line x1="210" y1="310" x2="210" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="181" y="319.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}04$</div></foreignObject>
  <line x1="275" y1="310" x2="275" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="246" y="319.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}06$</div></foreignObject>
  <line x1="340" y1="310" x2="340" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="311" y="319.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}08$</div></foreignObject>
  <line x1="405" y1="310" x2="405" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="382.5" y="319.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}1$</div></foreignObject>
  <line x1="470" y1="310" x2="470" y2="317" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="441" y="319.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}12$</div></foreignObject>
  <line x1="73" y1="270" x2="80" y2="270" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="73" y1="230" x2="80" y2="230" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="215.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="73" y1="190" x2="80" y2="190" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="175.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="73" y1="150" x2="80" y2="150" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="73" y1="110" x2="80" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="95.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="73" y1="70" x2="80" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="55.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$120$</div></foreignObject>
  <foreignObject x="50" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="295.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="70" y="13.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_\text{ka}\ (\text{kN})$</div></foreignObject>
  <polygon points="80,310 80,289 405,289 405,310" fill="#1971c2" fill-opacity="0.45"/>
  <polyline points="80,289 405,289 405,310" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polygon points="372.5,310 372.5,101.5 405,101.5 405,310" fill="#b8622d" fill-opacity="0.6"/>
  <polyline points="372.5,310 372.5,101.5 405,101.5 405,310" fill="none" stroke="#b8622d" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="96" y="256.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{vyössä: } F_\text{ka} \approx 10\,\text{kN}$</span></div></foreignObject>
  <foreignObject x="96" y="103.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#b8622d"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{ilman vyötä: } F_\text{ka} \approx 100\,\text{kN}$</span></div></foreignObject>
</svg>

Kuvaajan suorakulmioiden pinta-alat ovat yhtä suuret, koska kumpikin on sama liikemäärän muutos $m\,\Delta v$. Todellisuudessa voima vaihtelee törmäyksen aikana. Suurin voima on keskimääräistä suurempi.

## Esimerkki
Auto ajaa kuivalla asfaltilla nopeudella $80\,\text{km/h}$. Kuljettaja vilkaisee puhelinta. Siksi hänen reaktioaikansa vaaratilanteessa on $2{,}0\,\text{s}$. Auton hidastuvuus jarrutuksessa on $9{,}0\,\text{m/s}^2$. Kuinka pitkä on auton pysähtymismatka?

<!-- vaihe -->

**Tunnetut ja kysytty.** $v_0 = 80\,\text{km/h}$, $t_\text{r} = 2{,}0\,\text{s}$ ja $a = 9{,}0\,\text{m/s}^2$.

Kysytään pysähtymismatkaa $s_\text{p}$.

<!-- vaihe -->

**Periaate.** Reaktioajan auto liikkuu tasaisella nopeudella, joten reaktiomatka on nopeus kertaa aika. Sen jälkeen auto hidastuu vakiohidastuvuudella, kun tie on vaakasuora ja ilmanvastus jätetään huomiotta. Silloin jarrutusmatka on $(t,v)$-kuvaajan kolmion pinta-ala. Pysähtymismatka on näiden summa.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&s_\text{p} = s_\text{r} + s_\text{j} \\
&s_\text{p} = v_0\,t_\text{r} + \frac{v_0^2}{2a}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Nopeus muunnetaan yksikköön $\text{m/s}$: $80\,\text{km/h} = \tfrac{80 \cdot 1000\,\text{m}}{3600\,\text{s}} \approx 22{,}22\,\text{m/s}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin kumpikin osamatka ja sitten summa:
```latex
\begin{aligned}
&s_\text{r} = v_0\,t_\text{r} \\
&\phantom{s_\text{r}} = 22{,}22\,\tfrac{\text{m}}{\text{s}} \cdot 2{,}0\,\text{s} \\
&\phantom{s_\text{r}} = 44{,}44\,\text{m} \\
&s_\text{j} = \frac{(22{,}22\,\text{m/s})^2}{2 \cdot 9{,}0\,\text{m/s}^2} \\
&\phantom{s_\text{j}} = 27{,}43\,\text{m} \\
&s_\text{p} = (44{,}44 + 27{,}43)\,\text{m} \\
&\phantom{s_\text{p}} \approx 72\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Pysähtymismatka on noin $72\,\text{m}$. Vastauksessa on kaksi merkitsevää numeroa, kuten reaktioajassa $2{,}0\,\text{s}$ ja hidastuvuudessa $9{,}0\,\text{m/s}^2$. Reaktiomatka $44\,\text{m}$ on siitä yli puolet.

<!-- vaihe -->

**Järkevyys.** Reaktioajalla $1{,}0\,\text{s}$ reaktiomatka olisi $22\,\text{m}$ ja pysähtymismatka noin $50\,\text{m}$. Puhelimen vilkaisu pidentää pysähtymismatkaa siis noin $22\,\text{m}$, eli noin viiden auton pituuden verran. Jarrutusmatka on silti sama. Nopeus $22\,\text{m/s}$ ja jarrutusaika $22\,\text{m/s} : 9\,\text{m/s}^2 \approx 2{,}5\,\text{s}$ antavat jarrutusmatkaksi noin $\tfrac{1}{2} \cdot 22\,\text{m/s} \cdot 2{,}5\,\text{s} \approx 27\,\text{m}$, kuten laskussa.

## Yleinen virhekäsitys
Moni ajattelee, että kaksinkertainen nopeus tarkoittaa kaksinkertaista pysähtymismatkaa. Reaktiomatka kaksinkertaistuu, mutta jarrutusmatka nelinkertaistuu, koska se riippuu nopeuden neliöstä. Toinen virhe on ajatella, että turvavyö pienentää liikemäärän muutosta. Kun matkustaja pysähtyy samasta nopeudesta, liikemäärä muuttuu arvosta $mv$ nollaan kummassakin tapauksessa. Vyö pidentää aikaa, jossa muutos tapahtuu, ja pienentää siksi voimaa. Kolmas virhe on uskoa, että hitaassa kolarissa voi ottaa vastaan käsillä. Jo $50\,\text{km/h}$:n törmäyksessä keskimääräinen voima on vyössäkin noin $10\,\text{kN}$. Se on yli kymmenkertainen ihmisen painoon verrattuna, eikä käsien lihasvoima riitä siihen.

## Tiivistelmä
- Pysähtymismatka on reaktiomatka $s_\text{r} = v_0\,t_\text{r}$ plus jarrutusmatka $s_\text{j} = \tfrac{v_0^2}{2a}$. Tämä pätee, kun hidastuvuus on vakio.
- Reaktiomatka on verrannollinen nopeuteen ja jarrutusmatka nopeuden neliöön. Kaksinkertainen nopeus antaa nelinkertaisen jarrutusmatkan.
- Jarrutuksessa autoa hidastaa renkaiden ja tien välinen kitka. Vaakasuoralla tiellä $a = \mu g$. Liukkaalla tiellä jarrutusmatka on siksi monta kertaa pidempi.
- Kun matkustaja pysähtyy samasta alkunopeudesta samaan loppunopeuteen, hänen liikemääränsä muutos on sama vyön kanssa ja ilman. Turvavyö ja turvatyyny pidentävät törmäysaikaa. Siksi keskimääräinen voima $F_\text{ka} = \tfrac{m\,\Delta v}{\Delta t}$ pienenee.
- Turvatyyny jakaa voiman suurelle alalle. Se toimii yhdessä turvavyön kanssa, ei sen sijasta.
