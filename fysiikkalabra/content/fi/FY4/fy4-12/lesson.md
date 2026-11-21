# Kahden kappaleen liikkeiden vertailu

> **Miksi** paikaltaan lähtevä auto saavuttaa edellä tasaisesti polkevan pyöräilijän vasta kaukana, vaikka auto kiihtyy koko ajan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: maantie maaseudulla aamupäivällä. Liikennevalot ovat vaihtuneet vihreiksi, ja auto lähtee pysäytysviivalta liikkeelle. Sen edellä tiellä polkee jo pyöräilijä tasaisessa vauhdissa. Auton takana on pakokaasupilvi ja pyöräilijän takana vauhtiviivoja. Tienvarressa on tasavälein merkkitolppia, taustalla pelto, punainen talo, koivuja ja kuusimetsää." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-12-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Kahden kappaleen liikkeitä voi verrata vain, kun molempien paikka mitataan samasta koordinaatistosta. Valitaan yksi $x$-akseli, yksi origo ja yksi positiivinen suunta sekä yksi kello, joka on nollassa liikkeiden alussa. Silloin kummallakin kappaleella on oma paikka ajan funktiona: $x_\text{A}(t)$ ja $x_\text{B}(t)$. Origo ja suunta voi valita vapaasti, mutta ne valitaan kerran ja pidetään koko tehtävän ajan.

Kappaleet **kohtaavat**, kun ne ovat samassa paikassa samalla hetkellä eli $x_\text{A} = x_\text{B}$. Kohtaamisesta kysytään aina kahta asiaa: milloin se tapahtuu ja missä. Jos kappaleet tulevat vastakkaisista suunnista, ne kohtaavat toisensa. Jos takana kulkeva tavoittaa edellä kulkevan ja menee sen ohi, kyseessä on **ohitus**. Molemmissa fysiikka on sama: paikat ovat yhtä suuret.

```pysahdy
Kaksi pyöräilijää ajaa samaan suuntaan, toinen edellä. Mistä tiedät, että takana ollut on ehtinyt toisen kohdalle?
---
Heidän paikkansa ovat samat samalla hetkellä: $x_\text{A} = x_\text{B}$. Sen jälkeen takaa tullut on edellä.
```

