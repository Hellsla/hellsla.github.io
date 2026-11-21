# Normaalikiihtyvyys ja ympyräliikkeen liikeyhtälö

> **Miksi** auto suistuu liukkaassa kaarteessa ulos tieltä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvinen maantie kaartaa metsän läpi oikealle ja katoaa kauas mäkien taakse. Kaarteen keskellä ajaa henkilöauto takaapäin nähtynä. Tien reunoilla on lumipenkat ja kuusia." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-4-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Nopeuden suunta muuttuu, joten kappale kiihtyy
Luvussa *Ympyrärata: jaksonaika ja ratanopeus* opit, että tasaisessa ympyräliikkeessä kappale kiertää ympyrärataa vakiovauhdilla. Nopeuden suuruus eli ratanopeus $v$ pysyy samana, mutta nopeuden suunta muuttuu koko ajan: nopeus $\overline{v}$ on aina radan tangentin suuntainen. Nopeus on vektori, joten suunnan muutoskin on nopeuden muutos. Kun nopeus muuttuu, kappaleella on kiihtyvyys. Tasaisessa ympyräliikkeessä kappale siis kiihtyy, vaikka sen vauhti ei muutu.

<svg data-fig="muutos" viewBox="0 0 600 340" role="img" aria-label="Kaksi kuvaa. Vasemmalla kappale kiertää ympyrärataa vastapäivään tasaisella vauhdilla. Kahdessa kohdassa radan yläosassa sininen nopeusnuoli v 1 ja v 2 on radan tangentin suuntainen; nuolet ovat yhtä pitkiä mutta eri suuntiin. Radan ylimmässä kohdassa näiden välissä oranssi kiihtyvyysnuoli a n osoittaa suoraan alas radan keskipisteeseen. Oikealla samat nopeusnuolet on piirretty samasta pisteestä. Nuolten kärkien välinen nuoli, nopeuden muutos delta v, osoittaa suoraan alas eli samaan suuntaan kuin kiihtyvyys, kohti radan keskipistettä. Nopeusnuolet ovat molemmissa kuvissa yhtä pitkiä, samassa mittakaavassa." style="max-width:100%;font-size:24px">
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

Kuvassa kappaleen nopeus on ensin $\overline{v}_1$ ja hetken kuluttua $\overline{v}_2$. Kun nuolet piirretään samasta pisteestä, niiden kärkien välinen nuoli on nopeuden muutos $\Delta\overline{v}$. Se osoittaa radan sisäpuolelle, samaan suuntaan kuin aikavälin puolivälistä keskipisteeseen piirretty nuoli, mutta ei täsmälleen keskipisteeseen alku- tai loppuhetken kohdasta. Kun aikaväliä pienennetään, kohdat lähestyvät toisiaan, ja nopeuden muutoksen suunta lähestyy kappaleen kohdalta keskipisteeseen osoittavaa suuntaa. Hetkellinen kiihtyvyys on nopeuden muutos aikayksikköä kohti hyvin lyhyellä aikavälillä, joten hetkellinen normaalikiihtyvyys osoittaa keskipisteeseen.

<figure class="unit-photo"><img src="pics/fy5/apollo8-centrifuge.webp" alt="Kolme avaruuspukuista astronauttia makaa selällään istuimissa pyöreän luukun takana."><figcaption>Apollo 8:n miehistö sentrifugin kammiossa vuonna 1968. Sentrifugi pyörittää kammiota ympyrärataa pitkin, ja normaalikiihtyvyys jäljittelee laukaisun suurta kiihtyvyyttä.</figcaption></figure>

### Normaalikiihtyvyys osoittaa keskipisteeseen
Tasaisen ympyräliikkeen kiihtyvyys on kohtisuorassa nopeutta vastaan ja osoittaa radan joka kohdassa kohti ympyrän keskipistettä. Sitä kutsutaan **normaalikiihtyvyydeksi** $\overline{a}_\text{n}$ tai **keskeiskiihtyvyydeksi**. Nimi tulee siitä, että kiihtyvyys on radan normaalin eli tangenttia vastaan kohtisuoran suoran suuntainen. Koska kiihtyvyydellä ei ole nopeuden suuntaista osaa, vauhti ei kasva eikä pienene: kiihtyvyys muuttaa vain nopeuden suuntaa.

