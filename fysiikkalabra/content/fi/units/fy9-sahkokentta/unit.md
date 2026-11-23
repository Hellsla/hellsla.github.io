# Sähkökenttä ja kondensaattori

> **Miksi** ovenkahvasta pakkaspäivänä lyövä kipinä ei vahingoita, vaikka sen jännite on tuhansia voltteja?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvi-ilta eteisessä. Keskellä on puinen ulko-ovi, jossa on messinkinen kahva pitkässä metallilevyssä. Oikealta kurottaa käsi punaisessa neulehihassa kohti kahvaa, ja sormenpään ja metallilevyn välissä välähtää pieni kirkas kipinä. Lattialla on raidallinen villamatto. Vasemmalla on ikkuna, josta näkyy luminen yö, kuu ja kuusia, ja ikkunan alla patteri. Seinän naulakossa roikkuu villapipo." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-sahkokentta-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

Tunnin tehtävät alkavat samasta ajatuksesta: **varaus synnyttää ympärilleen sähkökentän, ja kenttä kohdistaa toiseen varaukseen voiman** $\overline{F} = q\overline{E}$. Positiiviseen varaukseen voima osoittaa kentän suuntaan ja negatiiviseen kenttää vastaan. Kun kenttä siirtää varausta, se tekee työtä, ja varauksen potentiaalienergia muuttuu kuten pallon korkeusenergia painovoimakentässä. Kondensaattori varastoi energiaa levyjensä väliseen kenttään. Puolijohdekomponentit ja sähköturvallisuus palaavat samoihin suureisiin: jännite, virta ja eristeen kestämä kenttä.

<svg data-fig="kartta" viewBox="0 0 380 780" role="img" aria-label="Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Piirrä tilanne ensin ja katso, mikä tehtävän tunnusmerkki  sopii. Kaksi varattua kappaletta: Coulombin voima on Coulombin vakio kertaa varausten tulo jaettuna etäisyyden  neliöllä. Varaus sähkökentässä: kentän voimakkuus on voima jaettuna varauksella. Levyjen välillä tasainen  kenttä: jännite on kentän voimakkuus kertaa etäisyys. Varaus kiihtyy jännitteessä: kentän työ varauksen ja  jännitteen tulo on yhtä suuri kuin liike-energia. Kondensaattorin varaus: varaus on kapasitanssi kertaa jännite.  Levykondensaattorin mitat: kapasitanssi on tyhjiön permittiivisyys kertaa suhteellinen permittiivisyys kertaa  pinta-ala jaettuna levyjen välimatkalla. Kondensaattorin energia: puolet kapasitanssin ja jännitteen neliön  tulosta. LED tarvitsee etuvastuksen: silmukkaan sovelletaan Kirchhoffin 2. lakia, jännitteiden summa on nolla." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="736" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{mistä tunnistan lain?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{piirrä tilanne ensin, sitten tunnusmerkki}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kaksi varattua kappaletta}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{voima}$</div></foreignObject>
  <rect x="238" y="142" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="144" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_E = kQ_1Q_2/r^2$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{varaus sähkökentässä}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{kentän voimakkuus}$</div></foreignObject>
  <rect x="238" y="228" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="230" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E = F_E/Q$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{levyjen välillä tasainen kenttä}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{jännite ja matka}$</div></foreignObject>
  <rect x="238" y="314" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="316" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$U = Ed$</div></foreignObject>
  <line x1="14" y1="392" x2="30" y2="392" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{varaus kiihtyy jännitteessä}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{työ ja energia}$</div></foreignObject>
  <rect x="238" y="400" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="402" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$QU = \tfrac12 mv^2$</div></foreignObject>
  <line x1="14" y1="478" x2="30" y2="478" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="442" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="452.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kondensaattorin varaus}$</div></foreignObject>
  <line x1="40" y1="482" x2="362" y2="482" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="487" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{kapasitanssi}$</div></foreignObject>
  <rect x="238" y="486" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="488" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$Q = CU$</div></foreignObject>
  <line x1="14" y1="564" x2="30" y2="564" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="528" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="538.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{levykondensaattorin mitat}$</div></foreignObject>
  <line x1="40" y1="568" x2="362" y2="568" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="573" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{kapasitanssi}$</div></foreignObject>
  <rect x="238" y="572" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="574" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$C = \varepsilon_0\varepsilon_\text{r}A/d$</div></foreignObject>
  <line x1="14" y1="650" x2="30" y2="650" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="614" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="624.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kondensaattorin energia}$</div></foreignObject>
  <line x1="40" y1="654" x2="362" y2="654" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="659" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{varastoitu energia}$</div></foreignObject>
  <rect x="238" y="658" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="660" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E = \tfrac12 CU^2$</div></foreignObject>
  <line x1="14" y1="736" x2="30" y2="736" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="700" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="710.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{LED tarvitsee etuvastuksen}$</div></foreignObject>
  <line x1="40" y1="740" x2="362" y2="740" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="745" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{silmukka}$</div></foreignObject>
  <rect x="238" y="744" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="746" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma\Delta V = 0$</div></foreignObject>
