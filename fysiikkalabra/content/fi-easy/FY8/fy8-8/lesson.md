# Atomiydin ja radioaktiivinen hajoaminen

> **Miksi** savuilmaisimen pienestä americiumnäytteestä lähtee koko ajan hiukkasia, ja mitä americiumytimelle tapahtuu, kun hiukkanen lähtee?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: olohuoneen katossa on valkoinen pyöreä savuilmaisin. Osa siitä on piirretty auki. Sisällä kahden metallilevyn välisessä kammiossa on pieni americiumnäyte. Näytteestä lähtee ilmaan lyhyitä violetteja hiukkasratoja. Huoneessa on ikkuna ja kattovalaisin." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-8-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Ydin koostuu nukleoneista
Atomin massasta melkein kaikki on atomin keskellä olevassa ytimessä. Ytimen halkaisija on noin $10^{-15}$–$10^{-14}\,\text{m}$. Atomin halkaisija on noin $10^{-10}\,\text{m}$. Ydin on siis kymmeniätuhansia kertoja atomia pienempi. Ydin koostuu protoneista ja neutroneista. Niiden yhteinen nimi on **nukleoni**. Protonin varaus on $+e$. Neutroni on sähköisesti neutraali eli sillä ei ole varausta.

Ydintä kuvataan kahdella luvulla. **Järjestysluku** $Z$ on protonien määrä, ja se määrää alkuaineen. **Massaluku** $A$ on nukleonien määrä. Neutroniluku on siis $N = A - Z$. Ydin merkitään ${}^{A}_{Z}\text{X}$, missä X on alkuaineen tunnus. Saman alkuaineen ytimiä, joissa on eri määrä neutroneja, sanotaan alkuaineen **isotoopeiksi**. Hiili-12 ${}^{12}_{6}\text{C}$ ja hiili-14 ${}^{14}_{6}\text{C}$ ovat hiilen isotooppeja. Tietyn ydinlajin nimi on nuklidi.

<svg data-fig="isotopes" viewBox="0 0 600 340" role="img" aria-label="Kaksi hiilen ydintä vierekkäin, ei mittakaavassa. Vasemmalla on hiili-12: kuusi punaista protonia ja kuusi harmaata neutronia. Merkinnässä luku 12 on yläindeksinä ja luku 6 alaindeksinä C:n edessä. Oikealla on hiili-14: kuusi protonia ja kahdeksan neutronia. Molemmissa on kuusi protonia, joten ne ovat saman alkuaineen isotooppeja. Alhaalla on selite: punainen pallo on protoni ja harmaa pallo on neutroni." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-8-isotopes.webp" x="0" y="0" width="600" height="352.5" preserveAspectRatio="none"/>
  <foreignObject x="99" y="204" width="102" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">${}^{12}_{\phantom{1}6}\text{C}$</div></foreignObject>
  <foreignObject x="100.5" y="247.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Z = 6,\ N = 6$</div></foreignObject>
  <foreignObject x="399" y="204" width="102" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px">${}^{14}_{\phantom{1}6}\text{C}$</div></foreignObject>
  <foreignObject x="400.5" y="247.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Z = 6,\ N = 8$</div></foreignObject>
  <foreignObject x="190" y="297.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{protoni } p^+$</div></foreignObject>
  <foreignObject x="400" y="297.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{neutroni } n$</div></foreignObject>
</svg>

```pysahdy
Natriumytimen merkintä on ${}^{23}_{11}\text{Na}$. Montako protonia ja montako neutronia ytimessä on?
---
Protoneja on $Z = 11$. Neutroneja on $N = A - Z = 23 - 11 = 12$.
```

### Miksi osa ytimistä hajoaa
Protonit hylkivät toisiaan sähköisesti, mutta ydin pysyy silti koossa. Sen aiheuttaa vahva vuorovaikutus. Se vetää nukleoneja toisiinsa, mutta vain hyvin lyhyellä matkalla, ytimen kokoisella etäisyydellä. Neutronit lisäävät vetoa, mutta eivät lisää hylkimistä. Siksi pysyvissä raskaissa ytimissä on enemmän neutroneja kuin protoneja.

