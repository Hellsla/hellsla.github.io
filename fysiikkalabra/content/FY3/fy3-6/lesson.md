# Aineen lämpeneminen ja jäähtyminen: Q = cmΔT

> **Miksi** uimarannan hiekka polttaa jalkapohjia jo aamupäivällä, kun vesi on vielä viileää, vaikka aurinko on paistanut molempiin yhtä kauan?

## Ydinajatus
Kun kappaleeseen siirtyy lämpöä, sen sisäenergia kasvaa ja lämpötila nousee. Kokeissa havaitaan, että tarvittava lämpömäärä on suoraan verrannollinen sekä lämpötilan muutokseen että kappaleen massaan: kaksi kertaa suurempi lämpötilan nousu vaatii kaksinkertaisen lämpömäärän, ja kaksinkertainen vesimäärä vaatii kaksinkertaisen lämpömäärän. Lisäksi lämpömäärä riippuu aineesta. Kilogramman veden lämmittäminen yhdellä asteella vaatii noin 4,2 kJ, mutta kilogramman raudan lämmittäminen vain noin 0,45 kJ. Aineelle ominainen kerroin on ominaislämpökapasiteetti c, jonka yksikkö on J/(kg·K). Se kertoo, kuinka paljon energiaa tarvitaan yhden kilogramman lämmittämiseen yhdellä kelvinillä, ja sama määrä vapautuu, kun aine jäähtyy yhden kelvinin.

Tärkeä syy on, että veden ominaislämpökapasiteetti on poikkeuksellisen suuri: vesi lämpenee auringossa hitaasti ja jäähtyy illalla hitaasti, kun taas hiekka, jonka c on noin viidesosa veden arvosta, kuumenee samalla energialla moninkertaisesti enemmän. Lisäksi aurinko lämmittää vain hiekan ohutta pintakerrosta, kun taas vedessä lämpeneminen ulottuu syvemmälle. Suuren ominaislämpökapasiteettinsa vuoksi järvet tasaavat rannikon lämpötiloja ja vesi on hyvä lämmönsiirtoaine lämmitysputkissa.

<svg viewBox="0 0 600 300" role="img" aria-label="Kaavakuva: yhtä suuriin massoihin vettä ja hiekkaa siirtyy sama lämpömäärä Q. Vasemmalla veden lämpömittari nousee vain vähän, oikealla hiekan lämpömittari nousee noin viisi kertaa enemmän, koska hiekan ominaislämpökapasiteetti on noin viidesosa veden arvosta. Nousujen suhde on piirretty mittakaavassa." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <foreignObject x="150" y="2" width="300" height="42"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{sama } Q \text{ ja sama } m$</div></foreignObject>
  <line x1="300" y1="50" x2="300" y2="290" stroke="currentColor" stroke-opacity="0.4" stroke-dasharray="6 6"/>
  <line x1="115" y1="62" x2="115" y2="118" stroke="currentColor" stroke-width="4"/>
  <polygon points="115,138 103,114 127,114" fill="currentColor"/>
  <foreignObject x="128" y="70" width="50" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$Q$</div></foreignObject>
  <rect x="40" y="150" width="150" height="92" fill="currentColor" fill-opacity="0.15"/>
  <polyline points="40,140 40,244 190,244 190,140" fill="none" stroke="currentColor" stroke-width="3"/>
  <path d="M40,150 Q58,142 77,150 T115,150 T152,150 T190,150" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="115" y="284" text-anchor="middle" fill="currentColor">vesi</text>
  <rect x="228" y="50" width="16" height="200" rx="8" fill="none" stroke="currentColor" stroke-width="2"/>
  <circle cx="236" cy="258" r="13" fill="currentColor" fill-opacity="0.35" stroke="currentColor" stroke-width="2"/>
  <rect x="231" y="200" width="10" height="50" fill="currentColor" fill-opacity="0.35"/>
  <rect x="231" y="180" width="10" height="20" fill="currentColor"/>
  <line x1="222" y1="200" x2="250" y2="200" stroke="currentColor" stroke-width="2" stroke-dasharray="3 3"/>
  <foreignObject x="250" y="166" width="48" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$\Delta T$</div></foreignObject>
  <line x1="415" y1="62" x2="415" y2="118" stroke="currentColor" stroke-width="4"/>
  <polygon points="415,138 403,114 427,114" fill="currentColor"/>
  <foreignObject x="428" y="70" width="50" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$Q$</div></foreignObject>
  <rect x="340" y="196" width="150" height="46" fill="currentColor" fill-opacity="0.3"/>
  <polyline points="340,140 340,244 490,244 490,140" fill="none" stroke="currentColor" stroke-width="3"/>
  <path d="M340,196 L365,190 L392,197 L420,189 L450,196 L490,191" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="415" y="284" text-anchor="middle" fill="currentColor">hiekka</text>
  <rect x="528" y="50" width="16" height="200" rx="8" fill="none" stroke="currentColor" stroke-width="2"/>
  <circle cx="536" cy="258" r="13" fill="currentColor" fill-opacity="0.35" stroke="currentColor" stroke-width="2"/>
  <rect x="531" y="200" width="10" height="50" fill="currentColor" fill-opacity="0.35"/>
  <rect x="531" y="95" width="10" height="105" fill="currentColor"/>
  <line x1="522" y1="200" x2="550" y2="200" stroke="currentColor" stroke-width="2" stroke-dasharray="3 3"/>
  <foreignObject x="550" y="128" width="48" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$\Delta T$</div></foreignObject>