</svg>

Alun kipinä ratkeaa näillä laeilla. Kun kävelet villamatolla, kehoosi kertyy varausta, ja kahvan metallilevyn lähipinnalle siirtyy influenssin vuoksi vastakkaismerkkinen varaus. Kipinä hyppää, kun ilmavälin kenttä ylittää ilman läpilyöntilujuuden noin $3\,\text{MV/m}$. Noin $3\,\text{mm}$:n kipinä kertoo siis noin $9\,\text{kV}$:n jännitteestä.

Jännite on suuri, mutta keho on pieni kondensaattori, jonka kapasitanssi on noin $100\,\text{pF}$, joten varausta on vain noin $0{,}9\,\mu\text{C}$ ja energiaa noin $4\,\text{mJ}$. Purkaus kestää noin mikrosekunnin. Vaarallinen virta, noin $50\,\text{mA}$ sekunnin ajan, kuljettaisi kehon läpi $0{,}05\,\text{C}$, yli $50\,000$ kertaa enemmän varausta.

<svg data-fig="kipina" viewBox="0 0 600 540" role="img" aria-label="Kaavakuva, ei mittakaavassa. Vasemmalla sormenpää, jonka pinnalla on negatiivisia varauksia. Oikealla oven kahvan metallilevy, jonka sormen puoleiselle pinnalle on influenssin vuoksi siirtynyt positiivisia varauksia. Niiden välissä on noin 3 millimetrin ilmaväli, jonka poikki kulkee vihreitä kenttäviivoja levystä sormeen ja kirkas sinivalkoinen kipinä; kenttä on noin 3 MV/m, ilman läpilyöntilujuus. Alla laskelma: jännite U = E kertaa d on noin 9 kV, keho on kondensaattori, jonka kapasitanssi on noin 100 pF, joten varaus Q = C U on noin 0,9 mikrocoulombia ja energia W = puoli C U toiseen noin 4 millijoulea." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-sahkokentta-kipina.webp" x="0" y="0" width="600" height="541.2" preserveAspectRatio="none"/>
  <foreignObject x="322" y="29" width="40" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="261" y="261" width="160" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px">$d \approx 3\,\text{mm}$</div></foreignObject>
  <foreignObject x="69.5" y="223" width="81" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{sormi}$</div></foreignObject>
  <foreignObject x="464.5" y="253" width="81" height="34" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:28px;color:#6b7480">$\text{kahva}$</div></foreignObject>
  <foreignObject x="14" y="319.5" width="379" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:34px">$U = Ed \approx 3\,\text{MV/m} \cdot 3\,\text{mm} \approx 9\,\text{kV}$</div></foreignObject>
  <foreignObject x="14" y="381.5" width="397" height="41" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:34px">$Q = CU \approx 100\,\text{pF} \cdot 9\,\text{kV} \approx 0{,}9\,\mu\text{C}$</div></foreignObject>
  <foreignObject x="14" y="443" width="238" height="82" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:34px">$W = \dfrac12 CU^2 \approx 4\,\text{mJ}$</div></foreignObject>
</svg>

## Kaava: Sähkökenttä ja kondensaattori

### Varaus, voima ja kenttä

```kaavat
Q = ne
Coulombin voiman suuruus :: F_E = k\,\frac{Q_1 Q_2}{r^2}
sähkökentän voimakkuus :: E = \frac{F_E}{Q}
jännite homogeenisessa sähkökentässä :: U = Ed
```

