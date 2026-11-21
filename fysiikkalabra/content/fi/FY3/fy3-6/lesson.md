# Aineen lämpeneminen ja jäähtyminen: $Q = cm\Delta T$

> **Miksi** uimarannan hiekka polttaa jalkapohjia jo aamupäivällä, kun vesi on vielä viileää, vaikka aurinko on paistanut molempiin yhtä kauan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: järven uimaranta aamupäivällä. Aurinko paistaa sekä hiekkaan että veteen. Hiekan yllä väreilee kuumuus, ja hiekkaan pistetyn lämpömittarin punainen pylväs on korkealla. Rantaveteen pistetyn lämpömittarin pylväs on matalalla, koska vesi on vielä viileää." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-6-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Kun kappaleeseen siirtyy lämpöä eikä sen olomuoto muutu, sen sisäenergia kasvaa ja lämpötila nousee. Kokeissa havaitaan, että tarvittava lämpömäärä on suoraan verrannollinen sekä lämpötilan muutokseen että kappaleen massaan: kaksi kertaa suurempi lämpötilan nousu vaatii kaksinkertaisen lämpömäärän, ja kaksinkertainen vesimäärä vaatii kaksinkertaisen lämpömäärän. Lisäksi lämpömäärä riippuu aineesta. Kilogramman veden lämmittäminen yhdellä asteella vaatii noin $4{,}2\,\text{kJ}$, mutta kilogramman raudan lämmittäminen vain noin $0{,}45\,\text{kJ}$. Aineelle ominainen kerroin on ominaislämpökapasiteetti $c$, jonka yksikkö on J/(kg·K). Se kertoo, kuinka paljon energiaa tarvitaan yhden kilogramman lämmittämiseen yhdellä kelvinillä, ja sama määrä vapautuu, kun aine jäähtyy yhden kelvinin.

<figure class="unit-photo"><img src="pics/fy3/steaming-kettle.webp" alt="Vedenkeittimestä kaadetaan kuumaa vettä lasikannuun tummaa taustaa vasten, ja vesi höyryää."><figcaption>Kuumaa vettä kaadetaan vedenkeittimestä. Näkyvä huuru on tiivistyneitä vesipisaroita.</figcaption></figure>

Tärkeä syy on, että veden ominaislämpökapasiteetti on poikkeuksellisen suuri: vesi lämpenee auringossa hitaasti ja jäähtyy illalla hitaasti, kun taas hiekka, jonka $c$ on noin viidesosa veden arvosta, kuumenee samalla energialla moninkertaisesti enemmän. Lisäksi aurinko lämmittää vain hiekan ohutta pintakerrosta, kun taas vedessä lämpeneminen ulottuu syvemmälle. Suuren ominaislämpökapasiteettinsa vuoksi järvet tasaavat rannikon lämpötiloja ja vesi on hyvä lämmönsiirtoaine lämmitysputkissa.

<svg data-fig="water-sand" viewBox="0 0 600 384" role="img" aria-label="Kaavakuva: yhtä suuriin massoihin vettä ja hiekkaa siirtyy sama lämpömäärä Q, mitä kuvaavat yhtä pitkät nuolet. Veden lämpömittarin lukema nousee vähän, hiekan noin viisi kertaa enemmän, koska hiekan ominaislämpökapasiteetti 800 J/(kg·K) on noin viidesosa veden arvosta 4190 J/(kg·K). Lämpötilan nousut on piirretty mittakaavassa ja korostettu punaisella. Hiekkaa on astiassa tilavuutena vähemmän, koska se on tiheämpää kuin vesi." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-6-water-sand.webp" x="0" y="1.2" width="600" height="392.5" preserveAspectRatio="none"/>
  <foreignObject x="221" y="9.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sama } Q \text{ ja sama } m$</div></foreignObject>
  <foreignObject x="216" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="24" y="211.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\Delta T$</div></foreignObject>
  <foreignObject x="163" y="279.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{vesi}$</div></foreignObject>
  <foreignObject x="107" y="317" width="170" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$c = 4190\,\dfrac{\text{J}}{\text{kg}\cdot\text{K}}$</div></foreignObject>
  <foreignObject x="536" y="65.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="307" y="168.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\approx 5\,\Delta T$</div></foreignObject>
  <foreignObject x="470.5" y="279.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hiekka}$</div></foreignObject>
  <foreignObject x="427" y="317" width="170" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$c = 800\,\dfrac{\text{J}}{\text{kg}\cdot\text{K}}$</div></foreignObject>
</svg>

