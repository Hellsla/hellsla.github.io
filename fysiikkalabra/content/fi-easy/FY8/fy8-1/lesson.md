# Valosähköinen ilmiö ja fotoni

> **Miksi** heikkokin lyhytaaltoinen ultraviolettivalo irrottaa elektroneja sinkkilevystä, mutta kirkaskaan punainen valo ei irrota yhtäkään?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion pöydällä on kaksi lasikupuista elektroskooppia. Niiden päällä on kiiltävä sinkkilevy. Vasemman elektroskoopin yllä pieni ultraviolettilamppu loistaa violettina. Levystä lentää pieniä sinisiä elektroneja, ja elektroskoopin lehdet riippuvat alhaalla. Oikean elektroskoopin yllä suuri punainen lamppu loistaa kirkkaasti. Elektroneja ei kuitenkaan irtoa, ja elektroskoopin lehdet ovat yhä erillään." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-1-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Valo irrottaa elektroneja metallista
Sinkkilevy on varattu negatiiviseksi. Kun levyä valaistaan riittävän lyhytaaltoisella ultraviolettisäteilyllä, levy menettää varauksensa nopeasti. Säteily irrottaa levyn pinnasta elektroneja. Ilmiötä sanotaan **valosähköiseksi ilmiöksi**. Metallissa on paljon elektroneja, jotka liikkuvat vapaasti metallin sisällä. Ne eivät kuitenkaan pääse itsestään ulos metallin pinnan läpi. Pienintä energiaa, jolla elektroni saadaan irti metallista, sanotaan **irrotustyöksi** $W$. Irrotustyö riippuu metallista. Natriumilla se on noin $2{,}3\,\text{eV}$ ja sinkillä noin $4{,}3\,\text{eV}$. Yksikkö elektronivoltti selitetään tämän luvun lopussa.

<svg data-fig="ilmio" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva, ei mittakaavassa: vaakasuora sinkkilevy on kuvan alareunassa. Vasemmalla levyyn osuu neljä punaisen valon fotonia. Aallonpituus on 650 nanometriä. Fotonit ovat aaltoviivanuolia, joissa on merkintä hf. Levystä ei irtoa yhtään elektronia. Oikealla levyyn osuu vain kaksi ultraviolettivalon fotonia. Aallonpituus on 254 nanometriä. Kummankin osumakohdasta lähtee sininen elektroni e miinus. Elektronilla on nopeusnuoli v, jonka päällä on viiva. Nuoli osoittaa ylös ja oikealle. Pystysuora katkoviiva erottaa tilanteet." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-1-ilmio.webp" x="2.5" y="1.2" width="594.1" height="346.5" preserveAspectRatio="none"/>
  <foreignObject x="233.5" y="303.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sinkkilevy}$</div></foreignObject>
  <foreignObject x="40" y="13.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{punainen valo}$</div></foreignObject>
  <foreignObject x="40" y="45.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\lambda = 650\,\text{nm}$</div></foreignObject>
  <foreignObject x="35" y="153.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#db0000">$hf$</div></foreignObject>
  <foreignObject x="334" y="13.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ultraviolettivalo}$</div></foreignObject>
  <foreignObject x="334" y="45.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\lambda = 254\,\text{nm}$</div></foreignObject>
  <foreignObject x="317" y="153.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$hf$</div></foreignObject>
  <foreignObject x="512" y="231.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$e^-$</div></foreignObject>
  <foreignObject x="546" y="155.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
</svg>

### Aaltomalli ei selitä havaintoja
Valo on sähkömagneettista aaltoliikettä. Aallon intensiteetti kertoo, kuinka paljon energiaa aalto tuo pinnalle sekunnissa. Aaltomallin mukaan kirkkaamman valon pitäisi siis irrottaa elektroneja helpommin. Sen pitäisi myös antaa elektroneille enemmän liike-energiaa, väristä riippumatta. Himmeällä valolla elektronin pitäisi kerätä energiaa jonkin aikaa ennen irtoamista. Kokeissa 1900-luvun alussa mitattiin tarkasti, kuinka monta elektronia irtoaa ja kuinka suuri niiden liike-energia on. Tulos oli aivan toisenlainen:

