# Kaasun tekemä työ ja lämpövoimakone

> **Miksi** lämpövoimalaitos saa polttoaineen energiasta sähköksi vain alle puolet, ja minne loput energiasta menee?

## Ydinajatus
Kun kaasu laajenee ja työntää mäntää, se tekee työtä. Kaasu painaa mäntää voimalla F = pA, missä A on männän pinta-ala. Jos mäntä liikkuu matkan s ja paine pysyy samana, kaasun tekemä työ on oppitunnin fy3-2 tapaan voima kertaa matka: W = Fs = pAs. Tulo As on kaasun tilavuuden muutos ΔV, joten työ on pΔV. (V, p)-kuvaajassa työ on kuvaajan ja V-akselin väliin jäävä pinta-ala, samoin kuin (s, F)-kuvaajassa. Kun kaasua puristetaan, ympäristö tekee työtä kaasuun. Termodynamiikan ensimmäisessä pääsäännössä ΔU = Q + W työ W tarkoittaa ympäristön kaasuun tekemää työtä, joten laajenevalle kaasulle se on −pΔV.

Lämpövoimakone muuttaa lämpöä jatkuvasti työksi. Höyryvoimalaitoksessa vesi kiehuu kattilassa, kuuma höyry laajenee turbiinissa ja pyörittää generaattoria, ja turbiinista tuleva höyry tiivistyy jälleen vedeksi lauhduttimessa, jota merivesi jäähdyttää. Työaine kiertää samaa rataa yhä uudelleen, joten kierroksen lopussa sen sisäenergia on sama kuin alussa. Energia säilyy: koneeseen kuumasta lähteestä tullut lämpö Q₁ on yhtä suuri kuin koneen tekemä työ W ja kylmempään ympäristöön luovutettu lämpö Q₂ yhteensä. Kokemus osoittaa, ettei lämpövoimakone voi muuttaa kaikkea saamaansa lämpöä työksi, vaan osa on aina luovutettava kylmempään ympäristöön. Tämä on termodynamiikan toisen pääsäännön sisältö. Mitä suurempi on kuuman lähteen ja kylmän ympäristön lämpötilaero, sitä suuremman osan lämmöstä kone voi muuttaa työksi.

<svg viewBox="0 0 600 300" role="img" aria-label="Lämpövoimakoneen energiavirrat: kuumasta lähteestä tulee lämpö Q1 koneeseen, kone tekee työn W ja luovuttaa lämmön Q2 kylmempään ympäristöön. Nuolten leveys kuvaa energiaa: Q1 on yhtä leveä kuin W ja Q2 yhteensä." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <rect x="170" y="8" width="260" height="52" rx="10" fill="currentColor" fill-opacity="0.18" stroke="currentColor" stroke-width="2"/>
  <text x="300" y="42" text-anchor="middle" fill="currentColor">kuuma lähde T₁</text>
  <rect x="170" y="240" width="260" height="52" rx="10" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-width="2"/>
  <text x="300" y="274" text-anchor="middle" fill="currentColor">kylmä ympäristö T₂</text>
  <circle cx="300" cy="150" r="46" fill="none" stroke="currentColor" stroke-width="3"/>
  <text x="300" y="158" text-anchor="middle" fill="currentColor">kone</text>
  <rect x="285" y="60" width="30" height="36" fill="currentColor" fill-opacity="0.55"/>
  <polygon points="276,96 324,96 300,106" fill="currentColor" fill-opacity="0.55"/>
  <text x="330" y="90" fill="currentColor">Q₁</text>
  <rect x="291" y="196" width="18" height="34" fill="currentColor" fill-opacity="0.35"/>
  <polygon points="282,230 318,230 300,240" fill="currentColor" fill-opacity="0.35"/>
  <text x="330" y="224" fill="currentColor">Q₂</text>
  <rect x="346" y="144" width="140" height="12" fill="currentColor" fill-opacity="0.8"/>
  <polygon points="486,136 486,164 506,150" fill="currentColor" fill-opacity="0.8"/>
  <text x="514" y="158" fill="currentColor">W</text>
</svg>

Hyötysuhde kertoo, kuinka suuri osa koneeseen tuodusta energiasta saadaan hyödyksi. Suomalainen lauhdevoimalaitos, joka tuottaa vain sähköä, saa polttoaineen energiasta sähköksi noin 40 %, ja ydinvoimalaitos noin 35 %. Loput siirtyvät lauhduttimen kautta mereen. Automoottorin hyötysuhde on noin 30 %, ja loput energiasta poistuu pakokaasujen ja jäähdyttimen mukana. Sähkön ja lämmön yhteistuotannossa lauhduttimesta tuleva lämpö johdetaan kaukolämpöverkkoon kaupungin taloihin, joten polttoaineen energiasta saadaan hyödyksi sähkönä ja lämpönä yhteensä 85–90 %. Tämä vastaa alun kysymykseen: sähköksi saadaan alle puolet, mutta loput eivät katoa, vaan siirtyvät lämpönä ympäristöön tai kaukolämpöverkkoon.

