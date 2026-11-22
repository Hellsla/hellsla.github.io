# Virtapiiri, sähkövirta ja jännite

> **Miksi** taskulampun lamppu syttyy samalla hetkellä, kun painat katkaisijaa, vaikka johdon elektronit etenevät hitaammin kuin etana?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: pimeä huone illalla. Pöydällä on taskulamppu, jonka kylki on piirretty auki: sisällä näkyy kaksi paristoa peräkkäin, jousi ja katkaisija. Lampun valokeila valaisee pöytää ja seinää oikealla." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy61h-night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f2933"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy61h-table" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#a97a35"/></linearGradient><linearGradient id="fy61h-tube" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4f8fbf"/><stop offset="1" stop-color="#1971c2"/></linearGradient><linearGradient id="fy61h-head" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy61h-cell420" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient><linearGradient id="fy61h-cell556" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy61h-night)"/>
  <rect x="0" y="440" width="1200" height="160" fill="url(#fy61h-table)"/>
  <rect x="0" y="436" width="1200" height="8" fill="#f1dfb5"/>
  <path d="M0,470 Q600,463.829163520506 1200,474" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,492 Q600,491.40084824198675 1200,496" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,514 Q600,511.6439512766883 1200,518" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,536 Q600,532.5474926083261 1200,540" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,558 Q600,552.7240073720895 1200,562" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M0,580 Q600,580.2344871059468 1200,584" fill="none" stroke="#a97a35" stroke-width="2" stroke-linejoin="round" stroke-opacity="0.5"/>
  <path d="M790,390 L1200,170 L1200,440 Z" fill="#ffc078" stroke-linejoin="round" fill-opacity="0.55"/>
  <path d="M790,390 L1200,250 L1200,440 Z" fill="#f1dfb5" stroke-linejoin="round" fill-opacity="0.45"/>
  <ellipse cx="1150" cy="300" rx="44" ry="150" fill="#ffffff" fill-opacity="0.35"/>
  <rect x="330" y="344" width="400" height="92" rx="20" fill="url(#fy61h-tube)" stroke="#1f2933" stroke-width="4"/>
  <path d="M730,350 L790,330 L790,450 L730,430 Z" fill="url(#fy61h-head)" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <rect x="786" y="330" width="14" height="112" rx="4" fill="#8a96a3" stroke="#1f2933" stroke-width="3"/>
  <circle cx="788" cy="390" r="30" fill="#ffffff"/>
  <rect x="470" y="326" width="60" height="20" rx="8" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="372" y="358" width="330" height="64" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="420" y="368" width="128" height="44" rx="6" fill="url(#fy61h-cell420)" stroke="#1f2933" stroke-width="3"/>
  <rect x="504" y="370" width="36" height="40" fill="#f1dfb5"/>
  <rect x="548" y="382" width="9" height="16" rx="2" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <rect x="556" y="368" width="128" height="44" rx="6" fill="url(#fy61h-cell556)" stroke="#1f2933" stroke-width="3"/>
  <rect x="640" y="370" width="36" height="40" fill="#f1dfb5"/>
  <rect x="684" y="382" width="9" height="16" rx="2" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <polyline points="378,410 383,370 388,410 393,370 398,410 403,370 408,410 413,370 418,410" fill="none" stroke="#8a96a3" stroke-width="4" stroke-linejoin="round"/>
  <line x1="694" y1="390" x2="730" y2="390" stroke="#b8622d" stroke-width="5" stroke-linecap="butt"/>
</svg>

## Ydinajatus
Kaikki aine koostuu atomeista, joissa on positiivisesti varattuja protoneja ja negatiivisesti varattuja elektroneja. Varaukset vaikuttavat toisiinsa **sähköisellä vuorovaikutuksella**: samanmerkkiset varaukset hylkivät toisiaan ja erimerkkiset vetävät toisiaan puoleensa. Tavallisessa kappaleessa protoneja ja elektroneja on yhtä paljon, joten kappale on sähköisesti neutraali. Kun varauksia saadaan liikkumaan samaan suuntaan, syntyy **sähkövirta**. Sähkövirta on siis varauksen liikettä, ja sen avulla sähköinen vuorovaikutus siirtää energiaa paristosta lamppuun.

