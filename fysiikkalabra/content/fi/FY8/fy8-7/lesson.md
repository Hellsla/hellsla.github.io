# Laser ja kvanttirakenteet

> **Miksi** laserosoittimen valo kulkee pimeän luokan poikki kapeana säteenä ja näkyy seinällä pienenä pisteenä, kun taskulampun valo leviää laajaksi himmeäksi läiskäksi?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: hämärässä luokassa pöydällä on laserosoitin ja taskulamppu, jotka osoittavat samaan valkoiseen varjostimeen. Laserosoittimesta lähtee ohut punainen säde, joka osuu varjostimeen pienenä kirkkaana pisteenä. Taskulampun valo leviää laajaksi kartioksi ja valaisee varjostimesta suuren, himmeän ja kellertävän alueen." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-7-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Atomi ja fotoni: kolme tapahtumaa
Luvussa *Vetyatomin energiatasot ja Bohrin malli* atomi absorboi fotonin, jonka energia on kahden tason erotus, tai lähettää sellaisen pudotessaan alemmalle tasolle. Viritetty atomi lähettää fotonin yleensä itsestään, satunnaisella hetkellä ja satunnaiseen suuntaan. Tämä on **spontaani emissio**. Lampun ja LEDin valo syntyy näin, joten eri atomien fotonit lähtevät eri suuntiin ja eri tahdissa.

Albert Einstein päätteli vuonna 1917, että on olemassa myös kolmas tapahtuma. Kun viritettyyn atomiin osuu fotoni, jonka energia on täsmälleen tasojen erotus $E_2 - E_1$, se voi saada atomin putoamaan alemmalle tasolle heti. Tämä on **stimuloitu emissio**. Saapuva fotoni ei absorboidu, vaan sen rinnalle syntyy toinen fotoni, jolla on sama energia eli sama aallonpituus, sama kulkusuunta ja sama vaihe. Yhdestä fotonista tulee kaksi samanlaista, kahdesta neljä ja niin edelleen. Tähän valon vahvistumiseen laser perustuu: sana tulee englannin sanoista *light amplification by stimulated emission of radiation*.

<svg data-fig="processes" viewBox="0 0 600 380" role="img" aria-label="Kolme tapahtumaa vierekkäin, kaavakuva, ei mittakaavassa. Kussakin on atomin kaksi energiatasoa, alempi E1 ja ylempi E2, ja sininen piste on elektroni; rengas näyttää, missä se oli ennen tapahtumaa. Vasemmalla absorptio: fotoni, jonka energia hf on tasojen erotus, tulee atomiin ja nostaa elektronin tasolle E2, ja fotoni katoaa. Keskellä spontaani emissio: elektroni putoaa itsestään tasolta E2 tasolle E1, ja fotoni lähtee satunnaiseen suuntaan, tässä vinosti ylös. Oikealla stimuloitu emissio: saapuva fotoni saa viritetyn atomin elektronin putoamaan, ja atomista lähtee kaksi samanlaista fotonia samaan suuntaan samassa tahdissa." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-7-processes.webp" x="0" y="0" width="600" height="390" preserveAspectRatio="none"/>
  <foreignObject x="7" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_2$</div></foreignObject>
  <foreignObject x="7" y="221.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_1$</div></foreignObject>
  <foreignObject x="78" y="303.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{absorptio}$</div></foreignObject>
  <foreignObject x="260" y="287.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{spontaani}$</div></foreignObject>
  <foreignObject x="272.5" y="321.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{emissio}$</div></foreignObject>
  <foreignObject x="435.5" y="287.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{stimuloitu}$</div></foreignObject>
  <foreignObject x="454.5" y="321.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{emissio}$</div></foreignObject>
  <foreignObject x="77.5" y="109.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$hf$</div></foreignObject>
  <foreignObject x="353.5" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$hf$</div></foreignObject>
  <foreignObject x="431.5" y="111.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$hf$</div></foreignObject>
  <foreignObject x="535.5" y="95.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$hf$</div></foreignObject>
</svg>

