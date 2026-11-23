# Paine, kaasut ja lämpövoimakone

> **Miksi** auton renkaiden paine pitää tarkistaa, kun pakkanen kiristyy, vaikka renkaista ei ole vuotanut ilmaa?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: pakkasaamu pihalla. Vasemmalla autotalli, jonka ovi on auki ja jonka sisällä palaa lämmin valo; seinällä roikkuu paineilmaletku. Pihalla seisoo auto, joka on ollut ulkona koko yön: sen katolla ja ikkunoissa on huurretta. Autotallin ulkoseinän lämpömittarin punainen pylväs on matalalla. Taustalla lumiset kuuset ja vaalea aamutaivas." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-kaasut-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

Tämän tunnin tehtävät kiertyvät yhden suureen ympärille: **paine on pintaa vastaan kohtisuora voima jaettuna pinta-alalla**. Nesteessä paine syntyy yläpuolisen nesteen painosta, joten se kasvaa syvyyden mukana. Kaasussa se syntyy hiukkasten törmäyksistä astian seinämiin, joten se riippuu kaasun määrästä, tilavuudesta ja lämpötilasta. Kun kaasun paine työntää mäntää, kaasu tekee työtä, ja lämpövoimakone muuttaa näin osan lämmöstä työksi.

Kokeen kaasutehtävissä tarvitaan kaksi tarkistusta ennen lukuja. **Lämpötila kelvineinä**, koska kaasulait ovat verrannollisuuksia, jotka alkavat absoluuttisesta nollapisteestä. **Kokonaispaine**, koska painemittari näyttää yleensä vain ylipaineen, ja kaasun hiukkaset tuottavat koko paineen.

