# Tasapaino, ympyräliike ja gravitaatio

> **Miksi** lautasantenni voidaan suunnata kerran ja jättää paikalleen, vaikka televisiosatelliitti kiertää Maata noin $3\,\text{km/s}$:n nopeudella?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvinen iltahämärä maaseudulla. Keskellä on punainen puutalo, jonka katolla on lunta ja ikkunoissa valoa. Talon päätyseinässä on lautasantenni, joka on suunnattu matalalle vasemmalle taivaalle. Antennista lähtee himmeä katkoviiva taivaalla olevaan televisiosatelliittiin, jolla on kaksi aurinkopaneelia. Satelliitti on taivaan poikki kulkevalla katkoviivakaarella. Taivaalla on tähtiä, taustalla metsän reuna ja edessä lumipenkkoja ja kuusia." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-ympyraliike-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

Tämän tunnin tehtävät alkavat samoin kuin mekaniikan tehtävät yleensä: **valitse kappale, piirrä voimakuvio ja kirjoita Newtonin toinen laki**. Tilanne kertoo, mikä kiihtyvyys on. Tasapainossa kappale ei etene eikä kierry, joten sekä voimien summa että momenttien summa ovat nolla. Tasaisessa ympyräliikkeessä kiihtyvyys osoittaa radan keskipisteeseen, joten myös voimien summa osoittaa sinne. Satelliittiin vaikuttaa vain gravitaatio, joten gravitaatiovoima on itse kokonaisvoima.

```pysahdy
Mihin suuntaan voimien summa osoittaa tasaisessa ympyräliikkeessä ja miksi?
---
Radan keskipisteeseen, koska kiihtyvyys osoittaa sinne ja kokonaisvoima on samansuuntainen kuin kiihtyvyys.
```

<svg data-fig="kartta" viewBox="0 0 380 870" role="img" aria-label="Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Piirrä ensin voimakuvio ja katso, mikä tehtävän tunnusmerkki sopii. Tanko pysyy paikallaan: myös momenttien summa on nolla. Ympyrärata: normaalikiihtyvyys on v toiseen jaettuna r:llä. Kulmanopeus annettu: ratanopeus on omega kertaa r. Mikä voima kaartaa rataa: voimien summa on massa kertaa normaalikiihtyvyys. Kaarre tasaisella tiellä: lepokitka kaartaa, ja kitkavoima on m v toiseen per r. Kaksi kappaletta vetää toisiaan: gravitaatiolaki, F g on gamma M m per r toiseen. Putoamiskiihtyvyys kysytään: paino on gravitaatiota, m g on gamma M m per r toiseen. Satelliitti kiertää: gravitaatio kaartaa rataa, gamma M m per r toiseen on m v toiseen per r." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="811" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{mistä tunnistan lain?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{voimakuvio ensin, sitten tunnusmerkki}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{tanko pysyy paikallaan}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="204" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{myös momentit}$</div></foreignObject>
  <rect x="262" y="142" width="100" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="266" y="144" width="92" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma M = 0$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{ympyrärata}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="188" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{normaalikiihtyvyys}$</div></foreignObject>
  <rect x="246" y="228" width="116" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="250" y="230" width="108" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$a_\text{n} = v^2/r$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kulmanopeus annettu}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="204" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{ratanopeus}$</div></foreignObject>
  <rect x="262" y="314" width="100" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="266" y="316" width="92" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$v = \omega r$</div></foreignObject>
  <line x1="14" y1="392" x2="30" y2="392" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{mikä voima kaartaa rataa?}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="180" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{voimien summa}$</div></foreignObject>
  <rect x="238" y="400" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="402" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma F = ma_\text{n}$</div></foreignObject>
  <line x1="14" y1="478" x2="30" y2="478" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="442" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="452.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kaarre tasaisella tiellä}$</div></foreignObject>
  <line x1="40" y1="482" x2="362" y2="482" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="487" width="180" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{lepokitka kaartaa}$</div></foreignObject>
  <rect x="238" y="486" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="488" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F = mv^2/r$</div></foreignObject>
  <line x1="14" y1="579" x2="30" y2="579" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="528" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="538.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kaksi kappaletta vetää toisiaan}$</div></foreignObject>
  <line x1="40" y1="568" x2="362" y2="568" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="573" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{gravitaatiolaki}$</div></foreignObject>
  <rect x="192" y="601" width="170" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="196" y="604" width="162" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$F_\text{g} = \gamma Mm/r^2$</div></foreignObject>
  <line x1="14" y1="695" x2="30" y2="695" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="644" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="654.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{putoamiskiihtyvyys kysytään}$</div></foreignObject>
  <line x1="40" y1="684" x2="362" y2="684" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="689" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{paino on gravitaatiota}$</div></foreignObject>
  <rect x="192" y="717" width="170" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="196" y="720" width="162" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$mg = \gamma Mm/r^2$</div></foreignObject>
  <line x1="14" y1="811" x2="30" y2="811" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="760" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="770.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{satelliitti kiertää}$</div></foreignObject>
  <line x1="40" y1="800" x2="362" y2="800" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="805" width="304" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{gravitaatio kaartaa}$</div></foreignObject>
  <rect x="162" y="833" width="200" height="26" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="166" y="836" width="192" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\gamma Mm/r^2 = mv^2/r$</div></foreignObject>
