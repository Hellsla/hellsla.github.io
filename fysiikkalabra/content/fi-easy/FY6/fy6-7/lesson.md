# Sähköenergia kotona

> **Miksi** sähkölasku lasketaan kilowattitunneista eikä kodin laitteiden watteista?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvi-ilta ja leikkauskuva omakotitalosta. Vasemmalla saunassa hehkuu sähkökiuas. Keskellä keittiössä höyryää vedenkeitin jääkaapin vieressä, ja kattovalaisin palaa. Oikealla olohuoneessa on televisio ja lattiavalaisin. Talon ulkoseinällä on sähkömittari. Ulkona on lunta." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-7-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Teho kertoo tahdin, energia määrän
Jokaisen sähkölaitteen arvokilvessä on laitteen **nimellisteho**. Vedenkeittimessä se on esimerkiksi $2000\,\text{W}$ ja televisiossa $100\,\text{W}$. Teho kertoo, kuinka nopeasti laite ottaa sähköenergiaa sähköverkosta (luku *Sähköteho ja vastuksen lämpeneminen*). Laite käyttää energiaa sitä enemmän, mitä kauemmin se on päällä. Kun teho pysyy samana, **energia on teho kertaa aika**. Sähkölaskussa maksetaan pääosin energiasta, ei tehosta.

Suuri teho ei siis yksin tarkoita suurta kulutusta. Vedenkeitin, jonka teho on $2{,}0\,\text{kW}$, käyttää kuudessa minuutissa yhtä paljon energiaa kuin $0{,}10\,\text{kW}$:n televisio kahdessa tunnissa. Kuvaajassa on tehon ja ajan välinen yhteys. Siinä energia on kuvaajan ja aika-akselin väliin jäävä pinta-ala. Kapea ja korkea suorakulmio voi olla yhtä suuri kuin leveä ja matala.

<svg data-fig="power-time" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja mittakaavassa: teho P kilowatteina ajan t funktiona tunteina. Vedenkeittimen teho on 2,0 kW ajan 0–0,10 h. Sen alue on kapea ja korkea suorakulmio. Television teho on 0,10 kW ajan 0–2,0 h. Sen alue on leveä ja matala suorakulmio. Kummankin suorakulmion pinta-ala on 0,20 kWh. Energia on siis sama." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy67-energy" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e8590c"/><stop offset="1" stop-color="#ffc078"/></linearGradient></defs>
  <line x1="161" y1="300" x2="161" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="237.5" y1="300" x2="237.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="314.5" y1="300" x2="314.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="391" y1="300" x2="391" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="468" y1="300" x2="468" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="253" x2="468" y2="253" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="205.5" x2="468" y2="205.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="158.5" x2="468" y2="158.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="111" x2="468" y2="111" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="64" x2="468" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="83" y1="300" x2="482" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M494,300 L481,306 L481,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="84" y1="301" x2="84" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M84,38 L90,51 L78,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="161" y1="300" x2="161" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="138.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}5$</div></foreignObject>
  <line x1="237.5" y1="300" x2="237.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="227.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="314.5" y1="300" x2="314.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="292" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}5$</div></foreignObject>
  <line x1="391" y1="300" x2="391" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="381" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="468" y1="300" x2="468" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="77" y1="253" x2="84" y2="253" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="27" y="238.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}5$</div></foreignObject>
  <line x1="77" y1="205.5" x2="84" y2="205.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="191" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="77" y1="158.5" x2="84" y2="158.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="27" y="144" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}5$</div></foreignObject>
  <line x1="77" y1="111" x2="84" y2="111" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="52" y="96.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="77" y1="64" x2="84" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="500" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{h})$</div></foreignObject>
  <foreignObject x="74" y="7.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P\ (\text{kW})$</div></foreignObject>
  <rect x="84" y="290.5" width="307" height="9.5" fill="url(#fy67-energy)" stroke="#1f2933" stroke-width="2"/>
  <rect x="84" y="111" width="15.5" height="189" fill="url(#fy67-energy)" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="113.5" y="94.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{vedenkeitin}$</span></div></foreignObject>
  <foreignObject x="113.5" y="126.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$E = 0{,}20\,\text{kWh}$</span></div></foreignObject>
  <foreignObject x="172.5" y="226" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{televisio}$</span></div></foreignObject>
  <foreignObject x="152.5" y="256" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$E = 0{,}20\,\text{kWh}$</span></div></foreignObject>
