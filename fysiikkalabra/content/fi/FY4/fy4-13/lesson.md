# Liikeyhtälö kytketyille kappaleille

> **Miksi** pöydän reunalta riippuva punnus putoaa hitaammin kuin vapaasti pudotessaan, kun se vetää langalla pöydällä olevaa kärryä mukanaan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: fysiikan luokan pöytä. Pöydällä on kärry, jonka päällä on kaksi metallipunnusta. Kärryyn sidottu lanka kulkee pöydän reunalla olevan väkipyörän yli, ja langan toisessa päässä roikkuu yksi metallipunnus. Pöydällä on mitta-asteikko ja sekuntikello, ja oppilas seisoo pöydän vieressä." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-13-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Usein kaksi kappaletta liikkuu yhdessä, koska ne on sidottu toisiinsa langalla. Kun lanka on kireä ja venymätön, kappaleet kulkevat saman matkan samassa ajassa, joten niiden kiihtyvyyksillä on sama suuruus $a$. Lanka välittää voiman kappaleelta toiselle: se vetää kumpaakin kappaletta itseään kohti. Tässä luvussa lanka on kevyt ja venymätön, väkipyörä kevyt ja kitkaton, ja pöydän kitka ja ilmanvastus jätetään huomiotta.

Kytketyt kappaleet käsitellään yksi kerrallaan. Kummallekin piirretään oma voimakuvio, jossa on vain siihen vaikuttavat voimat, ja kummallekin kirjoitetaan oma liikeyhtälö. Kuvan kärryyn vaikuttavat paino $\overline{G}_1$, pöydän tukivoima $\overline{N}$ ja langan jännitysvoima $\overline{T}_1$. Riippuvaan punnukseen vaikuttavat paino $\overline{G}_2$ ja langan jännitysvoima $\overline{T}_2$.

<svg data-fig="tilanne" viewBox="0 0 600 340" role="img" aria-label="Kaksi kappaletta ja niiden voimakuviot. Vasemmalla tilannekuva: pöydällä on kärry, ja siihen sidottu lanka kulkee pöydän reunan väkipyörän yli riippuvaan punnukseen. Kärryn yllä ovat ohuet nuolet: sininen nopeus oikealle ja lyhyempi oranssi kiihtyvyys oikealle. Oikealla ylhäällä kärryn voimakuvio, kärry suorakulmiona: paino G1 keskipisteestä alas, pöydän tukivoima N alapinnasta ylös ja yhtä pitkä kuin paino sekä langan jännitysvoima T1 oikealta reunalta oikealle. Oikealla alhaalla riippuvan punnuksen voimakuvio: paino G2 keskipisteestä alas ja langan jännitysvoima T2 yläpinnasta ylös. Nuoli T2 on lyhyempi kuin G2, ja nuolet T1 ja T2 ovat yhtä pitkät." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-13-tilanne.webp" x="1.2" y="0" width="597" height="345.8" preserveAspectRatio="none"/>
  <foreignObject x="77.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="147.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="127.5" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="35.5" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="210.8" y="234.8" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <foreignObject x="312" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio: kärry}$</div></foreignObject>
  <foreignObject x="312" y="187.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio: punnus}$</div></foreignObject>
  <foreignObject x="439.5" y="148.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{1}$</div></foreignObject>
  <foreignObject x="379.5" y="56.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="499" y="89.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{1}$</div></foreignObject>
  <foreignObject x="439.5" y="293" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{2}$</div></foreignObject>
  <foreignObject x="439.5" y="234" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{2}$</div></foreignObject>
</svg>

Lanka vetää kärryä voimalla $\overline{T}_1$ ja punnusta voimalla $\overline{T}_2$. Ne vaikuttavat eri kappaleisiin, joten ne ovat eri voimakuvioissa. Kevyt lanka ja kitkaton väkipyörä vain välittävät voiman ja kääntävät sen suunnan, joten voimien suuruudet ovat samat: $T_1 = T_2 = T$. Voimat $\overline{T}_1$ ja $\overline{T}_2$ eivät kuitenkaan ole voima ja vastavoima. Kun lanka vetää kärryä, kärry vetää lankaa takaisin yhtä suurella voimalla, ja se vaikuttaa lankaan eikä ole kärryn voimakuviossa.

