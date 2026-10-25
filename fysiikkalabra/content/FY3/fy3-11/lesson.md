# Kaasun tekemä työ ja lämpövoimakone

> **Miksi** lämpövoimalaitos saa polttoaineen energiasta sähköksi vain alle puolet, ja minne loput energiasta menee?

## Ydinajatus
Kun kaasu laajenee ja työntää mäntää, se tekee työtä. Kaasu painaa mäntää voimalla F = pA, missä A on männän pinta-ala. Jos mäntä liikkuu matkan s ja paine pysyy samana, kaasun tekemä työ on oppitunnin fy3-2 tapaan voima kertaa matka: W = Fs = pAs. Tulo As on kaasun tilavuuden muutos ΔV, joten työ on pΔV. (V, p)-kuvaajassa työ on kuvaajan ja V-akselin väliin jäävä pinta-ala, samoin kuin (s, F)-kuvaajassa. Kun kaasua puristetaan, ympäristö tekee työtä kaasuun. Termodynamiikan ensimmäisessä pääsäännössä ΔU = Q + W työ W tarkoittaa ympäristön kaasuun tekemää työtä, joten laajenevalle kaasulle se on −pΔV.

Lämpövoimakone muuttaa lämpöä jatkuvasti työksi. Höyryvoimalaitoksessa vesi kiehuu kattilassa, kuuma höyry laajenee turbiinissa ja pyörittää generaattoria, ja turbiinista tuleva höyry tiivistyy jälleen vedeksi lauhduttimessa, jota merivesi jäähdyttää. Työaine kiertää samaa rataa yhä uudelleen, joten kierroksen lopussa sen sisäenergia on sama kuin alussa. Energia säilyy: koneeseen kuumasta lähteestä tullut lämpö Q₁ on yhtä suuri kuin koneen tekemä työ W ja kylmempään ympäristöön luovutettu lämpö Q₂ yhteensä. Kokemus osoittaa, ettei lämpövoimakone voi muuttaa kaikkea saamaansa lämpöä työksi, vaan osa on aina luovutettava kylmempään ympäristöön. Tämä on termodynamiikan toisen pääsäännön sisältö. Mitä suurempi on kuuman lähteen ja kylmän ympäristön lämpötilaero, sitä suuremman osan lämmöstä kone voi muuttaa työksi.

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

Pelkkää sähköä tuotettaessa hyötysuhde on
```latex
\eta = \frac{190\,\text{MW}}{500\,\text{MW}} = 0{,}38 = 38\,\%
```
ja hukkalämmön teho on $500\,\text{MW} - 190\,\text{MW} = 310\,\text{MW}$, joka siirtyy lauhduttimen kautta mereen.

Yhteistuotannossa hyödyksi saadaan sähköä ja kaukolämpöä yhteensä $150\,\text{MW} + 290\,\text{MW} = 440\,\text{MW}$, joten kokonaishyötysuhde on $440/500 = 0{,}88 = 88\,\%$. Hukkalämpöä on enää 60 MW. Sähköä saadaan vähemmän, koska höyry lauhdutetaan korkeammassa lämpötilassa, jotta sen lämpö kelpaa kaukolämmöksi. Polttoaineen energia käytetään kuitenkin paljon paremmin hyödyksi.

## Yleinen virhekäsitys
Moni ajattelee, että parempi tekniikka voisi tehdä lämpövoimakoneesta lähes täydellisen, niin että kaikki lämpö muuttuisi työksi. Kitkan ja muiden häviöiden vähentäminen auttaa, mutta osa lämmöstä on aina luovutettava kylmempään ympäristöön, joten hyötysuhde jää selvästi alle 100 %:n. Toinen virhe on pitää lämpöpumppua ikiliikkujana, koska se luovuttaa enemmän lämpöä kuin käyttää sähköä. Ylimääräinen lämpö tulee ulkoilmasta, eikä energiaa synny tyhjästä. Kolmas virhe on ajatella, että paineistettu kaasu tekee työtä jo sillä, että sen paine on suuri. Työtä tehdään vain, kun tilavuus muuttuu ja mäntä liikkuu.

## Tiivistelmä
- Vakiopaineessa laajeneva kaasu tekee työn $W = p\,\Delta V$, joka on (V, p)-kuvaajan alle jäävä pinta-ala.
- Lämpövoimakone ottaa lämpöä $Q_1$ kuumasta lähteestä, tekee työn $W$ ja luovuttaa lämmön $Q_2$ kylmempään ympäristöön: $W = Q_1 - Q_2$.
- Hyötysuhde on $\eta = W/Q_1$. Lämpövoimakone ei voi muuttaa kaikkea lämpöä työksi.
- Lauhdevoimalaitoksen hyötysuhde on noin 40 %, mutta sähkön ja lämmön yhteistuotannossa kokonaishyötysuhde on 85–90 %.
- Jäähdytyskone ja lämpöpumppu siirtävät työn avulla lämpöä kylmästä lämpimään. Ne eivät luo energiaa.
