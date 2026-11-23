# Newtonin toinen laki

> **Miksi** täyteen lastattu kuorma-auto kiihtyy liikennevaloista hitaammin kuin tyhjä, vaikka moottori on sama?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: maantien liikennevalot ovat juuri vaihtuneet vihreiksi, ja kaksi samanlaista kuorma-autoa on lähtenyt liikkeelle vierekkäisiltä kaistoilta. Lähempänä on täyteen tukeilla lastattu auto, joka on vasta päässyt pysäytysviivan yli. Kauempana oleva tyhjä auto on jo selvästi edellä. Taustalla on metsää ja peltoa." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-4-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Kokonaisvoima muuttaa nopeutta
Luvussa *Vuorovaikutus ja voima: Newtonin ensimmäinen ja kolmas laki* opit, että kappaleen nopeus pysyy muuttumattomana, kun siihen vaikuttavat voimat kumoavat toisensa. Kappale on silloin levossa tai liikkuu tasaisella nopeudella suoraan. Kun voimat eivät kumoa toisiaan, nopeus muuttuu: kappale kiihtyy, hidastuu tai kääntyy. Ratkaisevaa ei ole mikään yksittäinen voima vaan kaikkien kappaleeseen vaikuttavien voimien yhteisvaikutus eli **kokonaisvoima** $\Sigma\overline{F}$. Se on voimien vektorisumma eikä yksi voima lisää.

Kuvan vasemmalla laatikko lepää lattialla. Paino $\overline{G}$ ja lattian tukivoima $\overline{N}$ ovat yhtä suuret ja vastakkaiset, joten kokonaisvoima on nolla. Oikealla laatikkoa vedetään narulla. Pystysuorat voimat kumoavat edelleen toisensa, mutta vaakasuunnassa narun jännitysvoima $\overline{T}$ on suurempi kuin lattian kitkavoima $\overline{F}_\mu$. Kokonaisvoima osoittaa oikealle, ja laatikko kiihtyy oikealle.

<svg data-fig="kokonaisvoima" viewBox="0 0 600 420" role="img" aria-label="Kaksi tilannetta. Vasemmalla laatikko lepää lattialla. Sen voimakuviossa laatikko on suorakulmio: paino G keskipisteestä alas ja lattian tukivoima N alapinnasta ylös, yhtä pitkinä. Oikealla samaa laatikkoa vedetään narulla vaakasuoraan oikealle, ja tilannekuvassa laatikon yllä on oranssi kiihtyvyysnuoli oikealle. Sen voimakuviossa on paino ja tukivoima yhtä pitkinä, narun jännitysvoima T oikealle ja lattian kitkavoima alapinnan takakulmasta vasemmalle, kolmasosa jännitysvoiman pituudesta. Erillään on vihreä ontto nuoli, kokonaisvoima, oikealle: jännitysvoiman ja kitkan erotus. Nuolet ovat mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-4-kokonaisvoima.webp" x="0" y="0" width="600" height="425" preserveAspectRatio="none"/>
  <foreignObject x="102.5" y="5.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{levossa}$</div></foreignObject>
  <foreignObject x="153.5" y="326" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="170.5" y="209" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="396" y="5.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{vedetään}$</div></foreignObject>
  <foreignObject x="423.5" y="326" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="440.5" y="209" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="530.5" y="253.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="333.5" y="301.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="437.5" y="33.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="513.5" y="345.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\Sigma\overline{F}$</div></foreignObject>
</svg>

```pysahdy
Laatikkoa vedetään narulla oikealle, ja se kiihtyy. Mitä tästä voi päätellä vaakasuuntaisista voimista?
---
Narun voima on suurempi kuin kitka, joten vaakasuuntainen kokonaisvoima ei ole nolla vaan osoittaa oikealle.
```