<svg data-fig="kartta" viewBox="0 0 380 956" role="img" aria-label="Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Aloita tilanteesta ja katso, mikä tehtävän tunnusmerkki sopii. Voima jakautuu pinta-alalle: paine on voima jaettuna pinta-alalla. Syvyys nesteessä: nesteen paine on tiheys kertaa putoamiskiihtyvyys kertaa syvyys. Syvyys ja ilmanpaine: kokonaispaine on pinnan paine, yleensä ilmanpaine, plus nesteen paine. Ainemäärä tiedossa: käytä tilanyhtälöä, paine kertaa tilavuus on ainemäärä kertaa kaasuvakio kertaa lämpötila. Tila muuttuu, ainemäärä ei: kirjoita kaksi tilaa, paineen ja tilavuuden tulo jaettuna lämpötilalla on sama alussa ja lopussa. Lämpötila celsiusasteina: muunna kelvineiksi lisäämällä 273,15. Paine vakio, tilavuus muuttuu: työn suuruus on paine kertaa tilavuuden muutoksen suuruus. Sisäenergia muuttuu: lämpöopin ensimmäinen pääsääntö, sisäenergian muutos on lämpö plus työ. Kone ottaa lämmön ja tekee työn: lämpövoimakoneen hyötysuhde on työ jaettuna otetulla lämmöllä." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="912" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{mistä tunnistan lain?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{tilanne ensin, sitten tunnusmerkki}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{voima jakautuu pinta-alalle}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{paine}$</div></foreignObject>
  <rect x="238" y="142" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="144" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$p = F/A$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{syvyys nesteessä}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{nesteen paine}$</div></foreignObject>
  <rect x="238" y="228" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="230" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$p = \rho g h$</div></foreignObject>
  <line x1="14" y1="321" x2="30" y2="321" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{syvyys ja ilmanpaine}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{kokonaispaine}$</div></foreignObject>
  <rect x="192" y="344" width="170" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="196" y="346" width="162" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$p = p_0 + \rho g h$</div></foreignObject>
  <line x1="14" y1="422" x2="30" y2="422" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="386" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="396.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{ainemäärä (mol) tiedossa}$</div></foreignObject>
  <line x1="40" y1="426" x2="362" y2="426" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="431" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{tilanyhtälö}$</div></foreignObject>
  <rect x="238" y="430" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="432" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$pV = nRT$</div></foreignObject>
  <line x1="14" y1="523" x2="30" y2="523" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="472" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="482.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{tila muuttuu, ainemäärä ei}$</div></foreignObject>
  <line x1="40" y1="512" x2="362" y2="512" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="517" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{kaksi tilaa}$</div></foreignObject>
  <rect x="182" y="546" width="180" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="186" y="548" width="172" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$p_1V_1/T_1 = p_2V_2/T_2$</div></foreignObject>
  <line x1="14" y1="639" x2="30" y2="639" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="588" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="598.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{lämpötila celsiusasteina}$</div></foreignObject>
  <line x1="40" y1="628" x2="362" y2="628" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="633" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{muunna kelvineiksi}$</div></foreignObject>
  <rect x="172" y="662" width="190" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="176" y="664" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$T = \theta + 273{,}15\,\text{K}$</div></foreignObject>
  <line x1="14" y1="740" x2="30" y2="740" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="704" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="714.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{paine vakio, tilavuus muuttuu}$</div></foreignObject>
  <line x1="40" y1="744" x2="362" y2="744" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="749" width="176" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{työn suuruus}$</div></foreignObject>
  <rect x="232" y="748" width="130" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="236" y="750" width="122" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$W = p\Delta V$</div></foreignObject>
  <line x1="14" y1="826" x2="30" y2="826" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="790" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="800.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{sisäenergia muuttuu}$</div></foreignObject>
  <line x1="40" y1="830" x2="362" y2="830" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="835" width="176" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{1. pääsääntö}$</div></foreignObject>
  <rect x="232" y="834" width="130" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="236" y="836" width="122" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Delta U = Q + W$</div></foreignObject>
  <line x1="14" y1="912" x2="30" y2="912" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="876" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="886.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kone ottaa lämmön, tekee työn}$</div></foreignObject>
  <line x1="40" y1="916" x2="362" y2="916" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="921" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{hyötysuhde}$</div></foreignObject>
  <rect x="238" y="920" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="922" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\eta = W/Q_1$</div></foreignObject>
</svg>

Alun kysymys ratkeaa näillä kahdella tarkistuksella. Lämpimässä autotallissa ($+20\,{}^\circ\text{C}$) mittari näytti ylipainetta $230\,\text{kPa}$, joten kokonaispaine oli $101\,\text{kPa} + 230\,\text{kPa} = 331\,\text{kPa}$. Kun renkaan tilavuus pysyy lähes samana, kokonaispaine on verrannollinen kelvinlämpötilaan: pakkasyön ($-20\,{}^\circ\text{C}$) jälkeen se on $$
\begin{aligned}
&331\,\text{kPa} \cdot 253\,\text{K} : 293\,\text{K} \\
&\approx 286\,\text{kPa}
\end{aligned}
$$. Mittari näyttää enää noin $185\,\text{kPa}$, vaikka ilmaa ei ole vuotanut.

<svg data-fig="rengas" viewBox="0 0 480 330" role="img" aria-label="Pylväskuvio mittakaavassa: renkaan ilman kokonaispaine kahdessa lämpötilassa. Kumpikin vaakapylväs on jaettu kahteen osaan: ilmanpaine 101 kPa ja mittarin näyttämä ylipaine. Lämpimässä autotallissa, +20 °C, ylipaine on 230 kPa ja kokonaispaine 331 kPa. Pakkasyön jälkeen, −20 °C, kokonaispaine on 286 kPa ja ylipaine 185 kPa. Kokonaispaine on pienentynyt kelvinlämpötilan suhteessa, mutta mittarin lukema on pienentynyt 45 kPa eli noin viidenneksen." style="max-width:100%;font-size:20px">
  <line x1="140" y1="40" x2="140" y2="268" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="40" x2="240" y2="268" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="340" y1="40" x2="340" y2="268" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="50" y="26" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#c92a2a">$+20\,{}^\circ\text{C}$</div></foreignObject>
  <rect x="40" y="60" width="101" height="46" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <rect x="141" y="60" width="230" height="46" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="76" y="71" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$p_0$</div></foreignObject>
  <foreignObject x="221" y="71" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\Delta p = 230$</div></foreignObject>
  <foreignObject x="379" y="71" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$331\,\text{kPa}$</div></foreignObject>
  <foreignObject x="50" y="138" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#1971c2">$-20\,{}^\circ\text{C}$</div></foreignObject>
  <rect x="40" y="172" width="101" height="46" fill="#f1dfb5" stroke="#1f2933" stroke-width="2"/>
  <rect x="141" y="172" width="185" height="46" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="76" y="183" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$p_0$</div></foreignObject>
  <foreignObject x="198.5" y="183" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\Delta p = 185$</div></foreignObject>
  <foreignObject x="334" y="183" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$286\,\text{kPa}$</div></foreignObject>
  <line x1="39" y1="268" x2="392" y2="268" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M404,268 L391,274 L391,262 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="40" y1="269" x2="40" y2="40" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="140" y1="268" x2="140" y2="275" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="120.5" y="280" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$100$</div></foreignObject>
  <line x1="240" y1="268" x2="240" y2="275" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220.5" y="280" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$200$</div></foreignObject>
  <line x1="340" y1="268" x2="340" y2="275" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="320.5" y="280" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$300$</div></foreignObject>
  <foreignObject x="16" y="280" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="410" y="256" width="74" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$p\ (\text{kPa})$</div></foreignObject>
</svg>

```pysahdy
Miksi kaasun paineen laskussa ei käytetä suoraan mittarin lukemaa $230\,\text{kPa}$?
---
Mittari näyttää vain ylipaineen, mutta kaasun hiukkaset tuottavat koko paineen. Siksi lisätään ilmanpaine: $101\,\text{kPa} + 230\,\text{kPa} = 331\,\text{kPa}$.
```

## Kaava: Paine, kaasut ja lämpövoimakone

### Paine ja nesteen paine

```kaavat
voiman aiheuttama paine :: p = \frac{F}{A}
```

missä $p$ on paine (Pa), $F$ pintaa vastaan kohtisuora voima (N) ja $A$ pinta-ala (m²). Levossa olevassa nesteessä syvyydellä $h$

```kaavat
hydrostaattinen paine :: p = \rho g h
```

missä $\rho$ on nesteen tiheys (kg/m³) ja $g = 9{,}81\,\text{m/s}^2$. Hydrostaattinen paine on ylipaine, ja se riippuu vain syvyydestä ja tiheydestä, ei astian muodosta. Kokonaispaine syvyydellä $h$ on $p_0 + \rho g h$, missä $p_0$ on paine pinnalla, yleensä ilmanpaine noin $101\,\text{kPa}$. Paineen aiheuttama voima on aina kohtisuorassa pintaa vastaan.

### Kaasun tila

```kaavat
ideaalikaasun tilanyhtälö :: pV = nRT
```

missä $V$ on tilavuus (m³), $n$ ainemäärä (mol), $R = 8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}}$ ja $T$ lämpötila kelvineinä. Ainemäärä saadaan massasta, $n = m/M$, missä $M$ on moolimassa. Yhtälö pätee harvalle kaasulle, kun paine ei ole kovin suuri eikä lämpötila kovin matala. Kun kaasun määrä pysyy samana,