### Johteet ja eristeet
Aine, jossa varaukset pääsevät liikkumaan, on **johde**. Metalleissa osa elektroneista ei ole sidottu yksittäiseen atomiin, vaan ne liikkuvat vapaasti metalli-ionien välissä. Näitä kutsutaan vapaiksi elektroneiksi. Siksi kupari, alumiini ja muut metallit johtavat hyvin sähköä. Aine, jossa varaukset eivät pääse liikkumaan, on **eriste**: muovi, kumi, lasi ja kuiva puu. Sähköjohdossa on kuparinen johdin, jonka ympärillä on muovinen eristekuori. Eriste estää virtaa kulkemasta sinne, minne sen ei kuulu kulkea.

```pysahdy
Sähkömies käyttää kumikäsineitä. Miksi kumi suojaa sähkövirralta?
---
Kumi on eriste: sen varaukset eivät pääse liikkumaan, joten virta ei pääse käsineen läpi.
```

### Virtapiiri
Lamppu palaa vain, kun se on osa suljettua **virtapiiriä**: jännitelähteestä, kuten paristosta, lähtee johdin lamppuun ja lampusta johdin takaisin jännitelähteen toiseen napaan. Kytkin avaa ja sulkee piirin. Kun kytkin avataan, piiriin tulee katko. Kytkentämuutos etenee nopeasti koko virtapiiriin, ja virta lakkaa kulkemasta. Muutos ei kuitenkaan etene äärettömän nopeasti. Virtaa ei synny paristossa eikä se kulu lampussa. Lampun läpi kulkee yhtä suuri virta kuin piirin muissakin kohdissa, ja sama varaus palaa paristoon. Lamppu ei kuluta varausta vaan muuttaa sähköistä energiaa valoksi ja hehkulangan sisäenergiaksi, joka siirtyy lämpönä ympäristöön.

<svg data-fig="piiri" viewBox="0 0 600 340" role="img" aria-label="Suljettu virtapiiri pöydällä. Alhaalla vasemmalla kaksi AA-paristoa peräkkäin pidikkeessä, plusnapa oikealla. Pariston plusnavasta johto kulkee oikealle suljetun kytkimen kautta, nousee oikeaan yläkulmaan ja kulkee ylhäällä vasemmalle lampun kautta. Lamppu palaa. Johto palaa vasenta reunaa alas pariston miinusnapaan. Violetit nuolet näyttävät sovitun virran suunnan: plusnavasta ulkoisen piirin kautta miinusnapaan. Kaavakuva, ei mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-1-piiri.webp" x="0" y="-1.2" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="560" y="121.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="176.5" y="295.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{paristo}$</div></foreignObject>
  <foreignObject x="362.5" y="295.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kytkin}$</div></foreignObject>
  <foreignObject x="380" y="35.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{lamppu}$</div></foreignObject>
  <foreignObject x="118.5" y="81.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{johdin}$</div></foreignObject>
  <foreignObject x="315" y="229.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="111" y="229.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
</svg>

### Virran suunta ja elektronien liike
Virran suunnaksi on sovittu suunta, johon positiivinen varaus liikkuisi: ulkoisessa piirissä jännitelähteen plusnavasta miinusnapaan. Metallijohtimessa liikkuvat kuitenkin negatiiviset elektronit, ja ne kulkevat päinvastaiseen suuntaan, miinusnavasta plusnapaan. Sovittu suunta on peräisin ajalta ennen elektronin löytämistä, ja sitä käytetään edelleen kaikissa kytkentäkaavioissa. Elektronit etenevät johdossa hitaasti, tyypillisesti alle millimetrin sekunnissa. Kun kytkin suljetaan, sähkömagneettinen häiriö etenee virtapiirissä hyvin nopeasti mutta rajallisella nopeudella. Johtimissa on valmiiksi vapaita elektroneja, myös lampun hehkulangassa, joten niiden ei tarvitse kulkea paristolta lampulle asti ennen lampun syttymistä. Tavallisessa lyhyessä virtapiirissä etenemisviive on niin pieni, että lamppu näyttää syttyvän heti.

