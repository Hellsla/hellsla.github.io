# Hyötysuhde

> **Miksi** hehkulamppu kuumenee niin, että siihen voi polttaa sormensa, vaikka sen tehtävä on antaa valoa, ja miksi ledilamppu valaisee yhtä kirkkaasti paljon pienemmällä sähkönkulutuksella?

## Ydinajatus
Energia ei katoa, mutta kaikki laitteeseen otettu energia ei muutu siihen muotoon, jota laitteelta halutaan. Hehkulampun tehtävä on valaista, joten sen hyötyenergia on valo. Suurin osa lampun ottamasta sähköenergiasta muuttuu kuitenkin lämmöksi, joka lämmittää lamppua ja ympäristöä mutta ei valaise. Tätä osaa sanotaan häviöiksi. Häviöt eivät ole kadonnutta energiaa vaan energiaa, joka on muuttunut hyödyttömään muotoon, yleensä lämmöksi.

<svg data-fig="lamp" viewBox="0 0 600 350" role="img" aria-label="Energiavirtakuvio mittakaavassa: hehkulamppu ottaa sähköenergiaa 100 J. Sähkö kulkee vasemmalta lampun kuvaan. Oikealle jatkuu ohut vihreä nuoli, valon energia 5 J, ja paksu oranssi nuoli, lämmön energia 95 J. Nuolten paksuudet ovat suhteessa energioihin, joten valon osuus on 5 prosenttia tulevasta energiasta." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy24l-in" gradientUnits="userSpaceOnUse" x1="30" y1="0" x2="292" y2="0"><stop offset="0" stop-color="#e3dccb"/><stop offset="1" stop-color="#c9c2b2"/></linearGradient><linearGradient id="fy24l-ok" gradientUnits="userSpaceOnUse" x1="292" y1="0" x2="550" y2="0"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient><linearGradient id="fy24l-loss" gradientUnits="userSpaceOnUse" x1="292" y1="0" x2="550" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <path d="M30,96 L168,96 L168,88 L190,156.0 L168,224 L168,216 L30,216 Z" fill="url(#fy24l-in)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M292,96 L520,96 L520,88 L550,99.0 L520,110.0 L520,102.0 L292,102.0 Z" fill="url(#fy24l-ok)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M292,102.0 C382,102.0 322,196 422,196 L520,196 L520,188 L550,253.0 L520,318.0 L520,310.0 L422,310.0 C322,310.0 382,216 292,216 Z" fill="url(#fy24l-loss)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="190" y="70" width="102" height="172" rx="12" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="241" cy="110" r="34" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M225,110 L233,96 L241,122 L249,96 L257,110" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round"/>
  <rect x="225" y="144" width="32" height="30" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="225" y1="154" x2="257" y2="154" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="225" y1="164" x2="257" y2="164" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="30" y="13.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{hehkulamppu}$</div></foreignObject>
  <foreignObject x="30" y="55.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{o} = 100\,\text{J}$</div></foreignObject>
  <foreignObject x="30" y="233.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{sähkö}$</div></foreignObject>
  <foreignObject x="297" y="53.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$E_\text{a} = 5\,\text{J}\ (\text{valo})$</div></foreignObject>
  <foreignObject x="287" y="323.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{h} = 95\,\text{J}\ (\text{lämpö})$</div></foreignObject>
  <foreignObject x="186" y="255.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\eta = 5\,\%$</div></foreignObject>
</svg>

Energian kulkua laitteen läpi voi havainnollistaa energiavirtakuviolla eli Sankey-kuviolla. Kuviossa nuolen paksuus on verrannollinen energiaan: tuleva nuoli jakautuu ohueen hyötynuoleen ja paksuun häviönuoleen. Kun lamppu ottaa sähköenergiaa $100\,\text{J}$, valoksi muuttuu vain $5\,\text{J}$ ja loput $95\,\text{J}$ on lämpöä. Lähtevien nuolten paksuudet ovat yhteensä yhtä suuret kuin tulevan nuolen paksuus, koska energia säilyy.

