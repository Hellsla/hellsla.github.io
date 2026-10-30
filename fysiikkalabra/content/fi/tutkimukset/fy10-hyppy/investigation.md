# Hypyn tutkiminen voimalevyllä

> **Tutkimuskysymys:** Miten hyppääjän lähtönopeus ja hypyn korkeus saadaan voimalevyn mittaamasta voima–aika-kuvaajasta, ja vastaako tulos toisella menetelmällä määritettyä hyppykorkeutta?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: opiskelija on hypännyt suoraan ylös voimalevyn päältä ja on ilmassa kädet lanteilla. Hänen varjonsa näkyy levyllä. Voimalevystä kulkee johto pöydällä olevaan tietokoneeseen, jonka näytöllä on tyhjä koordinaatisto, johon mittaus piirtyy." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10hh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10hh-floor" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10hh-wall)"/>
  <rect x="0" y="490" width="1200" height="110" fill="url(#fy10hh-floor)"/>
  <line x1="0" y1="512" x2="1200" y2="508" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="536" x2="1200" y2="532" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="560" x2="1200" y2="556" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="584" x2="1200" y2="580" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="490" x2="1200" y2="490" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="330" y="466" width="300" height="24" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="342" y="472" width="276" height="6" rx="2" fill="#8a96a3"/>
  <ellipse cx="480" cy="465" rx="62" ry="7" fill="#1f2933" fill-opacity="0.18"/>
  <path d="M452.5,400 L459,242.5 H501 L507.5,400 H486.5 L480,295 L473.5,400 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M450.5,152 L410.5,194 L444.5,238.5" fill="none" stroke="#1971c2" stroke-width="23.1" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M509.5,152 L549.5,194 L515.5,238.5" fill="none" stroke="#1971c2" stroke-width="23.1" stroke-linejoin="round" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M444.5,253 Q440,137.5 480,131 Q520,137.5 515.5,253 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="446.5" cy="238.5" r="11.55" fill="#f1dfb5"/>
  <circle cx="513.5" cy="238.5" r="11.55" fill="#f1dfb5"/>
  <rect x="470.5" y="110" width="19" height="25" fill="#f1dfb5"/>
  <circle cx="480" cy="89" r="31.5" fill="#f1dfb5"/>
  <path d="M447.5,89 Q448.5,51.5 480,53.5 Q513.5,53.5 512.5,85 Q486.5,72.5 447.5,89 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M452,414 v34" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.5"/>
  <path d="M480,414 v46" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.5"/>
  <path d="M508,414 v34" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.5"/>
  <path d="M630,480 C700,480 720,470 760,470 S820,420 870,404" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="840" y="400" width="300" height="14" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="860" y1="414" x2="860" y2="490" stroke="#1f2933" stroke-width="5" stroke-linecap="butt"/>
  <line x1="1120" y1="414" x2="1120" y2="490" stroke="#1f2933" stroke-width="5" stroke-linecap="butt"/>
  <path d="M900,400 L1080,400 L1092,392 L888,392 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="906" y="272" width="168" height="116" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="916" y="282" width="148" height="96" rx="2" fill="#ffffff"/>
  <line x1="926" y1="368" x2="1056" y2="368" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="926" y1="368" x2="926" y2="290" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M1056,368 l-8,-4 v8 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M926,290 l-4,8 h8 Z" fill="#1f2933" stroke-linejoin="round"/>
</svg>

Voimalevy näyttää lattialla vain vaa'alta, mutta se mittaa jalkojen ja levyn välistä voimaa hyvin tiheästi, monta kertaa sekunnin aikana. Hypyn aikana voima muuttuu nopeasti, ja juuri muutoksesta voi päätellä, kuinka suurella nopeudella hyppääjä irtosi levystä ja kuinka korkealle hän nousi. Tässä tutkimuksessa määrität hypyn korkeuden voimamittauksesta ja tarkistat tuloksen toisella menetelmällä, joka perustuu eri oletuksiin. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** mitä voima–aika-kuvaajan eri osat kertovat hypyn vaiheista, sekä ponnistuksen aikana tapahtuva liikemäärän muutos, lähtönopeus ja hypyn korkeus. Määritä hypyn korkeus myös toisella menetelmällä ja vertaa tuloksia epävarmuuksineen.

Hyppääjän paino ja massa ovat henkilökohtaisia tietoja. Tarvitset painoa laskuissa, mutta sitä ja massaa ei tarvitse kirjata raporttiin: voit ilmoittaa voimat painon monikertoina $\dfrac{N}{G}$. Kukaan ei ole velvollinen hyppäämään, ja ryhmä voi käyttää yhtä vapaaehtoista hyppääjää.