```pysahdy
Lanka vetää kärryä voimalla $\overline{T}_1$ ja punnusta voimalla $\overline{T}_2$. Miksi nämä kaksi voimaa eivät ole voima ja vastavoima?
---
Ne kuuluvat kahteen eri vuorovaikutukseen: langan ja kärryn sekä langan ja punnuksen. Voiman $\overline{T}_1$ vastavoima on voima, jolla kärry vetää lankaa.
```

<figure class="unit-photo"><img src="pics/fy4/inclined-plane-apparatus.webp" alt="Vanha kaltevan tason koelaite: kaltevalla sauvalla oleva pieni rulla ja riippuva punnus on yhdistetty narulla väkipyörän yli."><figcaption>Kaltevan tason opetusväline 1900-luvun alusta Bremerhavenin koulumuseossa. Kaltevalla tasolla oleva rulla ja riippuva punnus on yhdistetty narulla, joka kulkee väkipyörän yli.</figcaption></figure>

Kun punnus kiihtyy alaspäin, langan jännitysvoima on pienempi kuin punnuksen paino. Kiihtyvyys on alas, joten punnuksen kokonaisvoima osoittaa alas ja $G_2 > T$. Jos $T$ olisi yhtä suuri kuin $G_2$, punnukseen vaikuttava kokonaisvoima olisi nolla eikä punnus lähtisi liikkeelle. Punnus laskee siksi hitaammin kuin vapaasti putoava kappale: kiihtyvyys $a = \tfrac{m_2 g}{m_1 + m_2}$ on pienempi kuin $g$, koska punnuksen paino kiihdyttää myös kärryä.

```pysahdy
Kärryn massa kasvaa mutta punnus pysyy samana. Miten punnuksen kiihtyvyys muuttuu ja miksi?
---
Se pienenee. Sama paino $m_2 g$ kiihdyttää nyt suurempaa kokonaismassaa $m_1 + m_2$.
```

## Kaava: Kytkettyjen kappaleiden liikeyhtälöt
Jokaiselle kappaleelle kirjoitetaan oma liikeyhtälö $\Sigma F = ma$. Positiivinen suunta valitaan kullekin kappaleelle erikseen kiihtyvyyden suuntaan: kärryllä oikealle ja punnuksella alas. Koska lanka on venymätön, kummankin kappaleen kiihtyvyydellä on sama suuruus $a$. Kärryn ja punnuksen yhtälöt ovat
```latex
\begin{aligned}
T &= m_1 a \\
m_2 g - T &= m_2 a
\end{aligned}
```
missä $m_1$ on kärryn massa (kg), $m_2$ punnuksen massa (kg), $T$ langan jännitysvoima (N), $a$ kiihtyvyys (m/s²) ja $g = 9{,}81\,\text{m/s}^2$. Tuntemattomia on kaksi, $a$ ja $T$, ja yhtälöitä kaksi.

Kun yhtälöt lasketaan puolittain yhteen, $T$ supistuu pois, koska langan jännitysvoima on kappaleiden välinen sisäinen voima. Näin saadaan kiihtyvyys ja sen jälkeen jännitysvoima:
```latex
\begin{aligned}
a &= \frac{m_2}{m_1 + m_2}\,g \\
T &= m_1 a = \frac{m_1 m_2}{m_1 + m_2}\,g
\end{aligned}
```
Jännitysvoima on aina pienempi kuin punnuksen paino $m_2 g$, koska $\tfrac{m_1}{m_1 + m_2} < 1$. Mitä raskaampi kärry on punnukseen verrattuna, sitä vähemmän kappaleet kiihtyvät ja sitä lähempänä $T$ on painoa $m_2 g$.

### Kaksi riippuvaa kappaletta
Kun langan kummassakin päässä roikkuu kappale, raskaampi ($m_2$) laskee ja kevyempi ($m_1$) nousee. Positiivinen suunta valitaan liikkeen suuntaan: kevyemmällä ylös ja raskaammalla alas. Silloin
```latex
\begin{aligned}
T - m_1 g &= m_1 a \\
m_2 g - T &= m_2 a
\end{aligned}
```
```latex
\begin{aligned}
a &= \frac{m_2 - m_1}{m_1 + m_2}\,g \\
T &= \frac{2 m_1 m_2}{m_1 + m_2}\,g
\end{aligned}
```
missä $m_2 > m_1$. Jännitysvoima on kappaleiden painojen $m_1 g$ ja $m_2 g$ välissä. Jos massat ovat yhtä suuret, $a = 0$ ja $T = mg$.

