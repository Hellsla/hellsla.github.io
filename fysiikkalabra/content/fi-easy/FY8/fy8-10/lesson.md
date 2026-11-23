# Massavaje ja ytimen sidosenergia

> **Miksi** helium-4-atomi on kevyempi kuin kaksi vetyatomia ja kaksi neutronia yhteensä, vaikka se koostuu juuri niistä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion pöydällä on vanhanaikainen vaaka. Vasemmassa vaakakupissa on erillään kaksi punaista protonia ja kaksi harmaata neutronia. Se on alempana. Oikeassa kupissa samat neljä hiukkasta ovat tiiviisti yhdessä heliumytimenä. Se on ylempänä. Heliumydin hehkuu ja lähettää kaksi oranssia fotonia. Erilliset hiukkaset painavat enemmän kuin niistä koottu ydin." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-10-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Atomimassayksikkö
Atomien ja ytimien massat ilmoitetaan **atomimassayksikköinä**. Se on hyvin pieni massan yksikkö, ja sen merkki on $\text{u}$. Yksikkö on määritelty niin, että hiili-12-atomin massa on tasan $12\,\text{u}$. Siksi $1\,\text{u} = 1{,}66054 \cdot 10^{-27}\,\text{kg}$. Protonin ja neutronin massat ovat kumpikin noin $1\,\text{u}$. Atomin massa atomimassayksikköinä on siis lähellä sen massalukua $A$, mutta se ei ole tasan sama. Massaluku $A$ kertoo, montako protonia ja neutronia ytimessä on yhteensä. Taulukon arvot ovat **atomien** massoja, joten niihin sisältyvät myös elektronit. Vetyatomin ${}^{1}\text{H}$ massa on protonin ja elektronin massa yhteensä.

| Hiukkanen | Merkintä | Massa ($\text{u}$) |
| --- | --- | --- |
| vety-1 | ${}^{1}\text{H}$ | $1{,}007825$ |
| neutroni | $\text{n}$ | $1{,}008665$ |
| vety-2 | ${}^{2}\text{H}$ | $2{,}014102$ |
| helium-4 | ${}^{4}\text{He}$ | $4{,}002603$ |
| hiili-12 | ${}^{12}\text{C}$ | $12{,}000000$ |
| happi-16 | ${}^{16}\text{O}$ | $15{,}994915$ |
| rauta-56 | ${}^{56}\text{Fe}$ | $55{,}934936$ |
| uraani-238 | ${}^{238}\text{U}$ | $238{,}050787$ |

Lähde: atomimassataulukko AME2020 (Atomic Mass Evaluation 2020, IAEA:n Atomic Mass Data Center). Arvot on pyöristetty kuuteen desimaaliin. Ytimen massoissa tarvitaan näin monta desimaalia, koska tärkeät erot ovat pieniä.

### Massavaje
Helium-4-atomissa on kaksi protonia, kaksi neutronia ja kaksi elektronia. Samat hiukkaset ovat kahdessa vetyatomissa ja kahdessa neutronissa. Niiden yhteinen massa on $$
\begin{aligned}
&2 \cdot 1{,}007825\,\text{u} + 2 \cdot 1{,}008665\,\text{u} \\
&= 4{,}032980\,\text{u}
\end{aligned}
$$. Helium-4-atomin massa on kuitenkin vain $4{,}002603\,\text{u}$. Kun protonit ja neutronit eli **nukleonit** ovat sitoutuneet ytimeksi, niiden massa on pienempi kuin erillään. Erotus $$
\begin{aligned}
&4{,}032980\,\text{u} - 4{,}002603\,\text{u} \\
&= 0{,}030377\,\text{u}
\end{aligned}
$$ on ytimen **massavaje** $\Delta m$. Se on noin $0{,}76\,\%$ atomin massasta. Laskussa käytetään vetyatomeja erillisten protonien sijaan, jotta elektronien massat kumoutuvat eli niitä ei tarvitse laskea erikseen: molemmilla puolilla on kaksi elektronia.