```pysahdy
Valopulssissa on $1000$ fotonia, joiden aallonpituus on $650\,\text{nm}$. Pulssi kulkee aineen läpi, jossa on runsaasti virittyneitä atomeja, ja jokainen fotoni aiheuttaa yhden stimuloidun emission. Kuinka monta fotonia tulee ulos ja kuinka paljon energiaa aine on antanut valolle yhteensä? Käytä $hc = 1240\,\text{eV}\,\text{nm}$.
---
Jokaista saapuvaa fotonia kohti syntyy yksi uusi, joten ulos tulee $2000$ fotonia. Uusia fotoneja on $1000$, ja kunkin energia on $hf = \tfrac{hc}{\lambda} = \tfrac{1240\,\text{eV}\,\text{nm}}{650\,\text{nm}} = 1{,}91\,\text{eV}$. Aine antaa valolle energiaa $1000 \cdot 1{,}91\,\text{eV} \approx 1{,}9\,\text{keV}$.
```

### Populaatioinversio
Fotoni, joka saa viritetyn atomin emittoimaan, voi perustilassa olevaan atomiin osuessaan absorboitua. Kumpi tapahtuu useammin, riippuu siitä, kummalla tasolla atomeja on enemmän. Tavallisesti lähes kaikki atomit ovat perustilassa, joten fotoni absorboituu paljon todennäköisemmin kuin monistuu, ja valo heikkenee aineessa. Valo vahvistuu vain, jos ylemmällä tasolla on enemmän atomeja kuin alemmalla, $N_2 > N_1$. Tätä tilaa kutsutaan **populaatioinversioksi**. Lämmittäminen ei tuota sitä: lämpimässäkin aineessa alemmalla tasolla on aina enemmän atomeja kuin ylemmällä.

Inversio tehdään **pumppaamalla** eli tuomalla atomeihin energiaa valolla, sähköpurkauksella tai sähkövirralla. Yksinkertaisessa kahden erillisen energiatason mallissa inversiota ei saada aikaan pumppaamalla samalla resonanssivalolla, koska pumppausvalon fotonit aiheuttavat ylätilan atomeissa stimuloitua emissiota yhtä todennäköisesti kuin ne virittävät perustilan atomeja: ylätilaan saadaan enintään puolet atomeista. Siksi monissa atomi- ja ionilasereissa hyödynnetään kolmen tai neljän energiatason rakennetta. Puolijohdelasereissa valon vahvistuminen perustuu sen sijaan puolijohteen energiavöihin ja sähkövirralla synnytettyyn inversioon. Rubiinissa pumppauslampun vihreä valo nostaa atomeja lyhytikäiselle tasolle $E_3$, josta ne siirtyvät nopeasti ja ilman valoa tasolle $E_2$. Taso $E_2$ on pitkäikäinen: atomi pysyy siinä keskimäärin muutaman millisekunnin, satojatuhansia kertoja kauemmin kuin tavallisessa viritystilassa ($10^{-8}\,\text{s}$). Siksi tasolle $E_2$ ehtii kertyä enemmän atomeja kuin perustilaan jää.

<svg data-fig="inversion" viewBox="0 0 600 360" role="img" aria-label="Kolmitasoisen laseraineen, kuten rubiinin, energiatasot, kaavakuva, ei mittakaavassa. Alimpana perustila E1, ylimpänä lyhytikäinen taso E3 ja niiden välissä pitkäikäinen taso E2. Vihreä nuoli: pumppaus nostaa atomeja tasolta E1 tasolle E3. Harmaa katkoviivanuoli: atomit siirtyvät tasolta E3 nopeasti ja ilman valoa tasolle E2. Punainen nuoli: lasersiirtymä tasolta E2 tasolle E1, aallonpituus 694 nm. Siniset pisteet ovat atomeja: tasolla E2 on seitsemän ja tasolla E1 neljä, eli ylemmällä tasolla on enemmän atomeja kuin alemmalla. Tätä kutsutaan populaatioinversioksi." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-7-inversion.webp" x="2.5" y="0" width="597" height="365.7" preserveAspectRatio="none"/>
  <foreignObject x="77" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_3$</div></foreignObject>
  <foreignObject x="77" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_2$</div></foreignObject>
  <foreignObject x="77" y="285.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E_1$</div></foreignObject>
  <foreignObject x="330" y="90.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{nopea, ilman valoa}$</div></foreignObject>
  <foreignObject x="330" y="190.5" width="149" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{laser}\ 694\,\text{nm}$</div></foreignObject>
  <foreignObject x="330" y="247.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{pumppaus}$</div></foreignObject>
  <foreignObject x="181" y="321.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N_2 > N_1$</div></foreignObject>
</svg>

