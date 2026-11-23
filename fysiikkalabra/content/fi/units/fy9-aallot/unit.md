# Värähtely, aallot ja ääni

> **Miksi** uinninvalvojan pillin vihellys kuuluu myös veden alle, ja muuttuuko ääni matkalla ilmasta veteen?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: uimahalli poikkileikkauksena. Taustalla laatoitettu seinä ja korkeat ikkunat. Vasemmalla allasreunalla on uinninvalvojan korkea tuoli, jonka käsinojalta roikkuu pilli. Pillistä lähtee ilmaan tiheästi toisiaan seuraavia aaltorintamien kaaria kohti allasta. Oikealla allas sivulta nähtynä: vesi, pinnalla ratamerkkiköysi kohoineen ja pohjalla tumma ratamerkintä. Veden alla samat aaltorintamat jatkuvat noin neljä kertaa harvempina." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-aallot-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

Moduulin kaikki ilmiöt alkavat **värähtelystä**: kappale liikkuu edestakaisin tasapainoasemansa molemmin puolin, ja liikettä kuvaavat jaksonaika $T$, taajuus $f$ ja amplitudi $A$. Jousen ja heilurin jaksonaika määräytyy värähtelijästä itsestään. **Aalto** on värähtely, joka etenee väliaineessa: hiukkaset värähtelevät paikoillaan, ja aalto kuljettaa energiaa mutta ei ainetta. **Ääni** on pitkittäinen paineaalto. Sen korkeus määräytyy taajuudesta ja voimakkuus intensiteetistä.

<svg data-fig="kartta" viewBox="0 0 380 896" role="img" aria-label="Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Aloita kysymällä, onko tehtävässä liike vai aalto, ja katso, mikä tunnusmerkki sopii. Massa jousen päässä: värähtelijän jaksonaika on kaksi pii kertaa neliöjuuri massasta jaettuna jousivakiolla. Heiluri, pieni kulma: jaksonaika on kaksi pii kertaa neliöjuuri pituudesta jaettuna putoamiskiihtyvyydellä. Aallon nopeus, taajuus, pituus: aaltoyhtälö, nopeus on taajuus kertaa aallonpituus. Kaksi lähdettä, voimistuu: matkaero on kokonaisluku kertaa aallonpituus. Kaksi lähdettä, vaimenee: matkaero on kokonaisluku ja puoli kertaa aallonpituus. Kieli tai avoin putki: seisova aalto, ominaistaajuus on n kertaa nopeus jaettuna kahdella pituudella. Kaksi lähes samaa taajuutta: huojunta, huojuntataajuus on taajuuksien erotuksen itseisarvo. Lähde tai havaitsija liikkuu: taajuus muuttuu, kyseessä on Dopplerin ilmiö. Äänen voimakkuus desibeleinä: intensiteettitaso on kymmenen kertaa intensiteetin ja kynnysintensiteetin suhteen kymmenkantainen logaritmi desibeleinä." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="837" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{mistä tunnistan lain?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{liike vai aalto? katso tunnusmerkki}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{massa jousen päässä}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="156" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{jaksonaika}$</div></foreignObject>
  <rect x="212" y="140" width="150" height="28" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="216" y="133.5" width="142" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$T = 2\pi\sqrt{m/k}$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{heiluri, pieni kulma}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="156" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{jaksonaika}$</div></foreignObject>
  <rect x="212" y="226" width="150" height="28" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="216" y="219.5" width="142" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$T = 2\pi\sqrt{l/g}$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{aallon nopeus, taajuus, pituus}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{aaltoyhtälö}$</div></foreignObject>
  <rect x="238" y="314" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="316" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$v = f\lambda$</div></foreignObject>
  <line x1="14" y1="392" x2="30" y2="392" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kaksi lähdettä, voimistuu}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{matkaero}$</div></foreignObject>
  <rect x="238" y="400" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="402" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Delta s = n\lambda$</div></foreignObject>
  <line x1="14" y1="478" x2="30" y2="478" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="442" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="452.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kaksi lähdettä, vaimenee}$</div></foreignObject>
  <line x1="40" y1="482" x2="362" y2="482" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="487" width="146" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{matkaero}$</div></foreignObject>
  <rect x="202" y="486" width="160" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="206" y="488" width="152" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Delta s = (n + 1/2)\lambda$</div></foreignObject>
  <line x1="14" y1="564" x2="30" y2="564" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="528" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="538.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kieli tai avoin putki}$</div></foreignObject>
  <line x1="40" y1="568" x2="362" y2="568" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="573" width="176" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{seisova aalto}$</div></foreignObject>
  <rect x="232" y="572" width="130" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="236" y="574" width="122" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$f_n = n\,v/(2L)$</div></foreignObject>
  <line x1="14" y1="650" x2="30" y2="650" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="614" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="624.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kaksi lähes samaa taajuutta}$</div></foreignObject>
  <line x1="40" y1="654" x2="362" y2="654" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="659" width="156" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{huojunta}$</div></foreignObject>
  <rect x="212" y="658" width="150" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="216" y="660" width="142" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$f_\text{H} = |f_1 - f_2|$</div></foreignObject>
  <line x1="14" y1="736" x2="30" y2="736" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="700" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="710.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{lähde tai havaitsija liikkuu}$</div></foreignObject>
  <line x1="40" y1="740" x2="362" y2="740" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="745" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{taajuus muuttuu}$</div></foreignObject>
  <rect x="238" y="744" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="746" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\text{Doppler}$</div></foreignObject>
  <line x1="14" y1="837" x2="30" y2="837" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="786" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="796.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{äänen voimakkuus desibeleinä}$</div></foreignObject>
  <line x1="40" y1="826" x2="362" y2="826" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="831" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{intensiteettitaso}$</div></foreignObject>
  <rect x="172" y="860" width="190" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="176" y="862" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$L = 10\lg(I/I_0)\,\text{dB}$</div></foreignObject>
