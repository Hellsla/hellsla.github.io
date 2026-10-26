# Voima vuorovaikutuksen mittana ja paino G = mg

> **Miksi** astronautti painaa Kuussa vain kuudesosan siitä, mitä hän painaa Maassa, vaikka hänestä ei ole kadonnut mitään?

## Ydinajatus
Kun kaksi kappaletta vaikuttaa toisiinsa, ne ovat vuorovaikutuksessa. Esimerkiksi Maa vetää omenaa puoleensa. Voima kertoo, kuinka voimakas vuorovaikutus on: mitä suurempi voima, sitä voimakkaampi vuorovaikutus. Voiman yksikkö on newton (N), ja noin 1 N on sadan gramman omenan paino Maassa. Tässä vaiheessa kiinnostaa vain voiman suuruus, ja kuvissa nuoli näyttää, mihin suuntaan voima osoittaa.

Voiman voi mitata voimamittarilla. Siinä on jousi, joka venyy sitä enemmän, mitä suurempi voima siihen vaikuttaa.

<svg viewBox="0 0 600 300" role="img" aria-label="Voimamittari (periaatekuva, ei mittakaavassa): jousi venyy, kun siihen ripustetaan kappale; kappaleen paino G osoittaa alas" style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <rect x="150" y="20" width="100" height="14" fill="#6c757d"/>
  <polyline points="200,34 200,52 184,60 216,76 184,92 216,108 184,124 216,140 200,148 200,166" fill="none" stroke="#6c757d" stroke-width="3"/>
  <rect x="160" y="166" width="80" height="70" rx="6" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <text x="200" y="210" text-anchor="middle" fill="#1f2933">m</text>
  <line x1="200" y1="236" x2="200" y2="272" stroke="#e8590c" stroke-width="4"/>
  <polygon points="200,290 188,268 212,268" fill="#e8590c"/>
  <text x="224" y="284" fill="#1f2933">G = m g</text>
  <text x="290" y="72" fill="#1f2933">jousi venyy</text>
  <text x="290" y="102" fill="#1f2933">voiman mukaan</text>
</svg>

Venymä on suoraan verrannollinen voimaan, kun jousta ei venytetä liikaa: kaksinkertainen voima venyttää jousta kaksinkertaisen matkan. Kuvaaja (voima, venymä) on siis suora, joka kulkee origon kautta, kuten FY1:n suoraan verrannollisissa malleissa, esimerkiksi tasaisen liikkeen $s = v t$. Jos 5,0 N venyttää jousta 2,0 cm, niin 10 N venyttää sitä 4,0 cm ja 2,5 N venyttää sitä 1,0 cm.

<svg viewBox="0 0 600 300" role="img" aria-label="Kuvaaja mittakaavassa: jousen venymä x senttimetreinä voiman F funktiona. Pisteet 2,5 N ja 1,0 cm, 5,0 N ja 2,0 cm sekä 10 N ja 4,0 cm ovat samalla origon kautta kulkevalla suoralla." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <line x1="90" y1="250" x2="570" y2="250" stroke="#1f2933" stroke-width="3"/>
  <line x1="90" y1="250" x2="90" y2="36" stroke="#1f2933" stroke-width="3"/>
  <g stroke="#6b7480" stroke-width="2" stroke-dasharray="6 5">
    <line x1="190" y1="250" x2="190" y2="200"/><line x1="90" y1="200" x2="190" y2="200"/>
    <line x1="290" y1="250" x2="290" y2="150"/><line x1="90" y1="150" x2="290" y2="150"/>
    <line x1="490" y1="250" x2="490" y2="50"/><line x1="90" y1="50" x2="490" y2="50"/>
  </g>
  <line x1="90" y1="250" x2="530" y2="30" stroke="#1f2933" stroke-width="4"/>
  <circle cx="190" cy="200" r="8" fill="#1f2933"/>
  <circle cx="290" cy="150" r="8" fill="#1f2933"/>
  <circle cx="490" cy="50" r="8" fill="#1f2933"/>
  <text x="100" y="28" fill="#e8590c">x (cm)</text>
  <text x="80" y="58" text-anchor="end" fill="#e8590c">4,0</text>
  <text x="80" y="158" text-anchor="end" fill="#e8590c">2,0</text>
  <text x="80" y="208" text-anchor="end" fill="#1f2933">1,0</text>
  <text x="190" y="282" text-anchor="middle" fill="#1f2933">2,5</text>
  <text x="290" y="282" text-anchor="middle" fill="#1f2933">5,0</text>
  <text x="490" y="282" text-anchor="middle" fill="#1f2933">10</text>
  <text x="595" y="282" text-anchor="end" fill="#1f2933">F (N)</text>
  <text x="308" y="202" fill="#1f2933">suora origon</text>
  <text x="308" y="232" fill="#1f2933">kautta</text>
