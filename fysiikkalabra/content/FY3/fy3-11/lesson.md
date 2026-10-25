# Kaasun tekemä työ ja lämpövoimakone

> **Miksi** lämpövoimalaitos saa polttoaineen energiasta sähköksi vain alle puolet, ja minne loput energiasta menee?

## Ydinajatus
Kun kaasu laajenee ja työntää mäntää, se tekee työtä. Kaasu painaa mäntää voimalla $F = pA$, missä $A$ on männän pinta-ala. Jos mäntä liikkuu matkan $s$ ja paine pysyy samana, kaasun tekemä työ on oppitunnin fy3-2 tapaan voima kertaa matka: $W = Fs = pAs$. Tulo $As$ on kaasun tilavuuden muutos $\Delta V$, joten työ on $p\,\Delta V$. (V, p)-kuvaajassa työ on kuvaajan ja V-akselin väliin jäävä pinta-ala, samoin kuin (s, F)-kuvaajassa. Kun kaasua puristetaan, ympäristö tekee työtä kaasuun. Termodynamiikan ensimmäisessä pääsäännössä ($\Delta U = Q + W$) työ $W$ tarkoittaa ympäristön kaasuun tekemää työtä, joten laajenevalle kaasulle se on $-p\,\Delta V$.

Lämpövoimakone muuttaa lämpöä jatkuvasti työksi. Höyryvoimalaitoksessa vesi kiehuu kattilassa, kuuma höyry laajenee turbiinissa ja pyörittää generaattoria, ja turbiinista tuleva höyry tiivistyy jälleen vedeksi lauhduttimessa, jota merivesi jäähdyttää. Työaine kiertää samaa rataa yhä uudelleen, joten kierroksen lopussa sen sisäenergia on sama kuin alussa. Energia säilyy: koneeseen kuumasta lähteestä tullut lämpö $Q_1$ on yhtä suuri kuin koneen tekemä työ $W$ ja kylmempään ympäristöön luovutettu lämpö $Q_2$ yhteensä. Kokemus osoittaa, ettei lämpövoimakone voi muuttaa kaikkea saamaansa lämpöä työksi, vaan osa on aina luovutettava kylmempään ympäristöön. Tämä on termodynamiikan toisen pääsäännön sisältö. Mitä suurempi on kuuman lähteen ja kylmän ympäristön lämpötilaero, sitä suuremman osan lämmöstä kone voi muuttaa työksi.

<svg viewBox="0 0 600 300" role="img" aria-label="Lämpövoimakoneen energiavirrat nuolina, joiden leveys kuvaa energiavirtaa eli tehoa: kuumasta lähteestä, jonka lämpötila on T1, tulee koneeseen lämpö Q1. Kone tekee työn W, joka on noin 40 prosenttia Q1:stä, ja luovuttaa loput, lämmön Q2, kylmään ympäristöön, jonka lämpötila on T2. Q1-nuoli on yhtä leveä kuin W- ja Q2-nuolet yhteensä. Kaaviokuva, ei mittakaavassa." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <rect x="150" y="6" width="300" height="54" rx="10" fill="currentColor" fill-opacity="0.22" stroke="currentColor" stroke-width="2"/>
  <text x="268" y="42" text-anchor="middle" fill="currentColor">kuuma lähde</text>
  <foreignObject x="356" y="16" width="70" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$T_1$</div></foreignObject>
  <rect x="150" y="240" width="300" height="54" rx="10" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-width="2"/>
  <text x="262" y="276" text-anchor="middle" fill="currentColor">kylmä ympäristö</text>
  <foreignObject x="362" y="250" width="70" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$T_2$</div></foreignObject>
  <rect x="270" y="60" width="60" height="38" fill="currentColor" fill-opacity="0.55"/>
  <polygon points="260,98 340,98 300,112" fill="currentColor" fill-opacity="0.55"/>
  <foreignObject x="352" y="62" width="70" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$Q_1$</div></foreignObject>
  <circle cx="300" cy="150" r="44" fill="none" stroke="currentColor" stroke-width="3"/>
  <text x="300" y="158" text-anchor="middle" fill="currentColor">kone</text>
  <rect x="344" y="138" width="126" height="24" fill="currentColor" fill-opacity="0.85"/>
  <polygon points="470,128 470,172 496,150" fill="currentColor" fill-opacity="0.85"/>
  <foreignObject x="504" y="134" width="60" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$W$</div></foreignObject>
  <rect x="282" y="194" width="36" height="34" fill="currentColor" fill-opacity="0.3"/>
  <polygon points="272,228 328,228 300,240" fill="currentColor" fill-opacity="0.3"/>
  <foreignObject x="340" y="190" width="70" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$Q_2$</div></foreignObject>
  <text x="20" y="138" fill="currentColor">nuolen leveys</text>
  <text x="20" y="168" fill="currentColor">kuvaa tehoa</text>
</svg>

