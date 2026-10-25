# Ideaalikaasun tilanyhtälö pV = nRT

> **Miksi** samankokoiset helium- ja ilmapallot sisältävät yhtä monta kaasuhiukkasta, vaikka heliumpallo on paljon kevyempi?

## Ydinajatus
Kaasujen tilanmuutoksia tutkittiin edellisellä oppitunnilla yksi kerrallaan: vakiolämpötilassa pV on vakio, vakiopaineessa V/T on vakio ja vakiotilavuudessa p/T on vakio. Nämä kolme kaasulakia voidaan yhdistää. Kun suljetun kaasumäärän paine, tilavuus ja lämpötila muuttuvat samanaikaisesti, suure pV/T pysyy vakiona. Tätä sanotaan yhdistetyksi kaasulaiksi.

Vakion arvo riippuu siitä, kuinka paljon kaasua on. Jos samaan paineeseen ja lämpötilaan otetaan kaksi kertaa enemmän kaasua, se vie kaksinkertaisen tilavuuden. Kaasun määrää mitataan ainemääränä n, jonka yksikkö on mooli (mol). Yksi mooli on 6,022 · 10²³ hiukkasta, ja tätä lukua sanotaan Avogadron vakioksi. Aineen moolimassa M kertoo yhden moolin massan: heliumin moolimassa on 4,0 g/mol, ilman keskimäärin 29 g/mol ja hiilidioksidin 44 g/mol.

Mittauksissa havaitaan, että pV/(nT) on kaikille kaasuille sama luku, kun paine ei ole kovin suuri eikä lämpötila kovin matala. Se on moolinen kaasuvakio R = 8,31 J/(mol·K). Siitä saadaan ideaalikaasun tilanyhtälö pV = nRT, joka sitoo yhteen kaasun neljä tilaa kuvaavaa suuretta. Kaasun laatu ei näy yhtälössä lainkaan. Samassa paineessa ja lämpötilassa yhtä suuressa tilavuudessa on siis aina yhtä monta moolia kaasua, olipa kaasu heliumia tai ilmaa. Tämä vastaa alun kysymykseen: pallot sisältävät yhtä monta hiukkasta, mutta heliumhiukkaset ovat paljon kevyempiä.

Ideaalikaasu on mikromalli. Siinä hiukkaset ajatellaan pistemäisiksi, ja ne vaikuttavat toisiinsa ja astian seinämiin vain törmätessään. Paine syntyy seinämiin osuvista törmäyksistä, ja se kasvaa, kun hiukkasia on enemmän, kun ne liikkuvat nopeammin eli lämpötila on korkeampi tai kun tilavuus on pienempi. Todelliset kaasut noudattavat mallia hyvin tavallisissa oloissa. Malli alkaa pettää suurissa paineissa ja matalissa lämpötiloissa, kun hiukkaset ovat lähellä toisiaan ja niiden välinen vetovoima tiivistää kaasun nesteeksi.

## Kaava
Ideaalikaasun tilanyhtälö on
```latex
pV = nRT
```
missä p on paine (Pa), V tilavuus (m³), n ainemäärä (mol), R = 8,31 J/(mol·K) moolinen kaasuvakio ja T lämpötila kelvineinä (K). Tilanyhtälössä paine on aina kokonaispaine pascaleina ja tilavuus kuutiometreinä, koska R:n yksikössä on joule eli Pa·m³.

Ainemäärä saadaan massasta ja moolimassasta:
```latex
n = \frac{m}{M}
```
missä m on massa (kg tai g) ja M moolimassa (kg/mol tai g/mol).

Kun kaasun määrä ei muutu, tilanyhtälöstä seuraa yhdistetty kaasulaki
```latex
\frac{p_1 V_1}{T_1} = \frac{p_2 V_2}{T_2}
```
missä alaindeksit 1 ja 2 tarkoittavat alku- ja lopputilaa. Siitä saadaan jokainen edellisen oppitunnin kaasulaki, kun yksi suure pidetään vakiona.

## Esimerkki
Juhlapallo täytetään heliumilla, kunnes sen tilavuus on 5,0 l. Pallossa paine on 101 kPa ja lämpötila 20 °C. Kuinka monta moolia heliumia pallossa on, ja mikä on heliumin massa? Heliumin moolimassa on 4,0 g/mol.

Muutetaan yksiköt: $V = 5{,}0\,\text{l} = 0{,}0050\,\text{m}^3$, $p = 101\,000\,\text{Pa}$ ja $T = (20 + 273{,}15)\,\text{K} = 293{,}15\,\text{K}$. Ratkaistaan tilanyhtälöstä ainemäärä:
```latex
n = \frac{pV}{RT} = \frac{101\,000\,\text{Pa} \cdot 0{,}0050\,\text{m}^3}{8{,}31\,\tfrac{\text{J}}{\text{mol}\cdot\text{K}} \cdot 293{,}15\,\text{K}} \approx 0{,}21\,\text{mol}
```
Heliumin massa on $m = nM = 0{,}207\,\text{mol} \cdot 4{,}0\,\text{g/mol} \approx 0{,}83\,\text{g}$.

Samankokoisessa ilmapallossa on samassa paineessa ja lämpötilassa yhtä paljon eli 0,21 mol ilmaa, mutta sen massa on noin 6,0 g, koska ilman moolimassa on 29 g/mol. Tulos on järkevä: litrassa kaasua on huoneenlämmössä noin 0,04 mol.

## Yleinen virhekäsitys
Yleisin virhe on käyttää tilanyhtälössä celsiusasteita. Esimerkiksi 0 °C antaisi nollan, mutta kaasulla on paine myös jäätymispisteessä. Lämpötila muutetaan aina kelvineiksi. Toinen virhe on sijoittaa paine kilopascaleina ja tilavuus litroina. Silloin tulos on tuhat tai miljoona kertaa väärä, ellei yksiköitä muuteta perusyksiköiksi. Kolmas virhe on ajatella, että raskaampaa kaasua mahtuu samaan tilavuuteen vähemmän moolia. Ainemäärä riippuu vain paineesta, tilavuudesta ja lämpötilasta, ei kaasun laadusta. Massa sen sijaan riippuu moolimassasta.

## Tiivistelmä
- Ideaalikaasun tilanyhtälö on $pV = nRT$, missä $R = 8{,}31\,\text{J/(mol·K)}$ ja T on kelvineinä.
- Ainemäärä n kertoo kaasun määrän mooleina, ja $n = m/M$. Yksi mooli on 6,022 · 10²³ hiukkasta.
- Kun kaasun määrä pysyy samana, $p_1V_1/T_1 = p_2V_2/T_2$, ja siitä saadaan erilliset kaasulait.
- Samassa paineessa, lämpötilassa ja tilavuudessa on aina yhtä monta moolia kaasua, kaasun laadusta riippumatta.
- Ideaalikaasumalli toimii hyvin tavallisissa oloissa ja pettää suurissa paineissa ja matalissa lämpötiloissa.
