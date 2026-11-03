# Aaltojen heijastuminen ja diffraktio

> **Miksi** aallot ylettyvät aallonmurtajan kapeasta aukosta myös sataman nurkkiin eivätkä kulje vain suoraan aukon kohdalle?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: satama ylhäältä katsottuna. Yläosassa on avomeri, jolla aallonharjat kulkevat suorina riveinä kohti rantaa. Kivistä tehty aallonmurtaja kulkee poikki kuvan, ja sen keskellä on kapea aukko. Aukon takana sataman altaassa aallonharjat ovat kaaria, jotka ulottuvat altaan nurkkiin asti. Laitureissa on veneitä, ja nurkassa oleva vene keinuu aalloissa." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy511h-sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><clipPath id="fy511h-basin"><rect x="150" y="300" width="900" height="300"/></clipPath></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy511h-sea)"/>
  <path d="M0,40 Q30,32 60,40 Q90,32 120,40 Q150,32 180,40 Q210,32 240,40 Q270,32 300,40 Q330,32 360,40 Q390,32 420,40 Q450,32 480,40 Q510,32 540,40 Q570,32 600,40 Q630,32 660,40 Q690,32 720,40 Q750,32 780,40 Q810,32 840,40 Q870,32 900,40 Q930,32 960,40 Q990,32 1020,40 Q1050,32 1080,40 Q1110,32 1140,40 Q1170,32 1200,40" fill="none" stroke="#ffffff" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <path d="M0,100 Q30,92 60,100 Q90,92 120,100 Q150,92 180,100 Q210,92 240,100 Q270,92 300,100 Q330,92 360,100 Q390,92 420,100 Q450,92 480,100 Q510,92 540,100 Q570,92 600,100 Q630,92 660,100 Q690,92 720,100 Q750,92 780,100 Q810,92 840,100 Q870,92 900,100 Q930,92 960,100 Q990,92 1020,100 Q1050,92 1080,100 Q1110,92 1140,100 Q1170,92 1200,100" fill="none" stroke="#ffffff" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <path d="M0,160 Q30,152 60,160 Q90,152 120,160 Q150,152 180,160 Q210,152 240,160 Q270,152 300,160 Q330,152 360,160 Q390,152 420,160 Q450,152 480,160 Q510,152 540,160 Q570,152 600,160 Q630,152 660,160 Q690,152 720,160 Q750,152 780,160 Q810,152 840,160 Q870,152 900,160 Q930,152 960,160 Q990,152 1020,160 Q1050,152 1080,160 Q1110,152 1140,160 Q1170,152 1200,160" fill="none" stroke="#ffffff" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <path d="M0,220 Q30,212 60,220 Q90,212 120,220 Q150,212 180,220 Q210,212 240,220 Q270,212 300,220 Q330,212 360,220 Q390,212 420,220 Q450,212 480,220 Q510,212 540,220 Q570,212 600,220 Q630,212 660,220 Q690,212 720,220 Q750,212 780,220 Q810,212 840,220 Q870,212 900,220 Q930,212 960,220 Q990,212 1020,220 Q1050,212 1080,220 Q1110,212 1140,220 Q1170,212 1200,220" fill="none" stroke="#ffffff" stroke-width="5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.8"/>
  <g clip-path="url(#fy511h-basin)"><path d="M540,300 A60,60 0 0 0 660,300" fill="none" stroke="#ffffff" stroke-width="5" stroke-opacity="0.85" stroke-linecap="round"/><path d="M480,300 A120,120 0 0 0 720,300" fill="none" stroke="#ffffff" stroke-width="5" stroke-opacity="0.78" stroke-linecap="round"/><path d="M420,300 A180,180 0 0 0 780,300" fill="none" stroke="#ffffff" stroke-width="5" stroke-opacity="0.71" stroke-linecap="round"/><path d="M360,300 A240,240 0 0 0 840,300" fill="none" stroke="#ffffff" stroke-width="5" stroke-opacity="0.64" stroke-linecap="round"/><path d="M300,300 A300,300 0 0 0 900,300" fill="none" stroke="#ffffff" stroke-width="5" stroke-opacity="0.57" stroke-linecap="round"/><path d="M240,300 A360,360 0 0 0 960,300" fill="none" stroke="#ffffff" stroke-width="5" stroke-opacity="0.50" stroke-linecap="round"/><path d="M180,300 A420,420 0 0 0 1020,300" fill="none" stroke="#ffffff" stroke-width="5" stroke-opacity="0.43" stroke-linecap="round"/><path d="M120,300 A480,480 0 0 0 1080,300" fill="none" stroke="#ffffff" stroke-width="5" stroke-opacity="0.36" stroke-linecap="round"/><path d="M60,300 A540,540 0 0 0 1140,300" fill="none" stroke="#ffffff" stroke-width="5" stroke-opacity="0.29" stroke-linecap="round"/><path d="M0,300 A600,600 0 0 0 1200,300" fill="none" stroke="#ffffff" stroke-width="5" stroke-opacity="0.22" stroke-linecap="round"/><path d="M-60,300 A660,660 0 0 0 1260,300" fill="none" stroke="#ffffff" stroke-width="5" stroke-opacity="0.15" stroke-linecap="round"/></g>
  <rect x="0" y="300" width="150" height="300" fill="#e9c98a"/>
  <rect x="0" y="300" width="150" height="300" fill="none" stroke="#1f2933" stroke-width="3"/>
  <rect x="1050" y="300" width="150" height="300" fill="#e9c98a"/>
  <rect x="1050" y="300" width="150" height="300" fill="none" stroke="#1f2933" stroke-width="3"/>
  <rect x="0" y="560" width="1200" height="40" fill="#e9c98a" stroke="#1f2933" stroke-width="3"/>
  <line x1="10" y1="300" x2="10" y2="560" stroke="#d9b26a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="56" y1="300" x2="56" y2="560" stroke="#d9b26a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="102" y1="300" x2="102" y2="560" stroke="#d9b26a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="148" y1="300" x2="148" y2="560" stroke="#d9b26a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1060" y1="300" x2="1060" y2="560" stroke="#d9b26a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1106" y1="300" x2="1106" y2="560" stroke="#d9b26a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1152" y1="300" x2="1152" y2="560" stroke="#d9b26a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1198" y1="300" x2="1198" y2="560" stroke="#d9b26a" stroke-width="3" stroke-linecap="butt"/>
  <rect x="0" y="262" width="560" height="40" fill="#8a96a3"/>
  <circle cx="18" cy="272" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="52" cy="290" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="86" cy="272" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="120" cy="290" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="154" cy="272" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="188" cy="290" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="222" cy="272" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="256" cy="290" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="290" cy="272" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="324" cy="290" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="358" cy="272" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="392" cy="290" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="426" cy="272" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="460" cy="290" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="494" cy="272" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="528" cy="290" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="640" y="262" width="560" height="40" fill="#8a96a3"/>
  <circle cx="658" cy="272" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="692" cy="290" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="726" cy="272" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="760" cy="290" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="794" cy="272" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="828" cy="290" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="862" cy="272" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="896" cy="290" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="930" cy="272" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="964" cy="290" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="998" cy="272" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1032" cy="290" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1066" cy="272" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1100" cy="290" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1134" cy="272" r="15" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1168" cy="290" r="15" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <g transform="translate(214 360) rotate(90)"><path d="M-60,0 Q-50,-22 0,-24 Q50,-22 70,0 Q50,22 0,24 Q-50,22 -60,0 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3"/><rect x="-24" y="-11" width="40" height="22" rx="5" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/></g>
  <g transform="translate(986 380) rotate(90)"><path d="M-60,0 Q-50,-22 0,-24 Q50,-22 70,0 Q50,22 0,24 Q-50,22 -60,0 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3"/><rect x="-24" y="-11" width="40" height="22" rx="5" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/></g>
  <g transform="translate(986 470) rotate(90)"><path d="M-60,0 Q-50,-22 0,-24 Q50,-22 70,0 Q50,22 0,24 Q-50,22 -60,0 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="3"/><rect x="-24" y="-11" width="40" height="22" rx="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/></g>
  <g transform="translate(230 506) rotate(72)"><path d="M-60,0 Q-50,-22 0,-24 Q50,-22 70,0 Q50,22 0,24 Q-50,22 -60,0 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3"/><rect x="-24" y="-11" width="40" height="22" rx="5" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/></g>
  <circle cx="150" cy="360" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="150" cy="506" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1050" cy="380" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1050" cy="470" r="7" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M150,360 L178,360" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1050,380 L1022,380" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M1050,470 L1022,470" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M150,506 L198,496" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <ellipse cx="230" cy="506" rx="82" ry="37" transform="rotate(72 230 506)" fill="none" stroke="#ffffff" stroke-width="3" stroke-opacity="0.6"/>
  <ellipse cx="230" cy="506" rx="100" ry="45" transform="rotate(72 230 506)" fill="none" stroke="#ffffff" stroke-width="3" stroke-opacity="0.6"/>