```kaavat
tilanyhtälö vakioainemäärälle :: \frac{pV}{T} = \text{vakio}
```

eli kahdessa tilassa $\tfrac{p_1 V_1}{T_1} = \tfrac{p_2 V_2}{T_2}$. Siitä saadaan erikoistapaukset: vakiolämpötilassa Boylen laki $p_1V_1 = p_2V_2$, vakiopaineessa $V \propto T$ ja vakiotilavuudessa $p \propto T$. Kelvinlämpötila on

```pysahdy
Miksi suoran jatkaminen nollapaineeseen on vain kaasumallin ennuste?
---
Todellinen kaasu tiivistyy nesteeksi ennen kuin lämpötila ehtii sinne, joten suoran jatkaminen nollaan on kaasumallin ennuste.
```

```latex
T = \theta + 273{,}15\,\text{K}
```

missä $\theta$ on celsiuslämpötilan lukuarvo. Absoluuttinen nollapiste saadaan kokeessa jatkamalla $(\theta, p)$- tai $(\theta, V)$-suoraa nollaan. Se on mallin ennuste: todellinen kaasu tiivistyy nesteeksi ennen sitä.

### Kaasun työ ja lämpövoimakone

Vakiopaineessa laajeneva kaasu tekee työn, ja puristettuun kaasuun tehdään työ

