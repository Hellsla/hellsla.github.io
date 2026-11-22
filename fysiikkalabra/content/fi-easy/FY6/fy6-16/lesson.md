# Soveltava luku: sähköauto ja kodin sähköjärjestelmä

> **Miksi** sähköautoa ei kannata ladata jatkojohdolla tavallisesta pistorasiasta? Riittävätkö kodin sähköt saunaan ja auton lataukseen yhtä aikaa?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvi-ilta ja punainen omakotitalo lumen keskellä. Talon ikkunoista loistaa valo, ja saunan piipusta nousee savua. Talon päätyseinällä on latausasema, josta kiemurteleva latauskaapeli kulkee pihalla seisovan sinisen sähköauton etuoven alla olevaan latausliitäntään. Taustalla on kuusia ja sähkölinjan pylväs, josta johdot tulevat talon katolle." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-16-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Akku, teho ja latausaika
Sähköauton akku on suuri litiumioniakku (luku *Akut ja latauspiiri*). Tässä luvussa käytetään esimerkkiautoa. Sen akun nimellisjännite on $400\,\text{V}$ ja kapasiteetti $160\,\text{Ah}$. Nimellisjännite on jännite, jonka akku yleensä antaa. Akun energia on silloin $$\begin{aligned} W &= UQ \\ &= 400\,\text{V} \cdot 160\,\text{Ah} \\ &= 64\,\text{kWh} \end{aligned}$$. Energia riittää noin $350\,\text{km}$:n ajoon, kun auto käyttää $18\,\text{kWh}$ sadalla kilometrillä. Akkuun mahtuu siis yhtä paljon energiaa kuin $6\,\text{kW}$:n kiuas käyttää yli kymmenessä tunnissa.

Latausaika riippuu kahdesta asiasta. Ensimmäinen on se, kuinka paljon energiaa akkuun pitää siirtää. Toinen on se, kuinka suurella teholla energia siirretään. Latauksessa osa verkosta otetusta energiasta ei päädy akkuun. Se muuttuu auton laturin, johtojen ja akun sisäenergiaksi, joka siirtyy lämpönä ympäristöön. Kotilatauksen hyötysuhde on tyypillisesti noin $80\text{–}95\,\%$. Hyötysuhde kertoo, kuinka suuri osa verkosta otetusta energiasta päätyy akkuun. Se jää aina alle $100\,\%$. Verkosta on siksi otettava enemmän energiaa kuin akkuun varastoituu.

<figure class="unit-photo"><img src="pics/fy6/ev-charging-socket.webp" alt="Valkoisen auton keulassa on auki oleva luukku. Sen alla on kaksi latausliitäntää."><figcaption>Sähköauton latausliitännät. Isommalla liitännällä ladataan nopeasti tasavirralla. Pienemmällä ladataan vaihtovirralla. Silloin auton oma laturi muuttaa vaihtovirran tasavirraksi akkua varten.</figcaption></figure>

```pysahdy
Latauksen hyötysuhde on $0{,}85$. Mitä se tarkoittaa verkosta otetulle energialle? Minne loppu menee?
---
Vain $85\,\%$ verkosta otetusta energiasta siirtyy akkuun. Loput $15\,\%$ muuttuu laturin, johtojen ja akun sisäenergiaksi.
```

### Yksi vaihe vai kolme
Suomalaiseen omakotitaloon tulee yleensä **kolmivaihesähkö**. Siinä on kolme vaihejohdinta $\text{L}_1$, $\text{L}_2$ ja $\text{L}_3$ sekä nollajohdin $\text{N}$. Vaihejohdin on johto, jossa on jännite. Jokaisen vaihejohtimen ja nollajohtimen välillä on jännite $230\,\text{V}$. Tavallinen pistorasia ja vedenkeitin käyttävät yhtä vaihetta. Kiuas ja latausasema käyttävät yleensä kaikkia kolmea vaihetta. Kun laite ottaa jokaisesta vaihejohtimesta saman virran $I$, jokainen vaihe siirtää tehon $UI$. Kokonaisteho on silloin kolminkertainen. Vaihejohtimien välinen jännite on $400\,\text{V}$, mutta sitä ei tässä tarvita.