```pysahdy
Kappale kiertää ympyrärataa tasaisella vauhdilla. Miksi vauhti ei kasva, vaikka kappaleella on kiihtyvyys?
---
Kiihtyvyys on kohtisuorassa nopeutta vastaan, joten sillä ei ole nopeuden suuntaista osaa. Se muuttaa vain nopeuden suuntaa.
```

### Kokonaisvoima osoittaa keskipisteeseen
Newtonin toisen lain mukaan kokonaisvoima $\Sigma\overline{F}$ on samansuuntainen kuin kiihtyvyys. Tasaisessa ympyräliikkeessä kappaleeseen vaikuttavien voimien summa osoittaa siis kohti radan keskipistettä. Tätä keskipisteeseen osoittavaa kokonaisvoimaa kutsutaan **keskeisvoimaksi**. Ilman sitä kappale jatkaisi Newtonin ensimmäisen lain mukaisesti suoraan, radan tangentin suuntaan.

Keskeisvoima ei ole uusi voiman laji, eikä sitä piirretä voimakuvioon omana nuolenaan. Se on todellisten voimien summa, ja tilanne kertoo, mitkä voimat sen muodostavat. Kun auto ajaa kaarteessa vaakasuoralla tiellä ja ilmanvastus jätetään huomiotta, ainoa vaakasuora voima autoon on tien kitka renkaisiin, joten kitka osoittaa kohti kaarteen keskipistettä. Narun päässä pyörivään kiveen sen tuottaa narun jännitysvoima, ja karusellissa istujaan istuimen ja tuen voimat.

<svg data-fig="kaarre" viewBox="0 0 600 380" role="img" aria-label="Kaksi kuvaa. Vasemmalla tilannekuva ylhäältä: tie kaartaa vasemmalle, ja auto on kaarteessa. Kaarteen keskipiste on vasemmalla, ja katkoviiva r yhdistää sen autoon. Auton vieressä sininen nopeusnuoli v osoittaa ylös tien suuntaisesti ja oranssi kiihtyvyysnuoli a n vasemmalle kohti keskipistettä. Oikealla auton voimakuvio takaa katsottuna, auto suorakulmiona tien päällä: paino G keskipisteestä alas, tien tukivoima N alapinnasta ylös yhtä pitkänä ja tien kitkavoima alapinnan vasemmasta kulmasta vasemmalle kohti kaarteen keskipistettä, noin puolet painon pituudesta. Erillään oranssi kiihtyvyysnuoli a n vasemmalle." style="max-width:100%;font-size:24px">
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

Voimakuviossa auto on piirretty takaa katsottuna, jolloin kaarteen keskipiste on vasemmalla. Pystysuunnassa auto ei kiihdy, joten tukivoima $\overline{N}$ ja paino $\overline{G}$ kumoavat toisensa. Kitkavoima $\overline{F}_\mu$ jää kokonaisvoimaksi. Jos tie on liukas, lepokitka ei riitä tähän. Silloin auto kaartaa vähemmän kuin tie ja ajautuu ulkokaarteen puolelle, vaikka mikään ei työnnä sitä ulospäin.

## Kaava: Normaalikiihtyvyys
Kun kappale liikkuu tasaisessa ympyräliikkeessä, sen normaalikiihtyvyyden suuruus on
```kaavat
normaalikiihtyvyys :: a_\text{n} = \frac{v^2}{r}
```
missä $a_\text{n}$ on normaalikiihtyvyys ($\text{m/s}^2$), $v$ ratanopeus ($\text{m/s}$) ja $r$ radan säde ($\text{m}$). Kiihtyvyys kasvaa nopeuden neliön mukana: kun nopeus kaksinkertaistuu, kiihtyvyys nelinkertaistuu. Samalla nopeudella tiukka kaarre eli pieni säde antaa suuren kiihtyvyyden. Jos tunnetaan kierrosaika $T$, ratanopeus saadaan ensin kaavasta $v = \tfrac{2\pi r}{T}$.