</svg>

Kokeen aaltotehtävissä kannattaa ensin kysyä, mikä määrää minkin suureen. Taajuuden määrää lähde, nopeuden väliaine, ja aallonpituus seuraa niistä. Kun aalto kohtaa esteen, raon tai toisen aallon, se heijastuu, taipuu tai interferoi, ja kaikissa ratkaisee matkojen vertaaminen aallonpituuteen.

Tästä saadaan vastaus alun kysymykseen. Pilli värähtelee taajuudella $3{,}0\,\text{kHz}$, ja sama taajuus säilyy, kun ääni siirtyy veteen, joten sävel on sama. Äänen nopeus on hallin lämpimässä ilmassa noin $350\,\text{m/s}$ ja vedessä noin $1500\,\text{m/s}$, joten aallonpituus kasvaa $0{,}12\,\text{m}$:stä $0{,}50\,\text{m}$:iin. Valtaosa äänestä kuitenkin heijastuu vedenpinnasta, joten veden alla vihellys kuuluu heikkona.

<svg data-fig="pilli" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva mittakaavassa: saman pillin ääni paineaaltona ilmassa ja vedessä, kummassakin yhden metrin matka yhtä pitkänä. Ylempänä ilmassa aallonpituus on 0,12 metriä, joten metrille mahtuu lähes yhdeksän aaltoa. Alempana vedessä aallonpituus on 0,50 metriä, ja metrille mahtuu kaksi aaltoa. Kummassakin yksi aallonpituus on merkitty hakasulkeella, ja nuoli näyttää etenemissuunnan. Käyrä kuvaa paineen vaihtelua. Taajuus on molemmissa sama, 3,0 kilohertsiä, mutta äänen nopeus on ilmassa noin 350 ja vedessä noin 1500 metriä sekunnissa." style="max-width:100%;font-size:26px">
  <foreignObject x="86.5" y="4.5" width="427" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$\text{paineaalto, sama taajuus } f = 3{,}0\,\text{kHz}$</div></foreignObject>
  <rect x="14" y="72" width="420" height="92" rx="8" fill="#eef5f9" stroke="#c9c2b2" stroke-width="1.5"/>
  <line x1="24" y1="118" x2="424" y2="118" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <polyline points="24,118 25.5,111.5 27.5,105 29,99.5 30.5,94.5 32.5,91 34,89 35.5,88 37.5,89 39,91 40.5,94.5 42.5,99.5 44,105 45.5,111.5 47.5,118 49,124.5 50.5,131 52.5,136.5 54,141.5 55.5,145 57.5,147 59,148 60.5,147 62.5,145 64,141.5 65.5,136.5 67.5,131 69,124.5 70.5,118 72.5,111.5 74,105 75.5,99.5 77.5,94.5 79,91 80.5,89 82.5,88 84,89 85.5,91 87.5,94.5 89,99.5 90.5,105 92.5,111.5 94,118 95.5,124.5 97.5,131 99,136.5 100.5,141.5 102.5,145 104,147 105.5,148 107.5,147 109,145 110.5,141.5 112.5,136.5 114,131 115.5,124.5 117.5,118 119,111.5 120.5,105 122.5,99.5 124,94.5 125.5,91 127.5,89 129,88 130.5,89 132.5,91 134,94.5 135.5,99.5 137.5,105 139,111.5 140.5,118 142.5,124.5 144,131 145.5,136.5 147.5,141.5 149,145 150.5,147 152.5,148 154,147 155.5,145 157.5,141.5 159,136.5 160.5,131 162.5,124.5 164,118 165.5,111.5 167.5,105 169,99.5 170.5,94.5 172.5,91 174,89 175.5,88 177.5,89 179,91 180.5,94.5 182.5,99.5 184,105 185.5,111.5 187.5,118 189,124.5 190.5,131 192.5,136.5 194,141.5 195.5,145 197.5,147 199,148 200.5,147 202.5,145 204,141.5 205.5,136.5 207.5,131 209,124.5 210.5,118 212.5,111.5 214,105 215.5,99.5 217.5,94.5 219,91 220.5,89 222.5,88 224,89 225.5,91 227.5,94.5 229,99.5 230.5,105 232.5,111.5 234,118 235.5,124.5 237.5,131 239,136.5 240.5,141.5 242.5,145 244,147 245.5,148 247.5,147 249,145 250.5,141.5 252.5,136.5 254,131 255.5,124.5 257.5,118 259,111.5 260.5,105 262.5,99.5 264,94.5 265.5,91 267.5,89 269,88 270.5,89 272.5,91 274,94.5 275.5,99.5 277.5,105 279,111.5 280.5,118 282.5,124.5 284,131 285.5,136.5 287.5,141.5 289,145 290.5,147 292.5,148 294,147 295.5,145 297.5,141.5 299,136.5 300.5,131 302.5,124.5 304,118 305.5,111.5 307.5,105 309,99.5 310.5,94.5 312.5,91 314,89 315.5,88 317.5,89 319,91 320.5,94.5 322.5,99.5 324,105 325.5,111.5 327.5,118 329,124.5 330.5,131 332.5,136.5 334,141.5 335.5,145 337.5,147 339,148 340.5,147 342.5,145 344,141.5 345.5,136.5 347.5,131 349,124.5 350.5,118 352.5,111.5 354,105 355.5,99.5 357.5,94.5 359,91 360.5,89 362.5,88 364,89 365.5,91 367.5,94.5 369,99.5 370.5,105 372.5,111.5 374,118 375.5,124.5 377.5,131 379,136.5 380.5,141.5 382.5,145 384,147 385.5,148 387.5,147 389,145 390.5,141.5 392.5,136.5 394,131 395.5,124.5 397.5,118 399,111.5 400.5,105 402.5,99.5 404,94.5 405.5,91 407.5,89 409,88 410.5,89 412.5,91 414,94.5 415.5,99.5 417.5,105 419,111.5 420.5,118 422.5,124.5 424,131" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <foreignObject x="446" y="84.5" width="62" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{ilma}$</div></foreignObject>
  <foreignObject x="446" y="119.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda \approx 0{,}12\,\text{m}$</div></foreignObject>
  <path d="M35.5,84 V78 H82.5 V84" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="49" y="47.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <foreignObject x="24" y="167.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v \approx 350\,\text{m/s}$</div></foreignObject>
  <rect x="14" y="232" width="420" height="92" rx="8" fill="#dcecf8" stroke="#c9c2b2" stroke-width="1.5"/>
  <line x1="24" y1="278" x2="424" y2="278" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 5"/>
  <polyline points="24,278 25.5,276.5 27.5,275 29,273.5 30.5,272 32.5,270 34,268.5 35.5,267 37.5,266 39,264.5 40.5,263 42.5,261.5 44,260.5 45.5,259 47.5,258 49,257 50.5,255.5 52.5,254.5 54,253.5 55.5,253 57.5,252 59,251.5 60.5,250.5 62.5,250 64,249.5 65.5,249 67.5,248.5 69,248.5 70.5,248 72.5,248 74,248 75.5,248 77.5,248 79,248.5 80.5,248.5 82.5,249 84,249.5 85.5,250 87.5,250.5 89,251.5 90.5,252 92.5,253 94,253.5 95.5,254.5 97.5,255.5 99,257 100.5,258 102.5,259 104,260.5 105.5,261.5 107.5,263 109,264.5 110.5,266 112.5,267 114,268.5 115.5,270 117.5,272 119,273.5 120.5,275 122.5,276.5 124,278 125.5,279.5 127.5,281 129,282.5 130.5,284 132.5,286 134,287.5 135.5,289 137.5,290 139,291.5 140.5,293 142.5,294.5 144,295.5 145.5,297 147.5,298 149,299 150.5,300.5 152.5,301.5 154,302.5 155.5,303 157.5,304 159,304.5 160.5,305.5 162.5,306 164,306.5 165.5,307 167.5,307.5 169,307.5 170.5,308 172.5,308 174,308 175.5,308 177.5,308 179,307.5 180.5,307.5 182.5,307 184,306.5 185.5,306 187.5,305.5 189,304.5 190.5,304 192.5,303 194,302.5 195.5,301.5 197.5,300.5 199,299 200.5,298 202.5,297 204,295.5 205.5,294.5 207.5,293 209,291.5 210.5,290 212.5,289 214,287.5 215.5,286 217.5,284 219,282.5 220.5,281 222.5,279.5 224,278 225.5,276.5 227.5,275 229,273.5 230.5,272 232.5,270 234,268.5 235.5,267 237.5,266 239,264.5 240.5,263 242.5,261.5 244,260.5 245.5,259 247.5,258 249,257 250.5,255.5 252.5,254.5 254,253.5 255.5,253 257.5,252 259,251.5 260.5,250.5 262.5,250 264,249.5 265.5,249 267.5,248.5 269,248.5 270.5,248 272.5,248 274,248 275.5,248 277.5,248 279,248.5 280.5,248.5 282.5,249 284,249.5 285.5,250 287.5,250.5 289,251.5 290.5,252 292.5,253 294,253.5 295.5,254.5 297.5,255.5 299,257 300.5,258 302.5,259 304,260.5 305.5,261.5 307.5,263 309,264.5 310.5,266 312.5,267 314,268.5 315.5,270 317.5,272 319,273.5 320.5,275 322.5,276.5 324,278 325.5,279.5 327.5,281 329,282.5 330.5,284 332.5,286 334,287.5 335.5,289 337.5,290 339,291.5 340.5,293 342.5,294.5 344,295.5 345.5,297 347.5,298 349,299 350.5,300.5 352.5,301.5 354,302.5 355.5,303 357.5,304 359,304.5 360.5,305.5 362.5,306 364,306.5 365.5,307 367.5,307.5 369,307.5 370.5,308 372.5,308 374,308 375.5,308 377.5,308 379,307.5 380.5,307.5 382.5,307 384,306.5 385.5,306 387.5,305.5 389,304.5 390.5,304 392.5,303 394,302.5 395.5,301.5 397.5,300.5 399,299 400.5,298 402.5,297 404,295.5 405.5,294.5 407.5,293 409,291.5 410.5,290 412.5,289 414,287.5 415.5,286 417.5,284 419,282.5 420.5,281 422.5,279.5 424,278" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <foreignObject x="446" y="244.5" width="62" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{vesi}$</div></foreignObject>
  <foreignObject x="446" y="279.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda \approx 0{,}50\,\text{m}$</div></foreignObject>
  <path d="M74,244 V238 H274 V244" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="164" y="207.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <foreignObject x="24" y="327.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v \approx 1500\,\text{m/s}$</div></foreignObject>
  <line x1="446" y1="362" x2="528" y2="362" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M540,362 L527,368 L527,356 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="446" y="321.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{etenee}$</div></foreignObject>
  <line x1="24" y1="360" x2="424" y2="360" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="24" y1="352" x2="24" y2="368" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="424" y1="352" x2="424" y2="368" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="201.5" y="327.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1\,\text{m}$</div></foreignObject>