<svg data-fig="massat" viewBox="0 0 600 350" role="img" aria-label="Pylväskuva. Pystyakseli on mittakaavassa mutta katkaistu: se alkaa arvosta 3,990 u eikä nollasta. Vasen pylväs on kahden vetyatomin ja kahden neutronin yhteenlaskettu massa, 4,032980 u. Oikea pylväs on helium-4-atomin massa, 4,002603 u. Pylväiden ero eli massavaje on 0,030377 u. Se on merkitty punaisella hakasulkeella." style="max-width:100%;font-size:24px">
  <line x1="130" y1="243" x2="560" y2="243" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="243" x2="130" y2="243" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="228.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4{,}000$</div></foreignObject>
  <line x1="130" y1="196.5" x2="560" y2="196.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="196.5" x2="130" y2="196.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="182" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4{,}010$</div></foreignObject>
  <line x1="130" y1="149.5" x2="560" y2="149.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="149.5" x2="130" y2="149.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="135" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4{,}020$</div></foreignObject>
  <line x1="130" y1="103" x2="560" y2="103" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="103" x2="130" y2="103" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="88.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4{,}030$</div></foreignObject>
  <line x1="130" y1="56" x2="560" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="56" x2="130" y2="56" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="41.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4{,}040$</div></foreignObject>
  <line x1="130" y1="290" x2="560" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="130" y1="291" x2="130" y2="40" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M130,28 L136,41 L124,41 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="142" y="5.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m\ (\text{u})$</div></foreignObject>
  <rect x="121" y="264" width="18" height="12" fill="#ffffff"/>
  <line x1="121" y1="268" x2="139" y2="262" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="121" y1="278" x2="139" y2="272" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="160" y="89" width="80" height="201" fill="#c9c2b2" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="133.5" y="54.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$4{,}032980\,\text{u}$</span></div></foreignObject>
  <foreignObject x="152.5" y="305.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2m_\text{H} + 2m_\text{n}$</div></foreignObject>
  <rect x="280" y="231" width="80" height="59" fill="#b2f2bb" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="253.5" y="196.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$4{,}002603\,\text{u}$</span></div></foreignObject>
  <foreignObject x="278.5" y="305.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m({}^{4}\text{He})$</div></foreignObject>
  <line x1="240" y1="89" x2="428" y2="89" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="360" y1="231" x2="428" y2="231" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="420" y1="89" x2="420" y2="231" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="412" y1="89" x2="428" y2="89" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="412" y1="231" x2="428" y2="231" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="437" y="128.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta m$</span></div></foreignObject>
  <foreignObject x="437" y="162.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$0{,}030377\,\text{u}$</span></div></foreignObject>
</svg>

### Massa ja energia
Massavaje ei ole kadonnutta ainetta. Einsteinin suhteellisuusteorian mukaan massa ja energia ovat **ekvivalentit** eli samanarvoiset. Kun kappaleen energia muuttuu määrällä $\Delta E$, sen massa muuttuu määrällä $\tfrac{\Delta E}{c^2}$. Tässä $c$ on valon nopeus. Kun protonit ja neutronit sitoutuvat ytimeksi, vahva vuorovaikutus vetää ne yhteen. Silloin energiaa vapautuu esimerkiksi gammafotoneina. Syntyneen ytimen energia on pienempi kuin erillisten nukleonien energia, ja siksi myös sen massa on pienempi. Saman verran energiaa tarvitaan, jos ydin hajotetaan takaisin erillisiksi nukleoneiksi. Tämä energia on ytimen **sidosenergia** $E_\text{B}$.

<svg data-fig="energia" viewBox="0 0 600 345" role="img" aria-label="Kaavakuva, ei mittakaavassa: energiatasot. Ylempi vaakaviiva on erillisten protonien ja neutronien energia. Sen päällä on kaksi punaista protonia ja kaksi harmaata neutronia erillään. Alempi vaakaviiva on helium-4-ytimen energia. Sen päällä samat neljä nukleonia ovat tiiviisti yhdessä. Vasemmalla on oranssi nuoli ylöspäin: ytimen hajottaminen nukleoneiksi vaatii sidosenergian E B. Oikealla on oranssi nuoli alaspäin: kun ydin muodostuu, sama energia vapautuu. Tasojen väliin on kirjoitettu E B = Δm c²." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-10-energia.webp" x="0" y="0" width="600" height="355" preserveAspectRatio="none"/>
  <foreignObject x="136.5" y="25.5" width="357" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{erilliset protonit ja neutronit}$</div></foreignObject>
  <foreignObject x="259" y="301.5" width="112" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ydin}\ {}^{4}_{2}\text{He}$</div></foreignObject>
  <foreignObject x="261" y="135.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$E_\text{B} = \Delta m\,c^2$</div></foreignObject>
  <foreignObject x="118" y="185.5" width="149" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{tarvitaan}\ E_\text{B}$</div></foreignObject>
  <foreignObject x="378" y="185.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{vapautuu}\ E_\text{B}$</div></foreignObject>