### Peilit tekevät valosta säteen
Laseraine on kahden peilin välissä. Toinen peili heijastaa kaiken valon, toinen esimerkiksi $99\,\%$ ja päästää loput läpi. Peilien välillä akselin suuntaisesti kulkeva fotoni kulkee aineen läpi satoja kertoja ja synnyttää matkallaan stimuloituja kopioita itsestään. Sivulle lähtevät fotonit poistuvat aineesta eivätkä ehdi monistua. Siksi vahvistuu vain akselin suuntainen valo, ja osittain läpäisevän peilin läpi tulee ulos säde. Laser alkaa toimia vasta, kun pumppaus on niin voimakas, että vahvistuminen korvaa peilin läpi ja muualle menetetyn valon. Tätä pumppauksen raja-arvoa kutsutaan **kynnykseksi**.

Laservalo on siksi lähes yksiväristä, koska fotonit syntyvät samassa siirtymässä. Se on suuntautunutta, koska vain akselin suuntainen valo vahvistuu, ja säde levenee vain vähän. Lisäksi se on koherenttia: aallot ovat samassa tahdissa, koska jokainen stimuloitu fotoni kopioi saapuvan fotonin vaiheen. Taskulampun valossa on monia aallonpituuksia, ja se lähtee eri suuntiin ja eri tahdissa. Myös laserdiodissa on vahvistava aine ja peilit: sähkövirta synnyttää inversion puolijohteessa, ja kiteen lohkaistut päät toimivat peileinä. Sen energiatasot ovat kuitenkin energiavöitä eivätkä yksittäisen atomin tasoja.

<svg data-fig="cavity" viewBox="0 0 600 300" role="img" aria-label="Laserin rakenne, kaavakuva, ei mittakaavassa. Keskellä vaakasuora sauva aktiivista ainetta. Sen vasemmassa päässä on peili, joka heijastaa kaiken valon, ja oikeassa päässä peili, joka heijastaa 99 prosenttia ja päästää läpi 1 prosentin. Sauvan alla on pumppauslamppu, jonka valo nostaa atomeja viritystilaan. Sauvan sisällä punaiset fotonit kulkevat akselin suuntaisesti edestakaisin peilien välillä ja monistuvat. Kaksi fotonia lähtee vinosti sivulle ja poistuu sauvasta. Oikean peilin läpi tulee ulos kapea punainen lasersäde." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-7-cavity.webp" x="30.7" y="23.6" width="566" height="293.6" preserveAspectRatio="none"/>
  <foreignObject x="47.5" y="49.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{peili}\ 100\,\%$</div></foreignObject>
  <foreignObject x="422" y="49.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{peili}\ 99\,\%$</div></foreignObject>
  <foreignObject x="208.5" y="73.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{aktiivinen aine}$</div></foreignObject>
  <foreignObject x="468" y="171.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\text{lasersäde}$</div></foreignObject>
  <foreignObject x="246" y="255.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\text{pumppaus}$</div></foreignObject>
</svg>

### Kvanttirakenteet: koko määrää energiatasot
Puolijohteen **energia-aukko** on pienin energia, jonka sen elektroni voi saada valosta tai luovuttaa valoksi, ja se määrää LEDin valon värin (luku *LEDin valo ja Planckin vakion mittaaminen*). Isossa kiteessä energia-aukko riippuu vain aineesta. Luvussa *Aaltomekaaninen atomimalli ja orbitaalit* elektronin tiloja verrattiin kielen seisoviin aaltoihin: lyhyemmän kielen sallitut värähtelyt ovat korkeampia ja kauempana toisistaan. Samoin käy, kun elektronit suljetaan rakenteeseen, jonka koko on vain muutamia nanometrejä. Sallitut energiat erkanevat toisistaan, ja energia-aukko kasvaa rakenteen pienentyessä. Tällaisia puolijohteen rakenteita kutsutaan **kvanttirakenteiksi**. Ohut kerros on kvanttikaivo, ja joka suunnasta rajattu nanokide on **kvanttipiste**.