```pysahdy
Samaan määrään vettä ja hiekkaa siirtyy yhtä paljon energiaa, ja massat ovat yhtä suuret. Kumpi lämpenee enemmän, ja miksi?
---
Hiekka. Sen ominaislämpökapasiteetti on noin viidesosa veden arvosta, joten sama energia nostaa sen lämpötilaa noin viisi kertaa enemmän.
```

Kun kuuma ja kylmä kappale laitetaan yhteen eristettyyn astiaan, lämpöä siirtyy kuumemmasta kylmempään, kunnes molemmilla on sama lämpötila. Tätä tilaa sanotaan lämpötasapainoksi. Energia säilyy: kuuman kappaleen luovuttama lämpömäärä on yhtä suuri kuin kylmän vastaanottama. Eristettyä astiaa, jossa tämä mitataan, sanotaan kalorimetriksi, ja mittausta kalorimetriseksi mittaukseksi. Sillä voidaan määrittää tuntemattoman aineen ominaislämpökapasiteetti, kun veden ominaislämpökapasiteetti tunnetaan.

<svg data-fig="calorimeter" viewBox="0 0 600 432" role="img" aria-label="Kalorimetri ennen ja jälkeen lämpötasapainon, periaatekuva, ei mittakaavassa. Ennen: eristetyssä astiassa on 0,300 kg vettä 20,0 °C:ssa ja sen yläpuolella langasta roikkuu 0,200 kg:n metallikappale 100,0 °C:ssa. Jälkeen: kappale on vedessä, ja sekä vesi että kappale ovat lämpötilassa 24,5 °C. Metallin luovuttama lämpömäärä on yhtä suuri kuin veden vastaanottama." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-6-calorimeter.webp" x="0" y="0" width="600" height="440" preserveAspectRatio="none"/>
  <foreignObject x="115" y="7.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ennen}$</div></foreignObject>
  <foreignObject x="402.5" y="7.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{jälkeen}$</div></foreignObject>
  <foreignObject x="137" y="77.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$T_\text{m} = 100{,}0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="137" y="107.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m_\text{m} = 0{,}200\,\text{kg}$</div></foreignObject>
  <foreignObject x="50" y="317.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$T_\text{v} = 20{,}0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="50" y="351.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m_\text{v} = 0{,}300\,\text{kg}$</div></foreignObject>
  <foreignObject x="456" y="221.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$Q$</span></div></foreignObject>
  <foreignObject x="350" y="317.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T = 24{,}5\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="340" y="351.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sama } T \text{ kaikkialla}$</div></foreignObject>
  <foreignObject x="130" y="399.5" width="340" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q_\text{luovutettu} = Q_\text{vastaanotettu}$</div></foreignObject>
</svg>

## Kaava: Lämpömäärä ja lämpötasapaino
Kun aineen olomuoto ei muutu, lämpömäärä, joka tarvitaan massan $m$ lämmittämiseen tai joka vapautuu sen jäähtyessä, on
```kaavat
siirtynyt lämpömäärä :: Q = c m \Delta T
\Delta T = T_\text{loppu} - T_\text{alku}
```
missä $Q$ on lämpömäärä (J), $c$ aineen ominaislämpökapasiteetti (J/(kg·K)), $m$ massa (kg) ja $\Delta T$ lämpötilan muutos (K) eli loppulämpötila $T_\text{loppu}$ miinus alkulämpötila $T_\text{alku}$. Lämpötilan muutos on sama kelvineinä ja celsiusasteina, joten $\Delta T$ voidaan laskea suoraan celsiuslämpötiloista. Lämmetessä $\Delta T$ ja $Q$ ovat positiivisia, jäähtyessä negatiivisia.

Koko kappaleen lämpökapasiteetti
```kaavat
lämpökapasiteetti :: C = c m
```
kertoo, kuinka monta joulea kappaleen lämpötilan nostaminen yhdellä kelvinillä vaatii. $C$ on lämpökapasiteetti (J/K), $c$ ominaislämpökapasiteetti ja $m$ massa. Kappale, jonka lämpökapasiteetti on suuri, lämpenee ja jäähtyy hitaasti.

```pysahdy
Kappaleen lämpökapasiteetti on $C = 300\,\text{J/K}$. Kuinka paljon energiaa tarvitaan sen lämmittämiseen $4{,}0\,\text{K}$?
---
Lämpökapasiteetti kertoo energian yhtä kelviniä kohti, joten tarvitaan $300\,\text{J/K} \cdot 4{,}0\,\text{K} = 1200\,\text{J}$.
```

