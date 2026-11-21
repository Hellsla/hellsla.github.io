# Normaalikiihtyvyys ja ympyräliikkeen liikeyhtälö

> **Miksi** auto suistuu liukkaassa kaarteessa ulos tieltä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Talvinen maantie kaartaa metsän läpi oikealle. Kaarteessa ajaa auto takaapäin nähtynä. Tien reunoilla on lumipenkat ja kuusia." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-4-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Nopeuden suunta muuttuu, joten kappale kiihtyy
Luvussa *Ympyrärata: jaksonaika ja ratanopeus* opit, että tasaisessa ympyräliikkeessä kappale kiertää ympyrärataa vakiovauhdilla. Nopeuden suuruus eli ratanopeus $v$ pysyy samana. Nopeuden suunta kuitenkin muuttuu koko ajan, sillä nopeus $\overline{v}$ osoittaa aina radan tangentin suuntaan. Tangentti on suora, joka koskettaa rataa yhdessä pisteessä. Nopeus on vektori, eli sillä on suuruus ja suunta. Siksi myös suunnan muutos on nopeuden muutos. Kun nopeus muuttuu, kappale kiihtyy. Tasaisessa ympyräliikkeessä kappale siis kiihtyy, vaikka sen vauhti ei muutu.

<svg data-fig="muutos" viewBox="0 0 600 340" role="img" aria-label="Kaksi kuvaa. Vasemmalla kappale kiertää ympyrärataa tasaisella vauhdilla. Siniset nopeusnuolet v 1 ja v 2 ovat yhtä pitkät mutta osoittavat eri suuntiin. Oikealla samat nuolet on piirretty samasta pisteestä: niiden kärkien välinen nuoli, nopeuden muutos, osoittaa kohti radan keskipistettä." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-4-muutos.webp" x="0" y="0" width="600" height="340" preserveAspectRatio="none"/>
  <foreignObject x="65" y="7.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kappaleen rata}$</div></foreignObject>
  <foreignObject x="93.5" y="209.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{keskipiste}$</div></foreignObject>
  <foreignObject x="209" y="51" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <foreignObject x="1" y="227" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <foreignObject x="174" y="136.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
  <foreignObject x="368.5" y="7.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{nopeuden muutos}$</div></foreignObject>
  <foreignObject x="516.5" y="71" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}_1$</div></foreignObject>
  <foreignObject x="516.5" y="204" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}_2$</div></foreignObject>
  <foreignObject x="446" y="135.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\Delta\overline{v}$</div></foreignObject>
</svg>

Kuvassa kappaleen nopeus on ensin $\overline{v}_1$ ja hetken kuluttua $\overline{v}_2$. Kun nuolet piirretään samasta pisteestä, niiden kärkien välinen nuoli on nopeuden muutos $\Delta\overline{v}$. Se osoittaa radan sisäpuolelle. Sen suunta on sama kuin nuolella, joka piirretään aikavälin puolivälistä keskipisteeseen. Alku- tai loppuhetken kohdasta se ei osoita täsmälleen keskipisteeseen. Kun aikaväliä lyhennetään, kohdat tulevat lähemmäs toisiaan. Silloin nopeuden muutoksen suunta lähestyy suuntaa, joka osoittaa kappaleen kohdalta keskipisteeseen. Kiihtyvyys kertoo, kuinka nopeasti nopeus muuttuu hyvin lyhyellä aikavälillä. Siksi hetkellinen normaalikiihtyvyys osoittaa kohti keskipistettä.

<figure class="unit-photo"><img src="pics/fy5/apollo8-centrifuge.webp" alt="Kolme astronauttia makaa selällään istuimissa pyöreän luukun takana."><figcaption>Apollo 8:n astronautit sentrifugissa vuonna 1968. Sentrifugi pyörittää astronautteja ympyrää pitkin. Sentrifugissa normaalikiihtyvyys voi olla yhtä suuri kuin laukaisun kiihtyvyys.</figcaption></figure>