Miksi juuri nopeuden neliö? Nopeus vaikuttaa kahdesti. Suuremmalla nopeudella nopeusnuoli on pidempi, joten sama suunnan kääntyminen merkitsee suurempaa nopeuden muutosta $\Delta\overline{v}$. Lisäksi kappale kiertää kaaren nopeammin, joten nopeus kääntyy saman kulman lyhyemmässä ajassa. Kumpikin tekijä kasvaa nopeuden mukana, joten kiihtyvyys kasvaa nopeuden neliön mukana. Samalla nopeudella pienemmän säteen kaarteessa nopeuden suunta kääntyy nopeammin, joten kiihtyvyys on suurempi.

```pysahdy
Pyöräilijä kulkee nopeudella $6{,}0\,\text{m/s}$ kaarteessa, jonka säde on $12\,\text{m}$. Mikä on normaalikiihtyvyys?
---
$a_\text{n} = \tfrac{v^2}{r} = \tfrac{(6{,}0\,\text{m/s})^2}{12\,\text{m}} = 3{,}0\,\text{m/s}^2$, ja se osoittaa kaarteen keskipisteeseen.
```

<svg data-fig="kuvaaja" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja mittakaavassa: vaaka-akselilla ratanopeus v metreinä sekunnissa nollasta 30:een, pystyakselilla normaalikiihtyvyys a n metreinä sekunnissa toiseen nollasta 18:aan. Kaksi oranssia käyrää nousee origosta yhä jyrkemmin. Säteellä 50 metriä yhtenäinen käyrä: nopeudella 10 kiihtyvyys on 2, nopeudella 20 se on 8 ja nopeudella 30 se on 18. Säteellä 100 metriä katkoviivakäyrä on puolet alempana: nopeudella 20 kiihtyvyys on 4 ja nopeudella 30 se on 9. Pisteet nopeuksilla 10 ja 20 on merkitty yhtenäiselle käyrälle apuviivoin." style="max-width:100%;font-size:24px">
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

Kuvaajassa säteellä $50\,\text{m}$ normaalikiihtyvyys on nopeudella $10\,\text{m/s}$ vain $2{,}0\,\text{m/s}^2$, mutta nopeudella $20\,\text{m/s}$ jo $8{,}0\,\text{m/s}^2$. Kaksinkertaisella säteellä $100\,\text{m}$ se on samalla nopeudella puolet pienempi, $4{,}0\,\text{m/s}^2$.

### Newtonin toinen laki ympyräliikkeessä
Newtonin toisen lain mukaan kappaleeseen vaikuttavien voimien summan suuruus on tasaisessa ympyräliikkeessä
```latex
\Sigma F = m\,\frac{v^2}{r}
```
missä $\Sigma F$ on keskipisteeseen osoittava kokonaisvoima ($\text{N}$) ja $m$ kappaleen massa ($\text{kg}$). Laskussa toimitaan kuten luvussa *Voimakuvio ja voimien yhteisvaikutus*: piirretään ensin voimakuvio ja valitaan yksi akseli osoittamaan kohti radan keskipistettä. Silloin keskipisteeseen osoittavat voimat ovat positiivisia, poispäin osoittavat negatiivisia, ja niiden summa on $m\tfrac{v^2}{r}$. Kohtisuoraan ratatasoa vastaan kappale ei kiihdy, joten siinä suunnassa voimien summa on nolla.