</svg>

## Kaava: Värähtely, aallot ja ääni

### Värähtelijät

```kaavat
taajuus :: f = \frac{1}{T}
harmoninen voima :: \overline{F} = -k\overline{x}
harmonisen värähtelijän jaksonaika :: T = 2\pi\sqrt{\frac{m}{k}}
matemaattisen heilurin jaksonaika :: T = 2\pi\sqrt{\frac{l}{g}}
```

missä $f$ on taajuus ($\text{Hz}$), $T$ jaksonaika ($\text{s}$), $\overline{F}$ jousen voima ($\text{N}$), $k$ jousivakio ($\text{N/m}$), $\overline{x}$ poikkeama tasapainoasemasta ($\text{m}$); miinusmerkki kertoo, että voima osoittaa kohti tasapainoasemaa, $m$ massa ($\text{kg}$) ja $l$ heilurin pituus ($\text{m}$). Jousen voima pätee, kun jousta ei venytetä liikaa. Heilurin jaksonaika pätee pienillä heilahduksilla, eikä se riipu massasta. Jousen potentiaalienergia on $E_\text{p} = \tfrac12 kx^2$, ja ilman kitkaa värähtelyn energia $\tfrac12 kA^2$ säilyy.

### Aallot

```kaavat
aaltoliikkeen perusyhtälö :: v = f\lambda
\Delta s = n\lambda
\Delta s = \left(n + \tfrac12\right)\lambda
```

