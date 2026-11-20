# Hyötysuhde

> **Miksi** hehkulamppu kuumenee niin, että siihen voi polttaa sormensa, vaikka sen tehtävä on antaa valoa? Miksi ledilamppu antaa yhtä paljon valoa paljon pienemmällä sähkönkulutuksella?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: illalla huoneessa on pöydän yllä kaksi kattolamppua vierekkäin. Vasemmalla on hehkulamppu. Sen hehkulanka hohtaa, ja lampun ympärillä väreilee lämpöä. Oikealla on ledilamppu. Kummankin lampun valo pöydälle on yhtä kirkas." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-4-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Energia ei katoa. Kaikki laitteeseen otettu energia ei kuitenkaan muutu siihen muotoon, jota laitteelta halutaan. Hehkulampun tehtävä on valaista, joten sen hyötyenergia on valo. Suurin osa lampun ottamasta sähköenergiasta muuttuu lämmöksi. Lämpö lämmittää lamppua ja ympäristöä, mutta se ei valaise. Tätä osaa sanotaan häviöiksi. Häviöt eivät ole kadonnutta energiaa. Ne ovat energiaa, joka on muuttunut hyödyttömään muotoon, yleensä lämmöksi.

<svg data-fig="lamp" viewBox="0 0 600 350" role="img" aria-label="Energiavirtakuvio mittakaavassa: hehkulamppu ottaa sähköenergiaa 100 J. Sähkö kulkee vasemmalta lampun kuvaan. Oikealle jatkuu ohut vihreä nuoli, joka on valon energia 5 J. Oikealle jatkuu myös paksu oranssi nuoli, joka on lämmön energia 95 J. Nuolten paksuudet ovat suhteessa energioihin. Valon osuus on siis 5 prosenttia tulevasta energiasta." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-4-lamp.webp" x="1.2" y="0" width="597" height="358.2" preserveAspectRatio="none"/>
  <foreignObject x="30" y="13.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{hehkulamppu}$</div></foreignObject>
  <foreignObject x="30" y="55.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{o} = 100\,\text{J}$</div></foreignObject>
  <foreignObject x="30" y="233.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{sähkö}$</div></foreignObject>
  <foreignObject x="297" y="53.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$E_\text{a} = 5\,\text{J}\ (\text{valo})$</div></foreignObject>
  <foreignObject x="287" y="323.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{h} = 95\,\text{J}\ (\text{lämpö})$</div></foreignObject>
  <foreignObject x="186" y="255.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\eta = 5\,\%$</div></foreignObject>
</svg>

Energian kulkua laitteen läpi voi havainnollistaa energiavirtakuviolla eli Sankey-kuviolla. Kuviossa nuolen paksuus on verrannollinen energiaan. Tuleva nuoli jakautuu ohueen hyötynuoleen ja paksuun häviönuoleen. Lamppu ottaa sähköenergiaa $100\,\text{J}$. Siitä vain $5\,\text{J}$ muuttuu valoksi, ja loput $95\,\text{J}$ on lämpöä. Lähtevien nuolten paksuudet ovat yhteensä yhtä suuret kuin tulevan nuolen paksuus, koska energia säilyy.

### Häviö määräytyy laitteen tarkoituksesta
Vedenkeittimessä lämpö on hyötyä, kun se lämmittää veden. Lämpö on häviötä, kun se karkaa keittimen kyljistä huoneeseen. Hehkulampun lämpö lasketaan häviöksi. Näin on silloinkin, kun lamppu lämmittää huonetta talvella, koska lampun hyödyksi on määritelty valo. Se, mikä on hyötyä, riippuu siis laitteen tarkoituksesta eli siitä, mihin laitetta käytetään. Hyötysuhteen arvoon vaikuttaa, mikä määritellään hyödyksi ja mitkä osat lasketaan kuuluviksi laitteeseen.

```pysahdy
Sähkölämmittimen tarkoitus on lämmittää huonetta. Onko sen tuottama lämpö hyötyä vai häviötä?
---
Se on hyötyä, koska lämmittimen hyödyksi on määritelty lämpö. Sama lämpö olisi häviötä laitteessa, jonka tarkoitus on esimerkiksi valaista.
```

