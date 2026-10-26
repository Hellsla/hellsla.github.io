# Termodynaaminen systeemi, tilanmuuttujat ja lämpötila

> **Miksi** pyörän rengas tuntuu kovemmalta kuumana kesäpäivänä kuin pakkasella, vaikka renkaaseen ei pumpata lisää ilmaa?

## Ydinajatus
Kun tutkitaan ilmiötä, tarkasteltava osa maailmasta rajataan erilleen muusta. Rajattu osa on termodynaaminen systeemi ja kaikki sen ulkopuolella oleva on ympäristö. Pyörän renkaan ilma on esimerkki systeemistä. Jos systeemistä ei pääse ainetta ulos eikä sisään, systeemi on suljettu. Systeemin tilaa kuvataan tilanmuuttujilla, joita ovat lämpötila, paine ja tilavuus sekä aineen määrä. Paine on voima pinta-alaa kohti; sen yksikkö on pascal (Pa), ja 1 kPa = 1000 Pa. Paineeseen paneudutaan tarkemmin myöhemmin. Kun kaasusysteemissä muutetaan yhtä tilanmuuttujaa, vähintään yksi muista muuttuu myös.

Miksi näin käy, selittää aineen mikromalli. Kaasu koostuu hiukkasista, jotka liikkuvat jatkuvasti joka suuntaan ja törmäilevät toisiinsa ja astian seinämiin. Lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta: mitä kuumempaa kaasu on, sitä nopeammin hiukkaset keskimäärin liikkuvat. Paine syntyy, kun hiukkaset törmäävät seinämään ja jokainen törmäys työntää seinää hieman. Kun tilavuus pienenee, hiukkasilla on vähemmän tilaa ja ne osuvat seinään useammin, joten paine kasvaa, mutta yksittäinen törmäys ei muutu kovemmaksi. Kun lämpötila nousee mutta tilavuus pysyy samana, hiukkaset osuvat seinään sekä useammin että kovempaa, joten paine kasvaa. Tästä syystä rengas tuntuu kesällä kovemmalta.

<svg viewBox="0 0 600 300" role="img" aria-label="Kaaviokuva kaasun mikromallista: kaksi samankokoista suljettua astiaa, joissa on yhtä monta hiukkasta. Kylmässä kaasussa nopeutta kuvaavat nuolet ovat lyhyitä, kuumassa pitkiä, ja kuuman kaasun paine p2 on suurempi kuin kylmän kaasun paine p1." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <defs><marker id="fy33-nuoli" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#1f2933"/></marker></defs>
  <text x="155" y="40" text-anchor="middle" fill="#1f2933">kylmä kaasu</text>
  <text x="445" y="40" text-anchor="middle" fill="#1f2933">kuuma kaasu</text>
  <rect x="40" y="60" width="230" height="180" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="4"/>
  <rect x="330" y="60" width="230" height="180" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="4"/>
  <circle cx="95" cy="105" r="7" fill="#1971c2"/><line x1="95" y1="105" x2="111" y2="121" stroke="#1f2933" stroke-width="3" marker-end="url(#fy33-nuoli)"/>
  <circle cx="210" cy="100" r="7" fill="#1971c2"/><line x1="210" y1="100" x2="191" y2="111" stroke="#1f2933" stroke-width="3" marker-end="url(#fy33-nuoli)"/>
  <circle cx="155" cy="155" r="7" fill="#1971c2"/><line x1="155" y1="155" x2="177" y2="155" stroke="#1f2933" stroke-width="3" marker-end="url(#fy33-nuoli)"/>
  <circle cx="85" cy="190" r="7" fill="#1971c2"/><line x1="85" y1="190" x2="101" y2="174" stroke="#1f2933" stroke-width="3" marker-end="url(#fy33-nuoli)"/>
  <circle cx="215" cy="200" r="7" fill="#1971c2"/><line x1="215" y1="200" x2="194" y2="192" stroke="#1f2933" stroke-width="3" marker-end="url(#fy33-nuoli)"/>
  <circle cx="140" cy="215" r="7" fill="#1971c2"/><line x1="140" y1="215" x2="162" y2="219" stroke="#1f2933" stroke-width="3" marker-end="url(#fy33-nuoli)"/>
  <circle cx="385" cy="105" r="7" fill="#1971c2"/><line x1="385" y1="105" x2="416" y2="136" stroke="#1f2933" stroke-width="3" marker-end="url(#fy33-nuoli)"/>
  <circle cx="500" cy="100" r="7" fill="#c92a2a"/><line x1="500" y1="100" x2="462" y2="122" stroke="#1f2933" stroke-width="3" marker-end="url(#fy33-nuoli)"/>
  <circle cx="445" cy="155" r="7" fill="#c92a2a"/><line x1="445" y1="155" x2="489" y2="155" stroke="#1f2933" stroke-width="3" marker-end="url(#fy33-nuoli)"/>
  <circle cx="375" cy="190" r="7" fill="#c92a2a"/><line x1="375" y1="190" x2="406" y2="159" stroke="#1f2933" stroke-width="3" marker-end="url(#fy33-nuoli)"/>
  <circle cx="505" cy="200" r="7" fill="#c92a2a"/><line x1="505" y1="200" x2="464" y2="185" stroke="#1f2933" stroke-width="3" marker-end="url(#fy33-nuoli)"/>
  <circle cx="430" cy="215" r="7" fill="#c92a2a"/><line x1="430" y1="215" x2="473" y2="223" stroke="#1f2933" stroke-width="3" marker-end="url(#fy33-nuoli)"/>
  <foreignObject x="115" y="250" width="80" height="42"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$p_1$</div></foreignObject>
  <foreignObject x="390" y="250" width="130" height="42"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$p_2 \gt p_1$</div></foreignObject>