</svg>

## Ydinajatus

### Aaltorintama ja säde
Aaltoa on helpointa kuvata ylhäältä katsottuna. **Aaltorintama** on viiva, joka yhdistää aallon samassa vaiheessa olevat kohdat, esimerkiksi yhden aallonharjan. Kahden peräkkäisen harjan välinen etäisyys on aallonpituus $\lambda$ (luku *Mekaaninen aaltoliike*). **Säde** on nuoli, joka näyttää aallon etenemissuunnan, ja se on aina kohtisuorassa aaltorintamaa vastaan. Suoran rintaman aalto on tasoaalto, ja pistemäisestä lähteestä, kuten veteen pudonneesta kivestä, lähtee ympyräaalto, jonka säteet osoittavat lähteestä poispäin joka suuntaan.

<svg data-fig="rintamat" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva kahdesta aallosta ylhäältä katsottuna. Vasemmalla tasoaalto: aaltorintamat ovat yhdensuuntaisia suoria, joiden väli on aallonpituus lambda, ja säteet ovat niitä vastaan kohtisuoria nuolia. Oikealla pistemäisestä lähteestä lähtevä ympyräaalto: aaltorintamat ovat samankeskisiä ympyröitä ja säteet lähtevät lähteestä joka suuntaan, kohtisuoraan rintamia vastaan." style="max-width:100%;font-size:24px">
  <rect x="12" y="44" width="276" height="236" rx="8" fill="#eef5f9"/>
  <rect x="312" y="44" width="276" height="236" rx="8" fill="#eef5f9"/>
  <line x1="300" y1="40" x2="300" y2="330" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="90" y="7.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tasoaalto}$</div></foreignObject>
  <foreignObject x="377.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ympyräaalto}$</div></foreignObject>
  <line x1="70" y1="60" x2="70" y2="264" stroke="#2f74b5" stroke-width="3" stroke-linecap="butt"/>
  <line x1="130" y1="60" x2="130" y2="264" stroke="#2f74b5" stroke-width="3" stroke-linecap="butt"/>
  <line x1="190" y1="60" x2="190" y2="264" stroke="#2f74b5" stroke-width="3" stroke-linecap="butt"/>
  <line x1="250" y1="60" x2="250" y2="264" stroke="#2f74b5" stroke-width="3" stroke-linecap="butt"/>
  <line x1="30" y1="96" x2="265" y2="96" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M278,96 L264,102.5 L264,89.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="30" y1="162" x2="265" y2="162" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M278,162 L264,168.5 L264,155.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="30" y1="228" x2="265" y2="228" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M278,228 L264,234.5 L264,221.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="292" x2="130" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="70" y1="284" x2="70" y2="300" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="130" y1="284" x2="130" y2="300" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="90" y="301.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <foreignObject x="126" y="301.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{aaltorintama}$</div></foreignObject>
  <circle cx="450" cy="162" r="34" fill="none" stroke="#2f74b5" stroke-width="3"/>
  <circle cx="450" cy="162" r="68" fill="none" stroke="#2f74b5" stroke-width="3"/>
  <circle cx="450" cy="162" r="102" fill="none" stroke="#2f74b5" stroke-width="3"/>
  <circle cx="450" cy="162" r="6" fill="#1f2933"/>
  <line x1="461" y1="157.5" x2="552.5" y2="119.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M564.5,114.5 L554,125.5 L549,114 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="454.5" y1="151" x2="492.5" y2="59.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M497.5,47.5 L498,63 L486.5,58 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="445.5" y1="151" x2="407.5" y2="59.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M402.5,47.5 L413.5,58 L402,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="439" y1="157.5" x2="347.5" y2="119.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M335.5,114.5 L351,114 L346,125.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="439" y1="166.5" x2="347.5" y2="204.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M335.5,209.5 L346,198.5 L351,210 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="445.5" y1="173" x2="407.5" y2="264.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M402.5,276.5 L402,261 L413.5,266 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="454.5" y1="173" x2="492.5" y2="264.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M497.5,276.5 L486.5,266 L498,261 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="461" y1="166.5" x2="552.5" y2="204.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M564.5,209.5 L549,210 L554,198.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="526" y="301.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{säde}$</div></foreignObject>
  <line x1="540" y1="304" x2="536" y2="252" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
