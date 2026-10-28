# Mittaaminen ja mittauksen luotettavuus

> **Miksi** kymmenen oppilasta saa samasta kuulan vierimisajasta kymmenen eri tulosta, vaikka kaikki käyttävät samaa kelloa?

## Ydinajatus
**Mittaus** on suureen arvon määrittämistä vertaamalla sitä yksikköön. Mittaustulos on lukuarvo ja yksikkö, esimerkiksi $2{,}43\,\text{s}$. Tulos ei ole koskaan täsmälleen suureen oikea arvo, koska mittarin lukeminen, mittaustapa ja olosuhteet tuovat siihen poikkeaman. Tuloksen ja oikean arvon erotus on **mittausvirhe** $e = x - x_\text{oikea}$. Virhe kuuluu jokaiseen mittaukseen, eikä se ole sama asia kuin moka, esimerkiksi väärin kirjattu luku. Fysiikassa virhe arvioidaan ja ilmoitetaan tuloksen mukana.

Virheet jaetaan kahteen lajiin sen mukaan, miten ne käyttäytyvät, kun mittaus toistetaan.

### Satunnaisvirhe
**Satunnaisvirhe** vaihtelee mittauksesta toiseen sattumanvaraisesti ja voi olla kumpaan suuntaan tahansa. Käsikellolla kuulan vierimisaikaa mitattaessa se syntyy reaktioajasta: välillä kello käynnistyy hieman liian aikaisin ja välillä liian myöhään. Myös asteikon lukeminen kahden viivan väliltä tuo satunnaisvirhettä. Se näkyy hajontana: samasta suureesta saadaan joka kerta vähän eri luku. Toistamalla mittaus hajonta tulee näkyviin, ja keskiarvo vaimentaa sitä, koska liian suuret ja liian pienet tulokset kumoavat osin toisensa.

### Systemaattinen virhe
**Systemaattinen virhe** on joka mittauksessa suunnaltaan ja suuruudeltaan lähes sama. Se syntyy esimerkiksi väärästä nollakohdasta (vaaka näyttää tyhjänä $1{,}2\,\text{g}$), huonosti säädetystä mittarista tai mittaustavasta, kuten asteikon katsomisesta vinosti. Kaikki tulokset siirtyvät samaan suuntaan, joten ne voivat olla tiiviisti ryhmässä mutta väärässä paikassa. Toistaminen ja keskiarvo eivät poista sitä. Se huomataan vertaamalla tulosta tunnettuun vertailuarvoon tai toiseen mittaustapaan, ja sitten se korjataan.

