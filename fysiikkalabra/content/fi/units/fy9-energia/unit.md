# Energia, teho ja hyötysuhde

> **Miksi** sähköauton lataaminen kodin pistorasiasta kestää koko yön, vaikka akkuun mahtuu vähemmän energiaa kuin kymmeneen litraan bensiiniä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvi-ilta. Etualalla punainen omakotitalo, jonka ikkunoista loistaa valoa, ja sen seinän latauslaitteeseen kytketty sähköauto. Talolta lähtee sähköjohto pylväiden kautta kauas järven yli. Järven toisella rannalla on voimalaitos, jonka piipusta ja jäähdytyksestä nousee höyryä, ja sen vieressä kolme tuulivoimalaa." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-energia-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

Kaikki tämän tunnin tehtävät lähtevät samasta periaatteesta: **energia säilyy**. Se muuttuu muodosta toiseen ja siirtyy paikasta toiseen, mutta sitä ei synny eikä katoa. Kun laite ”kuluttaa” energiaa, se muuttaa sitä, ja suurin osa päätyy lopulta lämpönä ympäristöön.

Säilymislaista haarautuu kolme kysymystä, joihin kokeen energiatehtävät palautuvat. **Kuinka nopeasti** energiaa muuttuu? Sen kertoo teho. **Kuinka suuri osa** tulee hyödyksi? Sen kertoo hyötysuhde. **Mistä** energia tulee? Polttoaineen lämpöarvosta, voiman tekemästä työstä tai virtaavasta vedestä, tuulesta ja auringosta.

```pysahdy
Tehtävässä kysytään, kuinka nopeasti energiaa muuttuu ja kuinka suuri osa siitä tulee hyödyksi. Mitkä suureet kertovat nämä?
---
Kuinka nopeasti energiaa muuttuu, kertoo teho. Kuinka suuri osa tulee hyödyksi, kertoo hyötysuhde.
```