missä $n$ on alkeisvarausten lukumäärä, $e = 1{,}602 \cdot 10^{-19}\,\text{C}$ alkeisvaraus, $F_E$ sähköisen voiman suuruus ($\text{N}$), $Q_1$ ja $Q_2$ varausten suuruudet ($\text{C}$), $r$ niiden etäisyys ($\text{m}$), $k = 8{,}988 \cdot 10^{9}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{C}^2}$, $E$ sähkökentän voimakkuus ($\text{N/C} = \text{V/m}$) varauksen $Q$ kohdalla, $U$ levyjen välinen jännite ($\text{V}$) ja $d$ levyjen etäisyys ($\text{m}$). Positiiviseen varaukseen kohdistuva voima on kentän suuntainen, negatiiviseen vastakkainen, eli vektoreina $\overline{F}_E = Q\overline{E}$. Varaus säilyy. Coulombin laki pätee pistevarauksille ja tasaisesti varatuille palloille, ja usean varauksen voimat lasketaan yhteen vektoreina. Yhteys $U = Ed$ pätee vain laajojen yhdensuuntaisten levyjen välissä, jossa kenttä on homogeeninen.

<svg data-fig="levyt" viewBox="0 0 600 440" role="img" aria-label="Kaavakuva: kaksi vaakasuoraa levyä. Ylempi levy on positiivinen ja sen potentiaali on 200 V, alempi negatiivinen levy on nollakohta 0 V. Levyjen välissä on viisi vihreää pystysuoraa kenttäviivaa, jotka osoittavat alas: kenttä on homogeeninen. Harmaat katkoviivat ovat tasapotentiaalipintoja 150 V, 100 V ja 50 V. Vasemmalla protoni, jonka punainen voimanuoli osoittaa alas kentän suuntaan. Oikealla elektroni, jonka punainen voimanuoli osoittaa ylös kenttää vastaan, kohti suurempaa potentiaalia." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-sahkokentta-levyt.webp" x="0" y="0" width="600" height="447.5" preserveAspectRatio="none"/>
  <foreignObject x="34" y="124.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px;color:#6b7480">$150\,\text{V}$</div></foreignObject>
  <foreignObject x="34" y="194.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px;color:#6b7480">$100\,\text{V}$</div></foreignObject>
  <foreignObject x="48" y="264.5" width="62" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px;color:#6b7480">$50\,\text{V}$</div></foreignObject>
  <foreignObject x="34" y="45.5" width="76" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$200\,\text{V}$</div></foreignObject>
  <foreignObject x="61" y="343.5" width="49" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:26px">$0\,\text{V}$</div></foreignObject>
  <foreignObject x="524" y="285.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{E}$</div></foreignObject>
  <foreignObject x="230" y="245.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F} = e\overline{E}$</span></div></foreignObject>
  <foreignObject x="486" y="157.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{F} = -e\overline{E}$</span></div></foreignObject>
  <foreignObject x="164.5" y="391.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{protoni}$</div></foreignObject>
  <foreignObject x="408" y="391.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{elektroni}$</div></foreignObject>
</svg>

### Potentiaali ja energia

```kaavat
sähkökentän potentiaali :: V = \frac{E_\text{p}}{Q}
sähkökentän tekemä työ :: W = QU
```

missä $V$ on kohdan potentiaali ($\text{V}$) valittuun nollakohtaan nähden, $E_\text{p}$ varauksen $Q$ sähköinen potentiaalienergia ($\text{J}$), $W$ kentän tekemä työ ($\text{J}$), kun varaus $Q$ siirtyy pisteestä A pisteeseen B, ja $U = U_{AB} = V_A - V_B$ pisteiden välinen jännite. Työ ei riipu reitistä. Kenttä osoittaa suuremmasta potentiaalista pienempään, ja levosta lähtevä varaus liikkuu suuntaan, jossa sen potentiaalienergia pienenee. Energian yksikkö $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$.

Kun hiukkanen, jonka massa on $m$ ($\text{kg}$) ja varaus $Q$, lähtee levosta ja kiihtyy sähkökentässä jännitteen $U$ läpi, kentän tekemä työ muuttuu hiukkasen liike-energiaksi. Hiukkasen vauhti lopussa on $v$ ($\text{m/s}$).

```johda
Hiukkanen (massa $m$, varaus $Q$) lähtee levosta ja kiihtyy sähkökentässä kahden pisteen välillä, joiden välinen jännite on $U$. Vain sähköinen voima tekee työtä. Johda yhtälö hiukkasen loppuvauhdille $v$.
---
Mekaniikan energiaperiaatteen mukaan hiukkaseen tehty työ muuttaa sen liike-energiaa. Vain sähköinen voima tekee työtä, ja hiukkanen lähtee levosta, joten liike-energia alussa on nolla:

$$W = E_\text{k} - 0 = \tfrac12 mv^2$$

Sähkökentän tekemä työ on $W = QU$. Levosta lähtevä varaus liikkuu aina suuntaan, jossa kenttä tekee positiivista työtä, joten työn suuruus on $\lvert Q \rvert U$, kun $U$ on jännitteen suuruus:

$$\tfrac12 mv^2 = \lvert Q \rvert U$$

Ratkaistaan vauhti:

$$v = \sqrt{\frac{2\lvert Q \rvert U}{m}}$$

Esimerkiksi alkeisvaraus saa jännitteen $1\,\text{V}$ läpi liike-energian $1\,\text{eV}$.
```