### Normaalikiihtyvyys osoittaa keskipisteeseen
Tasaisessa ympyräliikkeessä kiihtyvyys on kohtisuorassa nopeutta vastaan. Se osoittaa radan joka kohdassa kohti ympyrän keskipistettä. Tätä kiihtyvyyttä kutsutaan **normaalikiihtyvyydeksi** $\overline{a}_\text{n}$ tai **keskeiskiihtyvyydeksi**. Nimi tulee siitä, että kiihtyvyys on radan normaalin suuntainen. Normaali on suora, joka on kohtisuorassa tangenttia vastaan. Kiihtyvyydellä ei ole nopeuden suuntaista osaa, joten vauhti ei kasva eikä pienene. Kiihtyvyys muuttaa vain nopeuden suuntaa.

```pysahdy
Kappale kiertää ympyrää tasaisella vauhdilla. Miksi vauhti ei kasva, vaikka kappale kiihtyy?
---
Kiihtyvyys on kohtisuorassa nopeutta vastaan. Siksi se ei lisää vauhtia. Se muuttaa vain nopeuden suuntaa.
```

### Kokonaisvoima osoittaa keskipisteeseen
Newtonin toisen lain mukaan kokonaisvoima $\Sigma\overline{F}$ on samansuuntainen kuin kiihtyvyys. Kokonaisvoima on kaikkien kappaleeseen vaikuttavien voimien summa. Tasaisessa ympyräliikkeessä tämä summa osoittaa siis kohti radan keskipistettä. Keskipisteeseen osoittavaa kokonaisvoimaa kutsutaan **keskeisvoimaksi**. Ilman sitä kappale jatkaisi Newtonin ensimmäisen lain mukaan suoraan, radan tangentin suuntaan.

Keskeisvoima ei ole uusi voiman laji. Sitä ei piirretä voimakuvioon omana nuolenaan. Se on todellisten voimien summa, ja tilanne kertoo, mitkä voimat sen muodostavat. Oletetaan, että auto ajaa kaarteessa vaakasuoralla tiellä ja ilmanvastus jätetään huomiotta. Silloin autoon vaikuttaa vaakasuunnassa vain tien kitka renkaisiin. Kitka osoittaa siis kohti kaarteen keskipistettä. Narun päässä pyörivässä kivessä keskeisvoiman tuottaa narun jännitysvoima. Karusellissa istujaan sen tuottavat istuimen ja tuen voimat.

<svg data-fig="kaarre" viewBox="0 0 600 380" role="img" aria-label="Kaksi kuvaa. Vasemmalla kaarteessa oleva auto ylhäältä katsottuna: nopeus osoittaa tien suuntaan ja kiihtyvyys vasemmalle kohti keskipistettä. Oikealla auton voimakuvio takaa katsottuna: paino alas, yhtä pitkä tukivoima ylös ja kitkavoima vasemmalle kohti keskipistettä." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-4-kaarre.webp" x="0" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="27.5" y="7.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva ylhäältä}$</div></foreignObject>
  <foreignObject x="44" y="211.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{keskipiste}$</div></foreignObject>
  <foreignObject x="100" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="262.5" y="145.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="132.5" y="265.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
  <foreignObject x="352.5" y="7.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio takaa}$</div></foreignObject>
  <foreignObject x="477.5" y="283.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="499.5" y="109.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="332.5" y="233.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="331.5" y="113.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
</svg>

Voimakuviossa auto on piirretty takaa katsottuna, joten kaarteen keskipiste on vasemmalla. Pystysuunnassa auto ei kiihdy. Siksi tukivoima $\overline{N}$ ja paino $\overline{G}$ kumoavat toisensa. Kitkavoima $\overline{F}_\mu$ jää kokonaisvoimaksi. Jos tie on liukas, lepokitka ei riitä tähän. Silloin auto kääntyy vähemmän kuin tie kaartaa ja ajautuu kaarteen ulkoreunalle. Mikään ei silti työnnä autoa ulospäin.

