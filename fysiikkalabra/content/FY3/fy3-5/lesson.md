# Sisäenergia, lämpömäärä ja energian säilyminen

> **Miksi** polkupyörän pumppu kuumenee, kun rengasta pumpataan, vaikka pumppua ei lämmitetä millään?

## Ydinajatus
Edellisillä oppitunneilla työ todettiin tavaksi siirtää energiaa, ja Joulen koe näytti, että mekaaninen työ voi lämmittää vettä. Vesi ei kuitenkaan sisällä ”lämpöä”, vaan sisäenergiaa. Systeemin sisäenergia U on sen hiukkasten liike-energian ja hiukkasten välisten vuorovaikutusten energian summa. Mikromallin mukaan lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta, joten kun kaasun tai nesteen lämpötila nousee, sen sisäenergia kasvaa. Sisäenergia riippuu myös aineen määrästä: iso järvi sisältää paljon enemmän sisäenergiaa kuin kuppi kuumaa teetä, vaikka järvi on kylmempi.

Systeemin sisäenergiaa voi muuttaa kahdella tavalla. Ensimmäinen on työ: kun pumpun mäntä puristaa ilmaa, ympäristö tekee kaasuun työtä, ja kaasun sisäenergia kasvaa. Siksi pumppu kuumenee. Toinen on lämpö: kun kaksi eri lämpötilassa olevaa kappaletta koskettavat, energiaa siirtyy itsestään kuumemmasta kylmempään, kunnes lämpötilat ovat samat. Näin siirtynyttä energiaa sanotaan lämmöksi, ja siirtyneen energian määrä on lämpömäärä Q. Lämpö on siis energian siirtymistä, ei aineen ominaisuus: kappaleella on lämpötila ja sisäenergia, mutta ei lämpöä.

Energia säilyy. Kun systeemiin siirtyy energiaa lämpönä tai työnä, sen sisäenergia kasvaa täsmälleen siirtyneen energian verran, ja kun energiaa siirtyy pois, sisäenergia pienenee yhtä paljon. Tämä on termodynamiikan ensimmäinen pääsääntö: energian säilymisen laki kirjoitettuna lämmölle ja työlle. Eristetyssä systeemissä, johon ei siirry energiaa kumpaankaan suuntaan, sisäenergia pysyy vakiona, vaikka energia sen sisällä vaihtaisi muotoa.

## Kaava
Sisäenergian muutos on systeemiin tuodun lämpömäärän ja systeemiin tehdyn työn summa:
```latex
\Delta U = Q + W
```
missä ΔU on sisäenergian muutos (J), Q systeemiin siirtynyt lämpömäärä (J) ja W ympäristön systeemiin tekemä työ (J). Merkit kertovat suunnan: Q on positiivinen, kun lämpöä siirtyy systeemiin, ja negatiivinen, kun sitä siirtyy pois; W on positiivinen, kun ympäristö tekee työtä systeemiin (esimerkiksi puristaa kaasua), ja negatiivinen, kun systeemi tekee työtä ympäristöön (kaasu laajenee ja työntää mäntää). Kaikki termit ovat jouleja, samaa yksikköä kuin työ edellisellä oppitunnilla.

<svg viewBox="0 0 600 300" role="img" aria-label="Energiakaavio: systeemiin tulee lämpömäärä Q ja työ W, ja systeemin sisäenergia muuttuu niiden summan verran" style="max-width:100%;font-family:system-ui,sans-serif;font-size:22px">
  <rect x="200" y="70" width="200" height="160" rx="14" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="3"/>
  <text x="300" y="140" text-anchor="middle" fill="currentColor">systeemi</text>
  <text x="300" y="176" text-anchor="middle" fill="currentColor">ΔU = Q + W</text>
  <line x1="60" y1="110" x2="186" y2="110" stroke="currentColor" stroke-width="4"/>
  <polygon points="200,110 182,100 182,120" fill="currentColor"/>
  <text x="120" y="98" text-anchor="middle" fill="currentColor">lämpö Q</text>
  <line x1="60" y1="190" x2="186" y2="190" stroke="currentColor" stroke-width="4"/>
  <polygon points="200,190 182,180 182,200" fill="currentColor"/>
  <text x="120" y="222" text-anchor="middle" fill="currentColor">työ W</text>
  <line x1="414" y1="150" x2="530" y2="150" stroke="currentColor" stroke-width="4" stroke-dasharray="8 6"/>
  <polygon points="546,150 528,140 528,160" fill="currentColor"/>
  <text x="478" y="138" text-anchor="middle" fill="currentColor">Q &lt; 0 tai W &lt; 0</text>
  <text x="478" y="186" text-anchor="middle" fill="currentColor">ulos</text>
  <text x="300" y="270" text-anchor="middle" fill="currentColor">sisään positiivinen, ulos negatiivinen</text>
</svg>

## Esimerkki
Pumpun sylinterissä on ilmaa. Mäntää painetaan alas, jolloin ympäristö tekee ilmaan työn 150 J. Samalla kuumenevasta ilmasta siirtyy sylinterin seinien kautta ympäristöön lämpömäärä 40 J. Kuinka paljon ilman sisäenergia muuttuu?

Ilma on systeemi. Ympäristö tekee työtä systeemiin, joten $W = +150\,\text{J}$. Lämpöä siirtyy systeemistä pois, joten $Q = -40\,\text{J}$.

$\Delta U = Q + W = -40\,\text{J} + 150\,\text{J} = 110\,\text{J}$

Ilman sisäenergia kasvaa 110 J, joten sen lämpötila nousee. Jos puristus tehtäisiin niin hitaasti, että kaikki työn tuoma energia ehtisi siirtyä lämpönä pois, olisi Q = −150 J ja ΔU = 0, eikä lämpötila muuttuisi.

## Yleinen virhekäsitys
Arkikielessä sanotaan, että kappaleessa ”on lämpöä” tai että lämpö ”varastoituu”. Fysiikassa lämpö on energian siirtymistä lämpötilaeron vuoksi, ja se, mikä kappaleeseen varastoituu, on sisäenergiaa. Toinen virhe on pitää lämpötilaa ja sisäenergiaa samana asiana: kuuman kipinän lämpötila on tuhansia asteita, mutta sen sisäenergia on pieni, koska siinä on vähän ainetta. Kolmas virhe on ajatella, että sisäenergiaa voi muuttaa vain lämmittämällä. Pumpun ilma kuumenee ilman mitään lämmönlähdettä, koska siihen tehdään työtä.

## Tiivistelmä
- Sisäenergia U on systeemin hiukkasten liike-energian ja hiukkasten välisten vuorovaikutusten energian summa. Se kasvaa, kun lämpötila nousee, ja riippuu myös aineen määrästä.
- Lämpö on energian siirtymistä kuumemmasta kylmempään lämpötilaeron vuoksi; siirtynyt energia on lämpömäärä Q. Kappaleella ei ”ole lämpöä”.
- Sisäenergiaa muuttavat lämpö ja työ: $\Delta U = Q + W$. Sisään siirtyvä energia on positiivista, ulos siirtyvä negatiivista.
- Energia säilyy: tämä on termodynamiikan ensimmäinen pääsääntö. Eristetyn systeemin sisäenergia pysyy vakiona.