### Hyötysuhde kertoo hyödyn osuuden
Hyötysuhde on hyötyenergian osuus laitteeseen otetusta energiasta. Hyötysuhde on enintään $100\,\%$, koska energia säilyy. Hyötyä ei voi saada enemmän kuin energiaa otetaan. Todellisissa laitteissa hyötysuhde jää usein alle $100\,\%$. Syy on, että osa otetusta energiasta ei päädy määriteltyyn hyödylliseen käyttötarkoitukseen. Se muuttuu esimerkiksi kitkassa tai johtimissa lämmöksi, ja lämpö leviää ympäristöön. Jos laitteen hyöty on muuta kuin lämpöä, hyötysuhde vaihtelee paljon. Sähkömoottori pääsee noin $90\,\%$:iin, mutta lamppu ja polttomoottori jäävät selvästi alle $100\,\%$:n. Sähkölämmittimessä hyöty on itse lämpö. Käytännössä kaikki sähköenergia muuttuu huonetta lämmittäväksi lämmöksi, joten hyötysuhde on lähes $100\,\%$. Ihanteellisen, häviöttömän laitteen hyötysuhde olisi $100\,\%$. Laitteiden hyötysuhteet vaihtelevat paljon:

| Laite ja sen hyöty | tyypillinen $\eta$ |
| --- | --- |
| hehkulamppu: valo | $5\,\%$ |
| ledilamppu: valo | $30\,\%$ |
| vedenkeitin: veden lämpeneminen | $90\,\%$ |
| sähkömoottori: liike | $90\,\%$ |
| bensiinimoottori: auton liike | $25\,\%$ |
| aurinkopaneeli: sähkö | $20\,\%$ |

Taulukon arvot ovat tyypillisiä pyöristettyjä arvoja. Ne eivät ole minkään tietyn laitteen mittauksia. Todellinen hyötysuhde riippuu laitteen mallista ja käyttötilanteesta. Bensiinimoottorin arvo on tyypillinen tasaisessa maantieajossa. Kaupunkiajossa ja muulla pienellä kuormalla hyötysuhde on selvästi pienempi. Sähkömoottorin hyötysuhde muuttuu vähän, kun moottori käy lähellä tehoa, jolle se on suunniteltu.

```pysahdy
Valmistaja sanoo, että laitteen hyötysuhde on $120\,\%$. Miksi tämä ei voi olla totta?
---
Energia säilyy. Laite ei voi antaa hyötyenergiaa enemmän kuin se ottaa energiaa. Siksi hyötysuhde on enintään $100\,\%$.
```

## Kaava: Hyötysuhde
Hyötysuhde $\eta$ (eeta) on hyötyenergian ja laitteeseen otetun energian suhde. Kun laite käy tasaisella teholla, saman suhteen saa myös tehoista:
```kaavat
hyötysuhde :: \eta = \frac{E_\text{a}}{E_\text{o}} = \frac{P_\text{a}}{P_\text{o}}
```
Tässä $\eta$ on hyötysuhde (suhdeluku, usein prosentteina), $E_\text{a}$ laitteen antama hyötyenergia (J), $E_\text{o}$ laitteeseen otettu energia (J), $P_\text{a}$ hyötyteho (W) ja $P_\text{o}$ laitteeseen otettu teho (W). Suhdeluvun muutat prosenteiksi kertomalla sen luvulla $100\,\%$. Esimerkki: $0{,}30 \cdot 100\,\% = 30\,\%$. Kertominen ei muuta lukua, koska $1\,\% = 0{,}01$ ja siis $100\,\% = 100 \cdot 0{,}01 = 1$.

Tehojen suhde on sama kuin energioiden suhde. Tasaisella teholla energia on nimittäin teho kerrottuna ajalla (luku *Teho: $P = \Delta E/\Delta t$*). Laite käy ajan $t$. Silloin energiat ovat $E_\text{a} = P_\text{a} \cdot t$ ja $E_\text{o} = P_\text{o} \cdot t$, ja aika supistuu:
```latex
\begin{aligned}
\eta &= \frac{E_\text{a}}{E_\text{o}} \\
&= \frac{P_\text{a} \cdot t}{P_\text{o} \cdot t} \\
&= \frac{P_\text{a}}{P_\text{o}}
\end{aligned}
```
Hyötysuhde ei siis riipu siitä, mitataanko energiaa vai tehoa. Se ei riipu myöskään käyntiajasta.

### Energian säilyminen ja häviöt
Energian säilyminen jakaa laitteeseen otetun energian hyötyenergiaan ja häviöihin $E_\text{h}$:
```latex
E_\text{o} = E_\text{a} + E_\text{h}
```
Sama pätee tehoille, $P_\text{o} = P_\text{a} + P_\text{h}$. Kun hyötysuhde tunnetaan, hyötyenergia on $E_\text{a} = \eta \cdot E_\text{o}$. Otettu energia on silloin $E_\text{o} = \tfrac{E_\text{a}}{\eta}$.