<svg data-fig="atwood" viewBox="0 0 600 410" role="img" aria-label="Kaksi riippuvaa kappaletta ja niiden voimakuviot. Vasemmalla tilannekuva: katosta riippuvan väkipyörän yli kulkevan langan vasemmassa päässä on kevyempi kappale ja oikeassa raskaampi. Kevyemmän vieressä on oranssi nuoli ylös ja raskaamman vieressä yhtä pitkä oranssi nuoli alas: kiihtyvyyden suuruus on sama. Oikealla ylhäällä kevyemmän kappaleen voimakuvio, kappale suorakulmiona: langan jännitysvoima T1 yläpinnasta ylös ja paino G1 keskipisteestä alas, ja T1 on pidempi kuin G1. Oikealla alhaalla raskaamman kappaleen voimakuvio: T2 yläpinnasta ylös ja G2 keskipisteestä alas, ja G2 on pidempi kuin T2. Nuolet T1 ja T2 ovat yhtä pitkät." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-13-atwood.webp" x="-1.3" y="-1.3" width="603" height="418.3" preserveAspectRatio="none"/>
  <foreignObject x="77.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="21.5" y="173.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="217.5" y="285.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="91.5" y="255.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="135.5" y="301.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <foreignObject x="312" y="7.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio: kevyempi}$</div></foreignObject>
  <foreignObject x="312" y="191.5" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio: raskaampi}$</div></foreignObject>
  <foreignObject x="439.5" y="156.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{1}$</div></foreignObject>
  <foreignObject x="439.5" y="49.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{1}$</div></foreignObject>
  <foreignObject x="545.5" y="91.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="439.5" y="382" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{2}$</div></foreignObject>
  <foreignObject x="439.5" y="228.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{2}$</div></foreignObject>
  <foreignObject x="545.5" y="319.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

### Menetelmä kytketyille kappaleille
1. **Piirrä oma voimakuvio** kummallekin kappaleelle. Lanka vetää kumpaakin kappaletta itseään kohti, ja jokaisella kappaleella on oma jännitysvoimansa nuoli.
2. **Valitse positiivinen suunta** kullekin kappaleelle kiihtyvyyden suuntaan. Jos kiihtyvyyden todellista suuntaa ei tiedetä, positiivisen suunnan saa olettaa, kunhan kappaleiden suunnat sopivat yhteen langan kanssa. Jos ratkaisuksi tulee negatiivinen kiihtyvyys, todellinen kiihtyvyys on vastakkaiseen suuntaan. Kitkan suunta riippuu liikkeen suunnasta, joten kitkallisessa tilanteessa oletettu suunta on tarkistettava.
3. **Kirjoita liikeyhtälö** $\Sigma F = ma$ kummallekin kappaleelle erikseen. Kiihtyvyys $a$ ja jännitysvoiman suuruus $T$ ovat samat molemmissa. Jos kappaletta vedetään lisäksi ulkoisella voimalla $\overline{F}$, se kuuluu vain vedettävän kappaleen voimakuvioon ja liikeyhtälöön.
4. **Ratkaise** kaksi yhtälöä: laske ne yhteen, jolloin $T$ poistuu, tai sijoita toisesta saatu $T$ toiseen.
5. **Tarkista** etumerkit ja vertaa: jännitysvoima ei ole yhtä suuri kuin riippuvan kappaleen paino, kun kappaleet kiihtyvät.

## Esimerkki
Pöydällä on kärry, jonka massa on $1{,}5\,\text{kg}$. Siihen sidottu lanka kulkee pöydän reunalla olevan kevyen väkipyörän yli, ja langan toisessa päässä roikkuu punnus, jonka massa on $0{,}60\,\text{kg}$. Kärry päästetään liikkeelle levosta. Kitka ja ilmanvastus jätetään huomiotta, ja lanka on kevyt ja venymätön. Kuinka suuri on kärryn kiihtyvyys ja kuinka suuri on langan jännitysvoima?

<!-- vaihe -->

**Tunnetut ja kysytty.** $m_1 = 1{,}5\,\text{kg}$, $m_2 = 0{,}60\,\text{kg}$ ja $g = 9{,}81\,\text{m/s}^2$.

Kysytään kiihtyvyyttä $a$ ja langan jännitysvoimaa $T$.

<!-- vaihe -->

**Periaate.** Kärry ja punnus ovat kaksi kappaletta, joten kummallekin kirjoitetaan oma liikeyhtälö. Lanka on venymätön, joten kappaleiden kiihtyvyyksillä on sama suuruus $a$. Lanka on kevyt ja väkipyörä kevyt ja kitkaton, joten lanka vetää kumpaakin kappaletta samalla voimalla $T$. Kitkaa ei ole, joten vaakasuunnassa kärryyn vaikuttaa vain lanka.