### Kondensaattori

```kaavat
kondensaattorilaki :: Q = CU
levykondensaattorin kapasitanssi :: C = \varepsilon_0\varepsilon_\text{r}\,\frac{A}{d}
kondensaattorin energia :: E = \tfrac12 CU^2
```

missä $C$ on kapasitanssi ($\text{F}$), $A$ levyn pinta-ala ($\text{m}^2$), $\varepsilon_0 = 8{,}854 \cdot 10^{-12}\,\text{F/m}$, $\varepsilon_\text{r}$ eristeen suhteellinen permittiivisyys, $E$ kondensaattoriin varastoitunut energia ($\text{J}$), myös $E = \tfrac12 QU$. Levykondensaattorin kaava pätee, kun $d$ on pieni levyjen kokoon verrattuna ja eriste täyttää välin. Lähteeseen kytketyn kondensaattorin jännite pysyy samana, irrotetun varaus.

Eristeen läpilyöntilujuus $E_\text{max}$ ($\text{V/m}$) on suurin sähkökentän voimakkuus, jonka eriste kestää. Jos kenttä kasvaa suuremmaksi, eriste alkaa johtaa ja levyjen välillä tapahtuu läpilyönti, joten kondensaattorin jännitteellä on suurin arvo $U_\text{max}$ ($\text{V}$).

```johda
Levykondensaattorin levyjen etäisyys on $d$, ja levyjen välin täyttävän eristeen läpilyöntilujuus on $E_\text{max}$. Johda suurin jännite $U_\text{max}$, jonka kondensaattori kestää.
---
Levyjen välissä kenttä on homogeeninen, joten jännite homogeenisessa sähkökentässä on

$$U = Ed$$

Kun jännite kasvaa, kenttä kasvaa samassa suhteessa. Läpilyönti tapahtuu, kun kenttä saavuttaa läpilyöntilujuuden, eli $E = E_\text{max}$:

$$U_\text{max} = E_\text{max}d$$

Sama päättely antaa alun kipinän jännitteen: ilmavälin $d$ yli voi olla enintään jännite, jolla kenttä on ilman läpilyöntilujuus.
```

### Komponentit ja turvallisuus

```kaavat
+ \eta = \frac{P}{GA}
jännitehäviö johtimessa :: U = RI
```

missä $\eta$ on aurinkokennon hyötysuhde, $P$ kennon sähköteho maksimitehopisteessä ($\text{W}$), $G$ kennoon tulevan valon voimakkuus eli teho pinta-alaa kohti ($\text{W/m}^2$) ja $A$ kennon pinta-ala ($\text{m}^2$). Hyötysuhteen yhtälö pätee, kun valo tulee kohtisuoraan kennoon. Yhtälö on lisätietoa: sitä ei ole MAFY-taulukoissa, ja kokeessa se annetaan tehtävässä, jos sitä tarvitaan.

Jännitehäviön yhtälössä $U$ on jännite ($\text{V}$), $R$ resistanssi ($\Omega$) ja $I$ virta ($\text{A}$). Yhtälöstä saadaan kehon läpi kulkeva virta $I = \tfrac{U}{R}$, kun $U$ on kosketusjännite ja $R$ koko virtatien resistanssi. Diodi johtaa vain päästösuuntaan, kun sen jännite ylittää kynnysjännitteen. Sulake suojaa johtoa, vikavirtasuoja ihmistä.

LED kytketään jännitelähteeseen $U$ ($\text{V}$) sarjaan etuvastuksen $R$ ($\Omega$) kanssa, joka rajoittaa virran $I$ ($\text{A}$) sopivaksi. Johtavan LEDin jännite $U_\text{D}$ ($\text{V}$) pysyy lähes samana virrasta riippumatta.