- **Kynnys.** Aaltomallin mukaan mikä tahansa valo irrottaisi elektroneja, kun se on tarpeeksi kirkasta. Kokeissa elektroneja ei irtoa lainkaan, jos valon taajuus on liian pieni. Valo voi olla kuinka kirkasta tahansa.
- **Viive.** Aaltomallin mukaan himmeällä valolla irtoaminen alkaisi viiveellä. Kokeissa elektroneja irtoaa heti, kun valo osuu levyyn. Näin käy himmeälläkin valolla.
- **Intensiteetti.** Aaltomallin mukaan kirkkaampi valo antaisi elektroneille enemmän liike-energiaa. Kokeissa kirkkaampi valo irrottaa enemmän elektroneja, mutta niiden suurin liike-energia pysyy samana.
- **Taajuus.** Kokeissa elektronien suurin liike-energia kasvaa, kun valon taajuus kasvaa. Aaltomallissa taajuudella ei ole tällaista merkitystä.

### Fotoni: valon energiakvantti
Albert Einstein selitti havainnot vuonna 1905. Valon energia ei jakaudu tasaisesti aaltoon. Se on pakkautunut erillisiksi annoksiksi eli **kvanteiksi**. Valon kvanttia sanotaan **fotoniksi**. Yhden fotonin energia on $E = hf$. Tässä $f$ on valon taajuus ja $h$ on **Planckin vakio**. Fotoni luovuttaa koko energiansa yhdelle elektronille kerralla. Tavallisessa valossa elektroni ei ehdi kerätä energiaa usealta fotonilta. Jos $hf < W$, elektroni ei irtoa, vaikka fotoneja tulisi kuinka paljon tahansa. Jos $hf > W$, elektroni irtoaa. Ylimääräinen energia jää elektronille liike-energiaksi.

<svg data-fig="energia" viewBox="0 0 600 304" role="img" aria-label="Energiakaavio mittakaavassa natriumille. Alempi vaakaviiva on energia, joka metallin heikoimmin sidotulla elektronilla on. Ylempi viiva on 2,28 elektronivolttia korkeammalla. Se on energia, jolla elektroni juuri pääsee irti. Ero on irrotustyö W. Kolme pystysuoraa fotoninuolta alkaa alemmalta viivalta. Nuolen pituus on fotonin energia hf. Punaisen valon fotoni, 650 nanometriä ja 1,91 elektronivolttia, jää ylemmän viivan alle. Silloin hf on pienempi kuin W, eikä elektroni irtoa. Vihreän valon fotoni, 544 nanometriä, ulottuu juuri ylemmälle viivalle. Silloin hf on yhtä suuri kuin W. Violetin valon fotoni, 405 nanometriä ja 3,06 elektronivolttia, ulottuu viivan yli. Ylimenevä osa, 0,78 elektronivolttia, on elektronin suurin liike-energia E k max. Se on merkitty sinisellä hakasella." style="max-width:100%;font-size:24px">
  <image href="pics/fy8/fy8-1-energia.webp" x="0" y="2.5" width="600" height="316.2" preserveAspectRatio="none"/>
  <foreignObject x="92" y="70.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{irti}$</div></foreignObject>
  <foreignObject x="11" y="207.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{metallissa}$</div></foreignObject>
  <foreignObject x="532" y="139" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$W$</div></foreignObject>
  <foreignObject x="214" y="150.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#db0000">$hf$</div></foreignObject>
  <foreignObject x="158.5" y="233.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$650\,\text{nm}$</div></foreignObject>
  <foreignObject x="171" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$hf < W$</div></foreignObject>
  <foreignObject x="334" y="139" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7ac600">$hf$</div></foreignObject>
  <foreignObject x="278.5" y="233.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$544\,\text{nm}$</div></foreignObject>
  <foreignObject x="291" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$hf = W$</div></foreignObject>
  <foreignObject x="454" y="95.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6f00ac">$hf$</div></foreignObject>
  <foreignObject x="398.5" y="233.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$405\,\text{nm}$</div></foreignObject>
  <foreignObject x="411" y="263.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$hf > W$</div></foreignObject>
  <foreignObject x="153" y="191.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$e^-$</div></foreignObject>
  <foreignObject x="478" y="41" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$E_\text{k,max}$</div></foreignObject>
