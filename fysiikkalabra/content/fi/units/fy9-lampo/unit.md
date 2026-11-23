# Lämpö ja olomuodon muutokset

> **Miksi** lumen sulattaminen juomavedeksi nuotiolla kestää niin kauan, vaikka lumi on vain vähän pakkasen puolella? Kumpi vie enemmän energiaa: sulattaminen vai sulamisveden kuumentaminen kiehuvaksi?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: aurinkoinen talvipäivä Lapissa. Vasemmalla hirsinen laavu, jonka katolla on lunta. Laavun edessä palaa nuotio kivien keskellä, ja sen päällä riippuu kolmijalasta noessa musta pannu, joka on täynnä lunta. Pannusta nousee höyryä. Nuotion vieressä on sanko lunta. Taustalla on lumisia tuntureita ja kuusia." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-lampo-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

Lämpöopissa on erotettava kolme käsitettä. **Lämpötila** kuvaa hiukkasten lämpöliikkeen voimakkuutta. **Sisäenergia** on hiukkasten liike-energian ja niiden välisten vuorovaikutusten energian summa, joten se riippuu myös aineen määrästä ja olomuodosta. **Lämpö** on energian siirtymistä lämpötilaeron vuoksi: kappaleella on lämpötila ja sisäenergia, mutta ei lämpöä.

Kaikki tunnin tehtävät palautuvat energian säilymiseen. Aineeseen siirtyvä lämpö joko nostaa sen lämpötilaa tai muuttaa sen olomuotoa, ja lämpötilan noustessa aine myös laajenee. Eristetyssä systeemissä kuuman osan luovuttama lämpö on yhtä suuri kuin kylmän osan vastaanottama. Talon lämpötila pysyy vakiona, kun siihen tulee yhtä suuri teho kuin siitä lähtee.

