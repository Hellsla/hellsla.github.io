# Työ ja energia

> **Miksi** painavan repun kantaminen tasaista käytävää pitkin ei fysiikan mielessä ole työtä, vaikka olkapäät väsyvät?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: opiskelija kävelee koulun tasaista käytävää pitkin painava reppu selässään. Lattia on vaakasuora, ja katkoviivanuoli lattian suuntaisesti näyttää kulkusuunnan. Taustalla on kaappirivi ja ikkunoita." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-2-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Arkikielessä työ tarkoittaa usein ponnistelua. Fysiikassa työllä on täsmällisempi merkitys: voima tekee työtä, kun kappale siirtyy ja voimalla on siirtymän suuntainen komponentti.

Kun kannat reppua vaakasuoraan tasaisella vauhdilla, reppua kannatteleva voimasi osoittaa ylöspäin, mutta reppu siirtyy vaakasuunnassa. Voima on kohtisuorassa siirtymään nähden, joten tämän voiman tekemä mekaaninen työ on nolla. Lihaksesi kuluttavat silti energiaa myös repun kannattelemiseen.

```pysahdy
Pidät raskasta kirjaa paikallaan ojennetulla kädellä. Tekeekö kätesi kannatteluvoima työtä?
---
Ei tee. Kirja ei siirry, joten voimalla ei ole siirtymää, eikä mekaanista työtä tehdä.
```

<svg data-fig="carry-lift" viewBox="0 0 600 320" role="img" aria-label="Kaavakuva kahdesta tilanteesta. Vasemmalla reppua kannetaan vaakasuoraan: kannatteleva voima F osoittaa ylös, mutta liike on sivulle, joten voima ei tee työtä, W = 0. Oikealla reppu nostetaan ylös: voima F ja liike ovat samansuuntaiset, joten voima tekee työn W = F s." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-2-carry-lift.webp" x="3.7" y="2.5" width="594.1" height="324.3" preserveAspectRatio="none"/>
  <foreignObject x="71" y="15.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kanto sivulle}$</div></foreignObject>
  <foreignObject x="390" y="15.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{nosto ylös}$</div></foreignObject>
  <foreignObject x="166" y="84.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$F$</div></foreignObject>
  <foreignObject x="107" y="251.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{liike}$</div></foreignObject>
  <foreignObject x="127.5" y="291.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = 0$</div></foreignObject>
  <foreignObject x="414" y="84.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$F$</div></foreignObject>
  <foreignObject x="534" y="145.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{liike}$</div></foreignObject>
  <foreignObject x="415" y="291.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = F\,s$</div></foreignObject>
</svg>

Työ on tapa siirtää energiaa. Tämän osoitti James Prescott Joule 1840-luvulla antamalla putoavan painon pyörittää siipipyörää vedessä. Paino teki työn, ja vesi lämpeni mitattavan verran, vaikka sitä ei lämmitetty: työ kasvatti veden sisäenergiaa. Kokeissa veden lämpeneminen osoittautui verrannolliseksi painon ja pudotusmatkan tuloon eli voiman ja matkan tuloon. Tämä kokeellinen tulos perustelee työn määritelmän $W = Fs$ (kaava alla). Sama lämpeneminen saadaan aikaan myös lämmittämällä, joten työ ja lämpö ovat kaksi tapaa siirtää energiaa, ja molemmat mitataan samalla yksiköllä, joulella.

```pysahdy
Joulen kokeessa vettä ei lämmitetty, mutta se lämpeni. Mistä lämpeneminen johtui?
---
Putoavan painon tekemä työ pyöritti siipipyörää ja kasvatti veden sisäenergiaa.
```

<svg data-fig="joule" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva Joulen kokeesta. Putoava paino vetää narua, joka kulkee väkipyörän yli ja pyörittää vesiastiassa olevaa siipipyörää. Painon voima tekee työn pudotusmatkalla h, ja siipipyörä lämmittää vettä: työ kasvattaa veden sisäenergiaa." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-2-joule.webp" x="1.2" y="0" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="152.5" y="15.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{työ} \to \text{sisäenergia}$</div></foreignObject>
  <foreignObject x="304" y="165.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{paino}$</div></foreignObject>
  <foreignObject x="500" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="81" y="289.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{vesi lämpenee}$</div></foreignObject>
</svg>