</svg>

Kuva on kaaviokuva: nuolen pituus kuvaa hiukkasen nopeutta. Astiat ovat yhtä suuret, ja niissä on yhtä monta hiukkasta.

Lämpötilaa mitataan celsiusasteikolla, jossa 0 °C on veden jäätymispiste ja 100 °C veden kiehumispiste normaalipaineessa, ja kelvinasteikolla. Kelvinasteikon nollapiste on absoluuttinen nollapiste, alin mahdollinen lämpötila. Siinä hiukkasten keskimääräinen liike-energia on pienimmillään, eikä kylmempää voi olla. Celsiusasteen ja kelvinin suuruus on sama, joten lämpötilaero on sama kelvineinä ja celsiusasteina. Kun tilavuus ja kaasun määrä pysyvät samoina, kaasun paine on suoraan verrannollinen kelvinlämpötilaan. Myös hiukkasten keskimääräinen liike-energia on suoraan verrannollinen kelvinlämpötilaan, joten lämpötilojen suhteita verrataan kelvineinä. Paineen, tilavuuden ja lämpötilan yhteyttä tutkitaan tarkemmin luvussa *Kaasujen tilanmuutokset ja Boylen laki*.

## Kaava: Kelvinasteikko
Celsiuslämpötilan θ muunnos kelvineiksi on:
```latex
T = \theta + 273{,}15
```
missä T on lämpötila kelvineinä (K) ja θ lämpötila celsiusasteina (°C). Käytännössä riittää usein luku 273. Kelvineissä ei käytetä sanaa aste: sanotaan ”300 kelviniä”, ei ”300 kelvinastetta”.

Absoluuttinen nollapiste on siis 0 K = −273,15 °C. Kelvinlämpötila ei voi olla negatiivinen, mutta celsiuslämpötila voi.