Eristetyssä astiassa energia säilyy, kun astian omaa lämpökapasiteettia ei oteta huomioon. Kuuman kappaleen $1$ luovuttama lämpömäärä on yhtä suuri kuin kylmän kappaleen $2$ vastaanottama:
```latex
Q_\text{luovutettu} = Q_\text{vastaanotettu}
```
Kun kummallekin kappaleelle pätee $Q = c m \Delta T$, tämä on
```latex
c_1 m_1 (T_1 - T) = c_2 m_2 (T - T_2)
```
missä $T_1$ ja $T_2$ ovat kappaleiden alkulämpötilat ja $T$ yhteinen loppulämpötila eli tasapainolämpötila. Yhtälön molemmat puolet ovat positiivisia lämpömääriä: kuumalle kappaleelle lasketaan alkulämpötila miinus loppulämpötila, kylmälle loppulämpötila miinus alkulämpötila. Yhtälöstä voidaan ratkaista mikä tahansa suure, kun muut tunnetaan: loppulämpötila, massa tai tuntematon ominaislämpökapasiteetti.


Tasapainolämpötila $T$ esiintyy yhtälössä kahdessa termissä. Se ratkaistaan kertomalla sulut auki, keräämällä $T$:tä sisältävät termit samalle puolelle ja ottamalla $T$ yhteiseksi tekijäksi:
```latex
\begin{aligned}
&c_1 m_1 T_1 - c_1 m_1 T \\
&\quad = c_2 m_2 T - c_2 m_2 T_2 \\[6pt]
&c_1 m_1 T_1 + c_2 m_2 T_2 \\
&\quad = c_1 m_1 T + c_2 m_2 T \\
&\quad = (c_1 m_1 + c_2 m_2)\,T
\end{aligned}
```
Kun yhtälö jaetaan puolittain summalla $c_1 m_1 + c_2 m_2$, saadaan
```latex
T = \frac{c_1 m_1 T_1 + c_2 m_2 T_2}{c_1 m_1 + c_2 m_2}
```
Tasapainolämpötila on siis alkulämpötilojen painotettu keskiarvo, jossa painoina ovat kappaleiden lämpökapasiteetit $c_1 m_1$ ja $c_2 m_2$. Tavallinen keskiarvo saadaan vain, kun lämpökapasiteetit ovat yhtä suuret.

```pysahdy
Eristetyssä astiassa sekoitetaan yhtä suuret massat samaa nestettä, joiden lämpötilat ovat $20\,{}^\circ\text{C}$ ja $60\,{}^\circ\text{C}$. Mikä on tasapainolämpötila?
---
Lämpökapasiteetit ovat yhtä suuret, joten tasapainolämpötila on tavallinen keskiarvo: $(20\,{}^\circ\text{C} + 60\,{}^\circ\text{C})/2 = 40\,{}^\circ\text{C}$.
```

| Aine | $c$ (J/(kg·K)) |
| --- | --- |
| vesi | 4190 |
| jää | 2100 |
| alumiini | 900 |
| hiekka | 800 |
| rauta | 450 |
| kupari | 385 |

<svg data-fig="c-bars" viewBox="0 0 600 350" role="img" aria-label="Vaakapylväskaavio ominaislämpökapasiteeteista yksikössä J/(kg·K): vesi 4190, jää 2100, alumiini 900, hiekka 800, rauta 450 ja kupari 385. Pylväiden pituudet ovat mittakaavassa: veden pylväs on noin viisi kertaa hiekan pylvään pituinen." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-6-c-bars.webp" x="0" y="-1.2" width="600" height="360" preserveAspectRatio="none"/>
  <foreignObject x="130" y="9.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$c\ \left(\text{J/(kg}\cdot\text{K)}\right)$</div></foreignObject>
  <foreignObject x="62" y="51.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{vesi}$</div></foreignObject>
  <foreignObject x="529" y="51.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$4190$</div></foreignObject>
  <foreignObject x="75" y="93.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{jää}$</div></foreignObject>
  <foreignObject x="334" y="93.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2100$</div></foreignObject>
  <foreignObject x="12" y="135.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{alumiini}$</div></foreignObject>
  <foreignObject x="222" y="135.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$900$</div></foreignObject>
  <foreignObject x="37" y="177.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{hiekka}$</div></foreignObject>
  <foreignObject x="212.5" y="177.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$800$</div></foreignObject>
  <foreignObject x="50" y="219.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{rauta}$</div></foreignObject>
  <foreignObject x="180" y="219.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$450$</div></foreignObject>
  <foreignObject x="37" y="261.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{kupari}$</div></foreignObject>
  <foreignObject x="174" y="261.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$385$</div></foreignObject>
  <foreignObject x="120" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="194.5" y="315.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1000$</div></foreignObject>
  <foreignObject x="287.5" y="315.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$2000$</div></foreignObject>
  <foreignObject x="381" y="315.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$3000$</div></foreignObject>
  <foreignObject x="474.5" y="315.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$4000$</div></foreignObject>
