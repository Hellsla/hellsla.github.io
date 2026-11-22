# Laser ja kvanttirakenteet

> **Miksi** laserosoittimen valo kulkee pimeän luokan poikki kapeana säteenä ja näkyy seinällä pienenä pisteenä, mutta taskulampun valo leviää laajaksi himmeäksi läiskäksi?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: hämärässä luokassa pöydällä on laserosoitin ja taskulamppu. Ne osoittavat samaan valkoiseen varjostimeen. Laserosoittimesta lähtee ohut punainen säde. Säde osuu varjostimeen pienenä kirkkaana pisteenä. Taskulampun valo leviää laajaksi kartioksi. Se valaisee varjostimesta suuren, himmeän ja kellertävän alueen." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-7-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Atomi ja fotoni: kolme tapahtumaa
Luvussa *Vetyatomin energiatasot ja Bohrin malli* atomi voi ottaa vastaan eli absorboida fotonin. Fotonin energian pitää olla sama kuin kahden energiatason erotus. Atomi voi myös lähettää tällaisen fotonin, kun se putoaa alemmalle tasolle. Viritetty atomi on atomi, jonka elektroni on ylemmällä tasolla. Viritetty atomi lähettää fotonin yleensä itsestään. Se tapahtuu satunnaisella hetkellä ja satunnaiseen suuntaan. Tämä on **spontaani emissio**. Emissio tarkoittaa valon lähettämistä. Lampun ja LEDin valo syntyy näin. Eri atomien fotonit lähtevät siksi eri suuntiin ja eri tahdissa.

Albert Einstein päätteli vuonna 1917, että on olemassa myös kolmas tapahtuma. Viritettyyn atomiin osuu fotoni. Sen energia on täsmälleen tasojen erotus $E_2 - E_1$. Silloin atomi voi pudota alemmalle tasolle heti. Tämä on **stimuloitu emissio**. Stimuloitu tarkoittaa, että toinen fotoni saa tapahtuman aikaan. Saapuva fotoni ei katoa. Sen viereen syntyy toinen fotoni. Uudella fotonilla on sama energia eli sama aallonpituus, sama kulkusuunta ja sama vaihe. Vaihe tarkoittaa, että aallot ovat samassa tahdissa. Yhdestä fotonista tulee kaksi samanlaista, kahdesta neljä ja niin edelleen. Laser toimii tämän valon vahvistumisen avulla. Sana tulee englannin sanoista *light amplification by stimulated emission of radiation*.