</svg>

```pysahdy
Hiili-12-ytimen sidosenergia on $92{,}2\,\text{MeV}$. Kuinka monta atomimassayksikköä ydin on kevyempi kuin sen $12$ nukleonia erillään? Käytä arvoa $1\,\text{u} = 931{,}5\,\tfrac{\text{MeV}}{c^2}$.
---
Sidosenergia vastaa massaeroa: $\Delta m = \tfrac{E_\text{B}}{c^2} = \tfrac{92{,}2\,\text{MeV}}{931{,}5\,\text{MeV}/\text{u}} \approx 0{,}0990\,\text{u}$. Ydin on noin $0{,}099\,\text{u}$ kevyempi.
```

### Miksi massan muutosta ei huomaa arjessa
Massan ja energian ekvivalenssi koskee kaikkia energian muutoksia. Luku $c^2$ on kuitenkin niin suuri, että tavallisissa ilmiöissä massan muutos on liian pieni mitattavaksi. Yhtä grammaa massaa vastaa energia
```latex
\begin{aligned}
&E = 1{,}00 \cdot 10^{-3}\,\text{kg} \\
&\quad \cdot (2{,}998 \cdot 10^{8}\,\text{m/s})^2 \\
&\approx 9{,}0 \cdot 10^{13}\,\text{J}.
\end{aligned}
```
Kun hiili palaa, massa pienenee vain noin kymmenesmiljardisosan. Ytimissä sidosenergia on niin suuri, että massavaje on noin $0{,}8\,\%$ atomin massasta. Näin on sekä helium-4:llä että uraani-238:lla. Siksi ydinfysiikassa energia lasketaan suoraan massojen erotuksesta.

## Kaava: Sidosenergia

### Massavaje ja sidosenergia
Ytimessä ${}^{A}_{Z}\text{X}$ on $Z$ protonia ja $N = A - Z$ neutronia. Massavaje lasketaan atomimassoista:
```latex
\Delta m = Z\,m_\text{H} + N\,m_\text{n} - m_\text{atomi}
```
Tässä $m_\text{H}$ on vetyatomin ${}^{1}\text{H}$ massa, $m_\text{n}$ on neutronin massa ja $m_\text{atomi}$ on atomin ${}^{A}_{Z}\text{X}$ massa. Ytimen sidosenergia on massavajetta vastaava energia:
```kaavat
ytimen sidosenergia :: E_\text{B} = \Delta m\,c^2
```
Tässä $E_\text{B}$ on sidosenergia ja $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$ on valon nopeus. Elektronien omaa sidosenergiaa atomissa ei oteta huomioon. Se on enintään satoja kiloelektronivoltteja. Raskaimmillakin atomeilla se on alle tuhannesosa ytimen sidosenergiasta.