</svg>

Kun kuuma ja kylmä kappale laitetaan yhteen eristettyyn astiaan, lämpöä siirtyy kuumemmasta kylmempään, kunnes molemmilla on sama lämpötila. Tätä tilaa sanotaan lämpötasapainoksi. Energia säilyy: kuuman kappaleen luovuttama lämpömäärä on yhtä suuri kuin kylmän vastaanottama. Eristettyä astiaa, jossa tämä mitataan, sanotaan kalorimetriksi, ja mittausta kalorimetriseksi mittaukseksi. Sillä voidaan määrittää tuntemattoman aineen ominaislämpökapasiteetti, kun veden ominaislämpökapasiteetti tunnetaan.

## Kaava
Lämpömäärä, joka tarvitaan massan m lämmittämiseen tai joka vapautuu sen jäähtyessä, on
```latex
\begin{aligned}
Q &= c m \Delta T \\
\Delta T &= T_\text{loppu} - T_\text{alku}
\end{aligned}
```
missä Q on lämpömäärä (J), c aineen ominaislämpökapasiteetti (J/(kg·K)), m massa (kg) ja ΔT lämpötilan muutos (K) eli loppulämpötila $T_\text{loppu}$ miinus alkulämpötila $T_\text{alku}$. Lämpötilan muutos on sama kelvineinä ja celsiusasteina, joten ΔT voidaan laskea suoraan celsiuslämpötiloista. Lämmetessä ΔT ja Q ovat positiivisia, jäähtyessä negatiivisia.

Koko kappaleen lämpökapasiteetti
```latex
C = c m
```
kertoo, kuinka monta joulea kappaleen lämpötilan nostaminen yhdellä kelvinillä vaatii. C on lämpökapasiteetti (J/K), c ominaislämpökapasiteetti ja m massa. Kappale, jonka lämpökapasiteetti on suuri, lämpenee ja jäähtyy hitaasti.

Eristetyssä astiassa kuuman kappaleen 1 luovuttama lämpömäärä on yhtä suuri kuin kylmän kappaleen 2 vastaanottama:
```latex
c_1 m_1 (T_1 - T) = c_2 m_2 (T - T_2)
```
missä T₁ ja T₂ ovat kappaleiden alkulämpötilat ja T yhteinen loppulämpötila eli tasapainolämpötila. Yhtälön molemmat puolet ovat positiivisia lämpömääriä: kuumalle kappaleelle lasketaan alkulämpötila miinus loppulämpötila, kylmälle loppulämpötila miinus alkulämpötila. Yhtälöstä voidaan ratkaista mikä tahansa suure, kun muut tunnetaan: loppulämpötila, massa tai tuntematon ominaislämpökapasiteetti.

Tasapainolämpötila T esiintyy yhtälössä kahdessa termissä. Se ratkaistaan kertomalla sulut auki, keräämällä T:tä sisältävät termit samalle puolelle ja ottamalla T yhteiseksi tekijäksi:
```latex
\begin{aligned}
&c_1 m_1 T_1 - c_1 m_1 T \\
&\quad = c_2 m_2 T - c_2 m_2 T_2 \\[6pt]
&c_1 m_1 T_1 + c_2 m_2 T_2 \\
&\quad = c_1 m_1 T + c_2 m_2 T \\
&\quad = (c_1 m_1 + c_2 m_2)\,T
\end{aligned}
```
Kun yhtälö jaetaan puolittain summalla c₁m₁ + c₂m₂, saadaan
```latex
T = \frac{c_1 m_1 T_1 + c_2 m_2 T_2}{c_1 m_1 + c_2 m_2}
```
Tasapainolämpötila on siis alkulämpötilojen painotettu keskiarvo, jossa painoina ovat kappaleiden lämpökapasiteetit c₁m₁ ja c₂m₂. Tavallinen keskiarvo saadaan vain, kun lämpökapasiteetit ovat yhtä suuret.

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

<!-- vaihe -->

**Tunnetut ja kysytty.** Vesi: $c_\text{v} = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$, $m_\text{v} = 0{,}300\,\text{kg}$, $T_\text{v} = 20{,}0\,{}^\circ\text{C}$. Metalli: $m_\text{m} = 0{,}200\,\text{kg}$, $T_\text{m} = 100{,}0\,{}^\circ\text{C}$. Tasapainolämpötila $T = 24{,}5\,{}^\circ\text{C}$. Kysytään metallin ominaislämpökapasiteettia $c_\text{m}$. Metalli jäähtyy 75,5 K ja vesi lämpenee 4,5 K.

<!-- vaihe -->