<svg data-fig="tilanne" viewBox="0 0 600 420" role="img" aria-label="Kaavakuva, jossa kaksi kappaletta on samalla x-akselilla, mittakaavassa. Ylhäällä hetkellä t = 0 kappale A on paikassa 0 m ja liikkuu nopeudella 3,0 m/s oikealle, kappale B on paikassa 60 m ja liikkuu nopeudella 2,0 m/s vasemmalle. Alhaalla hetkellä t = 12 s kumpikin on paikassa 36 m: kappaleet ovat kohdanneet. Nopeusnuolet ovat sinisiä ja eri pituisia." style="max-width:100%;font-size:24px">
  <line x1="32" y1="168" x2="516" y2="168" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M528,168 L515,174 L515,162 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="164" x2="50" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="40" y="179.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="125" y1="164" x2="125" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="108.5" y="179.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="200" y1="164" x2="200" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="183.5" y="179.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="275" y1="164" x2="275" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="258.5" y="179.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="350" y1="164" x2="350" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="333.5" y="179.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="425" y1="164" x2="425" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="408.5" y="179.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="500" y1="164" x2="500" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="483.5" y="179.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="536" y="153.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="24" y="11.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t = 0$</div></foreignObject>
  <line x1="50" y1="87" x2="50" y2="168" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="50" cy="70" r="17" fill="#2b8a3e" stroke="#ffffff" stroke-width="2.5"/>
  <foreignObject x="40" y="55.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{A}$</div></foreignObject>
  <circle cx="50" cy="168" r="7" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <line x1="76" y1="70" x2="103" y2="70" stroke="#1971c2" stroke-width="4.5" stroke-linecap="butt"/>
  <path d="M118,70 L102,77 L102,63 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="500" y1="135" x2="500" y2="168" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="500" cy="118" r="17" fill="#8a5f22" stroke="#ffffff" stroke-width="2.5"/>
  <foreignObject x="490" y="103.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{B}$</div></foreignObject>
  <circle cx="500" cy="168" r="7" fill="#8a5f22" stroke="#ffffff" stroke-width="2"/>
  <line x1="474" y1="118" x2="461" y2="118" stroke="#1971c2" stroke-width="4.5" stroke-linecap="butt"/>
  <path d="M446,118 L462,111 L462,125 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="94" y="23.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}_\text{A}$</div></foreignObject>
  <foreignObject x="415" y="71.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}_\text{B}$</div></foreignObject>
  <line x1="24" y1="214" x2="576" y2="214" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <line x1="32" y1="380" x2="516" y2="380" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M528,380 L515,386 L515,374 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="50" y1="376" x2="50" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="40" y="391.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="125" y1="376" x2="125" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="108.5" y="391.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="200" y1="376" x2="200" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="183.5" y="391.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="275" y1="376" x2="275" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="258.5" y="391.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="350" y1="376" x2="350" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="333.5" y="391.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="425" y1="376" x2="425" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="408.5" y="391.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="500" y1="376" x2="500" y2="387" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="483.5" y="391.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="536" y="365.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="24" y="227.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t = 12\,\text{s}$</div></foreignObject>
  <line x1="320" y1="299" x2="320" y2="380" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="320" cy="282" r="17" fill="#2b8a3e" stroke="#ffffff" stroke-width="2.5"/>
  <foreignObject x="310" y="267.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{A}$</div></foreignObject>
  <line x1="346" y1="282" x2="373" y2="282" stroke="#1971c2" stroke-width="4.5" stroke-linecap="butt"/>
  <path d="M388,282 L372,289 L372,275 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="320" y1="347" x2="320" y2="380" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="320" cy="330" r="17" fill="#8a5f22" stroke="#ffffff" stroke-width="2.5"/>
  <foreignObject x="310" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{B}$</div></foreignObject>
  <line x1="294" y1="330" x2="281" y2="330" stroke="#1971c2" stroke-width="4.5" stroke-linecap="butt"/>
  <path d="M266,330 L282,323 L282,337 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="320" cy="380" r="7.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="406" y="291.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x_\text{A} = x_\text{B} = 36\,\text{m}$</div></foreignObject>
</svg>

Kuvassa kappale A lähtee paikasta $0\,\text{m}$ ja B paikasta $60\,\text{m}$, ja ne liikkuvat vastakkain. Kun kappaleiden paikat on merkitty samalle akselille, näkee heti, kumpi on missäkin ja miten niiden välimatka muuttuu. Kohtaamishetkellä välimatka on nolla.

$(t,x)$-kuvaajassa kumpikin liike on oma viivansa samassa koordinaatistossa. Kohtaaminen on viivojen leikkauspiste: sen vaakakoordinaatti on kohtaamishetki ja pystykoordinaatti kohtaamispaikka. Kuvaajassa ylempänä oleva viiva tarkoittaa suurempaa paikkakoordinaattia. Kohtaamishetkellä kappaleiden kuvaajat leikkaavat toisensa. Kumpi kappale on edellä, riippuu myös liikkeen suunnasta: kun kappaleet liikkuvat $x$-akselin positiiviseen suuntaan, ylempänä oleva viiva kuuluu edellä olevalle kappaleelle. Negatiiviseen suuntaan liikuttaessa edellä on se kappale, jonka viiva on alempana.