**Päätät itse:** hyppytavan ja sen, miten pidät sen samana hypystä toiseen, hyppyjen määrän ja sen, millä perusteella hylkäät epäonnistuneen hypyn, sen, miten luet kuvaajasta hyppääjän painon sekä irtoamis- ja alastulohetken, mistä mihin lasket pinta-alan, toisen menetelmän sekä tavan, jolla arvioit tulosten epävarmuuden. Ohjatussa ja osittain ohjatussa työtavassa sivu antaa näihin tukea, itsenäisessä työtavassa perustelet valintasi itse.

::: tuki I
**Itsenäinen työtapa.** Valitse toinen menetelmä itse ja perustele, mitä se mittaa ja missä mielessä se on riippumaton voimamittauksesta.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Hyppääjä seisoo levyllä ja kyykistyy nopeasti ennen ponnistusta. Kasvaako levyn näyttämä voima, pieneneekö se vai pysyykö se samana kyykistymisen alussa? Entä kun hän on ilmassa?
2. Onko levyn tukivoima ponnistuksen aikana suurempi, pienempi vai yhtä suuri kuin hyppääjän paino? Perustele Newtonin lakien avulla.
3. Hahmottele vihkoon, millainen voima–aika-kuvaaja on koko hypyn ajalta, kun hyppääjä seisoo ensin paikallaan, hyppää ja laskeutuu takaisin levylle.
4. Jos hyppääjä laskeutuu polvet selvästi enemmän koukussa kuin irrotessaan, miten se vaikuttaa ilmassaoloaikaan? Mikä mittauksessa on mielestäsi suurin epävarmuuden lähde?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Voimalevy mittaa vain voimaa ja aikaa, mutta tutkimuskysymyksessä kysytään nopeutta ja korkeutta. Ennen kuin luet eteenpäin, kirjaa:

1. Miten saat hyppääjän painon ja massan levyn mittauksesta?
2. Mikä fysiikan periaate yhdistää voiman ja ajan nopeuden muutokseen? Mitä hypyn osaa sinun pitää tarkastella, jotta saat lähtönopeuden?
3. Miten lähtönopeudesta saadaan hypyn korkeus?
4. Mitä muuta voisit mitata, jotta saat korkeuden toisella tavalla? Mitä oletuksia se vaatii?

## Teoriaa lyhyesti

Hyppääjään vaikuttaa kaksi voimaa: alaspäin paino $\overline{G}$ ja ylöspäin levyn tukivoima $\overline{N}$. Hyppääjä painaa levyä yhtä suurella voimalla kuin levy tukee häntä (Newtonin III laki), joten levy mittaa tukivoiman suuruuden $N$. Kun hyppääjä seisoo levossa, voimat kumoavat toisensa. Kun ne eivät kumoa toisiaan, kokonaisvoima muuttaa hyppääjän nopeutta Newtonin toisen lain mukaisesti. [[apua:fy4-4|Newtonin toinen laki]]

<svg data-fig="forces" viewBox="0 0 600 340" role="img" aria-label="Kaksi voimakuviota, hyppääjä suorakulmiona. Vasemmalla hyppääjä seisoo levossa voimalevyllä: paino G osoittaa keskipisteestä alas ja levyn tukivoima N alapinnasta ylös, ja nuolet ovat yhtä pitkät. Oikealla hyppääjä ponnistaa: tukivoima N on pidempi kuin paino G, ja hyppääjän vieressä oleva oranssi nuoli a näyttää kiihtyvyyden ylöspäin." style="max-width:100%;font-size:24px">
  <rect x="60" y="270" width="200" height="12" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="112.5" y="11.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{levossa}$</div></foreignObject>
  <rect x="125" y="110" width="70" height="160" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="160" y1="190" x2="160" y2="248" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M160,265 L152,247 L168,247 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="119.5" y="240.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="182" y1="270" x2="182" y2="212" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M182,195 L190,213 L174,213 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="195.5" y="192.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <rect x="340" y="270" width="200" height="12" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="323.5" y="11.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{ponnistuksen aikana}$</div></foreignObject>
  <rect x="405" y="110" width="70" height="160" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="190" x2="440" y2="248" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,265 L432,247 L448,247 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="399.5" y="240.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="462" y1="270" x2="462" y2="152" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M462,135 L470,153 L454,153 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="475.5" y="132.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="520" y1="220" x2="520" y2="158" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526.5,169 L520,156 L513.5,169" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="521.5" y="149.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <line x1="300" y1="14" x2="300" y2="326" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
</svg>

Kokonaisvoiman vaikutusta ajan kuluessa kuvaa **impulssi**, ja impulssiperiaatteen mukaan kokonaisvoiman impulssi on yhtä suuri kuin liikemäärän muutos. Kun voima muuttuu koko ajan, impulssi on voima–aika-kuvaajan ja aika-akselin väliin jäävä pinta-ala. [[apua:fy4-9|Impulssi ja voima–aika-kuvaajan pinta-ala]]