</svg>

### Heijastuminen köyden päästä
Kun aalto saapuu väliaineen rajalle, se heijastuu eli osa siitä tai koko aalto palaa takaisin. Köydessä tämän näkee yhdestä pulssista. Jos köyden pää on kiinni seinässä, pää ei pääse liikkumaan. Ylöspäin suuntautuva pulssi vetää kiinnitystä ylöspäin, ja seinä vetää köyttä yhtä suurella voimalla alaspäin. Siksi **kiinteästä päästä heijastunut pulssi on kääntynyt**: se palaa alaspäin suuntautuvana. Jos köyden pää on rengas, joka liukuu kitkatta tankoa pitkin, pää heilahtaa pulssin mukana ylös, eikä mikään vedä sitä alas. **Vapaasta päästä heijastunut pulssi ei käänny**, vaan palaa samanmerkkisenä.

<svg data-fig="koysi" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva, ei mittakaavassa: köyden pulssin heijastuminen kahdessa tapauksessa. Vasemmalla köyden pää on kiinnitetty seinään (kiinteä pää), oikealla pää on rengas, joka liukuu kitkatta pystysuoraa tankoa pitkin (vapaa pää). Ylärivillä ennen heijastumista ylöspäin suuntautunut pulssi etenee oikealle kohti päätä. Alarivillä heijastumisen jälkeen pulssi etenee vasemmalle: kiinteästä päästä heijastunut pulssi on kääntynyt alaspäin, vapaasta päästä heijastunut on yhä ylöspäin." style="max-width:100%;font-size:24px">
  <foreignObject x="83.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kiinteä pää}$</div></foreignObject>
  <foreignObject x="396" y="7.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{vapaa pää}$</div></foreignObject>
  <line x1="300" y1="40" x2="300" y2="368" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="12" y1="204" x2="588" y2="204" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="16" y="45.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{ennen}$</div></foreignObject>
  <line x1="28" y1="140" x2="248" y2="140" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <rect x="252" y="86" width="22" height="108" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="256" y1="114" x2="270" y2="100" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="134" x2="270" y2="120" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="154" x2="270" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="174" x2="270" y2="160" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="194" x2="270" y2="180" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="250" cy="140" r="5" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M28,140 L29,140 L30,140 L31,140 L32,140 L33,140 L34,140 L35,140 L36,140 L37,140 L38,140 L39,140 L40,140 L41,140 L42,140 L43,140 L44,140 L45,140 L46,140 L47,140 L48,140 L49,140 L50,140 L51,140 L52,140 L53,139.5 L54,139.5 L55,139.5 L56,139.5 L57,139.5 L58,139.5 L59,139 L60,139 L61,139 L62,138.5 L63,138.5 L64,138 L65,137.5 L66,137.5 L67,137 L68,136.5 L69,136 L70,135 L71,134.5 L72,134 L73,133 L74,132 L75,131 L76,130 L77,129 L78,128 L79,126.5 L80,125.5 L81,124 L82,122.5 L83,121 L84,119.5 L85,118 L86,116.5 L87,115 L88,113.5 L89,112 L90,110.5 L91,109 L92,107.5 L93,106 L94,105 L95,104 L96,103 L97,102 L98,101.5 L99,100.5 L100,100.5 L101,100 L102,100 L103,100 L104,100.5 L105,100.5 L106,101.5 L107,102 L108,103 L109,104 L110,105 L111,106 L112,107.5 L113,109 L114,110.5 L115,112 L116,113.5 L117,115 L118,116.5 L119,118 L120,119.5 L121,121 L122,122.5 L123,124 L124,125.5 L125,126.5 L126,128 L127,129 L128,130 L129,131 L130,132 L131,133 L132,134 L133,134.5 L134,135 L135,136 L136,136.5 L137,137 L138,137.5 L139,137.5 L140,138 L141,138.5 L142,138.5 L143,139 L144,139 L145,139 L146,139.5 L147,139.5 L148,139.5 L149,139.5 L150,139.5 L151,139.5 L152,140 L153,140 L154,140 L155,140 L156,140 L157,140 L158,140 L159,140 L160,140 L161,140 L162,140 L163,140 L164,140 L165,140 L166,140 L167,140 L168,140 L169,140 L170,140 L171,140 L172,140 L173,140 L174,140 L175,140 L176,140 L177,140 L178,140 L179,140 L180,140 L181,140 L182,140 L183,140 L184,140 L185,140 L186,140 L187,140 L188,140 L189,140 L190,140 L191,140 L192,140 L193,140 L194,140 L195,140 L196,140 L197,140 L198,140 L199,140 L200,140 L201,140 L202,140 L203,140 L204,140 L205,140 L206,140 L207,140 L208,140 L209,140 L210,140 L211,140 L212,140 L213,140 L214,140 L215,140 L216,140 L217,140 L218,140 L219,140 L220,140 L221,140 L222,140 L223,140 L224,140 L225,140 L226,140 L227,140 L228,140 L229,140 L230,140 L231,140 L232,140 L233,140 L234,140 L235,140 L236,140 L237,140 L238,140 L239,140 L240,140 L241,140 L242,140 L243,140 L244,140 L245,140 L246,140 L247,140 L248,140" fill="none" stroke="#8a5f22" stroke-width="4" stroke-linejoin="round"/>
  <line x1="76" y1="74" x2="116" y2="74" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M128,74 L115,80 L115,68 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="136" y="59.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="16" y="211.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{jälkeen}$</div></foreignObject>
  <line x1="28" y1="300" x2="248" y2="300" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <rect x="252" y="246" width="22" height="108" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="256" y1="274" x2="270" y2="260" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="294" x2="270" y2="280" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="314" x2="270" y2="300" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="334" x2="270" y2="320" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="354" x2="270" y2="340" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="250" cy="300" r="5" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M28,300 L29,300 L30,300 L31,300 L32,300 L33,300 L34,300 L35,300 L36,300 L37,300 L38,300 L39,300 L40,300 L41,300 L42,300 L43,300 L44,300 L45,300 L46,300 L47,300 L48,300 L49,300 L50,300 L51,300 L52,300 L53,300 L54,300 L55,300 L56,300 L57,300 L58,300 L59,300 L60,300 L61,300 L62,300 L63,300 L64,300 L65,300 L66,300 L67,300 L68,300 L69,300 L70,300 L71,300 L72,300 L73,300 L74,300 L75,300 L76,300 L77,300 L78,300 L79,300 L80,300 L81,300 L82,300 L83,300 L84,300 L85,300 L86,300 L87,300 L88,300 L89,300 L90,300 L91,300 L92,300 L93,300 L94,300 L95,300 L96,300 L97,300 L98,300 L99,300 L100,300 L101,300 L102,300 L103,300 L104,300 L105,300 L106,300 L107,300 L108,300 L109,300 L110,300 L111,300 L112,300 L113,300 L114,300 L115,300 L116,300 L117,300 L118,300 L119,300 L120,300 L121,300 L122,300 L123,300 L124,300 L125,300.5 L126,300.5 L127,300.5 L128,300.5 L129,300.5 L130,300.5 L131,301 L132,301 L133,301 L134,301.5 L135,301.5 L136,302 L137,302.5 L138,302.5 L139,303 L140,303.5 L141,304 L142,305 L143,305.5 L144,306 L145,307 L146,308 L147,309 L148,310 L149,311 L150,312 L151,313.5 L152,314.5 L153,316 L154,317.5 L155,319 L156,320.5 L157,322 L158,323.5 L159,325 L160,326.5 L161,328 L162,329.5 L163,331 L164,332.5 L165,334 L166,335 L167,336 L168,337 L169,338 L170,338.5 L171,339.5 L172,339.5 L173,340 L174,340 L175,340 L176,339.5 L177,339.5 L178,338.5 L179,338 L180,337 L181,336 L182,335 L183,334 L184,332.5 L185,331 L186,329.5 L187,328 L188,326.5 L189,325 L190,323.5 L191,322 L192,320.5 L193,319 L194,317.5 L195,316 L196,314.5 L197,313.5 L198,312 L199,311 L200,310 L201,309 L202,308 L203,307 L204,306 L205,305.5 L206,305 L207,304 L208,303.5 L209,303 L210,302.5 L211,302.5 L212,302 L213,301.5 L214,301.5 L215,301 L216,301 L217,301 L218,300.5 L219,300.5 L220,300.5 L221,300.5 L222,300.5 L223,300.5 L224,300 L225,300 L226,300 L227,300 L228,300 L229,300 L230,300 L231,300 L232,300 L233,300 L234,300 L235,300 L236,300 L237,300 L238,300 L239,300 L240,300 L241,300 L242,300 L243,300 L244,300 L245,300 L246,300 L247,300 L248,300" fill="none" stroke="#8a5f22" stroke-width="4" stroke-linejoin="round"/>
  <line x1="200" y1="234" x2="160" y2="234" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M148,234 L161,228 L161,240 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="120" y="219.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="316" y="45.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{ennen}$</div></foreignObject>
  <line x1="328" y1="140" x2="548" y2="140" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <rect x="545" y="78" width="6" height="124" rx="3" fill="#8a96a3"/>
  <ellipse cx="548" cy="140" rx="11" ry="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M328,140 L329,140 L330,140 L331,140 L332,140 L333,140 L334,140 L335,140 L336,140 L337,140 L338,140 L339,140 L340,140 L341,140 L342,140 L343,140 L344,140 L345,140 L346,140 L347,140 L348,140 L349,140 L350,140 L351,140 L352,140 L353,139.5 L354,139.5 L355,139.5 L356,139.5 L357,139.5 L358,139.5 L359,139 L360,139 L361,139 L362,138.5 L363,138.5 L364,138 L365,137.5 L366,137.5 L367,137 L368,136.5 L369,136 L370,135 L371,134.5 L372,134 L373,133 L374,132 L375,131 L376,130 L377,129 L378,128 L379,126.5 L380,125.5 L381,124 L382,122.5 L383,121 L384,119.5 L385,118 L386,116.5 L387,115 L388,113.5 L389,112 L390,110.5 L391,109 L392,107.5 L393,106 L394,105 L395,104 L396,103 L397,102 L398,101.5 L399,100.5 L400,100.5 L401,100 L402,100 L403,100 L404,100.5 L405,100.5 L406,101.5 L407,102 L408,103 L409,104 L410,105 L411,106 L412,107.5 L413,109 L414,110.5 L415,112 L416,113.5 L417,115 L418,116.5 L419,118 L420,119.5 L421,121 L422,122.5 L423,124 L424,125.5 L425,126.5 L426,128 L427,129 L428,130 L429,131 L430,132 L431,133 L432,134 L433,134.5 L434,135 L435,136 L436,136.5 L437,137 L438,137.5 L439,137.5 L440,138 L441,138.5 L442,138.5 L443,139 L444,139 L445,139 L446,139.5 L447,139.5 L448,139.5 L449,139.5 L450,139.5 L451,139.5 L452,140 L453,140 L454,140 L455,140 L456,140 L457,140 L458,140 L459,140 L460,140 L461,140 L462,140 L463,140 L464,140 L465,140 L466,140 L467,140 L468,140 L469,140 L470,140 L471,140 L472,140 L473,140 L474,140 L475,140 L476,140 L477,140 L478,140 L479,140 L480,140 L481,140 L482,140 L483,140 L484,140 L485,140 L486,140 L487,140 L488,140 L489,140 L490,140 L491,140 L492,140 L493,140 L494,140 L495,140 L496,140 L497,140 L498,140 L499,140 L500,140 L501,140 L502,140 L503,140 L504,140 L505,140 L506,140 L507,140 L508,140 L509,140 L510,140 L511,140 L512,140 L513,140 L514,140 L515,140 L516,140 L517,140 L518,140 L519,140 L520,140 L521,140 L522,140 L523,140 L524,140 L525,140 L526,140 L527,140 L528,140 L529,140 L530,140 L531,140 L532,140 L533,140 L534,140 L535,140 L536,140 L537,140 L538,140 L539,140 L540,140 L541,140 L542,140 L543,140 L544,140 L545,140 L546,140 L547,140 L548,140" fill="none" stroke="#8a5f22" stroke-width="4" stroke-linejoin="round"/>
  <line x1="376" y1="74" x2="416" y2="74" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M428,74 L415,80 L415,68 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="436" y="59.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="316" y="211.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{jälkeen}$</div></foreignObject>
  <line x1="328" y1="300" x2="548" y2="300" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <rect x="545" y="238" width="6" height="124" rx="3" fill="#8a96a3"/>
  <ellipse cx="548" cy="300" rx="11" ry="5" fill="none" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M328,300 L329,300 L330,300 L331,300 L332,300 L333,300 L334,300 L335,300 L336,300 L337,300 L338,300 L339,300 L340,300 L341,300 L342,300 L343,300 L344,300 L345,300 L346,300 L347,300 L348,300 L349,300 L350,300 L351,300 L352,300 L353,300 L354,300 L355,300 L356,300 L357,300 L358,300 L359,300 L360,300 L361,300 L362,300 L363,300 L364,300 L365,300 L366,300 L367,300 L368,300 L369,300 L370,300 L371,300 L372,300 L373,300 L374,300 L375,300 L376,300 L377,300 L378,300 L379,300 L380,300 L381,300 L382,300 L383,300 L384,300 L385,300 L386,300 L387,300 L388,300 L389,300 L390,300 L391,300 L392,300 L393,300 L394,300 L395,300 L396,300 L397,300 L398,300 L399,300 L400,300 L401,300 L402,300 L403,300 L404,300 L405,300 L406,300 L407,300 L408,300 L409,300 L410,300 L411,300 L412,300 L413,300 L414,300 L415,300 L416,300 L417,300 L418,300 L419,300 L420,300 L421,300 L422,300 L423,300 L424,300 L425,299.5 L426,299.5 L427,299.5 L428,299.5 L429,299.5 L430,299.5 L431,299 L432,299 L433,299 L434,298.5 L435,298.5 L436,298 L437,297.5 L438,297.5 L439,297 L440,296.5 L441,296 L442,295 L443,294.5 L444,294 L445,293 L446,292 L447,291 L448,290 L449,289 L450,288 L451,286.5 L452,285.5 L453,284 L454,282.5 L455,281 L456,279.5 L457,278 L458,276.5 L459,275 L460,273.5 L461,272 L462,270.5 L463,269 L464,267.5 L465,266 L466,265 L467,264 L468,263 L469,262 L470,261.5 L471,260.5 L472,260.5 L473,260 L474,260 L475,260 L476,260.5 L477,260.5 L478,261.5 L479,262 L480,263 L481,264 L482,265 L483,266 L484,267.5 L485,269 L486,270.5 L487,272 L488,273.5 L489,275 L490,276.5 L491,278 L492,279.5 L493,281 L494,282.5 L495,284 L496,285.5 L497,286.5 L498,288 L499,289 L500,290 L501,291 L502,292 L503,293 L504,294 L505,294.5 L506,295 L507,296 L508,296.5 L509,297 L510,297.5 L511,297.5 L512,298 L513,298.5 L514,298.5 L515,299 L516,299 L517,299 L518,299.5 L519,299.5 L520,299.5 L521,299.5 L522,299.5 L523,299.5 L524,300 L525,300 L526,300 L527,300 L528,300 L529,300 L530,300 L531,300 L532,300 L533,300 L534,300 L535,300 L536,300 L537,300 L538,300 L539,300 L540,300 L541,300 L542,300 L543,300 L544,300 L545,300 L546,300 L547,300 L548,300" fill="none" stroke="#8a5f22" stroke-width="4" stroke-linejoin="round"/>
  <line x1="500" y1="234" x2="460" y2="234" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M448,234 L461,228 L461,240 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="420" y="219.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
