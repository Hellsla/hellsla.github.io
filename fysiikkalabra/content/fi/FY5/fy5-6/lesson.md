# Satelliitit ja planeetat ympyräradalla

> **Miksi** Kansainvälinen avaruusasema ISS ei putoa Maahan, ja miksi astronautit leijuvat sen sisällä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: Kansainvälinen avaruusasema ISS kiertää Maata mustaa avaruutta vasten. Aseman poikki kulkee pitkä ristikkorunko, jonka kummassakin päässä on kaksi paria suuria kullanruskeita aurinkopaneelisiipiä. Rungon keskeltä lähtee sen poikki lieriön muotoisten asuinmoduulien ketju, ja rungosta riippuu valkoisia jäähdytyspaneeleita. Alhaalla näkyy Maan kaareutuva reuna: sinistä merta, vihreää ja ruskeaa maata, valkoisia pilviä ja ohut sininen ilmakehä." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-6-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Kappaletta, joka kiertää toista kappaletta gravitaation varassa, kutsutaan satelliitiksi. Kuu on Maan luonnollinen satelliitti, ISS ja sääsatelliitit ovat ihmisen rakentamia. Rataa, jota pitkin satelliitti kiertää, kutsutaan kiertoradaksi. Satelliittiin vaikuttaa avaruudessa käytännössä vain yksi voima: Maan gravitaatiovoima, joka osoittaa kohti Maan keskipistettä. Koska se on ainoa voima, se on myös kokonaisvoima. Luvussa *Normaalikiihtyvyys ja ympyräliikkeen liikeyhtälö* todettiin, että tasaisessa ympyräliikkeessä kokonaisvoima osoittaa radan keskipisteeseen ja antaa kappaleelle normaalikiihtyvyyden. Ympyräradalla gravitaatiovoima tekee juuri tämän: se on kohtisuorassa nopeuteen nähden, joten se ei muuta vauhtia vaan kääntää nopeuden suuntaa koko ajan.

<svg data-fig="orbit" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei mittakaavassa: satelliitti kiertää Maata ympyrärataa, joka on piirretty katkoviivalla. Satelliitti on radan ylimmässä kohdassa. Sininen nopeusnuoli v osoittaa radan tangentin suuntaan oikealle. Punainen gravitaatiovoiman nuoli F osoittaa kohti Maan keskipistettä, ja sen vieressä oranssi normaalikiihtyvyyden nuoli a n osoittaa samaan suuntaan. Ohut katkoviiva jatkaa suoraan oikealle: sitä pitkin satelliitti liikkuisi ilman gravitaatiota." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-6-orbit.webp" x="-1.3" y="0" width="603" height="370.6" preserveAspectRatio="none"/>
  <foreignObject x="177.5" y="225.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Maa}$</div></foreignObject>
  <foreignObject x="339" y="47.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{ilman gravitaatiota}$</div></foreignObject>
  <foreignObject x="349.5" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="207.5" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="125.5" y="127.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
  <foreignObject x="268" y="133.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="412" y="141.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ainoa voima}$</div></foreignObject>
  <foreignObject x="412" y="177.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="412" y="213.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kohti Maan}$</div></foreignObject>
  <foreignObject x="412" y="247.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{keskipistettä}$</div></foreignObject>
  <foreignObject x="412" y="297.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\overline{F} = m\,\overline{a}_\text{n}$</div></foreignObject>
</svg>

Satelliitti siis putoaa koko ajan kohti Maata, mutta ei osu siihen. Ilman gravitaatiota se jatkaisi suoraan radan tangentin suuntaan. Gravitaatio taivuttaa rataa, ja kun vauhti on juuri sopiva, rata kaartuu samaa tahtia kuin Maan pinta kaartuu satelliitin alla. Silloin etäisyys Maan keskipisteestä pysyy samana ja rata on ympyrä.

```pysahdy
Mitä satelliitille tapahtuisi, jos Maan gravitaatio yhtäkkiä lakkaisi vaikuttamasta?
---
Mikään voima ei taivuttaisi rataa, joten satelliitti jatkaisi suoraan radan tangentin suuntaan samalla vauhdilla. Se ei putoaisi Maahan eikä kiertäisi enää ympyrää.
```