Kun jalat irtoavat levystä, hyppääjään vaikuttaa vain paino, kun ilmanvastus jätetään huomiotta. Silloin hyppääjän mekaaninen energia säilyy, ja liike on tasaisesti hidastuvaa ylöspäin ja tasaisesti kiihtyvää alaspäin. **Hypyn korkeudella** $h$ tarkoitetaan tässä sitä, kuinka paljon hyppääjän painopiste nousee irtoamishetkestä lakikorkeuteen. [[apua:fy4-8|Mekaanisen energian säilyminen]]

::: tuki O OO
Tarkista kirjauksesi tästä. Valitaan positiivinen suunta ylöspäin. Hyppääjään vaikuttava kokonaisvoima on $N - G$.

**Paino ja massa.** Kun hyppääjä seisoo levossa, $N = G$, joten levyn lukema on paino $G$. Massa on $m = \dfrac{G}{g}$.

**Lähtönopeus impulssista.** Hyppääjä on aluksi levossa, joten hänen liikemääränsä on nolla. Irtoamishetkellä liikemäärä on $mv_0$, missä $v_0$ on lähtönopeus. Impulssiperiaatteen mukaan kokonaisvoiman $N - G$ impulssi liikkeen alusta irtoamishetkeen on

```latex
I = m v_0 - 0
```

joten $v_0 = \dfrac{I}{m}$. Impulssi $I$ on se pinta-ala, joka jää voima–aika-kuvaajan ja painoa $G$ kuvaavan vaakasuoran viivan väliin. Painon yläpuolelle jäävä pinta-ala on positiivinen ja alapuolelle jäävä negatiivinen. Mittausohjelma laskee pinta-alan mittauspisteistä summana

```latex
I \approx \sum (N_i - G)\cdot\Delta t
```

missä $N_i$ on tukivoima mittauspisteessä $i$ ja $\Delta t$ kahden mittauspisteen välinen aika. Koska $m = \dfrac{G}{g}$, lähtönopeus on myös

```latex
v_0 = \frac{I}{m} = g\cdot\frac{I}{G}
```

joten massaa ei tarvitse ilmoittaa: riittää impulssi painon monikertana $\dfrac{I}{G}$, jonka yksikkö on sekunti. Saman saat, kun jaat jokaisen voiman painolla ja lasket pinta-alan kuvaajasta $\dfrac{N}{G}$ ajan funktiona, viivan $\dfrac{N}{G} = 1$ yläpuolelta ja alapuolelta.

**Korkeus lähtönopeudesta.** Irtoamisen jälkeen liike-energia muuttuu potentiaalienergiaksi: $\tfrac{1}{2}mv_0^2 = mgh$, joten

```latex
h = \frac{v_0^2}{2g}
```

**Korkeus lentoajasta.** Jos hyppääjä on alastulohetkellä samassa asennossa kuin irtoamishetkellä, nousu ja lasku kestävät yhtä kauan, kumpikin puolet lentoajasta $t_\text{lento}$. Nousun aikana nopeus pienenee arvosta $v_0$ nollaan tasaisesti, joten $v_0 = g\cdot\dfrac{t_\text{lento}}{2}$, ja korkeudeksi saadaan

```latex
h = \frac{g\cdot t_\text{lento}^2}{8}
```

Lentoaika luetaan kuvaajasta tai muusta mittauksesta: se on aika irtoamishetkestä alastulohetkeen, jolloin levyn lukema on nolla.