Vain tietyt protonien ja neutronien yhdistelmät ovat pysyviä. Piirrä ytimet nuklidikarttaan, jonka akseleilla ovat $N$ ja $Z$. Silloin pysyvät ytimet muodostavat kapean vyön. Vyön ulkopuolella oleva ydin on epävakaa eli **radioaktiivinen**. Se hajoaa ajan myötä itsestään ja lähettää samalla säteilyä. Alfa- ja beetahajoamisessa ydin muuttuu toiseksi nuklidiksi. Gammahajoamisessa viritetty ydin vain siirtyy alemmalle energiatasolle ja pysyy samana nuklidina. Yksittäisen ytimen hajoamishetkeä ei voi ennustaa, koska hajoaminen on satunnaista.

<svg data-fig="chart" viewBox="0 0 600 380" role="img" aria-label="Nuklidikartta kaavamaisesti: vaaka-akselilla on neutroniluku N nollasta 140:een ja pystyakselilla järjestysluku Z nollasta 90:een. Vihreä vyö on pysyvien ytimien alue. Kevyillä ytimillä vyö kulkee katkoviivan N = Z lähellä. Raskailla ytimillä vyö kaartuu viivan alapuolelle, koska raskaissa pysyvissä ytimissä on enemmän neutroneja kuin protoneja. Vyön alapuolella neutroneja on liikaa, ja ydin hajoaa beeta miinus -hajoamisella. Vyön yläpuolella neutroneja on liian vähän, ja ydin hajoaa beeta plus -hajoamisella. Vyön yläpäässä, missä Z on yli 82, raskaat ytimet hajoavat usein alfahajoamisella. Violetti nuoli vyön yläpään oikealla puolella osoittaa vinosti alas vasemmalle, koska alfahajoaminen pienentää sekä neutroniluvun että järjestysluvun kahdella." style="max-width:100%;font-size:24px">
  <line x1="135.5" y1="336" x2="135.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="191.5" y1="336" x2="191.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="247" y1="336" x2="247" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="303" y1="336" x2="303" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="358.5" y1="336" x2="358.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="414.5" y1="336" x2="414.5" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="336" x2="470" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="278" x2="470" y2="278" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="220.5" x2="470" y2="220.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="162.5" x2="470" y2="162.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="105" x2="470" y2="105" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="79" y1="336" x2="484" y2="336" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,336 L483,342 L483,330 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="337" x2="80" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,50 L86,63 L74,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="135.5" y1="336" x2="135.5" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="119" y="345.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="191.5" y1="336" x2="191.5" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="175" y="345.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="247" y1="336" x2="247" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="230.5" y="345.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="303" y1="336" x2="303" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="286.5" y="345.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="358.5" y1="336" x2="358.5" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="336" y="345.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="414.5" y1="336" x2="414.5" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="392" y="345.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$120$</div></foreignObject>
  <line x1="470" y1="336" x2="470" y2="343" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="345.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$140$</div></foreignObject>
  <line x1="73" y1="278" x2="80" y2="278" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="263.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="73" y1="220.5" x2="80" y2="220.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="206" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="73" y1="162.5" x2="80" y2="162.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="148" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="73" y1="105" x2="80" y2="105" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="90.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <foreignObject x="50" y="341.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="321.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N$</div></foreignObject>
  <foreignObject x="70" y="19.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Z$</div></foreignObject>
  <polyline points="80,336 330.5,76" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="7 6"/>
  <foreignObject x="135.5" y="194.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$N = Z$</div></foreignObject>
  <polygon points="88,315.5 94,310 100,304.5 106,299.5 112,294 118,289 124.5,284 130.5,278.5 137,273.5 143,268.5 149.5,263.5 156,259 162.5,254 169,249 175.5,244.5 182,239.5 188.5,235 195,230 202,225.5 208.5,221 215,216 222,211.5 228.5,207 235.5,202.5 242.5,198 249,193.5 256,189 263,185 270,180.5 276.5,176 283.5,171.5 290.5,167.5 297.5,163 305,159 312,154.5 319,150.5 326,146 333,142 340.5,138 347.5,134 354.5,129.5 362,125.5 369,121.5 376.5,117.5 383.5,113.5 391,109.5 398,105.5 405.5,101.5 412.5,97.5 420,93.5 427.5,89.5 439.5,102.5 432.5,106.5 425,110 417.5,114 410.5,118 403,122 396,126 388.5,130 381.5,134 374,138.5 367,142.5 359.5,146.5 352.5,150.5 345.5,155 338,159 331,163 324,167.5 317,171.5 310,176 303,180 296,184.5 289,188.5 282,193 275,197.5 268,202 261.5,206.5 254.5,211 247.5,215.5 241,220 234,224.5 227.5,229 220.5,233.5 214,238 207.5,243 201,247.5 194,252 187.5,257 181,262 174.5,266.5 168,271.5 162,276.5 155.5,281.5 149,286.5 143,291.5 136.5,296.5 130.5,301.5 124.5,307 118.5,312 112,317.5 106.5,323 100.5,328.5" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2"/>
  <foreignObject x="314" y="258" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{liikaa neutroneja: } \beta^-$</div></foreignObject>
  <foreignObject x="91" y="125" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{liian vähän: } \beta^+$</div></foreignObject>
  <circle cx="467" cy="73" r="5" fill="#7048e8" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="464" y1="76" x2="455.5" y2="85.5" stroke="#7048e8" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M447.5,93.5 L452,81 L460,88.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="427.5" y="53" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$\alpha$</div></foreignObject>
  <line x1="266.5" y1="197.5" x2="347.5" y2="197.5" stroke="#2b8a3e" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="353" y="183" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\text{pysyvät}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy8/cloud-chamber-beta.webp" alt="Mustalla pohjalla on paljon ohuita, mutkittelevia valkoisia viivoja."><figcaption>Beetahiukkasten jälkiä sumukammiossa. Beetahiukkanen on elektroni. Se on kevyt ja ionisoi ilmaa vähemmän kuin alfahiukkanen. Siksi jälki on ohut ja pitkä. Jälki mutkittelee, koska elektroni muuttaa helposti suuntaa.</figcaption></figure>