Puolijohdekvanttipisteen väri voidaan siis valita sen koolla, vaikka aine on sama. Kadmiumselenidistä tehty kvanttipiste, jonka halkaisija on $2\,\text{nm}$, lähettää syaania valoa ja halkaisijaltaan $6\,\text{nm}$:n piste punaista. Ison kadmiumselenidikiteen energia-aukko on $1{,}74\,\text{eV}$, mikä vastaa tummanpunaista valoa näkyvän alueen reunalla, noin $713\,\text{nm}$. Pisteen pienentäminen siirtää valon siis kohti lyhyempiä aallonpituuksia. Tässä luvussa riittää tämä laadullinen yhteys. Energiatasojen tarkka laskeminen pisteen koosta vaatii kvanttimekaanista mallinnusta, ja tehtävät, joissa koon ja aallonpituuden yhteyttä mallinnetaan laskemalla, ovat lisätietoa. Kvanttipisteiden löytämisestä ja valmistamisesta myönnettiin kemian Nobel-palkinto vuonna 2023.

<svg data-fig="qdots" viewBox="0 0 600 370" role="img" aria-label="Viisi kvanttipistettä allekkain, halkaisijat keskenään mittakaavassa, kukin piirretty lähettämänsä valon värisenä. Halkaisija 2,0 nm: aallonpituus 480 nm, fotonin energia 2,58 eV, syaani. 3,0 nm: 530 nm, 2,34 eV, vihreä. 4,0 nm: 570 nm, 2,18 eV, kellanvihreä. 5,0 nm: 600 nm, 2,07 eV, oranssi. 6,0 nm: 620 nm, 2,00 eV, punainen. Mitä pienempi piste, sitä lyhyempi aallonpituus ja sitä suurempi fotonin energia." style="max-width:100%;font-size:24px">
  <circle cx="78" cy="46" r="11" fill="#1098ad" stroke="#1f2933" stroke-width="2"/>
  <circle cx="75" cy="43" r="2.2" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="31.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 2{,}0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="31.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1098ad">$\lambda = 480\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="31.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2{,}58\,\text{eV}$</div></foreignObject>
  <circle cx="78" cy="114" r="16.5" fill="#2b8a3e" stroke="#1f2933" stroke-width="2"/>
  <circle cx="73" cy="109" r="3.3" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="99.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 3{,}0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="99.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\lambda = 530\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="99.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2{,}34\,\text{eV}$</div></foreignObject>
  <circle cx="78" cy="182" r="22" fill="#a8a21f" stroke="#1f2933" stroke-width="2"/>
  <circle cx="71.5" cy="175.5" r="4.4" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="167.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 4{,}0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="167.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda = 570\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="167.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2{,}18\,\text{eV}$</div></foreignObject>
  <circle cx="78" cy="250" r="27.5" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <circle cx="70" cy="242" r="5.5" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="235.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 5{,}0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="235.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\lambda = 600\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="235.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2{,}07\,\text{eV}$</div></foreignObject>
  <circle cx="78" cy="318" r="33" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <circle cx="68.5" cy="308.5" r="6.6" fill="#ffffff" fill-opacity="0.45"/>
  <foreignObject x="150" y="303.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$d = 6{,}0\,\text{nm}$</div></foreignObject>
  <foreignObject x="316" y="303.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\lambda = 620\,\text{nm}$</div></foreignObject>
  <foreignObject x="455" y="303.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$hf = 2{,}00\,\text{eV}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy8/helium-neon-laser.webp" alt="Musta laatikkomainen laite, jonka kyljessä lukee He-Ne LASER, on pöydällä telineessä; sen päässä loistaa punainen valo, ja edessä on pidike."><figcaption>Helium-neonlaser optiikan koeasetelmassa. Sähköpurkaus pumppaa putken kaasun, ja putken päiden peilit vahvistavat valon kapeaksi punaiseksi säteeksi, jonka aallonpituus on $633\,\text{nm}$.</figcaption></figure>

```pysahdy
Kadmiumselenidistä tehty kvanttipiste lähettää sinistä valoa aallonpituudella $450\,\text{nm}$. Käytä $hc = 1240\,\text{eV}\,\text{nm}$. Laske fotonin energia ja päättele, onko piste halkaisijaltaan suurempi vai pienempi kuin $2{,}0\,\text{nm}$:n piste. Kuinka paljon pisteen energia-aukko ylittää ison kiteen energia-aukon $1{,}74\,\text{eV}$?
---
Fotonin energia on $\tfrac{hc}{\lambda} = \tfrac{1240\,\text{eV}\,\text{nm}}{450\,\text{nm}} \approx 2{,}76\,\text{eV}$, ja energia-aukko on likimain tämän suuruinen. Se on suurempi kuin $2{,}0\,\text{nm}$:n pisteen aukko ($480\,\text{nm}$ vastaa $2{,}58\,\text{eV}$), joten piste on pienempi kuin $2{,}0\,\text{nm}$. Ylitys on $2{,}76\,\text{eV} - 1{,}74\,\text{eV} \approx 1{,}0\,\text{eV}$.
```