<svg data-fig="johdin" viewBox="0 0 600 330" role="img" aria-label="Johdon pala suurennettuna. Uloinna on muovinen eristekuori, jonka sisällä on kuparijohdin. Kuparissa on säännöllisessä hilassa positiivisia metalli-ioneja ja niiden välissä vapaita elektroneja. Sininen nuoli osoittaa vasemmalle: vapaat elektronit liikkuvat vasemmalle. Violetti nuoli osoittaa oikealle: sovittu virran suunta on elektronien liikkeelle vastakkainen. Kaavakuva, ei mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-1-johdin.webp" x="0" y="0" width="600" height="340" preserveAspectRatio="none"/>
  <foreignObject x="193" y="275.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\text{elektronit}$</div></foreignObject>
  <foreignObject x="482" y="31.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="40" y="31.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{eriste}$</div></foreignObject>
  <foreignObject x="40" y="275.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{kupari}$</div></foreignObject>
</svg>

### Kytkentäkaavio
Virtapiiri piirretään **kytkentäkaaviona**, jossa jokaisella komponentilla on oma piirrosmerkkinsä. Paristossa pitkä ohut viiva on plusnapa ja lyhyt paksu viiva miinusnapa. Lamppu on ympyrä, jonka sisällä on risti, ja vastus on suorakulmio. Mittarit piirretään ympyröinä, joiden sisällä on mittarin kirjain: ampeerimittari $\text{A}$ ja volttimittari $\text{V}$. Johtimet piirretään suorina vaakasuorina ja pystysuorina viivoina. Kahden johtimen liitoskohta merkitään pisteellä.

<svg data-fig="symbolit" viewBox="0 0 600 390" role="img" aria-label="Kytkentäkaavion piirrosmerkit kahdessa sarakkeessa. Vasemmalla ylhäältä alas: paristo, jossa pitkä ohut viiva on plusnapa ja lyhyt paksu viiva miinusnapa; lamppu, ympyrä jonka sisällä on risti; vastus, suorakulmio; ampeerimittari, ympyrä jonka sisällä on A. Oikealla: avoin kytkin, jonka vipu on nostettu irti, suljettu kytkin, jonka vipu on kosketuksissa, johdin, liitoskohta pisteenä ja volttimittari, ympyrä jonka sisällä on V." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-1-symbolit.webp" x="0" y="1.2" width="600" height="398.8" preserveAspectRatio="none"/>
  <foreignObject x="31" y="15.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="71" y="15.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="120" y="47.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{paristo}$</div></foreignObject>
  <foreignObject x="120" y="125.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lamppu}$</div></foreignObject>
  <foreignObject x="120" y="203.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vastus}$</div></foreignObject>
  <foreignObject x="49" y="281.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <foreignObject x="120" y="281.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ampeerimittari}$</div></foreignObject>
  <foreignObject x="416" y="47.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{avoin kytkin}$</div></foreignObject>
  <foreignObject x="416" y="125.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{suljettu kytkin}$</div></foreignObject>
  <foreignObject x="416" y="203.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{johdin}$</div></foreignObject>
  <foreignObject x="416" y="281.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{liitoskohta}$</div></foreignObject>
  <foreignObject x="347" y="329.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="416" y="329.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{volttimittari}$</div></foreignObject>
</svg>

Kaavio näyttää, mitkä komponentit on kytketty toisiinsa, ei sitä, miltä laitteet näyttävät tai kuinka pitkiä johdot ovat. Samasta virtapiiristä voi siksi piirtää monta oikean näköistä kaaviota. Tärkeää on, että virta kulkee kaaviossa samojen komponenttien kautta samassa järjestyksessä kuin todellisessa piirissä. Virran suunta merkitään johtimen viereen nuolella plusnavasta miinusnapaan.

