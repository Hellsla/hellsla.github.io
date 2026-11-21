# Ilmanvastus ja putoaminen ilmassa

> **Miksi** laskuvarjohyppääjän nopeus lakkaa kasvamasta, vaikka paino vetää häntä alas koko pudotuksen ajan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: korkealla peltojen, metsien ja järven yläpuolella kaksi laskuvarjohyppääjää. Vasemmalla ylempänä hyppääjä putoaa vatsa alaspäin kädet ja jalat levällään, ja hänen yläpuolellaan näkyvät ilmavirran viivat. Oikealla alempana toinen hyppääjä leijuu hitaasti avatun laskuvarjon alla. Taivaan yläreunassa lentokone, josta he hyppäsivät." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-14-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Ilma vastustaa liikettä
Kun kappale liikkuu ilmassa tai vedessä, sen on työnnettävä väliainetta tieltään. Väliaine työntää kappaletta takaisin: kappaleeseen vaikuttaa **väliaineen vastus**, ilmassa **ilmanvastus** $\overline{F}_\text{v}$. Se osoittaa kappaleen nopeutta vastaan, kun ilma on tyyntä. Luvussa *Paino, kitka ja kalteva taso* kitka vastusti liukumista alustaa pitkin. Ilmanvastus on samanlainen vastusvoima, mutta sen aiheuttaja on ympäröivä ilma, eikä kappaleen tarvitse koskettaa mitään kiinteää pintaa. Pyörällä ja autolla on lisäksi **vierimisvastus** $\overline{F}_\text{r}$, renkaiden ja tien aiheuttama vastus, joka on eri voima kuin ilmanvastus.

<figure class="unit-photo"><img src="pics/fy4/epic-parachute-test.webp" alt="Valkoinen pyöreä laskuvarjo sinisellä taivaalla, ja pitkän narun päässä roikkuu pieni metallinen koekappale."><figcaption>NASAn EPIC-koe Kaliforniassa kesäkuussa 2025: drooni pudotti mittalaittein varustetun laskuvarjon ja sen kuorman. Kuvassa ei ole ihmistä, vaan koekappale.</figcaption></figure>

Liukukitkasta ilmanvastus eroaa siinä, että se riippuu nopeudesta. Ilman suhteen paikallaan olevaan kappaleeseen ilmanvastus ei vaikuta lainkaan, ja se kasvaa nopeasti, kun kappaleen nopeus ilman suhteen kasvaa. Samalla nopeudella ilmanvastus on sitä suurempi, mitä suurempi on kappaleen poikkipinta-ala ja mitä huonommin ilma pääsee virtaamaan sen ohi. Samalla nopeudella vastus on vedessä paljon suurempi kuin ilmassa, koska vesi on tiheämpää.

```pysahdy
Hyppääjä lähtee ilman suhteen levosta, vaikka hänen ympärillään on ilmaa. Miksi ilmanvastusta ei ole heti hypyn jälkeen?
---
Ilmanvastus riippuu nopeudesta ilman suhteen, ja heti hypyn jälkeen nopeus on nolla. Vasta nopeuden kasvaessa ilma alkaa vastustaa liikettä.
```

### Pudotuksen kolme vaihetta
Hyppääjä lähtee ilman suhteen levosta (koneen vauhti jätetään huomiotta), joten heti hypyn jälkeen ilmanvastusta ei vielä ole. Ainoa voima on paino, ja hyppääjä kiihtyy alaspäin putoamiskiihtyvyydellä $g$. Nopeuden kasvaessa ilmanvastus kasvaa. Paino pysyy samana, joten kokonaisvoima pienenee, ja samalla pienenee kiihtyvyys: nopeus kasvaa yhä hitaammin. Lopulta ilmanvastus on yhtä suuri kuin paino. Silloin kokonaisvoima on nolla, kiihtyvyys on nolla ja nopeus pysyy vakiona, kuten Newtonin ensimmäinen laki sanoo. Tätä nopeutta sanotaan **rajanopeudeksi**.