</svg>

```pysahdy
Ajattele aaltomallia. Elektroni voi kerätä energiaa vain pinta-alalta $1{,}0 \cdot 10^{-19}\,\text{m}^2$. Se on suunnilleen yhden atomin ala. Himmeän valon intensiteetti on $1{,}0 \cdot 10^{-3}\,\text{W/m}^2$. Sinkin irrotustyö on $4{,}3\,\text{eV}$. Kauanko energian keräämiseen menisi? Entä mitä kokeessa nähdään?
---
Elektronin saama teho on $P = 1{,}0 \cdot 10^{-3}\,\text{W/m}^2 \cdot 1{,}0 \cdot 10^{-19}\,\text{m}^2 = 1{,}0 \cdot 10^{-22}\,\text{W}$. Irrotustyö on $W = 4{,}3 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 6{,}9 \cdot 10^{-19}\,\text{J}$. Aika on $t = W/P = 6{,}9 \cdot 10^{3}\,\text{s}$, eli noin $1{,}9\,\text{h}$. Kokeessa elektroneja irtoaa silti heti, joten aaltomalli ei kelpaa.
```

Tällä mallilla jokainen havainto selittyy. Samanvärisellä valolla intensiteetti kertoo, kuinka monta fotonia osuu pintaan sekunnissa. Kirkkaampi valo irrottaa siksi enemmän elektroneja. Yksittäinen elektroni saa silti vain yhden fotonin energian. Taajuus määrää yhden fotonin energian ja siksi elektronin suurimman liike-energian. Viivettä ei ole, koska jo ensimmäinen riittävän energinen fotoni voi irrottaa elektronin. Tässä mallissa energia on **kvantittunut**. Se tarkoittaa, että säteily ja aine vaihtavat energiaa vain kokonaisina fotonin energioina.

```pysahdy
Punaisen valon yhden fotonin energia on pienempi kuin metallin irrotustyö $W$, eikä elektroneja irtoa. Mitä nähdään, jos valon taajuutta kasvatetaan niin, että fotonin energia on vain vähän suurempi kuin $W$? Valo pysyy himmeänä.
---
Elektroneja alkaa irrota heti, koska yksi fotoni riittää. Liike-energia $hf - W$ on melkein nolla. Elektroneja irtoaa vähän, koska himmeä valo tuo vähän fotoneja sekunnissa.
```

<figure class="unit-photo"><img src="pics/fy8/photomultiplier-tube.webp" alt="Suuri pyöreä lasikupu museon vitriinissä. Kuvun sisäpinta on kuin peili."><figcaption>Valomonistinputki museossa Tokiossa. Fotoni osuu kuvun sisäpintaan ja irrottaa elektronin. Tämä on valosähköinen ilmiö. Putki vahvistaa elektronin mitattavaksi sähköpulssiksi.</figcaption></figure>

### Elektronivoltti
Fotonin ja elektronin energiat ovat jouleina hyvin pieniä lukuja. Siksi niille käytetään usein yksikköä **elektronivoltti** ($\text{eV}$). Yksi elektronivoltti on se energia, jonka elektroni saa, kun se kiihtyy sähkökentässä $1\,\text{V}$:n jännitteen läpi. Elektronin varauksen suuruus on $e = 1{,}602 \cdot 10^{-19}\,\text{C}$. Siksi $$
\begin{aligned}
&1\,\text{eV} \\
&= 1{,}602 \cdot 10^{-19}\,\text{C} \cdot 1\,\text{V} \\
&= 1{,}602 \cdot 10^{-19}\,\text{J}
\end{aligned}
$$. Muunnos tehdään sijoittamalla. Esimerkiksi $$
\begin{aligned}
&3{,}20 \cdot 10^{-19}\,\text{J} \\
&= \tfrac{3{,}20 \cdot 10^{-19}}{1{,}602 \cdot 10^{-19}}\,\text{eV} \\
&\approx 2{,}00\,\text{eV}
\end{aligned}
$$.

