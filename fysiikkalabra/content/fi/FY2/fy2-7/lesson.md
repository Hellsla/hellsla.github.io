# Energian siirtäminen: sähkö ja lämpö

> **Miksi** voimalinjojen jännite on satoja kilovoltteja, vaikka pistorasiasta saa vain $230\,\text{V}$, ja miksi kaukolämpöputket kääritään paksuun eristeeseen?

## Ydinajatus

Energiaa tuotetaan usein kaukana siitä, missä sitä käytetään: voimalaitos on kaupungin ulkopuolella, mutta lämmitin ja pistorasia ovat kotona. Energia täytyy siis siirtää käyttäjälle. Suomessa se tapahtuu kahdella tavalla: **sähköenergiana** sähköverkossa ja **lämpöenergiana** kaukolämpöverkon vesiputkissa.

### Sähköverkko

**Sähköverkko** vie sähköenergian voimalaitokselta kotiin. Pitkät matkat kulkevat kantaverkon voimalinjoissa, joiden jännite on $110\text{–}400\,\text{kV}$. Lähempänä käyttäjää jännite lasketaan ensin $20\,\text{kV}$:iin ja lopuksi pienjänniteverkon $0{,}4\,\text{kV}$:iin, josta kodin pistorasiat saavat $230\,\text{V}$. Jännitteen muuttaminen tapahtuu muuntajissa.

<svg data-fig="grid" viewBox="0 0 600 332" role="img" aria-label="Kaavakuva sähköverkon reitistä voimalaitokselta kotiin. Vasemmalta oikealle: voimalaitos ja sen muuntaja, kantaverkon voimalinja (jännite 110 kV:sta 400 kV:iin), sähköasema, jakeluverkon pylväät (20 kV) ja koti (0,4 kV, pistorasiassa 230 V). Alla oranssi nuoli kuvaa energian kulkua voimalaitokselta kotiin. Kuva ei ole mittakaavassa." style="max-width:100%;font-size:24px">
  <line x1="12" y1="206" x2="588" y2="206" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="30" y="150" width="76" height="56" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="44" y="96" width="16" height="54" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <ellipse cx="58" cy="82" rx="14" ry="9" fill="#eef5f9" stroke="#c9c2b2" stroke-width="1.5"/><ellipse cx="72" cy="66" rx="12" ry="8" fill="#eef5f9" stroke="#c9c2b2" stroke-width="1.5"/>
  <rect x="76" y="166" width="18" height="22" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="118" y="172" width="34" height="34" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="130" cy="189" r="8" fill="none" stroke="#ffffff" stroke-width="2"/>
  <circle cx="141" cy="189" r="8" fill="none" stroke="#ffffff" stroke-width="2"/>
  <path d="M106,160 Q135,150 164,124" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M152,178 Q158,155 164,124" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M170,206 L185,112 L195,112 L210,206" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="176" y1="172" x2="204" y2="172" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="140" x2="200" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="177" y1="172" x2="200" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="203" y1="172" x2="180" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="160" y1="124" x2="220" y2="124" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="164" y1="124" x2="164" y2="132" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="216" y1="124" x2="216" y2="132" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M280,206 L295,112 L305,112 L320,206" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="286" y1="172" x2="314" y2="172" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="290" y1="140" x2="310" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="287" y1="172" x2="310" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="313" y1="172" x2="290" y2="140" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270" y1="124" x2="330" y2="124" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="274" y1="124" x2="274" y2="132" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="326" y1="124" x2="326" y2="132" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M164,124 Q217,152 270,124" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M216,124 Q245,144 274,124" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M326,124 Q349,157 372,150" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M190,124 Q230,148 270,124" fill="none" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <rect x="372" y="164" width="54" height="42" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="382" y="176" width="18" height="30" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="406" y="176" width="14" height="30" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="396" y1="164" x2="396" y2="150" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="380" y1="150" x2="412" y2="150" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="452" y1="206" x2="452" y2="142" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="438" y1="150" x2="466" y2="150" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="500" y1="206" x2="500" y2="142" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="486" y1="150" x2="514" y2="150" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M412,150 Q432,162 452,150" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M452,150 Q476,166 500,150" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M500,150 Q519,167 538,168" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="528" y="172" width="54" height="34" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M520,174 L555,142 L590,174 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="536" y="182" width="14" height="24" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="558" y="182" width="16" height="14" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="160" y="47.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$110\text{–}400\,\text{kV}$</div></foreignObject>
  <foreignObject x="426" y="93.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20\,\text{kV}$</div></foreignObject>
  <foreignObject x="506" y="47.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}4\,\text{kV}$</div></foreignObject>
  <foreignObject x="90" y="92" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{muuntaja}$</div></foreignObject>
  <line x1="135" y1="124" x2="135" y2="171" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="556" y1="82" x2="556" y2="130" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <foreignObject x="18" y="247.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{voimalaitos}$</div></foreignObject>
  <foreignObject x="175" y="247.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kantaverkko}$</div></foreignObject>
  <foreignObject x="325" y="281.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sähköasema}$</div></foreignObject>
  <foreignObject x="450" y="247.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{jakeluverkko}$</div></foreignObject>
  <path d="M30,235 L544,235 L544,243 L570,228 L544,213 L544,221 L30,221 Z" fill="#e8590c" stroke-linejoin="round"/>