<svg data-fig="model" viewBox="0 0 600 420" role="img" aria-label="Kuvaaja: voimalevyn tukivoima N ajan t funktiona mallin mukaan, ilman lukuarvoja. Vaakasuora katkoviiva on paino G. Kuvaajaan on merkitty numeroin kuusi vaihetta: 1 tasainen osa painon kohdalla, 2 notko painon alapuolella, 3 korkea huippu painon yläpuolella, joka laskee nollaan, 4 nollaosa, 5 jyrkkä ja korkea huippu sekä 6 paluu painon tasolle. Ennen irtoamista painon alapuolelle jäävä alue on merkitty miinusmerkillä ja yläpuolelle jäävä alue plusmerkillä. Nollaosan pituus on merkitty t lento. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="69" y1="360" x2="494" y2="360" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,360 L493,366 L493,354 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="361" x2="70" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M70,34 L76,47 L64,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="40" y="365.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="345.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="60" y="3.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N$</div></foreignObject>
  <polygon points="127.5,298 127.5,298 128,298 128.5,298 129,298 129.5,298.5 130,298.5 130.5,299 131,299 131.5,299.5 132,300 132.5,300.5 133,301 133,301.5 133.5,302 134,302.5 134.5,303.5 135,304 135.5,304.5 136,305.5 136.5,306.5 137,307 137.5,308 138,309 138.5,309.5 139,310.5 139.5,311.5 140,312.5 140.5,313.5 141,314.5 141.5,315.5 142,316 142,317 142.5,318 143,319 143.5,320 144,321 144.5,322 145,323 145.5,323.5 146,324.5 146.5,325.5 147,326.5 147.5,327 148,328 148.5,328.5 149,329.5 149.5,330 150,330.5 150.5,331.5 150.5,332 151,332.5 151.5,333 152,333.5 152.5,333.5 153,334 153.5,334.5 154,334.5 154.5,335 155,335 155.5,335 156,335 156.5,335 157,335 157.5,335 158,335 158.5,334.5 159,334 159.5,333.5 159.5,333 160,332.5 160.5,331.5 161,331 161.5,330 162,329 162.5,328 163,327 163.5,325.5 164,324.5 164.5,323 165,322 165.5,320.5 166,319 166.5,317 167,315.5 167.5,314 168,312 168.5,310.5 168.5,308.5 169,306.5 169.5,304.5 170,302.5 170.5,300.5 171,298.5 171.5,298" fill="#d0e6fb" fill-opacity="0.8"/>
  <polygon points="171.5,298 171.5,296.5 172,294 172.5,292 173,290 173.5,287.5 174,285.5 174.5,283 175,281 175.5,278.5 176,276.5 176.5,274 177,272 177,269.5 177.5,267 178,265 178.5,262.5 179,260.5 179.5,258 180,256 180.5,254 181,251.5 181.5,249.5 182,247.5 182.5,245.5 183,243.5 183.5,241.5 184,239.5 184.5,237.5 185,235.5 185.5,234 186,232 186,230.5 186.5,229 187,227.5 187.5,226 188,224.5 188.5,223 189,221.5 189.5,220.5 190,219.5 190.5,218 191,217 191.5,216 192,215.5 192.5,214.5 193,214 193.5,213 194,212.5 194.5,212.5 195,212 195,211.5 195.5,211.5 196,211.5 196.5,211 197,211 197.5,211.5 198,211.5 198.5,211.5 199,211.5 199.5,211.5 200,211.5 200.5,211.5 201,212 201.5,212 202,212 202.5,212 203,212.5 203.5,212.5 204,213 204,213 204.5,213 205,213.5 205.5,213.5 206,214 206.5,214 207,214.5 207.5,214.5 208,215 208.5,215.5 209,215.5 209.5,216 210,216 210.5,216.5 211,217 211.5,217 212,217.5 212.5,218 212.5,218 213,218.5 213.5,219 214,219 214.5,219.5 215,220 215.5,220 216,220.5 216.5,221 217,221 217.5,221.5 218,222 218.5,222 219,222.5 219.5,222.5 220,223 220.5,223 221,223.5 221.5,224 221.5,224 222,224.5 222.5,224.5 223,225 223.5,225 224,225 224.5,225.5 225,225.5 225.5,225.5 226,226 226.5,226 227,226 227.5,226.5 228,226.5 228.5,226.5 229,226.5 229.5,226.5 230,226.5 230.5,226.5 230.5,226.5 231,226.5 231.5,227 232,227 232.5,227 233,227.5 233.5,228 234,228.5 234.5,229 235,230 235.5,231 236,231.5 236.5,233 237,234 237.5,235 238,236.5 238.5,238 239,239 239,241 239.5,242.5 240,244 240.5,246 241,247.5 241.5,249.5 242,251.5 242.5,253.5 243,256 243.5,258 244,260 244.5,262.5 245,264.5 245.5,267 246,269.5 246.5,272 247,274.5 247.5,277 248,279.5 248,282 248.5,284.5 249,287 249.5,289.5 250,292 250.5,295 251,297.5 251.5,298 252,298 252.5,298 253,298 253.5,298 254,298 254.5,298 255,298 255.5,298 256,298 256.5,298 257,298 257,298 257.5,298 258,298 258.5,298 259,298 259.5,298 260,298 260.5,298 261,298 261.5,298 262,298 262.5,298 263,298 263.5,298 264,298 264.5,298 265,298 265.5,298 265.5,298 266,298 266.5,298 267,298 267.5,298 268,298 268.5,298 269,298 269.5,298 269.5,298" fill="#ffc078" fill-opacity="0.8"/>
  <line x1="70" y1="298" x2="480" y2="298" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="40" y="283.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$G$</div></foreignObject>
  <polyline points="70,298 70.5,298 71.5,298 72,298 72.5,298 73.5,298 74,298 75,298 75.5,298 76,298 77,298 77.5,298 78,298 79,298 79.5,298 80,298 81,298 81.5,298 82.5,298 83,298 83.5,298 84.5,298 85,298 85.5,298 86.5,298 87,298 88,298 88.5,298 89,298 90,298 90.5,298 91,298 92,298 92.5,298 93,298 94,298 94.5,298 95.5,298 96,298 96.5,298 97.5,298 98,298 98.5,298 99.5,298 100,298 101,298 101.5,298 102,298 103,298 103.5,298 104,298 105,298 105.5,298 106,298 107,298 107.5,298 108.5,298 109,298 109.5,298 110.5,298 111,298 111.5,298 112.5,298 113,298 113.5,298 114.5,298 115,298 116,298 116.5,298 117,298 118,298 118.5,298 119,298 120,298 120.5,298 121,298 122,298 122.5,298 123.5,298 124,298 124.5,298 125.5,298 126,298 126.5,298 127.5,298 128,298 129,298 129.5,298.5 130,298.5 131,299 131.5,299.5 132,300.5 133,301 133.5,302 134,302.5 135,303.5 135.5,304.5 136.5,306 137,307 137.5,308 138.5,309.5 139,311 139.5,312 140.5,313.5 141,315 142,316 142.5,317.5 143,319 144,320.5 144.5,321.5 145,323 146,324.5 146.5,325.5 147,326.5 148,328 148.5,329 149.5,330 150,331 150.5,331.5 151.5,332.5 152,333 152.5,333.5 153.5,334 154,334.5 154.5,335 155.5,335 156,335 157,335 157.5,335 158,334.5 159,334 159.5,333.5 160,332.5 161,331.5 161.5,330 162,328.5 163,327 163.5,325.5 164.5,323.5 165,321.5 165.5,319.5 166.5,317 167,315 167.5,312.5 168.5,309.5 169,307 170,304 170.5,301.5 171,298.5 172,295.5 172.5,292 173,289 174,286 174.5,282.5 175,279 176,276 176.5,272.5 177.5,269.5 178,266 178.5,263 179.5,259.5 180,256.5 180.5,253 181.5,250 182,247 183,244 183.5,241 184,238.5 185,236 185.5,233 186,230.5 187,228.5 187.5,226 188,224 189,222 189.5,220.5 190.5,218.5 191,217 191.5,216 192.5,214.5 193,213.5 193.5,213 194.5,212 195,211.5 195.5,211.5 196.5,211 197,211 198,211.5 198.5,211.5 199,211.5 200,211.5 200.5,211.5 201,212 202,212 202.5,212.5 203,212.5 204,213 204.5,213 205.5,213.5 206,214 206.5,214 207.5,214.5 208,215 208.5,215.5 209.5,216 210,216.5 211,217 211.5,217.5 212,217.5 213,218 213.5,218.5 214,219 215,219.5 215.5,220 216,220.5 217,221 217.5,221.5 218.5,222 219,222.5 219.5,223 220.5,223.5 221,223.5 221.5,224 222.5,224.5 223,224.5 224,225 224.5,225.5 225,225.5 226,226 226.5,226 227,226 228,226.5 228.5,226.5 229,226.5 230,226.5 230.5,226.5 231.5,226.5 232,227 232.5,227 233.5,228 234,228.5 234.5,229.5 235.5,230.5 236,232 236.5,233.5 237.5,235.5 238,237 239,239.5 239.5,241.5 240,244 241,246.5 241.5,249.5 242,252 243,255 243.5,258 244.5,261.5 245,265 245.5,268 246.5,271.5 247,275 247.5,279 248.5,282.5 249,286 249.5,290 250.5,293.5 251,297.5 252,301 252.5,305 253,308.5 254,312 254.5,315.5 255,319 256,322.5 256.5,326 257,329 258,332 258.5,335 259.5,338 260,340.5 260.5,343 261.5,345.5 262,348 262.5,350 263.5,351.5 264,353.5 265,355 265.5,356.5 266,357.5 267,358.5 267.5,359 268,359.5 269,360 269.5,360 270,360 271,360 271.5,360 272.5,360 273,360 273.5,360 274.5,360 275,360 275.5,360 276.5,360 277,360 277.5,360 278.5,360 279,360 280,360 280.5,360 281,360 282,360 282.5,360 283,360 284,360 284.5,360 285,360 286,360 286.5,360 287.5,360 288,360 288.5,360 289.5,360 290,360 290.5,360 291.5,360 292,360 293,360 293.5,360 294,360 295,360 295.5,360 296,360 297,360 297.5,360 298,360 299,360 299.5,360 300.5,360 301,360 301.5,360 302.5,360 303,360 303.5,360 304.5,360 305,360 306,360 306.5,360 307,360 308,360 308.5,360 309,360 310,360 310.5,360 311,360 312,360 312.5,360 313.5,360 314,360 314.5,360 315.5,360 316,360 316.5,360 317.5,360 318,360 318.5,360 319.5,360 320,360 321,360 321.5,360 322,360 323,360 323.5,360 324,360 325,360 325.5,360 326,360 327,360 327.5,360 328.5,360 329,360 329.5,360 330.5,360 331,360 331.5,360 332.5,360 333,360 334,360 334.5,360 335,360 336,360 336.5,360 337,360 338,360 338.5,360 339,360 340,360 340.5,360 341.5,360 342,360 342.5,360 343.5,360 344,360 344.5,360 345.5,360 346,360 347,360 347.5,360 348,360 349,360 349.5,360 350,360 351,360 351.5,360 352,360 353,360 353.5,360 354.5,360 355,360 355.5,360 356.5,360 357,360 357.5,360 358.5,360 359,360 359.5,360 360.5,360 361,360 362,360 362.5,360 363,360 364,360 364.5,360 365,360 366,360 366.5,360 367.5,360 368,360 368.5,360 369.5,360 370,360 370.5,360 371.5,360 372,360 372.5,360 373.5,360 374,360 375,360 375.5,360 376,360 377,360 377.5,360 378,360 379,357.5 379.5,348.5 380,333.5 381,312 381.5,286.5 382.5,257.5 383,226.5 383.5,195 384.5,165 385,137.5 385.5,114 386.5,95.5 387,83.5 388,77.5 388.5,77 389,77 390,78 390.5,79.5 391,81.5 392,84 392.5,87 393,91 394,95.5 394.5,100.5 395.5,106 396,111.5 396.5,118 397.5,125 398,132 398.5,139.5 399.5,147.5 400,155.5 400.5,164 401.5,172.5 402,181 403,189.5 403.5,198.5 404,207 405,216 405.5,224.5 406,233 407,241.5 407.5,249.5 408,257.5 409,265 409.5,272.5 410.5,279.5 411,286 411.5,292 412.5,297.5 413,302.5 413.5,307 414.5,311 415,314.5 416,317.5 416.5,319.5 417,321.5 418,322.5 418.5,323 419,323 420,322.5 420.5,322.5 421,322.5 422,322.5 422.5,322 423.5,322 424,321.5 424.5,321.5 425.5,321 426,320.5 426.5,320 427.5,319.5 428,319.5 429,319 429.5,318 430,317.5 431,317 431.5,316.5 432,316 433,315.5 433.5,314.5 434,314 435,313.5 435.5,312.5 436.5,312 437,311.5 437.5,310.5 438.5,310 439,309 439.5,308.5 440.5,308 441,307 441.5,306.5 442.5,306 443,305 444,304.5 444.5,304 445,303.5 446,303 446.5,302.5 447,302 448,301.5 448.5,301 449,300.5 450,300 450.5,299.5 451.5,299.5 452,299 452.5,299 453.5,298.5 454,298.5 454.5,298 455.5,298 456,298 457,298 457.5,298 458,298 459,298 459.5,298 460,298 461,298 461.5,298 462,298 463,298 463.5,298 464.5,298 465,298 465.5,298 466.5,298 467,298 467.5,298 468.5,298 469,298 470,298 470.5,298 471,298 472,298 472.5,298 473,298 474,298 474.5,298 475,298 476,298 476.5,298 477.5,298 478,298 478.5,298 479.5,298 480,298" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="129" y="291.5" width="41" height="38" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:32px">$\boldsymbol{-}$</div></foreignObject>
  <foreignObject x="193.5" y="248" width="41" height="38" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:32px">$\boldsymbol{+}$</div></foreignObject>
  <line x1="269.5" y1="380" x2="378.5" y2="380" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="269.5" y1="372" x2="269.5" y2="388" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="378.5" y1="372" x2="378.5" y2="388" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="282.5" y="389.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{lento}$</div></foreignObject>
  <circle cx="99" cy="270" r="13" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="90.5" y="259" width="17" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:18px">$\text{1}$</div></foreignObject>
  <circle cx="112" cy="329" r="13" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="103.5" y="318" width="17" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:18px">$\text{2}$</div></foreignObject>
  <circle cx="181.5" cy="189.5" r="13" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="173" y="178.5" width="17" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:18px">$\text{3}$</div></foreignObject>
  <circle cx="324" cy="332" r="13" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="315.5" y="321" width="17" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:18px">$\text{4}$</div></foreignObject>
  <circle cx="405" cy="110" r="13" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="396.5" y="99" width="17" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:18px">$\text{5}$</div></foreignObject>
  <circle cx="466.5" cy="270" r="13" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="458" y="259" width="17" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:18px">$\text{6}$</div></foreignObject>