missä $v$ on aallon nopeus ($\text{m/s}$), $\lambda$ aallonpituus ($\text{m}$) ja $\Delta s$ matkaero kahdesta samassa vaiheessa värähtelevästä lähteestä ($\text{m}$), $n = 0, 1, 2, \ldots$ Ensimmäinen ehto antaa vahvistavan ja toinen heikentävän interferenssin. Diffraktio on voimakasta, kun raon tai esteen leveys on aallonpituuden suuruinen tai pienempi. Heijastuksessa tulokulma on heijastuskulman suuruinen, kun kulmat mitataan pinnan normaalista.

Seisovassa aallossa vierekkäisten solmujen väli on $\tfrac{\lambda}{2}$. Kielellä ja avoimella putkella on ominaistaajuudet $f_n = n \cdot \tfrac{v}{2L}$, $n = 1, 2, 3, \ldots$, ja toisesta päästä suljetulla putkella $f_n = n \cdot \tfrac{v}{4L}$, $n = 1, 3, 5, \ldots$, missä $L$ on kielen tai putken pituus.

<svg data-fig="ominais" viewBox="0 0 600 466" role="img" aria-label="Kaavakuva, ei mittakaavassa: kolme seisovaa aaltoa perustaajuudella allekkain, kaikki pituudeltaan L. Ylimpänä kahdesta päästä kiinnitetty kieli: päissä on solmu, keskellä kupu, ja kielen pituus on puolet aallonpituudesta. Keskellä molemmista päistä avoin putki: ilman siirtymän kuvut ovat putken päissä ja solmu keskellä, ja putken pituus on puolet aallonpituudesta. Alimpana toisesta päästä suljettu putki: suljetussa päässä on solmu ja avoimessa kupu, ja putken pituus on neljäsosa aallonpituudesta." style="max-width:100%;font-size:26px">
  <image href="pics/fy9/fy9-aallot-ominais.webp" x="0" y="0" width="600" height="470" preserveAspectRatio="none"/>
  <foreignObject x="390" y="36.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{kieli}$</div></foreignObject>
  <foreignObject x="390" y="74.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$L = \lambda/2$</div></foreignObject>
  <foreignObject x="190" y="245.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{S}$</div></foreignObject>
  <foreignObject x="30" y="245.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{K}$</div></foreignObject>
  <foreignObject x="350" y="245.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{K}$</div></foreignObject>
  <foreignObject x="390" y="174.5" width="143" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{avoin putki}$</div></foreignObject>
  <foreignObject x="390" y="212.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$L = \lambda/2$</div></foreignObject>
  <foreignObject x="54" y="379.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{S}$</div></foreignObject>
  <foreignObject x="350" y="379.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{K}$</div></foreignObject>
  <foreignObject x="390" y="308.5" width="184" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{suljettu putki}$</div></foreignObject>
  <foreignObject x="390" y="346.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$L = \lambda/4$</div></foreignObject>
  <foreignObject x="189" y="412.5" width="22" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$L$</div></foreignObject>
  <foreignObject x="390" y="431.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{S solmu, K kupu}$</div></foreignObject>