</svg>

### Miksi pitkä matka siirretään korkealla jännitteellä

Saman tehon voi siirtää kahdella tavalla: pienellä jännitteellä ja suurella sähkövirralla tai suurella jännitteellä ja pienellä sähkövirralla. Johdin lämpenee sitä enemmän, mitä suurempi virta siinä kulkee, ja lämmitykseen menevä energia on häviötä. Siksi pitkä matka siirretään suurella jännitteellä, jolloin virta ja häviö jäävät pieniksi. Jännitteen, virran ja häviön tarkka yhteys kuuluu myöhempiin sähkökursseihin.

Muuntaja nostaa jännitteen voimalaitoksella ja laskee sen takaisin käyttäjän lähellä. Hyvässä muuntajassa häviö on hyvin pieni.

### Kaukolämpö

**Kaukolämpö** siirtää energian kuumana vetenä. Lämpölaitoksessa lämmitetty vesi virtaa menoputkessa rakennuksiin ja luovuttaa lämpöä rakennuksen lämmitysjärjestelmälle. Jäähtynyt vesi palaa paluuputkessa takaisin lämmitettäväksi. Putket ovat maan alla paksussa eristeessä, jotta lämpöä menisi ympäröivään maahan mahdollisimman vähän.

<svg data-fig="district" viewBox="0 0 600 320" role="img" aria-label="Kaavakuva kaukolämmön kierrosta. Vasemmalla lämpölaitos, oikealla koti. Punainen menoputki vie kuumaa vettä kotiin ja sininen paluuputki tuo jäähtyneen veden takaisin. Putket ovat yhteisen eristeen sisällä maan alla. Oranssit nuolet osoittavat, että eristeestäkin pääsee vähän lämpöä maahan. Kuva ei ole mittakaavassa." style="max-width:100%;font-size:24px">
  <rect x="20" y="124" width="86" height="80" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="34" y="80" width="16" height="44" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <ellipse cx="46" cy="66" rx="14" ry="9" fill="#eef5f9" stroke="#c9c2b2" stroke-width="1.5"/>
  <rect x="64" y="150" width="30" height="54" fill="#c92a2a" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M492,128 L546,84 L600,128 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="500" y="128" width="90" height="76" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="512" y="140" width="22" height="26" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="548" y="144" width="32" height="52" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="556" y1="148" x2="556" y2="192" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="564" y1="148" x2="564" y2="192" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="572" y1="148" x2="572" y2="192" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <rect x="106" y="120" width="394" height="78" rx="8" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="106" y="138" width="394" height="14" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <rect x="106" y="166" width="394" height="14" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <path d="M312,145 L293,137 L293,153 Z" fill="#ffffff" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M288,173 L307,165 L307,181 Z" fill="#ffffff" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M176,204 L176,222 L170,222 L180,236 L190,222 L184,222 L184,204 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M416,204 L416,222 L410,222 L420,236 L430,222 L424,222 L424,204 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="444" y="209.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{häviö}$</div></foreignObject>
  <foreignObject x="170" y="79.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{menovesi}$</div></foreignObject>
  <foreignObject x="165" y="253.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{paluuvesi}$</div></foreignObject>
  <foreignObject x="331" y="79.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{eriste}$</div></foreignObject>
  <line x1="376" y1="108" x2="376" y2="124" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="-7" y="247.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpölaitos}$</div></foreignObject>
  <foreignObject x="505" y="247.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{koti}$</div></foreignObject>
</svg>

### Siirtohäviö