Hyötysuhde kertoo, kuinka suuri osa koneeseen tuodusta energiasta saadaan hyödyksi. Suomalainen lauhdevoimalaitos, joka tuottaa vain sähköä, saa polttoaineen energiasta sähköksi noin 40 %, ja ydinvoimalaitos noin 35 %. Loput siirtyvät lauhduttimen kautta mereen. Automoottorin hyötysuhde on noin 30 %, ja loput energiasta poistuu pakokaasujen ja jäähdyttimen mukana. Sähkön ja lämmön yhteistuotannossa lauhduttimesta tuleva lämpö johdetaan kaukolämpöverkkoon kaupungin taloihin, joten polttoaineen energiasta saadaan hyödyksi sähkönä ja lämpönä yhteensä 85–90 %. Tämä vastaa alun kysymykseen: sähköksi saadaan alle puolet, mutta loput eivät katoa, vaan siirtyvät lämpönä ympäristöön tai kaukolämpöverkkoon.

Jäähdytyskone ja lämpöpumppu toimivat päinvastoin kuin lämpövoimakone: ne käyttävät työtä, yleensä sähköä, ja siirtävät sen avulla lämpöä kylmästä paikasta lämpimään. Jääkaappi siirtää lämpöä kaapin sisältä huoneeseen, ja ilmalämpöpumppu ulkoilmasta sisälle. Sisälle luovutettu lämpö on ulkoa otetun lämmön ja käytetyn sähkön summa, joten pumppu voi lämmittää taloa esimerkiksi kolminkertaisella teholla käyttämäänsä sähkötehoon verrattuna. Tätä lämpötehon ja sähkötehon suhdetta sanotaan lämpökertoimeksi. Pumppu ei luo energiaa, vaan siirtää sitä.

## Kaava
Kun kaasun paine pysyy vakiona, kaasun tekemä työ on
```latex
W = p\,\Delta V
```
missä $W$ on kaasun tekemä työ (J), $p$ kaasun paine (Pa) ja $\Delta V$ kaasun tilavuuden muutos (m³). Työ on positiivinen, kun kaasu laajenee, ja negatiivinen, kun kaasua puristetaan.

Lämpövoimakoneen tekemä työ ja hyötysuhde ovat
```latex
W = Q_1 - Q_2
```
```latex
\eta = \frac{W}{Q_1}
```
missä $Q_1$ on kuumasta lähteestä koneeseen siirtynyt lämpö (J), $Q_2$ kylmempään ympäristöön luovutettu lämpö (J), $W$ koneen tekemä työ (J) ja $\eta$ hyötysuhde, joka ilmoitetaan usein prosentteina. Hyötysuhde voidaan laskea samalla tavalla tehoista, esimerkiksi sähköteho jaettuna polttoaineteholla.

<svg viewBox="0 0 600 300" role="img" aria-label="(V, p)-kuvaaja vakiopaineessa laajenevasta kaasusta: paine p pysyy vakiona, kun tilavuus kasvaa arvosta V1 arvoon V2, joten kuvaaja on vaakasuora jana, jonka nuoli osoittaa laajenemisen suuntaa. Janan ja V-akselin väliin jäävä varjostettu suorakulmio, jonka leveys on tilavuuden muutos delta V ja korkeus p, on kaasun tekemä työ W = p kertaa delta V. Kaaviokuva." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <rect x="180" y="100" width="280" height="140" fill="currentColor" fill-opacity="0.2"/>
  <line x1="70" y1="240" x2="566" y2="240" stroke="currentColor" stroke-width="3"/>
  <polygon points="578,240 564,233 564,247" fill="currentColor"/>
  <line x1="70" y1="240" x2="70" y2="24" stroke="currentColor" stroke-width="3"/>
  <polygon points="70,12 63,26 77,26" fill="currentColor"/>
  <line x1="70" y1="100" x2="180" y2="100" stroke="currentColor" stroke-width="2" stroke-dasharray="6 5"/>
  <line x1="180" y1="100" x2="460" y2="100" stroke="currentColor" stroke-width="4"/>
  <polygon points="336,100 318,91 318,109" fill="currentColor"/>
  <text x="320" y="84" text-anchor="middle" fill="currentColor">kaasu laajenee</text>
  <line x1="194" y1="214" x2="446" y2="214" stroke="currentColor" stroke-width="2"/>
  <polygon points="184,214 198,207 198,221" fill="currentColor"/>
  <polygon points="456,214 442,207 442,221" fill="currentColor"/>
  <foreignObject x="84" y="4" width="44" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$p$</div></foreignObject>
  <foreignObject x="22" y="78" width="40" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$p$</div></foreignObject>
  <foreignObject x="540" y="248" width="50" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$V$</div></foreignObject>
  <foreignObject x="152" y="248" width="60" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$V_1$</div></foreignObject>
  <foreignObject x="430" y="248" width="60" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$V_2$</div></foreignObject>
  <foreignObject x="225" y="112" width="190" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$W = p\,\Delta V$</div></foreignObject>
  <foreignObject x="285" y="160" width="70" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$\Delta V$</div></foreignObject>