<svg data-fig="kohtaus" viewBox="0 0 600 350" role="img" aria-label="(t,x)-kuvaaja mittakaavassa kahdesta tasaisesta liikkeestä. Kappale A lähtee paikasta 0 m ja kulkee nopeudella 3,0 m/s: suora nousee. Kappale B lähtee paikasta 60 m nopeudella −2,0 m/s: suora laskee. Suorat leikkaavat pisteessä, jossa t = 12 s ja x = 36 m. Katkoviivat johtavat pisteestä akseleille." style="max-width:100%;font-size:24px">
  <line x1="186" y1="300" x2="186" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="280" y1="300" x2="280" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="374" y1="300" x2="374" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="468" y1="300" x2="468" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="258.5" x2="468" y2="258.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="217.5" x2="468" y2="217.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="176" x2="468" y2="176" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="134.5" x2="468" y2="134.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="93.5" x2="468" y2="93.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="300" x2="482" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,300 L481,306 L481,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="301" x2="92" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,26 L98,39 L86,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="186" y1="300" x2="186" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="280" y1="300" x2="280" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="270" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="374" y1="300" x2="374" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="357.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="468" y1="300" x2="468" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="451.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$16$</div></foreignObject>
  <line x1="85" y1="258.5" x2="92" y2="258.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="244" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="85" y1="217.5" x2="92" y2="217.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="203" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$24$</div></foreignObject>
  <line x1="85" y1="176" x2="92" y2="176" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="161.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$36$</div></foreignObject>
  <line x1="85" y1="134.5" x2="92" y2="134.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="120" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$48$</div></foreignObject>
  <line x1="85" y1="93.5" x2="92" y2="93.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="79" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="62" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="500" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="106" y="17.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$x\ (\text{m})$</span></div></foreignObject>
  <polyline points="92,300 468,134.5" fill="none" stroke="#2b8a3e" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92,93.5 468,203.5" fill="none" stroke="#8a5f22" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="374" y1="176" x2="374" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="176" x2="374" y2="176" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="374" cy="176" r="7.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="476" y="120" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$x_\text{A}$</div></foreignObject>
  <foreignObject x="476" y="189" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#8a5f22">$x_\text{B}$</div></foreignObject>
  <foreignObject x="388" y="244" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kohtaaminen}$</div></foreignObject>
</svg>

Kohtaaminen ei tarkoita, että kappaleilla olisi sama nopeus. Leikkauspisteessä viivat ovat eri jyrkkiä, koska kappaleiden nopeudet ovat erisuuret. Jos kahden tasaisesti liikkuvan kappaleen nopeudet olisivat yhtä suuret, viivat olisivat yhdensuuntaiset ja kappaleiden välimatka pysyisi samana, joten ne eivät kohtaisi, jos ne lähtevät eri paikoista. Ohituksessa takaa tuleva kappale on kohtaamishetkellä nopeampi kuin ohitettava.

```pysahdy
Kaksi autoa ajaa samaan suuntaan samalla nopeudella, toinen $50\,\text{m}$ edellä. Kohtaavatko ne?
---
Eivät kohtaa. Välimatka pysyy $50\,\text{m}$, koska kuvaajien viivat ovat yhdensuuntaiset eivätkä leikkaa.
```

## Kaava: Kohtaamisehto
Kohtaamishetki ja kohtaamispaikka saadaan kirjoittamalla kummankin kappaleen paikka ajan funktiona ja merkitsemällä paikat yhtä suuriksi:
```latex
x_\text{A}(t) = x_\text{B}(t)
```
missä $x_\text{A}(t)$ ja $x_\text{B}(t)$ ovat kappaleiden paikat samassa koordinaatistossa ($\text{m}$) ja $t$ on kohtaamishetki ($\text{s}$). Kun $t$ on ratkaistu, se sijoitetaan jompaankumpaan paikkafunktioon, ja tulos on kohtaamispaikka. Tarkistuksena toinen paikkafunktio antaa saman paikan.

Paikkafunktio riippuu liikkeen lajista. Tasaisessa liikkeessä se on $x = x_0 + v\,t$ (luku *Paikka, nopeus ja tasainen liike kuvaajina*). Tasaisesti kiihtyvässä liikkeessä (luku *Kiihtyvyys ja tasaisesti kiihtyvä liike*) se on
```kaavat
paikka tasaisesti kiihtyvässä suoraviivaisessa liikkeessä :: x = x_0 + v_0\,t + \tfrac12\,a\,t^2
nopeus tasaisesti kiihtyvässä suoraviivaisessa liikkeessä :: v = v_0 + a\,t
```
missä $x_0$ on alkupaikka ($\text{m}$), $v_0$ alkunopeus ($\text{m/s}$), $a$ kiihtyvyys ($\text{m/s}^2$), $t$ aika ($\text{s}$) ja $v$ nopeus hetkellä $t$ ($\text{m/s}$). Kaavat pätevät, kun liike on suoraviivaista ja kiihtyvyys on vakio. Kahden tasaisen liikkeen yhtälö on ensimmäisen asteen yhtälö. Jos paikkafunktiot ovat eri suoria, niillä on enintään yksi leikkauspiste, joten kappaleet kohtaavat enintään kerran. Jos paikkafunktiot ovat samat, kappaleet ovat samassa paikassa koko tarkastelun ajan. Jos toinen kiihtyy, yhtälö on toisen asteen yhtälö, ja viivoilla voi olla kaksi leikkauspistettä.