### Atomimassayksikkö energiana
Ytimien energiat ilmoitetaan megaelektronivoltteina: $1\,\text{MeV} = 10^{6}\,\text{eV}$ ja $1\,\text{eV} = 1{,}602177 \cdot 10^{-19}\,\text{J}$. Lasketaan, paljonko energiaa vastaa massa $1\,\text{u}$. Massavaje on pieni erotus. Siksi vakioissa käytetään tässä kuutta merkitsevää numeroa:
```latex
\begin{aligned}
&E = 1\,\text{u} \cdot c^2 \\
&= 1{,}66054 \cdot 10^{-27}\,\text{kg} \\
&\quad \cdot (2{,}99792 \cdot 10^{8}\,\text{m/s})^2 \\
&= 1{,}49241 \cdot 10^{-10}\,\text{J} \\
&= \frac{1{,}49241 \cdot 10^{-10}}{1{,}602177 \cdot 10^{-19}}\,\text{eV} \\
&= 9{,}3149 \cdot 10^{8}\,\text{eV} \\
&\approx 931{,}5\,\text{MeV}
\end{aligned}
```
Siis $1\,\text{u} = 931{,}5\,\tfrac{\text{MeV}}{c^2}$. Kun massavaje on atomimassayksikköinä, tämä arvo sijoitetaan yksikön paikalle, ja $c^2$ supistuu pois. Esimerkiksi $$
\begin{aligned}
&0{,}001000\,\text{u} \cdot c^2 \\
&= 0{,}001000 \cdot 931{,}5\,\tfrac{\text{MeV}}{c^2} \cdot c^2 \\
&= 0{,}9315\,\text{MeV}
\end{aligned}
$$. Jos vakioissa olisi vain neljä numeroa, $1{,}661 \cdot 10^{-27}\,\text{kg}$, $2{,}998 \cdot 10^{8}\,\text{m/s}$ ja $1{,}602 \cdot 10^{-19}\,\text{J}$, tulos olisi $931{,}9\,\text{MeV}$. Neljän numeron vakiot muuttavat siis jo tuloksen neljättä numeroa.

```pysahdy
Ytimen massavaje on $0{,}0020\,\text{u}$. Kuinka suuri on ytimen sidosenergia megaelektronivoltteina?
---
Käytetään arvoa $1\,\text{u} = 931{,}5\,\tfrac{\text{MeV}}{c^2}$. Silloin $E_\text{B} = 0{,}0020 \cdot 931{,}5\,\text{MeV} \approx 1{,}9\,\text{MeV}$.
```

### Sidosenergia nukleonia kohti
Ytimien sidoksen lujuutta vertaillaan **sidosenergialla nukleonia kohti**:
```kaavat
ytimen sidososuus :: \frac{E_\text{B}}{A}
```
Tässä $A$ on massaluku eli nukleonien määrä. Kuvaajassa suure on laskettu atomimassoista $32$ ytimelle. Kevyillä ytimillä arvo kasvaa jyrkästi, koska jokaisella nukleonilla on yhä enemmän naapureita, joihin vahva vuorovaikutus sitoo sen. Helium-4 on poikkeuksellisen tiiviisti sidottu. Arvo on suurin, noin $8{,}8\,\text{MeV}$, rauta-56:n ja nikkeli-62:n kohdalla. Raskaammilla ytimillä arvo pienenee loivasti. Vahva vuorovaikutus vaikuttaa vain lähinaapureiden välillä. Protonien sähköinen hylkiminen sen sijaan ulottuu koko ytimen yli.