</svg>

## Esimerkki
Kalorimetrissä on $0{,}300\,\text{kg}$ vettä, jonka lämpötila on $20{,}0\,{}^\circ\text{C}$. Siihen upotetaan $0{,}200\,\text{kg}$:n metallikappale, joka on kuumennettu kiehuvassa vedessä $100{,}0\,{}^\circ\text{C}$:n lämpötilaan. Sekoituksen jälkeen lämpötila asettuu arvoon $24{,}5\,{}^\circ\text{C}$. Mikä on metallin ominaislämpökapasiteetti? Kalorimetrin oma lämpökapasiteetti ja lämpöhäviöt ympäristöön jätetään huomiotta.

<!-- vaihe -->

**Tunnetut ja kysytty.** Vesi: $m_\text{v} = 0{,}300\,\text{kg}$, $T_\text{v} = 20{,}0\,{}^\circ\text{C}$ ja taulukosta $c_\text{v} = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$.

Metalli: $m_\text{m} = 0{,}200\,\text{kg}$, $T_\text{m} = 100{,}0\,{}^\circ\text{C}$. Tasapainolämpötila $T = 24{,}5\,{}^\circ\text{C}$.

Kysytään metallin ominaislämpökapasiteettia $c_\text{m}$.

<!-- vaihe -->

**Periaate.** Energia säilyy. Kun kalorimetri ja ilma eivät ota lämpöä, metallin luovuttama lämpömäärä on yhtä suuri kuin veden vastaanottama. Kumpikin vain lämpenee tai jäähtyy eikä olomuoto muutu, joten kummallekin pätee $Q = c m \Delta T$. Lopussa molemmat ovat samassa lämpötilassa $T$.

<!-- vaihe -->

**Kaava ratkaistuna.** Metallin luovuttama lämpömäärä $Q_\text{m}$ on yhtä suuri kuin veden vastaanottama lämpömäärä $Q_\text{v}$. Kirjoitetaan se auki ja ratkaistaan $c_\text{m}$:
```latex
\begin{aligned}
&Q_\text{m} = Q_\text{v} \\[6pt]
&c_\text{m} m_\text{m} (T_\text{m} - T) \\
&\quad = c_\text{v} m_\text{v} (T - T_\text{v}) \\[6pt]
&c_\text{m} = \frac{c_\text{v} m_\text{v} (T - T_\text{v})}{m_\text{m} (T_\text{m} - T)}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Massat ovat jo kilogrammoina. Lämpötilaero on sama kelvineinä ja celsiusasteina, joten metalli jäähtyy $T_\text{m} - T = 75{,}5\,\text{K}$ ja vesi lämpenee $T - T_\text{v} = 4{,}5\,\text{K}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin osoittaja eli veden vastaanottama lämpömäärä $Q_\text{v}$ ja jaetaan se sitten:
```latex
\begin{aligned}
&Q_\text{v} = c_\text{v} m_\text{v} (T - T_\text{v}) \\
&= 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 0{,}300\,\text{kg} \cdot 4{,}5\,\text{K} \\
&= 5656{,}5\,\text{J} \\[6pt]
&c_\text{m} = \frac{Q_\text{v}}{m_\text{m} (T_\text{m} - T)} \\
&= \frac{5656{,}5\,\text{J}}{0{,}200\,\text{kg} \cdot 75{,}5\,\text{K}} \\
&= 374{,}6\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Metallin ominaislämpökapasiteetti on noin $3{,}7 \cdot 10^2\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla, koska veden lämpötilan muutos $4{,}5\,\text{K}$ tunnetaan vain kahden numeron tarkkuudella: jos loppulukema olisi $0{,}1\,\text{K}$ suurempi eli $24{,}6\,{}^\circ\text{C}$, tulos olisi $383\,\text{J/(kg}\cdot\text{K)}$.

<!-- vaihe -->

**Järkevyys.** Arvo on lähellä kuparin ominaislämpökapasiteettia $385\,\text{J/(kg}\cdot\text{K)}$, joten kappale on luultavasti kuparia. Häviöttömässä kalorimetrissä $0{,}200\,\text{kg}$:n kuparikappale nostaisi veden $24{,}6\,{}^\circ\text{C}$:seen (kokeile simulaatiossa); mitattu $0{,}1\,\text{K}$ pienempi lukema selittyy lukematarkkuudella tai sillä, että todellisuudessa osa lämmöstä siirtyi myös kalorimetrin astiaan ja ilmaan.

