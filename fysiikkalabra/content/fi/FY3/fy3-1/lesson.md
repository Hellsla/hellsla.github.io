# Voima vuorovaikutuksen mittana ja paino $G = mg$

> **Miksi** astronautti painaa Kuussa vain kuudesosan siitä, mitä hän painaa Maassa, vaikka hänestä ei ole kadonnut mitään?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: astronautti loikkaa Kuun harmaalla pinnalla, ja hänen jalanjälkensä näkyvät pölyssä. Mustalla taivaalla näkyy Maa, jossa on meriä, mantereita ja pilviä." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-1-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Kun kaksi kappaletta vaikuttaa toisiinsa, ne ovat vuorovaikutuksessa. Esimerkiksi Maa vetää omenaa puoleensa. Voima kertoo, kuinka voimakas vuorovaikutus on: mitä suurempi voima, sitä voimakkaampi vuorovaikutus. Voiman yksikkö on newton (N), ja noin $1\,\text{N}$ on sadan gramman omenan paino Maassa. Tässä vaiheessa kiinnostaa vain voiman suuruus, ja kuvissa nuoli näyttää, mihin suuntaan voima osoittaa.

Voiman voi mitata voimamittarilla. Siinä on jousi, joka venyy sitä enemmän, mitä suurempi voima siihen vaikuttaa.

<svg data-fig="forcemeter" viewBox="0 0 600 410" role="img" aria-label="Voimamittari, periaatekuva, ei mittakaavassa. Kaksi samanlaista jousta ripustettu telineeseen: vasemmanpuoleiseen on ripustettu kappale, jonka massa on m, oikeanpuoleiseen kaksi samanlaista kappaletta. Kaksinkertainen paino venyttää jousta kaksinkertaisen matkan. Kunkin kappaleen paino G on alaspäin osoittava nuoli." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-1-forcemeter.webp" x="-1.3" y="0" width="603" height="417.1" preserveAspectRatio="none"/>
  <foreignObject x="160" y="176.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m$</div></foreignObject>
  <foreignObject x="184" y="219.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$G$</div></foreignObject>
  <foreignObject x="360" y="226.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m$</div></foreignObject>
  <foreignObject x="360" y="276.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m$</div></foreignObject>
  <foreignObject x="384" y="337.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2G$</div></foreignObject>
  <foreignObject x="260" y="116.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <foreignObject x="460" y="141.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2x$</div></foreignObject>
</svg>

Venymä on suoraan verrannollinen voimaan, kun jousta ei venytetä liikaa: kaksinkertainen voima venyttää jousta kaksinkertaisen matkan. Kuvaaja (voima, venymä) on siis suora, joka kulkee origon kautta, kuten FY1:n suoraan verrannollisissa malleissa, esimerkiksi tasaisen liikkeen $s = v t$. Jos $5{,}0\,\text{N}$ venyttää jousta $2{,}0\,\text{cm}$, niin $10\,\text{N}$ venyttää sitä $4{,}0\,\text{cm}$ ja $2{,}5\,\text{N}$ venyttää sitä $1{,}0\,\text{cm}$.

```pysahdy
Jousi venyy $3{,}0\,\text{cm}$, kun siihen vaikuttaa $4{,}0\,\text{N}$:n voima. Kuinka paljon se venyy $12\,\text{N}$:n voimalla?
---
Venymä on suoraan verrannollinen voimaan. Voima on kolminkertainen, joten venymä on $3 \cdot 3{,}0\,\text{cm} = 9{,}0\,\text{cm}$.
```