<svg data-fig="error-types" viewBox="0 0 600 400" role="img" aria-label="Kaavakuva samasta mittauksesta kahdella tavalla, aikaakseli mittakaavassa. Ylhäällä on satunnaisvirhe: kymmenen tulosta hajaantuu oikean arvon 2,40 s molemmin puolin, ja keskiarvo 2,41 s on lähellä oikeaa arvoa. Alhaalla on systemaattinen virhe: kymmenen tulosta on tiiviissä ryhmässä, mutta ryhmä on kokonaan oikean arvon oikealla puolella ja keskiarvo 2,59 s on noin 0,19 s liian suuri." style="max-width:100%;font-size:24px">
  <foreignObject x="14" y="11.5" width="432" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Satunnaisvirhe: tulokset hajaantuvat}$</div></foreignObject>
  <line x1="203.5" y1="158" x2="203.5" y2="72" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="208.5" y1="158" x2="208.5" y2="72" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="131.5" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="160.5" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="174.5" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="189" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="203.5" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="203.5" cy="130" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="232" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="232" cy="130" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="260.5" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="289.5" cy="146" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="48" y1="158" x2="502" y2="158" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M514,158 L501,164 L501,152 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="60" y1="158" x2="60" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="37.5" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}2$</div></foreignObject>
  <line x1="131.5" y1="158" x2="131.5" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="109" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}3$</div></foreignObject>
  <line x1="203.5" y1="158" x2="203.5" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="181" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}4$</div></foreignObject>
  <line x1="275" y1="158" x2="275" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="252.5" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}5$</div></foreignObject>
  <line x1="346.5" y1="158" x2="346.5" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="324" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}6$</div></foreignObject>
  <line x1="418.5" y1="158" x2="418.5" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="396" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}7$</div></foreignObject>
  <line x1="490" y1="158" x2="490" y2="165" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="467.5" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}8$</div></foreignObject>
  <foreignObject x="520" y="143.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="74.5" y="43.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\text{oikea arvo}$</div></foreignObject>
  <foreignObject x="217.5" y="43.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{keskiarvo}$</div></foreignObject>
  <foreignObject x="14" y="207.5" width="470" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Systemaattinen virhe: tulokset siirtyvät}$</div></foreignObject>
  <line x1="203.5" y1="354" x2="203.5" y2="268" stroke="#2b8a3e" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 6"/>
  <line x1="342.5" y1="354" x2="342.5" y2="268" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="303.5" cy="342" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="318" cy="342" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="342" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="326" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="346.5" cy="342" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="346.5" cy="326" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="346.5" cy="310" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="346.5" cy="294" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="361" cy="342" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="375.5" cy="342" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="48" y1="354" x2="502" y2="354" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M514,354 L501,360 L501,348 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="60" y1="354" x2="60" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="37.5" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}2$</div></foreignObject>
  <line x1="131.5" y1="354" x2="131.5" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="109" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}3$</div></foreignObject>
  <line x1="203.5" y1="354" x2="203.5" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="181" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}4$</div></foreignObject>
  <line x1="275" y1="354" x2="275" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="252.5" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}5$</div></foreignObject>
  <line x1="346.5" y1="354" x2="346.5" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="324" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}6$</div></foreignObject>
  <line x1="418.5" y1="354" x2="418.5" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="396" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}7$</div></foreignObject>
  <line x1="490" y1="354" x2="490" y2="361" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="467.5" y="365.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}8$</div></foreignObject>
  <foreignObject x="520" y="339.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="74.5" y="239.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\text{oikea arvo}$</div></foreignObject>
  <foreignObject x="351.5" y="239.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{keskiarvo}$</div></foreignObject>
  <line x1="205.5" y1="288" x2="327.5" y2="288" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M340.5,288 L326.5,294.5 L326.5,281.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="244" y="255.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\delta_\text{sys}$</div></foreignObject>
  <line x1="24" y1="206" x2="576" y2="206" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
</svg>

### Toistettavuus ja oikeellisuus
Mittauksen luotettavuutta kuvataan kahdella asialla. **Toistettavuus** kertoo, kuinka lähelle toisiaan toistetut mittaukset osuvat, ja sitä heikentää satunnaisvirhe. **Oikeellisuus** kertoo, kuinka lähellä keskiarvo on oikeaa arvoa, ja sitä heikentää systemaattinen virhe. Mittaus voi olla toistettava mutta ei oikea, kuten kuvan alempi sarja. Luotettavassa mittauksessa on molemmat.

## Kaava: Keskiarvo ja virhe-arvio
Toistetun mittauksen paras arvio on tulosten keskiarvo:
```latex
\bar{x} = \frac{x_1 + x_2 + \dots + x_n}{n}
```
missä $\bar{x}$ on keskiarvo, $x_1, x_2, \dots, x_n$ ovat yksittäiset mittaustulokset ja $n$ on mittausten lukumäärä. Keskiarvo summaa tulokset ja jakaa summan lukumäärällä, joten yhden tuloksen heitto vaikuttaa siihen sitä vähemmän, mitä enemmän mittauksia on.

Satunnaisvirheen suuruus arvioidaan vaihteluvälin puolikkaana:
```latex
\Delta x = \frac{x_\text{max} - x_\text{min}}{2}
```
missä $\Delta x$ on virhe-arvio, $x_\text{max}$ suurin ja $x_\text{min}$ pienin tulos. Tulos ilmoitetaan muodossa $\bar{x} \pm \Delta x$. Virhe-arvio on karkea arvio, ei tarkka raja: yksittäinen tulos voi joskus jäädä sen ulkopuolelle.