Jos nopeus on pienempi, gravitaatio kääntää rataa jyrkemmin kuin ympyrä vaatisi: satelliitti laskeutuu alemmas ja palaa sitten lähtökorkeudelle, tai osuu Maahan, jos nopeus on paljon liian pieni. Jos nopeus on suurempi, rata kaartuu loivemmin ja satelliitti nousee kauemmas ennen paluutaan. Näissä tapauksissa rata ei ole ympyrä vaan soikea, eikä tasaisen ympyräliikkeen malli kuvaa sitä.

<svg data-fig="cannon" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva, ei mittakaavassa: kappale lähtee vaakasuoraan samasta pisteestä Maan yläpuolelta kolmella nopeudella. Radat on laskettu gravitaatiolaista. Liian pienellä nopeudella rata kaartuu jyrkemmin kuin ympyrä ja osuu Maahan. Ympyräradan nopeudella kappale kiertää lähtöpisteen etäisyydellä pysyvää ympyrää. Suuremmalla nopeudella rata kaartuu loivemmin, ja kappale loittonee kauemmas ja palaa lähtöpisteeseen. Tämä rata on ellipsi, jonka Maata lähin piste on lähtöpiste." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-6-cannon.webp" x="0" y="0" width="600" height="386.2" preserveAspectRatio="none"/>
  <foreignObject x="213.5" y="147.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Maa}$</div></foreignObject>
  <foreignObject x="323.5" y="21.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="444" y="135.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{liian hidas}$</div></foreignObject>
  <foreignObject x="444" y="179.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ympyrärata}$</div></foreignObject>
  <foreignObject x="444" y="223.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{liian nopea}$</div></foreignObject>
</svg>

## Kaava: Ratanopeus ympyräradalla
Kun satelliitti, jonka massa on $m$, kiertää ympyrärataa keskuskappaleen ympäri, gravitaatiovoima on ainoa voima ja siis kokonaisvoima. Newtonin toisen lain mukaan sen on oltava yhtä suuri kuin ympyräliikkeeseen tarvittava voima $m a_\text{n} = \tfrac{m v^2}{r}$:
```latex
\gamma \frac{M m}{r^2} = \frac{m v^2}{r}
```
missä $\gamma = 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}$ on gravitaatiovakio, $M$ keskuskappaleen massa ($\text{kg}$), $m$ satelliitin massa ($\text{kg}$), $r$ radan säde ($\text{m}$) ja $v$ satelliitin ratanopeus ($\text{m/s}$). Radan säde mitataan keskuskappaleen keskipisteestä: Maan satelliitille $r = R + h$, missä $R = 6371\,\text{km}$ on Maan säde ja $h$ satelliitin korkeus maanpinnasta.

Satelliitin massa $m$ on yhtälön kummallakin puolella ja supistuu pois. Kun yhtälö kerrotaan puolittain luvulla $r$ ja jaetaan massalla $m$, saadaan $v^2 = \tfrac{\gamma M}{r}$, joten ympyräradan ratanopeus on
```latex
v = \sqrt{\frac{\gamma M}{r}}
```
Ratanopeus riippuu vain keskuskappaleen massasta $M$ ja radan säteestä $r$, ei satelliitin massasta. Raskas avaruusasema ja pieni kuutiosatelliitti kiertävät samalla korkeudella samalla nopeudella. Mitä kauempana satelliitti kiertää, sitä pienempi sen ratanopeus on.