</svg>

### Huygensin periaate
Hollantilainen Christiaan Huygens esitti 1600-luvulla periaatteen, jolla aallon etenemistä voi päätellä piirtämällä. **Huygensin periaatteen** mukaan aaltorintaman jokainen piste toimii uuden pienen ympyräaallon, alkeisaallon, lähteenä. Alkeisaallot etenevät samalla nopeudella kuin alkuperäinen aalto, ja hetken kuluttua uusi aaltorintama on viiva, joka sivuaa kaikkia alkeisaaltoja. Avoimessa vedessä alkeisaaltojen sivuaja on taas suora, joten tasoaalto jatkaa suoraan. Kun osa rintamasta pysähtyy esteeseen tai kimpoaa seinästä, jäljelle jääneet alkeisaallot kertovat, mihin aalto etenee.

### Diffraktio
Kun aalto kulkee raosta tai esteen ohi, se taipuu myös esteen taakse, alueelle, jonne suoraan etenevä säde ei osu. Tätä kutsutaan **diffraktioksi** eli taipumiseksi. Huygensin periaate selittää sen: raon kohdalla olevat rintaman pisteet ovat alkeisaaltojen lähteitä, ja reunimmaisten pisteiden alkeisaallot leviävät sivuille. Raon leveyttä merkitään $b$. Jos rako on monta aallonpituutta leveä, rintama jatkaa raon kohdalla lähes suorana ja kaartuu vain reunoilta. Kun rako on selvästi aallonpituutta kapeampi, eli $b < \lambda$, alkeisaaltoja on raon kohdalla kuin yhdestä pisteestä, ja aalto leviää puoliympyränä koko alueelle raon taakse. Jo silloin, kun rako on suunnilleen aallonpituuden levyinen, $b \approx \lambda$, aalto leviää paljon.