```pysahdy
Laite ottaa energiaa $50\,\text{J}$ ja antaa hyötyenergiaa $20\,\text{J}$. Paljonko häviöitä syntyy ja mikä on hyötysuhde?
---
Häviöt ovat $E_\text{h} = 50\,\text{J} - 20\,\text{J} = 30\,\text{J}$.
Hyötysuhde on $20\,\text{J} : 50\,\text{J} = 0{,}40$ eli $40\,\%$.
```

### Kahden lampun vertailu
Lamppu, jonka hyötysuhde on pieni, tarvitsee saman hyödyn saamiseen suuremman tehon. Valotehoon $3\,\text{W}$ hehkulamppu tarvitsee $60\,\text{W}$, mutta ledilamppu vain $10\,\text{W}$. Syy on hyötysuhteissa: ne ovat $5\,\%$ ja $30\,\%$. Kuviossa nuolten paksuudet ovat samassa mittakaavassa. Vihreät valotehon nuolet ovat yhtä paksut. Hehkulampun tuleva nuoli on kuusi kertaa paksumpi.

Tässä yksinkertaisessa mallissa lampun hyödyllinen energia on näkyvän valon säteilyenergia. Käytännössä lampun valaisukykyä kuvaa paremmin valovirta. Valovirta ottaa huomioon, että silmä näkee eri aallonpituudet eri herkästi.

<svg data-fig="pair" viewBox="0 0 600 450" role="img" aria-label="Kaksi energiavirtakuviota samassa mittakaavassa. Ylhäällä hehkulamppu ottaa tehon 60 W ja antaa valotehoa 3 W. Hyötysuhde on 5 prosenttia, ja 57 W muuttuu lämmöksi. Alhaalla ledilamppu ottaa tehon 10 W ja antaa saman valotehon 3 W. Hyötysuhde on 30 prosenttia, ja 7 W muuttuu lämmöksi. Molemmissa vihreä valoteho-nuoli on yhtä paksu. Ledilampun tuleva nuoli on kuudesosa hehkulampun tulevasta nuolesta." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-4-pair.webp" x="0" y="0" width="600" height="455" preserveAspectRatio="none"/>
  <foreignObject x="30" y="11.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{hehkulamppu}$</div></foreignObject>
  <foreignObject x="30" y="43.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{o} = 60\,\text{W}$</div></foreignObject>
  <foreignObject x="30" y="195.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\eta = 5\,\%$</div></foreignObject>
  <foreignObject x="257" y="41.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$P_\text{a} = 3\,\text{W}\ (\text{valo})$</div></foreignObject>
  <foreignObject x="247" y="230.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P_\text{h} = 57\,\text{W}\ (\text{lämpö})$</div></foreignObject>
  <foreignObject x="30" y="281.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ledilamppu}$</div></foreignObject>
  <foreignObject x="30" y="313.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{o} = 10\,\text{W}$</div></foreignObject>
  <foreignObject x="257" y="309.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$P_\text{a} = 3\,\text{W}\ (\text{valo})$</div></foreignObject>
  <foreignObject x="30" y="383.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\eta = 30\,\%$</div></foreignObject>
  <foreignObject x="257" y="412.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P_\text{h} = 7\,\text{W}\ (\text{lämpö})$</div></foreignObject>
</svg>

Mittakaavaan piirretystä kuviosta näkee hyötysuhteen suoraan. Se on hyötynuolen paksuuden osuus tulevan nuolen paksuudesta. Ajatellaan toista kuviota, jossa tuleva nuoli on $5{,}0\,\text{cm}$ ja hyötynuoli $4{,}0\,\text{cm}$ paksu. Silloin hyötysuhde on $4{,}0 : 5{,}0 = 0{,}80$ eli $80\,\%$.

## Esimerkki
Vedenkeittimen hyötysuhde on $90\,\%$. Se ottaa sähköverkosta tehon $2{,}0\,\text{kW}$. Keitin on päällä $3{,}0\,\text{min}$. Kuinka paljon sähköenergiaa muuttuu häviöiksi eli lämmöksi, joka ei lämmitä vettä?

<!-- vaihe -->

**Tunnetut ja kysytty.**

- Hyötysuhde $\eta = 90\,\%$,
- otettu teho $P_\text{o} = 2{,}0\,\text{kW}$ ja
- käyntiaika $t = 3{,}0\,\text{min}$.

Kysytään häviöenergiaa $E_\text{h}$.

<!-- vaihe -->