```kaavat
kaasun tekemä laajenemistyö / kaasuun tehty puristustyö :: W = p\Delta V
```

missä $\Delta V$ on tilavuuden muutoksen suuruus (m³); työ on ($V$, $p$)-kuvaajan alle jäävä pinta-ala. Kaasun sisäenergia muuttuu ensimmäisen pääsäännön mukaan

```kaavat
lämpöopin 1. pääsääntö :: \Delta U = Q + W
```

missä $Q$ on kaasuun siirtynyt lämpö (J) ja $W$ kaasuun tehty työ (J). Puristuksessa $W = p\Delta V$ on positiivinen. Laajeneva kaasu tekee työn $p\Delta V$ itse, joten silloin $W = -p\Delta V$ ja sisäenergia pienenee tämän verran.

Lämpövoimakone ottaa kierroksessa kuumasta lähteestä lämmön $Q_1$ ($\text{J}$), tekee työn $W$ ($\text{J}$) ja luovuttaa lämmön $Q_2$ ($\text{J}$) kylmempään ympäristöön. Kierroksen lopussa koneen kaasu on samassa tilassa kuin alussa. Koneen hyötysuhde on

```kaavat
lämpövoimakoneen hyötysuhde :: \eta = \frac{W}{Q_1}
```

```pysahdy
Miksi lämpövoimakoneen hyötysuhde on aina alle $100\,\%$?
---
Osa otetusta lämmöstä $Q_1$ on luovutettava kylmempään ympäristöön lämpönä $Q_2$, joten työ $W$ on pienempi kuin $Q_1$.
```

Osa lämmöstä on aina luovutettava kylmempään, joten lämpövoimakoneen hyötysuhde jää selvästi alle $100\,\%$:n. Mitä pienempi lämpötilaero $T_1 - T_2$ on kuuman lähteen lämpötilaan $T_1$ nähden, sitä pienemmän osan lämmöstä kone voi muuttaa työksi. Voimalaitoksessa sama lasketaan tehoista: sähköteho jaettuna polttoaineteholla.

<svg data-fig="kone" viewBox="0 0 420 470" role="img" aria-label="Lämpövoimakoneen energiavirrat yhden kierroksen aikana, nuolten leveydet mittakaavassa. Ylhäällä kuuma lähde, jonka lämpötila on T1. Siitä tulee alas koneeseen leveä lämpönuoli Q1 = 1000 J. Koneesta lähtee oikealle kapea vihreä nuoli, työ W = 350 J, ja alas kylmempään ympäristöön, jonka lämpötila on T2, lämpönuoli Q2 = 650 J. Lähtevät nuolet ovat yhteensä yhtä leveät kuin tuleva nuoli." style="max-width:100%;font-size:20px">
  <image href="pics/fy9/fy9-kaasut-kone.webp" x="0" y="0" width="420" height="469" preserveAspectRatio="none"/>
  <foreignObject x="143.5" y="31" width="133" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{kuuma lähde } T_1$</div></foreignObject>
  <foreignObject x="222" y="120" width="102" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#e8590c">$Q_1 = 1000\,\text{J}$</div></foreignObject>
  <foreignObject x="125" y="226" width="50" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{kone}$</div></foreignObject>
  <foreignObject x="187" y="328" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#e8590c">$Q_2 = 650\,\text{J}$</div></foreignObject>
  <foreignObject x="230" y="188" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#2b8a3e">$W = 350\,\text{J}$</div></foreignObject>
  <foreignObject x="107" y="413" width="206" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{kylmempi ympäristö } T_2$</div></foreignObject>