<svg data-fig="vr" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja mittakaavassa: ympyräradan ratanopeus v kilometreinä sekunnissa etäisyyden r funktiona, kun r on Maan keskipisteestä mitattu etäisyys tuhansina kilometreinä. Käyrä alkaa Maan pinnalta, r on 6 371 km ja v noin 7,9 km/s, ja laskee loivenevasti: kaukana kiertävä satelliitti liikkuu hitaammin. Käyrälle on merkitty pisteinä ISS (r 6 790 km, v 7,65 km/s), GPS-satelliitti (r 26 560 km, v 3,87 km/s) ja geostationaarinen satelliitti (r 42 164 km, v 3,07 km/s), jotka on laskettu todellisista kiertoajoista." style="max-width:100%;font-size:24px">
  <line x1="126.5" y1="300" x2="126.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="163.5" y1="300" x2="163.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="300" x2="200" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="236.5" y1="300" x2="236.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="273.5" y1="300" x2="273.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="310" y1="300" x2="310" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="346.5" y1="300" x2="346.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="383.5" y1="300" x2="383.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="300" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="273.5" x2="420" y2="273.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="246.5" x2="420" y2="246.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="220" x2="420" y2="220" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="193.5" x2="420" y2="193.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="166.5" x2="420" y2="166.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="140" x2="420" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="113.5" x2="420" y2="113.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="86.5" x2="420" y2="86.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="60" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="300" x2="434" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M446,300 L433,306 L433,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="301" x2="90" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,34 L96,47 L84,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="126.5" y1="300" x2="126.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="163.5" y1="300" x2="163.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="147" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="200" y1="300" x2="200" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="236.5" y1="300" x2="236.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="273.5" y1="300" x2="273.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="310" y1="300" x2="310" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="293.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="346.5" y1="300" x2="346.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="383.5" y1="300" x2="383.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="367" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="420" y1="300" x2="420" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="273.5" x2="90" y2="273.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="246.5" x2="90" y2="246.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="232" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="83" y1="220" x2="90" y2="220" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="193.5" x2="90" y2="193.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="179" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="83" y1="166.5" x2="90" y2="166.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="140" x2="90" y2="140" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="125.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="83" y1="113.5" x2="90" y2="113.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="83" y1="86.5" x2="90" y2="86.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="72" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="83" y1="60" x2="90" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="60" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="452" y="285.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r\ (1000\,\text{km})$</div></foreignObject>
  <foreignObject x="80" y="3.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\text{km/s})$</div></foreignObject>
  <polyline points="136.5,89 139,94 141.5,99 144,103.5 146,107.5 148.5,111.5 151,115.5 153,118.5 155.5,122 158,125 160.5,128 162.5,131 165,133.5 167.5,136 170,138.5 172,141 174.5,143 177,145.5 179,147.5 181.5,149.5 184,151.5 186.5,153 188.5,155 191,156.5 193.5,158 195.5,160 198,161.5 200.5,163 203,164.5 205,165.5 207.5,167 210,168.5 212.5,169.5 214.5,171 217,172 219.5,173.5 221.5,174.5 224,175.5 226.5,176.5 229,177.5 231,178.5 233.5,179.5 236,180.5 238,181.5 240.5,182.5 243,183.5 245.5,184.5 247.5,185 250,186 252.5,187 255,187.5 257,188.5 259.5,189.5 262,190 264,191 266.5,191.5 269,192 271.5,193 273.5,193.5 276,194.5 278.5,195 280.5,195.5 283,196.5 285.5,197 288,197.5 290,198 292.5,198.5 295,199.5 297,200 299.5,200.5 302,201 304.5,201.5 306.5,202 309,202.5 311.5,203 314,203.5 316,204 318.5,204.5 321,205 323,205.5 325.5,206 328,206.5 330.5,207 332.5,207.5 335,208 337.5,208.5 339.5,209 342,209 344.5,209.5 347,210 349,210.5 351.5,211 354,211.5 356.5,211.5 358.5,212 361,212.5 363.5,213 365.5,213 368,213.5 370.5,214 373,214.5 375,214.5 377.5,215 380,215.5 382,215.5 384.5,216 387,216.5 389.5,216.5 391.5,217 394,217.5 396.5,217.5 399,218 401,218.5 403.5,218.5 406,219 408,219 410.5,219.5 413,220 415.5,220 417.5,220.5 420,220.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="140" cy="96" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="156" y="59.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{ISS}$</span></div></foreignObject>
  <circle cx="285" cy="196.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="262.5" y="152" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{GPS}$</span></div></foreignObject>
  <circle cx="399" cy="218" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="203" y="233.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{geostationaarinen}$</span></div></foreignObject>
  <foreignObject x="235" y="95" width="150" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$v = \sqrt{\dfrac{\gamma M}{r}}$</div></foreignObject>