Laitteen virta saadaan tehosta samalla tavalla kuin luvussa *Sähköenergia kotona*. Yhdessä vaiheessa $I = P : U$. Tavallisesta pistorasiasta ladattaessa latauskaapeli rajoittaa virran yleensä noin $8\,\text{A}$:iin. Teho on silloin $230\,\text{V} \cdot 8\,\text{A} \approx 1{,}8\,\text{kW}$. Yksivaiheinen latausasema, jonka virta on $16\,\text{A}$, lataa teholla noin $3{,}7\,\text{kW}$. Kolmivaiheinen asema lataa samalla virralla kolminkertaisella teholla, noin $11\,\text{kW}$. Sama $40\,\text{kWh}$:n lataus kestää pistorasiasta yli vuorokauden, kun latauksen häviöt otetaan huomioon. Kolmivaiheisella asemalla se kestää noin neljä tuntia.

```pysahdy
Kolmivaiheisen latausaseman teho on $6{,}9\,\text{kW}$ ja vaihejännite $230\,\text{V}$. Kuinka suuri on virta jokaisessa vaihejohtimessa?
---
Kaavasta $P = 3UI$ saadaan $I = \tfrac{P}{3U}$, joten $I = \tfrac{6900\,\text{W}}{3 \cdot 230\,\text{V}} = 10\,\text{A}$.
```

### Kodin sähköjärjestelmä
Sähköverkosta tuleva kaapeli kulkee mittarin kautta **sähkökeskukseen**. Keskuksessa ovat ensin **pääsulakkeet**. Jokaisessa vaihejohtimessa on yksi pääsulake, esimerkiksi $3 \cdot 25\,\text{A}$. Pääsulakkeiden jälkeen virta jakautuu **ryhmiin**. Jokaisella ryhmällä on oma johto ja oma sulake tai johdonsuojakatkaisija, esimerkiksi $10\,\text{A}$ tai $16\,\text{A}$. Sulake suojaa johtoa. Se katkaisee virran, ennen kuin virta lämmittää johtoa vaarallisesti (luku *Sähköturvallisuus kotona ja työssä*). Siksi sulakkeen koko valitaan johdon poikkipinta-alan mukaan. Sulakkeen tilalle ei saa vaihtaa suurempaa.

<svg data-fig="koti" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva, ei mittakaavassa: kodin sähköjärjestelmä. Vasemmalla ylhäältä tulee sähköverkosta kolmen vaihejohtimen kaapeli sähkökeskukseen. Keskuksessa ovat ensin pääsulakkeet, kolme kappaletta, 25 ampeeria kukin, ja niiden alla kiskot, joista lähtee kolme ryhmää. Ylin ryhmä on kolmivaiheinen, sen johdonsuojakatkaisija on 16 ampeeria ja se syöttää sähkökiuasta. Keskimmäinen ryhmä on yksivaiheinen, 16 ampeeria, ja se syöttää keittiön pistorasioita, joihin on kytketty vedenkeitin. Alin ryhmä on latausaseman oma kolmivaiheinen ryhmä: siinä on 16 ampeerin johdonsuojakatkaisija ja vikavirtasuoja, jonka laukaisuvirta on 30 milliampeeria. Kolmivaiheiset johdot on piirretty kolmena viivana, yksivaiheinen yhtenä." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-16-koti.webp" x="0" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="112" y="15.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{sähköverkosta}$</div></foreignObject>
  <foreignObject x="120" y="87.5" width="98" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$3 \cdot 25\,\text{A}$</div></foreignObject>
  <foreignObject x="101" y="121.5" width="98" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3 \cdot 16\,\text{A}$</div></foreignObject>
  <foreignObject x="317" y="135.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kiuas}$</div></foreignObject>
  <foreignObject x="101" y="207.5" width="98" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$16\,\text{A}$</div></foreignObject>
  <foreignObject x="317" y="221.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pistorasiat}$</div></foreignObject>
  <foreignObject x="101" y="285.5" width="98" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3 \cdot 16\,\text{A}$</div></foreignObject>
  <foreignObject x="213" y="285.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30\,\text{mA}$</div></foreignObject>
  <foreignObject x="317" y="299.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{latausasema}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/ev-charging-station.webp" alt="Keltainen latausasema pysäköintihallissa. Sen ympärillä on keltaiset kaiteet."><figcaption>Sähköauton latausasema pysäköintihallissa Jyväskylässä. Asemalla on oma ryhmä, oma sulake ja oma vikavirtasuoja. Kaiteet suojaavat asemaa, jos auto törmää.</figcaption></figure>