<svg data-fig="kaavio" viewBox="0 0 600 320" role="img" aria-label="Kuvan 2 virtapiiri kytkentäkaaviona. Suorakulmion muotoinen silmukka. Alareunassa vasemmalla kaksi paristokennoa peräkkäin, pitkä viiva eli plusnapa oikealla. Alareunassa oikealla suljettu kytkin, yläreunan keskellä lamppu, ympyrä jossa on risti. Violetti nuoli oikean reunan vieressä osoittaa ylöspäin ja on merkitty I: virta kulkee plusnavasta kytkimen ja lampun kautta miinusnapaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-1-kaavio.webp" x="10.8" y="9.6" width="576.9" height="319.7" preserveAspectRatio="none"/>
  <foreignObject x="237" y="279.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="163" y="279.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="199" y="279.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="558" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="358.5" y="279.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kytkin}$</div></foreignObject>
  <foreignObject x="253.5" y="15.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lamppu}$</div></foreignObject>
</svg>

## Kaava: Sähkövirta
Sähkövirta kertoo, kuinka suuri varaus kulkee johtimen poikkileikkauksen läpi aikayksikössä:
```kaavat
sähkövirta :: I = \frac{Q}{t}
```
missä $I$ on sähkövirta ($\text{A}$), $Q$ poikkileikkauksen läpi kulkenut varaus ($\text{C}$) ja $t$ aika ($\text{s}$). Varauksen yksikkö on coulombi $\text{C}$ ja virran yksikkö ampeeri $\text{A}$. Virta on $1\,\text{A}$, kun poikkileikkauksen läpi kulkee joka sekunti varaus $1\,\text{C}$, eli $1\,\text{A} = 1\,\text{C/s}$. Kun virta tunnetaan, kulkenut varaus saadaan tulona $Q = It$.

<svg data-fig="virta" viewBox="0 0 600 320" role="img" aria-label="Kuparijohdin suurennettuna. Johdon keskellä on katkoviivalla piirretty poikkileikkaus. Sinisiä elektroneja on koko johdossa, ja ne liikkuvat vasemmalle poikkileikkauksen läpi. Oikealla ylhäällä sekuntikello. Violetti nuoli johdon yläpuolella osoittaa oikealle ja on merkitty I. Merkinnät: ajassa t poikkileikkauksen läpi kulkee varaus Q. Kaavakuva, ei mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-1-virta.webp" x="3.7" y="0" width="594.1" height="325.5" preserveAspectRatio="none"/>
  <foreignObject x="262" y="237.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{elektronit}$</div></foreignObject>
  <foreignObject x="396" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="208.5" y="19.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{poikkileikkaus}$</div></foreignObject>
  <foreignObject x="450" y="47.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="180" y="279.5" width="240" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q\ \text{kulkee ajassa}\ t$</div></foreignObject>
</svg>

```pysahdy
Johtimen läpi kulkeva virta kaksinkertaistuu. Miten tietyssä ajassa poikkileikkauksen läpi kulkeva varaus muuttuu?
---
Varaus kaksinkertaistuu. Kaavan $Q = It$ mukaan se on verrannollinen virtaan, kun aika $t$ pysyy samana.
```

### Varaus ja elektronien määrä
Elektronin varaus on $-e$, missä $e$ on alkeisvaraus, pienin vapaana esiintyvä varaus. Kun $N$ elektronia kulkee poikkileikkauksen läpi, kulkenut varaus on niiden varausten summa:
```latex
Q = N e
```
missä $Q$ on varauksen suuruus ($\text{C}$), $N$ elektronien lukumäärä ja $e = 1{,}602 \cdot 10^{-19}\,\text{C}$ alkeisvaraus. Yhden coulombin varaukseen tarvitaan siis noin $6{,}24 \cdot 10^{18}$ elektronia. Siksi elektroneja ei lasketa yksitellen, vaan virtaa mitataan ampeereina.