</svg>

Yhden kierroksen aikana satelliitti kulkee ympyrän kehän $2\pi r$, joten kiertoaika saadaan luvun *Normaalikiihtyvyys ja ympyräliikkeen liikeyhtälö* yhteydestä $v = \tfrac{2\pi r}{T}$:
```latex
T = \frac{2\pi r}{v}
```
missä $T$ on kiertoaika ($\text{s}$). Kaukana kiertävän satelliitin rata on pidempi ja sen vauhti pienempi, joten kiertoaika kasvaa nopeasti etäisyyden kasvaessa: ISS kiertää Maan noin puolessatoista tunnissa, Kuu noin $27\,\text{d}$:ssä. Kun satelliitin säde ja kiertoaika mitataan, samasta yhtälöstä voidaan ratkaista myös keskuskappaleen massa $M$. Näin on määritetty esimerkiksi Maan, Auringon ja Marsin massat.

```pysahdy
Satelliitti kiertää ympyrärataa vauhdilla $3{,}0\,\text{km/s}$, ja yksi kierros kestää $4{,}0\,\text{h}$. Kuinka pitkä rata on?
---
Rata on yhden kierroksen matka, joten $2\pi r = vT$. Siis $vT = 3{,}0 \cdot 10^{3}\,\text{m/s} \cdot 14\,400\,\text{s}$, mikä on noin $4{,}3 \cdot 10^{7}\,\text{m}$ eli $43\,000\,\text{km}$.
```

### Geostationaarinen rata
Geostationaarinen satelliitti kiertää päiväntasaajan yläpuolella samaan suuntaan kuin Maa pyörii, ja sen kiertoaika on sama kuin Maan pyörähdysaika, $23\,\text{h}\;56\,\text{min}$. Siksi se näyttää pysyvän taivaalla paikallaan, ja lautasantennin voi suunnata siihen kerran. Koska kiertoaika määrää radan säteen, kaikki geostationaariset satelliitit kiertävät samalla korkeudella, noin $35\,800\,\text{km}$:n korkeudella.

## Painottomuus
Avaruusasemalla astronautit leijuvat, ja vaaka näyttäisi nollaa. Syy ei ole painovoiman puuttuminen. ISS:n korkeudella $420\,\text{km}$ gravitaatiovoiman antama kiihtyvyys on $\tfrac{\gamma M}{r^2} \approx 8{,}6\,\text{m/s}^2$, noin $88\,\%$ maanpinnan arvosta. Astronauttiin, jonka massa on $70\,\text{kg}$, vaikuttaa siis noin $605\,\text{N}$:n paino eli Maan gravitaatiovoima $F$, kun maanpinnalla se olisi $687\,\text{N}$.

Asema ja astronautti ovat vapaassa pudotuksessa: kumpaankin vaikuttaa vain gravitaatio, ja kumpikin saa saman kiihtyvyyden kohti Maata. Koska ne putoavat samalla tavalla, lattia ei paina astronauttia eikä vaaka joudu tukemaan häntä, joten tukivoima on nolla. **Painottomuus on tuettomuutta ja yhteistä vapaata putoamista: kappaleeseen vaikuttaa vain gravitaatio, ja se putoaa samalla kiihtyvyydellä kuin ympäristönsä. Tukivoima on nolla, vaikka paino vaikuttaa koko ajan.**

