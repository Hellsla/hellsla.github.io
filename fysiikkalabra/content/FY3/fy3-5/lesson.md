# Sisäenergia, lämpömäärä ja energian säilyminen

> **Miksi** polkupyörän pumppu kuumenee, kun rengasta pumpataan, vaikka pumppua ei lämmitetä millään?

## Ydinajatus
Oppitunnilla fy3-2 työ todettiin tavaksi siirtää energiaa, ja Joulen koe näytti, että mekaaninen työ voi lämmittää vettä. Siellä sanottiin arkikielen tapaan, että työ muuttuu lämmöksi, mutta tarkemmin työ kasvattaa veden sisäenergiaa: vesi ei sisällä ”lämpöä”. Systeemin sisäenergia U on sen hiukkasten liike-energian ja hiukkasten välisten vuorovaikutusten energian summa. Mikromallin mukaan lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta, joten kun kaasun tai nesteen lämpötila nousee, sen sisäenergia kasvaa. Sisäenergia riippuu myös aineen määrästä: iso järvi sisältää paljon enemmän sisäenergiaa kuin kuppi kuumaa teetä, vaikka järvi on kylmempi.

Systeemin sisäenergiaa voi muuttaa kahdella tavalla. Ensimmäinen on työ: kun pumpun mäntä puristaa ilmaa, ympäristö tekee kaasuun työtä, ja kaasun sisäenergia kasvaa, koska liikkuva mäntä osuu hiukkasiin kuin maila palloon ja ne kimpoavat nopeampina. Siksi pumppu kuumenee. Toinen on lämpö: kun kaksi eri lämpötilassa olevaa kappaletta koskettavat, energiaa siirtyy itsestään kuumemmasta kylmempään, kunnes lämpötilat ovat samat. Näin siirtynyttä energiaa sanotaan lämmöksi, ja siirtyneen energian määrä on lämpömäärä Q. Lämpö on siis energian siirtymistä, ei aineen ominaisuus: kappaleella on lämpötila ja sisäenergia, mutta ei lämpöä.

<svg viewBox="0 0 600 300" role="img" aria-label="Kaksi tapaa muuttaa sisäenergiaa (kaaviokuva, ei mittakaavassa). Vasemmalla mäntä työntyy sylinteriin ja tekee ilmaan työn W, ja ilman hiukkaset liikkuvat nopeammin. Oikealla kuuma ja kylmä kappale koskettavat, ja lämpömäärä Q siirtyy kuumasta kylmään." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <text x="150" y="36" text-anchor="middle" fill="currentColor">työ</text>
  <line x1="30" y1="84" x2="110" y2="84" stroke="currentColor" stroke-width="4"/>
  <polygon points="126,84 108,74 108,94" fill="currentColor"/>
  <foreignObject x="140" y="62" width="120" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$W \gt 0$</div></foreignObject>
  <path d="M60,116 H250 V232 H60" fill="none" stroke="currentColor" stroke-width="3"/>
  <rect x="96" y="118" width="16" height="112" fill="currentColor" fill-opacity="0.6"/>
  <line x1="30" y1="174" x2="96" y2="174" stroke="currentColor" stroke-width="6"/>
  <g fill="currentColor" stroke="currentColor" stroke-width="2">
    <circle cx="140" cy="144" r="6"/><line x1="146" y1="144" x2="170" y2="138"/>
    <circle cx="200" cy="140" r="6"/><line x1="206" y1="142" x2="230" y2="152"/>
    <circle cx="228" cy="190" r="6"/><line x1="222" y1="194" x2="200" y2="206"/>
    <circle cx="160" cy="200" r="6"/><line x1="166" y1="198" x2="188" y2="180"/>
    <circle cx="132" cy="178" r="6"/><line x1="138" y1="180" x2="160" y2="168"/>
    <circle cx="196" cy="218" r="6"/><line x1="190" y1="216" x2="168" y2="222"/>
  </g>
  <text x="155" y="276" text-anchor="middle" fill="currentColor">ilma kuumenee</text>
  <line x1="300" y1="20" x2="300" y2="285" stroke="currentColor" stroke-width="2" stroke-dasharray="6 6" stroke-opacity="0.5"/>
  <text x="450" y="36" text-anchor="middle" fill="currentColor">lämpö</text>
  <line x1="400" y1="84" x2="486" y2="84" stroke="currentColor" stroke-width="4"/>
  <polygon points="502,84 484,74 484,94" fill="currentColor"/>
  <foreignObject x="512" y="62" width="60" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$Q$</div></foreignObject>
  <rect x="330" y="116" width="120" height="116" fill="currentColor" fill-opacity="0.3" stroke="currentColor" stroke-width="3"/>
  <rect x="450" y="116" width="120" height="116" fill="currentColor" fill-opacity="0.05" stroke="currentColor" stroke-width="3"/>
  <text x="390" y="182" text-anchor="middle" fill="currentColor">kuuma</text>
  <text x="510" y="182" text-anchor="middle" fill="currentColor">kylmä</text>
  <text x="450" y="276" text-anchor="middle" fill="currentColor">kuumasta kylmään</text>