<!-- vaihe -->

**Voimakuvio.** Kummallekin kappaleelle on oma voimakuvio. Kärryn positiivinen suunta on oikealle ja punnuksen alas. Pystysuunnassa kärry ei kiihdy, joten $N = G_1$. Vaakasuunnassa kärryä vetää vain $\overline{T}_1$. Punnukseen vaikuttavat $\overline{G}_2$ alas ja $\overline{T}_2$ ylös.

<svg data-fig="esimerkki" viewBox="0 0 600 340" role="img" aria-label="Esimerkin kärry ja riippuva punnus. Vasemmalla tilannekuva: pöydällä oleva kärry, lanka väkipyörän yli riippuvaan punnukseen, ja kärryn yllä sininen nopeus ja oranssi kiihtyvyys oikealle. Oikealla ylhäällä kärryn voimakuvio: paino G1 alas, yhtä pitkä tukivoima N ylös ja jännitysvoima T1 oikealle. Oikealla alhaalla riippuvan punnuksen voimakuvio: paino G2 alas ja lyhyempi jännitysvoima T2 ylös. Nuolet T1 ja T2 ovat yhtä pitkät." style="max-width:100%;font-size:24px">
  <foreignObject x="77.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <rect x="20" y="176" width="214" height="12" rx="2" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="28" y="188" width="12" height="108" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="190" y="188" width="12" height="108" fill="#e9c98a" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="10" y1="296" x2="290" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="244" cy="164" r="12" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="244" cy="164" r="7" fill="#ffffff" stroke="#8a96a3" stroke-width="1.5"/>
  <circle cx="244" cy="164" r="2.5" fill="#1f2933"/>
  <rect x="226" y="172" width="12" height="10" fill="#8a96a3" stroke="#1f2933" stroke-width="1.5"/>
  <rect x="70" y="146" width="60" height="18" rx="3" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="83" cy="169" r="7" fill="#1f2933"/>
  <circle cx="117" cy="169" r="7" fill="#1f2933"/>
  <circle cx="83" cy="169" r="3" fill="#c4ccd4"/>
  <circle cx="117" cy="169" r="3" fill="#c4ccd4"/>
  <rect x="82" y="132" width="36" height="14" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M130,156 H244 A12,12 0 0 1 256,164 V236" fill="none" stroke="#b8622d" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="244" y="236" width="24" height="32" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="256" y1="236" x2="256" y2="232" stroke="#b8622d" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="82" y1="124" x2="140" y2="124" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M129,130.5 L142,124 L129,117.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="147.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="82" y1="84" x2="120" y2="84" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M109,90.5 L122,84 L109,77.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="127.5" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="35.5" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_1$</div></foreignObject>
  <foreignObject x="197.5" y="225.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_2$</div></foreignObject>
  <line x1="300" y1="12" x2="300" y2="332" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="310" y1="182" x2="590" y2="182" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="312" y="7.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio: kärry}$</div></foreignObject>
  <foreignObject x="312" y="187.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio: punnus}$</div></foreignObject>
  <rect x="400" y="88" width="80" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="108" x2="440" y2="157" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,174 L432,156 L448,156 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="155.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{1}$</div></foreignObject>
  <line x1="418" y1="128" x2="418" y2="79" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M418,62 L426,80 L410,80 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="379.5" y="49.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="480" y1="102" x2="482" y2="102" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M499,102 L481,110 L481,94 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="498.5" y="89.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{1}$</div></foreignObject>
  <rect x="420" y="266" width="40" height="20" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="276" x2="440" y2="285.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,302.5 L432,284.5 L448,284.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="290" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{2}$</div></foreignObject>
  <line x1="440" y1="266" x2="440" y2="264" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,247 L448,265 L432,265 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="439.5" y="234.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{2}$</div></foreignObject>
</svg>

<!-- vaihe -->