<svg data-fig="pudotus" viewBox="0 0 600 450" role="img" aria-label="Kolme vaihetta laskuvarjohyppääjän pudotuksesta vatsa alaspäin, mittakaavassa. Ylhäällä tilannekuvat ja alhaalla voimakuviot, joissa hyppääjä on suorakulmio. Vasemmalla heti hypyn jälkeen: hyppääjä lähtee ilman suhteen levosta, nopeus on nolla, voimakuviossa on vain paino G keskipisteestä alas, ja oranssi kiihtyvyysnuoli osoittaa alas. Keskellä hyppääjä kiihtyy: sininen nopeusnuoli alas, paino G alas ja ilmanvastus F_v alhaalta ylös alapintaan asti, puolet painon pituudesta, ja kiihtyvyysnuoli on lyhyempi. Oikealla rajanopeus: pitkä nopeusnuoli alas, ilmanvastus yhtä pitkä kuin paino, ja kiihtyvyys on nolla." style="max-width:100%;font-size:30px">
  <image href="pics/fy4/fy4-14-pudotus.webp" x="0" y="0" width="600" height="457.5" preserveAspectRatio="none"/>
  <foreignObject x="58.5" y="7.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{alussa}$</div></foreignObject>
  <foreignObject x="72.5" y="130" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#6b7480">$v = 0$</div></foreignObject>
  <foreignObject x="94.5" y="336" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="148.5" y="308" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="65" y="406" width="70" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$F_\text{v} = 0$</div></foreignObject>
  <foreignObject x="252.5" y="7.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kiihtyy}$</div></foreignObject>
  <foreignObject x="368" y="75" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="294.5" y="336" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="218.5" y="310" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="348.5" y="288" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="265" y="406" width="70" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$F_\text{v} < G$</div></foreignObject>
  <foreignObject x="433.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rajanopeus}$</div></foreignObject>
  <foreignObject x="568" y="92" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="494.5" y="336" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="418.5" y="357" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="522.5" y="196" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="465" y="406" width="70" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">$F_\text{v} = G$</div></foreignObject>
</svg>

```pysahdy
Hyppääjä putoaa rajanopeudella. Miksi hänen nopeutensa ei silloin enää muutu, vaikka paino vetää häntä yhä alas?
---
Ilmanvastus on yhtä suuri kuin paino, joten kokonaisvoima ja kiihtyvyys ovat nolla. Nopeus pysyy vakiona.
```

### Rajanopeus riippuu massasta ja muodosta
Rajanopeudella ilmanvastus on yhtä suuri kuin paino. Raskaamman hyppääjän paino on suurempi, joten hänen nopeutensa ehtii kasvaa suuremmaksi ennen kuin ilmanvastus kasvaa painon suuruiseksi. Kuvaajassa samassa asennossa putoavien $60\,\text{kg}$:n ja $100\,\text{kg}$:n hyppääjien käyrät alkavat yhtä jyrkkinä, mutta ne tasaantuvat eri nopeuksiin, mallin arvoina noin $48\,\text{m/s}$:iin ja $61\,\text{m/s}$:iin. Pää edellä sukeltavan hyppääjän poikkipinta-ala on pienempi ja muoto virtaviivaisempi, joten hänen rajanopeutensa on suurempi.