### Jännite
Paristo ei anna piiriin varausta, sillä varaus kiertää piirissä ja palaa paristoon. Paristo antaa varaukselle energiaa, ja lamppu muuttaa sen energian valoksi ja hehkulangan sisäenergiaksi, joka siirtyy lämpönä ympäristöön. **Jännite** kertoo, kuinka paljon energiaa siirtyy jokaista varausyksikköä kohti, kun varaus kulkee kahden kohdan välillä:
```latex
U = \frac{E}{Q}
```
missä $U$ on jännite ($\text{V}$), $E$ siirtynyt energia ($\text{J}$) ja $Q$ varaus ($\text{C}$). Jännitteen yksikkö on voltti $\text{V}$, ja $1\,\text{V} = 1\,\text{J/C}$. AA-pariston jännite $1{,}5\,\text{V}$ tarkoittaa, että jokainen paristosta lamppuun kulkeva coulombi tuo lamppuun $1{,}5\,\text{J}$ energiaa, kun johtojen ja pariston oma vastus jätetään huomiotta. Mitä suurempi jännite, sitä enemmän energiaa sama varaus siirtää.

<svg data-fig="jannite" viewBox="0 0 600 350" role="img" aria-label="Paristo vasemmalla ja lamppu oikealla, välissä oranssi energiavirran nuoli paristosta lamppuun. Paristoon on merkitty jännite U yhtä suuri kuin 1,5 volttia, nuoleen energia 1,5 joulea jokaista coulombia kohti. Lamppu säteilee valoa ja lämpöä. Ylhäällä johto kulkee pariston plusnavasta lampun kylkeen, alhaalla johto palaa lampun kannasta pariston pohjaan, ja violetti nuoli näyttää, että sama varaus kiertää takaisin paristoon. Kaavakuva." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-1-jannite.webp" x="17" y="0" width="582.5" height="345.9" preserveAspectRatio="none"/>
  <foreignObject x="12" y="211.5" width="106" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U = 1{,}5\,\text{V}$</div></foreignObject>
  <foreignObject x="155" y="21.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="155" y="181.5" width="22" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="219" y="59.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}5\,\text{J}\ \text{/}\ 1\,\text{C}$</div></foreignObject>
  <foreignObject x="246.5" y="151.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{energia}$</div></foreignObject>
  <foreignObject x="140" y="303.5" width="320" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\text{sama varaus palaa paristolle}$</div></foreignObject>
</svg>

```pysahdy
Kaksi paristoa, $1{,}5\,\text{V}$ ja $3{,}0\,\text{V}$, siirtävät kumpikin saman varauksen lamppuun. Kumpi siirtää enemmän energiaa ja kuinka monta kertaa enemmän?
---
Kaavasta $U = E : Q$ saadaan $E = UQ$. Kun $Q$ on sama, energia on verrannollinen jännitteeseen, joten $3{,}0\,\text{V}$:n paristo siirtää kaksinkertaisen energian.
```

### Tyypillisiä arvoja
Jännitteet ja virrat vaihtelevat arkisissa laitteissa paljon. Taulukon arvot ovat suuruusluokkia.

<figure class="unit-photo"><img src="pics/fy6/macro-circuit-board.webp" alt="Piirilevy läheltä: vihreä kondensaattori, pieni raidallinen vastus ja muita komponentteja, joita johtimet yhdistävät."><figcaption>Elektroniikkalaitteen piirilevy. Komponentit on kytketty toisiinsa levyn johtimilla, ja kondensaattorin kylkeen on merkitty suurin jännite, jonka se kestää: $6{,}3\,\text{V}$.</figcaption></figure>

| Jännitelähde | Jännite |
|---|---|
| AA-paristo | $1{,}5\,\text{V}$ |
| puhelimen akku | $3{,}7\,\text{V}$ |
| auton akku | $12\,\text{V}$ |

| Laite | Virta |
|---|---|
| merkkivalon LED | $0{,}02\,\text{A}$ |
| taskulampun lamppu | $0{,}3\,\text{A}$ |
| puhelimen laturi | $2\,\text{A}$ |

## Esimerkki
Taskulampun lampun läpi kulkee $0{,}25\,\text{A}$:n virta, ja lamppu palaa $12\,\text{min}$. Kuinka suuri varaus kulkee tänä aikana lampun läpi?

