# Aineen lämpeneminen ja jäähtyminen: Q = cmΔT

> **Miksi** uimarannan hiekka polttaa jalkapohjia jo aamupäivällä, kun vesi on vielä viileää, vaikka aurinko on paistanut molempiin yhtä kauan?

## Ydinajatus
Kun kappaleeseen siirtyy lämpöä, sen sisäenergia kasvaa ja lämpötila nousee. Kokeissa havaitaan, että tarvittava lämpömäärä on suoraan verrannollinen sekä lämpötilan muutokseen että kappaleen massaan: kaksi kertaa suurempi lämpötilan nousu vaatii kaksinkertaisen lämpömäärän, ja kaksinkertainen vesimäärä vaatii kaksinkertaisen lämpömäärän. Lisäksi lämpömäärä riippuu aineesta. Kilogramman vettä lämmittäminen yhdellä asteella vaatii noin 4,2 kJ, mutta kilogramman rautaa vain noin 0,45 kJ. Aineelle ominainen kerroin on ominaislämpökapasiteetti c, jonka yksikkö on J/(kg·K). Se kertoo, kuinka paljon energiaa tarvitaan yhden kilogramman lämmittämiseen yhdellä kelvinillä, ja sama määrä vapautuu, kun aine jäähtyy yhden kelvinin.

Veden ominaislämpökapasiteetti on poikkeuksellisen suuri. Siksi vesi lämpenee auringossa hitaasti ja jäähtyy illalla hitaasti, kun taas hiekka, jonka c on noin viidesosa veden arvosta, kuumenee samalla energialla moninkertaisesti. Samasta syystä järvet tasaavat rannikon lämpötiloja ja vesi on hyvä lämmönsiirtoaine lämmitysputkissa. Koko kappaleen lämpökapasiteetti C = cm kertoo, kuinka monta joulea kappaleen lämpötilan nostaminen yhdellä kelvinillä vaatii; sen yksikkö on J/K.

Kun kuuma ja kylmä kappale laitetaan yhteen eristettyyn astiaan, lämpöä siirtyy kuumemmasta kylmempään, kunnes molemmilla on sama lämpötila. Tätä tilaa sanotaan lämpötasapainoksi. Energia säilyy: kuuman kappaleen luovuttama lämpömäärä on yhtä suuri kuin kylmän vastaanottama. Eristettyä astiaa, jossa tämä mitataan, sanotaan kalorimetriksi, ja mittausta kalorimetriseksi mittaukseksi. Sillä voidaan määrittää tuntemattoman aineen ominaislämpökapasiteetti, kun veden ominaislämpökapasiteetti tunnetaan.

## Kaava
Lämpömäärä, joka tarvitaan massan m lämmittämiseen tai joka vapautuu sen jäähtyessä, on
```latex
Q = c m \Delta T
```
missä Q on lämpömäärä (J), c aineen ominaislämpökapasiteetti (J/(kg·K)), m massa (kg) ja ΔT lämpötilan muutos (K). Lämpötilan muutos on sama kelvineinä ja celsiusasteina, joten ΔT voidaan laskea suoraan celsiuslämpötiloista. Lämmetessä Q on positiivinen ja jäähtyessä negatiivinen.

Eristetyssä astiassa kuuman kappaleen 1 luovuttama lämpömäärä on yhtä suuri kuin kylmän kappaleen 2 vastaanottama:
```latex
c_1 m_1 (T_1 - T) = c_2 m_2 (T - T_2)
```
missä T₁ ja T₂ ovat alkulämpötilat ja T yhteinen loppulämpötila eli tasapainolämpötila. Yhtälössä on useita termejä, ja siitä voidaan ratkaista mikä tahansa suure, kun muut tunnetaan: loppulämpötila, massa tai tuntematon ominaislämpökapasiteetti.

| Aine | c (J/(kg·K)) |
| --- | --- |
| vesi | 4190 |
| jää | 2100 |
| alumiini | 900 |
| hiekka | 800 |
| rauta | 450 |
| kupari | 385 |