<svg data-fig="diffraktio" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei mittakaavassa: tasoaalto tulee vasemmalta esteeseen, jossa on rako, ylhäältä katsottuna. Vasemmalla rako on noin neljän aallonpituuden levyinen: raon kohdalla aaltorintamat jatkavat suorina, ja vain reunoilla ne kaartuvat hieman varjoon. Raon pisteisiin on piirretty pienet Huygensin alkeisaallot. Oikealla rako on aallonpituutta kapeampi: raon takana aaltorintamat ovat puoliympyröitä, ja aalto leviää koko alueelle raon taakse." style="max-width:100%;font-size:24px">
  <defs><clipPath id="fy511-diffclip0"><rect x="12" y="44" width="276" height="292" rx="8"/></clipPath><clipPath id="fy511-diffclip1"><rect x="312" y="44" width="276" height="292" rx="8"/></clipPath></defs>
  <foreignObject x="121" y="7.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$b \approx 4\lambda$</div></foreignObject>
  <foreignObject x="427.5" y="7.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$b < \lambda$</div></foreignObject>
  <line x1="300" y1="40" x2="300" y2="348" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <rect x="12" y="44" width="276" height="292" rx="8" fill="#eef5f9"/>
  <g clip-path="url(#fy511-diffclip0)"><line x1="26" y1="44" x2="26" y2="336" stroke="#2f74b5" stroke-width="3"/><line x1="52" y1="44" x2="52" y2="336" stroke="#2f74b5" stroke-width="3"/><line x1="78" y1="44" x2="78" y2="336" stroke="#2f74b5" stroke-width="3"/><path d="M82,112 A26,26 0 0 1 108,138 L108,242 A26,26 0 0 1 82,268" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.94"/><path d="M82,86 A52,52 0 0 1 134,138 L134,242 A52,52 0 0 1 82,294" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.88"/><path d="M82,60 A78,78 0 0 1 160,138 L160,242 A78,78 0 0 1 82,320" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.82"/><path d="M82,34 A104,104 0 0 1 186,138 L186,242 A104,104 0 0 1 82,346" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.76"/><path d="M82,8 A130,130 0 0 1 212,138 L212,242 A130,130 0 0 1 82,372" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.70"/><path d="M82,-18 A156,156 0 0 1 238,138 L238,242 A156,156 0 0 1 82,398" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.64"/><path d="M82,-44 A182,182 0 0 1 264,138 L264,242 A182,182 0 0 1 82,424" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.58"/><path d="M82,-70 A208,208 0 0 1 290,138 L290,242 A208,208 0 0 1 82,450" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.52"/></g>
  <rect x="77" y="44" width="10" height="94" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="77" y="242" width="10" height="94" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M82,140 A11,11 0 0 1 82,162" fill="none" stroke="#4f8fbf" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="82" cy="151" r="4" fill="#1f2933"/>
  <path d="M82,166 A11,11 0 0 1 82,188" fill="none" stroke="#4f8fbf" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="82" cy="177" r="4" fill="#1f2933"/>
  <path d="M82,192 A11,11 0 0 1 82,214" fill="none" stroke="#4f8fbf" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="82" cy="203" r="4" fill="#1f2933"/>
  <path d="M82,218 A11,11 0 0 1 82,240" fill="none" stroke="#4f8fbf" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="82" cy="229" r="4" fill="#1f2933"/>
  <line x1="20" y1="318" x2="50" y2="318" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M62,318 L49,324 L49,312 Z" fill="#1971c2" stroke-linejoin="round"/>
  <rect x="312" y="44" width="276" height="292" rx="8" fill="#eef5f9"/>
  <g clip-path="url(#fy511-diffclip1)"><line x1="326" y1="44" x2="326" y2="336" stroke="#2f74b5" stroke-width="3"/><line x1="352" y1="44" x2="352" y2="336" stroke="#2f74b5" stroke-width="3"/><line x1="378" y1="44" x2="378" y2="336" stroke="#2f74b5" stroke-width="3"/><path d="M382,164 A26,26 0 0 1 382,216" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.92"/><path d="M382,138 A52,52 0 0 1 382,242" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.84"/><path d="M382,112 A78,78 0 0 1 382,268" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.76"/><path d="M382,86 A104,104 0 0 1 382,294" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.68"/><path d="M382,60 A130,130 0 0 1 382,320" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.60"/><path d="M382,34 A156,156 0 0 1 382,346" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.52"/><path d="M382,8 A182,182 0 0 1 382,372" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.44"/><path d="M382,-18 A208,208 0 0 1 382,398" fill="none" stroke="#2f74b5" stroke-width="3" stroke-opacity="0.36"/></g>
  <rect x="377" y="44" width="10" height="133" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="377" y="203" width="10" height="133" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="382" cy="190" r="4" fill="#1f2933"/>
  <line x1="320" y1="318" x2="350" y2="318" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M362,318 L349,324 L349,312 Z" fill="#1971c2" stroke-linejoin="round"/>