<svg data-fig="kayra" viewBox="0 0 600 350" role="img" aria-label="Kuvaaja mittakaavassa: sidosenergia nukleonia kohti megaelektronivoltteina massaluvun A funktiona. Massaluku A on nollasta 250:een ja pystyakseli nollasta 10 megaelektronivolttiin. Pisteet ovat 32 ytimen arvoja, jotka on laskettu atomimassoista. Deuteriumilla arvo on 1,11 MeV. Helium-4:llä arvo on 7,07 MeV, ja se on selvästi naapureitaan suurempi. Arvo nousee jyrkästi kevyillä ytimillä. Se on suurin, noin 8,8 MeV, rauta-56:n ja nikkeli-62:n kohdalla. Sitten se pienenee loivasti raskaita ytimiä kohti: uraani-238:lla se on 7,57 MeV. Vasemmalla on oranssi nuoli ylöspäin oikealle: fuusio eli kevyiden ytimien yhtyminen. Oikealla on oranssi nuoli vasemmalle kohti huippua: fissio eli raskaan ytimen halkeaminen." style="max-width:100%;font-size:24px">
  <line x1="212" y1="300" x2="212" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="294" y1="300" x2="294" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="376" y1="300" x2="376" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="458" y1="300" x2="458" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="540" y1="300" x2="540" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="252" x2="540" y2="252" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="204" x2="540" y2="204" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="156" x2="540" y2="156" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="108" x2="540" y2="108" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="130" y1="60" x2="540" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="129" y1="300" x2="554" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M566,300 L553,306 L553,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="130" y1="301" x2="130" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M130,34 L136,47 L124,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="212" y1="300" x2="212" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="195.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="294" y1="300" x2="294" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="271.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="376" y1="300" x2="376" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="353.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="458" y1="300" x2="458" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="435.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="540" y1="300" x2="540" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="517.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$250$</div></foreignObject>
  <line x1="123" y1="252" x2="130" y2="252" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="98" y="237.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="123" y1="204" x2="130" y2="204" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="98" y="189.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="123" y1="156" x2="130" y2="156" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="98" y="141.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="123" y1="108" x2="130" y2="108" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="98" y="93.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="123" y1="60" x2="130" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="85" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <foreignObject x="100" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="572" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="120" y="3.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{B}/A\ (\text{MeV})$</div></foreignObject>
  <path d="M195.5,266 L218.5,199 L226,201.5 L220,176 L199.5,192.5 L207,195 L184.5,262 Z" fill="#ffc078" stroke-linejoin="round"/>
  <foreignObject x="232" y="211.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\text{fuusio}$</div></foreignObject>
  <path d="M500,164 L382,164 L382,156 L360,170 L382,184 L382,176 L500,176 Z" fill="#ffc078" stroke-linejoin="round"/>
  <foreignObject x="388.5" y="189.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\text{fissio}$</div></foreignObject>
  <circle cx="133.5" cy="273.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="135" cy="232" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="135" cy="238.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="136.5" cy="130" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="140" cy="172" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="141.5" cy="165.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="145" cy="145" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="148" cy="133.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="149.5" cy="115.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="153" cy="120.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="156" cy="108.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="163" cy="107" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="169.5" cy="101.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="176" cy="97.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="182.5" cy="96" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="195.5" cy="95" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="222" cy="89" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="231.5" cy="89" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="233.5" cy="90" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="235" cy="90.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="268" cy="91" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="277.5" cy="91" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="305.5" cy="94.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="327" cy="96" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="356.5" cy="98.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="432" cy="108" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="453" cy="110" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="471" cy="111" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="473" cy="111.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="510.5" cy="117" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="515.5" cy="118" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="520.5" cy="118.5" r="5.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="139.5" y1="124" x2="168" y2="74" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="170" y="47.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">${}^{4}\text{He}$</div></foreignObject>
  <line x1="227" y1="84" x2="262" y2="70" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="264" y="47.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">${}^{56}\text{Fe}$</div></foreignObject>
  <foreignObject x="487.5" y="134" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${}^{238}\text{U}$</div></foreignObject>
  <foreignObject x="147.5" y="255" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">${}^{2}\text{H}$</div></foreignObject>
</svg>

Kuvaajasta näkee, milloin ydinreaktio vapauttaa energiaa. Jos syntyvät ytimet ovat tiiviimmin sidottuja kuin alkuperäiset, sidosenergia kasvaa ja ero vapautuu. Kevyiden ytimien yhtyminen eli **fuusio** siirtää nukleoneja kohti kuvaajan huippua. Samoin tekee raskaan ytimen halkeaminen eli **fissio**. Niitä tarkastellaan luvussa *Fissio, fuusio ja ydinvoima*.

```pysahdy
Ydinreaktiossa nukleoneja on yhtä monta molemmin puolin. Lähtöytimien sidosenergia on yhteensä $1800\,\text{MeV}$ ja tuotteiden $1805\,\text{MeV}$. Vapautuuko energiaa vai tarvitaanko sitä? Kuinka paljon? Miten massa muuttuu?
---
Energiaa vapautuu. Tuotteet ovat tiukemmin sidottuja, joten erotus $1805\,\text{MeV} - 1800\,\text{MeV} = 5\,\text{MeV}$ vapautuu tuotteiden liike-energiaksi. Kokonaismassa pienenee määrällä $\tfrac{5\,\text{MeV}}{c^2}$.
```