</svg>

```pysahdy
Lamppu, jonka teho on $0{,}060\,\text{kW}$, palaa $5{,}0\,\text{h}$. Kuinka paljon sähköenergiaa lamppu käyttää? Vastaa kilowattitunteina.
---
Energia on $E = Pt$. Siis $E = 0{,}060\,\text{kW} \cdot 5{,}0\,\text{h}$, joten $E = 0{,}30\,\text{kWh}$.
```

<figure class="unit-photo"><img src="pics/fy6/electricity-meter.webp" alt="Musta sähkömittari seinällä. Ylhäällä on numeroita ja yksikkö kWh. Alla on pyörivä levy."><figcaption>Vanha sähkömittari laskee, kuinka paljon sähköenergiaa koti käyttää. Yksikkö on kilowattitunti. Levy pyörii sitä nopeammin, mitä suurempi teho kodissa on päällä.</figcaption></figure>

### Kilowattitunti on energian yksikkö
Energian SI-yksikkö on joule. Kodin sähköenergia mitataan ja laskutetaan kuitenkin **kilowattitunteina**. Yksi kilowattitunti on energia, jonka $1\,\text{kW}$:n teholla toimiva laite käyttää tunnissa. Kun teho on kilowatteina ja aika tunteina, energia tulee suoraan kilowattitunteina. Nimi kertoo, miten se lasketaan: kilowatti kertaa tunti. Se ei ole kilowatti tunnissa. Yksi kilowattitunti on $3{,}6$ miljoonaa joulea.

```pysahdy
Kuinka monta kilowattituntia on $10{,}8\,\text{MJ}$?
---
Yksi kilowattitunti on $3{,}6\,\text{MJ}$. Siis $E = 10{,}8\,\text{MJ} : 3{,}6\,\text{MJ/kWh}$, joten $E = 3{,}0\,\text{kWh}$.
```

### Laitteen virta verkossa
Kodin pistorasioissa on jännite $230\,\text{V}$. Se on vaihtojännitteen tehollinen arvo. Tehollinen arvo tarkoittaa arvoa, jolla laskeminen onnistuu kuten tasajännitteellä. Tässä luvussa tarkastellaan yksinkertaistettuja sähköpiirejä. Niissä virta ja jännite ovat samanvaiheiset eli muuttuvat samaan tahtiin. Näin on esimerkiksi lämmittävissä laitteissa. Muissa laitteissa oletetaan, että tehokerroin on likimain yksi. Tehokerroin on luku, joka on yksi, kun virta ja jännite ovat samanvaiheiset. Silloin laitteen pätöteho eli todellinen teho lasketaan samoin kuin tasajännitteellä: $P = UI$. Yleensä vaihtovirtapiirin pätöteho riippuu myös siitä, kuinka paljon jännite ja virta ovat eri tahdissa. Tätä eroa sanotaan vaihe-eroksi. Laitteen nimellistehosta saadaan virta $I = P : U$. Vedenkeitin ottaa virran $2000\,\text{W} : 230\,\text{V} \approx 8{,}7\,\text{A}$. Puhelimen laturi ottaa vain murto-osan ampeerista. Suuritehoiset laitteet ottavat suuren virran. Siksi kodin virtapiirin sulake rajoittaa, kuinka monta tällaista laitetta voi olla yhtä aikaa päällä samassa piirissä (luku *Sähköturvallisuus kotona ja työssä*).

### Mihin kodin sähköenergia kuluu
Eniten energiaa käyttävät laitteet, joissa sekä teho että käyttöaika ovat suuria. Tällaisia ovat sähkölämmitys, lämminvesivaraaja ja sähkökiuas. Niiden vastuksissa sähköenergia muuttuu vastuksen sisäenergiaksi. Sisäenergia siirtyy lämpönä veteen, ilmaan tai kiviin. Kuuden kilowatin kiuas käyttää puolentoista tunnin saunomiskerralla $9{,}0\,\text{kWh}$. Yhtä paljon energiaa käyttää $100\,\text{W}$:n televisio $90$ tunnissa.

Pienitehoinenkin laite voi kerätä suuren kulutuksen, jos se on päällä koko ajan. Jääkaappi käy vuorokauden ympäri. Valmiustilassa oleva laite käyttää yhden watin teholla vuodessa noin $9\,\text{kWh}$. Säästää voi kahdella tavalla. Voi pienentää tehoa, esimerkiksi vaihtamalla lamput LED-lamppuihin. Voi myös lyhentää käyttöaikaa, esimerkiksi saunomalla harvemmin tai laskemalla huonelämpötilaa. Vaikutus on suurin niissä laitteissa, joiden energia on suurin.