```pysahdy
Kappale kiertää ympyrärataa tasaisella vauhdilla. Koska vauhti pysyy samana, voimien summa on nolla. Pitääkö tämä paikkansa?
---
Ei pidä. Nopeuden suunta muuttuu, joten kiihtyvyys ei ole nolla. Voimien summa on $m\tfrac{v^2}{r}$ ja osoittaa keskipisteeseen.
```

### Nyppylä ja notko
Kun auto ajaa tasaisella vauhdilla nyppylän huipun yli, se on hetken ympyräradalla, jonka keskipiste on tien alapuolella. Kiihtyvyys osoittaa silloin alas, joten paino on suurempi kuin tien tukivoima: $G - N = m\tfrac{v^2}{r}$. Tukivoima on painoa pienempi, ja matkustaja tuntee itsensä kevyeksi. Mitä suurempi nopeus, sitä pienempi tukivoima. Jos $\tfrac{v^2}{r}$ kasvaa yhtä suureksi kuin $g$, tukivoima on nolla. Jos se kasvaa suuremmaksi kuin $g$, auto irtoaa hetkeksi tiestä.

<svg data-fig="nyppyla" viewBox="0 0 600 420" role="img" aria-label="Neljä kuvaa kahdessa sarakkeessa. Vasemmalla ylhäällä auto nyppylän huipulla, oikealla ylhäällä auto notkon pohjalla; kummassakin auto ajaa samalla nopeudella oikealle. Alla kummankin auton voimakuvio, auto suorakulmiona: paino G keskipisteestä alas ja tien tukivoima N alapinnasta ylös. Nyppylän huipulla tukivoima on lyhyempi kuin paino, noin kuusi kymmenesosaa siitä, ja oranssi kiihtyvyysnuoli a n osoittaa alas, kohti nyppylän kaaren keskipistettä. Notkon pohjalla tukivoima on pidempi kuin paino, noin 1,4-kertainen, ja kiihtyvyysnuoli osoittaa ylös, kohti notkon kaaren keskipistettä. Paino on molemmissa yhtä pitkä." style="max-width:100%;font-size:24px">
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
Henkilöauto, jonka massa on $1200\,\text{kg}$, ajaa vaakasuoran tien kaarteessa tasaisella nopeudella $54\,\text{km/h}$. Kaarteen säde on $45\,\text{m}$. Kuinka suuri kitkavoima tien on kohdistettava autoon, ja kuinka suuri renkaiden ja tien välisen lepokitkakertoimen on vähintään oltava? Ilmanvastus ja vierimisvastus jätetään huomiotta, ja renkaiden voimat lasketaan yhteen.

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 1200\,\text{kg}$, $v = 54\,\text{km/h}$, $r = 45\,\text{m}$ ja $g = 9{,}81\,\text{m/s}^2$.

Kysytään tien kitkavoimaa $F_\mu$ ja pienintä lepokitkakerrointa $\mu_0$.

<!-- vaihe -->

**Periaate.** Valitaan kappaleeksi auto. Siihen vaikuttavat Maa (paino $\overline{G}$) ja tie (tukivoima $\overline{N}$ ja kitka $\overline{F}_\mu$). Auto on tasaisessa ympyräliikkeessä, joten Newtonin toisen lain mukaan kokonaisvoima osoittaa kohti kaarteen keskipistettä ja on suuruudeltaan $m\tfrac{v^2}{r}$.

Ainoa vaakasuora voima on kitka, joten se osoittaa kohti keskipistettä. Renkaat eivät liu'u sivuttain, joten kitka on lepokitkaa, enintään $\mu_0 N$. Voimakuviossa auto on takaa katsottuna ja kaarteen keskipiste oikealla, $x$-akseli kohti keskipistettä ja $y$-akseli ylös.

<svg data-fig="esimerkki" viewBox="0 0 600 360" role="img" aria-label="Auton voimakuvio takaa katsottuna, auto suorakulmiona tien päällä. Kaarteen keskipiste on oikealla. Paino G keskipisteestä alas, tien tukivoima N alapinnasta ylös yhtä pitkänä ja tien kitkavoima alapinnan oikeasta kulmasta oikealle kohti kaarteen keskipistettä, noin puolet painon pituudesta. Erillään oranssi kiihtyvyysnuoli a n oikealle. Nurkassa akselit: x oikealle kohti keskipistettä ja y ylös." style="max-width:100%;font-size:24px">
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