### Massa vastustaa nopeuden muutosta
Mittaukset kärryllä paljastavat kaksi säännönmukaisuutta. Kun kokonaisvoima kaksinkertaistuu, kiihtyvyys kaksinkertaistuu: kiihtyvyys on suoraan verrannollinen kokonaisvoimaan. Kun sama kokonaisvoima vaikuttaa kaksi kertaa massiivisempaan kärryyn, kiihtyvyys puolittuu. Massa kertoo siis kappaleen hitaudesta eli siitä, kuinka vaikeaa sen nopeutta on muuttaa. Kuvaajassa kumpikin massa antaa origon kautta kulkevan suoran, ja raskaamman kärryn suora on puolet loivempi.

<svg data-fig="kuvaaja" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja mittakaavassa: vaaka-akselilla kokonaisvoima newtoneina 0–3, pystyakselilla kiihtyvyys 0–6 metriä sekunnin neliölle. Kaksi suoraa origon kautta, kummallakin kolme pistettä. Massalla 0,50 kilogrammaa pisteet ovat 1 N ja 2, 2 N ja 4 sekä 3 N ja 6. Massalla 1,0 kilogrammaa pisteet ovat 1 N ja 1, 2 N ja 2 sekä 3 N ja 3. Katkoviivat näyttävät, että kokonaisvoimalla 2 N kevyemmän kärryn kiihtyvyys on 4 ja raskaamman 2." style="max-width:100%;font-size:24px">
  <line x1="138.5" y1="300" x2="138.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186.5" y1="300" x2="186.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="235" y1="300" x2="235" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="283.5" y1="300" x2="283.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="331.5" y1="300" x2="331.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="300" x2="380" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="261.5" x2="380" y2="261.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="223.5" x2="380" y2="223.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="185" x2="380" y2="185" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="146.5" x2="380" y2="146.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="108.5" x2="380" y2="108.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="70" x2="380" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="300" x2="394" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M406,300 L393,306 L393,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="301" x2="90" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,44 L96,57 L84,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="138.5" y1="300" x2="138.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="186.5" y1="300" x2="186.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="235" y1="300" x2="235" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="283.5" y1="300" x2="283.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="273.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="331.5" y1="300" x2="331.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="380" y1="300" x2="380" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="370" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="83" y1="261.5" x2="90" y2="261.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="247" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="83" y1="223.5" x2="90" y2="223.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="209" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="83" y1="185" x2="90" y2="185" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="170.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="83" y1="146.5" x2="90" y2="146.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="132" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="83" y1="108.5" x2="90" y2="108.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="94" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="83" y1="70" x2="90" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="55.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <foreignObject x="60" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="412" y="285.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Sigma F\ (\text{N})$</div></foreignObject>
  <foreignObject x="80" y="13.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$a\ (\text{m/s}^2)$</div></foreignObject>
  <line x1="283.5" y1="146.5" x2="283.5" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="90" y1="146.5" x2="283.5" y2="146.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="283.5" y1="223.5" x2="283.5" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="90" y1="223.5" x2="283.5" y2="223.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="90,300 380,70" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="90,300 380,185" fill="none" stroke="#b8622d" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="186.5" cy="223.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="186.5" cy="261.5" r="6.5" fill="#b8622d" stroke="#ffffff" stroke-width="2"/>
  <circle cx="283.5" cy="146.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="283.5" cy="223.5" r="6.5" fill="#b8622d" stroke="#ffffff" stroke-width="2"/>
  <circle cx="380" cy="70" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="380" cy="185" r="6.5" fill="#b8622d" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="394" y="55.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 0{,}50\,\text{kg}$</div></foreignObject>
  <foreignObject x="394" y="170.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#b8622d">$m = 1{,}0\,\text{kg}$</div></foreignObject>
</svg>

Tästä saadaan vastaus alun kysymykseen. Moottori pyörittää vetäviä pyöriä, ja tie työntää renkaita eteenpäin. Kun tämä voima on yhtä suuri lastatussa ja tyhjässä autossa, lastatun auton paljon suurempi massa tekee kiihtyvyydestä pienen. Lastin paino ei sinänsä vedä autoa taaksepäin, koska tien tukivoima kumoaa sen. Raskas lasti kasvattaa kyllä renkaiden vierimisvastusta, mutta pääsyy hitaaseen kiihtymiseen on suuri massa.