**Kaava ratkaistuna.** Metallin luovuttama lämpömäärä on yhtä suuri kuin veden vastaanottama. Ratkaistaan yhtälöstä $c_\text{m}$:
```latex
\begin{aligned}
&c_\text{m} m_\text{m} (T_\text{m} - T) \\
&\quad = c_\text{v} m_\text{v} (T - T_\text{v}) \\[6pt]
&c_\text{m} = \frac{c_\text{v} m_\text{v} (T - T_\text{v})}{m_\text{m} (T_\text{m} - T)}
\end{aligned}
```

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin osoittaja eli veden vastaanottama lämpömäärä $Q_\text{v}$ ja jaetaan se sitten:
```latex
\begin{aligned}
&Q_\text{v} = c_\text{v} m_\text{v} (T - T_\text{v}) \\
&= 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}300\,\text{kg} \cdot 4{,}5\,\text{K} \\
&= 5656{,}5\,\text{J} \\[6pt]
&c_\text{m} = \frac{Q_\text{v}}{m_\text{m} (T_\text{m} - T)} \\
&= \frac{5656{,}5\,\text{J}}{0{,}200\,\text{kg} \cdot 75{,}5\,\text{K}} \\
&= 374{,}6\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \\
&\approx 3{,}7 \cdot 10^2\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Metallin ominaislämpökapasiteetti on noin $3{,}7 \cdot 10^2\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla, koska veden lämpötilan muutos 4,5 K tunnetaan vain kahden numeron tarkkuudella: jos loppulukema olisi 0,1 K suurempi eli 24,6 °C, tulos olisi 383 J/(kg·K).

<!-- vaihe -->

**Järkevyys.** Arvo on lähellä kuparin ominaislämpökapasiteettia 385 J/(kg·K), joten kappale on luultavasti kuparia. Häviöttömässä kalorimetrissä 0,200 kg:n kuparikappale nostaisi veden 24,6 °C:seen (kokeile simulaatiossa); mitattu 0,1 K pienempi lukema selittyy lukematarkkuudella tai sillä, että todellisuudessa osa lämmöstä siirtyi myös kalorimetrin astiaan ja ilmaan. Vesi lämpeni vain 4,5 K, vaikka metalli jäähtyi 75,5 K: veden lämpökapasiteetti on 0,300 kg · 4190 J/(kg·K) = 1257 J/K, mikä on paljon enemmän kuin kappaleen lämpökapasiteetti 0,200 kg · 374,6 J/(kg·K) ≈ 75 J/K.

## Yleinen virhekäsitys
Moni ajattelee, että lämpömäärä ja lämpötila ovat sama asia, tai että samaan lämpötilaan lämmitetyt kappaleet ovat saaneet saman määrän energiaa. Kilon veden ja kilon raudan lämmittäminen 20 °C:sta 60 °C:seen vaatii vedelle lähes kymmenkertaisen energian. Toinen virhe on laskea tasapainolämpötila keskiarvona. Kun 1,0 kg 80-asteista vettä kaadetaan 3,0 kg:aan 20-asteista vettä, veden ominaislämpökapasiteetti c on yhtälön molemmilla puolilla ja supistuu pois:
```latex
\begin{aligned}
&1{,}0\,\text{kg} \cdot (80\,{}^\circ\text{C} - T) \\
&\quad = 3{,}0\,\text{kg} \cdot (T - 20\,{}^\circ\text{C}) \\[6pt]
&80\,{}^\circ\text{C} - T = 3T - 60\,{}^\circ\text{C} \\
&140\,{}^\circ\text{C} = 4T \\
&T = 35\,{}^\circ\text{C}
\end{aligned}
```
Kuuma vesi on vasemmalla puolella kuten yleisessä yhtälössä. Kolmannella rivillä yhtälö on jaettu puolittain kilogrammalla ja sulut on kerrottu auki. Lopputulos ei siis ole 50 °C vaan 35 °C, koska kylmää vettä on kolme kertaa enemmän kuin kuumaa. Sama tulos saadaan painotetulla keskiarvolla: T = (3,0 kg · 20 °C + 1,0 kg · 80 °C) / 4,0 kg = 35 °C.

Kolmas virhe on muuntaa ΔT kelvineiksi lisäämällä 273: lämpötilan muutos on sama kummallakin asteikolla.

## Tiivistelmä
- Lämpömäärä on verrannollinen massaan ja lämpötilan muutokseen: $Q = c m \Delta T$. Ominaislämpökapasiteetti c riippuu aineesta, ja vedellä se on suuri, 4190 J/(kg·K).
- Lämpökapasiteetti $C = cm$ kertoo, kuinka monta joulea koko kappaleen lämmittäminen yhdellä kelvinillä vaatii.
- Eristetyssä astiassa kuuman luovuttama lämpömäärä on yhtä suuri kuin kylmän vastaanottama: $c_1 m_1 (T_1 - T) = c_2 m_2 (T - T_2)$. Tasapainolämpötila T ratkaistaan keräämällä T:n termit samalle puolelle; se on lämpökapasiteeteilla painotettu keskiarvo eikä yleensä alkulämpötilojen tavallinen keskiarvo.
- Kalorimetrisellä mittauksella määritetään tuntemattoman aineen ominaislämpökapasiteetti veden avulla.