<svg data-fig="paino" viewBox="0 0 600 380" role="img" aria-label="Kaksi voimakuviota samassa mittakaavassa. Vasemmalla astronautti seisoo vaa&#x27;alla Maan pinnalla, ja hänet on piirretty suorakulmiona: gravitaatiovoima F (paino) osoittaa keskipisteestä alas ja vaa&#x27;an tukivoima N alapinnasta ylös, yhtä pitkinä, joten kiihtyvyys on nolla. Oikealla sama astronautti avaruusasemalla: ainoa voima on noin 12 prosenttia lyhyempi gravitaatiovoima F, tukivoimaa ei ole, ja oranssi kiihtyvyysnuoli a osoittaa alas kohti Maata kappaleen vieressä. Asema putoaa samalla kiihtyvyydellä, joten lattia ei paina astronauttia." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-6-paino.webp" x="1.2" y="1.2" width="597" height="386.8" preserveAspectRatio="none"/>
  <foreignObject x="71" y="11.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Maan pinnalla}$</div></foreignObject>
  <foreignObject x="352.5" y="11.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{avaruusasemalla}$</div></foreignObject>
  <foreignObject x="111.5" y="267" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="175.5" y="140" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="115" y="341.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{a} = \overline{0}$</div></foreignObject>
  <foreignObject x="411.5" y="256" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="511.5" y="203.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="427.5" y="341.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$N = 0$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy5/iss-from-soyuz.webp" alt="Kansainvälinen avaruusasema aurinkopaneeleineen mustaa avaruutta vasten. Alla näkyy Maan pilvinen pinta."><figcaption>Kansainvälinen avaruusasema ISS kuvattuna Sojuz-aluksesta lokakuussa 2018. Asema on koko ajan vapaassa pudotuksessa kohti Maata, mutta sen ratanopeus on niin suuri, että se ei osu Maahan.</figcaption></figure>

Saman tilan voi kokea hetken maan päälläkin: hypyn aikana, vapaasti putoavassa hississä tai lentokoneessa, joka lentää moottorit säädettyinä heittoliikkeen rataa. Painottomuutta ei selitä mikään gravitaation kumoava "keskipakoisvoima". Jos jokin voima kumoaisi gravitaation, kokonaisvoima olisi nolla, ja asema jatkaisi suoraan eteenpäin eikä kiertäisi Maata.

## Milloin ympyrämalli pätee
Tasaisen ympyräliikkeen malli on yksinkertaistus. Se kuvaa satelliitin liikettä hyvin, kun

- keskuskappale on paljon massiivisempi kuin satelliitti, joten sitä voidaan pitää paikallaan pysyvänä,
- muiden kappaleiden gravitaatio ja ilmanvastus ovat niin pieniä, että vain keskuskappaleen gravitaatio vaikuttaa,
- satelliitin nopeus on juuri sen radan säteen ympyräradan nopeus, jolloin etäisyys keskipisteestä pysyy vakiona.

Todellisessa satelliitin liikkeessä on aina pieniä poikkeamia mallista. Matalalla radalla ohut yläilmakehä jarruttaa liikettä, Kuun ja Auringon gravitaatio vetää satelliittia, eikä Maan massa jakaudu täsmälleen pallosymmetrisesti, koska Maa on navoiltaan hieman litistynyt. Yläilmakehän jarrutuksen vuoksi esimerkiksi ISS:n rataa nostetaan ajoittain rakettimoottoreilla.

Monet todelliset radat ovat lähes ympyröitä. Maan etäisyys Auringosta vaihtelee vain noin $3\,\%$ keskietäisyydestä, joten ympyrämalli kuvaa Maan rataa hyvin. Kuun etäisyys Maasta vaihtelee noin $11\,\%$, joten malli antaa Kuulle hyvän likiarvon. Halleyn komeetan rata on sen sijaan hyvin pitkänomainen, eikä ympyrämalli sovi siihen lainkaan.

| Kappale | lähin etäisyys | suurin etäisyys |
| --- | --- | --- |
| Maa | $147{,}1\,\text{milj. km}$ | $152{,}1\,\text{milj. km}$ |
| Kuu | $363\,300\,\text{km}$ | $405\,500\,\text{km}$ |
| Halleyn komeetta | $88\,\text{milj. km}$ | $5250\,\text{milj. km}$ |

Maan ja Halleyn komeetan etäisyydet on mitattu Auringosta, Kuun etäisyys Maasta. Lähde: NASA, Planetary Fact Sheets (Earth, Moon) ja Halleyn komeetan ratatiedot, 2024.