Yksinkertaisin ohitus: auto lähtee levosta samasta paikasta, jossa pyöräilijä kulkee tasaisella nopeudella $v$. Autolle $x_\text{A} = \tfrac12 a t^2$ ja pyöräilijälle $x_\text{B} = v\,t$:
```latex
\begin{aligned}
&\tfrac12\,a\,t^2 = v\,t \\
&t\left(\tfrac12\,a\,t - v\right) = 0 \\
&t = 0 \quad\text{tai}\quad t = \frac{2v}{a}
\end{aligned}
```
Ratkaisu $t = 0$ on lähtöhetki: kappaleet ovat silloin samassa paikassa. Ohitus tapahtuu hetkellä $t = 2v/a$. Silloin auton nopeus on $a\,t = 2v$, kaksi kertaa pyöräilijän nopeus.

<svg data-fig="kaava" viewBox="0 0 600 350" role="img" aria-label="(t,x)-kuvaaja mittakaavassa: paikaltaan lähtevä auto A ja samasta paikasta tasaisella nopeudella 6,0 m/s kulkeva pyöräilijä B. Auton paikka on paraabeli x = t², pyöräilijän suora. Kuvaajat leikkaavat kaksi kertaa: hetkellä t = 0, jolloin kappaleet ovat samassa paikassa lähtiessään, ja hetkellä t = 6,0 s paikassa 36 m." style="max-width:100%;font-size:24px">
  <line x1="186" y1="300" x2="186" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="280" y1="300" x2="280" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="374" y1="300" x2="374" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="468" y1="300" x2="468" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="258.5" x2="468" y2="258.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="217.5" x2="468" y2="217.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="176" x2="468" y2="176" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="134.5" x2="468" y2="134.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="93.5" x2="468" y2="93.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="300" x2="482" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,300 L481,306 L481,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="301" x2="92" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,26 L98,39 L86,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="186" y1="300" x2="186" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="280" y1="300" x2="280" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="270" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="374" y1="300" x2="374" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="364" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="468" y1="300" x2="468" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="458" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="85" y1="258.5" x2="92" y2="258.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="244" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="85" y1="217.5" x2="92" y2="217.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="203" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$24$</div></foreignObject>
  <line x1="85" y1="176" x2="92" y2="176" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="161.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$36$</div></foreignObject>
  <line x1="85" y1="134.5" x2="92" y2="134.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="120" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$48$</div></foreignObject>
  <line x1="85" y1="93.5" x2="92" y2="93.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="79" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="62" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="500" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="106" y="17.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$x\ (\text{m})$</span></div></foreignObject>
  <polyline points="92,300 95,300 98.5,300 101.5,300 104.5,300 107.5,299.5 111,299.5 114,299 117,299 120,299 123.5,298.5 126.5,298 129.5,298 132.5,297.5 136,297 139,296.5 142,296 145.5,295.5 148.5,295 151.5,294.5 154.5,294 158,293 161,292.5 164,292 167,291 170.5,290.5 173.5,289.5 176.5,289 179.5,288 183,287 186,286 189,285.5 192.5,284.5 195.5,283.5 198.5,282.5 201.5,281 205,280 208,279 211,278 214,276.5 217.5,275.5 220.5,274.5 223.5,273 226.5,271.5 230,270.5 233,269 236,267.5 239.5,266 242.5,264.5 245.5,263 248.5,261.5 252,260 255,258.5 258,257 261,255.5 264.5,253.5 267.5,252 270.5,250.5 273.5,248.5 277,246.5 280,245 283,243 286.5,241 289.5,239 292.5,237.5 295.5,235.5 299,233.5 302,231.5 305,229 308,227 311.5,225 314.5,223 317.5,220.5 320.5,218.5 324,216 327,214 330,211.5 333.5,209 336.5,207 339.5,204.5 342.5,202 346,199.5 349,197 352,194.5 355,192 358.5,189.5 361.5,187 364.5,184 367.5,181.5 371,178.5 374,176 377,173 380.5,170.5 383.5,167.5 386.5,164.5 389.5,162 393,159 396,156 399,153 402,150 405.5,147 408.5,144 411.5,140.5 414.5,137.5 418,134.5 421,131 424,128 427.5,124.5 430.5,121.5 433.5,118 436.5,115 440,111.5 443,108 446,104.5 449,101 452.5,97.5 455.5,94 458.5,90.5 461.5,87 465,83 468,79.5" fill="none" stroke="#2b8a3e" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92,300 468,134.5" fill="none" stroke="#8a5f22" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="374" y1="176" x2="374" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="176" x2="374" y2="176" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="92" cy="300" r="7.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="374" cy="176" r="7.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="476" y="65" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$x_\text{A}$</div></foreignObject>
  <foreignObject x="476" y="120" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#8a5f22">$x_\text{B}$</div></foreignObject>
  <foreignObject x="388" y="206.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ohitus}$</div></foreignObject>
  <foreignObject x="110" y="255.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lähtö}$</div></foreignObject>