### Reaktioenergia
**Ydinreaktiossa** ytimet muuttuvat: ydin hajoaa, tai ytimeen osuu toinen ydin tai hiukkanen. Reaktiossa massaluku ja varausluku säilyvät eli pysyvät samoina (luku *Atomiydin ja radioaktiivinen hajoaminen*). Massa ei kuitenkaan säily. Reaktioenergia on
```kaavat
ydinreaktiossa vapautuva energia :: Q = (m_\text{alku} - m_\text{loppu})\,c^2
```
Tässä $m_\text{alku}$ on lähtöaineiden massojen summa ja $m_\text{loppu}$ on syntyvien hiukkasten massojen summa. Kun $Q > 0$, energiaa vapautuu. Se muuttuu syntyvien hiukkasten liike-energiaksi ja gammasäteilyksi. Kun $Q < 0$, reaktio tarvitsee energiaa. Kaavaan lasketaan kummallakin puolella kaikkien hiukkasten massat. Taulukoiden atomimassoihin sisältyvät myös atomien elektronit. Alfahajoamisessa ja useimmissa ydinreaktioissa elektroneja on kummallakin puolella yhtä monta. Silloin atomimassat voi sijoittaa kaavaan suoraan. Esimerkiksi uraani-238:n alfahajoamisessa ${}^{238}_{92}\text{U} \to {}^{234}_{90}\text{Th} + {}^{4}_{2}\text{He}$ massa pienenee $0{,}004583\,\text{u}$. Siksi $$
\begin{aligned}
&Q \\
&= 0{,}004583 \cdot 931{,}5\,\text{MeV} \\
&\approx 4{,}27\,\text{MeV}
\end{aligned}
$$.

<svg data-fig="reaktio" viewBox="0 0 600 350" role="img" aria-label="Pylväskuva. Pystyakseli on mittakaavassa mutta katkaistu: se alkaa arvosta 238,040 u eikä nollasta. Vasen pylväs on uraani-238-atomin massa, 238,050787 u. Oikea pylväs on alfahajoamisessa syntyvien torium-234- ja helium-4-atomien yhteinen massa, 238,046204 u. Ero 0,004583 u on merkitty punaisella hakasulkeella. Se vastaa reaktioenergiaa Q = 4,27 MeV." style="max-width:100%;font-size:24px">
  <line x1="130" y1="212" x2="560" y2="212" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="212" x2="130" y2="212" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="197.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$238{,}045$</div></foreignObject>
  <line x1="130" y1="134" x2="560" y2="134" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="134" x2="130" y2="134" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="119.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$238{,}050$</div></foreignObject>
  <line x1="130" y1="56" x2="560" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="123" y1="56" x2="130" y2="56" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="23" y="41.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$238{,}055$</div></foreignObject>
  <line x1="130" y1="290" x2="560" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="130" y1="291" x2="130" y2="40" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M130,28 L136,41 L124,41 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="142" y="5.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m\ (\text{u})$</div></foreignObject>
  <rect x="121" y="264" width="18" height="12" fill="#ffffff"/>
  <line x1="121" y1="268" x2="139" y2="262" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="121" y1="278" x2="139" y2="272" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="160" y="121.5" width="80" height="168.5" fill="#c9c2b2" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="121" y="87" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$238{,}050787\,\text{u}$</span></div></foreignObject>
  <foreignObject x="171" y="305.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${}^{238}\text{U}$</div></foreignObject>
  <rect x="280" y="193" width="80" height="97" fill="#b2f2bb" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="241" y="158.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$238{,}046204\,\text{u}$</span></div></foreignObject>
  <foreignObject x="260" y="305.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${}^{234}\text{Th} + {}^{4}\text{He}$</div></foreignObject>
  <line x1="240" y1="121.5" x2="428" y2="121.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="360" y1="193" x2="428" y2="193" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="420" y1="121.5" x2="420" y2="193" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="412" y1="121.5" x2="428" y2="121.5" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="412" y1="193" x2="428" y2="193" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <foreignObject x="437" y="126" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$0{,}004583\,\text{u}$</span></div></foreignObject>
  <foreignObject x="437" y="160" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$Q = 4{,}27\,\text{MeV}$</span></div></foreignObject>
</svg>