</svg>

Sama pätee esteeseen. Laituripaalun kaltainen este, joka on aallonpituutta kapeampi, ei juuri jätä taakseen varjoa, koska aalto taipuu sen ympäri. Aallonpituutta paljon leveämmän esteen taakse jää suojaisa alue. Diffraktio on siis voimakasta silloin, kun raon tai esteen leveys on aallonpituuden suuruusluokkaa tai pienempi. Ääni taipuu ovesta käytävään, koska puheäänen aallonpituus on noin metrin suuruusluokkaa, oviaukon levyinen.

## Kaava: Heijastuslaki
Kun aalto osuu tasaiseen pintaan, kuten seinään tai rantamuuriin, osumakohtaan piirretään pinnan **normaali** eli pintaa vastaan kohtisuora suora. Kulmat mitataan aina normaalista: tulokulma on tulevan säteen ja normaalin välinen kulma ja heijastuskulma heijastuneen säteen ja normaalin välinen kulma. Heijastuslaki on
```latex
\beta = \alpha
```
missä $\alpha$ on tulokulma ja $\beta$ heijastuskulma. Lisäksi tuleva säde, heijastunut säde ja normaali ovat samassa tasossa, ja heijastunut säde on normaalin toisella puolella kuin tuleva. Säteen ja pinnan välinen kulma on $90^\circ - \alpha$, eikä sitä käytetä tulokulmana.