Kun teet kappaleeseen työtä, energiaa siirtyy: nostetun kappaleen energia kasvaa, jousi venyy ja tallentaa energiaa, ja kitkaa vastaan tehty työ lämmittää pintoja. Energia ei katoa, vaan vaihtaa muotoa. Teho kertoo, kuinka nopeasti työ tehdään. Portaat ylös kävellen ja juosten teet saman työn, mutta juosten teho on suurempi. Kiukaan $6\,\text{kW}$:n teho tarkoittaa, että se muuttaa joka sekunti 6000 joulea sähköenergiaa sisäenergiaksi, joka siirtyy lämpönä kiviin ja ilmaan.

<figure class="unit-photo"><img src="pics/fy3/crane-lifting-load.webp" alt="Nosturin koukussa roikkuu harmaa betoniastia rakenteilla olevan rakennuksen katon alla, ja kaksi työntekijää ohjaa sitä."><figcaption>Nosturi nostaa betoniastiaa rakennustyömaalla. Kun kuorma nousee, nostovoima tekee työtä ja kuorman potentiaalienergia kasvaa.</figcaption></figure>

## Kaava: Työ ja teho
Kun vakiovoima on liikkeen suuntainen, voiman tekemä työ on voiman ja matkan tulo:
```kaavat
voiman tekemä työ :: W = F s
```
missä $W$ on työ (J), $F$ voiman suuruus (N) ja $s$ kappaleen kulkema matka (m). Yksi joule on työ, jonka yhden newtonin voima tekee yhden metrin matkalla: $1\,\text{J} = 1\,\text{N} \cdot \text{m}$.

Jos voima muuttuu matkan aikana, työ on $(s,F)$-kuvaajassa voimakäyrän ja $s$-akselin väliin jäävä pinta-ala. Vakiovoimalla pinta-ala on suorakulmio, jonka ala on $F \cdot s$, joten sama laskusääntö toimii molemmissa tapauksissa. Monimutkaisen kuvaajan pinta-alan voi laskea jakamalla se suorakulmioihin, kolmioihin ja puolisuunnikkaisiin.

<svg data-fig="work-graphs" viewBox="0 0 600 346" role="img" aria-label="Kaavakuva kahdesta (s,F)-kuvaajasta. Vasemmalla voima on vakio, ja työ on suorakulmion pinta-ala F · s. Oikealla voima ensin kasvaa tasaisesti ja pysyy sitten vakiona; työ on kolmion pinta-ala A₁ plus suorakulmion pinta-ala A₂." style="max-width:100%;font-size:24px">
  <line x1="79" y1="240" x2="264" y2="240" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M276,240 L263,246 L263,234 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="241" x2="80" y2="66" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,54 L86,67 L74,67 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="282" y="225.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s$</div></foreignObject>
  <foreignObject x="70" y="23.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F$</div></foreignObject>
  <polygon points="80,240 80,144 216,144 216,240" fill="#ffc078" fill-opacity="0.55"/>
  <line x1="216" y1="144" x2="216" y2="240" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="80" y1="144" x2="216" y2="144" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="80,144 216,144" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="80" y1="262" x2="216" y2="262" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="255" x2="80" y2="269" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="216" y1="255" x2="216" y2="269" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="138" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s$</div></foreignObject>
  <line x1="58" y1="240" x2="58" y2="144" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="51" y1="240" x2="65" y2="240" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="51" y1="144" x2="65" y2="144" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="26" y="177.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$F$</div></foreignObject>
  <foreignObject x="113" y="177.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = F\,s$</div></foreignObject>
  <foreignObject x="81.5" y="307.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{vakiovoima}$</div></foreignObject>
  <line x1="369" y1="240" x2="554" y2="240" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M566,240 L553,246 L553,234 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="370" y1="241" x2="370" y2="66" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M370,54 L376,67 L364,67 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="572" y="225.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s$</div></foreignObject>
  <foreignObject x="360" y="23.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F$</div></foreignObject>
  <polygon points="370,240 438,144 438,240" fill="#e8590c" fill-opacity="0.4"/>
  <polygon points="438,240 438,144 523,144 523,240" fill="#ffc078" fill-opacity="0.55"/>
  <line x1="523" y1="144" x2="523" y2="240" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="370" y1="144" x2="523" y2="144" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="438,144 438,240" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <polyline points="370,240 438,144 523,144" fill="none" stroke="#e8590c" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="370" y1="262" x2="523" y2="262" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="370" y1="255" x2="370" y2="269" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="523" y1="255" x2="523" y2="269" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="436.5" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s$</div></foreignObject>
  <line x1="348" y1="240" x2="348" y2="144" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="341" y1="240" x2="355" y2="240" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="341" y1="144" x2="355" y2="144" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="316" y="177.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$F$</div></foreignObject>
  <foreignObject x="404.5" y="200" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A_1$</div></foreignObject>
  <foreignObject x="464" y="177.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A_2$</div></foreignObject>
  <foreignObject x="361.5" y="307.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{muuttuva voima}$</div></foreignObject>