### Häviö määräytyy laitteen tarkoituksesta
Vedenkeittimessä lämpö on hyötyä, kun se lämmittää veden, ja häviötä, kun se karkaa keittimen kyljistä huoneeseen. Hehkulampun lämpö on sen sijaan aina häviötä, vaikka se lämmittäisi huonetta talvella, koska lampun tehtävä on valaista. Hyöty määräytyy siis laitteen tarkoituksesta.

### Hyötysuhde kertoo hyödyn osuuden
Hyötysuhde on hyötyenergian osuus laitteeseen otetusta energiasta. Se on aina alle $100\,\%$, koska osa energiasta muuttuu käytännössä aina lämmöksi esimerkiksi sähkövastuksessa tai kitkassa, ja lämpö leviää ympäristöön, josta sitä on vaikea ottaa talteen. Laitteiden hyötysuhteet vaihtelevat paljon:

| Laite ja sen hyöty | tyypillinen $\eta$ |
| --- | --- |
| hehkulamppu: valo | $5\,\%$ |
| ledilamppu: valo | $30\,\%$ |
| vedenkeitin: veden lämpeneminen | $90\,\%$ |
| sähkömoottori: liike | $90\,\%$ |
| bensiinimoottori: auton liike | $25\,\%$ |
| aurinkopaneeli: sähkö | $20\,\%$ |

Taulukon arvot ovat tyypillisiä pyöristettyjä arvoja, eivät minkään tietyn laitteen mittauksia. Todellinen hyötysuhde riippuu laitteen mallista ja käyttötilanteesta. Bensiinimoottorin arvo on tyypillinen tasaisessa maantieajossa; kaupunkiajossa ja muulla pienellä kuormalla hyötysuhde on selvästi pienempi. Sähkömoottorin hyötysuhde muuttuu vähän, kun se käy lähellä tehoa, jolle se on suunniteltu.

## Kaava: Hyötysuhde
Hyötysuhde $\eta$ (eeta) on hyötyenergian ja laitteeseen otetun energian suhde. Kun laite käy tasaisella teholla, sama suhde saadaan myös tehoista:
```latex
\eta = \frac{E_\text{a}}{E_\text{o}} = \frac{P_\text{a}}{P_\text{o}}
```
missä $\eta$ on hyötysuhde (suhdeluku, usein prosentteina), $E_\text{a}$ laitteen antama hyötyenergia (J), $E_\text{o}$ laitteeseen otettu energia (J), $P_\text{a}$ hyötyteho (W) ja $P_\text{o}$ laitteeseen otettu teho (W). Suhdeluku muutetaan prosenteiksi kertomalla se luvulla $100\,\%$, esimerkiksi $0{,}30 \cdot 100\,\% = 30\,\%$. Kertominen ei muuta lukua, koska $1\,\% = 0{,}01$ ja siis $100\,\% = 100 \cdot 0{,}01 = 1$.

Tehojen suhde on sama kuin energioiden suhde, koska tasaisella teholla energia on teho kerrottuna ajalla (luku *Teho*). Laitteen käydessä aikaa $t$ energiat ovat $E_\text{a} = P_\text{a} \cdot t$ ja $E_\text{o} = P_\text{o} \cdot t$, ja aika supistuu:
```latex
\begin{aligned}
\eta &= \frac{E_\text{a}}{E_\text{o}} \\
&= \frac{P_\text{a} \cdot t}{P_\text{o} \cdot t} \\
&= \frac{P_\text{a}}{P_\text{o}}
\end{aligned}
```
Hyötysuhde ei siis riipu siitä, mitataanko energiaa vai tehoa, eikä käyntiajasta.

### Energian säilyminen ja häviöt
Energian säilyminen jakaa laitteeseen otetun energian hyötyenergiaan ja häviöihin $E_\text{h}$:
```latex
E_\text{o} = E_\text{a} + E_\text{h}
```
Tehoille pätee sama, $P_\text{o} = P_\text{a} + P_\text{h}$. Kun hyötysuhde tunnetaan, hyötyenergia on $E_\text{a} = \eta \cdot E_\text{o}$ ja otettu energia $E_\text{o} = \tfrac{E_\text{a}}{\eta}$.