<svg viewBox="0 0 600 300" role="img" aria-label="Pylväskaavio ominaislämpökapasiteeteista: vesi 4190, jää 2100, alumiini 900, hiekka 800, rauta 450 ja kupari 385 joulea kilogrammaa ja kelviniä kohti" style="max-width:100%;font-family:system-ui,sans-serif;font-size:20px">
  <line x1="70" y1="250" x2="580" y2="250" stroke="currentColor" stroke-width="3"/>
  <rect x="90" y="40" width="60" height="210" fill="currentColor" fill-opacity="0.75"/>
  <rect x="172" y="145" width="60" height="105" fill="currentColor" fill-opacity="0.55"/>
  <rect x="254" y="205" width="60" height="45" fill="currentColor" fill-opacity="0.55"/>
  <rect x="336" y="210" width="60" height="40" fill="currentColor" fill-opacity="0.55"/>
  <rect x="418" y="227" width="60" height="23" fill="currentColor" fill-opacity="0.55"/>
  <rect x="500" y="231" width="60" height="19" fill="currentColor" fill-opacity="0.55"/>
  <text x="120" y="32" text-anchor="middle" fill="currentColor">4190</text>
  <text x="202" y="137" text-anchor="middle" fill="currentColor">2100</text>
  <text x="284" y="197" text-anchor="middle" fill="currentColor">900</text>
  <text x="366" y="202" text-anchor="middle" fill="currentColor">800</text>
  <text x="448" y="219" text-anchor="middle" fill="currentColor">450</text>
  <text x="530" y="223" text-anchor="middle" fill="currentColor">385</text>
  <text x="120" y="278" text-anchor="middle" fill="currentColor">vesi</text>
  <text x="202" y="278" text-anchor="middle" fill="currentColor">jää</text>
  <text x="284" y="278" text-anchor="middle" fill="currentColor">alumiini</text>
  <text x="366" y="278" text-anchor="middle" fill="currentColor">hiekka</text>
  <text x="448" y="278" text-anchor="middle" fill="currentColor">rauta</text>
  <text x="530" y="278" text-anchor="middle" fill="currentColor">kupari</text>
  <text x="66" y="22" text-anchor="end" fill="currentColor">c</text>
</svg>

## Esimerkki
Kalorimetrissä on 0,300 kg vettä, jonka lämpötila on 20,0 °C. Siihen upotetaan 0,200 kg:n metallikappale, joka on kuumennettu kiehuvassa vedessä 100,0 °C:n lämpötilaan. Sekoituksen jälkeen lämpötila asettuu arvoon 24,5 °C. Mikä on metallin ominaislämpökapasiteetti? Kalorimetrin oma lämpökapasiteetti ja lämpöhäviöt ympäristöön jätetään huomiotta.

Metalli jäähtyy 100,0 °C:sta 24,5 °C:seen, eli 75,5 K, ja vesi lämpenee 20,0 °C:sta 24,5 °C:seen, eli 4,5 K. Luovutettu lämpömäärä on yhtä suuri kuin vastaanotettu:
```latex
c_\text{m} \cdot 0{,}200\,\text{kg} \cdot 75{,}5\,\text{K} = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}300\,\text{kg} \cdot 4{,}5\,\text{K}
```
Oikea puoli on 5660 J (tarkemmin 5656,5 J), joten
```latex
c_\text{m} = \frac{5656{,}5\,\text{J}}{0{,}200\,\text{kg} \cdot 75{,}5\,\text{K}} \approx 375\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}
```
Arvo on lähellä kuparin ominaislämpökapasiteettia 385 J/(kg·K), joten kappale on luultavasti kuparia. Pieni ero selittyy sillä, että osa lämmöstä siirtyi kalorimetrin astiaan ja ilmaan. Huomaa, että vesi lämpeni vain 4,5 K, vaikka metalli jäähtyi 75,5 K: veden lämpökapasiteetti 1257 J/K on paljon suurempi kuin kappaleen 75 J/K.

## Yleinen virhekäsitys
Moni ajattelee, että lämpömäärä ja lämpötila ovat sama asia, tai että samaan lämpötilaan lämmitetyt kappaleet ovat saaneet saman määrän energiaa. Kilon vettä ja kilon rautaa lämmittäminen 20 °C:sta 60 °C:seen vaatii vedelle lähes kymmenkertaisen energian. Toinen virhe on laskea tasapainolämpötila keskiarvona: kun 1,0 kg 80-asteista vettä kaadetaan 3,0 kg:aan 20-asteista vettä, lopputulos ei ole 50 °C vaan 35 °C, koska massat ovat erisuuret. Kolmas virhe on muuntaa ΔT kelvineiksi lisäämällä 273: lämpötilan muutos on sama kummallakin asteikolla.

## Tiivistelmä
- Lämpömäärä on verrannollinen massaan ja lämpötilan muutokseen: $Q = c m \Delta T$. Ominaislämpökapasiteetti c riippuu aineesta, ja vedellä se on suuri, 4190 J/(kg·K).
- Lämpökapasiteetti $C = cm$ kertoo, kuinka monta joulea koko kappaleen lämmittäminen yhdellä kelvinillä vaatii.
- Eristetyssä astiassa kuuman luovuttama lämpömäärä on yhtä suuri kuin kylmän vastaanottama: $c_1 m_1 (T_1 - T) = c_2 m_2 (T - T_2)$. Loppulämpötila on lämpötasapaino, ei keskiarvo.
- Kalorimetrisellä mittauksella määritetään tuntemattoman aineen ominaislämpökapasiteetti veden avulla.