<svg data-fig="vt" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja mittakaavassa, simulaation mallin arvoja: vaaka-akselilla aika 0–30 sekuntia, pystyakselilla nopeus 0–70 metriä sekunnissa. Katkoviivana suora, joka nousee jyrkästi: nopeus ilman ilmanvastusta, 49 metriä sekunnissa viiden sekunnin kohdalla. Kaksi käyrää alkaa samalla jyrkkyydellä mutta loivenee ja tasaantuu vaakasuoraksi: 60 kilogramman hyppääjän nopeus noin 48 metriin sekunnissa ja 100 kilogramman hyppääjän noin 61 metriin sekunnissa." style="max-width:100%;font-size:24px">
  <line x1="146.5" y1="304" x2="146.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="203.5" y1="304" x2="203.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="260" y1="304" x2="260" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="316.5" y1="304" x2="316.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="373.5" y1="304" x2="373.5" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="304" x2="430" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="270" x2="430" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="236" x2="430" y2="236" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="202" x2="430" y2="202" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="168" x2="430" y2="168" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="134" x2="430" y2="134" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="100" x2="430" y2="100" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="66" x2="430" y2="66" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="304" x2="444" y2="304" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M456,304 L443,310 L443,298 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="305" x2="90" y2="52" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,40 L96,53 L84,53 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="146.5" y1="304" x2="146.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="136.5" y="313.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="203.5" y1="304" x2="203.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="187" y="313.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="260" y1="304" x2="260" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="243.5" y="313.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="316.5" y1="304" x2="316.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="300" y="313.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="373.5" y1="304" x2="373.5" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="357" y="313.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$25$</div></foreignObject>
  <line x1="430" y1="304" x2="430" y2="311" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="413.5" y="313.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="83" y1="270" x2="90" y2="270" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="83" y1="236" x2="90" y2="236" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="221.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="83" y1="202" x2="90" y2="202" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="187.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="83" y1="168" x2="90" y2="168" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="153.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="83" y1="134" x2="90" y2="134" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="119.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="83" y1="100" x2="90" y2="100" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="85.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="83" y1="66" x2="90" y2="66" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="51.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$70$</div></foreignObject>
  <foreignObject x="60" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="462" y="289.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="80" y="9.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\text{m/s})$</div></foreignObject>
  <polyline points="90,304 171,66" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <foreignObject x="181" y="58.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{ilman ilmanvastusta}$</div></foreignObject>
  <polyline points="90,304 93,295.5 95.5,287.5 98.5,279 101.5,271 104,263 107,255 110,247 112.5,239.5 115.5,232 118.5,225 121,218 124,211 127,204.5 129.5,198 132.5,192 135.5,186 138,180.5 141,175.5 144,170.5 146.5,165.5 149.5,161 152.5,156.5 155,152.5 158,148.5 161,145 163.5,141.5 166.5,138.5 169.5,135.5 172,132.5 175,130 178,127.5 180.5,125.5 183.5,123 186.5,121 189,119 192,117.5 195,116 197.5,114.5 200.5,113 203.5,111.5 206,110.5 209,109.5 212,108 214.5,107 217.5,106.5 220.5,105.5 223,104.5 226,104 229,103.5 231.5,102.5 234.5,102 237.5,101.5 240,101 243,100.5 246,100.5 248.5,100 251.5,99.5 254.5,99 257,99 260,98.5 263,98.5 265.5,98 268.5,98 271.5,97.5 274,97.5 277,97.5 280,97 282.5,97 285.5,97 288.5,96.5 291,96.5 294,96.5 297,96.5 299.5,96.5 302.5,96 305.5,96 308,96 311,96 314,96 316.5,96 319.5,96 322.5,96 325,95.5 328,95.5 331,95.5 333.5,95.5 336.5,95.5 339.5,95.5 342,95.5 345,95.5 348,95.5 350.5,95.5 353.5,95.5 356.5,95.5 359,95.5 362,95.5 365,95.5 367.5,95.5 370.5,95.5 373.5,95.5 376,95.5 379,95.5 382,95.5 384.5,95.5 387.5,95 390.5,95 393,95 396,95 399,95 401.5,95 404.5,95 407.5,95 410,95 413,95 416,95 418.5,95 421.5,95 424.5,95 427,95 430,95" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="442" y="80.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 100\,\text{kg}$</div></foreignObject>
  <polyline points="90,304 93,295.5 95.5,287.5 98.5,279 101.5,271 104,263 107,255.5 110,248 112.5,241 115.5,234 118.5,227.5 121,221 124,215 127,209.5 129.5,204 132.5,199 135.5,194.5 138,190 141,186 144,182 146.5,178.5 149.5,175.5 152.5,172.5 155,170 158,167.5 161,165 163.5,163 166.5,161 169.5,159.5 172,157.5 175,156.5 178,155 180.5,153.5 183.5,152.5 186.5,151.5 189,151 192,150 195,149 197.5,148.5 200.5,148 203.5,147.5 206,147 209,146.5 212,146 214.5,145.5 217.5,145.5 220.5,145 223,145 226,144.5 229,144.5 231.5,144 234.5,144 237.5,143.5 240,143.5 243,143.5 246,143.5 248.5,143 251.5,143 254.5,143 257,143 260,143 263,143 265.5,143 268.5,142.5 271.5,142.5 274,142.5 277,142.5 280,142.5 282.5,142.5 285.5,142.5 288.5,142.5 291,142.5 294,142.5 297,142.5 299.5,142.5 302.5,142.5 305.5,142.5 308,142.5 311,142.5 314,142.5 316.5,142.5 319.5,142.5 322.5,142.5 325,142.5 328,142.5 331,142.5 333.5,142.5 336.5,142.5 339.5,142.5 342,142.5 345,142.5 348,142.5 350.5,142.5 353.5,142.5 356.5,142 359,142 362,142 365,142 367.5,142 370.5,142 373.5,142 376,142 379,142 382,142 384.5,142 387.5,142 390.5,142 393,142 396,142 399,142 401.5,142 404.5,142 407.5,142 410,142 413,142 416,142 418.5,142 421.5,142 424.5,142 427,142 430,142" fill="none" stroke="#b8622d" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="442" y="127.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#b8622d">$m = 60\,\text{kg}$</div></foreignObject>
