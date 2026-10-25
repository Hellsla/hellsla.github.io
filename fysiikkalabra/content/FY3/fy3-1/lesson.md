# Voima vuorovaikutuksen mittana ja paino G = mg

> **Miksi** astronautti painaa Kuussa vain kuudesosan siitä, mitä hän painaa Maassa, vaikka hänestä ei ole kadonnut mitään?

## Ydinajatus
Kun kaksi kappaletta vaikuttaa toisiinsa, ne ovat vuorovaikutuksessa. Esimerkiksi Maa vetää omenaa puoleensa. Voima kertoo, kuinka voimakas vuorovaikutus on: mitä suurempi voima, sitä voimakkaampi vuorovaikutus. Voiman yksikkö on newton (N), ja noin 1 N on sadan gramman omenan paino Maassa. Tässä vaiheessa kiinnostaa vain voiman suuruus, ja kuvissa nuoli näyttää, mihin suuntaan voima osoittaa.

Voiman voi mitata voimamittarilla. Siinä on jousi, joka venyy sitä enemmän, mitä suurempi voima siihen vaikuttaa.

Venymä on suoraan verrannollinen voimaan, kun jousta ei venytetä liikaa: kaksinkertainen voima venyttää jousta kaksinkertaisen matkan. Kuvaaja (voima, venymä) on siis suora, joka kulkee origon kautta, kuten FY1:n lineaarisessa mallissa silloin, kun vakiotermi on nolla. Jos 5,0 N venyttää jousta 2,0 cm, niin 10 N venyttää sitä 4,0 cm ja 2,5 N venyttää sitä 1,0 cm.

Asteikko kalibroidaan ripustamalla jouseen samanlaisia pieniä kappaleita, joiden paino on kunkin noin 1 N. Yksi kappale venyttää jousta tietyn matkan, ja kohta merkitään 1 N:ksi. Kaksi kappaletta venyttää jousta kaksinkertaisen matkan, ja kohta merkitään 2 N:ksi, ja niin edelleen. Sen jälkeen venymästä voi lukea voiman suoraan newtoneina.

Kappaleen paino on Maan ja kappaleen välisen vuorovaikutuksen voimakkuuden mitta. Se on voima, ja sen yksikkö on newton. Massa on aivan eri asia: se kertoo, kuinka paljon ainetta kappaleessa on, ja sen yksikkö on kilogramma. Massa on sama kaikkialla, mutta paino riippuu siitä, missä kappale on. Kuun ja astronautin välinen vuorovaikutus on heikompi kuin Maan ja astronautin, joten astronautti painaa Kuussa vähemmän.

## Kaava
Kaksi samanlaista kappaletta venyttää voimamittarin jousta kaksi kertaa niin paljon kuin yksi, joten paino on suoraan verrannollinen massaan:
```latex
G = m g
```
missä G on paino (N), m massa (kg) ja g painovoiman voimakkuus massayksikköä kohti (N/kg). Luku g kertoo, kuinka suuri on yhden kilogramman massan paino: Maan pinnalla g = 9,81 N/kg, joten 1 kg:n massan paino on 9,81 N. Luku 9,81 on sama kuin FY1:n putoamiskiihtyvyys 9,81 m/s². Tällä kurssilla g:lle käytetään yksikköä N/kg, ja syy lukujen yhtäsuuruuteen selviää FY4:ssä. Muualla g on erilainen. Taulukon arvot koskevat taivaankappaleen pintaa (Jupiterissa pilvien yläpinnan tasoa):

| Taivaankappale | g pinnalla (N/kg) |
| --- | --- |
| Kuu | 1,62 |
| Mars | 3,71 |
| Maa | 9,81 |
| Jupiter | 24,8 |

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

Maassa: $G = m g = 120\,\text{kg} \cdot 9{,}81\,\text{N/kg} \approx 1180\,\text{N}$ eli noin 1,18 kN.

Marsissa: $G = 120\,\text{kg} \cdot 3{,}71\,\text{N/kg} \approx 445\,\text{N}$.

Marsissa paino on pienempi, koska Marsin ja robotin välinen vuorovaikutus on heikompi kuin Maan ja robotin.

## Yleinen virhekäsitys
Arkikielessä sanotaan ”painan 70 kiloa”, mutta kilogramma on massan yksikkö, ei painon. Fysiikassa massa on 70 kg ja paino Maassa noin 690 N. Toinen virhe on ajatella, että kappaleen massa muuttuu Kuussa. Massa pysyy samana, ja vain paino pienenee. Huomaa myös, että voimamittari mittaa voimaa, ei massaa: sen lukema muuttuu, kun sama kappale viedään toiseen paikkaan. Kylpyhuonevaaka näyttää silti kilogrammoja, koska se mittaa voimaa ja sen asteikko on tehty Maassa jakamalla voima luvulla 9,81 N/kg. Kuussa tällainen vaaka näyttäisi vain noin kuudesosan massasta.

## Tiivistelmä
- Voima kertoo vuorovaikutuksen voimakkuuden, ja sen yksikkö on newton (N). Voimamittarin jousen venymä on suoraan verrannollinen voimaan.
- Paino on voima: $G = m g$. Massa on aineen määrä, ja se on sama kaikkialla.
- $g = 9{,}81\,\text{N/kg}$: yhden kilogramman massan paino Maassa. Kuussa $g = 1{,}62\,\text{N/kg}$ ja Marsissa $3{,}71\,\text{N/kg}$.