### Kvanttirakenteiden sovelluksia
Kvanttipistenäytössä sininen taustavalo osuu kvanttipisteisiin, jotka absorboivat sen ja lähettävät puhdasta vihreää tai punaista valoa samaan tapaan kuin fluoresenssissa luvussa *Spektrit paljastavat atomin energiatasot*. Useimmat laserdiodit ovat kvanttikaivolasereita, joissa kaivon paksuus valitsee aallonpituuden. Aurinkokennoihin tutkitaan kvanttipistekerroksia, jotka voidaan pisteiden koon avulla säätää absorboimaan haluttu osa Auringon spektristä.

Kvanttitietokoneen perusyksikkö on **kubitti**: kvanttijärjestelmä, jolla on kaksi tilaa ja joka voi olla myös niiden yhdistelmässä eli superpositiossa. Kubitteja tehdään esimerkiksi puolijohteen kvanttipisteisiin suljetuista elektroneista ja suprajohtavista piireistä. Tällainen piiri käyttäytyy kuin keinotekoinen atomi, jolla on omat kvantittuneet energiatasonsa. Suomessa suprajohtavia kvanttitietokoneita rakentavat VTT ja IQM. Kubitin tilat ovat herkkiä, joten piirit jäähdytetään lähelle absoluuttista nollapistettä ja suojataan ympäristön häiriöiltä.

<figure class="unit-photo"><img src="pics/fy8/rgb-laser-pointer.webp" alt="Kolme vaakasuoraa lasersädettä pimeässä: ylimpänä punainen, keskellä vihreä ja alimpana sininen; säteet lähtevät oikealla olevista laitteista."><figcaption>Punainen, vihreä ja sininen lasersäde. Ilmassa olevat hiukkaset sirottavat osan valosta kameraan, joten säteet näkyvät. Sinisen valon fotoni kantaa eniten energiaa ja punaisen vähiten.</figcaption></figure>

## Kaava: Laserin fotonit
Kaikki laserin fotonit syntyvät samassa siirtymässä, joten jokaisen fotonin energia ja aallonpituus ovat
```latex
\begin{aligned}
hf &= E_2 - E_1 \\
\lambda &= \frac{hc}{E_2 - E_1}
\end{aligned}
```
missä $E_2$ on ylemmän ja $E_1$ alemman lasertason energia, $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ Planckin vakio, $f$ valon taajuus, $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$ valon nopeus ja $\lambda$ aallonpituus.

Koska fotonit ovat samanlaisia, laserin teho on sekunnissa lähtevien fotonien määrä kerrottuna yhden fotonin energialla:
```latex
P = \frac{N}{t} \cdot hf
```
missä $P$ on laserin teho ja $N$ aikana $t$ lähtevien fotonien määrä. Fotonien määrä sekunnissa on siis $\tfrac{N}{t} = \tfrac{P}{hf}$. Energiat lasketaan usein elektronivoltteina ja muunnetaan jouleiksi sijoittamalla $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$.

Samalla teholla pidemmän aallonpituuden laser lähettää enemmän fotoneja, koska yksi fotoni kantaa vähemmän energiaa. Kuvaajassa $1{,}0\,\text{mW}$:n punainen laserosoitin lähettää noin $3{,}3 \cdot 10^{15}$ fotonia sekunnissa ja yhtä tehokas violetti noin $2{,}0 \cdot 10^{15}$.