<svg data-fig="kartta" viewBox="0 0 380 784" role="img" aria-label="Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Kysy, mitä aineelle tapahtuu, ja katso, mikä tehtävän tunnusmerkki sopii. Lämpötila muuttuu, olomuoto ei: lämpeneminen, lämpömäärä on ominaislämpökapasiteetti kertaa massa kertaa lämpötilan muutos. Jää sulaa tai vesi jäätyy: sulamislämpö, lämpömäärä on ominaissulamislämpö kertaa massa. Vesi kiehuu tai höyry tiivistyy: höyrystymislämpö, lämpömäärä on ominaishöyrystymislämpö kertaa massa. Eristetty astia, sekoitus: lämpötasapaino, luovutettu lämpömäärä on yhtä suuri kuin vastaanotettu. Kappaleen pituus muuttuu: lämpölaajeneminen, pituus on alkuperäinen pituus kertaa yksi plus pituuden lämpötilakerroin kertaa lämpötilan muutos. Nesteen tilavuus muuttuu: lämpölaajeneminen, tilavuus on alkuperäinen tilavuus kertaa yksi plus tilavuuden lämpötilakerroin kertaa lämpötilan muutos. Lämpö johtuu seinän läpi: U-arvo, teho on U-arvo kertaa pinta-ala kertaa lämpötilaero." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="740" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{mistä tunnistan lain?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{mitä aineelle tapahtuu?}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{lämpötila muuttuu, olomuoto ei}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="176" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{lämpeneminen}$</div></foreignObject>
  <rect x="232" y="142" width="130" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="236" y="144" width="122" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$Q = cm\Delta T$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{jää sulaa tai vesi jäätyy}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="206" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{sulamislämpö}$</div></foreignObject>
  <rect x="262" y="228" width="100" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="266" y="230" width="92" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$Q = sm$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{vesi kiehuu tai höyry tiivistyy}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="206" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{höyrystymislämpö}$</div></foreignObject>
  <rect x="262" y="314" width="100" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="266" y="316" width="92" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$Q = rm$</div></foreignObject>
  <line x1="14" y1="407" x2="30" y2="407" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{eristetty astia, sekoitus}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{lämpötasapaino}$</div></foreignObject>
  <rect x="112" y="430" width="250" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="116" y="432" width="242" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$Q_\text{luovutettu} = Q_\text{vastaanotettu}$</div></foreignObject>
  <line x1="14" y1="523" x2="30" y2="523" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="472" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="482.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kappaleen pituus muuttuu}$</div></foreignObject>
  <line x1="40" y1="512" x2="362" y2="512" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="517" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{lämpölaajeneminen}$</div></foreignObject>
  <rect x="172" y="546" width="190" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="176" y="548" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$l = l_0(1 + \alpha\Delta T)$</div></foreignObject>
  <line x1="14" y1="639" x2="30" y2="639" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="588" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="598.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{nesteen tilavuus muuttuu}$</div></foreignObject>
  <line x1="40" y1="628" x2="362" y2="628" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="633" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{lämpölaajeneminen}$</div></foreignObject>
  <rect x="172" y="662" width="190" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="176" y="664" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$V = V_0(1 + \gamma\Delta T)$</div></foreignObject>
  <line x1="14" y1="740" x2="30" y2="740" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="704" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="714.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{lämpö johtuu seinän läpi}$</div></foreignObject>
  <line x1="40" y1="744" x2="362" y2="744" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="749" width="166" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{U-arvo}$</div></foreignObject>
  <rect x="222" y="748" width="140" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="226" y="750" width="132" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$P = UA\Delta T$</div></foreignObject>
</svg>

Kokeessa seuraa ensin energiaa: mistä se lähtee, mihin se menee ja muuttuuko olomuoto matkalla. Valitse kaava vasta sitten.

## Kaava: Lämpömäärä ja energiatase

### Lämpötila ja sisäenergia

```latex
T = \theta + 273{,}15
```

missä $T$ on lämpötila kelvineinä ($\text{K}$) ja $\theta$ celsiusasteina (${}^\circ\text{C}$). Lämpötilaero on sama kelvineinä ja celsiusasteina, mutta lämpötilojen suhteet lasketaan kelvineinä. Sisäenergiaa muuttavat lämpö ja työ:

```kaavat
lämpöopin 1. pääsääntö :: \Delta U = Q + W
```

missä $\Delta U$ on sisäenergian muutos, $Q$ systeemiin siirtynyt lämpömäärä ja $W$ systeemiin tehty työ, kaikki jouleina. Systeemiin tuleva energia on positiivista. Yhtälö pätee, kun systeemin liike- ja potentiaalienergia eivät muutu.

### Lämpeneminen ja olomuodon muutos

```kaavat
siirtynyt lämpömäärä :: Q = cm\Delta T
```

missä $c$ on ominaislämpökapasiteetti ($\text{J/(kg}\cdot\text{K)}$), $m$ massa ($\text{kg}$) ja $\Delta T$ lämpötilan muutos ($\text{K}$). Kaava pätee vain, kun olomuoto ei muutu. Sulamisessa ja höyrystymisessä

```kaavat
sulamislämpö :: Q = sm
höyrystymislämpö :: Q = rm
```

missä $s$ on ominaissulamislämpö ja $r$ ominaishöyrystymislämpö ($\text{J/kg}$). Puhtaan aineen lämpötila pysyy vakiopaineessa muutoksen ajan vakiona, koska energia kasvattaa hiukkasten vuorovaikutusenergiaa. Sama energia vapautuu jähmettymisessä ja tiivistymisessä. Vedelle $c = 4190\,\text{J/(kg}\cdot\text{K)}$, jäälle $c = 2100\,\text{J/(kg}\cdot\text{K)}$, $s = 334\,\text{kJ/kg}$ ja $r = 2260\,\text{kJ/kg}$.

Tästä saadaan vastaus alun kysymykseen. Kilogramman lumen lämmittäminen $-10\,{}^\circ\text{C}$:sta $0\,{}^\circ\text{C}$:seen vie vain $21\,\text{kJ}$, mutta sen sulattaminen $334\,\text{kJ}$, melkein yhtä paljon kuin sulamisveden kuumentaminen kiehuvaksi, $419\,\text{kJ}$.

<svg data-fig="kayra" viewBox="0 0 600 380" role="img" aria-label="Kuvaaja mittakaavassa: kilogramman lumen lämpötila T celsiusasteina siirretyn energian Q funktiona kilojouleina. Lumi lämpenee −10 asteesta 0 asteeseen, kun energiaa on siirtynyt 21 kJ. Sitten lämpötila pysyy 0 asteessa, kunnes energiaa on siirtynyt 355 kJ: sulamiseen kuluu Q = s m = 334 kJ. Sulamisvesi lämpenee 100 asteeseen, kun energiaa on siirtynyt 774 kJ: tähän kuluu Q = c m ΔT = 419 kJ. Sen jälkeen vesi kiehuu 100 asteessa, ja kuvaaja jatkuu vaakasuorana nuolena, koska höyrystyminen Q = r m vaatisi vielä 2260 kJ." style="max-width:100%;font-size:24px">
  <line x1="138.5" y1="318" x2="138.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="181.5" y1="318" x2="181.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="224" y1="318" x2="224" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="266.5" y1="318" x2="266.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="309.5" y1="318" x2="309.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="352" y1="318" x2="352" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="394.5" y1="318" x2="394.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="437.5" y1="318" x2="437.5" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="318" x2="480" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="301" x2="480" y2="301" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="267" x2="480" y2="267" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="233.5" x2="480" y2="233.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="199.5" x2="480" y2="199.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="165.5" x2="480" y2="165.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="131.5" x2="480" y2="131.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="98" x2="480" y2="98" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="64" x2="480" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="318" x2="494" y2="318" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,318 L493,324 L493,312 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="319" x2="96" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,38 L102,51 L90,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="138.5" y1="318" x2="138.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="181.5" y1="318" x2="181.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="159" y="327.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="224" y1="318" x2="224" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="266.5" y1="318" x2="266.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="244" y="327.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="309.5" y1="318" x2="309.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="352" y1="318" x2="352" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="329.5" y="327.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$600$</div></foreignObject>
  <line x1="394.5" y1="318" x2="394.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="437.5" y1="318" x2="437.5" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="415" y="327.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$800$</div></foreignObject>
  <line x1="480" y1="318" x2="480" y2="325" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="301" x2="96" y2="301" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="286.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-20$</div></foreignObject>
  <line x1="89" y1="267" x2="96" y2="267" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="252.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="89" y1="233.5" x2="96" y2="233.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="219" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="199.5" x2="96" y2="199.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="185" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="89" y1="165.5" x2="96" y2="165.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="151" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="89" y1="131.5" x2="96" y2="131.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="117" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="89" y1="98" x2="96" y2="98" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="83.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="64" x2="96" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="49.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$120$</div></foreignObject>
  <foreignObject x="512" y="303.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q\ (\text{kJ})$</div></foreignObject>
  <foreignObject x="86" y="7.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ ({}^\circ\text{C})$</div></foreignObject>
  <foreignObject x="86" y="327.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="96,284 105,267 247.5,267 426,98 466.5,98" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="466.5" y1="98" x2="472" y2="98" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <path d="M484,98 L471,103.5 L471,92 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <circle cx="96" cy="284" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <circle cx="105" cy="267" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <circle cx="247.5" cy="267" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <circle cx="426" cy="98" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <path d="M105,254 V247 H247.5 V254" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="147" y="178" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = sm$</div></foreignObject>
  <foreignObject x="128.5" y="210.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$= 334\,\text{kJ}$</div></foreignObject>
  <path d="M247.5,273.5 V280.5 H426 V273.5" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="272" y="285" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = cm\Delta T = 419\,\text{kJ}$</div></foreignObject>
  <foreignObject x="422" y="59.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$Q = rm$</div></foreignObject>
</svg>

### Lämpötasapaino

Eristetyssä astiassa energia säilyy:

```latex
Q_\text{luovutettu} = Q_\text{vastaanotettu}
```

Kun jäätä ja vettä sekoitetaan, verrataan ensin, riittääkö lämpö, jonka vesi luovuttaa jäähtyessään $0\,{}^\circ\text{C}$:seen, lämmittämään jään $0\,{}^\circ\text{C}$:seen ja sulattamaan sen. Jos riittää, kaikki jää sulaa ja lopputila on vähintään $0\,{}^\circ\text{C}$. Jos ei riitä, jäätä jää jäljelle ja lämpötila on tasan $0\,{}^\circ\text{C}$. Hyvin kylmä jää voi myös jäädyttää osan vedestä tai kaiken veden.

### Laajeneminen ja lämmön siirtyminen

```kaavat
pituuden lämpölaajeneminen :: l = l_0(1 + \alpha\Delta T)
tilavuuden lämpölaajeneminen :: V = V_0(1 + \gamma\Delta T)
```

missä $\alpha$ ja $\gamma$ ovat pituuden ja tilavuuden lämpötilakertoimet ($1/\text{K}$), $l_0$ ja $V_0$ alkuperäinen pituus ja tilavuus ja $l$ ja $V$ pituus ja tilavuus lämpötilan muutoksen $\Delta T$ jälkeen. Muutokset ovat $\Delta l = \alpha l_0 \Delta T$ ja $\Delta V = \gamma V_0 \Delta T$. Kaavat pätevät kiinteille aineille noin $100\,\text{K}$:n lämpötilan muutokseen asti, ja nesteen $\gamma$ on käyttökelpoinen vain taulukon lämpötilan lähellä. Vesi on poikkeus: sen tiheys on suurin noin $4\,{}^\circ\text{C}$:ssa.

Lämpö siirtyy johtumalla, konvektiona ja säteilynä, nettomääräisesti lämpimämmästä kappaleesta kylmempään. Rakennusosan läpi johtuva teho on

```latex
P = UA\Delta T
```

missä $U$ on U-arvo ($\text{W/(m}^2\cdot\text{K)}$), $A$ pinta-ala ($\text{m}^2$) ja $\Delta T$ sisä- ja ulkolämpötilan ero ($\text{K}$). Kaava pätee, kun lämpötilat pysyvät vakioina.

## Yleisiä virheitä {Virheet}

- **Lämpö ja lämpötila sekaisin.** ”Kahvissa on paljon lämpöä” tarkoittaa fysiikassa sisäenergiaa. Lämpö on energiaa, joka siirtyy.
- **$Q = cm\Delta T$ olomuodon muutoksessa.** Sulamisen aikana lämpötila ei muutu, mutta energiaa kuluu $sm$.
- **Lopputila keskiarvona.** Alkulämpötilat painottuvat lämpökapasiteeteilla $cm$, ja jää tarvitsee lisäksi sulamislämmön.
- **Kelvinit väärässä paikassa.** Lämpötilaeroon ei lisätä lukua $273$, mutta lämpötilojen suhteisiin tarvitaan kelvinit.
- **Reikä pienenee lämmetessä.** Kappale laajenee kuin suurennettu valokuva, joten myös reikä suurenee.
- **Kylmä ”virtaa” sisään.** Energia siirtyy lämpimästä kylmään. Kylmyys ei ole aine eikä energia.
- **Häviöt unohtuvat.** Mittauksessa osa energiasta siirtyy ympäristöön. Mieti aina, kumpaan suuntaan häviö muuttaa tulosta.

## Kertaa tarvittaessa {Kertaa}

- Lämpötila ja kelvinasteikko: [*Termodynaaminen systeemi, tilanmuuttujat ja lämpötila*](fy3-3.html). Sisäenergia ja lämpö: [*Sisäenergia, lämpömäärä ja energian säilyminen*](fy3-5.html).
- Lämpömäärä ja lämpötasapaino: [*Aineen lämpeneminen ja jäähtyminen*](fy3-6.html). Sulaminen ja höyrystyminen: [*Olomuodon muutokset*](fy3-7.html).
- Jää ja vesi samassa astiassa: [*Lämpötasapaino olomuodon muuttuessa*](fy3-14.html). Pituuden ja tilavuuden muutos: [*Lämpölaajeneminen*](fy3-8.html).
- Johtuminen, konvektio, säteily ja U-arvo: [*Lämmön siirtyminen, energiatasapaino ja ilmastonmuutos*](fy3-12.html).