<svg data-fig="force-extension" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja mittakaavassa: jousen venymä x senttimetreinä voiman F funktiona, kun F on 0–11 N. Mittauspisteet 2,5 N ja 1,0 cm, 5,0 N ja 2,0 cm sekä 10 N ja 4,0 cm ovat samalla origon kautta kulkevalla suoralla; katkoviivat näyttävät pisteiden arvot akseleilla." style="max-width:100%;font-size:24px">
  <line x1="179.5" y1="290" x2="179.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="267.5" y1="290" x2="267.5" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="355" y1="290" x2="355" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="443" y1="290" x2="443" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="246" x2="478" y2="246" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="202" x2="478" y2="202" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="158" x2="478" y2="158" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="114" x2="478" y2="114" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="290" x2="492" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M504,290 L491,296 L491,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="291" x2="92" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,44 L98,57 L86,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="179.5" y1="290" x2="179.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="157" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}5$</div></foreignObject>
  <line x1="267.5" y1="290" x2="267.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="245" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5{,}0$</div></foreignObject>
  <line x1="355" y1="290" x2="355" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="332.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$7{,}5$</div></foreignObject>
  <line x1="443" y1="290" x2="443" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="426.5" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="85" y1="246" x2="92" y2="246" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}0$</div></foreignObject>
  <line x1="85" y1="202" x2="92" y2="202" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="187.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2{,}0$</div></foreignObject>
  <line x1="85" y1="158" x2="92" y2="158" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="143.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3{,}0$</div></foreignObject>
  <line x1="85" y1="114" x2="92" y2="114" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="99.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4{,}0$</div></foreignObject>
  <foreignObject x="62" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="510" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\text{N})$</div></foreignObject>
  <foreignObject x="82" y="13.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{cm})$</div></foreignObject>
  <polyline points="92,290 478,96.5" fill="none" stroke="#2f74b5" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="179.5" y1="246" x2="179.5" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="246" x2="179.5" y2="246" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="267.5" y1="202" x2="267.5" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="202" x2="267.5" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="443" y1="114" x2="443" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="92" y1="114" x2="443" y2="114" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="179.5" cy="246" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="267.5" cy="202" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="443" cy="114" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="309.5" y="222.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{suora origon kautta}$</span></div></foreignObject>
</svg>

Asteikko kalibroidaan ripustamalla jouseen samanlaisia pieniä kappaleita, joiden kunkin massa on noin $100\,\text{g}$ eli paino noin $1\,\text{N}$:

- Yksi kappale venyttää jousta tietyn matkan, ja kohta merkitään $1\,\text{N}$:ksi.
- Kukin kappale vetää jousta yhtä voimakkaasti, joten kaksi kappaletta vetää sitä kaksinkertaisella voimalla ja venyttää sitä kaksinkertaisen matkan. Kohta merkitään $2\,\text{N}$:ksi, ja niin edelleen.
- Sen jälkeen venymästä voi lukea voiman suoraan newtoneina.

Kappaleen paino on Maan ja kappaleen välisen vuorovaikutuksen voimakkuuden mitta. Se on voima, ja sen yksikkö on newton. Massa on aivan eri asia: se kertoo, kuinka paljon ainetta kappaleessa on, ja sen yksikkö on kilogramma. Massa on sama kaikkialla, mutta paino riippuu siitä, missä kappale on. Kuu on paljon pienempi taivaankappale kuin Maa, ja Kuun ja astronautin välinen vuorovaikutus on heikompi kuin Maan ja astronautin, joten astronautti painaa Kuussa vähemmän.

```pysahdy
Astronautin massa on Maassa $80\,\text{kg}$. Mikä on hänen massansa Kuussa, ja mitä hänen painolleen tapahtuu?
---
Massa on sama $80\,\text{kg}$, koska massa kertoo aineen määrän. Paino pienenee, koska Kuun ja astronautin välinen vuorovaikutus on heikompi.
```

<figure class="unit-photo"><img src="pics/fy3/iss-cupola.webp" alt="Astronautti leijuu ilmassa avaruusaseman ikkunakupolissa. Ikkunoista näkyy Maa ja pilviä."><figcaption>Astronautti Jessica Watkins leijuu kansainvälisen avaruusaseman Cupola-ikkunan edessä vuonna 2022. Maa vetää häntä puoleensa myös siellä, mutta asema ja astronautti putoavat yhdessä Maan ympäri.</figcaption></figure>

## Kaava: Paino
Kaksi samanlaista kappaletta venyttää voimamittarin jousta kaksi kertaa niin paljon kuin yksi, joten paino on suoraan verrannollinen massaan:
```kaavat
kappaleeseen vaikuttava painovoima Maan pinnalla :: G = m g
```
missä $G$ on paino (N), $m$ massa (kg) ja $g$ putoamiskiihtyvyys (m/s²), Maan pinnalla $9{,}81\,\text{m/s}^2$. Kun massa on kilogrammoina ja $g$ yksikössä m/s², paino tulee newtoneina, sillä $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$ (tämä perustellaan FY4:ssä). Yhden kilogramman massan paino Maassa on siis $9{,}81\,\text{N}$. Muualla $g$ on erilainen. Taulukon arvot koskevat taivaankappaleen pintaa (Jupiterissa pilvien yläpinnan tasoa):