### Miksi latausasemalla on oma ryhmä ja vikavirtasuoja
Auton lataus on kodin pisin suuri kuorma. Virta voi kulkea tuntikausia lähes ryhmän sulakkeen suuruisena. Jos samassa ryhmässä olisi muitakin pistorasioita, johto ja pistorasia olisivat tuntikausia lähes nimellisvirralla. Nimellisvirta on suurin virta, jolle johto on tehty. Pistorasian kosketuskohdat lämpenisivät, ja muut kuormat voisivat katkaista latauksen. Siksi sähköasennusstandardi vaatii, että jokaisella latauspisteellä on **oma ryhmä**. Ryhmä on mitoitettu latauspisteen virralle.

Latauspisteellä on myös oma **vikavirtasuoja**. Se katkaisee virran, jos osa virrasta vuotaa muuta reittiä ja ero on yli $30\,\text{mA}$. Virta voi vuotaa esimerkiksi märän kaapelin ja ihmisen kautta maahan. Ulkona kaapeli kastuu, jäätyy ja jää joskus renkaan alle. Eristeen vaurio on siksi todennäköisempi kuin sisällä. Ulos asennetun aseman kotelolla on kotelointiluokka (IP-luokka), esimerkiksi IP54. Se kertoo, että kotelo kestää pölyä ja roiskevettä.

### Pääsulake ja samanaikaiset kuormat
Pääsulakkeet rajoittavat koko talon virtaa. Kun pääsulakkeet ovat $3 \cdot 25\,\text{A}$, talo voi ottaa verkosta enintään noin $3 \cdot 230\,\text{V} \cdot 25\,\text{A} \approx 17\,\text{kW}$. Tämäkin pätee vain, jos kuorma jakautuu tasan kolmeen vaiheeseen. Ratkaisevaa on jokaisen vaihejohtimen oma virta. Kuvassa on yhtä aikaa päällä kolme laitetta. Ensimmäinen on $9{,}0\,\text{kW}$:n kiuas, joka ottaa jokaisesta vaiheesta $13{,}0\,\text{A}$. Toinen on $11\,\text{kW}$:n latausasema, joka ottaa jokaisesta vaiheesta $16\,\text{A}$. Kolmas on vedenkeitin vaiheessa $\text{L}_1$, ja se ottaa $8{,}7\,\text{A}$. Vaiheen $\text{L}_1$ virta on $37{,}7\,\text{A}$ ja muiden vaiheiden virta $29{,}0\,\text{A}$.