## Kaava: Fotonin energia

### Taajuus ja aallonpituus
Säteilyn taajuus on $f$. Tämän säteilyn fotonin energia on
```kaavat
fotonin energia :: E = hf
```
Tässä $E$ on fotonin energia ($\text{J}$), $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ on Planckin vakio ja $f$ on säteilyn taajuus ($\text{Hz}$). Sähkömagneettinen säteily etenee tyhjiössä valon nopeudella $c = 2{,}998 \cdot 10^8\,\text{m/s}$. Aaltoliikkeen perusyhtälö on $c = f\lambda$. Sijoitetaan siihen $f = \tfrac{c}{\lambda}$, ja saadaan
```kaavat
fotonin energia :: E = \frac{hc}{\lambda}
```
Tässä $\lambda$ on säteilyn aallonpituus tyhjiössä ($\text{m}$). Mitä lyhyempi aallonpituus on, sitä suurempi on fotonin energia. Esimerkki: vihreän valon aallonpituus on $\lambda = 500\,\text{nm}$. Sen fotonin energia on $$
\begin{aligned}
&E \\
&= \tfrac{6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2{,}998 \cdot 10^8\,\text{m/s}}{500 \cdot 10^{-9}\,\text{m}} \\
&= 3{,}97 \cdot 10^{-19}\,\text{J}
\end{aligned}
$$ eli $2{,}48\,\text{eV}$. Arvioita varten kannattaa muuntaa tulo $hc$ kerran elektronivolteiksi ja nanometreiksi. Muunnoksessa käytetään yhtälöitä $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$ ja $1\,\text{m} = 10^{9}\,\text{nm}$. Tulo on

```latex
\begin{aligned}
hc &= 1{,}986 \cdot 10^{-25}\,\text{J}\,\text{m} \\
&= \tfrac{1{,}986 \cdot 10^{-25}}{1{,}602 \cdot 10^{-19}}\,\text{eV}\,\text{m} \\
&\approx 1{,}240 \cdot 10^{-6}\,\text{eV}\,\text{m} \\
&= 1240\,\text{eV}\,\text{nm}
\end{aligned}
```
Sen avulla saa nopean arvion. Fotonin, jonka aallonpituus on $500\,\text{nm}$, energia on noin $1240\,\text{eV}\,\text{nm} : 500\,\text{nm} \approx 2{,}5\,\text{eV}$.

### Valosähköinen yhtälö
Kun fotoni irrottaa elektronin, osa fotonin energiasta kuluu irrotustyöhön. Loppu jää elektronin liike-energiaksi. Energian säilymisestä saadaan Einsteinin valosähköinen yhtälö
```latex
hf = W + E_\text{k,max}
```
Tässä $hf$ on fotonin energia, $W$ on metallin irrotustyö ja $E_\text{k,max}$ on irtoavan elektronin suurin mahdollinen liike-energia. Liike-energia on *suurin*, koska syvemmältä metallista irtoava elektroni menettää osan energiastaan jo matkalla pintaan. Sen liike-energia jää pienemmäksi. Elektroneja irtoaa vain, jos $hf \geq W$. Pienin irrottava taajuus on **rajataajuus** $f_0 = \tfrac{W}{h}$. Sitä vastaa pisin irrottava aallonpituus $\lambda_0 = \tfrac{hc}{W}$. Natriumilla $\lambda_0 \approx 544\,\text{nm}$. Se on vihreän valon keskivaiheilla. Punainen, keltainen ja kellertävän vihreä valo eivät siis irrota natriumista elektroneja. Sinivihreä, sininen ja violetti valo irrottavat.