</svg>
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, miten hyppäät, mitä mittaat ja mitä pidät samana hypystä toiseen.

::: tuki O
**Ohjattu.** Nollaa voimalevy ohjelmasta ennen kuin astut levylle. Käynnistä mittaus, seiso levyllä aivan paikallasi ainakin sekunnin ajan, kyykisty nopeasti, ponnista suoraan ylös ja laskeudu molemmille jaloille takaisin levylle. Seiso lopuksi taas paikallasi, kunnes lopetat mittauksen. Pidä kädet lanteilla koko hypyn ajan, jotta käsien heilautus ei muutu hypystä toiseen. Tee ainakin viisi hyppyä ja tallenna jokainen omaksi mittaukseksi. Toinen menetelmä on lentoaika, jonka luet samasta kuvaajasta.
:::

::: tuki OO
**Osittain ohjattu.** Lähtönopeus määritetään voimamittauksesta impulssiperiaatteella. Päätä itse hyppytapa, hyppyjen määrä ja toinen menetelmä hyppykorkeudelle. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Miksi hyppääjän pitää seistä paikallaan ennen hyppyä? Mitä tapahtuu tulokselle, jos hän liikkuu jo mittauksen alussa?
- Miten tunnistat kuvaajasta irtoamishetken ja alastulohetken, kun lukema ei ole lennon aikana tarkalleen nolla mittauskohinan takia?
- Miten käsien heilautus, alastulo varpailleen tai polvet koukussa ja levyn ulkopuolelle laskeutuminen vaikuttavat kumpaankin menetelmään?
- Mitä lentoaikamenetelmä ei tarvitse, jota impulssimenetelmä tarvitsee? Mieti esimerkiksi painon lukemista ja sitä, näyttääkö levy voiman oikein. Mitä oletusta lentoaikamenetelmä taas tarvitsee, jota impulssimenetelmä ei tarvitse?
- Mitä mittausohjelman asetuksia tarvitset? Kysy opettajalta, mikä näytteenottotaajuus on sopiva, jotta irtoamis- ja alastulohetki erottuvat tarkasti.
:::