</svg>

Tästä saadaan vastaus alun kysymykseen. Paino vetää hyppääjää alas koko ajan, mutta nopeuden kasvaessa ilmanvastus kasvaa, kunnes se kumoaa painon. Sen jälkeen nopeus ei enää muutu. Ilman ilmanvastusta kaikki kappaleet putoaisivat samalla kiihtyvyydellä $g$. Ilmassa kevyt ja laaja kappale, kuten paperiarkki tai sulka, saavuttaa pienen rajanopeuden hyvin pian ja putoaa siksi hitaasti.

```pysahdy
Miksi paperiarkki putoaa ilmassa hitaammin kuin saman painoinen, kokoon rutistettu paperipallo?
---
Laaja arkki saa samalla nopeudella suuremman ilmanvastuksen, joten ilmanvastus kasvaa painon suuruiseksi jo pienellä nopeudella. Arkin rajanopeus on siksi pienempi.
```

## Kaava: Liikeyhtälö ilmanvastuksen kanssa
Ilmanvastus on yksi kappaleeseen vaikuttavista voimista, joten liike noudattaa Newtonin toista lakia. Ilmassa putoavaan tai nousevaan kappaleeseen vaikuttavat paino ja ilmanvastus:
```latex
\overline{G} + \overline{F}_\text{v} = m\overline{a}
```
missä $\overline{G}$ on kappaleen paino ($\text{N}$), $\overline{F}_\text{v}$ ilmanvastus ($\text{N}$), $m$ kappaleen massa ($\text{kg}$) ja $\overline{a}$ sen kiihtyvyys ($\text{m/s}^2$). Tässä luvussa ilmanvastuksen suuruutta ei lasketa nopeudesta, vaan se annetaan tai päätellään liikkeestä: rajanopeudella $F_\text{v} = G$.

### Putoava ja nouseva kappale
Kuten aina, ensin valitaan kappale, piirretään sen voimakuvio ja valitaan positiivinen suunta, ja vasta sitten kirjoitetaan yhtälö. Putoavan kappaleen ilmanvastus osoittaa ylös, painoa vastaan. Kun positiivinen suunta on alas, $mg - F_\text{v} = ma$, joten kiihtyvyys on pienempi kuin $g$. Ylöspäin heitetyn pallon ilmanvastus osoittaa alas, samaan suuntaan kuin paino. Kun positiivinen suunta on ylös, $-mg - F_\text{v} = ma$. Kiihtyvyyden suuruus on silloin suurempi kuin $g$, ja nouseva pallo hidastuu nopeammin kuin ilman ilmanvastusta.