<!-- vaihe -->

**Tunnetut ja kysytty.** Virta $I = 0{,}25\,\text{A}$ ja aika $t = 12\,\text{min}$.

Kysytään lampun läpi kulkenutta varausta $Q$.

<!-- vaihe -->

**Periaate.** Virta kertoo, kuinka suuri varaus kulkee lampun läpi sekunnissa. Virta pysyy samana koko ajan, joten varaus saadaan virran määritelmästä $I = \tfrac{Q}{t}$.

<!-- vaihe -->

**Kaava ratkaistuna.** Ratkaistaan varaus kertomalla yhtälön molemmat puolet ajalla:
```latex
\begin{aligned}
&I = \frac{Q}{t} \\
&Q = I t
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ampeeri on coulombi sekunnissa, joten aika muutetaan sekunneiksi: $12\,\text{min} = 12 \cdot 60\,\text{s} = 720\,\text{s}$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen, ja $1\,\text{A}\cdot\text{s} = 1\,\text{C}$:
```latex
\begin{aligned}
Q &= I t \\
&= 0{,}25\,\text{A}\cdot 720\,\text{s} \\
&= 180\,\text{C}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Lampun läpi kulkee varaus $Q = 180\,\text{C}$, kahden merkitsevän numeron tarkkuudella $1{,}8 \cdot 10^{2}\,\text{C}$ kuten lähtötiedoissa $0{,}25\,\text{A}$ ja $12\,\text{min}$.

<!-- vaihe -->

**Järkevyys.** Joka sekunti lampun läpi kulkee neljäsosa coulombia, ja $720\,\text{s}$:ssa neljäsosa luvusta $720$ on $180$. Elektroneina varaus on $$180\,\text{C} : (1{,}602 \cdot 10^{-19}\,\text{C}) \approx 1{,}1 \cdot 10^{21}$$ elektronia, valtava määrä, mutta johdossa niitä on vielä paljon enemmän.

## Yleinen virhekäsitys
Moni ajattelee, että lamppu kuluttaa sähkövirtaa, joten lampun jälkeen johdossa kulkisi vähemmän virtaa kuin ennen lamppua. Näin ei ole: sama varaus, joka tulee lamppuun, lähtee siitä ja palaa paristoon, joten virta on yhtä suuri lampun molemmin puolin. Lamppu muuttaa varauksen kuljettamaa sähköistä energiaa valoksi ja hehkulangan sisäenergiaksi. Toinen virhekäsitys on, että elektronit lähtevät paristosta ja kulkevat lamppuun asti ennen kuin lamppu syttyy. Johto on kuitenkin valmiiksi täynnä vapaita elektroneja, ja ne alkavat liikkua kaikkialla piirissä yhtä aikaa.

## Tiivistelmä
- Sähkövirta on varauksen liikettä. Metallijohtimessa liikkuvat vapaat elektronit; eristeessä varaukset eivät pääse liikkumaan.
- Virta kulkee vain suljetussa virtapiirissä. Sama virta kulkee lampun läpi ja palaa paristoon: virta ei kulu. Paristosta kuluu energiaa, ei varausta.
- Sähkövirta on $I = \tfrac{Q}{t}$, yksikkö ampeeri, $1\,\text{A} = 1\,\text{C/s}$. Varaus on $Q = Ne$, missä $e = 1{,}602 \cdot 10^{-19}\,\text{C}$.
- Jännite on siirtynyt energia varausyksikköä kohti, $U = \tfrac{E}{Q}$, yksikkö voltti, $1\,\text{V} = 1\,\text{J/C}$.
- Sovittu virran suunta on ulkoisessa piirissä plusnavasta miinusnapaan; elektronit liikkuvat vastakkaiseen suuntaan.
- Kytkentäkaaviossa komponentit piirretään piirrosmerkeillä ja johtimet suorina viivoina. Kytkin piirretään avoimena (vipu irti) tai suljettuna (vipu kosketuksissa).