### Kahden lampun vertailu
Lamppu, jonka hyötysuhde on pieni, tarvitsee saman hyödyn saamiseen suuremman tehon. Valotehoon $3\,\text{W}$ tarvitaan hehkulampulta $60\,\text{W}$ mutta ledilampulta vain $10\,\text{W}$, koska hyötysuhteet ovat $5\,\%$ ja $30\,\%$. Kuviossa nuolten paksuudet ovat samassa mittakaavassa: vihreät valotehon nuolet ovat yhtä paksut, mutta hehkulampun tuleva nuoli on kuusi kertaa paksumpi.

<svg data-fig="pair" viewBox="0 0 600 450" role="img" aria-label="Kaksi energiavirtakuviota samassa mittakaavassa. Ylhäällä hehkulamppu ottaa tehon 60 W ja antaa valotehoa 3 W; hyötysuhde on 5 prosenttia, ja 57 W muuttuu lämmöksi. Alhaalla ledilamppu ottaa tehon 10 W ja antaa saman valotehon 3 W; hyötysuhde on 30 prosenttia, ja 7 W muuttuu lämmöksi. Molemmissa vihreä valoteho-nuoli on yhtä paksu, mutta ledilampun tuleva nuoli on kuudesosa hehkulampun tulevasta nuolesta." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy24a-in" gradientUnits="userSpaceOnUse" x1="30" y1="0" x2="200" y2="0"><stop offset="0" stop-color="#e3dccb"/><stop offset="1" stop-color="#c9c2b2"/></linearGradient><linearGradient id="fy24a-ok" gradientUnits="userSpaceOnUse" x1="200" y1="0" x2="532" y2="0"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient><linearGradient id="fy24a-loss" gradientUnits="userSpaceOnUse" x1="200" y1="0" x2="532" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient><linearGradient id="fy24b-in" gradientUnits="userSpaceOnUse" x1="30" y1="0" x2="200" y2="0"><stop offset="0" stop-color="#e3dccb"/><stop offset="1" stop-color="#c9c2b2"/></linearGradient><linearGradient id="fy24b-ok" gradientUnits="userSpaceOnUse" x1="200" y1="0" x2="532" y2="0"><stop offset="0" stop-color="#b2f2bb"/><stop offset="1" stop-color="#2b8a3e"/></linearGradient><linearGradient id="fy24b-loss" gradientUnits="userSpaceOnUse" x1="200" y1="0" x2="532" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <path d="M30,84 L200,84 L200,180.0 L30,180.0 Z" fill="url(#fy24a-in)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M200,84 L500,84 L500,76 L532,86.4 L500,96.8 L500,88.8 L200,88.8 Z" fill="url(#fy24a-ok)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M200,88.8 C290,88.8 230,124 330,124 L500,124 L500,116 L532,169.6 L500,223.2 L500,215.2 L330,215.2 C230,215.2 290,180.0 200,180.0 Z" fill="url(#fy24a-loss)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="30" y="11.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{hehkulamppu}$</div></foreignObject>
  <foreignObject x="30" y="43.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{o} = 60\,\text{W}$</div></foreignObject>
  <foreignObject x="30" y="195.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\eta = 5\,\%$</div></foreignObject>
  <foreignObject x="257" y="41.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$P_\text{a} = 3\,\text{W}\ (\text{valo})$</div></foreignObject>
  <foreignObject x="247" y="230.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P_\text{h} = 57\,\text{W}\ (\text{lämpö})$</div></foreignObject>
  <line x1="30" y1="268" x2="570" y2="268" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="30" y="281.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ledilamppu}$</div></foreignObject>
  <foreignObject x="30" y="313.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{o} = 10\,\text{W}$</div></foreignObject>
  <path d="M30,352 L200,352 L200,368.0 L30,368.0 Z" fill="url(#fy24b-in)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M200,352 L500,352 L500,344 L532,354.4 L500,364.8 L500,356.8 L200,356.8 Z" fill="url(#fy24b-ok)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M200,356.8 C290,356.8 230,386 330,386 L500,386 L500,378 L532,391.6 L500,405.2 L500,397.2 L330,397.2 C230,397.2 290,368.0 200,368.0 Z" fill="url(#fy24b-loss)" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="257" y="309.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$P_\text{a} = 3\,\text{W}\ (\text{valo})$</div></foreignObject>
  <foreignObject x="30" y="383.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\eta = 30\,\%$</div></foreignObject>
  <foreignObject x="257" y="412.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P_\text{h} = 7\,\text{W}\ (\text{lämpö})$</div></foreignObject>