<svg data-fig="radat" viewBox="0 0 600 360" role="img" aria-label="Kaksi rataa, kumpikin omassa mittakaavassaan, Aurinko radan polttopisteessä. Vasemmalla Maan rata: pienin etäisyys Auringosta 147,1 miljoonaa kilometriä ja suurin 152,1 miljoonaa kilometriä. Rata on piirretty yhtenäisellä viivalla ja sen päälle katkoviivalla ympyrä, eikä niitä erota toisistaan. Oikealla Halleyn komeetan rata: pienin etäisyys 88 miljoonaa kilometriä ja suurin noin 5 250 miljoonaa kilometriä, erittäin pitkänomainen ellipsi." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-6-radat.webp" x="0" y="0" width="600" height="367.5" preserveAspectRatio="none"/>
  <foreignObject x="96" y="11.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Maan rata}$</div></foreignObject>
  <foreignObject x="327.5" y="11.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Halleyn komeetan rata}$</div></foreignObject>
  <foreignObject x="52" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Maa}$</div></foreignObject>
  <foreignObject x="14" y="309.5" width="272" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$147{,}1\text{–}152{,}1\ \text{milj. km}$</div></foreignObject>
  <foreignObject x="328" y="123.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{komeetta}$</div></foreignObject>
  <foreignObject x="483" y="207.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{Aurinko}$</div></foreignObject>
  <foreignObject x="325" y="309.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$88\text{–}5250\ \text{milj. km}$</div></foreignObject>
</svg>

```pysahdy
Halleyn komeetan etäisyys Auringosta on pienimmillään $88\,\text{milj. km}$ ja suurimmillaan $5250\,\text{milj. km}$. Sopiiko ympyrämalli sen rataan?
---
Ei sovi. Suurin etäisyys on noin $60$-kertainen pienimpään verrattuna, mutta ympyräradalla etäisyys keskuskappaleesta pysyisi vakiona.
```

Pienet poikkeamat mallista näkyvät tarkoissa mittauksissa. Kuun mitatuista arvoista laskettu ratanopeus $1{,}023\,\text{km/s}$ on noin $0{,}5\,\%$ suurempi kuin mallin antama $1{,}018\,\text{km/s}$, koska Kuun massa on noin $\tfrac{1}{81}$ Maan massasta: Maa ja Kuu kiertävät yhteistä massakeskipistettä, eikä Maa pysy paikallaan. ISS:n korkeudella ohut ilma jarruttaa asemaa ja rata madaltuu hitaasti, joten asemaa nostetaan moottoreilla säännöllisesti.

## Esimerkki
Kansainvälinen avaruusasema ISS kiertää Maata lähes ympyrärataa noin $420\,\text{km}$:n korkeudella. Laske aseman ratanopeus ja kiertoaika. Maan massa on $M = 5{,}97 \cdot 10^{24}\,\text{kg}$ ja säde $R = 6371\,\text{km}$. Ilmanvastus jätetään huomiotta.

<!-- vaihe -->

**Tunnetut ja kysytty.** Korkeus $h = 420\,\text{km}$, Maan massa $M = 5{,}97 \cdot 10^{24}\,\text{kg}$ ja säde $R = 6371\,\text{km}$, gravitaatiovakio $\gamma = 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2}$.

Kysytään ratanopeutta $v$ ja kiertoaikaa $T$.

<!-- vaihe -->

**Periaate.** Asemaan vaikuttaa vain Maan gravitaatiovoima, kun ilmanvastus jätetään huomiotta. Se on siis kokonaisvoima ja antaa ympyräradalla normaalikiihtyvyyden kohti Maan keskipistettä: $\gamma \tfrac{Mm}{r^2} = \tfrac{mv^2}{r}$. Radan säde mitataan Maan keskipisteestä, joten $r = R + h$.

<!-- vaihe -->