<svg data-fig="rate-graph" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa: tehon 1,0 milliwattia laserin lähettämien fotonien määrä sekunnissa aallonpituuden funktiona. Vaaka-akselilla aallonpituus nollasta 700 nanometriin, pystyakselilla fotonien määrä sekunnissa yksikkönä 10 potenssiin 15 fotonia sekunnissa, nollasta 3,5:een. Kuvaaja on origon kautta kulkeva suora. Siihen on merkitty kolme laserosoitinta: violetti 405 nm, 2,04; vihreä 532 nm, 2,68; ja punainen 650 nm, 3,27. Pidemmän aallonpituuden laser lähettää samalla teholla enemmän fotoneja, koska yksi fotoni kantaa vähemmän energiaa." style="max-width:100%;font-size:24px">
  <line x1="151.5" y1="290" x2="151.5" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="207.5" y1="290" x2="207.5" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="263" y1="290" x2="263" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="319" y1="290" x2="319" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="374.5" y1="290" x2="374.5" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430.5" y1="290" x2="430.5" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="486" y1="290" x2="486" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="259" x2="486" y2="259" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="228.5" x2="486" y2="228.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="197.5" x2="486" y2="197.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="166.5" x2="486" y2="166.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="135.5" x2="486" y2="135.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="105" x2="486" y2="105" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="74" x2="486" y2="74" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="500" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M512,290 L499,296 L499,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="60" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,48 L102,61 L90,61 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="151.5" y1="290" x2="151.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="129" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="207.5" y1="290" x2="207.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="185" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="263" y1="290" x2="263" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="240.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="319" y1="290" x2="319" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="296.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="374.5" y1="290" x2="374.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="352" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="430.5" y1="290" x2="430.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="408" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="486" y1="290" x2="486" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="463.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$700$</div></foreignObject>
  <line x1="89" y1="259" x2="96" y2="259" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="244.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}5$</div></foreignObject>
  <line x1="89" y1="228.5" x2="96" y2="228.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="214" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="197.5" x2="96" y2="197.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="183" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}5$</div></foreignObject>
  <line x1="89" y1="166.5" x2="96" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="152" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="135.5" x2="96" y2="135.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="121" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2{,}5$</div></foreignObject>
  <line x1="89" y1="105" x2="96" y2="105" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="90.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="74" x2="96" y2="74" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="59.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3{,}5$</div></foreignObject>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="518" y="275.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\lambda\ (\text{nm})$</div></foreignObject>
  <foreignObject x="86" y="17.5" width="174" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N/t\ (10^{15}\,\text{1/s})$</div></foreignObject>
  <polyline points="96,290 486,72.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="321.5" cy="164" r="7" fill="#7048e8" stroke="#ffffff" stroke-width="2"/>
  <circle cx="392.5" cy="124.5" r="7" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <circle cx="458" cy="88" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="224.5" y="123.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$405\,\text{nm}$</div></foreignObject>
  <foreignObject x="295.5" y="84" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$532\,\text{nm}$</div></foreignObject>
  <foreignObject x="361" y="47.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$650\,\text{nm}$</div></foreignObject>
  <foreignObject x="362" y="235.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P = 1{,}0\,\text{mW}$</div></foreignObject>
</svg>

```pysahdy
Laserin teho pidetään samana, mutta fotonin energia kaksinkertaistuu. Mitä tapahtuu sekunnissa lähtevien fotonien määrälle?
---
Koska $\tfrac{N}{t} = \tfrac{P}{hf}$, fotonien määrä sekunnissa puolittuu.
```

## Esimerkki
Helium–neonlaserin lasersiirtymän tasojen energiaero on $1{,}96\,\text{eV}$, ja laserin teho on $1{,}0\,\text{mW}$. Kuinka monta fotonia laser lähettää sekunnissa?

<!-- vaihe -->

**Tunnetut ja kysytty.** Tasojen energiaero $E_2 - E_1 = 1{,}96\,\text{eV}$ ja teho $P = 1{,}0\,\text{mW}$.

Kysytään sekunnissa lähtevien fotonien määrää $\tfrac{N}{t}$.

<!-- vaihe -->

**Periaate.** Kaikki laserin fotonit syntyvät samassa siirtymässä, joten jokaisen energia on $hf = E_2 - E_1$. Teho on fotonien määrä sekunnissa kerrottuna yhden fotonin energialla.

<!-- vaihe -->