</svg>

Asteikko kalibroidaan ripustamalla jouseen samanlaisia pieniä kappaleita, joiden kunkin massa on noin 100 g eli paino noin 1 N:

- Yksi kappale venyttää jousta tietyn matkan, ja kohta merkitään 1 N:ksi.
- Kukin kappale vetää jousta yhtä voimakkaasti, joten kaksi kappaletta vetää sitä kaksinkertaisella voimalla ja venyttää sitä kaksinkertaisen matkan. Kohta merkitään 2 N:ksi, ja niin edelleen.
- Sen jälkeen venymästä voi lukea voiman suoraan newtoneina.

Kappaleen paino on Maan ja kappaleen välisen vuorovaikutuksen voimakkuuden mitta. Se on voima, ja sen yksikkö on newton. Massa on aivan eri asia: se kertoo, kuinka paljon ainetta kappaleessa on, ja sen yksikkö on kilogramma. Massa on sama kaikkialla, mutta paino riippuu siitä, missä kappale on. Kuu on paljon pienempi taivaankappale kuin Maa, ja Kuun ja astronautin välinen vuorovaikutus on heikompi kuin Maan ja astronautin, joten astronautti painaa Kuussa vähemmän.

## Kaava: Paino
Kaksi samanlaista kappaletta venyttää voimamittarin jousta kaksi kertaa niin paljon kuin yksi, joten paino on suoraan verrannollinen massaan:
```latex
G = m g
```
missä G on paino (N), m massa (kg) ja g putoamiskiihtyvyys (m/s²), Maan pinnalla 9,81 m/s². Kun massa on kilogrammoina ja g yksikössä m/s², paino tulee newtoneina, sillä 1 N = 1 kg·m/s² (tämä perustellaan FY4:ssä). Yhden kilogramman massan paino Maassa on siis 9,81 N. Muualla g on erilainen. Taulukon arvot koskevat taivaankappaleen pintaa (Jupiterissa pilvien yläpinnan tasoa):

| Taivaankappale | g pinnalla (m/s²) |
| --- | --- |
| Kuu | 1,62 |
| Mars | 3,71 |
| Maa | 9,81 |
| Jupiter | 24,8 |

Kuun g on noin Maan arvon kuudesosa (1,62/9,81 ≈ 0,17 ≈ 1/6), joten sama massa painaa Kuussa noin kuudesosan siitä, mitä Maassa. Tämä vastaa alun kysymykseen astronautista.

Kuvaajassa paino on piirretty massan funktiona. Jokaisella taivaankappaleella paino on suoraan verrannollinen massaan, joten kuvaaja on origon kautta kulkeva suora. Mitä suurempi g, sitä jyrkempi suora: samalla massalla paino on Jupiterissa suurin ja Kuussa pienin.

<svg viewBox="0 0 600 300" role="img" aria-label="Kuvaaja mittakaavassa: paino G newtoneina massan m funktiona, kun m on 0–100 kg. Neljä origon kautta kulkevaa suoraa: Jupiter jyrkin, sitten Maa (100 kg painaa 981 N), Mars (371 N) ja Kuu (162 N) loivin." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <line x1="90" y1="250" x2="570" y2="250" stroke="#1f2933" stroke-width="3"/>
  <line x1="90" y1="250" x2="90" y2="36" stroke="#1f2933" stroke-width="3"/>
  <g stroke="#c9c2b2" stroke-width="1.5">
    <line x1="90" y1="150" x2="490" y2="150"/><line x1="90" y1="50" x2="490" y2="50"/>
    <line x1="290" y1="250" x2="290" y2="50"/><line x1="490" y1="250" x2="490" y2="50"/>
  </g>
  <line x1="90" y1="250" x2="251.3" y2="50" stroke="#a97a35" stroke-width="4"/>
  <line x1="90" y1="250" x2="490" y2="53.8" stroke="#2f74b5" stroke-width="4"/>
  <line x1="90" y1="250" x2="490" y2="175.8" stroke="#b8622d" stroke-width="4"/>
  <line x1="90" y1="250" x2="490" y2="217.6" stroke="#6c757d" stroke-width="4"/>
  <text x="262" y="78" fill="#1f2933">Jupiter</text>
  <text x="500" y="62" fill="#1f2933">Maa</text>
  <text x="500" y="184" fill="#1f2933">Mars</text>
  <text x="500" y="226" fill="#1f2933">Kuu</text>
  <text x="100" y="28" fill="#1f2933">G (N)</text>
  <text x="80" y="58" text-anchor="end" fill="#1f2933">1000</text>
  <text x="80" y="158" text-anchor="end" fill="#1f2933">500</text>
  <text x="80" y="258" text-anchor="end" fill="#1f2933">0</text>
  <text x="290" y="282" text-anchor="middle" fill="#1f2933">50</text>
  <text x="490" y="282" text-anchor="middle" fill="#1f2933">100</text>
  <text x="595" y="282" text-anchor="end" fill="#1f2933">m (kg)</text>