**Kaava ratkaistuna.** Aseman massa supistuu pois:
```latex
\begin{aligned}
r &= R + h \\
v &= \sqrt{\frac{\gamma M}{r}} \\
T &= \frac{2\pi r}{v}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Etäisyydet metreiksi: $R = 6371\,\text{km} = 6{,}371 \cdot 10^{6}\,\text{m}$ ja $h = 420\,\text{km} = 0{,}420 \cdot 10^{6}\,\text{m}$, joten $r = 6{,}791 \cdot 10^{6}\,\text{m}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&v = \sqrt{\frac{\gamma M}{r}} \\
&\gamma M = 6{,}674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2} \\
&\quad \cdot 5{,}97 \cdot 10^{24}\,\text{kg} \\
&\quad = 3{,}98438 \cdot 10^{14}\,\text{m}^3/\text{s}^2 \\
&v = \sqrt{\frac{3{,}98438 \cdot 10^{14}\,\text{m}^3/\text{s}^2}{6{,}791 \cdot 10^{6}\,\text{m}}} \\
&= 7659{,}7\,\text{m/s} \\[6pt]
&T = \frac{2\pi r}{v} \\
&= \frac{2\pi \cdot 6{,}791 \cdot 10^{6}\,\text{m}}{7659{,}7\,\text{m/s}} \\
&= 5570{,}6\,\text{s}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Ratanopeus on $v \approx 7{,}66\,\text{km/s}$ ja kiertoaika $T \approx 5570\,\text{s} \approx 92{,}8\,\text{min}$. Tulokset ilmoitetaan kolmella merkitsevällä numerolla kuten Maan massa $5{,}97 \cdot 10^{24}\,\text{kg}$.

<!-- vaihe -->

**Järkevyys.** NASAn mukaan ISS kiertää Maan noin $92{,}9\,\text{min}$:ssa, joten malli on hyvin lähellä mitattua. Aivan maanpinnan tasolla ympyräradan nopeus olisi $\sqrt{gR} = \sqrt{9{,}81\,\text{m/s}^2 \cdot 6{,}371 \cdot 10^{6}\,\text{m}} \approx 7{,}9\,\text{km/s}$; ISS on hieman kauempana, joten sen nopeus on hieman pienempi, kuten pitääkin.

## Yleinen virhekäsitys
"Avaruudessa ei ole painovoimaa, siksi astronautit leijuvat." Väite on väärä. ISS:n korkeudella gravitaatio on lähes yhtä voimakas kuin maanpinnalla, ja juuri se pitää aseman radallaan. Ilman gravitaatiota asema lentäisi suoraan pois. Astronautit leijuvat, koska he ja asema putoavat vapaasti samalla kiihtyvyydellä.

Toinen virhe on sijoittaa kaavaan $v = \sqrt{\tfrac{\gamma M}{r}}$ korkeus $h$ eikä etäisyyttä Maan keskipisteestä $r = R + h$. ISS:lle se antaisi nopeudeksi noin $31\,\text{km/s}$, nelinkertaisen todelliseen verrattuna. Kolmas virhe on luulla, että raskaan satelliitin täytyy kiertää nopeammin: suurempi massa saa suuremman gravitaatiovoiman, mutta se tarvitsee myös suuremman voiman kääntyäkseen, joten massa supistuu pois.

## Tiivistelmä
- Satelliittiin vaikuttaa vain keskuskappaleen gravitaatiovoima. Se on kokonaisvoima, joka antaa ympyräradalla normaalikiihtyvyyden: $\gamma \tfrac{Mm}{r^2} = \tfrac{mv^2}{r}$.
- Ympyräradan ratanopeus on $v = \sqrt{\tfrac{\gamma M}{r}}$ ja kiertoaika $T = \tfrac{2\pi r}{v}$. Satelliitin massa ei vaikuta, ja kauempana kiertävä satelliitti on hitaampi ja sen kiertoaika on pidempi.
- Radan säde mitataan keskuskappaleen keskipisteestä: $r = R + h$.
- Painottomuus on tuettomuutta ja yhteistä vapaata putoamista: gravitaatio vaikuttaa, mutta tukivoima on nolla.
- Ympyrämalli pätee, kun keskuskappale on paljon satelliittia massiivisempi, muut voimat ovat pieniä ja rata on lähes ympyrä.