## Kaava: Normaalikiihtyvyys
Kun kappale liikkuu tasaisessa ympyräliikkeessä, sen normaalikiihtyvyyden suuruus on
```kaavat
normaalikiihtyvyys :: a_\text{n} = \frac{v^2}{r}
```
missä $a_\text{n}$ on normaalikiihtyvyys ($\text{m/s}^2$), $v$ ratanopeus ($\text{m/s}$) ja $r$ radan säde ($\text{m}$). Kiihtyvyys kasvaa nopeuden neliön mukana. Kun nopeus kaksinkertaistuu, kiihtyvyys nelinkertaistuu. Samalla nopeudella tiukka kaarre eli pieni säde antaa suuren kiihtyvyyden. Jos tunnetaan kierrosaika $T$, ratanopeus lasketaan ensin kaavalla $v = \tfrac{2\pi r}{T}$.

Miksi juuri nopeuden neliö? Nopeus vaikuttaa kahdesti. Kun nopeus on suurempi, nopeusnuoli on pidempi. Silloin sama suunnan kääntyminen tarkoittaa suurempaa nopeuden muutosta $\Delta\overline{v}$. Lisäksi kappale kiertää kaaren nopeammin. Nopeus kääntyy siis saman kulman lyhyemmässä ajassa. Molemmat tekijät kasvavat nopeuden mukana, joten kiihtyvyys kasvaa nopeuden neliön mukana. Kun nopeus on sama mutta säde pienempi, nopeuden suunta kääntyy nopeammin. Silloin kiihtyvyys on suurempi.

```pysahdy
Pyöräilijä kulkee nopeudella $6{,}0\,\text{m/s}$ kaarteessa, jonka säde on $12\,\text{m}$. Kuinka suuri normaalikiihtyvyys on?
---
$a_\text{n} = \tfrac{v^2}{r} = \tfrac{(6{,}0\,\text{m/s})^2}{12\,\text{m}} = 3{,}0\,\text{m/s}^2$. Kiihtyvyys osoittaa kaarteen keskipisteeseen.
```