</svg>

Miksi auton täytyy saavuttaa kaksinkertainen nopeus? Syy näkyy $(t,v)$-kuvaajasta. Siirtymä on nopeuskuvaajan ja aika-akselin välinen pinta-ala, ja kahden kuvaajan väliin jäävä pinta-ala kertoo, paljonko etumatka muuttuu. Niin kauan kuin auto on pyöräilijää hitaampi, pyöräilijän etumatka kasvaa. Kun takana oleva lähtee hitaampana, etumatka on suurimmillaan silloin, kun nopeudet ovat yhtä suuret, eikä se ole kohtaamishetki. Vasta sen jälkeen auto on nopeampi ja pienentää etumatkaa. Ohitus tapahtuu, kun etumatkan pieneneminen on yhtä suuri kuin aiempi kasvu: kuvassa kumpikin alue vastaa $9\,\text{m}$. Siksi ohitus tulee vasta kaukana: auton on ensin kurottava umpeen etumatkan kasvu, ja tässä esimerkissä ohituspaikka on $36\,\text{m}$ lähdöstä, vaikka etumatka kasvoi enimmillään vain $9\,\text{m}$.

<svg data-fig="vt" viewBox="0 0 600 350" role="img" aria-label="(t,v)-kuvaaja mittakaavassa samasta liikkeestä kuin edellinen kuvaaja. Auton nopeus kasvaa suorana nollasta, pyöräilijän nopeus on vakio 6,0 m/s. Hetkeen t = 3,0 s asti pyöräilijä on edellä ja etumatka kasvaa: suorien väliin jää pinta-ala, joka vastaa etumatkan kasvua 9 m. Hetkestä 3,0 s hetkeen 6,0 s auto pienentää etumatkaa, ja pinta-ala vastaa pienenemistä 9 m. Hetkellä t = 6,0 s auto on saavuttanut pyöräilijän." style="max-width:100%;font-size:24px">
  <line x1="186" y1="300" x2="186" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="280" y1="300" x2="280" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="374" y1="300" x2="374" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="468" y1="300" x2="468" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="238" x2="468" y2="238" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="176" x2="468" y2="176" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="114" x2="468" y2="114" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="52" x2="468" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="300" x2="482" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,300 L481,306 L481,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="301" x2="92" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,26 L98,39 L86,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="186" y1="300" x2="186" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="280" y1="300" x2="280" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="270" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="374" y1="300" x2="374" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="364" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="468" y1="300" x2="468" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="458" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="85" y1="238" x2="92" y2="238" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="223.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="85" y1="176" x2="92" y2="176" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="85" y1="114" x2="92" y2="114" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="99.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="85" y1="52" x2="92" y2="52" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="37.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$16$</div></foreignObject>
  <foreignObject x="62" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="500" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="106" y="17.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$v\ (\text{m/s})$</span></div></foreignObject>
  <polygon points="92,300 92,207 233,207" fill="#e9c98a" fill-opacity="0.55"/>
  <polygon points="233,207 374,114 374,207" fill="#b2f2bb" fill-opacity="0.75"/>
  <polyline points="92,207 468,207" fill="none" stroke="#8a5f22" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92,300 468,52" fill="none" stroke="#2b8a3e" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="233" y1="207" x2="233" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="207" x2="233" y2="207" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="374" y1="114" x2="374" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="233" cy="207" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="476" y="37.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$v_\text{A}$</div></foreignObject>
  <foreignObject x="476" y="194.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#8a5f22">$v_\text{B}$</div></foreignObject>
  <foreignObject x="119.5" y="168.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+9\,\text{m}$</div></foreignObject>
  <foreignObject x="312" y="168.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-9\,\text{m}$</div></foreignObject>
