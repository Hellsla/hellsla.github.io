# Voima vuorovaikutuksen mittana ja paino G = mg

> **Miksi** astronautti painaa Kuussa vain kuudesosan siitä, mitä hän painaa Maassa, vaikka hänestä ei ole kadonnut mitään?

## Ydinajatus
Kun kaksi kappaletta vaikuttaa toisiinsa, ne ovat vuorovaikutuksessa. Voima kertoo, kuinka voimakas vuorovaikutus on. Mitä suurempi voima, sitä voimakkaampi vuorovaikutus. Voiman yksikkö on newton (N), ja noin 1 N on sadan gramman omenan paino Maassa.

Voiman voi mitata voimamittarilla. Siinä on jousi, joka venyy sitä enemmän, mitä suurempi voima siihen vaikuttaa. Jousen venymä on suoraan verrannollinen voimaan, joten kuvaaja (voima, venymä) on suora, kuten FY1:n lineaarisessa mallissa. Kun mittarin asteikko on kalibroitu, venymästä voi lukea voiman suoraan newtoneina.

Kappaleen paino on Maan ja kappaleen välisen vuorovaikutuksen voimakkuuden mitta. Se on voima, ja sen yksikkö on newton. Massa on aivan eri asia: se kertoo, kuinka paljon ainetta kappaleessa on, ja sen yksikkö on kilogramma. Massa on sama kaikkialla, mutta paino riippuu siitä, missä kappale on. Kuun ja astronautin välinen vuorovaikutus on heikompi kuin Maan ja astronautin, joten astronautti painaa Kuussa vähemmän. Hänen massansa on silti sama.

## Kaava
Paino on suoraan verrannollinen massaan:
```latex
G = m g
```
missä G on paino (N), m massa (kg) ja g painovoiman voimakkuus massayksikköä kohti (N/kg). Maan pinnalla g = 9,81 N/kg, sama luku kuin FY1:ssä mittaamasi putoamiskiihtyvyys 9,81 m/s². Muualla g on erilainen:

| Taivaankappale | g (N/kg) |
| --- | --- |
| Kuu | 1,62 |
| Mars | 3,71 |
| Maa | 9,81 |
| Jupiter | 24,8 |

Tässä oppitunnissa paino ymmärretään vuorovaikutuksen voimakkuuden mittana. Voimaa tarkastellaan suureena, jolla on vain suuruus, ja kuvissa nuoli näyttää, mihin voima osoittaa.

## Esimerkki
Tutkimusrobotin massa on 120 kg. Mikä on sen paino Maassa ja Marsissa?

<svg viewBox="0 0 600 300" role="img" aria-label="Voimamittari: jousi venyy, kun siihen ripustetaan kappale; paino G osoittaa alas" style="max-width:100%;font-family:system-ui,sans-serif;font-size:20px">
  <rect x="150" y="20" width="100" height="14" fill="currentColor"/>
  <polyline points="200,34 200,52 184,60 216,76 184,92 216,108 184,124 216,140 200,148 200,166" fill="none" stroke="currentColor" stroke-width="3"/>
  <rect x="160" y="166" width="80" height="80" rx="6" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-width="3"/>
  <text x="200" y="215" text-anchor="middle" fill="currentColor">m</text>
  <line x1="280" y1="170" x2="280" y2="258" stroke="currentColor" stroke-width="4"/>
  <polygon points="280,272 268,250 292,250" fill="currentColor"/>
  <text x="302" y="228" fill="currentColor">G = m g</text>
  <text x="302" y="70" fill="currentColor">jousi venyy</text>
  <text x="302" y="96" fill="currentColor">voiman mukaan</text>
</svg>

Maassa: $G = m g = 120\ \text{kg} \cdot 9{,}81\ \text{N/kg} = 1177\ \text{N} \approx 1{,}2\ \text{kN}$.

Marsissa: $G = 120\ \text{kg} \cdot 3{,}71\ \text{N/kg} = 445\ \text{N}$.

Robotin massa on molemmissa paikoissa 120 kg. Vain paino muuttuu, koska Marsin ja robotin välinen vuorovaikutus on heikompi kuin Maan ja robotin.

## Yleinen virhekäsitys
Arkikielessä sanotaan "painan 70 kiloa", mutta kilogramma on massan yksikkö, ei painon. Fysiikassa massa on 70 kg ja paino Maassa noin 690 N. Toinen virhe on ajatella, että kappaleen massa muuttuu Kuussa. Massa pysyy samana, ja vain paino pienenee. Huomaa myös, että jousivaaka mittaa voimaa, ei massaa: sen lukema muuttuu, kun se viedään toiseen paikkaan.

## Tiivistelmä
- Voima kertoo vuorovaikutuksen voimakkuuden, ja sen yksikkö on newton (N). Voimamittarin jousen venymä on suoraan verrannollinen voimaan.
- Paino on voima: $G = m g$. Massa on aineen määrä, ja se on sama kaikkialla.
- Maassa $g = 9{,}81\ \text{N/kg}$, Kuussa $1{,}62\ \text{N/kg}$ ja Marsissa $3{,}71\ \text{N/kg}$.
- Sama kappale painaa eri paikoissa eri verran, mutta sen massa ei muutu.