**Kaava ratkaistuna.** Sijoitetaan fotonin energiaksi tasojen erotus ja ratkaistaan fotonien määrä sekunnissa:
```latex
\begin{aligned}
&P = \frac{N}{t} \cdot (E_2 - E_1) \\
&\frac{N}{t} = \frac{P}{E_2 - E_1}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Teho on $P = 1{,}0\,\text{mW} = 1{,}0 \cdot 10^{-3}\,\text{W}$, ja energiaero muunnetaan jouleiksi sijoittamalla $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$: $E_2 - E_1 = 1{,}96 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 3{,}1399 \cdot 10^{-19}\,\text{J}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&\frac{N}{t} = \frac{P}{E_2 - E_1} \\
&= \frac{1{,}0 \cdot 10^{-3}\,\text{W}}{3{,}1399 \cdot 10^{-19}\,\text{J}} \\
&= 3{,}1848 \cdot 10^{15}\,\tfrac{1}{\text{s}}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Laser lähettää noin $3{,}2 \cdot 10^{15}$ fotonia sekunnissa. Tulos ilmoitetaan kahdella merkitsevällä numerolla, koska teho $1{,}0\,\text{mW}$ on annettu kahdella.

<!-- vaihe -->

**Järkevyys.** Yksikkö on oikein, koska $\tfrac{\text{W}}{\text{J}} = \tfrac{\text{J/s}}{\text{J}} = \tfrac{1}{\text{s}}$. Energiaeroa vastaa aallonpituus $\lambda = \tfrac{hc}{E_2 - E_1} \approx 633\,\text{nm}$, helium–neonlaserin tuttu punainen valo. Kuvaajan mukaan $1{,}0\,\text{mW}$:n laser lähettää aallonpituudella $650\,\text{nm}$ noin $3{,}3 \cdot 10^{15}$ fotonia sekunnissa, joten hieman lyhyemmällä aallonpituudella hieman pienempi määrä on uskottava.

## Yleinen virhekäsitys
Moni luulee, että laservalo on vaarallista, koska sen fotonit olisivat erityisen energisiä. Fotonin energia riippuu kuitenkin vain aallonpituudesta: punaisen laserosoittimen fotonin energia $1{,}91\,\text{eV}$ on sama kuin minkä tahansa $650\,\text{nm}$:n valon, ja violetin $405\,\text{nm}$:n valon fotonit ovat energisempiä, tulivat ne laserista tai lampusta. Laserin vaara on siinä, että koko teho kulkee kapeassa säteessä, jonka silmän linssi kohdistaa verkkokalvolle hyvin pieneksi pisteeksi. Siksi koulussa käytetään vain pienitehoisia lasereita, eikä säteeseen tai sen peiliheijastukseen katsota eikä sitä suunnata ihmisiin.

Toinen virhe on ajatella, että stimuloidussa emissiossa atomi absorboi fotonin ja lähettää kaksi. Saapuva fotoni ei absorboidu, vaan jatkaa matkaansa. Uuden fotonin energian antaa viritetty atomi, joka putoaa tasolta $E_2$ tasolle $E_1$, joten energia säilyy.

## Tunneloituminen
Klassisen fysiikan mukaan pallo, jonka energia ei riitä mäen yli, vierii takaisin. Kvanttifysiikassa elektronin havaitsemisen todennäköisyys ei katkea esteen reunaan, vaan pienenee esteen sisällä nopeasti. Jos este on hyvin ohut, todennäköisyys jää esteen takana pieneksi mutta ei nollaksi: elektroni voi löytyä esteen takaa, vaikka sen energia on pienempi kuin esteen ylittämiseen tarvittava energia. Tätä kutsutaan **tunneloitumiseksi**. Todennäköisyys pienenee erittäin jyrkästi esteen paksuuntuessa ja korkeutensa kasvaessa, joten tunneloituminen on merkittävää vain nanometrien luokkaa olevilla esteillä.

<svg data-fig="tunnel" viewBox="0 0 600 320" role="img" aria-label="Periaatekuva tunneloitumisesta, ei mittakaavassa. Vasemmalta tulee elektroni, jonka energia E, vaakasuora katkoviiva, on pienempi kuin keskellä olevan harmaan esteen korkeus. Sininen alue kuvaa elektronin havaitsemisen todennäköisyyttä: esteen vasemmalla puolella se on suuri, esteen sisällä se pienenee nopeasti, ja esteen oikealla puolella se on pieni mutta ei nolla. Elektroni voi siis löytyä esteen takaa, vaikka sen energia ei riitä esteen yli." style="max-width:100%;font-size:24px">
  <rect x="270" y="90" width="60" height="170" rx="2" fill="#c9c2b2" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="24" y1="260" x2="576" y2="260" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="24" y1="180" x2="576" y2="180" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M30,260 L30,198 L30,198 L34,196 L38,194 L42,192.5 L46,192 L50,192 L54,193 L58,194.5 L62,197 L66,199 L70,201 L74,202.5 L78,203.5 L82,204 L86,203.5 L90,202 L94,200.5 L98,198.5 L102,196 L106,194 L110,193 L114,192 L118,192 L122,193 L126,194.5 L130,196.5 L134,198.5 L138,200.5 L142,202.5 L146,203.5 L150,204 L154,203.5 L158,202.5 L162,200.5 L166,198.5 L170,196.5 L174,194.5 L178,193 L182,192 L186,192 L190,193 L194,194 L198,196 L202,198.5 L206,200.5 L210,202 L214,203.5 L218,204 L222,203.5 L226,202.5 L230,201 L234,199 L238,197 L242,194.5 L246,193 L250,192 L254,192 L258,192.5 L262,194 L266,196 L270,198 L270,198 L271.5,200.5 L273,203.5 L274.5,206 L276,208 L277.5,210.5 L279,212.5 L280.5,215 L282,216.5 L283.5,218.5 L285,220.5 L286.5,222 L288,224 L289.5,225.5 L291,227 L292.5,228.5 L294,230 L295.5,231 L297,232.5 L298.5,233.5 L300,235 L301.5,236 L303,237 L304.5,238 L306,239 L307.5,240 L309,241 L310.5,241.5 L312,242.5 L313.5,243 L315,244 L316.5,244.5 L318,245.5 L319.5,246 L321,246.5 L322.5,247 L324,247.5 L325.5,248.5 L327,249 L328.5,249.5 L330,250 L570,250 L570,260 Z" fill="#d0e6fb" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="271" y="51.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{este}$</div></foreignObject>
  <foreignObject x="36" y="143.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$E$</div></foreignObject>
  <foreignObject x="52.5" y="275.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{tuleva elektroni}$</div></foreignObject>
  <foreignObject x="377" y="275.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{esteen takana}$</div></foreignObject>
  <line x1="380" y1="210" x2="439" y2="210" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M450,210 L438,215.5 L438,204.5 Z" fill="#1971c2" stroke-linejoin="round"/>
</svg>

Tunnelointimikroskoopissa terävä metallikärki viedään noin nanometrin päähän pinnasta. Kärjen ja pinnan välillä tunneloituvien elektronien virta muuttuu voimakkaasti etäisyyden mukaan, joten kärjellä voidaan kuvata yksittäisiä atomeja. Flash-muistin muistisoluun kirjoitetaan bitti siirtämällä elektroneja ohuen eristekerroksen läpi tunneloitumalla. Suprajohtavissa kubiteissa virta kulkee ohuen eristekerroksen läpi tunneloitumalla; vuoden 2025 fysiikan Nobel-palkinto myönnettiin kvanttitunneloitumisen ja energian kvantittumisen havaitsemisesta tällaisissa piireissä. Myös alfahajoaminen, josta kerrotaan luvussa *Atomiydin ja radioaktiivinen hajoaminen*, on tunneloitumista.

## Tiivistelmä
- Viritetty atomi voi lähettää fotonin itsestään (spontaani emissio) tai saapuvan fotonin vaikutuksesta (stimuloitu emissio). Stimuloidussa emissiossa syntyy fotoni, jolla on saapuvan fotonin energia, suunta ja vaihe.
- Valo vahvistuu vain, kun ylemmällä lasertasolla on enemmän atomeja kuin alemmalla, $N_2 > N_1$ (populaatioinversio). Atomi- ja ionilasereissa se saadaan pumppaamalla aineeseen, jossa on kolme tai neljä tasoa ja pitkäikäinen ylempi lasertaso. Puolijohdelaserissa inversio syntyy sähkövirralla energiavöihin.
- Peilien välissä akselin suuntainen valo kulkee aineen läpi monta kertaa ja vahvistuu; laser toimii, kun pumppaus ylittää kynnyksen. Laservalo on lähes yksiväristä, suuntautunutta ja koherenttia.
- Laserin fotonien energia on $hf = E_2 - E_1$, ja teho on $P = \tfrac{N}{t} \cdot hf$.
- Puolijohteen kvanttirakenteissa elektronit on suljettu nanometrien kokoiseen tilaan, ja energia-aukko kasvaa rakenteen pienentyessä: pienempi kvanttipiste lähettää lyhyempää aallonpituutta. Sovelluksia ovat kvanttipistenäytöt, kvanttikaivolaserit, aurinkokennojen tutkimus ja kvanttitietokoneiden kubitit.