<svg data-fig="processes" viewBox="0 0 600 380" role="img" aria-label="Kolme tapahtumaa vierekkäin, kaavakuva, ei mittakaavassa. Kussakin on atomin kaksi energiatasoa, alempi E1 ja ylempi E2. Sininen piste on elektroni. Rengas näyttää, missä elektroni oli ennen tapahtumaa. Vasemmalla on absorptio. Fotoni, jonka energia hf on tasojen erotus, tulee atomiin ja nostaa elektronin tasolle E2. Fotoni katoaa. Keskellä on spontaani emissio. Elektroni putoaa itsestään tasolta E2 tasolle E1. Fotoni lähtee satunnaiseen suuntaan, tässä vinosti ylös. Oikealla on stimuloitu emissio. Saapuva fotoni saa viritetyn atomin elektronin putoamaan. Atomista lähtee kaksi samanlaista fotonia samaan suuntaan ja samassa tahdissa." style="max-width:100%;font-size:24px">
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
Valopulssissa on $1000$ fotonia, joiden aallonpituus on $650\,\text{nm}$. Pulssi kulkee aineen läpi, jossa on paljon virittyneitä atomeja. Jokainen fotoni aiheuttaa yhden stimuloidun emission. Montako fotonia tulee ulos? Kuinka paljon energiaa aine antaa valolle yhteensä? Käytä $hc = 1240\,\text{eV}\,\text{nm}$.
---
Jokaista saapuvaa fotonia kohti syntyy yksi uusi, joten ulos tulee $2000$ fotonia. Uusia fotoneja on $1000$. Kunkin energia on $hf = \tfrac{hc}{\lambda} = \tfrac{1240\,\text{eV}\,\text{nm}}{650\,\text{nm}} = 1{,}91\,\text{eV}$. Aine antaa valolle energiaa $1000 \cdot 1{,}91\,\text{eV} \approx 1{,}9\,\text{keV}$.
```

### Populaatioinversio
Fotoni, joka saa viritetyn atomin lähettämään valoa, voi myös osua perustilassa olevaan atomiin. Silloin fotoni absorboituu. Kumpi tapahtuu useammin, riippuu siitä, kummalla tasolla atomeja on enemmän. Yleensä melkein kaikki atomit ovat perustilassa. Silloin fotoni absorboituu paljon todennäköisemmin kuin se monistuu, ja valo heikkenee aineessa. Valo vahvistuu vain, jos ylemmällä tasolla on enemmän atomeja kuin alemmalla, $N_2 > N_1$. Tätä tilaa kutsutaan **populaatioinversioksi**. Lämmittäminen ei tuota sitä. Lämpimässäkin aineessa alemmalla tasolla on aina enemmän atomeja kuin ylemmällä.

Inversio tehdään **pumppaamalla**. Pumppaaminen tarkoittaa, että atomeihin tuodaan energiaa valolla, sähköpurkauksella tai sähkövirralla. Ajatellaan yksinkertaista mallia, jossa on vain kaksi erillistä energiatasoa. Siinä inversiota ei saada aikaan pumppaamalla samalla resonanssivalolla. Pumppausvalon fotonit aiheuttavat ylätilan atomeissa stimuloitua emissiota yhtä todennäköisesti kuin ne virittävät perustilan atomeja. Siksi ylätilaan saadaan enintään puolet atomeista. Monissa atomi- ja ionilasereissa käytetään siksi kolmea tai neljää energiatasoa. Puolijohdelaserissa valon vahvistuminen perustuu puolijohteen energiavöihin. Inversio syntyy siinä sähkövirran avulla. Rubiinissa pumppauslampun vihreä valo nostaa atomeja lyhytikäiselle tasolle $E_3$. Sieltä atomit siirtyvät nopeasti ja ilman valoa tasolle $E_2$. Taso $E_2$ on pitkäikäinen. Atomi pysyy siinä keskimäärin muutaman millisekunnin. Se on satojatuhansia kertoja kauemmin kuin tavallisessa viritystilassa ($10^{-8}\,\text{s}$). Siksi tasolle $E_2$ ehtii kertyä enemmän atomeja kuin perustilaan jää.

<svg data-fig="inversion" viewBox="0 0 600 360" role="img" aria-label="Kolmitasoisen laseraineen, esimerkiksi rubiinin, energiatasot, kaavakuva, ei mittakaavassa. Alimpana on perustila E1. Ylimpänä on lyhytikäinen taso E3. Niiden välissä on pitkäikäinen taso E2. Vihreä nuoli: pumppaus nostaa atomeja tasolta E1 tasolle E3. Harmaa katkoviivanuoli: atomit siirtyvät tasolta E3 nopeasti ja ilman valoa tasolle E2. Punainen nuoli: lasersiirtymä tasolta E2 tasolle E1, aallonpituus 694 nm. Siniset pisteet ovat atomeja. Tasolla E2 on seitsemän atomia ja tasolla E1 neljä. Ylemmällä tasolla on siis enemmän atomeja kuin alemmalla. Tätä kutsutaan populaatioinversioksi." style="max-width:100%;font-size:24px">
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
Laseraine on kahden peilin välissä. Toinen peili heijastaa kaiken valon. Toinen heijastaa esimerkiksi $99\,\%$ ja päästää loput läpi. Fotoni kulkee peilien välillä akselin suuntaisesti. Se kulkee aineen läpi satoja kertoja ja tekee matkallaan stimuloituja kopioita itsestään. Sivulle lähtevät fotonit poistuvat aineesta, eivätkä ne ehdi monistua. Siksi vahvistuu vain akselin suuntainen valo. Osittain läpäisevän peilin läpi tulee ulos säde. Laser alkaa toimia vasta, kun pumppaus on niin voimakas, että vahvistuminen korvaa peilin läpi ja muualle menetetyn valon. Tätä pumppauksen raja-arvoa kutsutaan **kynnykseksi**.

Laservalo on lähes yksiväristä, koska fotonit syntyvät samassa siirtymässä. Se on suuntautunutta, koska vain akselin suuntainen valo vahvistuu. Siksi säde levenee vain vähän. Laservalo on myös koherenttia. Se tarkoittaa, että aallot ovat samassa tahdissa, koska jokainen stimuloitu fotoni kopioi saapuvan fotonin vaiheen. Taskulampun valossa on monia aallonpituuksia. Se lähtee eri suuntiin ja eri tahdissa. Myös laserdiodissa on vahvistava aine ja peilit. Sähkövirta synnyttää inversion puolijohteessa, ja kiteen lohkaistut päät toimivat peileinä. Laserdiodin energiatasot ovat kuitenkin energiavöitä eivätkä yksittäisen atomin tasoja.

<svg data-fig="cavity" viewBox="0 0 600 300" role="img" aria-label="Laserin rakenne, kaavakuva, ei mittakaavassa. Keskellä on vaakasuora sauva aktiivista ainetta. Sauvan vasemmassa päässä on peili, joka heijastaa kaiken valon. Oikeassa päässä on peili, joka heijastaa 99 prosenttia ja päästää läpi 1 prosentin. Sauvan alla on pumppauslamppu. Lampun valo nostaa atomit viritystilaan. Sauvan sisällä punaiset fotonit kulkevat akselin suuntaisesti edestakaisin peilien välillä ja monistuvat. Kaksi fotonia lähtee vinosti sivulle ja poistuu sauvasta. Oikean peilin läpi tulee ulos kapea punainen lasersäde." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-7-cavity.webp" x="30.7" y="23.6" width="566" height="293.6" preserveAspectRatio="none"/>
  <foreignObject x="47.5" y="49.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{peili}\ 100\,\%$</div></foreignObject>
  <foreignObject x="422" y="49.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{peili}\ 99\,\%$</div></foreignObject>
  <foreignObject x="208.5" y="73.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{aktiivinen aine}$</div></foreignObject>
  <foreignObject x="468" y="171.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\text{lasersäde}$</div></foreignObject>
  <foreignObject x="246" y="255.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\text{pumppaus}$</div></foreignObject>
</svg>

### Kvanttirakenteet: koko määrää energiatasot
Puolijohteen **energia-aukko** on pienin energia, jonka sen elektroni voi saada valosta tai antaa valoksi. Se määrää LEDin valon värin (luku *LEDin valo ja Planckin vakion mittaaminen*). Isossa kiteessä energia-aukko riippuu vain aineesta. Luvussa *Aaltomekaaninen atomimalli ja orbitaalit* elektronin tiloja verrattiin kielen seisoviin aaltoihin. Lyhyemmän kielen sallitut värähtelyt ovat korkeampia ja kauempana toisistaan. Samoin käy, kun elektronit suljetaan rakenteeseen, jonka koko on vain muutamia nanometrejä. Sallitut energiat ovat silloin kauempana toisistaan. Energia-aukko kasvaa, kun rakenne pienenee. Tällaisia puolijohteen rakenteita kutsutaan **kvanttirakenteiksi**. Ohut kerros on kvanttikaivo. Nanokide, joka on rajattu joka suunnasta, on **kvanttipiste**.

Puolijohdekvanttipisteen väri voidaan siis valita sen koolla, vaikka aine on sama. Kadmiumselenidistä tehty kvanttipiste, jonka halkaisija on $2\,\text{nm}$, lähettää syaania valoa. Piste, jonka halkaisija on $6\,\text{nm}$, lähettää punaista valoa. Ison kadmiumselenidikiteen energia-aukko on $1{,}74\,\text{eV}$. Se vastaa tummanpunaista valoa näkyvän alueen reunalla, noin $713\,\text{nm}$. Kun pistettä pienennetään, valon aallonpituus lyhenee. Tässä luvussa riittää tämä laadullinen yhteys. Energiatasojen tarkka laskeminen pisteen koosta vaatii kvanttimekaanista mallinnusta. Tehtävät, joissa koon ja aallonpituuden yhteyttä lasketaan, ovat lisätietoa. Kemian Nobel-palkinto myönnettiin kvanttipisteiden löytämisestä ja valmistamisesta vuonna 2023.

<svg data-fig="qdots" viewBox="0 0 600 370" role="img" aria-label="Viisi kvanttipistettä allekkain. Halkaisijat ovat keskenään mittakaavassa. Jokainen piste on piirretty sen lähettämän valon värisenä. Halkaisija 2,0 nm: aallonpituus 480 nm, fotonin energia 2,58 eV, syaani. Halkaisija 3,0 nm: 530 nm, 2,34 eV, vihreä. Halkaisija 4,0 nm: 570 nm, 2,18 eV, kellanvihreä. Halkaisija 5,0 nm: 600 nm, 2,07 eV, oranssi. Halkaisija 6,0 nm: 620 nm, 2,00 eV, punainen. Mitä pienempi piste on, sitä lyhyempi on aallonpituus ja sitä suurempi on fotonin energia." style="max-width:100%;font-size:24px">
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

<figure class="unit-photo"><img src="pics/fy8/helium-neon-laser.webp" alt="Musta laite, jossa lukee He-Ne LASER. Sen päässä loistaa punainen valo."><figcaption>Helium-neonlaser. Sähköpurkaus antaa kaasun atomeille energiaa. Putken päissä on peilit, jotka vahvistavat valoa. Laser tekee kapean punaisen säteen, jonka aallonpituus on $633\,\text{nm}$.</figcaption></figure>

```pysahdy
Kadmiumselenidistä tehty kvanttipiste lähettää sinistä valoa, jonka aallonpituus on $450\,\text{nm}$. Käytä $hc = 1240\,\text{eV}\,\text{nm}$. Laske fotonin energia. Päättele, onko piste halkaisijaltaan suurempi vai pienempi kuin $2{,}0\,\text{nm}$:n piste. Kuinka paljon pisteen energia-aukko on suurempi kuin ison kiteen aukko $1{,}74\,\text{eV}$?
---
Fotonin energia on $\tfrac{hc}{\lambda} = \tfrac{1240\,\text{eV}\,\text{nm}}{450\,\text{nm}} \approx 2{,}76\,\text{eV}$. Energia-aukko on melkein yhtä suuri. Se on suurempi kuin $2{,}0\,\text{nm}$:n pisteen aukko ($480\,\text{nm}$ vastaa $2{,}58\,\text{eV}$), joten piste on pienempi kuin $2{,}0\,\text{nm}$. Ero on $2{,}76\,\text{eV} - 1{,}74\,\text{eV} \approx 1{,}0\,\text{eV}$.
```

### Kvanttirakenteiden sovelluksia
Kvanttipistenäytössä sininen taustavalo osuu kvanttipisteisiin. Pisteet absorboivat sen ja lähettävät puhdasta vihreää tai punaista valoa. Sama tapahtuu fluoresenssissa luvussa *Spektrit paljastavat atomin energiatasot*. Useimmat laserdiodit ovat kvanttikaivolasereita. Niissä kaivon paksuus valitsee aallonpituuden. Aurinkokennoihin tutkitaan kvanttipistekerroksia. Pisteiden koon avulla kerros voidaan säätää absorboimaan haluttu osa Auringon spektristä.

Kvanttitietokoneen perusyksikkö on **kubitti**. Kubitti on kvanttijärjestelmä, jolla on kaksi tilaa. Se voi olla myös näiden tilojen yhdistelmässä eli superpositiossa. Kubitteja tehdään esimerkiksi elektroneista, jotka on suljettu puolijohteen kvanttipisteisiin, ja suprajohtavista piireistä. Tällainen piiri käyttäytyy kuin keinotekoinen atomi, jolla on omat kvantittuneet energiatasonsa. Suomessa suprajohtavia kvanttitietokoneita rakentavat VTT ja IQM. Kubitin tilat ovat herkkiä. Siksi piirit jäähdytetään lähelle absoluuttista nollapistettä ja suojataan ympäristön häiriöiltä.

<figure class="unit-photo"><img src="pics/fy8/rgb-laser-pointer.webp" alt="Kolme lasersädettä pimeässä: punainen, vihreä ja sininen."><figcaption>Punainen, vihreä ja sininen lasersäde. Ilmassa on pieniä hiukkasia, jotka sirottavat valoa. Siksi säteet näkyvät. Sinisen valon fotonissa on eniten energiaa ja punaisen valon fotonissa vähiten.</figcaption></figure>

## Kaava: Laserin fotonit
Kaikki laserin fotonit syntyvät samassa siirtymässä. Siksi jokaisen fotonin energia ja aallonpituus ovat
```latex
\begin{aligned}
hf &= E_2 - E_1 \\
\lambda &= \frac{hc}{E_2 - E_1}
\end{aligned}
```
missä $E_2$ on ylemmän ja $E_1$ alemman lasertason energia, $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ on Planckin vakio, $f$ on valon taajuus, $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$ on valon nopeus ja $\lambda$ on aallonpituus.

Fotonit ovat samanlaisia. Siksi laserin teho on sekunnissa lähtevien fotonien määrä kerrottuna yhden fotonin energialla:
```latex
P = \frac{N}{t} \cdot hf
```
missä $P$ on laserin teho ja $N$ on aikana $t$ lähtevien fotonien määrä. Fotonien määrä sekunnissa on siis $\tfrac{N}{t} = \tfrac{P}{hf}$. Energiat lasketaan usein elektronivoltteina. Ne muunnetaan jouleiksi sijoittamalla $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$.

Samalla teholla pidemmän aallonpituuden laser lähettää enemmän fotoneja, koska yksi fotoni kantaa vähemmän energiaa. Kuvaajassa punainen laserosoitin, jonka teho on $1{,}0\,\text{mW}$, lähettää noin $3{,}3 \cdot 10^{15}$ fotonia sekunnissa. Yhtä tehokas violetti laserosoitin lähettää noin $2{,}0 \cdot 10^{15}$ fotonia sekunnissa.

<svg data-fig="rate-graph" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa. Kuvaaja näyttää, kuinka monta fotonia sekunnissa laser lähettää, kun teho on 1,0 milliwattia. Fotonien määrä on aallonpituuden funktio. Vaaka-akselilla on aallonpituus nollasta 700 nanometriin. Pystyakselilla on fotonien määrä sekunnissa yksikössä 10 potenssiin 15 fotonia sekunnissa, nollasta 3,5:een. Kuvaaja on suora, joka kulkee origon kautta. Siihen on merkitty kolme laserosoitinta: violetti 405 nm, 2,04, vihreä 532 nm, 2,68, ja punainen 650 nm, 3,27. Laser, jonka aallonpituus on pidempi, lähettää samalla teholla enemmän fotoneja, koska yksi fotoni kantaa vähemmän energiaa." style="max-width:100%;font-size:24px">
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
Laserin teho pysyy samana, mutta yhden fotonin energia kaksinkertaistuu. Mitä tapahtuu sekunnissa lähtevien fotonien määrälle?
---
Koska $\tfrac{N}{t} = \tfrac{P}{hf}$, fotonien määrä sekunnissa puolittuu. Yksi fotoni kantaa enemmän energiaa, joten niitä tarvitaan vähemmän.
```