<svg data-fig="kuvaaja" viewBox="0 0 600 400" role="img" aria-label="Kuvaaja mittakaavassa. Se näyttää irtoavien elektronien suurimman liike-energian elektronivoltteina, kun valon taajuus muuttuu. Taajuusakseli alkaa nollasta ja päättyy 16 kertaa 10 potenssiin 14 hertsiin. Natriumin suora alkaa vaaka-akselilta rajataajuudelta 5,5 kertaa 10 potenssiin 14 hertsiä. Se nousee arvoon 4,3 elektronivolttia. Sinkin suora alkaa rajataajuudelta 10,4 kertaa 10 potenssiin 14 hertsiä. Se on natriumin suoran suuntainen. Rajataajuuden alapuolella elektroneja ei irtoa. Natriumin suoralle on piirretty katkoviivoin kolmio, joka näyttää kulmakertoimen. Merkintä kertoo, että kulmakerroin on Planckin vakio h." style="max-width:100%;font-size:24px">
  <line x1="136.5" y1="340" x2="136.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="177" y1="340" x2="177" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="217.5" y1="340" x2="217.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="258" y1="340" x2="258" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="298.5" y1="340" x2="298.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="339" y1="340" x2="339" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="379.5" y1="340" x2="379.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="340" x2="420" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="283" x2="420" y2="283" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="226.5" x2="420" y2="226.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="169.5" x2="420" y2="169.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="113" x2="420" y2="113" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="56" x2="420" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="340" x2="434" y2="340" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M446,340 L433,346 L433,334 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="341" x2="96" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,30 L102,43 L90,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="136.5" y1="340" x2="136.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="126.5" y="349.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="177" y1="340" x2="177" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="167" y="349.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="217.5" y1="340" x2="217.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="207.5" y="349.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="258" y1="340" x2="258" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="248" y="349.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="298.5" y1="340" x2="298.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="282" y="349.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="339" y1="340" x2="339" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="322.5" y="349.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="379.5" y1="340" x2="379.5" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="363" y="349.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$14$</div></foreignObject>
  <line x1="420" y1="340" x2="420" y2="347" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="403.5" y="349.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$16$</div></foreignObject>
  <line x1="89" y1="283" x2="96" y2="283" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="268.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="226.5" x2="96" y2="226.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="212" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="169.5" x2="96" y2="169.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="155" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="113" x2="96" y2="113" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="98.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="89" y1="56" x2="96" y2="56" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="41.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <foreignObject x="66" y="345.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="452" y="325.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$f\ (10^{14}\,\text{Hz})$</div></foreignObject>
  <foreignObject x="86" y="-0.5" width="137" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{k,max}\ (\text{eV})$</div></foreignObject>
  <polyline points="207.5,340 420,93.5" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="207.5" cy="340" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="430" y="79" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\text{natrium}$</div></foreignObject>
  <foreignObject x="166.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$f_0$</div></foreignObject>
  <polyline points="307,340 420,209" fill="none" stroke="#6c757d" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="307" cy="340" r="6.5" fill="#6c757d" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="430" y="194.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6c757d">$\text{sinkki}$</div></foreignObject>
  <foreignObject x="266" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6c757d">$f_0$</div></foreignObject>
  <line x1="278" y1="258" x2="359" y2="258" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="359" y1="258" x2="359" y2="164" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="120.5" y="115.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{kulmakerroin} = h$</span></div></foreignObject>
</svg>

Yhtälö voidaan kirjoittaa muotoon $E_\text{k,max} = hf - W$. Tämä on suoran yhtälö. Suurin liike-energia kasvaa tasaisesti taajuuden mukana. Suoran kulmakerroin on Planckin vakio $h$ kaikille metalleille. Eri metallien suorat ovat siksi yhdensuuntaiset. Ne alkavat vaaka-akselilta kunkin metallin rajataajuudelta. Robert Millikan mittasi tällaisia suoria vuonna 1916. Hän sai suorien kulmakertoimesta Planckin vakion. Valon intensiteetti ei esiinny yhtälössä lainkaan.