</svg>

## Esimerkki
Biovoimalaitoksen kattilaan syötetään puuhakkeen energiaa teholla 500 MW. Kun laitos tuottaa pelkkää sähköä, sähköteho on 190 MW. Talvella sama laitos toimii yhteistuotantovoimalaitoksena: se tuottaa 150 MW sähköä ja 290 MW kaukolämpöä. Mikä on hyötysuhde kummassakin tapauksessa, ja kuinka suuri teho siirtyy ympäristöön hukkalämpönä?

<!-- vaihe -->
**Tunnetut ja kysytty.** Polttoaineteho $P_1 = 500\,\text{MW}$. Pelkkää sähköä tuotettaessa sähköteho $P_\text{s} = 190\,\text{MW}$; yhteistuotannossa $P_\text{s} = 150\,\text{MW}$ ja kaukolämpöteho $P_\text{k} = 290\,\text{MW}$. Kysytään hyötysuhteita ja hukkalämmön tehoa $P_2$. Hyötysuhde lasketaan tehoista samoin kuin energioista.

<!-- vaihe -->
**Kaavat ratkaistuina.** Hyötysuhde on hyödyksi saatu teho jaettuna syötetyllä teholla, ja energia säilyy, joten hukkalämpö on se osa, joka ei tule hyödyksi:
```latex
\begin{aligned}
\eta &= \frac{P_\text{hyöty}}{P_1} \\
P_2 &= P_1 - P_\text{hyöty}
\end{aligned}
```

<!-- vaihe -->
**Pelkkä sähkö.** Nyt hyödyksi saadaan vain sähkö, $P_\text{hyöty} = P_\text{s}$:
```latex
\begin{aligned}
\eta &= \frac{P_\text{s}}{P_1} \\
&= \frac{190\,\text{MW}}{500\,\text{MW}} \\
&= 0{,}38 = 38\,\% \\
P_2 &= P_1 - P_\text{s} \\
&= 500\,\text{MW} - 190\,\text{MW} \\
&= 310\,\text{MW}
\end{aligned}
```
Hukkalämpö siirtyy lauhduttimen kautta mereen.

<!-- vaihe -->
**Yhteistuotanto.** Hyödyksi saadaan sähkö ja kaukolämpö, $P_\text{hyöty} = P_\text{s} + P_\text{k}$:
```latex
\begin{aligned}
\eta &= \frac{P_\text{s} + P_\text{k}}{P_1} \\
&= \frac{150\,\text{MW} + 290\,\text{MW}}{500\,\text{MW}} \\
&= 0{,}88 = 88\,\% \\
P_2 &= P_1 - (P_\text{s} + P_\text{k}) \\
&= 500\,\text{MW} - 440\,\text{MW} \\
&= 60\,\text{MW}
\end{aligned}
```

<!-- vaihe -->
**Järkevyys.** Sähköä saadaan yhteistuotannossa vähemmän, koska höyry lauhdutetaan korkeammassa lämpötilassa, jotta sen lämpö kelpaa kaukolämmöksi. Polttoaineen energia käytetään silti paljon paremmin hyödyksi, ja kumpikin hyötysuhde jää alle 100 %:n, kuten pitääkin.

## Yleinen virhekäsitys
Moni ajattelee, että parempi tekniikka voisi tehdä lämpövoimakoneesta lähes täydellisen, niin että kaikki lämpö muuttuisi työksi. Kitkan ja muiden häviöiden vähentäminen auttaa, mutta osa lämmöstä on aina luovutettava kylmempään ympäristöön, joten hyötysuhde jää selvästi alle 100 %:n. Toinen virhe on pitää lämpöpumppua ikiliikkujana, koska se luovuttaa enemmän lämpöä kuin käyttää sähköä. Ylimääräinen lämpö tulee ulkoilmasta, eikä energiaa synny tyhjästä. Kolmas virhe on ajatella, että paineistettu kaasu tekee työtä jo sillä, että sen paine on suuri. Työtä tehdään vain, kun tilavuus muuttuu ja mäntä liikkuu.

## Tiivistelmä
- Vakiopaineessa laajeneva kaasu tekee työn $W = p\,\Delta V$, joka on (V, p)-kuvaajan alle jäävä pinta-ala.
- Lämpövoimakone ottaa lämpöä $Q_1$ kuumasta lähteestä, tekee työn $W$ ja luovuttaa lämmön $Q_2$ kylmempään ympäristöön: $W = Q_1 - Q_2$.
- Hyötysuhde on $\eta = W/Q_1$. Lämpövoimakone ei voi muuttaa kaikkea lämpöä työksi.
- Lauhdevoimalaitoksen hyötysuhde on noin 40 %, mutta sähkön ja lämmön yhteistuotannossa kokonaishyötysuhde on 85–90 %.
- Jäähdytyskone ja lämpöpumppu siirtävät työn avulla lämpöä kylmästä lämpimään. Ne eivät luo energiaa.