</svg>

Jos pyöräilijä on lähtiessä matkan $x_{0\text{B}}$ edellä, yhtälö on $\tfrac12 a t^2 = x_{0\text{B}} + v\,t$. Se ratkaistaan toisen asteen yhtälön ratkaisukaavalla, ja kohtaamishetki on positiivinen juuri. Negatiivinen juuri kuvaisi hetkeä ennen lähtöä, eikä se kuulu tilanteeseen; kaksi positiivista juurta olisi kaksi kohtaamista. Jos positiivista juurta ei ole, kappaleet eivät kohtaa.

<figure class="unit-photo"><img src="pics/fy4/helsinki-trams.webp" alt="Kaksi valkoista raitiovaunua rinnakkain kadulla, taustalla vanhoja kivitaloja."><figcaption>Kaksi raitiovaunua Helsingissä heinäkuussa 2026.</figcaption></figure>

## Esimerkki
Pyöräilijä polkee suoraa tietä tasaisella nopeudella $6{,}0\,\text{m/s}$. Hetkellä $t = 0$ hän on $16\,\text{m}$ liikennevalojen pysäytysviivan edellä. Samalla hetkellä viivalla seisova auto lähtee liikkeelle ja kiihtyy tasaisesti kiihtyvyydellä $2{,}0\,\text{m/s}^2$ samaan suuntaan. Milloin auto ohittaa pyöräilijän ja kuinka kaukana pysäytysviivasta ohitus tapahtuu?

<!-- vaihe -->

**Tunnetut ja kysytty.** Origo on pysäytysviivalla ja positiivinen suunta on kulkusuunta. Auto A: $x_{0\text{A}} = 0$, $v_{0\text{A}} = 0$, $a = 2{,}0\,\text{m/s}^2$. Pyöräilijä B: $x_{0\text{B}} = 16\,\text{m}$, $v = 6{,}0\,\text{m/s}$ (vakio).

Kysytään ohitushetkeä $t$ ja ohituspaikkaa $x$.

<!-- vaihe -->

**Periaate.** Ohitushetkellä kappaleet ovat samassa paikassa, joten $x_\text{A} = x_\text{B}$. Auton liike on tasaisesti kiihtyvää ja pyöräilijän tasaista, joten kummankin paikka tunnetaan ajan funktiona. Merkitään paikat yhtä suuriksi ja ratkaistaan aika.

<!-- vaihe -->