</svg>

Energia säilyy. Kun systeemiin siirtyy energiaa lämpönä tai työnä, sen sisäenergia kasvaa täsmälleen siirtyneen energian verran, ja kun energiaa siirtyy pois, sisäenergia pienenee yhtä paljon. Tämä on termodynamiikan ensimmäinen pääsääntö: energian säilymisen laki kirjoitettuna lämmölle ja työlle. Eristetty systeemi on suljettu systeemi, johon tai josta ei myöskään siirry energiaa lämpönä eikä työnä. Sen kokonaisenergia pysyy vakiona, vaikka energia sen sisällä vaihtaisi muotoa.

## Kaava
Sisäenergian muutos on systeemiin tuodun lämpömäärän ja systeemiin tehdyn työn summa:
```latex
\Delta U = Q + W
```
missä ΔU on sisäenergian muutos (J), Q systeemiin siirtynyt lämpömäärä (J) ja W ympäristön systeemiin tekemä työ (J). Merkit kertovat suunnan: Q on positiivinen, kun lämpöä siirtyy systeemiin, ja negatiivinen, kun sitä siirtyy pois; W on positiivinen, kun ympäristö tekee työtä systeemiin (esimerkiksi puristaa kaasua), ja negatiivinen, kun systeemi tekee työtä ympäristöön (kaasu laajenee ja työntää mäntää). Kaikki termit ovat jouleja, samaa yksikköä kuin työ oppitunnilla fy3-2, ja männän kaasuun tekemä työ lasketaan samoin kuin siellä, voiman ja matkan tulona.

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
  <text x="414" y="138" text-anchor="start" fill="currentColor">Q &lt; 0 tai W &lt; 0</text>
  <text x="478" y="186" text-anchor="middle" fill="currentColor">ulos</text>
  <text x="300" y="270" text-anchor="middle" fill="currentColor">sisään positiivinen, ulos negatiivinen</text>
</svg>

## Esimerkki
Pumpun sylinterissä on ilmaa. Mäntää painetaan alas, jolloin ympäristö tekee ilmaan työn 150 J. Samalla kuumenevasta ilmasta siirtyy sylinterin seinien kautta ympäristöön lämpömäärä 40 J. Kuinka paljon ilman sisäenergia muuttuu?

<!-- vaihe -->

**Tunnetut ja kysytty.** Ilma on systeemi. Ympäristö tekee työtä systeemiin, joten $W = +150\,\text{J}$. Lämpöä siirtyy systeemistä pois, joten $Q = -40\,\text{J}$. Kysytty on sisäenergian muutos $\Delta U$.

<!-- vaihe -->

**Kaava.** Termodynamiikan ensimmäinen pääsääntö antaa kysytyn suureen suoraan: $\Delta U = Q + W$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan arvot etumerkkeineen:

$$
\begin{aligned}
&\Delta U = Q + W \\
&= -40\,\text{J} + 150\,\text{J} \\
&= 110\,\text{J}
\end{aligned}
$$

<!-- vaihe -->

**Tulos ja järkevyys.** Ilman sisäenergia kasvaa 110 J, joten sen lämpötila nousee. Jos sama 150 J:n työ tehtäisiin niin hitaasti, että kaikki työn tuoma energia ehtisi siirtyä lämpönä pois, olisi Q = −150 J ja ΔU = 0, eikä lämpötila muuttuisi.

## Yleinen virhekäsitys
Arkikielessä sanotaan, että kappaleessa ”on lämpöä” tai että lämpö ”varastoituu”. Fysiikassa lämpö on energian siirtymistä lämpötilaeron vuoksi, ja se, mikä kappaleeseen varastoituu, on sisäenergiaa. Toinen virhe on pitää lämpötilaa ja sisäenergiaa samana asiana: kuuman kipinän lämpötila on tuhansia asteita, mutta sen sisäenergia on pieni, koska siinä on vähän ainetta. Kolmas virhe on ajatella, että sisäenergiaa voi muuttaa vain lämmittämällä. Pumpun ilma kuumenee ilman mitään lämmönlähdettä, koska siihen tehdään työtä.

## Tiivistelmä
- Sisäenergia U on systeemin hiukkasten liike-energian ja hiukkasten välisten vuorovaikutusten energian summa. Se kasvaa, kun lämpötila nousee, ja riippuu myös aineen määrästä.
- Lämpö on energian siirtymistä kuumemmasta kylmempään lämpötilaeron vuoksi; siirtynyt energia on lämpömäärä Q. Kappaleella ei ”ole lämpöä”.
- Sisäenergiaa muuttavat lämpö ja työ: $\Delta U = Q + W$. Sisään siirtyvä energia on positiivista, ulos siirtyvä negatiivista.
- Energia säilyy: tämä on termodynamiikan ensimmäinen pääsääntö. Eristetyn systeemin kokonaisenergia pysyy vakiona.