```pysahdy
Natriumin irrotustyö on $2{,}3\,\text{eV}$. Fotonin energia kasvaa $3{,}0\,\text{eV}$:sta $6{,}0\,\text{eV}$:iin. Kaksinkertaistuuko elektronien suurin liike-energia?
---
Ei. Yhtälöstä $E_\text{k,max} = hf - W$ saadaan ensin $3{,}0\,\text{eV} - 2{,}3\,\text{eV} = 0{,}7\,\text{eV}$ ja sitten $6{,}0\,\text{eV} - 2{,}3\,\text{eV} = 3{,}7\,\text{eV}$. Irrotustyö vähennetään aina, joten liike-energia kasvaa yli viisinkertaiseksi.
```

### Sinkki tarvitsee lyhytaaltoista ultraviolettia
Rajataajuutta vastaa **raja-aallonpituus** $\lambda_0 = hc : W$. Sitä pidempiaaltoinen säteily ei irrota elektroneja. Sinkistä irtoaa elektroneja vain, jos fotonin energia on suurempi kuin sinkin irrotustyö. Irrotustyö on $4{,}31\,\text{eV}$, joten raja-aallonpituus on $$
\begin{aligned}
\lambda_0 &\approx 1240\,\text{eV}\,\text{nm} : 4{,}31\,\text{eV} \\
&\approx 288\,\text{nm}
\end{aligned}
$$. Tavallinen $365\,\text{nm}$:n UV-A-lamppu ei siksi riitä. Lyhytaaltoisempi säteily, esimerkiksi $254\,\text{nm}$:n UV-C, voi irrottaa elektroneja. Koe onnistuu parhaiten, kun sinkkipinta on juuri hiottu. Pinnan oksidikerros ja lika heikentävät ilmiötä.

UV-C-säteily vaurioittaa silmiä ja ihoa jo lyhyessä ajassa. Koulussa koetta ei tehdä suojaamattomalla UV-C-lampulla. Opettaja voi näyttää kokeen suojatulla laitteistolla. Muuten ilmiötä tutkitaan simulaatiolla ja valmiilla mittausaineistolla.

## Esimerkki
Violetti laserosoitin lähettää valoa, jonka aallonpituus on $405\,\text{nm}$. Valo osuu natriumpintaan, jonka irrotustyö on $2{,}28\,\text{eV}$. Kuinka suuri on irtoavien elektronien suurin liike-energia elektronivoltteina?

<!-- vaihe -->

**Tunnetut ja kysytty.** Aallonpituus on $\lambda = 405\,\text{nm}$ ja irrotustyö on $W = 2{,}28\,\text{eV}$. Lisäksi tunnetaan Planckin vakio $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$, valon nopeus $c = 2{,}998 \cdot 10^8\,\text{m/s}$ ja yhtälö $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$.

Kysytään suurinta liike-energiaa $E_\text{k,max}$.

<!-- vaihe -->

**Periaate.** Yksi fotoni luovuttaa koko energiansa yhdelle elektronille. Energia säilyy. Fotonin energiasta kuluu irrotustyö $W$ elektronin irrottamiseen, ja loppu jää liike-energiaksi. Valosähköinen yhtälö pätee, jos fotonin energia riittää irrotukseen. Tämä tarkistetaan tuloksesta.

<!-- vaihe -->

**Kaava ratkaistuna.** Valosähköisestä yhtälöstä ratkaistaan $E_\text{k,max}$. Fotonin energia kirjoitetaan aallonpituuden avulla:
```latex
E_\text{k,max} = \frac{hc}{\lambda} - W
```

<!-- vaihe -->