## Mittaa

Tallenna jokaisen hypyn alkuperäinen mittausdata omaksi tiedostokseen tai omaksi mittaussarjakseen, jotta voit palata siihen myöhemmin. Kirjaa jokaisesta hypystä kuvaajasta luetut ja niistä lasketut suureet taulukkoon.

::: tuki O
Voit käyttää esimerkiksi tällaisia taulukoita. Ensimmäiseen kirjaat kuvaajasta luetut suureet, toiseen niistä lasketut.

| hyppy | $\dfrac{I}{G}\ (\text{s})$ | $t_\text{lento}\ (\text{s})$ |
|---|---|---|
| 1. | | |
| 2. | | |
| 3. | | |

| hyppy | $v_0\ (\text{m/s})$ | $h\ (\text{m})$, impulssista | $h\ (\text{m})$, lentoajasta |
|---|---|---|---|
| 1. | | | |
| 2. | | | |
| 3. | | | |

Lue paino $G$ keskiarvona siltä ajalta, jolloin hyppääjä seisoo paikallaan ennen hyppyä; sitä ei tarvitse kirjata taulukkoon. Rajaa pinta-alan laskeminen niin, että se alkaa juuri ennen kuin voima alkaa muuttua ja päättyy irtoamishetkeen, jolloin lukema putoaa nollaan. Lentoaika on irtoamishetken ja alastulohetken välinen aika.