<svg data-fig="kuvaaja" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja: vaaka-akselilla ratanopeus nollasta 30:een, pystyakselilla normaalikiihtyvyys nollasta 18:aan. Kaksi käyrää nousee yhä jyrkemmin. Säteellä 50 metriä kiihtyvyys on nopeuksilla 10, 20 ja 30 arvoltaan 2, 8 ja 18. Säteellä 100 metriä arvot ovat puolet pienempiä." style="max-width:100%;font-size:24px">
  <line x1="141.5" y1="300" x2="141.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="197.5" y1="300" x2="197.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="253" y1="300" x2="253" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="308.5" y1="300" x2="308.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="364.5" y1="300" x2="364.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="300" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="260" x2="420" y2="260" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="220" x2="420" y2="220" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="180" x2="420" y2="180" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="140" x2="420" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="100" x2="420" y2="100" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="60" x2="420" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="85" y1="300" x2="434" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M446,300 L433,306 L433,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="86" y1="301" x2="86" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M86,34 L92,47 L80,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="141.5" y1="300" x2="141.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="131.5" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="197.5" y1="300" x2="197.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="181" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="253" y1="300" x2="253" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="236.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="308.5" y1="300" x2="308.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="292" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="364.5" y1="300" x2="364.5" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="348" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$25$</div></foreignObject>
  <line x1="420" y1="300" x2="420" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="403.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="79" y1="260" x2="86" y2="260" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="245.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="79" y1="220" x2="86" y2="220" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="205.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="79" y1="180" x2="86" y2="180" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="54" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$9$</div></foreignObject>
  <line x1="79" y1="140" x2="86" y2="140" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="41" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="79" y1="100" x2="86" y2="100" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="41" y="85.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="79" y1="60" x2="86" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="41" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$18$</div></foreignObject>
  <foreignObject x="56" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="452" y="285.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\text{m/s})$</div></foreignObject>
  <foreignObject x="76" y="3.5" width="112" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$a_\text{n}\ (\text{m/s}^2)$</div></foreignObject>
  <polyline points="86,300 89,300 91.5,300 94.5,300 97,299.5 100,299.5 102.5,299.5 105.5,299 108.5,299 111,298.5 114,298.5 116.5,298 119.5,297.5 122,297 125,296.5 128,296 130.5,295.5 133.5,295 136,294.5 139,294 141.5,293.5 144.5,292.5 147,292 150,291 153,290.5 155.5,289.5 158.5,288.5 161,288 164,287 166.5,286 169.5,285 172.5,284 175,283 178,282 180.5,280.5 183.5,279.5 186,278.5 189,277 192,276 194.5,274.5 197.5,273.5 200,272 203,270.5 205.5,269 208.5,267.5 211,266 214,264.5 217,263 219.5,261.5 222.5,260 225,258.5 228,256.5 230.5,255 233.5,253 236.5,251.5 239,249.5 242,247.5 244.5,246 247.5,244 250,242 253,240 256,238 258.5,236 261.5,234 264,231.5 267,229.5 269.5,227.5 272.5,225 275.5,223 278,220.5 281,218.5 283.5,216 286.5,213.5 289,211 292,208.5 295,206 297.5,203.5 300.5,201 303,198.5 306,196 308.5,193.5 311.5,190.5 314,188 317,185 320,182.5 322.5,179.5 325.5,176.5 328,174 331,171 333.5,168 336.5,165 339.5,162 342,159 345,156 347.5,152.5 350.5,149.5 353,146.5 356,143 359,140 361.5,136.5 364.5,133.5 367,130 370,126.5 372.5,123 375.5,119.5 378,116 381,112.5 384,109 386.5,105.5 389.5,102 392,98.5 395,94.5 397.5,91 400.5,87 403.5,83.5 406,79.5 409,75.5 411.5,72 414.5,68 417,64 420,60" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="86,300 89,300 91.5,300 94.5,300 97,300 100,300 102.5,299.5 105.5,299.5 108.5,299.5 111,299.5 114,299 116.5,299 119.5,299 122,298.5 125,298.5 128,298 130.5,298 133.5,297.5 136,297.5 139,297 141.5,296.5 144.5,296.5 147,296 150,295.5 153,295 155.5,295 158.5,294.5 161,294 164,293.5 166.5,293 169.5,292.5 172.5,292 175,291.5 178,291 180.5,290.5 183.5,290 186,289 189,288.5 192,288 194.5,287.5 197.5,286.5 200,286 203,285.5 205.5,284.5 208.5,284 211,283 214,282.5 217,281.5 219.5,281 222.5,280 225,279 228,278.5 230.5,277.5 233.5,276.5 236.5,275.5 239,275 242,274 244.5,273 247.5,272 250,271 253,270 256,269 258.5,268 261.5,267 264,266 267,265 269.5,263.5 272.5,262.5 275.5,261.5 278,260.5 281,259 283.5,258 286.5,257 289,255.5 292,254.5 295,253 297.5,252 300.5,250.5 303,249.5 306,248 308.5,246.5 311.5,245.5 314,244 317,242.5 320,241 322.5,240 325.5,238.5 328,237 331,235.5 333.5,234 336.5,232.5 339.5,231 342,229.5 345,228 347.5,226.5 350.5,225 353,223 356,221.5 359,220 361.5,218.5 364.5,216.5 367,215 370,213.5 372.5,211.5 375.5,210 378,208 381,206.5 384,204.5 386.5,203 389.5,201 392,199 395,197.5 397.5,195.5 400.5,193.5 403.5,191.5 406,190 409,188 411.5,186 414.5,184 417,182 420,180" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 7"/>
  <line x1="197.5" y1="273.5" x2="197.5" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="86" y1="273.5" x2="197.5" y2="273.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="197.5" cy="273.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="308.5" y1="193.5" x2="308.5" y2="300" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="86" y1="193.5" x2="308.5" y2="193.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="308.5" cy="193.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="430" y="45.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$r = 50\,\text{m}$</div></foreignObject>
  <foreignObject x="430" y="165.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$r = 100\,\text{m}$</div></foreignObject>
</svg>

Kuvaajassa säteellä $50\,\text{m}$ normaalikiihtyvyys on nopeudella $10\,\text{m/s}$ vain $2{,}0\,\text{m/s}^2$. Nopeudella $20\,\text{m/s}$ se on jo $8{,}0\,\text{m/s}^2$. Kun säde on kaksinkertainen, $100\,\text{m}$, kiihtyvyys on samalla nopeudella puolet pienempi, $4{,}0\,\text{m/s}^2$.