</svg>

## Esimerkki
Tutkimusrobotin massa on 120 kg. Mikä on sen paino Maassa ja Marsissa?

<!-- vaihe -->

**Tunnetut ja kysytty.** Massa on $m = 120\,\text{kg}$, ja taulukosta $g_\text{Maa} = 9{,}81\,\text{m/s}^2$ ja $g_\text{Mars} = 3{,}71\,\text{m/s}^2$. Kysytään painoja $G_\text{Maa}$ ja $G_\text{Mars}$.

<!-- vaihe -->

**Kaava ratkaistuna.** Kysytty paino on jo yksin kaavan vasemmalla puolella, joten kaavaa ei tarvitse muokata. Sama massa kerrotaan kummankin paikan putoamiskiihtyvyydellä:
```latex
\begin{aligned}
G_\text{Maa} &= m g_\text{Maa} \\
G_\text{Mars} &= m g_\text{Mars}
\end{aligned}
```

<!-- vaihe -->

**Sijoitus Maassa.** Arvot sijoitetaan yksiköineen, ja kg · m/s² on newton:
```latex
\begin{aligned}
&G_\text{Maa} = m g_\text{Maa} \\
&= 120\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \\
&= 1177{,}2\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Sijoitus Marsissa.** Massa on sama, vain g vaihtuu:
```latex
\begin{aligned}
&G_\text{Mars} = m g_\text{Mars} \\
&= 120\,\text{kg} \cdot 3{,}71\,\text{m/s}^2 \\
&= 445{,}2\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kolmen merkitsevän numeron tarkkuudella robotin paino Maassa on $G_\text{Maa} \approx 1180\,\text{N}$ eli noin 1,18 kN ja Marsissa $G_\text{Mars} \approx 445\,\text{N}$.

<!-- vaihe -->

**Järkevyys.** Yhden kilogramman massan paino Maassa on noin 10 N, joten 120 kg:n massan paino on noin 1200 N. Marsin g on vähän yli kolmasosa Maan arvosta (3,71/9,81 ≈ 0,38), ja 445 N on vähän yli kolmasosa 1180 N:sta. Marsissa paino on pienempi, koska Marsin ja robotin välinen vuorovaikutus on heikompi kuin Maan ja robotin. Massa on molemmissa sama.

## Yleinen virhekäsitys
Arkikielessä sanotaan ”painan 70 kiloa”, mutta kilogramma on massan yksikkö, ei painon. Fysiikassa massa on 70 kg ja paino Maassa noin 690 N. Toinen virhe on ajatella, että kappaleen massa muuttuu Kuussa. Massa pysyy samana, ja vain paino pienenee. Huomaa myös, että voimamittari mittaa voimaa, ei massaa: sen lukema muuttuu, kun sama kappale viedään toiseen paikkaan. Kylpyhuonevaaka näyttää silti kilogrammoja, koska se mittaa voimaa ja sen asteikko on tehty Maassa jakamalla voima arvolla 9,81 m/s². Kuussa tällainen vaaka näyttäisi vain noin kuudesosan massasta.

## Tiivistelmä
- Voima kertoo vuorovaikutuksen voimakkuuden, ja sen yksikkö on newton (N). Voimamittarin jousen venymä on suoraan verrannollinen voimaan.
- Paino on voima: $G = m g$. Massa kertoo, kuinka paljon ainetta kappaleessa on, ja se on sama kaikkialla.
- $g = 9{,}81\,\text{m/s}^2$ Maan pinnalla, joten yhden kilogramman massan paino Maassa on 9,81 N. Kuussa $g = 1{,}62\,\text{m/s}^2$ ja Marsissa $3{,}71\,\text{m/s}^2$.