```pysahdy
Sama kokonaisvoima vaikuttaa tyhjään ja täyteen kauppakärryyn. Kumpi kiihtyy enemmän ja miksi?
---
Tyhjä kärry, koska sen massa on pienempi. Massa vastustaa nopeuden muutosta: kaksinkertainen massa puolittaa kiihtyvyyden.
```

## Kaava: Newtonin toinen laki
Newtonin toinen laki eli dynamiikan peruslaki kokoaa havainnot yhteen yhtälöön:
```kaavat
Newtonin 2. laki (dynamiikan peruslaki) :: \Sigma\overline{F} = m\overline{a}
```
missä $\Sigma\overline{F}$ on kappaleeseen vaikuttavien voimien vektorisumma eli kokonaisvoima ($\text{N}$), $m$ kappaleen massa ($\text{kg}$) ja $\overline{a}$ sen kiihtyvyys ($\text{m/s}^2$). Voiman yksikkö määritellään tästä laista: yksi newton on voima, joka antaa yhden kilogramman massalle kiihtyvyyden $1\,\text{m/s}^2$. Siis $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$.

### Kokonaisvoima osoittaa kiihtyvyyden suuntaan
Laki on vektoriyhtälö: kokonaisvoima ja kiihtyvyys osoittavat aina samaan suuntaan. Nopeuden suunta voi olla toinen. Kuvan nosturi kannattelee laatikkoa köydellä. Kun laatikko nousee kiihtyen, köyden voima on painoa suurempi ja kokonaisvoima osoittaa ylös. Kun laatikko nousee hidastuen, köyden voima on painoa pienempi: kokonaisvoima ja kiihtyvyys osoittavat alas, vaikka laatikko liikkuu yhä ylöspäin. Levossa ja tasaisessa nousussa köyden voima ja paino ovat yhtä suuret.

<svg data-fig="nosturi" viewBox="0 0 600 620" role="img" aria-label="Neljä tilannetta, joissa nosturin köysi kannattelee laatikkoa. Kussakin on vasemmalla tilannekuva ja oikealla laatikon voimakuvio, jossa laatikko on suorakulmio: paino G keskipisteestä alas ja köyden jännitysvoima T yläpinnasta ylös. Voimakuvion vieressä on sininen nopeusnuoli ja oranssi kiihtyvyysnuoli, kun ne eivät ole nollia. Vasemmalla ylhäällä laatikko on levossa, v ja a ovat nollia ja nuolet T ja G yhtä pitkät. Oikealla ylhäällä laatikko nousee tasaisella nopeudella: nopeus ylös, a on nolla ja nuolet yhtä pitkät. Vasemmalla alhaalla laatikko nousee kiihtyen: nopeus ja kiihtyvyys ylös, T pidempi kuin G. Oikealla alhaalla laatikko nousee hidastuen: nopeus ylös mutta kiihtyvyys alas, ja T on lyhyempi kuin G." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-4-nosturi.webp" x="1.2" y="1.2" width="597" height="618.2" preserveAspectRatio="none"/>
  <foreignObject x="102.5" y="7.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{levossa}$</div></foreignObject>
  <foreignObject x="185.5" y="249.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="185.5" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="224" y="135.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$v = 0$</div></foreignObject>
  <foreignObject x="224" y="185.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="346" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{nousee tasaisesti}$</div></foreignObject>
  <foreignObject x="485.5" y="249.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="485.5" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="519.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="524" y="229.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="58.5" y="317.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{nousee kiihtyen}$</div></foreignObject>
  <foreignObject x="185.5" y="559.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="185.5" y="369.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="219.5" y="415.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="255.5" y="431.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="352.5" y="317.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{nousee hidastuen}$</div></foreignObject>
  <foreignObject x="485.5" y="559.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="485.5" y="417.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="519.5" y="415.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="555.5" y="509.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