</svg>

```johda
Lämpövoimakone ottaa kierroksessa kuumasta lähteestä lämmön $Q_1$ ja luovuttaa kylmempään ympäristöön lämmön $Q_2$. Johda työ $W$, jonka kone tekee yhden kierroksen aikana, lämpöjen $Q_1$ ja $Q_2$ avulla.
---
Sovelletaan lämpöopin 1. pääsääntöä $\Delta U = Q + W$ koneen kaasuun yhden kierroksen ajalta. Kierroksen lopussa kaasu on samassa tilassa kuin alussa, joten sen sisäenergia ei muutu: $\Delta U = 0$.

Kaasuun tulee kierroksessa lämpö $Q_1$, ja siitä lähtee lämpö $Q_2$. Kaasuun siirtynyt lämpö on siis

$$Q = Q_1 - Q_2$$

Pääsäännössä $W$ on kaasuun tehty työ. Kone tekee itse työn $W$ ympäristöönsä, joten kaasuun tehty työ on $-W$, samoin kuin laajenemisessa $-p\Delta V$. Sijoitetaan pääsääntöön:

$$0 = (Q_1 - Q_2) + (-W)$$

Ratkaistaan koneen työ:

$$W = Q_1 - Q_2$$

Tulos on energian säilyminen: kuvassa tuleva lämpö $Q_1$ jakautuu työksi $W$ ja luovutetuksi lämmöksi $Q_2$.
```

## Yleisiä virheitä {Virheet}

- **Celsiusasteet suhteessa.** $20\,{}^\circ\text{C}$:sta $40\,{}^\circ\text{C}$:seen lämmitetyn kaasun paine kasvaa vain noin $7\,\%$, ei kaksinkertaiseksi: $313\,\text{K} : 293\,\text{K} \approx 1{,}07$.
- **Ylipaine kaasulakiin.** Mittarin lukema ei ole kaasun paine. Lisää ilmanpaine ennen laskua ja vähennä se vasta lopuksi, jos kysytään mittarin lukemaa.
- **Yksiköt sekaisin.** Tilanyhtälössä paine on pascaleina ja tilavuus kuutiometreinä. Kilopascalit ja litrat käyvät yhdessä, koska $1\,\text{kPa} \cdot 1\,\textsf{l} = 1\,\text{J}$, mutta kilopascalit ja kuutiometrit antavat tuhatkertaisen virheen.
- **Paine ja voima sekaisin.** Sama voima pienelle alalle antaa suuren paineen. Paineesta saadaan voima vasta kertomalla alalla.
- **Imu vetää.** Imukuppi tai pilli ei vedä mitään: ulkoilman paine työntää, kun sisällä paine on pienempi.
- **Lämpövoimakone voisi muuttaa kaiken lämmön työksi.** Kitkan poistaminen ei auta: lämpöä $Q_2$ ei voi välttää.

## Kertaa tarvittaessa {Kertaa}

- Paine, ylipaine ja paine syvyydellä: [*Paine ja hydrostaattinen paine*](fy3-4.html).
- Boylen laki ja kaasujen tilanmuutokset: [*Kaasujen tilanmuutokset ja Boylen laki*](fy3-9.html). Ainemäärä ja tilanyhtälö: [*Ideaalikaasun tilanyhtälö*](fy3-10.html).
- Suoran jatkaminen nollaan ja sen epävarmuus: [*Absoluuttisen nollapisteen määrittäminen*](fy3-13.html).
- Kaasun työ, lämpövoimakone ja lämpöpumppu: [*Kaasun tekemä työ ja lämpövoimakone*](fy3-11.html). Voimalaitoksen hyötysuhde: [*Energiantuotanto ja voimalaitosten hyötysuhde*](fy3-15.html).