<svg data-fig="vaiheet" viewBox="0 0 600 340" role="img" aria-label="Vaakapylväskuvaaja mittakaavassa: pääsulakkeiden läpi kulkeva virta kussakin vaihejohtimessa L1, L2 ja L3, kun samaan aikaan ovat päällä 9,0 kilowatin kolmivaiheinen kiuas, 2,0 kilowatin vedenkeitin vaiheessa L1 ja 11 kilowatin kolmivaiheinen latausasema. Kiuas ottaa jokaisesta vaiheesta 13,0 ampeeria ja latausasema 16 ampeeria, vedenkeitin vaiheesta L1 8,7 ampeeria. Vaiheen L1 virta on 37,7 ampeeria ja vaiheiden L2 ja L3 29,0 ampeeria. Pystysuora katkoviiva 25 ampeerin kohdalla on pääsulakkeen koko: jokaisen vaiheen pylväs ulottuu sen yli." style="max-width:100%;font-size:24px">
  <line x1="176" y1="56" x2="176" y2="284" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="176" y1="284" x2="176" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="159.5" y="293.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="276" y1="56" x2="276" y2="284" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="276" y1="284" x2="276" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="259.5" y="293.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="376" y1="56" x2="376" y2="284" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="376" y1="284" x2="376" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="359.5" y="293.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="476" y1="56" x2="476" y2="284" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="284" x2="476" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="459.5" y="293.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <foreignObject x="46" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="75" y1="284" x2="490" y2="284" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,284 L489,290 L489,278 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="508" y="269.5" width="64" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{A})$</div></foreignObject>
  <line x1="76" y1="56" x2="76" y2="284" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="18" y="81.5" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{L}_1$</div></foreignObject>
  <rect x="76" y="73" width="130.5" height="46" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="79" y="81.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kiuas}$</div></foreignObject>
  <rect x="206.5" y="73" width="160" height="46" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="209.5" y="81.5" width="154" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{auto}$</div></foreignObject>
  <rect x="366.5" y="73" width="87" height="46" fill="#a5d8ff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="369.5" y="81.5" width="81" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{keitin}$</div></foreignObject>
  <foreignObject x="18" y="151.5" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{L}_2$</div></foreignObject>
  <rect x="76" y="143" width="130.5" height="46" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="79" y="151.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kiuas}$</div></foreignObject>
  <rect x="206.5" y="143" width="160" height="46" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="209.5" y="151.5" width="154" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{auto}$</div></foreignObject>
  <foreignObject x="18" y="221.5" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{L}_3$</div></foreignObject>
  <rect x="76" y="213" width="130.5" height="46" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="79" y="221.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kiuas}$</div></foreignObject>
  <rect x="206.5" y="213" width="160" height="46" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="209.5" y="221.5" width="154" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{auto}$</div></foreignObject>
  <line x1="326" y1="34" x2="326" y2="284" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="221" y="7.5" width="210" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pääsulake}\ 25\,\text{A}$</div></foreignObject>
</svg>

Pääsulake ei pala heti pienestä ylikuormasta. Jos ylikuorma on riittävän suuri ja jatkuu pitkään, pääsulake voi palaa. Silloin koko talo pimenee. Siksi latausasemassa on usein **kuormanhallinta**. Se mittaa pääsulakkeiden virtaa ja pienentää latausvirtaa, kun muut laitteet ovat päällä. Kun kiuas ottaa $13{,}0\,\text{A}$, autolle jää jokaisessa vaiheessa noin $12\,\text{A}$ eli noin $8{,}3\,\text{kW}$. Jos vedenkeitinkin kytketään päälle, vaiheeseen $\text{L}_1$ jää vain noin $3\,\text{A}$. Silloin kuormanhallinta keskeyttää latauksen hetkeksi.

### Johdon ja liitoksen lämpeneminen
Johto on vastus, ja sen läpi kulkee sama virta kuin laitteen läpi. Virta kulkee laitteelle vaihejohdinta pitkin ja palaa nollajohdinta pitkin. Kuparia on siis kaksi kertaa johdon pituus. Joulen lain mukaan johtoon tuleva teho on $RI^2$ (luku *Sähköteho ja vastuksen lämpeneminen*). Kun virta kaksinkertaistuu, lämpenemisteho nelinkertaistuu. Kelalla olevan $25\,\text{m}$:n jatkojohdon johtimet ovat $1{,}5\,\text{mm}^2$, ja sen resistanssi on noin $0{,}57\,\Omega$. Virralla $10\,\text{A}$ johtoon tulee noin $57\,\text{W}$. Kelalta siirtyy huonosti lämpöä ympäristöön, joten kela kuumenee. Kuumeneminen vanhentaa eristettä. Silloin eristeen läpilyöntilujuus voi heiketä, ja eriste voi pettää. Läpilyöntilujuus tarkoittaa suurinta sähkökenttää, jonka eriste kestää.