```pysahdy
Laatikko nousee köyden varassa ja hidastuu. Mihin suuntaan kokonaisvoima osoittaa?
---
Alaspäin, koska kiihtyvyys osoittaa alaspäin, vaikka laatikko liikkuu yhä ylöspäin. Köyden voima on painoa pienempi.
```

### Ensin voimat, sitten yhtälö
Kun lakia käytetään laskuun, edetään aina samassa järjestyksessä. Valitaan kappale ja piirretään sen voimakuvio, jossa jokaisella voimalla on aiheuttaja: Maa, köysi, alusta tai vetäjä. Valitaan positiivinen suunta, yleensä kiihtyvyyden suunta. Vasta sitten kirjoitetaan voimista kokonaisvoima etumerkkeineen ja asetetaan se yhtä suureksi kuin $ma$. Nosturin laatikolle, kun ylöspäin on positiivinen, saadaan $T - G = ma$. Luvussa *Voimakuvio ja voimien yhteisvaikutus* sama menetelmä laajenee vinoihin voimiin.

## Esimerkki
Rakennusnosturi nostaa betonielementtiä, jonka massa on $480\,\text{kg}$. Köyden jännitysvoima on $5{,}20\,\text{kN}$. Kuinka suuri on elementin kiihtyvyys, ja mihin suuntaan se osoittaa? Ilmanvastus jätetään huomiotta.

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 480\,\text{kg}$, $T = 5{,}20\,\text{kN}$ ja $g = 9{,}81\,\text{m/s}^2$.

Kysytään kiihtyvyyttä $a$ ja sen suuntaa.

<!-- vaihe -->

**Periaate.** Valitaan kappaleeksi betonielementti. Siihen vaikuttavat Maa (paino) ja köysi (jännitysvoima). Newtonin toisen lain mukaan kiihtyvyyden määrää näiden voimien summa. Köyden voima ei yksin kiihdytä elementtiä, koska suurin osa siitä kuluu painon kannattelemiseen.

<!-- vaihe -->

**Voimakuvio.** Elementti piirretään suorakulmiona. Paino $\overline{G}$ lähtee keskipisteestä alas, ja köyden jännitysvoima $\overline{T}$ lähtee yläpinnasta ylös. Positiivinen suunta valitaan ylös.

<svg data-fig="esimerkki" viewBox="0 0 600 360" role="img" aria-label="Betonielementin voimakuvio, elementti suorakulmiona. Köyden jännitysvoima T lähtee yläpinnasta ylös, ja paino G lähtee keskipisteestä alas. Nuoli T on vähän pidempi kuin nuoli G. Oikealla erillään oranssi kiihtyvyysnuoli ylös. Oikealla pieni nuoli y ylös: positiivinen suunta on ylös. Vasemmalla tilannekuva: nosturin koukku nostaa betonielementtiä köydellä." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy44-ex-elem" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <line x1="110" y1="20" x2="110" y2="138" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M110,138 q-14,5 -12,19 q5,12 17,7" fill="none" stroke="#6c757d" stroke-width="5" stroke-linejoin="round"/>
  <line x1="104" y1="168" x2="66" y2="200" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="116" y1="168" x2="154" y2="200" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="46" y="200" width="128" height="60" rx="2" fill="url(#fy44-ex-elem)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="46" y1="220" x2="174" y2="220" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="46" y1="240" x2="174" y2="240" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="8" y1="296" x2="212" y2="296" stroke="#a97a35" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="37.5" y="335.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="333.5" y="335.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <line x1="228" y1="20" x2="228" y2="340" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <rect x="285" y="165" width="110" height="50" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="340" y1="165" x2="340" y2="47" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M340,30 L348,48 L332,48 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="349.5" y="27.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <line x1="340" y1="190" x2="340" y2="295.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M340,312.5 L332,294.5 L348,294.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="349.5" y="292" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="470" y1="220" x2="470" y2="162" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M476.5,173 L470,160 L463.5,173" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="453.5" y="119.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <line x1="560" y1="300" x2="560" y2="245" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M560,236 L564.5,246 L555.5,246 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="550" y="203.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**Kaava ratkaistuna.** Lähdetään Newtonin toisesta laista $\Sigma F = ma$. Kuviosta kokonaisvoima on $T - mg$, ja kiihtyvyys ratkaistaan:
```latex
\begin{aligned}
&\Sigma F = ma \\
&T - mg = ma \\
&a = \frac{T - mg}{m}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Jännitysvoima muunnetaan newtoneiksi: $5{,}20\,\text{kN} = 5{,}20\cdot 1000\,\text{N} = 5200\,\text{N}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin paino ja sitten kiihtyvyys:
```latex
\begin{aligned}
&a = \frac{T - mg}{m} \\
&mg = 480\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 \\
&\phantom{mg} = 4708{,}8\,\text{N} \\
&a = \frac{5200\,\text{N} - 4708{,}8\,\text{N}}{480\,\text{kg}} \\
&\phantom{a} \approx 1{,}02\,\text{m/s}^2
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kiihtyvyys on $a \approx 1{,}02\,\text{m/s}^2$ ylöspäin. Kaikissa lähtöarvoissa on kolme merkitsevää numeroa: massa $480\,\text{kg}$, jännitysvoima $5{,}20\,\text{kN}$ ja putoamiskiihtyvyys $9{,}81\,\text{m/s}^2$. Siksi tuloksessakin on kolme merkitsevää numeroa.

<!-- vaihe -->

**Järkevyys.** Köyden voima on vain noin kymmenen prosenttia suurempi kuin paino $4{,}71\,\text{kN}$, joten kiihtyvyydenkin pitää olla noin kymmenesosa putoamiskiihtyvyydestä: $0{,}1\cdot 9{,}81\,\text{m/s}^2 \approx 1\,\text{m/s}^2$. Jos painon unohtaisi, tulos olisi $5200\,\text{N} : 480\,\text{kg} \approx 10{,}8\,\text{m/s}^2$. Se olisi väärin, koska elementtiin vaikuttaa köyden voiman lisäksi paino alaspäin, ja kiihtyvyyden määrää näiden voimien summa.

Esimerkiksi tasaisella nopeudella nousevaa elementtiä köysi vetää painon suuruisella voimalla, ja voimat kumoavat toisensa, mutta painon unohtava lasku antaisi kiihtyvyydeksi silloinkin noin $9{,}8\,\text{m/s}^2$.

## Yleinen virhekäsitys
Moni ajattelee, että liikkeen suuntaan vaikuttaa aina voima ja että kokonaisvoima osoittaa liikkeen suuntaan. Kokonaisvoima osoittaa kuitenkin kiihtyvyyden suuntaan. Kun ilmanvastus jätetään huomiotta, ylöspäin heitetty pallo nousee, vaikka siihen vaikuttaa vain alaspäin osoittava paino, ja siksi se hidastuu. Hidastuvassa liikkeessä kokonaisvoima osoittaa nopeutta vastaan. Toinen virhe on ajatella, että vakiovoima pitää yllä vakionopeutta. Kun kokonaisvoima on vakio eikä nolla, nopeus muuttuu tasaisesti. Kolmas virhe on sekoittaa massa ja paino. Vaakasuoralla radalla paino ei vastusta liikettä, koska tukivoima kumoaa sen: kiihtyvyyttä pienentää massa.

## Tiivistelmä
- Kun kokonaisvoima on nolla, nopeus ei muutu. Kun se ei ole nolla, kappale kiihtyy kokonaisvoiman suuntaan.
- Newtonin toinen laki on $\Sigma\overline{F} = m\overline{a}$. Kiihtyvyys on suoraan verrannollinen kokonaisvoimaan ja kääntäen verrannollinen massaan.
- Kokonaisvoima osoittaa kiihtyvyyden suuntaan, joka ei aina ole nopeuden suunta: hidastuvassa liikkeessä se on nopeutta vastaan.
- Ensin piirretään voimakuvio ja valitaan positiivinen suunta, sitten kirjoitetaan $\Sigma F = ma$ etumerkkeineen.
- Voiman yksikkö on $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$.