### Atomimassat beetahajoamisessa
Beetahajoamisessa ytimen varausluku muuttuu. Siksi lähtöatomissa ja tytäratomissa on eri määrä elektroneja. Jos käytetään ydinmassoja, mukaan lasketaan syntyvän elektronin tai positronin massa. Neutraalien atomien massoja merkitään $M$. Niitä käytettäessä laskutapa riippuu hajoamislajista. Beeta miinus -hajoamisessa tytärytimessä on yksi protoni enemmän. Siksi tytäratomissa on yksi elektroni enemmän kuin lähtöatomissa. Tämä ylimääräinen elektroni vastaa massaltaan syntyvää beetahiukkasta. Elektronin massaa ei siis lisätä erikseen:
```latex
Q(\beta^-) = [M(\text{X}) - M(\text{Y})]\,c^2
```
Tässä $M(\text{X})$ on lähtöatomin massa ja $M(\text{Y})$ tytäratomin massa. Beeta plus -hajoamisessa tytäratomissa on yksi elektroni vähemmän kuin lähtöatomissa. Lisäksi syntyy positroni, jonka massa on sama kuin elektronin. Siksi kahden elektronin massa vähennetään:
```latex
Q(\beta^+) = [M(\text{X}) - M(\text{Y}) - 2m_e]\,c^2
```
Tässä $m_e = 0{,}000549\,\text{u}$ on elektronin massa. Malli jättää huomiotta atomin elektronien sidosenergiat. Ne ovat tällä tarkkuudella niin pieniä, ettei niillä ole merkitystä.

## Esimerkki
Laske helium-4-ytimen ${}^{4}_{2}\text{He}$ sidosenergia ja sidosenergia nukleonia kohti. Käytä atomimassoja $m({}^{4}\text{He}) = 4{,}002603\,\text{u}$, $m_\text{H} = 1{,}007825\,\text{u}$ ja $m_\text{n} = 1{,}008665\,\text{u}$ (AME2020). Käytä myös arvoa $1\,\text{u} = 931{,}5\,\tfrac{\text{MeV}}{c^2}$.

<!-- vaihe -->
**Tunnetut ja kysytty.** Järjestysluku eli protonien määrä on $Z = 2$ ja massaluku on $A = 4$. Neutroneja on siis $N = A - Z = 2$. Atomimassat ovat $m_\text{atomi} = 4{,}002603\,\text{u}$, $m_\text{H} = 1{,}007825\,\text{u}$ ja $m_\text{n} = 1{,}008665\,\text{u}$.

Kysytään sidosenergiaa $E_\text{B}$ ja sidosenergiaa nukleonia kohti $\tfrac{E_\text{B}}{A}$ megaelektronivoltteina.

<!-- vaihe -->
**Periaate.** Ydin on kevyempi kuin sen erilliset nukleonit. Massavajetta $\Delta m$ vastaa sidosenergia $E_\text{B} = \Delta m\,c^2$. Lasketaan atomimassoilla. Kahdessa vetyatomissa on kaksi elektronia, kuten helium-4-atomissakin, joten elektronien massat kumoutuvat.

<!-- vaihe -->
**Kaava ratkaistuna.** Massavaje, sidosenergia ja sen osuus yhtä nukleonia kohti:
```latex
\begin{aligned}
&\Delta m = Z\,m_\text{H} + N\,m_\text{n} - m_\text{atomi} \\
&E_\text{B} = \Delta m\,c^2 \\
&\frac{E_\text{B}}{A} = \frac{\Delta m\,c^2}{A}
\end{aligned}
```

<!-- vaihe -->
**Yksikkömuunnokset.** Massaa ei muunneta kilogrammoiksi. Massavajeen yksikön paikalle sijoitetaan $1\,\text{u} = 931{,}5\,\tfrac{\text{MeV}}{c^2}$. Silloin $c^2$ supistuu pois, ja energia saadaan suoraan megaelektronivoltteina.