<svg viewBox="0 0 600 300" role="img" aria-label="Kelvinasteikko ja celsiusasteikko rinnakkain mittakaavassa: 0 K on −273,15 °C (absoluuttinen nollapiste), 273,15 K on 0 °C (vesi jäätyy) ja 373,15 K on 100 °C (vesi kiehuu). Asteikkojen välit ovat yhtä suuret, ja kelvinlukema saadaan lisäämällä celsiuslukemaan 273,15." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <text x="20" y="34" fill="#1f2933">absoluuttinen nollapiste</text>
  <text x="590" y="34" text-anchor="end" fill="#1f2933">vesi kiehuu</text>
  <line x1="40" y1="110" x2="575" y2="110" stroke="#1f2933" stroke-width="3"/>
  <line x1="40" y1="190" x2="575" y2="190" stroke="#1f2933" stroke-width="3"/>
  <line x1="60" y1="98" x2="60" y2="202" stroke="#1971c2" stroke-width="4"/>
  <line x1="411" y1="98" x2="411" y2="202" stroke="#1971c2" stroke-width="4"/>
  <line x1="540" y1="98" x2="540" y2="202" stroke="#c92a2a" stroke-width="4"/>
  <foreignObject x="20" y="52" width="80" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$0\,\text{K}$</div></foreignObject>
  <foreignObject x="340" y="52" width="128" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$273{,}15\,\text{K}$</div></foreignObject>
  <foreignObject x="470" y="52" width="128" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$373{,}15\,\text{K}$</div></foreignObject>
  <foreignObject x="110" y="130" width="250" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$T = \theta + 273{,}15$</div></foreignObject>
  <foreignObject x="8" y="206" width="150" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:left">$-273{,}15\,\text{°C}$</div></foreignObject>
  <foreignObject x="366" y="206" width="90" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$0\,\text{°C}$</div></foreignObject>
  <foreignObject x="480" y="206" width="112" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$100\,\text{°C}$</div></foreignObject>
  <text x="411" y="282" text-anchor="middle" fill="#1f2933">vesi jäätyy</text>
</svg>

Kuva on piirretty mittakaavassa. Yläasteikko on kelvinasteikko ja alaasteikko celsiusasteikko; väli 0 °C:sta 100 °C:een on yhtä pitkä kuin väli 273,15 K:sta 373,15 K:iin.

## Esimerkki
Suljetussa jäykässä astiassa on kaasua, joten sen tilavuus ja aineen määrä pysyvät samoina. Kaasun paine mitataan eri lämpötiloissa:

| θ (°C) | 0 | 20 | 40 | 60 | 80 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| p (kPa) | 100 | 107 | 115 | 122 | 129 | 137 |

Määritä ekstrapoloimalla lämpötila, jossa kaasun paine olisi nolla.

<!-- vaihe -->

**Kuvaaja.** Pisteet asettuvat suoralle. Jatketaan suoraa vasemmalle mittausalueen ulkopuolelle eli ekstrapoloidaan: sovitettua suoraa jatketaan mitattujen pisteiden yli, vaikka siellä ei ole mittauksia.

<svg viewBox="0 0 600 300" role="img" aria-label="Kaasun paine lämpötilan funktiona suljetussa astiassa: mittapisteet lämpötila-alueella 0–100 °C asettuvat suoralle, ja ekstrapoloitu suora kohtaa nollapaineen lämpötilassa noin −270 °C" style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <line x1="70" y1="250" x2="590" y2="250" stroke="#1f2933" stroke-width="3"/>
  <line x1="70" y1="250" x2="70" y2="30" stroke="#1f2933" stroke-width="3"/>
  <line x1="107" y1="250" x2="445" y2="100" stroke="#6b7480" stroke-width="3" stroke-dasharray="9 7"/>
  <line x1="445" y1="100" x2="570" y2="44" stroke="#1f2933" stroke-width="4"/>
  <circle cx="445" cy="100" r="5" fill="#1f2933"/><circle cx="470" cy="90" r="5" fill="#1f2933"/><circle cx="495" cy="78" r="5" fill="#1f2933"/><circle cx="520" cy="67" r="5" fill="#1f2933"/><circle cx="545" cy="56" r="5" fill="#1f2933"/><circle cx="570" cy="44" r="5" fill="#1f2933"/>
  <circle cx="107" cy="250" r="6" fill="none" stroke="#1971c2" stroke-width="3"/>
  <text x="107" y="282" text-anchor="middle" fill="#6b7480">−270</text>
  <text x="445" y="282" text-anchor="middle" fill="#6b7480">0</text>
  <text x="570" y="282" text-anchor="middle" fill="#6b7480">100</text>
  <text x="590" y="228" text-anchor="end" fill="#1f2933">θ (°C)</text>
  <text x="80" y="28" fill="#1f2933">p (kPa)</text>
  <text x="62" y="106" text-anchor="end" fill="#6b7480">100</text>
  <text x="62" y="50" text-anchor="end" fill="#6b7480">137</text>
  <text x="62" y="256" text-anchor="end" fill="#6b7480">0</text>
  <text x="80" y="212" fill="#1f2933">p = 0</text>