**Kaava ratkaistuna.** Kuvioista luetaan kaksi liikeyhtälöä ja ratkaistaan ne:
```latex
\begin{aligned}
&T = m_1 a \\
&m_2 g - T = m_2 a \\
&m_2 g = (m_1 + m_2) a \\
&a = \frac{m_2 g}{m_1 + m_2} \\
&T = m_1 a
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: massat ovat kilogrammoina ja $\tfrac{\text{kg} \cdot \text{m/s}^2}{\text{kg}} = \text{m/s}^2$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen:
```latex
\begin{aligned}
&a = \frac{m_2 g}{m_1 + m_2} \\
&\phantom{a} = \frac{0{,}60\,\text{kg} \cdot 9{,}81\,\text{m/s}^2}{1{,}5\,\text{kg} + 0{,}60\,\text{kg}} \\
&\phantom{a} \approx 2{,}80\,\text{m/s}^2 \\[4pt]
&T = m_1 a = 1{,}5\,\text{kg} \cdot 2{,}803\,\text{m/s}^2 \\
&\phantom{T} \approx 4{,}20\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kärryn kiihtyvyys on $a \approx 2{,}8\,\text{m/s}^2$ ja langan jännitysvoima $T \approx 4{,}2\,\text{N}$, kahden merkitsevän numeron tarkkuudella kuten massat $1{,}5\,\text{kg}$ ja $0{,}60\,\text{kg}$.

<!-- vaihe -->

**Järkevyys.** Punnuksen paino on $m_2 g \approx 5{,}9\,\text{N}$, ja jännitysvoima $4{,}2\,\text{N}$ on sitä pienempi, kuten pitääkin. Punnuksen kokonaisvoima on $5{,}886\,\text{N} - 4{,}204\,\text{N} \approx 1{,}68\,\text{N}$, ja se on $m_2 a = 0{,}60\,\text{kg} \cdot 2{,}803\,\text{m/s}^2 \approx 1{,}68\,\text{N}$. Kiihtyvyys on pienempi kuin $g$, koska punnus kiihdyttää myös kärryä. Jos kärryä ei olisi, punnus putoaisi kiihtyvyydellä $g$.

## Yleinen virhekäsitys
Usein ajatellaan, että kärryä vetää riippuvan punnuksen paino, joten jännitysvoima olisi $m_2 g$. Kärryä vetää kuitenkin lanka, ja langan voima on $T$. Vain silloin, kun kappaleet eivät kiihdy, esimerkiksi kun kärryä pidetään paikallaan, on $T = m_2 g$. Kun punnus laskee kiihtyen, punnuksen kokonaisvoiman $G_2 - T = m_2 a$ on osoitettava alas, joten $T < m_2 g$.

Toinen virhe on pitää voimia $\overline{T}_1$ ja $\overline{T}_2$ voimana ja vastavoimana. Ne vaikuttavat eri kappaleisiin mutta kuuluvat eri vuorovaikutuksiin: toinen lanka–kärry-parin ja toinen lanka–punnus-parin voimia. Ne ovat yhtä suuret, koska lanka on kevyt ja väkipyörä kevyt ja kitkaton, ei sen vuoksi, että ne olisivat vuorovaikutusparin voimia. Kolmas virhe on ajatella, että raskaampi kappale kiihtyy enemmän. Venymättömän langan päissä olevilla kappaleilla on sama kiihtyvyyden suuruus.

## Tiivistelmä
- Langalla tai väkipyörän yli kytketyillä kappaleilla on kummallakin oma voimakuvio ja oma liikeyhtälö $\Sigma F = ma$, ja positiivinen suunta valitaan kappaleelle kiihtyvyyden suuntaan tai oletetaan, jos suuntaa ei tiedetä: negatiivinen ratkaisu kertoo, että kiihtyvyys on vastakkainen.
- Kevyt, venymätön lanka ja kevyt, kitkaton väkipyörä antavat kappaleille saman kiihtyvyyden suuruuden $a$ ja samansuuruiset jännitysvoimat $T_1 = T_2 = T$.
- Kärrylle ja riippuvalle punnukselle $a = \frac{m_2}{m_1 + m_2}\,g$ ja $T = \frac{m_1 m_2}{m_1 + m_2}\,g$. Kahdelle riippuvalle kappaleelle $a = \frac{m_2 - m_1}{m_1 + m_2}\,g$ ja $T = \frac{2 m_1 m_2}{m_1 + m_2}\,g$.
- Kiihtyvän riippuvan kappaleen jännitysvoima ei ole sen paino: kärryn ja punnuksen tapauksessa $T < m_2 g$, ja kahdella riippuvalla kappaleella $T$ on painojen välissä.
- Jännitysvoimat $\overline{T}_1$ ja $\overline{T}_2$ vaikuttavat eri kappaleisiin eivätkä ole voima ja vastavoima.