<figure class="unit-photo"><img src="pics/fy8/cloud-chamber-alpha.webp" alt="Mustalla pohjalla on paljon lyhyitä, paksuja valkoisia viivoja."><figcaption>Alfahiukkasten jälkiä sumukammiossa. Alfahiukkanen ionisoi ilmaa voimakkaasti. Se menettää energiansa muutamassa senttimetrissä. Siksi jälki on lyhyt, paksu ja suora.</figcaption></figure>

### Alfa-, beeta- ja gammahajoaminen
**Alfahajoamisessa** ytimestä lähtee alfahiukkanen eli heliumydin ${}^{4}_{2}\text{He}$. Siinä on kaksi protonia ja kaksi neutronia. Alfahajoaminen on tyypillistä raskaille ytimille, kuten uraanille, radiumille ja savuilmaisimen americiumille.

**Beetahajoamisessa** ytimessä on liikaa tai liian vähän neutroneja protoneihin verrattuna. Beeta miinus -hajoamisessa ytimen neutroni muuttuu protoniksi. Ytimestä lähtee elektroni ja antineutriino. Elektroni ei ole ollut ytimessä valmiina, vaan se syntyy hajoamisessa. Beeta plus -hajoamisessa protoni muuttuu neutroniksi. Silloin ytimestä lähtee positroni eli elektronin antihiukkanen ja neutriino. Beetahajoamisen aiheuttaa heikko vuorovaikutus.

```pysahdy
Hiili-14 ${}^{14}_{6}\text{C}$ hajoaa beeta miinus -hajoamisella. Mikä on tyttärytimen massaluku ja järjestysluku? Mikä alkuaine se on?
---
Neutroni muuttuu protoniksi. Siksi $Z = 6 + 1 = 7$. Nukleonien määrä pysyy samana, joten $A = 14$. Tytärydin on typpi-14, ${}^{14}_{7}\text{N}$.
```

Beetahajoamisen kaltainen on **elektronisieppaus**. Ydin sieppaa elektronin atomin sisimmältä elektronikuorelta. Protoni muuttuu neutroniksi, ja ytimestä lähtee elektronineutriino ${}^{0}_{0}\nu_\text{e}$. Yleisesti
```kaavat
elektroninsieppaus :: {}^{A}_{Z}\text{X} + {}^{0}_{-1}\text{e} \to {}^{A}_{Z-1}\text{Y} + {}^{0}_{0}\nu_\text{e}
```
Tässä X on emoydin, Y on tytärydin ja $Z$ on järjestysluku. Esimerkki on ${}^{7}_{4}\text{Be} + {}^{0}_{-1}\text{e} \to {}^{7}_{3}\text{Li} + {}^{0}_{0}\nu_\text{e}$. Ydin muuttuu kuten beeta plus -hajoamisessa ($Z - 1$). Sieppaus on mahdollinen silloinkin, kun positronin syntymiseen ei riitä energiaa.