<svg data-fig="range-half" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva, ei lukuarvoja: kuusi mittaustulosta aika-akselilla. Suurin tulos t_max ja pienin tulos t_min rajaavat vaihteluvälin, jonka pituus on t_max − t_min. Keskiarvo on merkitty pystyviivalla. Vaihteluvälin puolikas Δt on arvio satunnaisvirheestä, ja tulos ilmoitetaan muodossa keskiarvo plus miinus Δt." style="max-width:100%;font-size:24px">
  <circle cx="143.5" cy="158" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="196" cy="158" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="227.5" cy="158" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="269.5" cy="158" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="158" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="395.5" cy="158" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="143.5" y1="144" x2="143.5" y2="104" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="395.5" y1="144" x2="395.5" y2="104" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="151.5" y1="114" x2="376.5" y2="114" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M387.5,114 L375.5,119.5 L375.5,108.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="387.5" y1="114" x2="162.5" y2="114" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M151.5,114 L163.5,108.5 L163.5,119.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="209.5" y="67.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{max} - t_\text{min}$</div></foreignObject>
  <line x1="58" y1="170" x2="502" y2="170" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M514,170 L501,176 L501,164 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="520" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="114.5" y="181.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{min}$</div></foreignObject>
  <foreignObject x="366.5" y="181.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t_\text{max}$</div></foreignObject>
  <path d="M260.75,177 L252.75,192 L268.75,192 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="244" y="199.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\bar{t}$</div></foreignObject>
  <rect x="134.5" y="236" width="252" height="16" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/>
  <line x1="261" y1="230" x2="261" y2="258" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="54.5" y="229.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\bar{t} - \Delta t$</div></foreignObject>
  <foreignObject x="397" y="229.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\bar{t} + \Delta t$</div></foreignObject>
  <foreignObject x="221" y="263" width="158" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t = \dfrac{t_\text{max} - t_\text{min}}{2}$</div></foreignObject>
</svg>

Virhe-arvio pyöristetään yhteen merkitsevään numeroon, tai kahteen, jos ensimmäinen numero on 1. Tulos pyöristetään samaan desimaaliin: $3{,}18 \pm 0{,}12\,\text{s}$ eikä $3{,}1817 \pm 0{,}12\,\text{s}$. Näin tuloksessa ei ole numeroita, jotka virhe jo sotkee. Kun mittaus tehdään vain kerran, virhe-arvio on puoli asteikkoväliä $d$:
```latex
\Delta x = \frac{d}{2}
```
Viivaimella, jonka pienin asteikkoväli on $1{,}0\,\text{mm}$, yksittäisen lukeman virhe-arvio on siis $0{,}5\,\text{mm}$.

Virhe-arvion suhdetta tulokseen kutsutaan suhteelliseksi virheeksi:
```latex
\varepsilon = \frac{\Delta x}{\bar{x}} \cdot 100\,\%
```
missä $\varepsilon$ on suhteellinen virhe prosentteina. Se kertoo, onko virhe tuloksen kokoon nähden pieni vai suuri: virhe $0{,}5\,\text{mm}$ on pieni metrin mittaukselle mutta suuri millimetrin paksuiselle langalle.

Systemaattinen virhe arvioidaan mittaamalla suure, jonka oikea arvo tunnetaan, ja vertaamalla keskiarvoon. Tunnettu arvo voi olla esimerkiksi tyhjä vaaka, $0\,{}^\circ\text{C}$ jäävedessä tai tarkasti tunnetun pituinen sauva:
```latex
\Delta x_\text{sys} = \bar{x}_\text{vertailu} - x_\text{oikea}
```
missä $\bar{x}_\text{vertailu}$ on vertailumittausten keskiarvo ja $x_\text{oikea}$ vertailusuureen oikea arvo. Korjattu tulos saadaan vähentämällä virhe lukemasta:
```latex
x = x_\text{lukema} - \Delta x_\text{sys}
```