## Kaava: Sähköenergia
Kun laitteen teho pysyy samana, laitteen käyttämä sähköenergia on
```latex
E = Pt
```
missä $E$ on energia (J tai kWh), $P$ teho (W tai kW) ja $t$ aika (s tai h). Kun teho on watteina ja aika sekunteina, energia tulee jouleina. Kun teho on kilowatteina ja aika tunteina, energia tulee kilowattitunteina. Muunnos tehdään sijoittamalla yksiköt: $$\begin{aligned} 1\,\text{kWh} &= 1000\,\text{W} \cdot 3600\,\text{s} \\ &= 3\,600\,000\,\text{J} \\ &= 3{,}6\,\text{MJ} \end{aligned}$$.

<svg data-fig="kwh" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei mittakaavassa. Vasemmalla on sähköpatteri, jonka teho on 1 kW. Sen yläpuolella on oransseja lämpönuolia. Keskellä on kello, jonka minuuttiosoitin kiertää kerran ympäri eli 1 tunnin. Oikealla on sähkömittari, jonka lukema kasvaa 1 kilowattitunnin. Kuvan alla: 1 kWh = 1000 W · 3600 s = 3,6 MJ." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-7-kwh.webp" x="0" y="-1.2" width="600" height="367.5" preserveAspectRatio="none"/>
  <foreignObject x="31" y="265.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P = 1\,\text{kW}$</div></foreignObject>
  <foreignObject x="199" y="142" width="30" height="48" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:40px">$\cdot$</div></foreignObject>
  <foreignObject x="237" y="265.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t = 1\,\text{h}$</div></foreignObject>
  <foreignObject x="385" y="145.5" width="30" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:34px">$=$</div></foreignObject>
  <foreignObject x="426" y="265.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E = 1\,\text{kWh}$</div></foreignObject>
  <foreignObject x="40" y="319.5" width="520" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{kWh} = 1000\,\text{W} \cdot 3600\,\text{s} = 3{,}6\,\text{MJ}$</div></foreignObject>
</svg>

Sähköteho on $P = UI$. Siksi energian voi laskea myös jännitteestä ja virrasta:
```latex
E = UIt
```
missä $U$ on laitteen jännite (V) ja $I$ sen läpi kulkeva virta (A).

```pysahdy
Laitteen jännite on $230\,\text{V}$ ja virta $0{,}50\,\text{A}$. Kuinka paljon energiaa se käyttää $2{,}0\,\text{h}$:ssa? Vastaa kilowattitunteina.
---
Teho on $P = UI = 230\,\text{V} \cdot 0{,}50\,\text{A}$, joten $P = 115\,\text{W} = 0{,}115\,\text{kW}$. Siis $E = Pt = 0{,}115\,\text{kW} \cdot 2{,}0\,\text{h}$, joten $E = 0{,}23\,\text{kWh}$.
```

Sähkölaskussa maksetaan sähköenergiasta ja sen siirrosta sähköverkossa kilowattituntia kohti. Lisäksi laskussa on kuukausittaisia perusmaksuja:
```latex
K = aE + K_\text{perus}
```
missä $K$ on laskun summa (€), $a$ energian ja siirron hinta yhteensä kilowattituntia kohti (€/kWh), $E$ laskutuskauden energia (kWh) ja $K_\text{perus}$ perusmaksut (€). Laskutuskauden energia on sähkömittarin lukemien erotus. Hinnat ilmoitetaan usein sentteinä: $18\,\text{snt/kWh} = 0{,}18\,\text{€/kWh}$.

## Esimerkki
Kylpyhuoneen sähköisen lattialämmityksen teho on $0{,}80\,\text{kW}$. Termostaatti pitää lämmityksen päällä keskimäärin $6\,\text{h}\ 15\,\text{min}$ vuorokaudessa. Kuinka paljon sähköenergiaa lattialämmitys käyttää $30$ vuorokaudessa? Paljonko se maksaa, kun sähkö maksaa siirtoineen $18\,\text{snt/kWh}$?

<!-- vaihe -->