Löystynyt tai hapettunut liitos on vielä vaarallisempi. Vanhan pistorasian kosketusresistanssi voi olla esimerkiksi $0{,}10\,\Omega$. Virralla $10\,\text{A}$ liitokseen tulee silloin teho $10\,\text{W}$. Teho keskittyy herneen kokoiseen kohtaan, ja lataus kestää tunteja. Siksi säännölliseen lataamiseen suositellaan latausasemaa. Jatkojohtoa ei käytetä.

### Lukuarvojen lähteet
Luvun lukuarvot ovat tyypillisiä esimerkkiarvoja. Ne eivät ole tietyn auton tai talon mittauksia. Verkkojännite $230\,\text{V}$ ja vakiovirrat $10\,\text{A}$, $16\,\text{A}$ ja $25\,\text{A}$ ovat Suomen sähköverkon ja kotien asennusten tavallisia arvoja. Akun koko $64\,\text{kWh}$ ja kulutus $18\,\text{kWh}$ sadalla kilometrillä ovat pienen ja keskikokoisen sähköauton suuruusluokkaa. Hyötysuhde $80\text{–}95\,\%$ on arvio. Vaatimus latauspisteen omasta ryhmästä ja vikavirtasuojasta on sähköasennusstandardista SFS 6000-7-722. Tukes ohjeistaa sähköauton latauksesta kotona. Kuparin resistiivisyys on luvun *Resistanssi ja Ohmin laki* taulukosta.

## Kaava: Latausaika, latausteho ja johdon lämpeneminen
Latauksen hyötysuhde kertoo, kuinka suuri osa verkosta otetusta energiasta varastoituu akkuun:
```kaavat
hyötysuhde :: \eta = \frac{W_\text{akku}}{W_\text{verkko}}
```
missä $\eta$ on hyötysuhde, $W_\text{akku}$ akkuun varastoitunut energia ($\text{kWh}$) ja $W_\text{verkko}$ verkosta otettu energia ($\text{kWh}$).

Kun latausteho $P$ on vakio, verkosta otettu energia on $W_\text{verkko} = Pt$ (luku *Sähköenergia kotona*). Latausaika on siksi
```latex
t = \frac{W_\text{akku}}{\eta P}
```
missä $t$ on latausaika ($\text{h}$) ja $P$ verkosta otettu teho ($\text{kW}$). Kuvan mallissa teho pysyy vakiona, kunnes akku on noin $90\,\%$:n varaustasossa. Sen jälkeen teho pienenee. Akun lähdejännite kasvaa, ja ohjauspiiri pienentää virtaa (luku *Akut ja latauspiiri*). Verkosta otettu energia on käyrän alle jäävä pinta-ala. Kaava sopii siis latauksen tasaiseen osaan, esimerkiksi varaustasosta $20\,\%$ tasoon $80\,\%$.