<svg data-fig="etuvastus" viewBox="0 0 600 300" role="img" aria-label="Kytkentäkaavio, ei lukuarvoja. Vasemmalla jännitelähde, jonka jännite on U ja plusnapa ylhäällä. Ylempään johtimeen on kytketty etuvastus R. Oikealla on LED päästösuuntaan: sen kolmio osoittaa alaspäin, plusnavan puolelta miinusnavan puolelle, ja siitä lähtee kaksi pientä valon nuolta. LEDin jännite on U D. Violetti virta I kulkee plusnavasta vastuksen ja LEDin kautta takaisin miinusnapaan." style="max-width:100%;font-size:24px">
  <polyline points="140,152 140,70 250,70" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="330,70 440,70 440,142" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="440,176 440,250 140,250 140,168" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="114" y1="152" x2="166" y2="152" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="127" y1="168" x2="153" y2="168" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="174" y="123" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$+$</div></foreignObject>
  <foreignObject x="86" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U$</div></foreignObject>
  <rect x="250" y="58" width="80" height="24" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="280" y="19.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <path d="M422,142 L458,142 L440,174 Z" fill="#ffffff" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="420" y1="176" x2="460" y2="176" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="464" y1="156" x2="483.5" y2="136.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M490,130 L486,140.5 L479.5,134 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="468" y1="170" x2="487.5" y2="150.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M494,144 L490,154.5 L483.5,148 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="502" y="170" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{LED}$</div></foreignObject>
  <line x1="400" y1="186" x2="400" y2="143" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M400,132 L405.5,144 L394.5,144 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="355" y="145.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$U_\text{D}$</div></foreignObject>
  <path d="M225,70 L205,62 L205,78 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M280,250 L300,242 L300,258 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="205" y="29.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
</svg>

```johda
LED ja etuvastus on kytketty sarjaan jännitelähteeseen, jonka jännite on $U$. LEDin jännite on $U_\text{D}$, ja piirissä halutaan kulkevan virta $I$. Johda etuvastuksen resistanssi $R$.
---
Kierretään piiri kerran virran suuntaan Kirchhoffin 2. lailla. Potentiaali nousee lähteessä jännitteen $U$ verran. Se laskee vastuksessa jännitehäviön $RI$ verran (jännitehäviö johtimessa) ja LEDissä jännitteen $U_\text{D}$ verran:

$$U - RI - U_\text{D} = 0$$

Ratkaistaan resistanssi:

$$R = \frac{U - U_\text{D}}{I}$$

Vastuksen yli on siis vain se osa lähteen jännitteestä, joka ei jää LEDin yli. Lähteen sisäinen resistanssi on oletettu pieneksi.
```

## Yleisiä virheitä {Virheet}

- **Kenttä ja voima samaan suuntaan aina.** Negatiiviseen varaukseen, kuten elektroniin, voima osoittaa kenttää vastaan.
- **Etäisyys ilman neliötä.** Kaksinkertainen etäisyys antaa Coulombin laissa neljäsosan voimasta.
- **Kenttä kasvaa levyä lähestyttäessä.** Levyjen välissä kenttä on homogeeninen: voima on sama kaikkialla.
- **Energia $QU$.** Kondensaattoriin varastoituu $\tfrac12 QU$; toinen puoli muuttuu latauksessa johtimien sisäenergiaksi.
- **Eriste irrotetussa kondensaattorissa.** Varaus pysyy, joten jännite ja energia pienenevät, eivät kasva.
- **Etuvastus ilman LEDin jännitettä.** Vastuksen yli on vain $U - U_\text{D}$.
- **Suuri jännite on aina vaarallinen.** Vaara syntyy kehon kautta kulkevasta virrasta, jonka ajaa kahden kohdan välinen jännite.

## Kertaa tarvittaessa {Kertaa}

- Varaus ja Coulombin laki: [*Sähkövaraus ja Coulombin laki*](fy6-10.html). Kenttä ja levyt: [*Homogeeninen sähkökenttä*](fy6-11.html).
- Potentiaali, työ ja elektronivoltti: [*Potentiaalienergia ja potentiaali sähkökentässä*](fy6-12.html). Kapasitanssi ja energia: [*Kondensaattori ja sen energia*](fy6-13.html).
- Diodi, LED ja aurinkokenno: [*Puolijohteet, diodi, LED ja aurinkokenno*](fy6-14.html).
- Sulake, maadoitus ja vikavirtasuoja: [*Sähköturvallisuus kotona ja työssä*](fy6-15.html). Lataus ja kolmivaihesähkö: [*Soveltava luku: sähköauto ja kodin sähköjärjestelmä*](fy6-16.html).