**Tunnetut ja kysytty.** $P = 0{,}80\,\text{kW}$, käyttöaika $6\,\text{h}\ 15\,\text{min}$ vuorokaudessa, $30$ vuorokautta, hinta $a = 18\,\text{snt/kWh}$.

Kysytään energiaa $E$ kilowattitunteina ja kustannusta $K$ euroina.

<!-- vaihe -->

**Periaate.** Kun lämmitys on päällä, sen teho pysyy samana. Siksi energia on teho kertaa yhteenlaskettu käyttöaika. Kustannus on energia kertaa hinta kilowattituntia kohti. Perusmaksut kuuluvat koko kodin laskuun, eivät yhdelle laitteelle.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&E = Pt \\
&K = aE
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** $15\,\text{min} = \tfrac{15}{60}\,\text{h} = 0{,}25\,\text{h}$. Vuorokauden käyttöaika on siis $6{,}25\,\text{h}$ ja kokonaisaika $t = 30 \cdot 6{,}25\,\text{h} = 187{,}5\,\text{h}$. Hinta $18\,\text{snt/kWh} = 0{,}18\,\text{€/kWh}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&E = Pt \\
&\phantom{E} = 0{,}80\,\text{kW} \cdot 187{,}5\,\text{h} \\
&\phantom{E} = 150\,\text{kWh} \\
&K = aE \\
&\phantom{K} = 0{,}18\,\tfrac{\text{€}}{\text{kWh}} \cdot 150\,\text{kWh} \\
&\phantom{K} = 27\,\text{€}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Lattialämmitys käyttää $30$ vuorokaudessa noin $150\,\text{kWh}$ sähköenergiaa. Se maksaa noin $27\,\text{€}$. Tulokset on annettu kahdella merkitsevällä numerolla kuten teho $0{,}80\,\text{kW}$ ja hinta $18\,\text{snt/kWh}$.

<!-- vaihe -->

**Järkevyys.** Vuorokaudessa lämmitys käyttää $0{,}80\,\text{kW} \cdot 6{,}25\,\text{h} = 5{,}0\,\text{kWh}$. Se maksaa noin $0{,}90\,\text{€}$. Kuukaudessa se on noin $30 \cdot 0{,}90\,\text{€} = 27\,\text{€}$. Jos minuutteja ei olisi muunnettu ja aika olisi $6{,}15\,\text{h}$, tulos olisi hieman liian pieni.

## Yleinen virhekäsitys
Moni ajattelee, että suuritehoinen laite on aina sähkölaskun suurin erä. Teho kertoo kuitenkin vain, kuinka nopeasti laite käyttää energiaa. Vedenkeitin on päällä vain muutamia minuutteja päivässä. Jääkaappi, lämminvesivaraaja ja lämmitys toimivat tuntikausia. Kulutuksen ratkaisee teho kertaa aika.

Toinen yleinen virhe on lukea kilowattitunti "kilowattia tunnissa". Kilowattitunti on energian yksikkö, kilowatti kertaa tunti. Se ei kerro, kuinka nopeasti mikään muuttuu. Kolmas virhe on sekoittaa yksiköitä. Tulos $2000\,\text{W} \cdot 15\,\text{min}$ ei ole $30\,000\,\text{kWh}$. Oikea tulos on $2{,}0\,\text{kW} \cdot 0{,}25\,\text{h} = 0{,}50\,\text{kWh}$.

## Tiivistelmä
- Laite toimii samalla teholla. Sen käyttämä sähköenergia on $E = Pt = UIt$. Teho kertoo, kuinka nopeasti energiaa käytetään. Energia kertoo, kuinka paljon sitä käytetään.
- Kilowattitunti on energian yksikkö: $$\begin{aligned} 1\,\text{kWh} &= 1000\,\text{W} \cdot 3600\,\text{s} \\ &= 3{,}6\,\text{MJ} \end{aligned}$$. Kilowateilla ja tunneilla laskettu energia tulee suoraan kilowattitunteina.
- Lämmittävän laitteen virta $230\,\text{V}$:n verkossa on $I = P : U$. Suuritehoinen laite ottaa suuren virran.
- Sähkölasku on energian ja siirron hinta kertaa kulutettu energia. Siihen lisätään perusmaksut. Energia on mittarin lukemien erotus.
- Eniten säästää pienentämällä niiden laitteiden tehoa tai käyttöaikaa, joiden energia on suurin: lämmitys, lämmin vesi ja sauna.