</svg>

Alun kysymys ratkeaa samalla tavalla. Satelliittiin vaikuttaa vain Maan gravitaatiovoima, ja se antaa satelliitille normaalikiihtyvyyden. Mitä kauempana satelliitti kiertää, sitä pidempi on sen kiertoaika. Geostationaarinen rata on päiväntasaajan yläpuolella juuri sillä etäisyydellä, jolla kiertoaika on sama kuin Maan pyörähdysaika $23\,\text{h}\;56\,\text{min}$. Kiertoajasta saadaan radan säteeksi $r \approx 42\,200\,\text{km}$ eli noin $35\,800\,\text{km}$ maanpinnan yläpuolella, ja ratanopeudeksi $v = \tfrac{2\pi r}{T} \approx 3{,}07\,\text{km/s}$. Satelliitti ja antenni kiertävät Maan akselin ympäri samassa ajassa ja samaan suuntaan, joten antennista katsottuna satelliitti pysyy paikallaan.

<svg data-fig="geo" viewBox="0 0 600 600" role="img" aria-label="Kaavakuva pohjoisnavan suunnasta, säteet mittakaavassa. Keskellä Maa, jonka ympäri kulkee katkoviivalla geostationaarinen rata. Radan säde r on noin 42 200 km eli noin 6,6 Maan sädettä. Maa pyörii ja satelliitti kiertää samaan suuntaan, vastapäivään, ja kumpikin tekee kierroksen ajassa T = 23 h 56 min. Satelliitin sininen nopeusnuoli on radan tangentin suuntainen ja punainen gravitaatiovoiman nuoli osoittaa Maan keskipisteeseen. Maan pinnalla on antennin paikka, josta katkoviiva kulkee satelliittiin. Kuuden tunnin kuluttua antenni ja satelliitti ovat kumpikin kiertyneet neljänneskierroksen: himmeästi piirretty uusi näkösuora on sama viiva kiertyneenä." style="max-width:100%;font-size:26px">
  <image href="pics/fy9/fy9-ympyraliike-geo.webp" x="0" y="0" width="600" height="600" preserveAspectRatio="none"/>
  <foreignObject x="166.5" y="57.5" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="297.5" y="155" width="35" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="326" y="243.5" width="103" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px">$\text{antenni}$</div></foreignObject>
  <foreignObject x="78" y="262.5" width="157" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px;color:#6b7480">$\text{6 h myöhemmin}$</div></foreignObject>
  <foreignObject x="416" y="414.5" width="103" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:26px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$r \approx 6{,}6\,R$</span></div></foreignObject>
  <foreignObject x="208" y="10.5" width="184" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px">$T = 23\,\text{h}\;56\,\text{min}$</div></foreignObject>
  <foreignObject x="161" y="564.5" width="278" height="31" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:26px;color:#6b7480">$\text{radan säde } r \approx 42\,200\,\text{km}$</div></foreignObject>