Jäähdytyskone ja lämpöpumppu toimivat päinvastoin kuin lämpövoimakone: ne käyttävät työtä, yleensä sähköä, ja siirtävät sen avulla lämpöä kylmästä paikasta lämpimään. Jääkaappi siirtää lämpöä kaapin sisältä huoneeseen, ja ilmalämpöpumppu ulkoilmasta sisälle. Sisälle luovutettu lämpö on ulkoa otetun lämmön ja käytetyn sähkön summa, joten pumppu voi lämmittää taloa esimerkiksi kolminkertaisella teholla käyttämäänsä sähkötehoon verrattuna. Lukua sanotaan lämpökertoimeksi. Pumppu ei luo energiaa, vaan siirtää sitä.

## Kaava
Kun kaasun paine pysyy vakiona, kaasun tekemä työ on
```latex
W = p\,\Delta V
```
missä W on kaasun tekemä työ (J), p kaasun paine (Pa) ja ΔV kaasun tilavuuden muutos (m³). Työ on positiivinen, kun kaasu laajenee, ja negatiivinen, kun kaasua puristetaan.

Lämpövoimakoneen tekemä työ ja hyötysuhde ovat
```latex
W = Q_1 - Q_2
```
```latex
\eta = \frac{W}{Q_1}
```
missä Q₁ on kuumasta lähteestä koneeseen siirtynyt lämpö (J), Q₂ kylmempään ympäristöön luovutettu lämpö (J), W koneen tekemä työ (J) ja η hyötysuhde, joka ilmoitetaan usein prosentteina. Hyötysuhde voidaan laskea samalla tavalla tehoista, esimerkiksi sähköteho jaettuna polttoaineteholla.

<svg viewBox="0 0 600 300" role="img" aria-label="Paine tilavuuden funktiona vakiopaineessa: vaakasuora jana tilavuudesta V1 tilavuuteen V2. Janan alle jäävä suorakulmio on kaasun tekemä työ p kertaa delta V." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <line x1="70" y1="250" x2="570" y2="250" stroke="currentColor" stroke-width="3"/>
  <line x1="70" y1="250" x2="70" y2="30" stroke="currentColor" stroke-width="3"/>
  <rect x="180" y="110" width="280" height="140" fill="currentColor" fill-opacity="0.2"/>
  <line x1="180" y1="110" x2="452" y2="110" stroke="currentColor" stroke-width="4"/>
  <polygon points="462,110 448,103 448,117" fill="currentColor"/>
  <line x1="70" y1="110" x2="180" y2="110" stroke="currentColor" stroke-width="2" stroke-dasharray="6 5"/>
  <text x="80" y="28" fill="currentColor">p</text>
  <text x="58" y="118" text-anchor="end" fill="currentColor">p</text>
  <text x="570" y="282" text-anchor="end" fill="currentColor">V</text>
  <text x="180" y="282" text-anchor="middle" fill="currentColor">V₁</text>
  <text x="460" y="282" text-anchor="middle" fill="currentColor">V₂</text>
  <text x="320" y="190" text-anchor="middle" fill="currentColor">W = pΔV</text>
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
**Järkevyys.** Sähköä saadaan yhteistuotannossa vähemmän, koska höyry lauhdutetaan korkeammassa lämpötilassa, jotta sen lämpö kelpaa kaukolämmöksi. Polttoaineen energia käytetään silti paljon paremmin hyödyksi, ja kumpikin hyötysuhde jää alle 100 %:n, kuten pitää.

## Yleinen virhekäsitys
Moni ajattelee, että parempi tekniikka voisi tehdä lämpövoimakoneesta lähes täydellisen, niin että kaikki lämpö muuttuisi työksi. Kitkan ja muiden häviöiden vähentäminen auttaa, mutta osa lämmöstä on aina luovutettava kylmempään ympäristöön, joten hyötysuhde jää selvästi alle 100 %:n. Toinen virhe on pitää lämpöpumppua ikiliikkujana, koska se luovuttaa enemmän lämpöä kuin käyttää sähköä. Ylimääräinen lämpö tulee ulkoilmasta, eikä energiaa synny tyhjästä. Kolmas virhe on ajatella, että paineistettu kaasu tekee työtä jo sillä, että sen paine on suuri. Työtä tehdään vain, kun tilavuus muuttuu ja mäntä liikkuu.

## Tiivistelmä
- Vakiopaineessa laajeneva kaasu tekee työn $W = p\,\Delta V$, joka on (V, p)-kuvaajan alle jäävä pinta-ala.
- Lämpövoimakone ottaa lämpöä $Q_1$ kuumasta lähteestä, tekee työn $W$ ja luovuttaa lämmön $Q_2$ kylmempään ympäristöön: $W = Q_1 - Q_2$.
- Hyötysuhde on $\eta = W/Q_1$. Lämpövoimakone ei voi muuttaa kaikkea lämpöä työksi.
- Lauhdevoimalaitoksen hyötysuhde on noin 40 %, mutta sähkön ja lämmön yhteistuotannossa kokonaishyötysuhde on 85–90 %.
- Jäähdytyskone ja lämpöpumppu siirtävät työn avulla lämpöä kylmästä lämpimään. Ne eivät luo energiaa.