### Newtonin toinen laki ympyräliikkeessä
Newtonin toisen lain mukaan kappaleeseen vaikuttavien voimien summan suuruus on tasaisessa ympyräliikkeessä
```latex
\Sigma F = m\,\frac{v^2}{r}
```
missä $\Sigma F$ on keskipisteeseen osoittava kokonaisvoima ($\text{N}$) ja $m$ kappaleen massa ($\text{kg}$). Lasku tehdään kuten luvussa *Voimakuvio ja voimien yhteisvaikutus*. Piirrä ensin voimakuvio ja valitse yksi akseli osoittamaan kohti radan keskipistettä. Silloin keskipisteeseen osoittavat voimat ovat positiivisia ja poispäin osoittavat negatiivisia. Niiden summa on $m\tfrac{v^2}{r}$. Kohtisuoraan ratatasoa vastaan kappale ei kiihdy, joten siinä suunnassa voimien summa on nolla.

```pysahdy
Kappale kiertää ympyrää tasaisella vauhdilla. Vauhti pysyy samana, joten voimien summa on nolla. Onko tämä totta?
---
Ei ole. Nopeuden suunta muuttuu, joten kappale kiihtyy. Voimien summa on $m\tfrac{v^2}{r}$, ja se osoittaa keskipisteeseen.
```

### Nyppylä ja notko
Kun auto ajaa tasaisella vauhdilla nyppylän huipun yli, se on hetken ympyräradalla. Radan keskipiste on tien alapuolella. Kiihtyvyys osoittaa silloin alas, joten paino on suurempi kuin tien tukivoima: $G - N = m\tfrac{v^2}{r}$. Tukivoima on painoa pienempi, ja matkustaja tuntee itsensä kevyeksi. Mitä suurempi nopeus, sitä pienempi tukivoima. Jos $\tfrac{v^2}{r}$ kasvaa yhtä suureksi kuin $g$, tukivoima on nolla. Jos se kasvaa suuremmaksi kuin $g$, auto irtoaa hetkeksi tiestä.

<svg data-fig="nyppyla" viewBox="0 0 600 420" role="img" aria-label="Neljä kuvaa. Vasemmalla auto nyppylän huipulla, oikealla auto notkon pohjalla, ja alla kummankin voimakuvio. Nyppylän huipulla tukivoima on painoa pienempi ja kiihtyvyys osoittaa alas. Notkon pohjalla tukivoima on painoa suurempi ja kiihtyvyys osoittaa ylös." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-4-nyppyla.webp" x="0" y="1.2" width="600" height="428.8" preserveAspectRatio="none"/>
  <foreignObject x="58.5" y="7.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{nyppylän huippu}$</div></foreignObject>
  <foreignObject x="377.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{notkon pohja}$</div></foreignObject>
  <foreignObject x="111.5" y="371.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="185.5" y="243.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="241.5" y="271.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
  <foreignObject x="411.5" y="371.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="485.5" y="163.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="541.5" y="243.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
</svg>

Notkon pohjalla keskipiste on tien yläpuolella, ja kiihtyvyys osoittaa ylös. Silloin tukivoiman on oltava painoa suurempi: $N - G = m\tfrac{v^2}{r}$. Siksi vuoristoradan notkossa matkustaja painuu istuinta vasten ja tuntee itsensä raskaaksi. Kummassakin tapauksessa paino on sama $mg$. Vain tukivoima muuttuu niin, että kokonaisvoima osoittaa kohti kaaren keskipistettä.

## Esimerkki
Henkilöauto, jonka massa on $1200\,\text{kg}$, ajaa vaakasuoran tien kaarteessa tasaisella nopeudella $54\,\text{km/h}$. Kaarteen säde on $45\,\text{m}$. Kuinka suuri kitkavoima tien on kohdistettava autoon? Kuinka suuri renkaiden ja tien välisen lepokitkakertoimen on vähintään oltava? Ilmanvastus ja vierimisvastus jätetään huomiotta. Renkaiden voimat lasketaan yhteen.

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 1200\,\text{kg}$, $v = 54\,\text{km/h}$, $r = 45\,\text{m}$ ja $g = 9{,}81\,\text{m/s}^2$.