<svg data-fig="ylos" viewBox="0 0 600 430" role="img" aria-label="Kaksi tilannetta, mittakaavassa: suoraan ylös heitetty pallo, kun ilmanvastusta ei jätetä huomiotta. Ylhäällä tilannekuvat ja alhaalla voimakuviot, joissa pallo on suorakulmio. Vasemmalla pallo nousee: sininen nopeusnuoli ylös. Voimakuviossa paino G keskipisteestä alas ja ilmanvastus F_v yläpinnasta alas. Erillään vihreä ontto kokonaisvoiman nuoli alas, painoa pidempi, ja oranssi kiihtyvyysnuoli alas. Oikealla pallo putoaa takaisin: nopeusnuoli alas. Voimakuviossa paino alas ja ilmanvastus alapinnasta ylös. Kokonaisvoiman nuoli alas on painoa lyhyempi, ja kiihtyvyysnuoli on lyhyempi kuin vasemmalla." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-14-ylos.webp" x="0" y="1.2" width="600" height="438.8" preserveAspectRatio="none"/>
  <foreignObject x="108.5" y="7.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{nousee}$</div></foreignObject>
  <foreignObject x="188" y="80.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="125.5" y="314" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="49.5" y="185.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="203.5" y="226.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="239.5" y="390" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\Sigma\overline{F}$</div></foreignObject>
  <foreignObject x="408.5" y="7.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{putoaa}$</div></foreignObject>
  <foreignObject x="488" y="80.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="425.5" y="314" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="349.5" y="289.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="503.5" y="207.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="539.5" y="326" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\Sigma\overline{F}$</div></foreignObject>
</svg>

### Kun laskuvarjo aukeaa
Laskuvarjon suuri pinta-ala kasvattaa ilmanvastuksen moninkertaiseksi. Varjon auetessa hyppääjä liikkuu vielä rajanopeudella alaspäin, joten ilmanvastus on hetken monta kertaa painon suuruinen. Kokonaisvoima ja kiihtyvyys osoittavat ylös, vaikka hyppääjä liikkuu alas: hyppääjä hidastuu mutta ei nouse. Nopeuden pienentyessä ilmanvastus pienenee, kunnes se uudella, pienellä rajanopeudella on taas yhtä suuri kuin paino. Kuinka monta kertaa painon suuruinen ilmanvastus on, riippuu varjosta ja hetkestä: kuviossa se on kolminkertainen, esimerkissä lähes kolminkertainen ja simulaation mallissa suurimmillaan noin viisinkertainen. Kokonaisvoiman suunta voi siis erota liikkeen suunnasta. Se kertoo aina kiihtyvyyden suunnan, ei nopeuden.

<svg data-fig="varjo" viewBox="0 0 600 500" role="img" aria-label="Kolme vaihetta, kun laskuvarjo avataan, voimat mittakaavassa. Ylhäällä tilannekuvat ja alhaalla hyppääjän voimakuviot, joissa hyppääjä varjoineen on suorakulmio. Vasemmalla putoaminen ennen varjon avaamista rajanopeudella: pitkä sininen nopeusnuoli alas, paino G keskipisteestä alas ja ilmanvastus F_v alhaalta ylös alapintaan asti, yhtä pitkinä, kiihtyvyys nolla. Keskellä varjo aukeaa: nopeusnuoli osoittaa yhä alas, ilmanvastus lähtee yläpinnasta ylös ja on kolme kertaa painon pituinen. Erillään vihreä ontto kokonaisvoiman nuoli ylös ja oranssi kiihtyvyysnuoli ylös. Oikealla varjo on auki: lyhyt nopeusnuoli alas, ilmanvastus yläpinnasta ylös yhtä pitkänä kuin paino, kiihtyvyys nolla." style="max-width:100%;font-size:30px">
  <image href="pics/fy4/fy4-14-varjo.webp" x="0" y="0" width="600" height="506.2" preserveAspectRatio="none"/>
  <foreignObject x="33.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rajanopeus}$</div></foreignObject>
  <foreignObject x="168" y="98" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="88.5" y="399" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="12.5" y="420" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="132.5" y="354" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#6b7480">$a = 0$</div></foreignObject>
  <foreignObject x="227.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{varjo aukeaa}$</div></foreignObject>
  <foreignObject x="368" y="87" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="288.5" y="399" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="212.5" y="205.5" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="346.5" y="252" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="350.5" y="338" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#2b8a3e">$\Sigma\overline{F}$</div></foreignObject>
  <foreignObject x="408.5" y="7.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{uusi rajanopeus}$</div></foreignObject>
  <foreignObject x="568" y="60" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:30px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="488.5" y="399" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="412.5" y="300" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <foreignObject x="532.5" y="354" width="55" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#6b7480">$a = 0$</div></foreignObject>