</svg>

Pystyakseli on piirretty kuvan vasempaan reunaan, noin −300 °C:n kohdalle, eikä kohtaan θ = 0. Yhtenäinen suora on mittausalue ja katkoviiva ekstrapolointi.

<!-- vaihe -->

**Kulmakerroin.** Suoran kulmakerroin lasketaan mittausalueen päätepisteistä:
```latex
\begin{aligned}
&k = \frac{\Delta p}{\Delta \theta} \\
&= \frac{(137 - 100)\,\text{kPa}}{(100 - 0)\,\text{°C}} \\
&= 0{,}37\,\text{kPa/°C}
\end{aligned}
```

<!-- vaihe -->

**Kaava ratkaistuna.** Suoran yhtälö on ylärivillä, missä p₀ on paine lämpötilassa 0 °C. Nollapaine saavutetaan, kun p = 0, ja siitä ratkaistaan lämpötila:
```latex
\begin{aligned}
&p = p_0 + k\theta \\
&0 = p_0 + k\theta \\
&\theta = -\frac{p_0}{k}
\end{aligned}
```

<!-- vaihe -->

**Sijoitus.** Tässä p₀ = 100 kPa, joten
```latex
\begin{aligned}
&\theta = -\frac{p_0}{k} \\
&= -\frac{100\,\text{kPa}}{0{,}37\,\text{kPa/°C}} \\
&\approx -270\,\text{°C}
\end{aligned}
```

<!-- vaihe -->

**Järkevyys.** Tulos on lähellä absoluuttista nollapistettä −273 °C. Mikromallin mukaan tässä lämpötilassa hiukkasten liike olisi niin vähäistä, ettei paine enää syntyisi. Näin absoluuttinen nollapiste voidaan määrittää kokeellisesti. Todelliset kaasut nesteytyvät jo ennen tätä lämpötilaa, joten suoran jatke on vain malli ja kuvaa raja-arvoa.

## Yleinen virhekäsitys
Moni ajattelee, että lämpötila kaksinkertaistuu, kun se nousee 10 °C:sta 20 °C:een. Fysikaalisesti oikea vertailu tehdään kelvineinä: 283 K:sta 293 K:iin. Lämpötilojen suhde on 293/283 ≈ 1,035, eli nousu on noin 3,5 %. Siksi hiukkasten keskimääräinen liike-energia ei kaksinkertaistu. Toinen virhe on pitää 0 °C:ta alimpana mahdollisena lämpötilana. Se on vain veden jäätymispiste, ja alin mahdollinen lämpötila on 0 K.

## Tiivistelmä
- Termodynaaminen systeemi on rajattu osa maailmaa. Sen tilaa kuvaavat tilanmuuttujat: lämpötila, paine, tilavuus ja aineen määrä.
- Kaasusysteemissä lämpötila, paine ja tilavuus riippuvat toisistaan: jos yhtä muutetaan, vähintään yksi muista muuttuu myös.
- Mikromalli: lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta, ja paine syntyy hiukkasten törmäyksistä seinämään.
- Kun tilavuus ja aineen määrä pysyvät samoina, paine on suoraan verrannollinen kelvinlämpötilaan. Mittapisteiden suoran jatkaminen eli ekstrapolointi antaa absoluuttisen nollapisteen.
- Muunnos on $T = \theta + 273{,}15$. Absoluuttinen nollapiste on 0 K = −273,15 °C.