**Kaava ratkaistuna.** Kuviosta luetaan liikeyhtälöt ja ratkaistaan kysytyt suureet:
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

**Tulos.** Tien kitkavoima on $F_\mu \approx 6{,}0\,\text{kN}$ kohti kaarteen keskipistettä, ja lepokitkakertoimen on oltava vähintään $0{,}51$, kahden merkitsevän numeron tarkkuudella kuten nopeus $54\,\text{km/h}$ ja säde $45\,\text{m}$.

<!-- vaihe -->

**Järkevyys.** Normaalikiihtyvyys on $a_\text{n} = \tfrac{(15\,\text{m/s})^2}{45\,\text{m}} = 5{,}0\,\text{m/s}^2$, noin puolet putoamiskiihtyvyydestä, joten kitkan on oltava noin puolet painosta $11{,}8\,\text{kN}$. Kuivalla asfaltilla lepokitkakerroin on noin $0{,}8$, joten auto pysyy kaarteessa. Märällä asfaltilla, jossa kerroin voi olla noin $0{,}5$, pito on rajoilla, ja jäällä se pettäisi. Massa supistuu, joten kertoimen vaatimus on sama kevyelle ja raskaalle autolle.

## Yleinen virhekäsitys
Moni ajattelee, että ympyräliikkeessä kappaleeseen vaikuttaa ulospäin **keskipakoisvoima**, joka pitää sen radalla tai heittää sen kaarteesta ulos. Maahan sidotussa eli inertiaalikoordinaatistossa sellaista todellista voimaa ei ole: mikään kappale ei vedä tai työnnä autoa tai matkustajaa ulospäin. Kun auto kääntyy, matkustajan keho pyrkii jatkamaan suoraan. Ovi painuu häntä vasten ja työntää häntä sisäänpäin, kohti kaarteen keskipistettä, ja se tuntuu painautumisena ulospäin. Kun pito pettää, auto ei lennä säteen suuntaisesti ulos, vaan jatkaa suoremmin kuin tie kaartaa. Auton mukana kääntyvässä, kiihtyvässä koordinaatistossa keskipakoisvoimaa voidaan käyttää näennäisvoimana, joka selittää matkustajan kokemuksen, mutta sitä ei aiheuta mikään kappale. Tämän kurssin voimakuviot piirretään maahan sidotussa koordinaatistossa, joten niissä on vain todellisia vuorovaikutusvoimia. Toinen virhe on piirtää voimakuvioon keskeisvoima omaksi nuolekseen. Keskeisvoima on todellisten voimien, kuten kitkan tai jännitysvoiman, summa.

## Tiivistelmä
- Tasaisessa ympyräliikkeessä ratanopeus on vakio, mutta nopeuden suunta muuttuu, joten kappale kiihtyy.
- Normaalikiihtyvyys eli keskeiskiihtyvyys osoittaa kohti radan keskipistettä, ja sen suuruus on $a_\text{n} = \tfrac{v^2}{r}$.
- Kappaleeseen vaikuttavien voimien summa eli keskeisvoima osoittaa kohti keskipistettä: $\Sigma F = m\tfrac{v^2}{r}$. Se on todellisten voimien summa, ei oma voimansa.
- Kaarteessa keskeisvoiman antaa tien kitka, narussa jännitysvoima. Nyppylän huipulla tukivoima on painoa pienempi, notkon pohjalla suurempi.
- Maahan sidotussa koordinaatistossa todellista keskipakoisvoimaa ei ole; pyörivässä koordinaatistossa se on näennäisvoima. Kun keskipisteeseen osoittava voima ei riitä, kappale jatkaa suoremmin kuin rata kaartaa.