</svg>

## Esimerkki
Laskuvarjohyppääjä, jonka massa varusteineen on $85{,}0\,\text{kg}$, avaa varjonsa. Eräällä hetkellä varjon auetessa ilmanvastus on $2{,}40\,\text{kN}$, ja hyppääjä liikkuu yhä alaspäin. Kuinka suuri on hyppääjän kiihtyvyys tällä hetkellä, ja mihin suuntaan se osoittaa?

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 85{,}0\,\text{kg}$, $F_\text{v} = 2{,}40\,\text{kN}$ ja $g = 9{,}81\,\text{m/s}^2$.

Kysytään kiihtyvyyttä $a$ ja sen suuntaa.

<!-- vaihe -->

**Periaate.** Valitaan kappaleeksi hyppääjä varusteineen ja varjoineen. Siihen vaikuttavat Maa (paino) ja ilma (ilmanvastus). Newtonin toisen lain mukaan kiihtyvyyden määrää näiden voimien summa; nopeuden suunta ei ratkaise kiihtyvyyden suuntaa.

<!-- vaihe -->

**Kaava ratkaistuna.** Voimakuviossa hyppääjä on suorakulmio. Paino $\overline{G}$ lähtee keskipisteestä alas. Ilmanvastus $\overline{F}_\text{v}$ vaikuttaa pääosin varjoon, joten se lähtee yläpinnasta ylös. Positiivinen suunta valitaan alas, liikkeen suuntaan.

<svg data-fig="esimerkki" viewBox="0 0 600 380" role="img" aria-label="Vasemmalla tilannekuva: hyppääjän laskuvarjo on aukeamassa, ja hyppääjän vieressä sininen nopeusnuoli osoittaa alas. Oikealla hyppääjän voimakuvio, hyppääjä varjoineen suorakulmiona: paino G keskipisteestä alas ja ilmanvastus F_v yläpinnasta ylös, lähes kolme kertaa painon pituisena. Erillään oranssi kiihtyvyysnuoli ylös. Oikealla pieni nuoli y alas: positiivinen suunta on alas." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy414-ex-c" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <line x1="100.5" y1="191.5" x2="71.5" y2="136.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="106" y1="191.5" x2="94.5" y2="136.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="114" y1="191.5" x2="125.5" y2="136.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="119.5" y1="191.5" x2="148.5" y2="136.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M67,136.5 Q67,106 110,106 Q153,106 153,136.5 Z" fill="url(#fy414-ex-c)" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="81.5" y1="136.5" x2="81.5" y2="124" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="136.5" x2="96" y2="115.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="136.5" x2="110" y2="112" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="124" y1="136.5" x2="124" y2="115.5" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="138.5" y1="136.5" x2="138.5" y2="124" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <g transform="translate(110,220) scale(0.95)">
  <path d="M-5,12 L-7,40" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M5,12 L7,40" fill="none" stroke="#2b8a3e" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.6"/>
  <rect x="-11" y="-18" width="22" height="34" rx="7" fill="#2b8a3e" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="-8" y="-16" width="16" height="14" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M-11,-12 L-18,-34" fill="none" stroke="#2b8a3e" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M11,-12 L18,-34" fill="none" stroke="#2b8a3e" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="0" cy="-28" r="10" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <path d="M-10,-28 A10,10 0 0 1 10,-28 Z" fill="#1f2933" stroke-linejoin="round"/>
  </g>
  <line x1="180" y1="200" x2="180" y2="278" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M173.5,267 L180,280 L186.5,267" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="198" y="225.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="27.5" y="341.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="333.5" y="341.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <line x1="232" y1="20" x2="232" y2="340" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <rect x="315" y="208" width="90" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="342" y1="208" x2="342" y2="81" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M342,64 L350,82 L334,82 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="285.5" y="61.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{v}$</div></foreignObject>
  <line x1="360" y1="230" x2="360" y2="263" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M360,280 L352,262 L368,262 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="367.5" y="261.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="470" y1="250" x2="470" y2="182" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M476.5,193 L470,180 L463.5,193" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="453.5" y="139.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <line x1="560" y1="200" x2="560" y2="257" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M560,266 L555.5,256 L564.5,256 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="550" y="269.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