**Kaava ratkaistuna.** Auton paikka on $x_\text{A} = \tfrac12 a t^2$ ja pyöräilijän $x_\text{B} = x_{0\text{B}} + v\,t$. Yhtälö ratkaistaan toisen asteen yhtälön ratkaisukaavalla ja valitaan positiivinen juuri:
```latex
\begin{aligned}
&\tfrac12\,a\,t^2 = x_{0\text{B}} + v\,t \\
&\tfrac12\,a\,t^2 - v\,t - x_{0\text{B}} = 0 \\
&t = \frac{v + \sqrt{v^2 + 2\,a\,x_{0\text{B}}}}{a}
\end{aligned}
```
Toisen asteen yhtälön $A t^2 + B t + C = 0$ kertoimet ovat tässä $A = \tfrac12 a$, $B = -v$ ja $C = -x_{0\text{B}}$, ja ratkaisukaava $t = \dfrac{-B \pm \sqrt{B^2 - 4AC}}{2A}$ antaa yllä olevan juuren.

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: kaikki suureet ovat SI-yksiköissä, ja juurrettavassa $v^2$ ja $2\,a\,x_{0\text{B}}$ ovat molemmat yksikössä $\text{m}^2/\text{s}^2$. Juurrettava on $v^2 + 2\,a\,x_{0\text{B}} = 36\,\text{m}^2/\text{s}^2 + 64\,\text{m}^2/\text{s}^2 = 100\,\text{m}^2/\text{s}^2$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan ensin aika ja sen jälkeen paikka:
```latex
\begin{aligned}
t &= \frac{v + \sqrt{v^2 + 2\,a\,x_{0\text{B}}}}{a} \\
&= \frac{6{,}0\,\text{m/s} + \sqrt{100\,\text{m}^2/\text{s}^2}}{2{,}0\,\text{m/s}^2} \\
&= \frac{6{,}0\,\text{m/s} + 10\,\text{m/s}}{2{,}0\,\text{m/s}^2} \\
&= 8{,}0\,\text{s}
\\[4pt]
x &= \tfrac12\,a\,t^2 \\
&= \tfrac12 \cdot 2{,}0\,\text{m/s}^2 \cdot (8{,}0\,\text{s})^2 \\
&= 64\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Auto ohittaa pyöräilijän hetkellä $t = 8{,}0\,\text{s}$ paikassa $x = 64\,\text{m}$ pysäytysviivalta laskien. Tuloksissa on kaksi merkitsevää numeroa, koska lähtötiedot $6{,}0\,\text{m/s}$, $2{,}0\,\text{m/s}^2$ ja $16\,\text{m}$ ovat kahdella numerolla.

<!-- vaihe -->

**Järkevyys.** Pyöräilijän paikka on $16\,\text{m} + 6{,}0\,\text{m/s} \cdot 8{,}0\,\text{s} = 64\,\text{m}$, joten toinen paikkafunktio antaa saman paikan. Auton nopeus ohitushetkellä on $a\,t = 2{,}0\,\text{m/s}^2 \cdot 8{,}0\,\text{s} = 16\,\text{m/s}$ ja pyöräilijän $6{,}0\,\text{m/s}$, joten auto on ohittaessaan nopeampi, kuten pitääkin. Toinen juuri $t = (6{,}0 - 10)\,\text{m/s} : 2{,}0\,\text{m/s}^2 = -2{,}0\,\text{s}$ on ennen lähtöä eikä kuulu tilanteeseen.

<svg data-fig="esimerkki" viewBox="0 0 600 350" role="img" aria-label="(t,x)-kuvaaja mittakaavassa esimerkin tilanteesta: pyöräilijä B on aluksi 16 m auton A edellä ja kulkee nopeudella 6,0 m/s; auto lähtee levosta kiihtyvyydellä 2,0 m/s². Suora x = 16 + 6t ja paraabeli x = t² leikkaavat hetkellä t = 8,0 s paikassa 64 m." style="max-width:100%;font-size:24px">
  <line x1="167" y1="300" x2="167" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="242.5" y1="300" x2="242.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="317.5" y1="300" x2="317.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="393" y1="300" x2="393" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="468" y1="300" x2="468" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="260.5" x2="468" y2="260.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="220.5" x2="468" y2="220.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="181" x2="468" y2="181" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="141.5" x2="468" y2="141.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="101.5" x2="468" y2="101.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="62" x2="468" y2="62" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="300" x2="482" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,300 L481,306 L481,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="301" x2="92" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,26 L98,39 L86,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="167" y1="300" x2="167" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="157" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="242.5" y1="300" x2="242.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="232.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="317.5" y1="300" x2="317.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="307.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="393" y1="300" x2="393" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="383" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="468" y1="300" x2="468" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="451.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="85" y1="260.5" x2="92" y2="260.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="246" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$16$</div></foreignObject>
  <line x1="85" y1="220.5" x2="92" y2="220.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="206" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$32$</div></foreignObject>
  <line x1="85" y1="181" x2="92" y2="181" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="166.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$48$</div></foreignObject>
  <line x1="85" y1="141.5" x2="92" y2="141.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="127" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$64$</div></foreignObject>
  <line x1="85" y1="101.5" x2="92" y2="101.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="87" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="85" y1="62" x2="92" y2="62" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="47.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$96$</div></foreignObject>
  <foreignObject x="62" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="500" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="106" y="17.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$x\ (\text{m})$</span></div></foreignObject>
  <polyline points="92,300 95,300 98.5,300 101.5,300 104.5,299.5 107.5,299.5 111,299.5 114,299 117,299 120,298.5 123.5,298.5 126.5,298 129.5,297.5 132.5,297 136,296.5 139,296 142,295.5 145.5,295 148.5,294.5 151.5,294 154.5,293 158,292.5 161,291.5 164,291 167,290 170.5,289 173.5,288.5 176.5,287.5 179.5,286.5 183,285.5 186,284.5 189,283.5 192.5,282.5 195.5,281 198.5,280 201.5,279 205,277.5 208,276.5 211,275 214,274 217.5,272.5 220.5,271 223.5,269.5 226.5,268 230,266.5 233,265 236,263.5 239.5,262 242.5,260.5 245.5,258.5 248.5,257 252,255 255,253.5 258,251.5 261,250 264.5,248 267.5,246 270.5,244 273.5,242 277,240 280,238 283,236 286.5,234 289.5,231.5 292.5,229.5 295.5,227 299,225 302,222.5 305,220.5 308,218 311.5,215.5 314.5,213 317.5,210.5 320.5,208 324,205.5 327,203 330,200.5 333.5,198 336.5,195 339.5,192.5 342.5,190 346,187 349,184 352,181.5 355,178.5 358.5,175.5 361.5,172.5 364.5,169.5 367.5,166.5 371,163.5 374,160.5 377,157.5 380.5,154 383.5,151 386.5,148 389.5,144.5 393,141.5 396,138 399,134.5 402,131 405.5,128 408.5,124.5 411.5,121 414.5,117.5 418,113.5 421,110 424,106.5 427.5,103 430.5,99 433.5,95.5 436.5,91.5 440,88 443,84 446,80 449,76 452.5,72 455.5,68.5 458.5,64 461.5,60 465,56 468,52" fill="none" stroke="#2b8a3e" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92,260.5 468,111.5" fill="none" stroke="#8a5f22" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="393" y1="141.5" x2="393" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="141.5" x2="393" y2="141.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="92" cy="260.5" r="6.5" fill="#8a5f22" stroke="#ffffff" stroke-width="2"/>
  <circle cx="92" cy="300" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <circle cx="393" cy="141.5" r="7.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="476" y="42.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$x_\text{A}$</div></foreignObject>
  <foreignObject x="476" y="107" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#8a5f22">$x_\text{B}$</div></foreignObject>
</svg>

## Yleinen virhekäsitys
Yleisin virhe on ajatella, että kappaleilla on kohtaamishetkellä sama nopeus, koska ne ovat samassa paikassa. Paikka ja nopeus ovat eri suureita: kappaleet ovat samassa paikassa vain sillä hetkellä, ja ohituksessa takaa tuleva kulkee ohitushetkellä nopeammin.

Toinen virhe on ratkaista kohtaamishetki merkitsemällä nopeudet yhtä suuriksi. Silloin löytyy hetki, jolla etumatka on suurimmillaan tai pienimmillään, ei hetki, jolla kappaleet ovat samassa paikassa. Kohtaamisessa yhtä suuria ovat paikat.

Kolmas virhe on lukea $(t,v)$-kuvaajan leikkauspiste kohtaamiseksi. Siinä viivat leikkaavat, kun nopeudet ovat yhtä suuret. Kohtaamisen näkee vain $(t,x)$-kuvaajasta.

## Tiivistelmä
- Kahden kappaleen paikat mitataan samassa koordinaatistossa: sama origo, sama positiivinen suunta ja sama kello.
- Kappaleet kohtaavat, kun $x_\text{A}(t) = x_\text{B}(t)$. Yhtälöstä saadaan kohtaamishetki, ja sijoittamalla se paikkafunktioon kohtaamispaikka.
- $(t,x)$-kuvaajassa kohtaaminen on viivojen leikkauspiste. Kohtaamisessa nopeudet ovat yleensä erisuuret.
- Kun toinen liike on tasaisesti kiihtyvää, yhtälö on toisen asteen yhtälö. Jokainen positiivinen juuri on kohtaaminen (niitä voi olla kaksi), ja negatiivinen juuri on ennen lähtöä eikä kuulu tilanteeseen.
- Kun takana oleva lähtee hitaampana, etumatka on suurimmillaan silloin, kun nopeudet ovat yhtä suuret, eikä se ole kohtaamishetki.