<svg data-fig="kayra" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, malli eikä mittaus: sähköauton latausasemalta verkosta otettu teho P kilowatteina ajan t funktiona tunteina, kun 64 kilowattitunnin akku ladataan 20 prosentin varaustasosta. Teho pysyy 11 kilowatissa noin 4,5 tuntia, kunnes varaustaso on 90 prosenttia. Sen jälkeen teho pienenee yhä hitaammin, ja lataus päättyy noin 6,0 tunnin kohdalla, kun varaustaso on 99 prosenttia. Tasaisen osan alle jäävä pinta-ala on varjostettu: se on verkosta otettu energia teho kertaa aika." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy616-energy" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e8590c"/><stop offset="1" stop-color="#ffc078"/></linearGradient></defs>
  <line x1="140.5" y1="300" x2="140.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="197" y1="300" x2="197" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="253.5" y1="300" x2="253.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="310.5" y1="300" x2="310.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="367" y1="300" x2="367" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="423.5" y1="300" x2="423.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="300" x2="480" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="261.5" x2="480" y2="261.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="223.5" x2="480" y2="223.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="185" x2="480" y2="185" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="146.5" x2="480" y2="146.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="108.5" x2="480" y2="108.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="70" x2="480" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="300" x2="494" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,300 L493,306 L493,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="301" x2="84" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,44 L90,57 L78,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="140.5" y1="300" x2="140.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="130.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="197" y1="300" x2="197" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="187" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="253.5" y1="300" x2="253.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="243.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="310.5" y1="300" x2="310.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="300.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="367" y1="300" x2="367" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="357" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="423.5" y1="300" x2="423.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="413.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="480" y1="300" x2="480" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="470" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$7$</div></foreignObject>
  <line x1="77" y1="261.5" x2="84" y2="261.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="247" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="77" y1="223.5" x2="84" y2="223.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="209" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="77" y1="185" x2="84" y2="185" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="170.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="77" y1="146.5" x2="84" y2="146.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="132" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="77" y1="108.5" x2="84" y2="108.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="94" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="77" y1="70" x2="84" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="55.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$12$</div></foreignObject>
  <foreignObject x="54" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{h})$</div></foreignObject>
  <foreignObject x="74" y="13.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P\ (\text{kW})$</div></foreignObject>
  <polygon points="84,300 84,89 340,89 340,300" fill="url(#fy616-energy)" fill-opacity="0.45"/>
  <polyline points="84,300 84,89 340,89 341,95 342,101 343,106.5 344,112 345.5,117.5 346.5,122.5 347.5,127.5 348.5,132.5 349.5,137.5 350.5,142 351.5,146.5 352.5,150.5 353.5,155 354.5,159 356,163 357,167 358,170.5 359,174.5 360,178 361,181.5 362,185 363,188 364,191 365.5,194.5 366.5,197.5 367.5,200 368.5,203 369.5,206 370.5,208.5 371.5,211 372.5,213.5 373.5,216 374.5,218.5 376,221 377,223 378,225 379,227.5 380,229.5 381,231.5 382,233.5 383,235 384,237 385.5,239 386.5,240.5 387.5,242.5 388.5,244 389.5,245.5 390.5,247 391.5,248.5 392.5,250 393.5,251.5 394.5,253 396,254 397,255.5 398,256.5 399,258 400,259 401,260.5 402,261.5 403,262.5 404,263.5 405.5,264.5 406.5,265.5 407.5,266.5 408.5,267.5 409.5,268.5 410.5,269.5 411.5,270 412.5,271 413.5,272 414.5,272.5 416,273.5 417,274 418,275 419,275.5 420,276.5 421,277 422,277.5 423,278.5 424,279 424,300" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="117" y="180" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$W_\text{verkko} = Pt$</span></div></foreignObject>
  <circle cx="84" cy="89" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="94" y="52.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{varaus}\ 20\,\%$</span></div></foreignObject>
  <circle cx="340" cy="89" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="265" y="52.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{varaus}\ 90\,\%$</span></div></foreignObject>
  <circle cx="424" cy="279" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="349" y="234.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{varaus}\ 99\,\%$</span></div></foreignObject>
</svg>

```pysahdy
Akkuun pitää varastoida $20\,\text{kWh}$. Hyötysuhde on $0{,}90$ ja latausteho $5{,}0\,\text{kW}$. Kuinka kauan lataus kestää?
---
$t = \tfrac{W_\text{akku}}{\eta P}$. Sijoitus: $\tfrac{20\,\text{kWh}}{0{,}90 \cdot 5{,}0\,\text{kW}} \approx 4{,}4\,\text{h}$.
```