</svg>

Kun nostat kappaleen tasaisella nopeudella ylös, nostovoima on yhtä suuri kuin kappaleen paino $G = mg$ (luku *Voima vuorovaikutuksen mittana ja paino*). Nostotyö korkeudelle $h$ on siis:
```latex
W = G h = m g h
```
missä $G$ on paino (N), $m$ massa (kg), $g = 9{,}81\,\text{m/s}^2$ ja $h$ nostokorkeus (m). Nostetun kappaleen energia kasvaa täsmälleen nostotyön verran.

<svg data-fig="lift-work" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva nostotyöstä, ei mittakaavassa. Laatikko nostetaan tasaisella nopeudella maasta korkeudelle h. Nostovoima F osoittaa ylös ja laatikon paino G alas, ja nuolet ovat yhtä pitkät, F = G. Nostotyö on W = F h = G h." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-2-lift-work.webp" x="0" y="0" width="597" height="335.8" preserveAspectRatio="none"/>
  <foreignObject x="196" y="39.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$F$</div></foreignObject>
  <foreignObject x="196" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$G$</div></foreignObject>
  <foreignObject x="8" y="181.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{liike}$</div></foreignObject>
  <foreignObject x="290" y="207.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="372" y="65.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F = G$</div></foreignObject>
  <foreignObject x="372" y="135.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$W = F\,h$</div></foreignObject>
  <foreignObject x="372" y="185.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$W = G\,h$</div></foreignObject>
  <foreignObject x="372" y="235.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$W = m\,g\,h$</div></foreignObject>
</svg>

Teho on työ jaettuna siihen kuluneella ajalla. Tasaisessa liikkeessä, jossa voima on liikkeen suuntainen, teho saadaan myös voiman ja nopeuden tulona, koska $s/t = v$:
```kaavat
teho :: P = \frac{W}{t} = F v
```
missä $P$ on teho (W), $t$ aika (s) ja $v$ nopeus (m/s). Yksi watti on yksi joule sekunnissa: $1\,\text{W} = 1\,\text{J/s}$.

```pysahdy
Kone tekee $600\,\text{J}$:n työn $20\,\text{s}$:ssa. Mikä on koneen teho?
---
$P = W/t = 600\,\text{J}/20\,\text{s} = 30\,\text{W}$.
```

## Esimerkki
Jousta venytetään $20\,\text{cm}$. Venyttävä voima kasvaa tasaisesti nollasta 40 newtoniin, kuten kuvaaja näyttää. Kuinka suuren työn venyttävä voima tekee?

<svg data-fig="spring-work" viewBox="0 0 600 320" role="img" aria-label="(s,F)-kuvaaja mittakaavassa: voima kasvaa suoraviivaisesti nollasta 40 newtoniin matkalla 0–0,20 metriä; kolmion pinta-ala on työ." style="max-width:100%;font-size:24px">
  <line x1="167.5" y1="270" x2="167.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="243" y1="270" x2="243" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="319" y1="270" x2="319" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="394.5" y1="270" x2="394.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="227" x2="470" y2="227" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="184.5" x2="470" y2="184.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="141.5" x2="470" y2="141.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="99" x2="470" y2="99" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="270" x2="484" y2="270" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,270 L483,276 L483,264 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="271" x2="92" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,30 L98,43 L86,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="167.5" y1="270" x2="167.5" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="138.5" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}05$</div></foreignObject>
  <line x1="243" y1="270" x2="243" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="214" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}10$</div></foreignObject>
  <line x1="319" y1="270" x2="319" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="290" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}15$</div></foreignObject>
  <line x1="394.5" y1="270" x2="394.5" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="365.5" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}20$</div></foreignObject>
  <line x1="85" y1="227" x2="92" y2="227" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="212.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="85" y1="184.5" x2="92" y2="184.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="170" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="85" y1="141.5" x2="92" y2="141.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="127" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="85" y1="99" x2="92" y2="99" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="84.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <foreignObject x="62" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="255.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s\ (\text{m})$</div></foreignObject>
  <foreignObject x="82" y="-0.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\text{N})$</div></foreignObject>
  <polygon points="92,270 394.5,99 394.5,270" fill="#ffc078" fill-opacity="0.6"/>
  <line x1="394.5" y1="99" x2="394.5" y2="270" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="99" x2="394.5" y2="99" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="92,270 394.5,99" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="394.5" cy="99" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="231" y="225.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = \text{pinta-ala}$</div></foreignObject>
