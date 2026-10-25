# Termodynaaminen systeemi, tilanmuuttujat ja lämpötila

> **Miksi** pyörän rengas tuntuu kovemmalta kuumana kesäpäivänä kuin pakkasella, vaikka renkaaseen ei pumpata lisää ilmaa?

## Ydinajatus
Kun tutkitaan ilmiötä, tarkasteltava osa maailmasta rajataan erilleen muusta. Rajattu osa on termodynaaminen systeemi ja kaikki sen ulkopuolella oleva on ympäristö. Pyörän renkaan ilma on esimerkki systeemistä. Jos systeemistä ei pääse ainetta ulos eikä sisään, systeemi on suljettu. Systeemin tilaa kuvataan tilanmuuttujilla, joita ovat lämpötila, paine ja tilavuus sekä aineen määrä. Paine on voima pinta-alaa kohti; sen yksikkö on pascal (Pa), ja 1 kPa = 1000 Pa. Paineeseen paneudutaan tarkemmin myöhemmin. Kun kaasusysteemissä muutetaan yhtä tilanmuuttujaa, vähintään yksi muista muuttuu myös.

Miksi näin käy, selittää aineen mikromalli. Kaasu koostuu hiukkasista, jotka liikkuvat jatkuvasti joka suuntaan ja törmäilevät toisiinsa ja astian seinämiin. Lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta: mitä kuumempaa kaasu on, sitä nopeammin hiukkaset keskimäärin liikkuvat. Paine syntyy, kun hiukkaset törmäävät seinämään ja jokainen törmäys työntää seinää hieman. Kun tilavuus pienenee, hiukkasilla on vähemmän tilaa ja ne osuvat seinään useammin, mutta yksittäinen törmäys ei muutu kovemmaksi. Kun lämpötila nousee mutta tilavuus pysyy samana, hiukkaset osuvat seinään sekä useammin että kovempaa, joten paine kasvaa. Tästä syystä rengas tuntuu kesällä kovemmalta.

Lämpötilaa mitataan celsiusasteikolla, jossa 0 °C on veden jäätymispiste ja 100 °C veden kiehumispiste normaalipaineessa, ja kelvinasteikolla. Kelvinasteikon nollapiste on absoluuttinen nollapiste, alin mahdollinen lämpötila. Siinä hiukkasten keskimääräinen liike-energia on pienimmillään, eikä kylmempää voi olla. Celsiusasteen ja kelvinin suuruus on sama, joten lämpötilaero on sama kelvineinä ja celsiusasteina. Kun tilavuus ja kaasun määrä pysyvät samoina, kaasun paine on suoraan verrannollinen kelvinlämpötilaan. Myös hiukkasten keskimääräinen liike-energia on suoraan verrannollinen kelvinlämpötilaan, joten lämpötilojen suhteita verrataan kelvineinä.

## Kaava
Celsiuslämpötilan θ muunnos kelvineiksi on:
```latex
T = \theta + 273{,}15
```
missä T on lämpötila kelvineinä (K) ja θ lämpötila celsiusasteina (°C). Käytännössä riittää usein luku 273. Kelvineissä ei käytetä sanaa aste: sanotaan ”300 kelviniä”, ei ”300 kelvinastetta”.

Absoluuttinen nollapiste on siis 0 K = −273,15 °C. Kelvinlämpötila ei voi olla negatiivinen, mutta celsiuslämpötila voi.

## Esimerkki
Suljetussa jäykässä astiassa on kaasua, joten sen tilavuus ja aineen määrä pysyvät samoina. Kaasun paine mitataan eri lämpötiloissa:

| θ (°C) | 0 | 20 | 40 | 60 | 80 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| p (kPa) | 100 | 107 | 115 | 122 | 129 | 137 |

Pisteet asettuvat suoralle:

<svg viewBox="0 0 600 300" role="img" aria-label="Kaasun paine lämpötilan funktiona suljetussa astiassa: mittapisteet lämpötila-alueella 0–100 °C asettuvat suoralle, ja ekstrapoloitu suora kohtaa nollapaineen lämpötilassa noin −270 °C" style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <line x1="70" y1="250" x2="590" y2="250" stroke="currentColor" stroke-width="3"/>
  <line x1="70" y1="250" x2="70" y2="30" stroke="currentColor" stroke-width="3"/>
  <line x1="107" y1="250" x2="445" y2="100" stroke="currentColor" stroke-width="3" stroke-dasharray="9 7"/>
  <line x1="445" y1="100" x2="570" y2="44" stroke="currentColor" stroke-width="4"/>
  <circle cx="445" cy="100" r="5" fill="currentColor"/><circle cx="470" cy="90" r="5" fill="currentColor"/><circle cx="495" cy="78" r="5" fill="currentColor"/><circle cx="520" cy="67" r="5" fill="currentColor"/><circle cx="545" cy="56" r="5" fill="currentColor"/><circle cx="570" cy="44" r="5" fill="currentColor"/>
  <circle cx="107" cy="250" r="6" fill="none" stroke="currentColor" stroke-width="3"/>
  <text x="107" y="282" text-anchor="middle" fill="currentColor">−270</text>
  <text x="445" y="282" text-anchor="middle" fill="currentColor">0</text>
  <text x="570" y="282" text-anchor="middle" fill="currentColor">100</text>
  <text x="590" y="228" text-anchor="end" fill="currentColor">θ (°C)</text>
  <text x="80" y="28" fill="currentColor">p (kPa)</text>
  <text x="62" y="106" text-anchor="end" fill="currentColor">100</text>
  <text x="62" y="50" text-anchor="end" fill="currentColor">137</text>
  <text x="62" y="256" text-anchor="end" fill="currentColor">0</text>
  <text x="80" y="212" fill="currentColor">p = 0</text>
</svg>

Pystyakseli on piirretty kuvan vasempaan reunaan, noin −300 °C:n kohdalle, eikä kohtaan θ = 0. Yhtenäinen suora on mittausalue ja katkoviiva ekstrapolointi.

Suoran kulmakerroin on
```latex
k = \frac{(137 - 100)\,\text{kPa}}{(100 - 0)\,\text{°C}} = 0{,}37\,\text{kPa/°C}
```

Jatketaan suoraa vasemmalle mittausalueen ulkopuolelle eli ekstrapoloidaan: sovitettua suoraa jatketaan mitattujen pisteiden yli, vaikka siellä ei ole mittauksia. Suoran yhtälö on
```latex
p = p_0 + k\theta
```
missä p₀ on paine lämpötilassa 0 °C. Nollapaine saavutetaan, kun 0 = p₀ + kθ, eli lämpötilassa θ = −p₀/k. Tässä p₀ = 100 kPa, joten
```latex
\theta = -\frac{p_0}{k} = -\frac{100\,\text{kPa}}{0{,}37\,\text{kPa/°C}} \approx -270\,\text{°C}
```

Tulos on lähellä absoluuttista nollapistettä −273 °C. Mikromallin mukaan tässä lämpötilassa hiukkasten liike olisi niin vähäistä, ettei paine enää syntyisi. Näin absoluuttinen nollapiste voidaan määrittää kokeellisesti. Todelliset kaasut nesteytyvät jo ennen tätä lämpötilaa, joten suoran jatke on vain malli ja kuvaa raja-arvoa.

## Yleinen virhekäsitys
Moni ajattelee, että lämpötila kaksinkertaistuu, kun se nousee 10 °C:sta 20 °C:een. Fysikaalisesti oikea vertailu tehdään kelvineinä: 283 K:sta 293 K:iin. Lämpötilojen suhde on 293/283 ≈ 1,035, eli nousu on noin 3,5 %. Siksi hiukkasten keskimääräinen liike-energia ei kaksinkertaistu. Toinen virhe on pitää 0 °C:ta alimpana mahdollisena lämpötilana. Se on vain veden jäätymispiste, ja alin mahdollinen lämpötila on 0 K.

## Tiivistelmä
- Termodynaaminen systeemi on rajattu osa maailmaa. Sen tilaa kuvaavat tilanmuuttujat: lämpötila, paine, tilavuus ja aineen määrä.
- Kaasusysteemissä lämpötila, paine ja tilavuus riippuvat toisistaan: jos yhtä muutetaan, vähintään yksi muista muuttuu myös.
- Mikromalli: lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta, ja paine syntyy hiukkasten törmäyksistä seinämään.
- Muunnos on $T = \theta + 273{,}15$. Absoluuttinen nollapiste on 0 K = −273,15 °C.