**Gammahajoamisessa** ydin on viritystilassa eli sillä on ylimääräistä energiaa. Viritystilassa oleva ydin merkitään tähdellä: ${}^{A}_{Z}\text{X}^{\ast}$. Ydin siirtyy alemmalle energiatasolle ja lähettää gammafotonin. Ydin pysyy samana nuklidina. Viritystila syntyy usein edellisessä alfa- tai beetahajoamisessa. Siksi gammasäteily tulee niiden jälkeen.

<svg data-fig="decays" viewBox="0 0 600 360" role="img" aria-label="Kolme hajoamislajia vierekkäin, kaavakuva, ei mittakaavassa. Vasemmalla on alfahajoaminen. Ytimestä lähtee alfahiukkanen eli heliumydin, jossa on kaksi protonia ja kaksi neutronia. Ytimen järjestysluku pienenee kahdella ja massaluku neljällä. Keskellä on beeta miinus -hajoaminen. Ytimen neutroni muuttuu protoniksi, ja ytimestä lähtee elektroni ja antineutriino. Järjestysluku kasvaa yhdellä ja massaluku pysyy samana. Oikealla on gammahajoaminen. Viritystilassa oleva ydin lähettää gammafotonin. Järjestysluku ja massaluku pysyvät samoina." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-8-decays.webp" x="0" y="0" width="600" height="367.5" preserveAspectRatio="none"/>
  <foreignObject x="88" y="18" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#7048e8">$\alpha$</div></foreignObject>
  <foreignObject x="50.5" y="285.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Z - 2,\ A - 4$</div></foreignObject>
  <foreignObject x="280.5" y="18" width="39" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#1971c2">$\beta^-$</div></foreignObject>
  <foreignObject x="236" y="285.5" width="128" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Z + 1,\ A\ \text{sama}$</div></foreignObject>
  <foreignObject x="488" y="18" width="24" height="36" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:30px;color:#e8590c">$\gamma$</div></foreignObject>
  <foreignObject x="444" y="285.5" width="112" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Z, A\ \text{samat}$</div></foreignObject>
  <foreignObject x="131" y="145.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">${}^4_2\text{He}$</div></foreignObject>
  <foreignObject x="355.5" y="51.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$e^-$</div></foreignObject>
  <foreignObject x="349.5" y="215.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\bar{\nu}$</div></foreignObject>
  <foreignObject x="550" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\gamma$</div></foreignObject>
  <foreignObject x="391" y="225.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{viritystila } {}^{\ast}$</div></foreignObject>
</svg>

### Ytimen energiatasot ja gammaspektri
Ytimen energia on kvantittunut, aivan kuten atomin elektronien energia. Se tarkoittaa, että ytimellä on vain tiettyjä energiatasoja. Kun ydin siirtyy ylemmältä energiatasolta alemmalle, lähtevän gammafotonin energia on tasojen erotus. Sama tapahtuu vetyatomin siirtymässä luvussa *Vetyatomin energiatasot ja Bohrin malli*. Siksi ytimen gammaspektri on viivaspektri. Jokainen piikki kertoo yhden tasoparin erotuksen. Mittakaava on kuitenkin eri. Atomin siirtymissä energiat ovat elektronivoltteja. Ytimen tasojen erot ovat tyypillisesti kymmeniä kiloelektronivoltteja tai enemmän. Ne ovat kymmeniätuhansia tai satojatuhansia kertoja suurempia.