Kummassakin verkossa osa energiasta muuttuu matkalla lämmöksi ympäristöön eikä tule perille. Tätä kutsutaan **siirtohäviöksi**. Energia ei katoa (luku *Energialajit ja energian säilyminen*), mutta häviö on käyttäjälle hyödytöntä.

Suomessa sähköverkon häviöt olivat vuonna 2024 noin $4\,\%$ sähkön kulutuksesta, kun kulutus oli noin $83\,\text{TWh}$ (Energiateollisuus, Sähkövuosi 2024). Kaukolämmön verkkoon hankittiin vuonna 2024 noin $36\,\text{TWh}$ ja asiakkaille käytettiin noin $32{,}7\,\text{TWh}$, joten noin $9\,\%$ jäi matkalle (Energiateollisuus, Kaukolämpötilasto 2024; osuus on laskettu erotuksesta, joten se on arvio). Kaukolämmön häviö on suhteessa suurempi, koska kuuma vesi on ympäristöä selvästi lämpimämpää: mitä suurempi lämpötilaero ympäristöön on, sitä enemmän lämpöä karkaa, ja lämpöä pääsee eristeen läpi koko putkiston pituudella.

### Energian siirtäminen ajassa: varastointi

Energiaa siirretään myös ajassa. Tuulivoimaa ja aurinkosähköä syntyy silloin, kun tuulee tai paistaa, mutta sähköä tarvitaan muulloinkin. Varasto ottaa energiaa vastaan silloin, kun sitä on liikaa, ja luovuttaa sen myöhemmin.

<svg data-fig="storage" viewBox="0 0 600 300" role="img" aria-label="Kaavakuva kolmesta energiavarastosta. Vasemmalla akku, jossa energia on kemiallista. Keskellä pumppuvoimala: ylempi allas, alempi allas ja putki, jossa vesi virtaa alas. Oikealla lämpövarasto, eristetty säiliö täynnä kuumaa vettä. Kuva ei ole mittakaavassa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy27-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy27-hot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2a69c"/><stop offset="1" stop-color="#c92a2a"/></linearGradient></defs>
  <rect x="60" y="100" width="80" height="110" rx="8" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="84" y="88" width="32" height="12" fill="#1f2933"/>
  <rect x="70" y="150" width="60" height="50" rx="4" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2"/>
  <line x1="100" y1="112" x2="100" y2="132" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="90" y1="122" x2="110" y2="122" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="90" y1="138" x2="110" y2="138" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M220,110 L330,110 L330,206 L186,206 Z" fill="#d9b26a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M220,110 L300,110 L300,128 L214,128 Z" fill="url(#fy27-water)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="190" y="190" width="72" height="16" fill="url(#fy27-water)" stroke="#1f2933" stroke-width="2"/>
  <line x1="290" y1="128" x2="290" y2="190" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="290" y1="190" x2="262" y2="198" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="290" cy="160" r="9" fill="none" stroke="#1f2933" stroke-width="3"/>
  <rect x="420" y="92" width="100" height="118" rx="14" fill="#f1dfb5" stroke="#1f2933" stroke-width="3"/>
  <rect x="430" y="102" width="80" height="98" rx="8" fill="url(#fy27-hot)" stroke="#1f2933" stroke-width="2"/>
  <line x1="470" y1="82" x2="470" y2="92" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="470" y1="210" x2="470" y2="222" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <foreignObject x="55" y="252.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{akku}$</div></foreignObject>
  <foreignObject x="160" y="252.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pumppuvoimala}$</div></foreignObject>
  <foreignObject x="375" y="252.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpövarasto}$</div></foreignObject>
  <foreignObject x="25" y="25.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kemiallinen}$</div></foreignObject>
  <foreignObject x="188" y="14" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{potentiaali-}$</div></foreignObject>
  <foreignObject x="188" y="42" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
  <foreignObject x="420" y="25.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpö}$</div></foreignObject>
  <foreignObject x="196" y="78" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{yläallas}$</div></foreignObject>
  <foreignObject x="176" y="210" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{alaallas}$</div></foreignObject>
  <line x1="184" y1="20" x2="184" y2="280" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="380" y1="20" x2="380" y2="280" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
</svg>

Akkuun energia varastoituu kemialliseksi energiaksi. Pumppuvoimalassa vettä pumpataan ylempään altaaseen, ja alas valuva vesi pyörittää voimalaitoksen koneita. Lämpövarastossa kuuma vesi säilyy eristetyssä säiliössä, ja sitä käytetään esimerkiksi kaukolämpöverkossa. Sähköä ei varastoida sellaisenaan vaan muuttamalla se toiseksi energialajiksi ja takaisin, ja jokaisessa muunnoksessa osa energiasta muuttuu lämmöksi.