Kysytään tien kitkavoimaa $F_\mu$ ja pienintä lepokitkakerrointa $\mu_0$.

<!-- vaihe -->

**Periaate.** Valitaan kappaleeksi auto. Siihen vaikuttavat Maa (paino $\overline{G}$) ja tie (tukivoima $\overline{N}$ ja kitka $\overline{F}_\mu$). Auto on tasaisessa ympyräliikkeessä. Newtonin toisen lain mukaan kokonaisvoima osoittaa siis kohti kaarteen keskipistettä, ja sen suuruus on $m\tfrac{v^2}{r}$.

Ainoa vaakasuora voima on kitka, joten se osoittaa kohti keskipistettä. Renkaat eivät liu'u sivuttain, joten kitka on lepokitkaa. Lepokitka on enintään $\mu_0 N$. Voimakuviossa auto on takaa katsottuna ja kaarteen keskipiste on oikealla. $x$-akseli osoittaa kohti keskipistettä ja $y$-akseli ylös.

<svg data-fig="esimerkki" viewBox="0 0 600 360" role="img" aria-label="Auton voimakuvio takaa katsottuna. Kaarteen keskipiste on oikealla. Paino alas, yhtä pitkä tukivoima ylös ja kitkavoima oikealle kohti keskipistettä, noin puolet painon pituudesta. Akselit: x oikealle ja y ylös." style="max-width:100%;font-size:24px">
  <line x1="80" y1="208" x2="440" y2="208" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="80" y1="208" x2="70" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="208" x2="86" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="112" y1="208" x2="102" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="128" y1="208" x2="118" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="144" y1="208" x2="134" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="160" y1="208" x2="150" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="176" y1="208" x2="166" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="192" y1="208" x2="182" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="208" y1="208" x2="198" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="224" y1="208" x2="214" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="208" x2="230" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="208" x2="246" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="272" y1="208" x2="262" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="288" y1="208" x2="278" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="304" y1="208" x2="294" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="208" x2="310" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="336" y1="208" x2="326" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="352" y1="208" x2="342" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="368" y1="208" x2="358" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384" y1="208" x2="374" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="400" y1="208" x2="390" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="416" y1="208" x2="406" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="432" y1="208" x2="422" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="195" y="132" width="150" height="76" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="270" y1="170" x2="270" y2="283" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M270,300 L262,282 L278,282 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="279.5" y="281.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="246" y1="208" x2="246" y2="95" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M246,78 L254,96 L238,96 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="203.5" y="71.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="345" y1="208" x2="394.5" y2="208" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M411.5,208 L393.5,216 L393.5,200 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="393" y="217.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="310" y1="90" x2="378" y2="90" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M367,96.5 L380,90 L367,83.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="379.5" y="71.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}_\text{n}$</div></foreignObject>
  <foreignObject x="347" y="25.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{kohti keskipistettä}$</div></foreignObject>
  <line x1="52" y1="318" x2="87" y2="318" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M96,318 L86,322.5 L86,313.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="52" y1="318" x2="52" y2="283" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M52,274 L56.5,284 L47.5,284 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="100" y="303.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$x$</div></foreignObject>
  <foreignObject x="42" y="245.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**Kaava ratkaistuna.** Kuviosta luetaan liikeyhtälöt, ja kysytyt suureet ratkaistaan:
```latex
\begin{aligned}
&x\text{:}\ \ F_\mu = m\frac{v^2}{r} \\
&y\text{:}\ \ N - mg = 0 \\
&F_\mu \le \mu_0 N = \mu_0 mg \\
&\mu_0 \ge \frac{v^2}{gr}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Nopeus muutetaan yksikköön $\text{m/s}$: $v = 54\,\text{km/h} = \tfrac{54\cdot 1000\,\text{m}}{3600\,\text{s}} = 15\,\text{m/s}$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen:
```latex
\begin{aligned}
&F_\mu = m\frac{v^2}{r} \\
&\phantom{F_\mu} = 1200\,\text{kg}\cdot\frac{(15\,\text{m/s})^2}{45\,\text{m}} \\
&\phantom{F_\mu} = 6000\,\text{N} \\[4pt]
&\mu_0 \ge \frac{v^2}{gr} \\
&\phantom{\mu_0} = \frac{(15\,\text{m/s})^2}{9{,}81\,\text{m/s}^2\cdot 45\,\text{m}} \\
&\phantom{\mu_0} \approx 0{,}510
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Tien kitkavoima on $F_\mu \approx 6{,}0\,\text{kN}$ kohti kaarteen keskipistettä. Lepokitkakertoimen on oltava vähintään $0{,}51$. Tuloksessa on kaksi merkitsevää numeroa, kuten nopeudessa $54\,\text{km/h}$ ja säteessä $45\,\text{m}$.

<!-- vaihe -->

**Järkevyys.** Normaalikiihtyvyys on $a_\text{n} = \tfrac{(15\,\text{m/s})^2}{45\,\text{m}} = 5{,}0\,\text{m/s}^2$. Se on noin puolet putoamiskiihtyvyydestä, joten kitkan on oltava noin puolet painosta $11{,}8\,\text{kN}$. Kuivalla asfaltilla lepokitkakerroin on noin $0{,}8$, joten auto pysyy kaarteessa. Märällä asfaltilla kerroin voi olla noin $0{,}5$. Silloin pito on rajoilla. Jäällä pito pettäisi. Massa supistuu, joten kertoimen vaatimus on sama kevyelle ja raskaalle autolle.

## Yleinen virhekäsitys
Moni ajattelee, että ympyräliikkeessä kappaleeseen vaikuttaa ulospäin **keskipakoisvoima**. Sen luullaan pitävän kappaleen radalla tai heittävän sen ulos kaarteesta. Maahan sidotussa koordinaatistossa sellaista todellista voimaa ei ole. Mikään kappale ei vedä tai työnnä autoa tai matkustajaa ulospäin. Kun auto kääntyy, matkustajan keho pyrkii jatkamaan suoraan. Ovi painuu häntä vasten ja työntää häntä sisäänpäin, kohti kaarteen keskipistettä. Tämä tuntuu painautumisena ulospäin. Kun pito pettää, auto ei lennä säteen suuntaan ulos. Se jatkaa suoremmin kuin tie kaartaa. Auton mukana kääntyvässä koordinaatistossa keskipakoisvoimaa voidaan käyttää näennäisvoimana. Näennäisvoima selittää matkustajan tunteen, mutta mikään kappale ei aiheuta sitä. Tämän kurssin voimakuviot piirretään maahan sidotussa koordinaatistossa. Niissä on siksi vain todellisia voimia. Toinen virhe on piirtää keskeisvoima voimakuvioon omaksi nuolekseen. Keskeisvoima on todellisten voimien, kuten kitkan tai jännitysvoiman, summa.

## Tiivistelmä
- Tasaisessa ympyräliikkeessä ratanopeus on vakio, mutta nopeuden suunta muuttuu. Siksi kappale kiihtyy.
- Normaalikiihtyvyys eli keskeiskiihtyvyys osoittaa kohti radan keskipistettä. Sen suuruus on $a_\text{n} = \tfrac{v^2}{r}$.
- Kappaleeseen vaikuttavien voimien summa eli keskeisvoima osoittaa kohti keskipistettä: $\Sigma F = m\tfrac{v^2}{r}$. Se on todellisten voimien summa, ei oma voimansa.
- Kaarteessa keskeisvoiman antaa tien kitka ja narussa jännitysvoima. Nyppylän huipulla tukivoima on painoa pienempi, notkon pohjalla suurempi.
- Maahan sidotussa koordinaatistossa todellista keskipakoisvoimaa ei ole. Pyörivässä koordinaatistossa se on näennäisvoima. Kun keskipisteeseen osoittava voima ei riitä, kappale jatkaa suoremmin kuin rata kaartaa.