Hylkää hyppy esimerkiksi silloin, jos hyppääjä liikkui jo ennen hypyn alkua tai laskeutui osittain levyn ulkopuolelle, ja kirjaa, miksi hylkäsit sen.
:::

Kirjaa myös hylkäämäsi hypyt ja hylkäämisen perusteet. Muista mittausepävarmuus: kirjaa, kuinka tarkasti voit lukea painon, irtoamishetken ja alastulohetken. [[apua:fy1-3|Toistomittausten keskiarvo ja epävarmuus]]

## Käsittele tulokset

Esitä yhden onnistuneen hypyn voima–aika-kuvaaja ja merkitse siihen hypyn vaiheet. Laske jokaisesta hypystä liikemäärän muutos (tai impulssi painon monikertana), lähtönopeus ja hypyn korkeus kahdella menetelmällä.

Vastaa:

1. Mitä kuvaajan kukin osa kertoo hypyn vaiheesta? Missä vaiheissa tukivoima on painoa pienempi, missä suurempi ja missä nolla, ja miksi?
2. Miksi hyppääjään kohdistuva tukivoima voi olla ponnistuksen aikana suurempi kuin paino? Mitä se kertoo hyppääjän kiihtyvyydestä?
3. Mikä pinta-ala kuvaajassa vastaa liikemäärän muutosta ponnistuksen aikana, ja miksi osa siitä lasketaan negatiiviseksi?
4. Ovatko kahdella menetelmällä saadut korkeudet samaa suuruusluokkaa? Kumpi on suurempi useimmissa hypyissä?

::: tuki O OO
**Vihje pinta-alaan.** Monet mittausohjelmat laskevat käyrän alle jäävän pinta-alan valitulta väliltä. Jos ohjelma laskee pinta-alan aika-akseliin asti, se antaa tukivoiman $N$ impulssin, ja kokonaisvoiman impulssi saadaan, kun siitä vähennetään painon impulssi $G\cdot T$, missä $T$ on valitun välin pituus. Taulukkolaskennassa voit laskea jokaiselle mittauspisteelle sarakkeen $(N_i - G)\cdot\Delta t$ ja summata sen valitulta väliltä.
:::