</svg>

### Ääni

```kaavat
huojunta :: f_\text{H} = |f_1 - f_2|
Dopplerin ilmiö, äänilähde liikkuu kohti havaitsijaa :: f = f_0\,\frac{v}{v - v_\text{L}}
Dopplerin ilmiö, äänilähde liikkuu pois päin havaitsijasta :: f = f_0\,\frac{v}{v + v_\text{L}}
Dopplerin ilmiö, havaitsija liikkuu kohti äänilähdettä :: f = f_0\,\frac{v + v_\text{H}}{v}
Dopplerin ilmiö, havaitsija liikkuu pois päin äänilähteestä :: f = f_0\,\frac{v - v_\text{H}}{v}
intensiteetti :: I = \frac{P}{A}
äänen intensiteettitaso :: L = 10\lg\left(\frac{I}{I_0}\right)\,\text{dB}
```

missä $f_\text{H}$ on huojuntataajuus ($\text{Hz}$), $f_0$ lähteen ja $f$ kuultu taajuus ($\text{Hz}$), $v$ äänen nopeus, $v_\text{L}$ lähteen ja $v_\text{H}$ havaitsijan nopeus ilman suhteen ($\text{m/s}$). Dopplerin kaavat pätevät, kun vain toinen liikkuu ja nopeus on äänen nopeutta pienempi. Intensiteetti on teho $P$ pinta-alaa $A$ kohti. Pistemäisen lähteen ääni jakautuu etäisyydellä $r$ pallon pinnalle, jonka ala on $A = 4\pi r^2$, kun heijastuksia ei ole. $L$ on intensiteettitaso ja $I_0 = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2$. Kaiusta etäisyys on $d = \tfrac{vt}{2}$, koska pulssi kulkee matkan kahdesti.