Esimerkiksi koboltti-60 hajoaa beeta miinus -hajoamisella nikkeli-60:n viritystilaan. Sen energia on $2505{,}8\,\text{keV}$ perustilan yläpuolella. Ydin palaa perustilaan välitason $1332{,}5\,\text{keV}$ kautta. Gammaspektrissä näkyy kaksi viivaa: $1173{,}2\,\text{keV}$ ja $1332{,}5\,\text{keV}$ (NNDC:n NuDat 3 -tietokanta, ENSDF-arvot). Fotonienergioiden summa jää tasosta noin $0{,}1\,\text{keV}$. Suurin osa erosta on pyöristystä. Rekyyli eli ytimen saama pieni liike-energia fotonin lähtiessä on vain noin $0{,}03\,\text{keV}$. Myös alfahiukkasilla on vain tietyt energiat. Beetahiukkasten energiat sen sijaan jakautuvat jatkuvasti, koska hajoamisenergia jakautuu elektronin ja antineutriinon kesken.

<svg data-fig="levels" viewBox="0 0 600 380" role="img" aria-label="Energiatasokaavio, energiat mittakaavassa: koboltti-60 hajoaa beeta miinus -hajoamisella nikkeli-60:n viritystilaan. Sen energia on 2505,8 keV perustilan yläpuolella. Ydin palaa perustilaan kahdessa vaiheessa. Ensin se siirtyy tasolle 1332,5 keV, ja silloin lähtee gammafotoni 1173,2 keV. Sitten se siirtyy perustilaan, ja silloin lähtee gammafotoni 1332,5 keV. Tiedot ovat NNDC:n NuDat-tietokannasta." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-8-levels.webp" x="3.7" y="1.2" width="594.1" height="386.1" preserveAspectRatio="none"/>
  <foreignObject x="58.5" y="50.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">${}^{60}_{27}\text{Co}$</div></foreignObject>
  <foreignObject x="170" y="77.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\beta^-$</div></foreignObject>
  <foreignObject x="440" y="59" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2505{,}8\,\text{keV}$</div></foreignObject>
  <foreignObject x="440" y="185.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1332{,}5\,\text{keV}$</div></foreignObject>
  <foreignObject x="440" y="329.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="153" y="329.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">${}^{60}_{28}\text{Ni}$</div></foreignObject>
  <foreignObject x="199" y="122" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$1173{,}2$</div></foreignObject>
  <foreignObject x="269" y="257.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$1332{,}5$</div></foreignObject>
</svg>

## Kaava: Hajoamisyhtälöt
Hajoamisyhtälössä säilyvät kaksi lukua. **Massaluku** on nukleonien kokonaismäärä. **Varausluku** on alaindeksien summa. Elektroni merkitään ${}^{0}_{-1}\text{e}$ ja positroni ${}^{0}_{+1}\text{e}$. Niiden massaluku on nolla, ja niiden varaus on $-e$ tai $+e$. Alfahajoaminen on
```kaavat
alfahajoaminen :: {}^{A}_{Z}\text{X} \to {}^{A-4}_{Z-2}\text{Y} + {}^{4}_{2}\text{He}
```
beeta miinus -hajoaminen
```kaavat
$\beta^-$-hajoaminen :: {}^{A}_{Z}\text{X} \to {}^{A}_{Z+1}\text{Y} + {}^{0}_{-1}\text{e} + \bar{\nu}
```
beeta plus -hajoaminen
```kaavat
$\beta^+$-hajoaminen :: {}^{A}_{Z}\text{X} \to {}^{A}_{Z-1}\text{Y} + {}^{0}_{+1}\text{e} + \nu
```
ja gammahajoaminen
```latex
{}^{A}_{Z}\text{X}^{\ast} \to {}^{A}_{Z}\text{X} + \gamma
```
Yhtälöissä X on hajoava emoydin ja Y syntyvä tytärydin. $A$ on massaluku ja $Z$ järjestysluku. $\bar{\nu}$ on antineutriino, $\nu$ neutriino ja $\gamma$ gammafotoni. Tyttärytimen alkuaineen näet jaksollisesta järjestelmästä sen järjestysluvun avulla.

```pysahdy
Uraani-238 ${}^{238}_{92}\text{U}$ hajoaa alfahajoamisella. Mikä on tyttärytimen massaluku ja järjestysluku?
---
Alfahiukkanen ${}^{4}_{2}\text{He}$ vie mukanaan neljä nukleonia ja kaksi protonia. Siksi $A = 238 - 4 = 234$ ja $Z = 92 - 2 = 90$.
```