Pinta-alan määrittämiseen voit käyttää voimalevyn mittausohjelmaa, Graphical Analysis -ohjelmaa tai taulukkolaskentaa. Ruukkilabran ohje ohjelmien käyttöön on tekeillä.

## Epävarmuus ja luotettavuus

Ilmoita hypyn korkeus kummallakin menetelmällä muodossa $\bar{h} \pm \Delta h$ ja perustele, miten arvioit epävarmuuden. Vertaa tuloksia: ovatko ne sopusoinnussa epävarmuuksien rajoissa? Päällekkäiset epävarmuusvälit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi.

::: tuki O OO
Epävarmuuden voit arvioida esimerkiksi näin:

- **Toistojen hajonta.** Laske kummankin menetelmän korkeuksien keskiarvo $\bar{h}$ onnistuneista hypyistä ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta h = \dfrac{h_\text{max} - h_\text{min}}{2}$. Hajonta sisältää sekä mittauksen epätarkkuuden että sen, että hypyt olivat todella eri korkuisia.
- **Herkkyys painolle.** Jos paino $G$ on luettu hieman väärin, virhe kertautuu koko sen ajan $T$, jolta pinta-ala lasketaan: impulssiin tulee virhe $\Delta G \cdot T$. Siksi pinta-alan laskeminen kannattaa aloittaa vasta juuri ennen liikkeen alkua.
- **Herkkyys lentoajalle.** Korkeus on verrannollinen lentoajan neliöön, joten korkeuden suhteellinen epävarmuus on noin kaksi kertaa lentoajan suhteellinen epävarmuus.

Pyöristä $\Delta h$ yhteen merkitsevään numeroon ja $\bar{h}$ samaan desimaaliin.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä tekijät aiheuttavat suurimmat epävarmuudet kummassakin menetelmässä? Ovatko ne satunnaisia vai systemaattisia, ja kumpaan suuntaan systemaattiset virheet muuttavat kumpaakin korkeutta? Jos tulokset eivät ole sopusoinnussa, mikä menetelmän oletuksista ei todennäköisesti pätenyt? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Miten voima–aika-kuvaajasta saatiin hyppääjän lähtönopeus ja hypyn korkeus, ja kuinka hyvin kahdella menetelmällä saadut korkeudet vastasivat toisiaan? Viittaa kuvaajaan, esimerkiksi "kuvaajasta 1 nähdään, että …". Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** miten lähtönopeus saadaan impulssiperiaatteesta ja korkeus lähtönopeudesta, ja mihin oletuksiin toinen menetelmä perustuu.
- **Työn suunnitelma:** hyppytapa, miten pidit sen samana, hyppyjen määrä ja hylkäämisen perusteet.
- **Mittaustulokset:** yhden hypyn voima–aika-kuvaaja vaiheineen ja taulukko, jossa kuvaajasta luetut suureet ovat ennen niistä laskettuja. Voimat ja impulssin voit ilmoittaa painon monikertoina; hyppääjän painoa ja massaa ei tarvitse ilmoittaa.
- **Tulos:** hypyn korkeus kummallakin menetelmällä epävarmuuksineen oikein pyöristettynä.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet kummassakin menetelmässä ja niiden vaikutuksen suunta.

## Laajennus: kyykkyhyppy ja vastaliikehyppy

Edellä hyppääjä kyykistyi nopeasti juuri ennen ponnistusta. Tätä kutsutaan **vastaliikehypyksi**. **Kyykkyhypyssä** hyppääjä laskeutuu ensin kyykkyyn, pysähtyy siihen hetkeksi ja ponnistaa vasta sitten ilman uutta alaspäin suuntautuvaa liikettä.

Ennusta ensin, kummalla tavalla hyppäät korkeammalle ja miten kuvaajat eroavat toisistaan ennen irtoamista. Tee sitten useita kyykkyhyppyjä samalla käsien asennolla kuin päämittauksessa ja määritä niiden korkeus samoilla menetelmillä. Vertaa kahden hyppytavan korkeuksia epävarmuuksineen ja vertaa kuvaajia toisiinsa: mikä kuvaajan osa puuttuu kyykkyhypystä, ja miten ero näkyy impulssissa?

::: tuki O OO
**Vihjeitä.** Kyykkyhypyssä pinta-alan laskeminen alkaa siitä, kun hyppääjä on pysähtynyt kyykkyyn, ja tukivoima on silloin taas yhtä suuri kuin paino. Jos kuvaajassa näkyy pieni notko juuri ennen ponnistusta, hyppääjä on tehnyt pienen vastaliikkeen: hylkää hyppy tai kerro siitä raportissa.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