## Yleisiä virheitä {Virheet}

- **Amplitudi ääriasemasta toiseen.** Amplitudi mitataan tasapainoasemasta, joten se on puolet ääriasemien välistä.
- **Puolikas jakso.** Kaksi peräkkäistä tasapainoaseman ohitusta on vain $\tfrac{T}{2}$:n päässä toisistaan; jakso on kahden huipun väli.
- **Taajuus muuttuu väliaineessa.** Taajuus säilyy, kun aalto siirtyy väliaineesta toiseen; nopeus ja aallonpituus muuttuvat.
- **Ajanhetken kuva ja yhden kohdan kuvaaja sekaisin.** Lue ensin vaaka-akseli: $(x, y)$-kuvaajasta luetaan $\lambda$, $(t, y)$-kuvaajasta $T$.
- **Desibelit lasketaan yhteen.** Kaksi yhtä voimakasta riippumatonta lähdettä nostaa tasoa noin $3\,\text{dB}$, koska intensiteetit lasketaan yhteen.
- **Kaiku ilman kahdella jakamista.** Kaiku kulkee matkan edestakaisin, joten $d = \tfrac{vt}{2}$.
- **Dopplerin etumerkki.** Tarkista lopuksi, että lähestyminen antaa $f > f_0$ ja loittoneminen $f < f_0$.

## Kertaa tarvittaessa {Kertaa}

- Värähtelyn suureet: [*Värähtelyn suureet: jaksonaika, taajuus ja amplitudi*](fy5-7.html). Jousi ja sen energia: [*Jousivoima ja jousen energia*](fy5-8.html). Jaksonajat: [*Jousivärähtelijä ja heiluri*](fy5-9.html).
- Aallot: [*Aaltojen synty ja eteneminen*](fy5-10.html), [*Aalto kohtaa esteen tai raon*](fy5-11.html), [*Aaltojen yhteisvaikutus: superpositio ja interferenssi*](fy5-12.html) ja [*Seisova aalto: solmut, kuvut ja ominaistaajuudet*](fy5-13.html).
- Ääni: [*Ääni aaltona: korkeus, sointiväri ja Dopplerin ilmiö*](fy5-14.html), [*Intensiteetti ja desibeliasteikko*](fy5-15.html) ja [*Melu, akustiikka ja äänentoisto*](fy5-16.html).
- Kaiut ja maanjäristykset: [*Soveltava luku: ultraäänikuvaus ja maanjäristysaallot*](fy5-17.html).