<svg data-fig="zero-scale" viewBox="0 0 600 392" role="img" aria-label="Kaavakuva, ei mittakaavassa: keittiövaaka kahdesti. Vasemmalla pannu on tyhjä, mutta vaaka näyttää 1,2 g, joten nollakohta on väärin. Oikealla pannulla on rautakappale ja vaaka näyttää 48,7 g. Kappaleen massa saadaan vähentämällä nollalukema lukemasta: 48,7 g miinus 1,2 g on 47,5 g." style="max-width:100%;font-size:24px">
  <rect x="50" y="206" width="200" height="100" rx="10" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="74" y="188" width="152" height="18" rx="6" fill="#8a96a3" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="90" y="238" width="120" height="44" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="115" y="245.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}2\,\text{g}$</div></foreignObject>
  <rect x="350" y="206" width="200" height="100" rx="10" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="374" y="188" width="152" height="18" rx="6" fill="#8a96a3" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="390" y="238" width="120" height="44" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="408.5" y="245.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$48{,}7\,\text{g}$</div></foreignObject>
  <rect x="412" y="128" width="76" height="60" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="424" y1="142" x2="476" y2="142" stroke="#c4ccd4" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="96" y="321.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tyhjä: } m_0$</div></foreignObject>
  <foreignObject x="365" y="321.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lukema } m_\text{lukema}$</div></foreignObject>
  <line x1="300" y1="48" x2="300" y2="352" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="109" y="13.5" width="382" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{systemaattinen virhe: nollakohta}$</div></foreignObject>
  <foreignObject x="221" y="357.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m = m_\text{lukema} - m_0$</div></foreignObject>
</svg>

## Esimerkki
Oppilas mittaa kuulan vierimisajan rampilla käsikellolla kuusi kertaa ja saa tulokset $3{,}12\,\text{s}$, $3{,}25\,\text{s}$, $3{,}07\,\text{s}$, $3{,}31\,\text{s}$, $3{,}19\,\text{s}$ ja $3{,}15\,\text{s}$. Mikä on mittaustulos virhe-arvion kanssa ja kuinka suuri on suhteellinen virhe?

<svg data-fig="example-plot" viewBox="0 0 600 330" role="img" aria-label="Mittaustulokset (t, aika) mittakaavassa: kuusi tulosta väliltä 3,07 s – 3,31 s, keskiarvo 3,18 s ja tulos 3,18 s ± 0,12 s vihreällä palkilla." style="max-width:100%;font-size:24px">
  <line x1="261" y1="150" x2="261" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="196" cy="138" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="332.5" cy="138" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="143.5" cy="138" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="395.5" cy="138" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="269.5" cy="138" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="227.5" cy="138" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="58" y1="150" x2="502" y2="150" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M514,150 L501,156 L501,144 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="150" x2="70" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="175" y1="150" x2="175" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="152.5" y="161.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3{,}1$</div></foreignObject>
  <line x1="280" y1="150" x2="280" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="257.5" y="161.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3{,}2$</div></foreignObject>
  <line x1="385" y1="150" x2="385" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="362.5" y="161.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3{,}3$</div></foreignObject>
  <line x1="490" y1="150" x2="490" y2="157" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="467.5" y="161.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3{,}4$</div></foreignObject>
  <foreignObject x="520" y="135.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="131" y="35.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\bar{t} = 3{,}18\,\text{s}$</div></foreignObject>
  <rect x="134.5" y="236" width="252" height="16" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2.5"/>
  <line x1="261" y1="230" x2="261" y2="258" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="202.5" y="277.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t = 3{,}18\,\text{s} \pm 0{,}12\,\text{s}$</div></foreignObject>
</svg>

<!-- vaihe -->

**Tunnetut ja kysytty.** Mittauksia on $n = 6$, ja pienin tulos on $t_\text{min} = 3{,}07\,\text{s}$ ja suurin $t_\text{max} = 3{,}31\,\text{s}$. Kysytään keskiarvoa $\bar{t}$, virhe-arviota $\Delta t$ ja suhteellista virhettä $\varepsilon$.

<!-- vaihe -->

**Periaate.** Käsin otetussa ajanotossa on satunnaisvirhe, koska reaktioaika vaihtelee. Siksi tulokseksi otetaan keskiarvo ja virhe-arvioksi vaihteluvälin puolikas. Suhteellinen virhe vertaa virhe-arviota tulokseen.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
\bar{t} &= \frac{t_1 + t_2 + \dots + t_n}{n} \\
\Delta t &= \frac{t_\text{max} - t_\text{min}}{2} \\
\varepsilon &= \frac{\Delta t}{\bar{t}} \cdot 100\,\%
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: kaikki ajat ovat sekunteina, ja suhteellinen virhe on yksikötön luku, jonka kerrotaan sadalla prosenteiksi.