Luvussa oletetaan, että latauslaitteen virta ja jännite ovat samanvaiheiset eli muuttuvat samaan tahtiin. Tällöin tehokerroin on likimain yksi. Silloin yksivaiheisen laitteen teho on $P = UI$. Mallissa oletetaan myös, että kolmivaihejärjestelmä on tasaisesti kuormitettu. Se tarkoittaa, että laite ottaa jokaisesta vaihejohtimesta saman virran. Silloin kokonaisteho on
```latex
P = 3UI
```
Tässä $U = 230\,\text{V}$ on vaihejohtimen ja nollajohtimen välinen jännite ja $I$ yhden vaihejohtimen virta ($\text{A}$).

Johtoon tuleva lämpenemisteho saadaan Joulen laista ja johtimen resistanssista $R = \rho l : A$ (luku *Resistanssi ja Ohmin laki*). Kuparin pituudeksi otetaan meno- ja paluujohdin yhteensä:
```latex
P_\text{johto} = \rho \frac{2l}{A} I^2
```
missä $P_\text{johto}$ on johtoon tuleva teho ($\text{W}$), $\rho$ kuparin resistiivisyys $1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m}$, $l$ johdon pituus ($\text{m}$), $A$ yhden johtimen poikkipinta-ala ($\text{m}^2$) ja $I$ virta ($\text{A}$).

Latauksen hinta lasketaan verkosta otetusta energiasta, ei akkuun varastoituneesta energiasta:
```latex
K = a W_\text{verkko}
```
missä $K$ on kustannus ($\text{€}$) ja $a$ energian ja siirron hinta yhteensä ($\text{€/kWh}$). Sadan kilometrin ajo vaatii akusta $18\,\text{kWh}$. Hyötysuhteella $90\,\%$ verkosta otetaan $20\,\text{kWh}$. Hinnalla $15\,\text{snt/kWh}$ ajo maksaa noin $3{,}0\,\text{€}$.

## Esimerkki
Esimerkkiauton akun energia on $64\,\text{kWh}$. Akku ladataan yöllä varaustasosta $20\,\%$ tasoon $80\,\%$. Latausasema on kolmivaiheinen ja ottaa jokaisesta vaihejohtimesta virran $16\,\text{A}$. Vaihejännite on $230\,\text{V}$ ja latauksen hyötysuhde $90\,\%$. Teho pysyy koko latauksen ajan vakiona. Kuinka kauan lataus kestää? Paljonko se maksaa, kun sähkö maksaa siirtoineen $15\,\text{snt/kWh}$?

<!-- vaihe -->

**Tunnetut ja kysytty.** Akun energia on $64\,\text{kWh}$, varaustaso $20\,\% \to 80\,\%$, $I = 16\,\text{A}$ kussakin kolmessa vaiheessa, $U = 230\,\text{V}$, $\eta = 0{,}90$ ja $a = 15\,\text{snt/kWh}$.

Kysytään latausaikaa $t$ ja kustannusta $K$.

<!-- vaihe -->

**Periaate.** Akkuun pitää siirtää $60\,\%$ sen energiasta. Asema ottaa jokaisesta kolmesta vaiheesta saman virran, joten sen teho on kolme kertaa yhden vaiheen teho. Häviöiden vuoksi verkosta otetaan akkuun menevä energia jaettuna hyötysuhteella. Hinta maksetaan verkosta otetusta energiasta.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&P = 3UI \\
&t = \frac{W_\text{akku}}{\eta P} \\
&K = \frac{a W_\text{akku}}{\eta}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** $W_\text{akku} = 0{,}60 \cdot 64\,\text{kWh} = 38{,}4\,\text{kWh}$, $\eta = 90\,\% = 0{,}90$ ja $a = 15\,\text{snt/kWh} = 0{,}15\,\text{€/kWh}$. Teho muunnetaan kilowateiksi, jotta aika saadaan tunteina.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&P = 3UI \\
&\phantom{P} = 3 \cdot 230\,\text{V} \cdot 16\,\text{A} \\
&\phantom{P} = 11\,040\,\text{W} = 11{,}04\,\text{kW} \\
&t = \frac{W_\text{akku}}{\eta P} \\
&\phantom{t} = \frac{38{,}4\,\text{kWh}}{0{,}90 \cdot 11{,}04\,\text{kW}} \\
&\phantom{t} \approx 3{,}86\,\text{h} \\
&K = \frac{a W_\text{akku}}{\eta} \\
&\phantom{K} = \frac{0{,}15\,\text{€/kWh} \cdot 38{,}4\,\text{kWh}}{0{,}90} \\
&\phantom{K} = 6{,}40\,\text{€}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Lataus kestää noin $3{,}9\,\text{h}$ ja maksaa noin $6{,}4\,\text{€}$. Verkosta otetaan $$\begin{aligned} &38{,}4\,\text{kWh} : 0{,}90 \\ &\approx 42{,}7\,\text{kWh} \end{aligned}$$. Tulokset ilmoitetaan kahdella merkitsevällä numerolla, kuten hyötysuhde $0{,}90$ ja hinta $15\,\text{snt/kWh}$.