</svg>

## Kaava: Tasapaino, ympyräliike ja gravitaatio

### Momentti ja tasapaino

```kaavat
voiman momentti :: M = Fr
\Sigma\overline{F} = \overline{0}
\Sigma M = 0
```

missä $M$ on voiman momentti ($\text{Nm}$), $F$ voiman suuruus ($\text{N}$) ja $r$ voiman varsi ($\text{m}$) eli kiertoakselin kohtisuora etäisyys voiman vaikutussuorasta. Jos voima muodostaa kulman $\alpha$ akselista vaikutuskohtaan kulkevan suoran kanssa ja vaikutuskohta on etäisyydellä $d$, varsi on $r = d\sin\alpha$. Vastapäivään kiertävä momentti on positiivinen. Levossa olevan kappaleen momenttiehto pätee minkä tahansa pisteen suhteen, joten momenttipisteeksi kannattaa valita tuntemattoman voiman vaikutuspiste. Paino vaikuttaa painopisteessä.

<svg data-fig="tilanteet" viewBox="0 0 380 690" role="img" aria-label="Kolme voimakuviota allekkain. Ylimpänä tasa-aineinen lankku levossa kahden tuen varassa suorakulmiona: paino G lähtee keskipisteestä alas, ja tukivoimat N 1 ja N 2 alapinnasta ylös. Tuki 2 on lähempänä keskipistettä, ja sen tukivoima on kaksi kertaa niin pitkä kuin N 1; yhdessä ne ovat painon pituiset. Ehdot: voimien summa ja momenttien summa ovat nolla. Keskellä auto nyppylän huipulla suorakulmiona: paino G alas ja tukivoima N ylös, painoa lyhyempänä. Auton vieressä sininen nopeusnuoli eteenpäin ja oranssi kiihtyvyysnuoli alas kohti kaaren keskipistettä. Ehto: G miinus N on m v toiseen jaettuna r:llä. Alimpana satelliitti suorakulmiona: ainoa voima on Maan gravitaatiovoima F alas kohti Maan keskipistettä. Vieressä nopeusnuoli eteenpäin ja kiihtyvyysnuoli alas. Ehto: gravitaatiovoima on m v toiseen jaettuna r:llä." style="max-width:100%;font-size:20px">
  <image href="pics/fy9/fy9-ympyraliike-tilanteet.webp" x="0" y="0" width="380" height="679.2" preserveAspectRatio="none"/>
  <foreignObject x="12" y="8" width="271" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{lankku levossa: } \Sigma\overline{F} = \overline{0},\ \Sigma M = 0$</div></foreignObject>
  <foreignObject x="157.5" y="194" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="90.5" y="65" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{N}_{1}$</div></foreignObject>
  <foreignObject x="234.5" y="45" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{N}_{2}$</div></foreignObject>
  <foreignObject x="12" y="232" width="237" height="48" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{nyppylän huippu: } G - N = m\dfrac{v^2}{r}$</div></foreignObject>
  <foreignObject x="291.5" y="330" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="269.5" y="398" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="115.5" y="430" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="161.5" y="304" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="12" y="466" width="195" height="48" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{satelliitti: } \gamma\dfrac{Mm}{r^2} = m\dfrac{v^2}{r}$</div></foreignObject>
  <foreignObject x="265.5" y="550" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="243.5" y="612" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="115.5" y="620" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="308.5" y="634" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{Maa}$</div></foreignObject>
</svg>

### Tasainen ympyräliike