## Esimerkki
Helium–neonlaserin lasersiirtymän tasojen energiaero on $1{,}96\,\text{eV}$, ja laserin teho on $1{,}0\,\text{mW}$. Kuinka monta fotonia laser lähettää sekunnissa?

<!-- vaihe -->

**Tunnetut ja kysytty.** Tasojen energiaero on $E_2 - E_1 = 1{,}96\,\text{eV}$ ja teho on $P = 1{,}0\,\text{mW}$.

Kysytään sekunnissa lähtevien fotonien määrää $\tfrac{N}{t}$.

<!-- vaihe -->

**Periaate.** Kaikki laserin fotonit syntyvät samassa siirtymässä. Siksi jokaisen fotonin energia on $hf = E_2 - E_1$. Teho on fotonien määrä sekunnissa kerrottuna yhden fotonin energialla.

<!-- vaihe -->

**Kaava ratkaistuna.** Sijoitetaan fotonin energiaksi tasojen erotus ja ratkaistaan fotonien määrä sekunnissa:
```latex
\begin{aligned}
&P = \frac{N}{t} \cdot (E_2 - E_1) \\
&\frac{N}{t} = \frac{P}{E_2 - E_1}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Teho on $P = 1{,}0\,\text{mW} = 1{,}0 \cdot 10^{-3}\,\text{W}$. Energiaero muunnetaan jouleiksi sijoittamalla $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$: $E_2 - E_1 = 1{,}96 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 3{,}1399 \cdot 10^{-19}\,\text{J}$.

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

**Tulos.** Laser lähettää noin $3{,}2 \cdot 10^{15}$ fotonia sekunnissa. Tulos annetaan kahdella merkitsevällä numerolla, koska teho $1{,}0\,\text{mW}$ on annettu kahdella.

<!-- vaihe -->

**Järkevyys.** Yksikkö on oikein, koska $\tfrac{\text{W}}{\text{J}} = \tfrac{\text{J/s}}{\text{J}} = \tfrac{1}{\text{s}}$. Energiaeroa vastaa aallonpituus $\lambda = \tfrac{hc}{E_2 - E_1} \approx 633\,\text{nm}$. Se on helium–neonlaserin tuttu punainen valo. Kuvaajan mukaan laser, jonka teho on $1{,}0\,\text{mW}$, lähettää aallonpituudella $650\,\text{nm}$ noin $3{,}3 \cdot 10^{15}$ fotonia sekunnissa. Lyhyemmällä aallonpituudella fotonien määrä on hieman pienempi, joten tulos on uskottava.

## Yleinen virhekäsitys
Moni luulee, että laservalo on vaarallista, koska sen fotonit ovat erityisen energisiä. Fotonin energia riippuu kuitenkin vain aallonpituudesta. Punaisen laserosoittimen fotonin energia $1{,}91\,\text{eV}$ on sama kuin minkä tahansa $650\,\text{nm}$:n valon fotonin energia. Violetin $405\,\text{nm}$:n valon fotonit ovat energisempiä, tulivat ne laserista tai lampusta. Laserin vaara on siinä, että koko teho kulkee kapeassa säteessä. Silmän linssi kohdistaa säteen verkkokalvolle hyvin pieneksi pisteeksi. Siksi koulussa käytetään vain pienitehoisia lasereita. Säteeseen tai sen peiliheijastukseen ei katsota, eikä sädettä suunnata ihmisiin.

Toinen virhe on ajatella, että stimuloidussa emissiossa atomi absorboi fotonin ja lähettää kaksi. Saapuva fotoni ei absorboidu, vaan jatkaa matkaansa. Uuden fotonin energian antaa viritetty atomi, joka putoaa tasolta $E_2$ tasolle $E_1$. Siksi energia säilyy.

## Tunneloituminen
Klassisen fysiikan mukaan pallo vierii takaisin, jos sen energia ei riitä mäen yli. Kvanttifysiikassa elektronin havaitsemisen todennäköisyys ei lopu esteen reunaan. Se pienenee esteen sisällä nopeasti. Jos este on hyvin ohut, todennäköisyys jää esteen takana pieneksi mutta ei nollaksi. Elektroni voi löytyä esteen takaa, vaikka sen energia on pienempi kuin esteen ylittämiseen tarvittava energia. Tätä kutsutaan **tunneloitumiseksi**. Todennäköisyys pienenee erittäin jyrkästi, kun este paksuuntuu tai sen korkeus kasvaa. Siksi tunneloituminen on merkittävää vain nanometrien luokkaa olevilla esteillä.

<svg data-fig="tunnel" viewBox="0 0 600 320" role="img" aria-label="Periaatekuva tunneloitumisesta, ei mittakaavassa. Vasemmalta tulee elektroni. Sen energia E on vaakasuora katkoviiva. Energia on pienempi kuin keskellä olevan harmaan esteen korkeus. Sininen alue kuvaa elektronin havaitsemisen todennäköisyyttä. Esteen vasemmalla puolella todennäköisyys on suuri. Esteen sisällä se pienenee nopeasti. Esteen oikealla puolella se on pieni mutta ei nolla. Elektroni voi siis löytyä esteen takaa, vaikka sen energia ei riitä esteen yli." style="max-width:100%;font-size:24px">
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

Tunnelointimikroskoopissa terävä metallikärki viedään noin nanometrin päähän pinnasta. Kärjen ja pinnan välillä tunneloituvien elektronien virta muuttuu voimakkaasti etäisyyden mukaan. Siksi kärjellä voidaan kuvata yksittäisiä atomeja. Flash-muistin muistisoluun kirjoitetaan bitti siirtämällä elektroneja ohuen eristekerroksen läpi tunneloitumalla. Suprajohtavissa kubiteissa virta kulkee ohuen eristekerroksen läpi tunneloitumalla. Vuoden 2025 fysiikan Nobel-palkinto myönnettiin kvanttitunneloitumisen ja energian kvantittumisen havaitsemisesta tällaisissa piireissä. Myös alfahajoaminen on tunneloitumista. Siitä kerrotaan luvussa *Atomiydin ja radioaktiivinen hajoaminen*.

## Tiivistelmä
- Viritetty atomi voi lähettää fotonin itsestään (spontaani emissio) tai saapuvan fotonin vaikutuksesta (stimuloitu emissio). Stimuloidussa emissiossa syntyy fotoni, jolla on saapuvan fotonin energia, suunta ja vaihe.
- Valo vahvistuu vain, kun ylemmällä lasertasolla on enemmän atomeja kuin alemmalla, $N_2 > N_1$ (populaatioinversio). Atomi- ja ionilasereissa inversio saadaan pumppaamalla aineeseen, jossa on kolme tai neljä tasoa ja pitkäikäinen ylempi lasertaso. Puolijohdelaserissa inversio syntyy sähkövirralla energiavöihin.
- Peilien välissä akselin suuntainen valo kulkee aineen läpi monta kertaa ja vahvistuu. Laser toimii, kun pumppaus ylittää kynnyksen. Laservalo on lähes yksiväristä, suuntautunutta ja koherenttia.
- Laserin fotonien energia on $hf = E_2 - E_1$, ja teho on $P = \tfrac{N}{t} \cdot hf$.
- Puolijohteen kvanttirakenteissa elektronit on suljettu nanometrien kokoiseen tilaan. Energia-aukko kasvaa, kun rakenne pienenee: pienempi kvanttipiste lähettää lyhyempää aallonpituutta. Sovelluksia ovat kvanttipistenäytöt, kvanttikaivolaserit, aurinkokennojen tutkimus ja kvanttitietokoneiden kubitit.