<svg data-fig="heijastuslaki" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva: tuleva säde osuu seinän pintaan kohdassa O, ja heijastunut säde lähtee siitä. Kohdasta O on piirretty katkoviivalla pinnan normaali eli pintaa vastaan kohtisuora suora. Tulokulma alfa on tulevan säteen ja normaalin välinen kulma ja heijastuskulma beeta heijastuneen säteen ja normaalin välinen kulma; molemmat ovat 40 astetta. Harmaalla on merkitty säteen ja pinnan välinen kulma, 90 astetta miinus alfa, jota ei käytetä tulokulmana." style="max-width:100%;font-size:24px">
  <rect x="12" y="262" width="576" height="22" fill="#c4ccd4"/>
  <line x1="20" y1="282" x2="34" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="38" y1="282" x2="52" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="282" x2="70" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="74" y1="282" x2="88" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="282" x2="106" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="282" x2="124" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="128" y1="282" x2="142" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="146" y1="282" x2="160" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="164" y1="282" x2="178" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="182" y1="282" x2="196" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="282" x2="214" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="218" y1="282" x2="232" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="236" y1="282" x2="250" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="254" y1="282" x2="268" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="272" y1="282" x2="286" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="290" y1="282" x2="304" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="308" y1="282" x2="322" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="326" y1="282" x2="340" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="344" y1="282" x2="358" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="362" y1="282" x2="376" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="282" x2="394" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="398" y1="282" x2="412" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="416" y1="282" x2="430" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="434" y1="282" x2="448" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="452" y1="282" x2="466" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="282" x2="484" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="488" y1="282" x2="502" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="506" y1="282" x2="520" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="524" y1="282" x2="538" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="542" y1="282" x2="556" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="560" y1="282" x2="574" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="578" y1="282" x2="592" y2="266" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="12" y1="262" x2="588" y2="262" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="300" y1="262" x2="300" y2="66" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <foreignObject x="246" y="33.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{normaali}$</div></foreignObject>
  <line x1="158.5" y1="93.5" x2="288.5" y2="248" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M297.5,259 L282.5,252 L293,243 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="300" y1="262" x2="432.5" y2="104" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M441.5,93.5 L437,109.5 L426.5,100.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M300,190 A72,72 0 0 0 253.5,207" fill="none" stroke="#2b8a3e" stroke-width="3"/>
  <path d="M346.5,207 A72,72 0 0 0 300,190" fill="none" stroke="#2b8a3e" stroke-width="3"/>
  <foreignObject x="257" y="157.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\alpha$</div></foreignObject>
  <foreignObject x="323" y="157.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\beta$</div></foreignObject>
  <path d="M217.5,164 A128,128 0 0 0 172,262" fill="none" stroke="#6b7480" stroke-width="2" stroke-dasharray="5 4"/>
  <foreignObject x="88" y="183.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$90^\circ - \alpha$</div></foreignObject>
  <foreignObject x="290" y="293.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <line x1="300" y1="266" x2="300" y2="292" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="20" y="57.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{tuleva säde}$</div></foreignObject>
  <foreignObject x="385" y="57.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{heijastunut säde}$</div></foreignObject>
  <foreignObject x="510" y="225.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{seinä}$</div></foreignObject>
</svg>

Huygensin periaate selittää, miksi kulmat ovat yhtä suuret. Tasoaallon rintama $AB$ osuu seinään vinosti, joten sen piste $A$ koskettaa seinää ensin. Siitä lähtee alkeisaalto, kun rintaman toinen pää $B$ on vielä matkan päässä. Kun $B$ saapuu seinälle kohtaan $C$, $A$:sta lähtenyt alkeisaalto on edennyt saman matkan, koska nopeus on sama. Heijastunut rintama $CD$ sivuaa alkeisaaltoja. Kolmiot $ABC$ ja $CDA$ ovat yhtenevät: niillä on yhteinen sivu $AC$, yhtä pitkät sivut $BC$ ja $AD$ sekä suora kulma kohdissa $B$ ja $D$. Siksi rintamat muodostavat seinän kanssa yhtä suuret kulmat. Rintaman ja seinän välinen kulma on yhtä suuri kuin säteen ja normaalin välinen kulma, joten $\beta = \alpha$.