</svg>

Mittakaavaan piirretyssä kuviossa hyötysuhteen näkee suoraan: se on hyötynuolen paksuuden osuus tulevan nuolen paksuudesta. Jos tuleva nuoli on $5{,}0\,\text{cm}$ ja hyötynuoli $4{,}0\,\text{cm}$ paksu, hyötysuhde on $4{,}0 : 5{,}0 = 0{,}80$ eli $80\,\%$.

## Esimerkki
Vedenkeittimen hyötysuhde on $90\,\%$, ja se ottaa sähköverkosta tehon $2{,}0\,\text{kW}$. Keitin on päällä $3{,}0\,\text{min}$. Kuinka paljon sähköenergiaa muuttuu häviöiksi eli lämmöksi, joka ei lämmitä vettä?

<!-- vaihe -->

**Tunnetut ja kysytty.** Hyötysuhde $\eta = 90\,\%$, otettu teho $P_\text{o} = 2{,}0\,\text{kW}$ ja käyntiaika $t = 3{,}0\,\text{min}$. Kysytään häviöenergiaa $E_\text{h}$.

<!-- vaihe -->

**Periaate.** Keitin käy tasaisella teholla, joten otettu energia on teho kerrottuna ajalla. Hyötysuhde kertoo, kuinka suuri osa otetusta energiasta lämmittää veden. Energia säilyy, joten loput on häviöitä.

<!-- vaihe -->

**Kaava ratkaistuna.** Otettu energia, hyötyenergia ja häviöt saadaan järjestyksessä:
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

**Tulos.** Häviöiksi muuttuu $36\,\text{kJ}$. Tulos annetaan kahdella merkitsevällä numerolla, koska lähtötiedot $90\,\%$, $2{,}0\,\text{kW}$ ja $3{,}0\,\text{min}$ on annettu kahden numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Häviöitä pitää olla $100\,\% - 90\,\% = 10\,\%$ otetusta energiasta, ja $0{,}10 \cdot 360\,\text{kJ} = 36\,\text{kJ}$. Lisäksi hyötyenergia ja häviöt antavat yhteensä otetun energian: $324\,\text{kJ} + 36\,\text{kJ} = 360\,\text{kJ}$.

## Yleinen virhekäsitys
Moni ajattelee, että häviöissä energia katoaa. Energia säilyy kuitenkin kaikissa laitteissa. Hehkulampusta lähtevä energia on yhteensä yhtä suuri kuin siihen tuleva: $3\,\text{W}$ valoa ja $57\,\text{W}$ lämpöä on yhteensä $60\,\text{W}$. Häviö tarkoittaa vain sitä, että osa energiasta päätyi muotoon, josta ei ole hyötyä.

Toinen virhe on pitää suuritehoista laitetta tehokkaana. Hyötysuhde on suhdeluku, ei määrä. $100\,\text{W}$:n hehkulamppu antaa valoa $5\,\text{W}$ ja $60\,\text{W}$:n lamppu $3\,\text{W}$, mutta molempien hyötysuhde on $5\,\%$. Suuritehoinen laite käyttää enemmän energiaa, mutta teho ei kerro, kuinka suuri osa energiasta on hyötyä.

## Tiivistelmä
- Hyötysuhde on hyötyenergian osuus laitteeseen otetusta energiasta: $\eta = \tfrac{E_\text{a}}{E_\text{o}} = \tfrac{P_\text{a}}{P_\text{o}}$. Se ilmoitetaan usein prosentteina ja on aina alle $100\,\%$.
- Energia säilyy: $E_\text{o} = E_\text{a} + E_\text{h}$. Häviöt ovat yleensä lämpöä, joka leviää ympäristöön.
- Energiavirtakuviossa nuolen paksuus on verrannollinen energiaan tai tehoon, ja hyötysuhde on hyötynuolen osuus tulevasta nuolesta.
- Tasaisesti käyvän laitteen hyötysuhde ei riipu käyntiajasta, koska aika supistuu energioiden suhteesta. Käyttötilanne voi muuttaa sitä: esimerkiksi bensiinimoottorin hyötysuhde on pienellä kuormalla selvästi pienempi.