```kaavat
ratanopeus :: v = \omega r
normaalikiihtyvyys :: a_\text{n} = \frac{v^2}{r} = \omega^2 r
```

missä $v$ on ratanopeus ($\text{m/s}$), $r$ radan säde ($\text{m}$), $\omega = \tfrac{2\pi}{T} = 2\pi f$ kulmanopeus ($\text{rad/s}$), $T$ kierrosaika ($\text{s}$) ja $f = \tfrac{1}{T}$ kierrostaajuus ($\tfrac{1}{\text{s}}$), joten $v = \tfrac{2\pi r}{T} = 2\pi r f$, ja $a_\text{n}$ normaalikiihtyvyys ($\text{m/s}^2$). Tasaisessa ympyräliikkeessä vauhti on vakio. Nopeus on radan tangentin suuntainen, ja normaalikiihtyvyys osoittaa radan keskipisteeseen.

```pysahdy
Mihin suuntaan nopeus osoittaa tasaisessa ympyräliikkeessä ja mihin normaalikiihtyvyys?
---
Nopeus on radan tangentin suuntainen ja normaalikiihtyvyys osoittaa radan keskipisteeseen.
```

Newtonin 2. lain mukaan kappaleeseen vaikuttava kokonaisvoima $\Sigma F$ ($\text{N}$) antaa sille normaalikiihtyvyyden, joten kokonaisvoima osoittaa keskipisteeseen. Normaalikiihtyvyys $a_\text{n} = \tfrac{v^2}{r}$ pätee myös hetkellisesti, kun vauhti muuttuu: radan ylimmässä ja alimmassa kohdassa tangentin suuntaista voimaa ei ole. Liikeyhtälössä keskipisteeseen osoittavat voimat ovat positiivisia, ja kohtisuoraan ratatasoa vastaan voimien summa on nolla.

```johda
Kappale, jonka massa on $m$, on tasaisessa ympyräliikkeessä vauhdilla $v$ radalla, jonka säde on $r$. Johda Newtonin 2. laista ja normaalikiihtyvyydestä kappaleeseen vaikuttava kokonaisvoima $\Sigma F$.
---
Newtonin 2. laki $\Sigma\overline{F} = m\overline{a}$ pätee myös ympyräliikkeessä. Tasaisessa ympyräliikkeessä kiihtyvyys on normaalikiihtyvyys $a_\text{n} = \tfrac{v^2}{r}$, joka osoittaa radan keskipisteeseen. Kokonaisvoima osoittaa siis keskipisteeseen, ja sen suuruus on

$$\Sigma F = ma_\text{n} = m\frac{v^2}{r}$$
```

<svg data-fig="kaarre" viewBox="0 0 380 280" role="img" aria-label="Voimakuvio, ei lukuarvoja: auto vaakasuoran tien kaarteessa takaa katsottuna suorakulmiona. Kaarteen keskipiste on vasemmalla. Paino G lähtee keskipisteestä alas, ja yhtä pitkä tukivoima N lähtee tien pinnasta ylös. Tien pinta on katkoviiva. Kitkavoima F myy lähtee auton vasemmasta alakulmasta vasemmalle tien suuntaisesti, kohti kaarteen keskipistettä. Auton vieressä oranssi kiihtyvyysnuoli osoittaa vasemmalle kohti keskipistettä. Nopeus on poispäin katsojasta, piirretty ympyränä, jonka sisällä on risti." style="max-width:100%;font-size:20px">
  <line x1="16" y1="206" x2="364" y2="206" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="12" y="23" width="186" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:18px;color:#6b7480">$\leftarrow \text{kaarteen keskipiste}$</div></foreignObject>
  <line x1="119" y1="142" x2="51" y2="142" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M62,135.5 L49,142 L62,148.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="32.5" y="108" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <rect x="135" y="130" width="130" height="76" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="200" y1="168" x2="200" y2="231" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M200,248 L192,230 L208,230 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="165.5" y="240" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="232" y1="206" x2="232" y2="143" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M232,126 L240,144 L224,144 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="237.5" y="100" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="135" y1="206" x2="94" y2="206" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M77,206 L95,198 L95,214 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="55.5" y="218" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <circle cx="305" cy="148" r="13" fill="#ffffff" stroke="#1971c2" stroke-width="2.5"/>
  <line x1="296" y1="139" x2="314" y2="157" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="296" y1="157" x2="314" y2="139" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="327" y="136" width="29" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#1971c2">$\overline{v}$</div></foreignObject>