**Periaate.** Keitin käy tasaisella teholla, joten otettu energia on teho kerrottuna ajalla. Hyötysuhde kertoo, kuinka suuri osa otetusta energiasta lämmittää veden. Energia säilyy, joten loput on häviöitä.

<!-- vaihe -->

**Kaava ratkaistuna.** Otettu energia, hyötyenergia ja häviöt saadaan tässä järjestyksessä:
```latex
\begin{aligned}
E_\text{o} &= P_\text{o} \cdot t \\
E_\text{a} &= \eta \cdot E_\text{o} \\
E_\text{h} &= E_\text{o} - E_\text{a}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Teho watteiksi: $2{,}0\,\text{kW} = 2{,}0 \cdot 1000\,\text{W} = 2000\,\text{W}$. Aika sekunneiksi: $3{,}0\,\text{min} = 3{,}0 \cdot 60\,\text{s} = 180\,\text{s}$. Hyötysuhde luvuksi: $90\,\% = 90 \cdot 0{,}01 = 0{,}90$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
E_\text{o} &= P_\text{o} \cdot t \\
&= 2000\,\text{W} \cdot 180\,\text{s} \\
&= 360\,000\,\text{J} \\[6pt]
E_\text{a} &= \eta \cdot E_\text{o} \\
&= 0{,}90 \cdot 360\,000\,\text{J} \\
&= 324\,000\,\text{J} \\[6pt]
E_\text{h} &= E_\text{o} - E_\text{a} \\
&= 360\,000\,\text{J} - 324\,000\,\text{J} \\
&= 36\,000\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Häviöiksi muuttuu $36\,000\,\text{J} = 36 \cdot 1000\,\text{J} = 36\,\text{kJ}$.

Tulos annetaan kahdella merkitsevällä numerolla. Lähtötiedot $90\,\%$, $2{,}0\,\text{kW}$ ja $3{,}0\,\text{min}$ on nimittäin annettu kahden numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Häviöitä pitää olla $100\,\% - 90\,\% = 10\,\%$ otetusta energiasta. Otettu energia on $360\,000\,\text{J} = 360 \cdot 1000\,\text{J} = 360\,\text{kJ}$, joten $0{,}10 \cdot 360\,\text{kJ} = 36\,\text{kJ}$. Hyötyenergia ja häviöt antavat myös yhteensä otetun energian: $324\,\text{kJ} + 36\,\text{kJ} = 360\,\text{kJ}$.

## Yleinen virhekäsitys
Moni ajattelee, että häviöissä energia katoaa. Energia säilyy kuitenkin kaikissa laitteissa. Hehkulampusta lähtevä energia on yhteensä yhtä suuri kuin siihen tuleva energia: $3\,\text{W}$ valoa ja $57\,\text{W}$ lämpöä on yhteensä $60\,\text{W}$. Häviö tarkoittaa vain sitä, että osa energiasta päätyi muotoon, josta ei ole hyötyä.

Toinen virhe on pitää suuritehoista laitetta tehokkaana. Hyötysuhde on suhdeluku, ei määrä. $100\,\text{W}$:n hehkulamppu antaa valoa $5\,\text{W}$ ja $60\,\text{W}$:n lamppu $3\,\text{W}$. Molempien hyötysuhde on silti $5\,\%$. Suuritehoinen laite käyttää enemmän energiaa. Teho ei kuitenkaan kerro, kuinka suuri osa energiasta on hyötyä.

## Tiivistelmä
- Hyötysuhde on hyötyenergian osuus laitteeseen otetusta energiasta: $\eta = \tfrac{E_\text{a}}{E_\text{o}} = \tfrac{P_\text{a}}{P_\text{o}}$. Se ilmoitetaan usein prosentteina. Se on enintään $100\,\%$. Todellisissa laitteissa se jää usein alle $100\,\%$, koska osa energiasta ei päädy hyötyyn. Sähkölämmittimellä se on lähes $100\,\%$.
- Energia säilyy: $E_\text{o} = E_\text{a} + E_\text{h}$. Häviöt ovat yleensä lämpöä, joka leviää ympäristöön.
- Energiavirtakuviossa nuolen paksuus on verrannollinen energiaan tai tehoon. Hyötysuhde on hyötynuolen osuus tulevasta nuolesta.
- Tasaisesti käyvän laitteen hyötysuhde ei riipu käyntiajasta, koska aika supistuu energioiden suhteesta. Käyttötilanne voi kuitenkin muuttaa sitä. Esimerkiksi bensiinimoottorin hyötysuhde on pienellä kuormalla selvästi pienempi.