<!-- vaihe -->

**Sijoitus.** Tulosten summa on $3{,}12\,\text{s} + 3{,}25\,\text{s} + 3{,}07\,\text{s} + 3{,}31\,\text{s} + 3{,}19\,\text{s} + 3{,}15\,\text{s} = 19{,}09\,\text{s}$. Sijoitetaan se ja muut lukuarvot yksiköineen:
```latex
\begin{aligned}
\bar{t} &= \frac{t_1 + t_2 + \dots + t_n}{n} \\
&= \frac{19{,}09\,\text{s}}{6} \\
&= 3{,}1817\,\text{s}
\\[4pt]
\Delta t &= \frac{t_\text{max} - t_\text{min}}{2} \\
&= \frac{3{,}31\,\text{s} - 3{,}07\,\text{s}}{2} \\
&= 0{,}12\,\text{s}
\\[4pt]
\varepsilon &= \frac{\Delta t}{\bar{t}} \cdot 100\,\% \\
&= \frac{0{,}12\,\text{s}}{3{,}1817\,\text{s}} \cdot 100\,\% \\
&= 3{,}8\,\%
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Virhe-arvio $0{,}12\,\text{s}$ on kahden numeron luku, koska sen ensimmäinen numero on 1. Keskiarvo pyöristetään samaan desimaaliin, joten mittaustulos on $t = 3{,}18\,\text{s} \pm 0{,}12\,\text{s}$. Suhteellinen virhe on $3{,}8\,\%$, kaksi merkitsevää numeroa kuten virhe-arviossa.

<!-- vaihe -->

**Järkevyys.** Väli $3{,}18\,\text{s} \pm 0{,}12\,\text{s}$ eli $3{,}06\,\text{s}$–$3{,}30\,\text{s}$ kattaa viisi kuudesta tuloksesta. Tulos $3{,}31\,\text{s}$ jää juuri sen ulkopuolelle, mikä sopii siihen, että virhe-arvio on karkea. Suhteellinen virhe on muutaman prosentin, mikä on tavallista käsin otetulle ajalle. Toistot kuitenkin kertovat vain satunnaisvirheestä: systemaattisen virheen paljastaisi vasta vertailu toiseen mittaustapaan.

## Yleinen virhekäsitys
Moni ajattelee, että tarkka laite tai paljon toistoja takaavat oikean tuloksen. Toistot pienentävät satunnaisvirhettä mutta eivät systemaattista virhettä, ja hyvä toistettavuus ei kerro oikeellisuudesta. Toinen virhekäsitys on pitää virhettä huolimattomuutena: virhe kuuluu myös taitavan mittaajan tulokseen, ja siksi se ilmoitetaan. Kolmas on laskea keskiarvo erilaisissa yksiköissä olevista luvuista: tulokset muunnetaan ensin samaan yksikköön.

## Tiivistelmä
- Mittausvirhe on tuloksen ja oikean arvon erotus. Virhe kuuluu jokaiseen mittaukseen, ja se arvioidaan ja ilmoitetaan tuloksen mukana.
- Satunnaisvirhe vaihtelee mittauksesta toiseen ja näkyy hajontana. Keskiarvo $\bar{x}$ vaimentaa sitä, ja sen suuruutta arvioidaan vaihteluvälin puolikkaalla $\Delta x$.
- Systemaattinen virhe siirtää kaikkia tuloksia samaan suuntaan, eikä toistaminen poista sitä. Se huomataan vertailuarvolla ja korjataan: $x = x_\text{lukema} - \Delta x_\text{sys}$.
- Toistettavuus kertoo satunnaisvirheestä ja oikeellisuus systemaattisesta virheestä. Luotettava mittaus on sekä toistettava että oikea.
- Tulos ilmoitetaan muodossa $\bar{x} \pm \Delta x$ yksikköineen. Virhe-arvio pyöristetään yhteen merkitsevään numeroon (kahteen, jos ensimmäinen numero on 1), ja tulos samaan desimaaliin.