</svg>

```johda
Auto, jonka massa on $m$, ajaa vauhdilla $v$ vaakasuoran tien kaarteessa, jonka säde on $r$. Tien kitka antaa autolle keskeisvoiman. Johda, kuinka suuri kitkavoima tarvitaan ja millä suurimmalla vauhdilla auto vielä pysyy tiellä, kun lepokitkakerroin on $\mu_0$.
---
Kaarteessa autoon vaikuttavat paino $G = mg$, tien tukivoima $N$ ja tien kitkavoima $F_\mu$ (kuva). Pystysuunnassa kiihtyvyyttä ei ole, joten $N = mg$. Vaakasuunnassa ainoa voima on kitka, joten se on kokonaisvoima. Tasaisessa ympyräliikkeessä kokonaisvoima on $\Sigma F = m\tfrac{v^2}{r}$, joten

$$F_\mu = m\frac{v^2}{r}$$

Renkaat eivät liu'u sivuttain, joten kitka on lepokitkaa. Se on enintään $\mu_0 N = \mu_0 mg$. Auto pysyy tiellä, kun

$$m\frac{v^2}{r} \le \mu_0 mg \quad\Rightarrow\quad v \le \sqrt{\mu_0 g r}$$

Massa supistuu, joten suurin vauhti ei riipu auton massasta.
```

### Gravitaatio ja satelliitit

```kaavat
Newtonin gravitaatiolaki :: F_\text{g} = \gamma\frac{m_1 m_2}{r^2}
```

missä $$
\gamma = 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}
$$ on gravitaatiovakio, $F_\text{g}$ gravitaatiovoiman suuruus ($\text{N}$), $m_1$ ja $m_2$ kappaleiden massat ($\text{kg}$) ja $r$ etäisyys keskipisteiden välillä ($\text{m}$). Laki pätee pistemäisille ja pallosymmetrisille kappaleille. Keskuskappaleen, jonka massa on $M$ ($\text{kg}$), gravitaatiokentän voimakkuus $g$ ($\text{N/kg}$ eli $\text{m/s}^2$) on gravitaatiovoima kappaleen massaa kohden; Maan pinnalla se on putoamiskiihtyvyys.

```pysahdy
Miten gravitaatiovoiman suuruus muuttuu, kun kappaleiden keskipisteiden etäisyys $r$ kaksinkertaistuu?
---
Se pienenee neljäsosaan, koska $F_\text{g}$ on verrannollinen suureeseen $\tfrac{1}{r^2}$.
```

```johda
Kappale, jonka massa on $m$, on etäisyydellä $r$ keskuskappaleen keskipisteestä, ja keskuskappaleen massa on $M$. Johda gravitaatiokentän voimakkuus $g$ eli putoamiskiihtyvyys tällä etäisyydellä.
---
Newtonin gravitaatiolain mukaan kappaleeseen vaikuttaa gravitaatiovoima

$$F_\text{g} = \gamma\frac{Mm}{r^2}$$

Tämä voima on kappaleeseen vaikuttava painovoima $G = mg$, kun keskuskappaleen pyörimistä ei oteta huomioon. Merkitään voimat yhtä suuriksi:

$$mg = \gamma\frac{Mm}{r^2}$$

Kappaleen massa $m$ supistuu:

$$g = \gamma\frac{M}{r^2}$$

Kentän voimakkuus ei riipu kappaleen massasta, joten kaikki kappaleet putoavat samalla kiihtyvyydellä. Ilmanvastus jätetään huomioimatta. Maan pinnalla $r = R$, ja kauempana $g$ pienenee etäisyyden neliön mukaan.
```