| Taivaankappale | $g$ pinnalla (m/s²) |
| --- | --- |
| Kuu | 1,62 |
| Mars | 3,71 |
| Maa | 9,81 |
| Jupiter | 24,8 |

Kuun $g$ on noin Maan arvon kuudesosa ($1{,}62 : 9{,}81 \approx 0{,}17 \approx 1 : 6$), joten sama massa painaa Kuussa noin kuudesosan siitä, mitä Maassa. Tämä vastaa alun kysymykseen astronautista.

Kuvaajassa paino on piirretty massan funktiona. Jokaisella taivaankappaleella paino on suoraan verrannollinen massaan, joten kuvaaja on origon kautta kulkeva suora. Mitä suurempi $g$, sitä jyrkempi suora: samalla massalla paino on Jupiterissa suurin ja Kuussa pienin.

```pysahdy
Miksi Jupiterin suora on jyrkempi kuin Kuun suora?
---
Jupiterissa $g$ on suurempi, joten sama massa painaa siellä enemmän. Siksi paino kasvaa massan mukana nopeammin.
```

<svg data-fig="weight-mass" viewBox="0 0 600 336" role="img" aria-label="Kuvaaja mittakaavassa: paino G newtoneina massan m funktiona, kun m on 0–100 kg. Neljä origon kautta kulkevaa suoraa, jyrkimmästä loivimpaan: Jupiter (suora jatkuu kuvan yläreunan yli), Maa (100 kg painaa 981 N), Mars (371 N) ja Kuu (162 N)." style="max-width:100%;font-size:24px">
  <line x1="185" y1="300" x2="185" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270" y1="300" x2="270" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="355" y1="300" x2="355" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="440" y1="300" x2="440" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="245.5" x2="440" y2="245.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="191" x2="440" y2="191" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="136.5" x2="440" y2="136.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="82" x2="440" y2="82" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="300" x2="454" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M466,300 L453,306 L453,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="301" x2="100" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,34 L106,47 L94,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="185" y1="300" x2="185" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="168.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$25$</div></foreignObject>
  <line x1="270" y1="300" x2="270" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="253.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="355" y1="300" x2="355" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="338.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$75$</div></foreignObject>
  <line x1="440" y1="300" x2="440" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="417.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="93" y1="245.5" x2="100" y2="245.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="231" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <line x1="93" y1="191" x2="100" y2="191" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="176.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$500$</div></foreignObject>
  <line x1="93" y1="136.5" x2="100" y2="136.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="122" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$750$</div></foreignObject>
  <line x1="93" y1="82" x2="100" y2="82" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="30" y="67.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1000$</div></foreignObject>
  <foreignObject x="70" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="472" y="285.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m\ (\text{kg})$</div></foreignObject>
  <foreignObject x="90" y="3.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$G\ (\text{N})$</div></foreignObject>
  <polyline points="100,300 251,60" fill="none" stroke="#a97a35" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="261" y="47.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#a97a35">$\text{Jupiter}$</div></foreignObject>
  <polyline points="100,300 440,86" fill="none" stroke="#2f74b5" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="452" y="71.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2f74b5">$\text{Maa}$</div></foreignObject>
  <polyline points="100,300 440,219" fill="none" stroke="#b8622d" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="452" y="204.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#b8622d">$\text{Mars}$</div></foreignObject>
  <polyline points="100,300 440,264.5" fill="none" stroke="#6c757d" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="452" y="243.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6c757d">$\text{Kuu}$</div></foreignObject>
</svg>

## Esimerkki
Tutkimusrobotin massa on $1{,}20 \cdot 10^2\,\text{kg}$. Mikä on sen paino Maassa ja Marsissa?

<!-- vaihe -->

**Tunnetut ja kysytty.** Massa on $m = 1{,}20 \cdot 10^2\,\text{kg}$, ja taulukosta $g_\text{Maa} = 9{,}81\,\text{m/s}^2$ ja $g_\text{Mars} = 3{,}71\,\text{m/s}^2$.