<svg data-fig="huygens" viewBox="0 0 600 350" role="img" aria-label="Kaavakuva: Huygensin periaate selittää heijastuslain. Tasoaallon aaltorintama AB osuu vinosti seinään: piste A on jo seinällä, kun piste B on vielä matkan päässä. Kun B etenee säteen suuntaan seinälle kohtaan C, kohdasta A lähtenyt alkeisaalto on ehtinyt yhtä pitkän matkan, ja sen säde on yhtä suuri kuin matka BC. Myös A:n ja C:n puolivälistä on piirretty pienempi alkeisaalto. Heijastunut aaltorintama CD sivuaa alkeisaaltoja. Rintama AB muodostaa seinän kanssa kulman alfa ja rintama CD kulman beeta, ja kulmat ovat yhtä suuret." style="max-width:100%;font-size:24px">
  <rect x="12" y="296" width="576" height="22" fill="#c4ccd4"/>
  <line x1="20" y1="316" x2="34" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="38" y1="316" x2="52" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="316" x2="70" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="74" y1="316" x2="88" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="316" x2="106" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="316" x2="124" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="128" y1="316" x2="142" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="146" y1="316" x2="160" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="164" y1="316" x2="178" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="182" y1="316" x2="196" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="316" x2="214" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="218" y1="316" x2="232" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="236" y1="316" x2="250" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="254" y1="316" x2="268" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="272" y1="316" x2="286" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="290" y1="316" x2="304" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="308" y1="316" x2="322" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="326" y1="316" x2="340" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="344" y1="316" x2="358" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="362" y1="316" x2="376" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="316" x2="394" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="398" y1="316" x2="412" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="416" y1="316" x2="430" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="434" y1="316" x2="448" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="452" y1="316" x2="466" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="316" x2="484" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="488" y1="316" x2="502" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="506" y1="316" x2="520" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="524" y1="316" x2="538" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="542" y1="316" x2="556" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="560" y1="316" x2="574" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="578" y1="316" x2="592" y2="300" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="12" y1="296" x2="588" y2="296" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M341,230.5 A211.5,211.5 0 0 0 61,100" fill="none" stroke="#4f8fbf" stroke-width="2" stroke-dasharray="6 5"/>
  <path d="M408,274 A105.5,105.5 0 0 0 201,274" fill="none" stroke="#4f8fbf" stroke-width="2" stroke-dasharray="6 5"/>
  <line x1="140" y1="296" x2="333" y2="134" stroke="#2f74b5" stroke-width="4" stroke-linecap="butt"/>
  <line x1="469" y1="296" x2="276" y2="134" stroke="#2f74b5" stroke-width="4" stroke-linecap="butt"/>
  <line x1="333" y1="134" x2="458.5" y2="283.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M467,293.5 L453,287 L463,279 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="140" y1="296" x2="267.5" y2="144" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M276,134 L271.5,149 L262,140.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="140" cy="296" r="5" fill="#1f2933"/>
  <circle cx="333" cy="134" r="5" fill="#1f2933"/>
  <circle cx="469" cy="296" r="5" fill="#1f2933"/>
  <circle cx="276" cy="134" r="5" fill="#1f2933"/>
  <circle cx="304.5" cy="296" r="5" fill="#1f2933"/>
  <path d="M194,296 A54,54 0 0 0 181.5,261.5" fill="none" stroke="#2b8a3e" stroke-width="3"/>
  <path d="M427.5,261.5 A54,54 0 0 0 415,296" fill="none" stroke="#2b8a3e" stroke-width="3"/>
  <foreignObject x="197.5" y="257" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\alpha$</div></foreignObject>
  <foreignObject x="391.5" y="257" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\beta$</div></foreignObject>
  <foreignObject x="108" y="263.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="481" y="263.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$C$</div></foreignObject>
  <foreignObject x="347" y="113.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$B$</div></foreignObject>
  <foreignObject x="242" y="113.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$D$</div></foreignObject>
  <foreignObject x="123.5" y="37.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{alkeisaalto}$</div></foreignObject>
  <line x1="160" y1="68" x2="106.5" y2="85" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
</svg>

## Esimerkki
Meren aallot saapuvat suoraa aallonmurtajaa kohti niin, että aaltorintamat muodostavat murtajan seinän kanssa $50^\circ$:n kulman. Mikä on aaltojen tulokulma ja heijastuskulma, ja mikä kulma heijastuneiden aaltojen etenemissuunnan ja murtajan seinän välille jää?

<!-- vaihe -->

**Tunnetut ja kysytty.** Aaltorintaman ja seinän välinen kulma on $\varphi = 50^\circ$. Kysytään tulokulmaa $\alpha$, heijastuskulmaa $\beta$ ja heijastuneen säteen ja seinän pinnan välistä kulmaa $\gamma$.

<!-- vaihe -->

**Periaate.** Säde on kohtisuorassa aaltorintamaa vastaan ja normaali kohtisuorassa seinää vastaan. Kun kumpaakin suoraa käännetään $90^\circ$, niiden välinen kulma ei muutu, joten säteen ja normaalin välinen kulma on sama kuin rintaman ja seinän välinen kulma. Heijastuslain mukaan heijastuskulma on yhtä suuri kuin tulokulma, kun molemmat mitataan normaalista.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&\alpha = \varphi \\
&\beta = \alpha \\
&\gamma = 90^\circ - \beta
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: kaikki kulmat ovat asteina.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&\alpha = 50^\circ \\
&\beta = 50^\circ \\
&\gamma = 90^\circ - 50^\circ = 40^\circ
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Tulokulma ja heijastuskulma ovat $50^\circ$, ja heijastuneet aallot etenevät $40^\circ$:n kulmassa murtajan seinään nähden. Kulmat ilmoitetaan kokonaisina asteina kuten lähtötieto $50^\circ$.

<!-- vaihe -->

**Järkevyys.** Jos rintamat olisivat seinän suuntaiset, eli $\varphi = 0^\circ$, aallot tulisivat kohtisuoraan ja palaisivat samaa reittiä, $\alpha = \beta = 0^\circ$. Kun $\varphi$ kasvaa, aallot tulevat yhä loivemmin. Lisäksi $\alpha + \gamma = 90^\circ$, kuten normaalin ja pinnan välisen suoran kulman pitääkin.

## Yleinen virhekäsitys
Yleisin virhe on mitata tulokulma pinnasta eikä normaalista. Jos säde muodostaa seinän kanssa $30^\circ$:n kulman, tulokulma ei ole $30^\circ$ vaan $90^\circ - 30^\circ = 60^\circ$. Piirrä siksi aina ensin normaali osumakohtaan. Toinen virhe on ajatella, että aalto taipuu vain hyvin kapeassa raossa ja leveä rako päästää sen läpi täysin suorana. Diffraktiota on jokaisessa raossa ja jokaisen esteen reunalla, mutta se näkyy selvästi vasta, kun raon leveys on aallonpituuden suuruusluokkaa. Kolmas virhe on luulla, että kiinteä pää vaimentaa pulssin. Jäykästä kiinnityksestä pulssi heijastuu lähes kokonaan, mutta kääntyneenä.

## Tiivistelmä
- Aaltorintama yhdistää samassa vaiheessa olevat kohdat, ja säde näyttää etenemissuunnan kohtisuoraan rintamaa vastaan.
- Heijastuslaki: $\beta = \alpha$, kun tulokulma ja heijastuskulma mitataan pinnan normaalista.
- Köyden kiinteästä päästä pulssi heijastuu kääntyneenä, vapaasta päästä kääntymättä.
- Huygensin periaate: aaltorintaman jokainen piste on alkeisaallon lähde, ja uusi rintama sivuaa alkeisaaltoja. Periaate selittää heijastumisen ja diffraktion.
- Diffraktio eli aallon taipuminen raon tai esteen taakse on voimakasta, kun raon tai esteen leveys on suunnilleen aallonpituuden suuruinen tai pienempi.