Satelliitti kiertää keskuskappaletta ympyräradalla, jonka säde on $r$, ratanopeudella $v$ ($\text{m/s}$). Siihen vaikuttaa vain gravitaatiovoima, ja se antaa satelliitille normaalikiihtyvyyden. Maan satelliitille $r = R + h$, missä $R = 6371\,\text{km}$ ja $h$ korkeus maanpinnasta, ja kiertoaika on $T = \tfrac{2\pi r}{v}$.

```johda
Satelliitti, jonka massa on $m$, kiertää ympyräradalla keskuskappaletta, jonka massa on $M$. Radan säde on $r$. Johda satelliitin ratanopeus $v$.
---
Satelliittiin vaikuttaa vain gravitaatiovoima, joten se on kokonaisvoima ja osoittaa radan keskipisteeseen. Newtonin 2. lain mukaan se antaa satelliitille normaalikiihtyvyyden $a_\text{n} = \tfrac{v^2}{r}$. Kun gravitaatiovoima kirjoitetaan Newtonin gravitaatiolain mukaan, saadaan

$$\gamma\frac{Mm}{r^2} = m\frac{v^2}{r}$$

Satelliitin massa $m$ supistuu. Kerrotaan yhtälö säteellä $r$:

$$v^2 = \frac{\gamma M}{r}$$

Ratanopeus on positiivinen, joten

$$v = \sqrt{\frac{\gamma M}{r}}$$

Ratanopeus ei riipu satelliitin massasta, ja se on sitä pienempi, mitä kauempana rata on. Tulos pätee, kun keskuskappale on paljon satelliittia massiivisempi, jolloin keskuskappale pysyy paikallaan.
```

## Yleisiä virheitä {Virheet}

- **Etäisyys varren paikalla.** Vinon voiman momentti on $Fd\sin\alpha$, ei $Fd$.
- **Kauempi tuki kantaa enemmän.** Asia on päinvastoin: painopistettä lähempänä oleva tuki kantaa enemmän.
- **Keskipakoisvoima voimakuvioon.** Ulospäin vaikuttavaa voimaa ei ole. Keskeisvoima on todellisten voimien summa, eikä sitä piirretä omana nuolenaan.
- **Halkaisija ja kierrokset minuutissa.** Kaavaan sijoitetaan säde, ja $\tfrac{1}{\text{min}}$ muunnetaan: $1\,\text{min} = 60\,\text{s}$.
- **Korkeus säteen paikalla.** Radan säde mitataan Maan keskipisteestä: $r = R + h$.
- **Painottomuus on painovoiman puuttumista.** Avaruusasemalla gravitaatio vaikuttaa, mutta asema ja astronautti putoavat vapaasti yhdessä, joten tukivoima on nolla.

## Kertaa tarvittaessa {Kertaa}

- Voiman varsi ja kiertosuunta: [*Momentti: voiman kiertävä vaikutus*](fy5-1.html). Tasapainoehdot ja painopiste: [*Kappaleen tasapaino: voimat ja momentit*](fy5-2.html).
- Kierrosaika ja ratanopeus: [*Ympyrärata: jaksonaika ja ratanopeus*](fy5-3.html). Normaalikiihtyvyys ja liikeyhtälö: [*Normaalikiihtyvyys ja ympyräliikkeen liikeyhtälö*](fy5-4.html).
- Gravitaatiolaki ja kentän voimakkuus: [*Kappaleiden välinen gravitaatiovoima*](fy5-5.html). Ratanopeus, kiertoaika ja painottomuus: [*Satelliitit ja planeetat ympyräradalla*](fy5-6.html).