<svg data-fig="shifts" viewBox="0 0 600 360" role="img" aria-label="Nuklidikartan ote, ruudukko: vaaka-akselilla on neutroniluku N ja pystyakselilla järjestysluku Z. Yksi ruutu on yksi yksikkö. Keskellä on emoydin. Alfahajoaminen siirtää ytimen kaksi ruutua alas ja kaksi vasemmalle (Z − 2, N − 2). Beeta miinus -hajoaminen siirtää sen yhden ruudun ylös ja yhden vasemmalle (Z + 1, N − 1). Beeta plus -hajoaminen siirtää sen yhden ruudun alas ja yhden oikealle (Z − 1, N + 1). Gammahajoamisessa ydin pysyy samassa ruudussa." style="max-width:100%;font-size:24px">
  <line x1="140" y1="40" x2="140" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="40" x2="416" y2="40" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186" y1="40" x2="186" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="86" x2="416" y2="86" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="232" y1="40" x2="232" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="132" x2="416" y2="132" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="278" y1="40" x2="278" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="178" x2="416" y2="178" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="324" y1="40" x2="324" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="224" x2="416" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="370" y1="40" x2="370" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="270" x2="416" y2="270" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="416" y1="40" x2="416" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="140" y1="316" x2="416" y2="316" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="281" y="135" width="40" height="40" rx="5" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="189" y="227" width="40" height="40" rx="5" fill="#ffffff" stroke="#7048e8" stroke-width="2"/>
  <rect x="235" y="89" width="40" height="40" rx="5" fill="#d0e6fb" stroke="#1971c2" stroke-width="2"/>
  <rect x="327" y="181" width="40" height="40" rx="5" fill="#f2a69c" stroke="#c92a2a" stroke-width="2"/>
  <line x1="288.5" y1="167.5" x2="228" y2="228" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M220.5,235.5 L225,223.5 L232.5,231 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="175" y="262.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$\alpha$</div></foreignObject>
  <line x1="288.5" y1="142.5" x2="274" y2="128" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M266.5,120.5 L278.5,125 L271,132.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="214" y="64.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\beta^-$</div></foreignObject>
  <line x1="313.5" y1="167.5" x2="328" y2="182" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <path d="M335.5,189.5 L323.5,185 L331,177.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="361" y="216.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\beta^+$</div></foreignObject>
  <path d="M311,138 A 14 14 0 1 1 318,149" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="331" y="110.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\gamma$</div></foreignObject>
  <line x1="140" y1="334" x2="434" y2="334" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M446,334 L433,340 L433,328 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="452" y="319.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N$</div></foreignObject>
  <line x1="122" y1="316" x2="122" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M122,34 L128,47 L116,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="92" y="29.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$Z$</div></foreignObject>
</svg>

Gammafotonin energia on ytimen tasojen erotus. Fotonin aallonpituuden saat fotonin energiasta:
```latex
\begin{aligned}
E_\gamma &= E_\text{y} - E_\text{a} \\
\lambda &= \frac{hc}{E_\gamma}
\end{aligned}
```
Kaavoissa $E_\text{y}$ ja $E_\text{a}$ ovat ylemmän ja alemman tason energiat. $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ on Planckin vakio ja $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$ on valon nopeus. Muunna kiloelektronivoltit jouleiksi sijoittamalla $1\,\text{keV} = 1000\,\text{eV}$ ja $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$.

## Esimerkki
Cesium-137 ${}^{137}_{55}\text{Cs}$ hajoaa beeta miinus -hajoamisella. Tytärydin syntyy useimmiten viritystilaan. Viritystila purkautuu niin, että ydin lähettää gammafotonin, jonka energia on $661{,}7\,\text{keV}$ (NNDC NuDat 3). Mikä tytärydin on, ja kuinka suuri on gammafotonin aallonpituus?

<!-- vaihe -->

**Tunnetut ja kysytty.** Emoydin on ${}^{137}_{55}\text{Cs}$, ja hajoaminen on beeta miinus -hajoaminen. Gammafotonin energia on $E_\gamma = 661{,}7\,\text{keV}$, $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ ja $c = 2{,}998 \cdot 10^{8}\,\text{m/s}$.

Kysytään tyttärytimen järjestyslukua $Z'$ ja massalukua $A'$ sekä fotonin aallonpituutta $\lambda$.

<!-- vaihe -->