**Yksikkömuunnokset.** Aallonpituus muunnetaan metreiksi: $\lambda = 405\,\text{nm} = 405 \cdot 10^{-9}\,\text{m}$. Irrotustyö muunnetaan jouleiksi sijoittamalla $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$: $W = 2{,}28\,\text{eV} = 2{,}28 \cdot 1{,}602 \cdot 10^{-19}\,\text{J} = 3{,}653 \cdot 10^{-19}\,\text{J}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&E_\text{k,max} = \frac{hc}{\lambda} - W \\
&= \frac{6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s} \cdot 2{,}998 \cdot 10^8\,\tfrac{\text{m}}{\text{s}}}{405 \cdot 10^{-9}\,\text{m}} \\
&\quad - 3{,}653 \cdot 10^{-19}\,\text{J} \\
&= 4{,}905 \cdot 10^{-19}\,\text{J} - 3{,}653 \cdot 10^{-19}\,\text{J} \\
&= 1{,}252 \cdot 10^{-19}\,\text{J} \\
&= \frac{1{,}252 \cdot 10^{-19}}{1{,}602 \cdot 10^{-19}}\,\text{eV} \\
&= 0{,}782\,\text{eV}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Irtoavien elektronien suurin liike-energia on $0{,}78\,\text{eV}$. Tulos ilmoitetaan kahdella desimaalilla. Syy on tämä: tulos on kahden lähes yhtä suuren energian erotus, ja irrotustyö $2{,}28\,\text{eV}$ on annettu sadasosan tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Fotonin energia on $3{,}06\,\text{eV}$. Se on suurempi kuin irrotustyö $2{,}28\,\text{eV}$, joten elektroneja todella irtoaa. Liike-energia on positiivinen ja pienempi kuin fotonin energia, kuten pitääkin. Arvio pyöreillä luvuilla: $E \approx 1240\,\text{eV}\,\text{nm} : 405\,\text{nm} \approx 3{,}1\,\text{eV}$ ja $3{,}1\,\text{eV} - 2{,}3\,\text{eV} = 0{,}8\,\text{eV}$.

## Yleinen virhekäsitys
Moni ajattelee, että kirkkaampi valo antaa elektroneille enemmän energiaa, koska kirkas valo tuo pinnalle enemmän energiaa. Kirkkaampi valo tuo kuitenkin enemmän *fotoneja*. Fotonit eivät ole yksittäin energisempiä. Yksi elektroni saa aina yhden fotonin energian. Siksi kirkkaampi valo kasvattaa irtoavien elektronien määrää, mutta ei niiden suurinta liike-energiaa. Tämän takia kirkaskaan punainen valo ei irrota sinkistä elektroneja. Jokaisen punaisen fotonin energia jää pienemmäksi kuin irrotustyö.

Toinen virhe on ajatella, että fotoni on pieni valon ”pallo”, jolla on tietty paikka ja koko. Sen mukaan valo olisi joko aalto tai hiukkasjoukko. Valosähköisessä ilmiössä valon energian siirtyminen näkyy kvantteina. Valon interferenssi eli aaltojen yhteisvaikutus selittyy kuitenkin aaltomallilla. Valon kaksoisluonteeseen palataan luvussa *Valo ja elektroni aaltoina ja hiukkasina*.

## Tiivistelmä
- Valosähköisessä ilmiössä valo irrottaa elektroneja metallin pinnasta. Pienin energia, joka irrottamiseen tarvitaan, on metallin irrotustyö $W$. Sinkki tarvitsee ultraviolettisäteilyä, jonka aallonpituus on alle noin $288\,\text{nm}$.
- Valon energia on kvantittunut fotoneiksi. Fotonin energia on $E = hf = \tfrac{hc}{\lambda}$, ja tässä $h = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$.
- Yksi fotoni luovuttaa energiansa yhdelle elektronille: $hf = W + E_\text{k,max}$. Elektroneja irtoaa vain, kun $hf \geq W$ eli $f \geq f_0 = \tfrac{W}{h}$.
- Valon intensiteetti määrää irtoavien elektronien määrän. Taajuus määrää niiden suurimman liike-energian.
- $1\,\text{eV} = 1{,}602 \cdot 10^{-19}\,\text{J}$.