</svg>

<!-- vaihe -->

**Tunnetut ja kysytty.** Jousen venytys eli voiman kulkema matka on $s = 20\,\text{cm}$, ja voiman suurin arvo on $F_\text{max} = 40\,\text{N}$.

Voima kasvaa tasaisesti nollasta.

Kysytään venyttävän voiman tekemää työtä $W$.

<!-- vaihe -->

**Periaate.** Työ on voiman ja matkan tulo vain, kun voima on vakio. Tässä voima kasvaa tasaisesti, joten työ saadaan $(s,F)$-kuvaajan pinta-alana: kuvaajan ja $s$-akselin väliin jäävä alue on kolmio. Voima on liikkeen suuntainen, joten työ on positiivinen.

<!-- vaihe -->

**Kaava ratkaistuna.** Voima ei ole vakio, joten kaava $W = Fs$ ei käy suoraan. Työ on $(s,F)$-kuvaajan kolmion pinta-ala $A_\text{kolmio}$, joka on puolet kannan $s$ ja korkeuden $F_\text{max}$ tulosta:
```latex
\begin{aligned}
W &= A_\text{kolmio} \\
&= \frac{1}{2} F_\text{max}\, s
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Matka on senttimetreinä, mutta työ lasketaan jouleina, joten matka muunnetaan metreiksi: $s = 20\,\text{cm} = 0{,}20\,\text{m}$. Voima on jo newtoneina, joten tulo $\text{N}\cdot\text{m}$ on suoraan jouleja.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan arvot yksiköineen:
```latex
\begin{aligned}
W &= A_\text{kolmio} \\
&= \frac{1}{2} F_\text{max}\, s \\
&= \frac{1}{2} \cdot 40\,\text{N} \cdot 0{,}20\,\text{m} \\
&= 4{,}0\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Venyttävä voima tekee $4{,}0\,\text{J}$:n työn, kaksi merkitsevää numeroa kuten annetuissa arvoissa $20\,\text{cm}$ ja $40\,\text{N}$. Työ ei katoa, vaan energia tallentuu venyneeseen jouseen.

<!-- vaihe -->

**Järkevyys.** Voima kasvaa tasaisesti, joten sen keskimääräinen suuruus on puolet huippuarvosta, $F_\text{ka} = 20\,\text{N}$. Keskimääräisellä voimalla saadaan sama tulos:
```latex
\begin{aligned}
W &= F_\text{ka}\, s \\
&= 20\,\text{N} \cdot 0{,}20\,\text{m} \\
&= 4{,}0\,\text{J}
\end{aligned}
```
Jos laskisit $40\,\text{N} \cdot 0{,}20\,\text{m} = 8{,}0\,\text{J}$, tulos olisi kaksinkertainen, koska voima ei ole $40\,\text{N}$ koko matkalla.

## Yleinen virhekäsitys
Työ ei ole sama asia kuin ponnistelu: väsyminen ei tarkoita, että olisit tehnyt fysiikan tarkoittamaa työtä. Toinen yleinen virhe on sotkea työ ja teho: suuri teho ei tarkoita suurta työtä, vaan nopeasti tehtyä työtä.

## Tiivistelmä
- Liikkeen suuntainen vakiovoima tekee työn $W = F s$. Muuttuvalla voimalla työ on $(s,F)$-kuvaajan pinta-ala.
- Liikettä vastaan kohtisuora voima ei tee työtä. Siksi vaakasuora kantaminen tasaisella vauhdilla ei ole kantajan voiman tekemää työtä.
- Työ siirtää energiaa: se voi nostaa kappaleen energiaa ($W = m g h$), venyttää jousta tai kasvattaa kitkassa pintojen sisäenergiaa. Joulen koe osoitti, että työ ja lämpö ovat kaksi tapaa siirtää energiaa.
- Teho on työ aikayksikössä: $P = W/t = F v$. Yksiköt: $1\,\text{J} = 1\,\text{N} \cdot \text{m}$ ja $1\,\text{W} = 1\,\text{J/s}$.