<!-- vaihe -->

**Järkevyys.** Arvio: noin $40\,\text{kWh}$ noin $10\,\text{kW}$:n teholla kestää noin $4\,\text{h}$. Ilman häviöitä lataus kestäisi $38{,}4\,\text{kWh} : 11{,}04\,\text{kW} \approx 3{,}5\,\text{h}$. Häviöt pidentävät latausta, kuten pitääkin. Hinta vastaa noin $210\,\text{km}$:n ajoa, noin $3\,\text{€}$ sadalta kilometriltä. Lataus mahtuu hyvin yhteen yöhön.

## Yleinen virhekäsitys
Moni ajattelee, että kun sulake palaa toistuvasti, sen tilalle voi vaihtaa suuremman. Sulake ei kuitenkaan suojaa laitetta vaan johtoa. Sen koko on valittu niin, että johto ei kuumene vaarallisesti. Suurempi sulake päästää johtoon virran, joka lämmittää johtoa enemmän kuin johto kestää. Eriste voi silloin sulaa tai syttyä. Oikea ratkaisu on oma ryhmä, kuten latausasemalle, tai kuormien vuorottelu.

Toinen yleinen virhe on olettaa, että $64\,\text{kWh}$:n akun täyttäminen vie verkosta $64\,\text{kWh}$. Häviöiden vuoksi verkosta otetaan enemmän. Akkuun menevä energia jaetaan hyötysuhteella, ei kerrota sillä.

## Tiivistelmä
- Latausaika on akkuun siirrettävä energia jaettuna hyötysuhteen ja tehon tulolla, $t = W_\text{akku} : (\eta P)$. Hyötysuhde jää alle $100\,\%$, koska latauksessa on aina häviöitä. Verkosta otetaan siis enemmän energiaa kuin akkuun varastoituu, ja hinta maksetaan verkosta otetusta energiasta.
- Yksivaiheisen latauksen teho on $P = UI$ ja kolmivaiheisen $P = 3UI$, kun jokaisessa vaihejohtimessa on sama virta. Samalla $16\,\text{A}$:n virralla kolmivaiheinen asema lataa kolme kertaa nopeammin.
- Pääsulakkeet rajoittavat jokaisen vaihejohtimen virtaa. Saman vaiheen virrat lasketaan yhteen. Kuormanhallinta pienentää latausvirtaa, kun kiuas tai muut laitteet ovat päällä.
- Latausasemalla on oma ryhmä ja oma vikavirtasuoja. Lataus on pitkä suuri kuorma, ja ulkona kaapelin eriste voi vaurioitua.
- Johdon lämpenemisteho on $RI^2$. Kaksinkertainen virta nelinkertaistaa sen. Kelattu jatkojohto ja löystynyt liitos kuumenevat. Kelalta siirtyy huonosti lämpöä ympäristöön, ja löystyneessä liitoksessa lämpenemisteho keskittyy pieneen kohtaan.