Kysytään painoja $G_\text{Maa}$ ja $G_\text{Mars}$.

<!-- vaihe -->

**Periaate.** Paino on vuorovaikutuksen voimakkuuden mitta: se on suoraan verrannollinen massaan, ja kerroin on sen taivaankappaleen $g$, jonka pinnalla robotti on. Robotin massa on sama kummassakin paikassa, joten vain $g$ vaihtuu.

<!-- vaihe -->

**Kaava ratkaistuna.** Kysytty paino on jo yksin kaavan vasemmalla puolella, joten kaavaa ei tarvitse muokata. Sama massa kerrotaan kummankin paikan putoamiskiihtyvyydellä:
```latex
\begin{aligned}
G_\text{Maa} &= m g_\text{Maa} \\
G_\text{Mars} &= m g_\text{Mars}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Massa on jo kilogrammoina ja $g$ yksikössä m/s², joten muunnoksia ei tarvita: $1\,\text{kg} \cdot 1\,\text{m/s}^2 = 1\,\text{N}$, ja tulos tulee suoraan newtoneina.

<!-- vaihe -->

**Sijoitus.** Arvot sijoitetaan yksiköineen kumpaankin kaavaan:
```latex
\begin{aligned}
&G_\text{Maa} = m g_\text{Maa} \\
&= 1{,}20 \cdot 10^2\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \\
&= 1177{,}2\,\text{N} \\[6pt]
&G_\text{Mars} = m g_\text{Mars} \\
&= 1{,}20 \cdot 10^2\,\text{kg} \cdot 3{,}71\,\text{m/s}^2 \\
&= 445{,}2\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kolmen merkitsevän numeron tarkkuudella robotin paino on Maassa noin $1{,}18\,\text{kN}$ ja Marsissa noin $445\,\text{N}$. Tulokset ilmoitetaan kolmella merkitsevällä numerolla, koska massa ja putoamiskiihtyvyyden arvot on annettu tällä tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Yhden kilogramman massan paino Maassa on noin $10\,\text{N}$, joten $120\,\text{kg}$:n massan paino on noin $1200\,\text{N}$. Marsin $g$ on vähän yli kolmasosa Maan arvosta ($3{,}71 : 9{,}81 \approx 0{,}38$), ja $445\,\text{N}$ on vähän yli kolmasosa $1{,}18\,\text{kN}$:sta. Marsissa paino on pienempi, koska Marsin ja robotin välinen vuorovaikutus on heikompi kuin Maan ja robotin. Massa on molemmissa sama.

## Yleinen virhekäsitys
Arkikielessä sanotaan ”painan 70 kiloa”, mutta kilogramma on massan yksikkö, ei painon. Fysiikassa massa on $70\,\text{kg}$ ja paino Maassa noin $690\,\text{N}$. Toinen virhe on ajatella, että kappaleen massa muuttuu Kuussa. Massa pysyy samana, ja vain paino pienenee. Huomaa myös, että voimamittari mittaa voimaa, ei massaa: sen lukema muuttuu, kun sama kappale viedään toiseen paikkaan. Kylpyhuonevaaka näyttää silti kilogrammoja, koska se mittaa voimaa ja sen asteikko on tehty Maassa jakamalla voima arvolla $9{,}81\,\text{m/s}^2$. Kuussa tällainen vaaka näyttäisi vain noin kuudesosan massasta.

## Tiivistelmä
- Voima kertoo vuorovaikutuksen voimakkuuden, ja sen yksikkö on newton (N). Voimamittarin jousen venymä on suoraan verrannollinen voimaan.
- Paino on voima: $G = m g$. Massa kertoo, kuinka paljon ainetta kappaleessa on, ja se on sama kaikkialla.
- $g = 9{,}81\,\text{m/s}^2$ Maan pinnalla, joten yhden kilogramman massan paino Maassa on $9{,}81\,\text{N}$. Kuussa $g = 1{,}62\,\text{m/s}^2$ ja Marsissa $3{,}71\,\text{m/s}^2$.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: sama reppu riippuu jousivaa&#x27;assa Maassa ja Kuussa. Maassa jousi venyy pitkäksi, Kuussa vain kuudesosan siitä, koska Kuu vetää reppua kuusi kertaa heikommin. Venymät on piirretty mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-1-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