## Kaava: Siirtohäviö

Häviö on verkkoon lähtevän ja perille tulevan energian erotus. Siirron hyötysuhde (luku *Hyötysuhde*) on perille tulevan energian osuus lähtevästä energiasta:

```latex
\begin{aligned}
E_\text{häviö} &= E_\text{lähtö} - E_\text{perille} \\
\eta &= \frac{E_\text{perille}}{E_\text{lähtö}}
\end{aligned}
```

missä $E_\text{lähtö}$ on verkkoon syötetty energia, $E_\text{perille}$ käyttäjälle asti tullut energia, $E_\text{häviö}$ matkalla lämmöksi muuttunut energia ja $\eta$ siirron hyötysuhde. Hyötysuhde annetaan prosentteina tai desimaalilukuna.

<svg data-fig="sankey" viewBox="0 0 600 330" role="img" aria-label="Energiavirtakuva mittakaavassa. Ylhäällä sähköverkko: lähtevästä energiasta 96 % tulee perille ja 4 % häviää. Alhaalla kaukolämpöverkko: 91 % tulee perille ja 9 % häviää. Virran leveys on verrannollinen energiaan; lähtevän energian leveys on molemmissa sama." style="max-width:100%;font-size:24px">
  <foreignObject x="12" y="17.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{sähkö}$</div></foreignObject>
  <rect x="150" y="52" width="121" height="80" fill="#e8590c"/>
  <polygon points="270,52 470,52 470,44 500,90.5 470,137 470,129 270,129" fill="#e8590c"/>
  <path d="M270,129 L330,129 C370,129 370,155 410,155 L460,155 L460,147 L490,156.5 L460,166 L460,158 L410,158 C370,158 370,132 330,132 L270,132 Z" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="50" y="77.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100\,\%$</div></foreignObject>
  <foreignObject x="510" y="76" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$96\,\%$</div></foreignObject>
  <foreignObject x="506" y="142" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$4\,\%$</div></foreignObject>
  <foreignObject x="12" y="175.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kaukolämpö}$</div></foreignObject>
  <rect x="150" y="210" width="121" height="80" fill="#e8590c"/>
  <polygon points="270,210 470,210 470,202 500,246.5 470,291 470,283 270,283" fill="#e8590c"/>
  <path d="M270,283 L330,283 C370,283 370,309 410,309 L460,309 L460,301 L490,312.5 L460,324 L460,316 L410,316 C370,316 370,290 330,290 L270,290 Z" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="50" y="235.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100\,\%$</div></foreignObject>
  <foreignObject x="510" y="232" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$91\,\%$</div></foreignObject>
  <foreignObject x="506" y="298" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$9\,\%$</div></foreignObject>
</svg>

Kuvassa virran leveys kuvaa energian määrää. Sähköverkossa $4\,\%$ lähtevästä energiasta häviää ja $96\,\%$ tulee perille, kaukolämmössä $9\,\%$ ja $91\,\%$.

### Laskeminen häviöprosentista

Häviöprosentti kerrotaan aina lähtevästä energiasta. Jos häviö on $9{,}0\,\%$, perille tulee $100\,\% - 9{,}0\,\% = 91{,}0\,\%$ lähtevästä, ja $91{,}0\,\% = 91{,}0 : 100 = 0{,}910$. Kaavasta ratkaistaan tarvittava energia: $E_\text{perille} = \eta\, E_\text{lähtö}$ ja $E_\text{lähtö} = E_\text{perille} : \eta$.

Sama koskee tehoa: perille tuleva teho on $\eta$ kertaa lähtevä teho. Energia ja teho liittyvät toisiinsa kaavalla $P = \tfrac{E}{t}$ (luku *Teho*), joten tasaisella häviöteholla $P_\text{häviö}$ aikana $t$ häviää energiaa $E_\text{häviö} = P_\text{häviö} \cdot t$.

## Esimerkki

Kaukolämpöverkko siirtää lämpölaitokselta kaupunginosaan $245\,\text{MWh}$ lämpöenergiaa viikossa (esimerkkitilanne). Verkon häviö on $9{,}0\,\%$ lähtevästä energiasta. Kuinka paljon energiaa tulee perille ja kuinka paljon sitä häviää?