<!-- vaihe -->
**Sijoitus.** Lasketaan ensin massavaje ja sitten energia:
```latex
\begin{aligned}
&\Delta m = Z\,m_\text{H} + N\,m_\text{n} - m_\text{atomi} \\
&= 2 \cdot 1{,}007825\,\text{u} \\
&\quad + 2 \cdot 1{,}008665\,\text{u} \\
&\quad - 4{,}002603\,\text{u} \\
&= 0{,}030377\,\text{u} \\[6pt]
&E_\text{B} = \Delta m\,c^2 = 0{,}030377\,\text{u} \cdot c^2 \\
&= 0{,}030377 \cdot 931{,}5\,\tfrac{\text{MeV}}{c^2} \cdot c^2 \\
&= 28{,}296\,\text{MeV} \\[6pt]
&\frac{E_\text{B}}{A} = \frac{28{,}296\,\text{MeV}}{4} \\
&= 7{,}074\,\text{MeV}
\end{aligned}
```

<!-- vaihe -->
**Tulos.** Helium-4-ytimen sidosenergia on $28{,}30\,\text{MeV}$ ja sidosenergia nukleonia kohti on $7{,}074\,\text{MeV}$. Vastauksessa on neljä merkitsevää numeroa, koska muuntoluvussa $931{,}5\,\tfrac{\text{MeV}}{c^2}$ on neljä.

<!-- vaihe -->
**Järkevyys.** Pyöristetyillä luvuilla $\Delta m \approx 0{,}03\,\text{u}$ ja $0{,}03 \cdot 900\,\text{MeV} = 27\,\text{MeV}$. Se on lähellä tulosta. Massavaje on noin $0{,}8\,\%$ atomin massasta, kuten ytimillä yleensä. Arvo $7{,}07\,\text{MeV}$ nukleonia kohti on kuvaajan helium-4:n piste, ja se on selvästi naapureitaan suurempi.

## Yleinen virhekäsitys
Moni ajattelee, että sidosenergia on ytimeen varastoitunutta energiaa, joka vapautuu, kun ydin hajotetaan osiin. Asia on päinvastoin. Sidosenergia *vapautui*, kun ydin muodostui. Saman verran energiaa *tarvitaan*, jotta ydin saadaan hajotettua erillisiksi nukleoneiksi. Siksi ydin on kevyempi kuin sen osat. Suuri sidosenergia nukleonia kohti tarkoittaa tiiviisti sidottua, pysyvää ydintä. Se ei tarkoita energiavarastoa. Ydinreaktiossa energiaa vapautuu, kun syntyvien ytimien sidosenergia on yhteensä *suurempi* kuin alkuperäisten ytimien.

Toinen virhe on ajatella, että massa säilyy ydinreaktiossa kuten kemiassa. Ydinreaktiossa säilyvät massaluku eli nukleonien määrä ja varausluku. Massa muuttuu vapautuvan energian verran: $\Delta m = \tfrac{Q}{c^2}$.

## Tiivistelmä
- Atomimassat ilmoitetaan atomimassayksikköinä. Yksikkö $1\,\text{u}$ on $\tfrac{1}{12}$ hiili-12-atomin massasta, eli $1\,\text{u} = 1{,}66054 \cdot 10^{-27}\,\text{kg}$.
- Ydin on kevyempi kuin sen erilliset nukleonit. Massavaje on

    $$\Delta m = Z\,m_\text{H} + N\,m_\text{n} - m_\text{atomi}$$.

- Sidosenergia $E_\text{B} = \Delta m\,c^2$ tarvitaan ytimen hajottamiseen nukleoneiksi, ja se vapautuu ytimen muodostuessa. Kun sijoitetaan $1\,\text{u} = 931{,}5\,\tfrac{\text{MeV}}{c^2}$, energia tulee megaelektronivoltteina.
- Sidosenergia nukleonia kohti on suurin, noin $8{,}8\,\text{MeV}$, raudan ja nikkelin kohdalla. Fuusio ja fissio vapauttavat energiaa, koska ne siirtävät nukleoneja tiiviimmin sidottuihin ytimiin.
- Reaktioenergia on $Q = (m_\text{alku} - m_\text{loppu})\,c^2$. Massa ei säily ydinreaktiossa, vaikka massaluku ja varausluku säilyvät. Atomimassoilla beeta miinus -hajoamisessa $Q(\beta^-) = [M(\text{X}) - M(\text{Y})]\,c^2$. Beeta plus -hajoamisessa vähennetään lisäksi $2m_e$.