Vesi lämpeni vain $4{,}5\,\text{K}$, vaikka metalli jäähtyi $75{,}5\,\text{K}$: veden lämpökapasiteetti on $C_\text{v} = m_\text{v} c_\text{v} = 0{,}300\,\text{kg} \cdot 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} = 1257\,\tfrac{\text{J}}{\text{K}}$, mikä on paljon enemmän kuin kappaleen lämpökapasiteetti $C_\text{m} = m_\text{m} c_\text{m} = 0{,}200\,\text{kg} \cdot 374{,}6\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \approx 75\,\tfrac{\text{J}}{\text{K}}$.

## Yleinen virhekäsitys
Moni ajattelee, että lämpömäärä ja lämpötila ovat sama asia, tai että samaan lämpötilaan lämmitetyt kappaleet ovat saaneet saman määrän energiaa. Kilon veden ja kilon raudan lämmittäminen $20\,{}^\circ\text{C}$:sta $60\,{}^\circ\text{C}$:seen vaatii vedelle lähes kymmenkertaisen energian. Toinen virhe on laskea tasapainolämpötila keskiarvona. Kun $1{,}0\,\text{kg}$ 80-asteista vettä kaadetaan $3{,}0\,\text{kg}$:aan 20-asteista vettä, veden ominaislämpökapasiteetti $c$ on yhtälön molemmilla puolilla ja supistuu pois:
```latex
\begin{aligned}
&Q_\text{luovutettu} = Q_\text{vastaanotettu} \\[6pt]
&c \cdot 1{,}0\,\text{kg} \cdot (80\,{}^\circ\text{C} - T) \\
&\quad = c \cdot 3{,}0\,\text{kg} \cdot (T - 20\,{}^\circ\text{C}) \\[6pt]
&1{,}0\,\text{kg} \cdot (80\,{}^\circ\text{C} - T) \\
&\quad = 3{,}0\,\text{kg} \cdot (T - 20\,{}^\circ\text{C}) \\[6pt]
&80\,{}^\circ\text{C} - T = 3T - 60\,{}^\circ\text{C} \\
&140\,{}^\circ\text{C} = 4T \\
&T = 35\,{}^\circ\text{C}
\end{aligned}
```
Kuuma vesi on vasemmalla puolella kuten yleisessä yhtälössä. Viimeisen ryhmän ensimmäisellä rivillä yhtälö on jaettu puolittain kilogrammalla ja sulut on kerrottu auki. Lopputulos ei siis ole $50\,{}^\circ\text{C}$ vaan $35\,{}^\circ\text{C}$, koska kylmää vettä on kolme kertaa enemmän kuin kuumaa. Sama tulos saadaan painotetulla keskiarvolla: $$\begin{aligned} &T \\ &= (3{,}0\,\text{kg} \cdot 20\,{}^\circ\text{C} + 1{,}0\,\text{kg} \cdot 80\,{}^\circ\text{C}) \\ &: 4{,}0\,\text{kg} \\ &= 35\,{}^\circ\text{C} \end{aligned}$$.

Kolmas virhe on muuntaa $\Delta T$ kelvineiksi lisäämällä 273: lämpötilan muutos on sama kummallakin asteikolla.

## Tiivistelmä
- Lämpömäärä on verrannollinen massaan ja lämpötilan muutokseen: $Q = c m \Delta T$, kun olomuoto ei muutu. Ominaislämpökapasiteetti $c$ riippuu aineesta, ja vedellä se on suuri, $4190\,\text{J/(kg}\cdot\text{K)}$.
- Lämpökapasiteetti $C = cm$ kertoo, kuinka monta joulea koko kappaleen lämmittäminen yhdellä kelvinillä vaatii.
- Eristetyssä astiassa kuuman luovuttama lämpömäärä on yhtä suuri kuin kylmän vastaanottama: $$\begin{aligned} &c_1 m_1 (T_1 - T) \\ &= c_2 m_2 (T - T_2) \end{aligned}$$. Tasapainolämpötila $T$ ratkaistaan keräämällä $T$:n termit samalle puolelle; se on lämpökapasiteeteilla painotettu keskiarvo eikä yleensä alkulämpötilojen tavallinen keskiarvo.
- Kalorimetrisellä mittauksella määritetään tuntemattoman aineen ominaislämpökapasiteetti veden avulla.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: saunan kiuas. Kuumille kiville heitetään kauhalla vettä, ja kivistä nousee löylyhöyryä. Taustalla on puiset lauteet." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-6-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
