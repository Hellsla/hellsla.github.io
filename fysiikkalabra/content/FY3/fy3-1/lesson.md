# Voima vuorovaikutuksen mittana ja paino G = mg

> **Miksi** astronautti painaa Kuussa vain kuudesosan siitä, mitä hän painaa Maassa, vaikka hänestä ei ole kadonnut mitään?

## Ydinajatus
Kun kaksi kappaletta vaikuttaa toisiinsa, ne ovat vuorovaikutuksessa. Esimerkiksi Maa vetää omenaa puoleensa. Voima kertoo, kuinka voimakas vuorovaikutus on: mitä suurempi voima, sitä voimakkaampi vuorovaikutus. Voiman yksikkö on newton (N), ja noin 1 N on sadan gramman omenan paino Maassa. Tässä vaiheessa kiinnostaa vain voiman suuruus, ja kuvissa nuoli näyttää, mihin suuntaan voima osoittaa.

Voiman voi mitata voimamittarilla. Siinä on jousi, joka venyy sitä enemmän, mitä suurempi voima siihen vaikuttaa. Venymä on suoraan verrannollinen voimaan, kun jousta ei venytetä liikaa: kaksinkertainen voima venyttää jousta kaksinkertaisen matkan. Kuvaaja (voima, venymä) on siis suora, joka kulkee origon kautta, kuten FY1:n suoraan verrannollisissa malleissa, esimerkiksi tasaisen liikkeen $s = v t$. Jos 5,0 N venyttää jousta 2,0 cm, niin 10 N venyttää sitä 4,0 cm ja 2,5 N venyttää sitä 1,0 cm. Asteikko kalibroidaan ripustamalla jouseen samanlaisia pieniä kappaleita, joiden kunkin massa on noin 100 g eli paino noin 1 N. Yksi kappale venyttää jousta tietyn matkan, ja kohta merkitään 1 N:ksi. Kukin kappale vetää jousta yhtä voimakkaasti, joten kaksi kappaletta vetää sitä kaksinkertaisella voimalla ja venyttää sitä kaksinkertaisen matkan; kohta merkitään 2 N:ksi, ja niin edelleen. Sen jälkeen venymästä voi lukea voiman suoraan newtoneina.

<svg viewBox="0 0 600 300" role="img" aria-label="Voimamittari: jousi venyy, kun siihen ripustetaan kappale; kappaleen paino G osoittaa alas" style="max-width:100%;font-family:system-ui,sans-serif;font-size:20px">
  <rect x="150" y="20" width="100" height="14" fill="currentColor"/>
  <polyline points="200,34 200,52 184,60 216,76 184,92 216,108 184,124 216,140 200,148 200,166" fill="none" stroke="currentColor" stroke-width="3"/>
  <rect x="160" y="166" width="80" height="70" rx="6" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-width="3"/>
  <text x="200" y="208" text-anchor="middle" fill="currentColor">m</text>
  <line x1="200" y1="236" x2="200" y2="272" stroke="currentColor" stroke-width="4"/>
  <polygon points="200,290 188,268 212,268" fill="currentColor"/>
  <text x="222" y="282" fill="currentColor">G = m g</text>
  <text x="302" y="70" fill="currentColor">jousi venyy</text>
  <text x="302" y="96" fill="currentColor">voiman mukaan</text>
</svg>

Kappaleen paino on Maan ja kappaleen välisen vuorovaikutuksen voimakkuuden mitta. Se on voima, ja sen yksikkö on newton. Massa on aivan eri asia: se kertoo, kuinka paljon ainetta kappaleessa on, ja sen yksikkö on kilogramma. Massa on sama kaikkialla, mutta paino riippuu siitä, missä kappale on. Kuu on paljon pienempi ja kevyempi kuin Maa, joten Kuun ja astronautin välinen vuorovaikutus on heikompi kuin Maan ja astronautin, ja astronautti painaa Kuussa vähemmän.

## Kaava
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

Kuun g on noin kuudesosa Maan arvosta (1,62/9,81 ≈ 0,17), joten sama massa painaa Kuussa noin kuudesosan siitä, mitä Maassa. Tämä vastaa alun kysymykseen astronautista.

## Esimerkki
Tutkimusrobotin massa on 120 kg. Mikä on sen paino Maassa ja Marsissa?

Maassa: $G = m g = 120\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \approx 1180\,\text{N}$ eli noin 1,18 kN.

Marsissa: $G = 120\,\text{kg} \cdot 3{,}71\,\text{m/s}^2 \approx 445\,\text{N}$.

Marsissa paino on pienempi, koska Marsin ja robotin välinen vuorovaikutus on heikompi kuin Maan ja robotin.

## Yleinen virhekäsitys
Arkikielessä sanotaan ”painan 70 kiloa”, mutta kilogramma on massan yksikkö, ei painon. Fysiikassa massa on 70 kg ja paino Maassa noin 690 N. Toinen virhe on ajatella, että kappaleen massa muuttuu Kuussa. Massa pysyy samana, ja vain paino pienenee. Huomaa myös, että voimamittari mittaa voimaa, ei massaa: sen lukema muuttuu, kun sama kappale viedään toiseen paikkaan. Kylpyhuonevaaka näyttää silti kilogrammoja, koska se mittaa voimaa ja sen asteikko on tehty Maassa jakamalla voima arvolla 9,81 m/s². Kuussa tällainen vaaka näyttäisi vain noin kuudesosan massasta.

## Tiivistelmä
- Voima kertoo vuorovaikutuksen voimakkuuden, ja sen yksikkö on newton (N). Voimamittarin jousen venymä on suoraan verrannollinen voimaan.
- Paino on voima: $G = m g$. Massa kertoo, kuinka paljon ainetta kappaleessa on, ja se on sama kaikkialla.
- $g = 9{,}81\,\text{m/s}^2$ Maan pinnalla, joten yhden kilogramman massan paino Maassa on noin 9,81 N. Kuussa $g = 1{,}62\,\text{m/s}^2$ ja Marsissa $3{,}71\,\text{m/s}^2$.