Kuviosta kirjoitetaan kokonaisvoima $mg - F_\text{v}$ ja ratkaistaan kiihtyvyys:
```latex
\begin{aligned}
&mg - F_\text{v} = ma \\
&a = \frac{mg - F_\text{v}}{m}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ilmanvastus muunnetaan newtoneiksi: $2{,}40\,\text{kN} = 2{,}40\cdot 1000\,\text{N} = 2400\,\text{N}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin paino ja sitten kiihtyvyys:
```latex
\begin{aligned}
&a = \frac{mg - F_\text{v}}{m} \\
&mg = 85{,}0\,\text{kg}\cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \\
&\phantom{mg} = 833{,}85\,\text{N} \\
&a = \frac{833{,}85\,\text{N} - 2400\,\text{N}}{85{,}0\,\text{kg}} \\
&\phantom{a} \approx -18{,}4\,\text{m/s}^2
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kiihtyvyys on negatiivinen, joten se osoittaa ylös, vastakkaiseen suuntaan kuin positiiviseksi valittu suunta. Kiihtyvyyden suuruus on $18{,}4\,\text{m/s}^2$ ylöspäin, kolmen merkitsevän numeron tarkkuudella kuten massassa $85{,}0\,\text{kg}$ ja ilmanvastuksessa $2{,}40\,\text{kN}$. Hyppääjä liikkuu alas, mutta hänen nopeutensa pienenee.

<!-- vaihe -->

**Järkevyys.** Ilmanvastus on lähes kolme kertaa paino $834\,\text{N}$, joten ylöspäin jää noin kaksi painon verran kokonaisvoimaa. Kiihtyvyyden pitää siis olla noin kaksi kertaa $g$ eli noin $20\,\text{m/s}^2$, ja tulos $18{,}4\,\text{m/s}^2$ sopii tähän. Varjon avautuminen tuntuu hyppääjästä voimakkaana nykäyksenä, mutta se kestää vain muutaman sekunnin.

## Yleinen virhekäsitys
Videoilla hyppääjä näyttää nousevan ylöspäin, kun hänen varjonsa aukeaa. Videokuvaaja putoaa itse vielä ilman varjoa, ja hyppääjä vain hidastuu videokuvaajaan nähden. Maahan nähden hyppääjä liikkuu koko ajan alaspäin: kokonaisvoima osoittaa hetken ylös, mutta se pienentää nopeutta eikä käännä liikettä. Toinen virhe on ajatella, että rajanopeudella ilmanvastus on painoa suurempi tai ettei voimia enää ole. Rajanopeudella voimat ovat yhtä suuret ja vastakkaiset. Kolmas virhe on väittää, että raskas kappale putoaa aina nopeammin. Ilman ilmanvastusta kaikki putoavat samalla kiihtyvyydellä. Ilmassa samankokoisista ja samanmuotoisista kappaleista raskaampi saavuttaa suuremman rajanopeuden.

## Tiivistelmä
- Väliaineen vastus eli ilmassa ilmanvastus $\overline{F}_\text{v}$ osoittaa nopeutta vastaan ja kasvaa, kun nopeus kasvaa. Se on suurempi suurella poikkipinta-alalla ja huonosti virtaviivaisella muodolla.
- Putoavan kappaleen kiihtyvyys pienenee, kun ilmanvastus kasvaa. Rajanopeudella $F_\text{v} = G$, kokonaisvoima on nolla ja nopeus pysyy vakiona.
- Samankokoisista ja samanmuotoisista kappaleista raskaammalla on suurempi rajanopeus. Laskuvarjo pienentää rajanopeuden turvalliseksi.
- Liikeyhtälö on $\overline{G} + \overline{F}_\text{v} = m\overline{a}$. Nousevalla kappaleella ilmanvastus osoittaa alas painon kanssa, joten hidastuvuus on suurempi kuin $g$.
- Varjon auetessa kokonaisvoima ja kiihtyvyys osoittavat ylös, vaikka hyppääjä liikkuu alas: kokonaisvoiman suunta voi erota liikkeen suunnasta.