<svg data-fig="kartta" viewBox="0 0 380 870" role="img" aria-label="Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Aloita luettelemalla energialajit ja katso, mikä tehtävän tunnusmerkki sopii. Eristetty systeemi: energia säilyy, joten energia alussa on yhtä suuri kuin energia lopussa. Energia ajan kuluessa: teho on energian muutos jaettuna ajalla. Tasainen teho, kesto tiedossa: energia on teho kertaa aika. Kilowattitunteja: muunna jouleiksi, yksi kilowattitunti on 3,6 megajoulea. Hyötyenergia ja otettu energia: hyötysuhde on annettu energia jaettuna otetulla energialla. Monta laitetta peräkkäin: kerro vaiheiden hyötysuhteet keskenään. Polttoaine, lämpöarvo: palamislämpö on lämpöarvo kertaa massa. Voima siirtää matkan: työ on voima kertaa matka." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="826" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{mistä tunnistan lain?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{energialajit ensin, sitten tunnusmerkki}$</div></foreignObject>
  <line x1="14" y1="149" x2="30" y2="149" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{eristetty systeemi}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{energia säilyy}$</div></foreignObject>
  <rect x="142" y="172" width="220" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="146" y="174" width="212" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E_\text{alussa} = E_\text{lopussa}$</div></foreignObject>
  <line x1="14" y1="250" x2="30" y2="250" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="214" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="224.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{energia ajan kuluessa}$</div></foreignObject>
  <line x1="40" y1="254" x2="362" y2="254" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="259" width="176" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{teho}$</div></foreignObject>
  <rect x="232" y="258" width="130" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="236" y="260" width="122" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$P = \Delta E/\Delta t$</div></foreignObject>
  <line x1="14" y1="336" x2="30" y2="336" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="300" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="310.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{tasainen teho, kesto tiedossa}$</div></foreignObject>
  <line x1="40" y1="340" x2="362" y2="340" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="345" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{energia}$</div></foreignObject>
  <rect x="238" y="344" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="346" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$E = Pt$</div></foreignObject>
  <line x1="14" y1="437" x2="30" y2="437" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="386" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="396.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{kilowattitunteja}$</div></foreignObject>
  <line x1="40" y1="426" x2="362" y2="426" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="431" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{muunna jouleiksi}$</div></foreignObject>
  <rect x="172" y="460" width="190" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="176" y="462" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$1\,\text{kWh} = 3{,}6\,\text{MJ}$</div></foreignObject>
  <line x1="14" y1="538" x2="30" y2="538" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="502" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="512.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{hyötyenergia ja otettu energia}$</div></foreignObject>
  <line x1="40" y1="542" x2="362" y2="542" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="547" width="176" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{hyötysuhde}$</div></foreignObject>
  <rect x="232" y="546" width="130" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="236" y="548" width="122" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\eta = W_\text{a}/W_\text{o}$</div></foreignObject>
  <line x1="14" y1="639" x2="30" y2="639" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="588" width="342" height="102" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="598.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{monta laitetta peräkkäin}$</div></foreignObject>
  <line x1="40" y1="628" x2="362" y2="628" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="633" width="314" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{kerro hyötysuhteet}$</div></foreignObject>
  <rect x="212" y="662" width="150" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="216" y="664" width="142" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\eta = \eta_1\eta_2\eta_3$</div></foreignObject>
  <line x1="14" y1="740" x2="30" y2="740" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="704" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="714.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{polttoaine, lämpöarvo}$</div></foreignObject>
  <line x1="40" y1="744" x2="362" y2="744" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="749" width="206" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{palamislämpö}$</div></foreignObject>
  <rect x="262" y="748" width="100" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="266" y="750" width="92" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$Q = Hm$</div></foreignObject>
  <line x1="14" y1="826" x2="30" y2="826" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="790" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="800.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{voima siirtää matkan}$</div></foreignObject>
  <line x1="40" y1="830" x2="362" y2="830" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="835" width="182" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{työ}$</div></foreignObject>
  <rect x="238" y="834" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="836" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$W = Fs$</div></foreignObject>
</svg>

Kokeessa ratkaisu alkaa siitä, että tunnistat, minkä tunnusmerkin tehtävä antaa, ja kirjoitat sen lain ennen lukuja. Energia ja teho ovat eri suureita: kilowatti kertoo vauhdin, kilowattitunti määrän.

Tästä saadaan myös vastaus alun kysymykseen. Kymmenessä litrassa bensiiniä on energiaa noin $7{,}5\,\text{kg} \cdot 43\,\text{MJ/kg} \approx 320\,\text{MJ} \approx 90\,\text{kWh}$, enemmän kuin $40\,\text{kWh}$:n akussa. Lataus kestää silti kauan, koska pistorasian teho on pieni: $40\,\text{kWh} : 2{,}3\,\text{kW} \approx 17\,\text{h}$.

## Kaava: Energia, teho ja hyötysuhde

### Säilyminen ja teho

Eristetyssä systeemissä, johon energiaa ei tule eikä josta sitä lähde, kokonaisenergia pysyy samana:

```latex
E_\text{alussa} = E_\text{lopussa}
```

missä kumpikin puoli on kaikkien energialajien summa, myös sisäenergian. Teho on muuntunut tai siirtynyt energia aikaa kohti:

```kaavat
teho :: P = \frac{\Delta E}{\Delta t}
```

missä $P$ on teho (W), $\Delta E$ energia (J) ja $\Delta t$ aika (s). Epätasaisessa käytössä kaava antaa keskitehon; tasaisella teholla $E = P\,t$. Kilowattitunti on energian yksikkö, ja sen muunnos tehdään sijoittamalla:

```latex
1\,\text{kWh} = 1000\,\text{W} \cdot 3600\,\text{s} = 3{,}6\,\text{MJ}
```

```pysahdy
Onko kilowattitunti tehon vai energian yksikkö, ja kuinka monta joulea se on?
---
Kilowattitunti on energian yksikkö, ja $1\,\text{kWh} = 3{,}6\,\text{MJ}$. Kilowatti puolestaan on tehon yksikkö.
```

### Hyötysuhde ja energiaketju

```kaavat
hyötysuhde :: \eta = \frac{W_\text{a}}{W_\text{o}} = \frac{P_\text{a}}{P_\text{o}}
```

missä $\eta$ on hyötysuhde, $W_\text{a}$ ja $P_\text{a}$ annettu hyötyenergia ja -teho ja $W_\text{o}$ ja $P_\text{o}$ otettu energia ja teho. Tehojen suhde käy, kun laite käy tasaisesti. Energia säilyy, joten $W_\text{o} = W_\text{a} + W_\text{h}$, missä $W_\text{h}$ on häviöt. Hyötysuhde on enintään $100\,\%$; se riippuu siitä, mikä määritellään hyödyksi.

Energiaketjussa on peräkkäisiä vaiheita, ja kunkin vaiheen antama hyötyteho on seuraavan vaiheen ottama teho. Kuvan esimerkkilaitoksessa vaiheita on kolme, ja niiden hyötysuhteet ovat $\eta_1$, $\eta_2$ ja $\eta_3$. Polttoainetehosta $500\,\text{MW}$ tulee sähköksi $198\,\text{MW}$, joten koko laitoksen hyötysuhde on $\eta = \tfrac{198\,\text{MW}}{500\,\text{MW}} \approx 0{,}40$. Kaistojen leveydet ovat mittakaavassa, ja lähtevät kaistat ovat yhteensä yhtä leveät kuin tuleva.

<svg data-fig="ketju" viewBox="0 0 420 476" role="img" aria-label="Energiavirtakuvio mittakaavassa lauhdevoimalaitoksesta. Vasemmalta tulee polttoaineteho 500 MW leveänä harmaana kaistana. Ensimmäisessä vaiheessa, kattilassa, hyötysuhde on 0,90: kaistasta kääntyy alas oranssi häviökaista 50 MW, ja jäljelle jää 450 MW. Toisessa vaiheessa, höyrykierrossa, hyötysuhde on 0,45: alas kääntyy leveä häviökaista 248 MW, ja jäljelle jää 203 MW. Kolmannessa vaiheessa, generaattorissa ja muuntajassa, hyötysuhde on 0,98 ja häviö vain 4 MW. Oikealle lähtee vihreä sähkön kaista, 198 MW eli noin 40 prosenttia polttoainetehosta. Häviöt siirtyvät hukkalämpönä ympäristöön." style="max-width:100%;font-size:20px">
  <image href="pics/fy9/fy9-energia-ketju.webp" x="0" y="0" width="420" height="475.1" preserveAspectRatio="none"/>
  <foreignObject x="57.5" y="8" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\eta_1 = 0{,}90$</div></foreignObject>
  <foreignObject x="157.5" y="8" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\eta_2 = 0{,}45$</div></foreignObject>
  <foreignObject x="257.5" y="8" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\eta_3 = 0{,}98$</div></foreignObject>
  <foreignObject x="23" y="144" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$500\,\text{MW}$</div></foreignObject>
  <foreignObject x="113" y="144" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$450\,\text{MW}$</div></foreignObject>
  <foreignObject x="213" y="80" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$203\,\text{MW}$</div></foreignObject>
  <foreignObject x="342" y="148.5" width="64" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:18px;color:#2b8a3e">$198\,\text{MW}$</div></foreignObject>
  <foreignObject x="351" y="176.5" width="55" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:18px;color:#2b8a3e">$\text{sähkö}$</div></foreignObject>
  <foreignObject x="90" y="324" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$50\,\text{MW}$</div></foreignObject>
  <foreignObject x="213" y="324" width="70" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$248\,\text{MW}$</div></foreignObject>
  <foreignObject x="332" y="292" width="50" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$4\,\text{MW}$</div></foreignObject>
  <foreignObject x="8" y="324" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{häviöt:}$</div></foreignObject>
  <foreignObject x="8" y="376" width="105" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\eta_1\ \text{kattila}$</div></foreignObject>
  <foreignObject x="8" y="404" width="146" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\eta_2\ \text{höyrykierto}$</div></foreignObject>
  <foreignObject x="8" y="432" width="261" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\eta_3\ \text{generaattori ja muuntaja}$</div></foreignObject>
</svg>

```johda
Energiaketjussa on kolme peräkkäistä vaihetta, joiden hyötysuhteet ovat $\eta_1$, $\eta_2$ ja $\eta_3$. Johda koko ketjun hyötysuhde $\eta$ vaiheiden hyötysuhteiden avulla.
---
Koko ketjun hyötysuhde on hyötysuhteen määritelmän mukaan $\eta = \tfrac{P_\text{a}}{P_\text{o}}$, missä $P_\text{o}$ on ensimmäisen vaiheen ottama teho ja $P_\text{a}$ viimeisen vaiheen antama hyötyteho. Merkitään vaiheiden antamia tehoja $P_1$, $P_2$ ja $P_3 = P_\text{a}$. Hyötysuhteesta saadaan kunkin vaiheen antama teho sen ottamasta tehosta, ja vaiheen ottama teho on edellisen vaiheen antama teho:

$$\begin{aligned} P_1 &= \eta_1 P_\text{o} \\ P_2 &= \eta_2 P_1 \\ P_3 &= \eta_3 P_2 \end{aligned}$$

Sijoitetaan tehot peräkkäin:

$$P_\text{a} = P_3 = \eta_3\,\eta_2\,\eta_1\,P_\text{o}$$

Jaetaan otetulla teholla:

$$\eta = \frac{P_\text{a}}{P_\text{o}} = \eta_1\,\eta_2\,\eta_3$$

Hyötysuhteet kerrotaan. Jokainen niistä on alle $1$, joten koko ketjun hyötysuhde on pienempi kuin minkään yksittäisen vaiheen.
```

```pysahdy
Ketjun vaiheiden hyötysuhteet ovat $0{,}90$, $0{,}45$ ja $0{,}98$. Miksi koko ketjun hyötysuhde on pienempi kuin $0{,}45$?
---
Hyötysuhteet kerrotaan keskenään, ja jokainen on alle $1$. Jokainen vaihe pienentää hyötytehoa, joten tulo on pienempi kuin pienin tekijä.
```

### Energian lähteet

Polttoaineesta vapautuva energia ja voiman tekemä työ ovat

```kaavat
palamisessa vapautuva lämpö :: Q = Hm
voiman tekemä työ :: W = Fs
```

missä $Q$ on vapautuva lämpö (J), $H$ lämpöarvo ($\text{MJ/kg}$) ja $m$ palanut massa (kg); $Q = Hm$ pätee, kun polttoaine palaa täydellisesti ja $H$ on sen todellisen kosteuden mukainen lämpöarvo. Työssä $F$ on liikkeen suuntainen vakiovoima (N) ja $s$ matka (m). Tasaisessa nostossa $W = mgh$, missä $g = 9{,}81\,\text{m/s}^2$ ja $h$ nostokorkeus.

## Yleisiä virheitä {Virheet}

- **Teho ja energia sekaisin.** ”Paneelin teho on $1{,}2\,\text{kWh}$” on virhe: teho on kilowatteina, energia kilowattitunteina. Suuritehoinen laite ei kuluta paljon energiaa, jos se on päällä vain hetken.
- **Hyötysuhteet lasketaan yhteen tai vähennetään.** Ketjussa ne kerrotaan, joten koko ketjun hyötysuhde on pienempi kuin heikoimman vaiheen.
- **Väärä nimittäjä.** Häviöprosentti ja hyötysuhde lasketaan aina otetusta energiasta, ei annetusta.
- **Minuutit tunteina.** $30\,\text{min} = 30 \cdot \tfrac{1}{60}\,\text{h} = 0{,}50\,\text{h}$; tehon ja ajan tulo on kilowattitunteja vain, kun aika on tunteina.
- **Häviöt ”katoavat”.** Häviöt ovat energiaa, joka on muuttunut hyödyttömään muotoon, yleensä sisäenergiaksi, joka siirtyy lämpönä ympäristöön.
- **Yhteistuotannon kokonaishyötysuhdetta verrataan sähköhyötysuhteeseen.** Sähkö ja kaukolämpö eivät ole yhtä arvokkaita, joten luvut kertovat eri asioita.

## Kertaa tarvittaessa {Kertaa}

- Energialajit ja säilymislaki: [*Energialajit ja energian säilyminen*](fy2-1.html), ketjut ja etuliitteet: [*Energian muuntuminen ja yksikkö joule*](fy2-2.html).
- Teho ja kilowattitunti: [*Teho*](fy2-3.html). Hyötysuhde ja energiavirtakuvio: [*Hyötysuhde*](fy2-4.html).
- Lämpöarvo: [*Polttoaineet ja lämpöarvo*](fy2-5.html). Tuotantotapojen vertailu: [*Energiantuotantotavat ja niiden vertailu*](fy2-6.html).
- Siirtohäviöt ja varastointi: [*Energian siirtäminen: sähkö ja lämpö*](fy2-7.html). Päästöt: [*Energiantuotanto, ympäristö ja ilmastonmuutos*](fy2-8.html).
- Työ ja nostotyö: [*Työ ja energia*](fy3-2.html). Voimalaitoksen ketju ja yhteistuotanto: [*Energiantuotanto ja voimalaitosten hyötysuhde*](fy3-15.html).