**Periaate.** Beeta miinus -hajoamisessa neutroni muuttuu protoniksi. Massaluku ja varausluku säilyvät, kun elektroni ${}^{0}_{-1}\text{e}$ lasketaan mukaan. Gammafotonin energia on viritystilan ja perustilan erotus. Fotonin energia on $\tfrac{hc}{\lambda}$.

<!-- vaihe -->

**Kaava ratkaistuna.** Säilymislaeista ja fotonin energiasta saadaan:
```latex
\begin{aligned}
&A = A' + 0, \quad Z = Z' - 1 \\
&A' = A, \quad Z' = Z + 1 \\
&\lambda = \frac{hc}{E_\gamma}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Muunna energia jouleiksi sijoittamalla $1\,\text{keV} = 1000\,\text{eV}$ ja $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$: $E_\gamma = 661{,}7 \cdot 1000 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 1{,}0600 \cdot 10^{-13}\,\text{J}$.

<!-- vaihe -->

**Sijoitus.** Tytärytimen luvut ja aallonpituus:
```latex
\begin{aligned}
&A' = 137, \quad Z' = 55 + 1 = 56 \\[6pt]
&hc = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \\
&\quad \cdot 2{,}998 \cdot 10^{8}\,\text{m/s} \\
&= 1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m} \\[6pt]
&\lambda = \frac{1{,}9865 \cdot 10^{-25}\,\text{J}\,\text{m}}{1{,}0600 \cdot 10^{-13}\,\text{J}} \\
&= 1{,}8740 \cdot 10^{-12}\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Järjestysluku $56$ on barium, joten tytärydin on ${}^{137}_{56}\text{Ba}$: ${}^{137}_{55}\text{Cs} \to {}^{137}_{56}\text{Ba} + {}^{0}_{-1}\text{e} + \bar{\nu}$. Aallonpituus on $\lambda \approx 1{,}874 \cdot 10^{-12}\,\text{m} = 1{,}874\,\text{pm}$. Vastauksessa on neljä merkitsevää numeroa, kuten energiassa $661{,}7\,\text{keV}$.

<!-- vaihe -->

**Järkevyys.** Yhtälön molemmilla puolilla massaluku on $137$ ja varausluku on $55 = 56 - 1$. Näkyvän valon aallonpituus $500\,\text{nm}$ on noin $270\,000$ kertaa pidempi. Siksi gammafotonin energia on satojatuhansia kertoja suurempi kuin näkyvän valon fotonin. Tämä on ytimen tasojen mittakaava.

## Yleinen virhekäsitys
Moni ajattelee, että beetahiukkanen on ytimessä valmiina oleva elektroni. Ytimessä ei ole elektroneja. Elektroni ja antineutriino syntyvät, kun neutroni muuttuu protoniksi. Siksi järjestysluku kasvaa yhdellä, vaikka ytimestä lähtee negatiivinen hiukkanen.

Toinen virhe on ajatella, että gammahajoaminen muuttaa alkuaineen. Gammafotoni vie vain energiaa. Protonien ja neutronien määrät pysyvät samoina, ja ydin siirtyy vain alemmalle energiatasolle. Alkuaine vaihtuu vain, kun protonien määrä muuttuu. Niin käy alfa- ja beetahajoamisessa sekä elektronisieppauksessa.

## Tiivistelmä
- Ydin koostuu nukleoneista: $Z$ protonia ja $N = A - Z$ neutronia. Saman alkuaineen isotoopeilla on sama $Z$ mutta eri $N$.
- Radioaktiivinen ydin hajoaa itsestään ja satunnaisesti. Alfahajoamisessa lähtee ${}^{4}_{2}\text{He}$ ($Z - 2$, $A - 4$). Beeta miinus -hajoamisessa lähtevät elektroni ja antineutriino ($Z + 1$). Beeta plus -hajoamisessa lähtevät positroni ja neutriino ($Z - 1$).
- Elektronisieppauksessa ydin sieppaa elektronin ja lähettää neutriinon ($Z - 1$).
- Hajoamisyhtälössä massaluku ja varausluku säilyvät.
- Ytimen energia on kvantittunut. Gammafotonin energia on ytimen tasojen erotus $E_\gamma = E_\text{y} - E_\text{a}$. Se on tyypillisesti kymmeniä tai satoja kiloelektronivoltteja tai megaelektronivoltteja, joten gammaspektri on viivaspektri.