<!-- vaihe -->

**Tunnetut ja kysytty.** $E_\text{lähtö} = 245\,\text{MWh}$ ja häviö $9{,}0\,\%$ lähtevästä energiasta. Kysytään perille tulevaa energiaa $E_\text{perille}$ ja häviötä $E_\text{häviö}$.

<!-- vaihe -->

**Periaate.** Energia ei katoa, joten lähtevä energia on yhtä suuri kuin perille tuleva ja häviävä energia yhteensä. Kun $9{,}0\,\%$ häviää, loput $91{,}0\,\%$ tulee perille, eli hyötysuhde on $\eta = 0{,}910$.

<!-- vaihe -->

**Kaava ratkaistuna.**

```latex
\begin{aligned}
&E_\text{perille} = \eta\, E_\text{lähtö} \\
&E_\text{häviö} = E_\text{lähtö} - E_\text{perille}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Hyötysuhde saadaan prosentista: $\eta = 100\,\% - 9{,}0\,\% = 91{,}0\,\% = 91{,}0 : 100 = 0{,}910$. Energiat ovat samassa yksikössä, megawattitunneissa, joten muuta muunnosta ei tarvita.

<!-- vaihe -->

**Sijoitus.**

```latex
\begin{aligned}
E_\text{perille} &= \eta\, E_\text{lähtö} \\
&= 0{,}910 \cdot 245\,\text{MWh} \\
&= 222{,}95\,\text{MWh} \\
E_\text{häviö} &= E_\text{lähtö} - E_\text{perille} \\
&= 245\,\text{MWh} - 222{,}95\,\text{MWh} \\
&= 22{,}05\,\text{MWh}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Perille tulee noin $223\,\text{MWh}$ ja häviää noin $22\,\text{MWh}$. Perille tuleva energia ilmoitetaan kolmella merkitsevällä numerolla, koska hyötysuhde $0{,}910$ ja lähtöenergia $245\,\text{MWh}$ tunnetaan kolmen numeron tarkkuudella. Häviö ilmoitetaan kahdella merkitsevällä numerolla, koska häviöprosentti $9{,}0\,\%$ tunnetaan vain kahden numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Kymmenen prosenttia energiasta $245\,\text{MWh}$ olisi $24{,}5\,\text{MWh}$, ja $9{,}0\,\%$ on hieman vähemmän, joten häviö $22\,\text{MWh}$ on oikean suuruinen. Lisäksi $222{,}95\,\text{MWh} + 22{,}05\,\text{MWh} = 245\,\text{MWh}$, eli energia säilyy.

## Yleinen virhekäsitys

Moni ajattelee, että siirtohäviössä energia katoaa. Energia ei katoa: se muuttuu lämmöksi, joka lämmittää johtimia, putkia ja niiden ympäristöä, eikä käyttäjä saa sitä hyötyyn.

Toinen virhe on laskea häviöprosentti perille tulevasta energiasta. Prosentti kuuluu laskea lähtevästä energiasta: jos häviö on $9{,}0\,\%$ ja perille tulee $245\,\text{MWh}$, lähtevä energia ei ole $245\,\text{MWh} + 0{,}090 \cdot 245\,\text{MWh}$ vaan $245\,\text{MWh} : 0{,}910$.

Kolmas virhe on ajatella, että häviö vähennetään yksikkönä prosentista: häviö $4\,\%$ ei tarkoita $4\,\text{MWh}$ vaan neljää sadasosaa lähtevästä energiasta.

## Tiivistelmä

- Sähköenergia siirretään sähköverkossa, pitkät matkat korkealla jännitteellä, koska silloin virta on pieni ja johtimien lämpenemisestä aiheutuva häviö vähäinen. Muuntajat nostavat ja laskevat jännitettä.
- Lämpöenergia siirretään kaukolämpöverkossa kuumana vetenä eristetyissä putkissa. Suomessa sähköverkon häviöt olivat noin $4\,\%$ ja kaukolämpöverkon noin $9\,\%$ (Energiateollisuus, 2024).
- Siirtohäviö $E_\text{häviö} = E_\text{lähtö} - E_\text{perille}$ ja siirron hyötysuhde $\eta = E_\text{perille} : E_\text{lähtö}$. Häviöprosentti lasketaan lähtevästä energiasta.
- Varastot (akku, pumppuvoimala, lämpövarasto) siirtävät energiaa ajassa, mutta niissäkin osa energiasta muuttuu lämmöksi.
