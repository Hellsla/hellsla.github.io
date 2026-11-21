# Sisäenergia, lämpömäärä ja energian säilyminen

> **Miksi** polkupyörän pumppu kuumenee, kun rengasta pumpataan, vaikka pumppua ei lämmitetä millään?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: kädet painavat jalkapumpun kahvaa alas. Letku vie ilman polkupyörän renkaaseen. Pumpun alaosa on lämmennyt, mitä kuvaavat oranssi hehku ja väreilevät viivat." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-5-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Luvussa *Työ ja energia* opit, että työ siirtää energiaa. Joulen koe näytti, että mekaaninen työ voi lämmittää vettä. Painon työ kasvatti veden sisäenergiaa, vaikka vettä ei lämmitetty. Vesi ei sisällä ”lämpöä”.

Systeemin sisäenergia $U$ on kahden energian summa. Ensimmäinen on hiukkasten liike-energia. Toinen on hiukkasten välisten vuorovaikutusten energia. (Systeemi on se kappale tai aine, jota tutkit.) Luvussa *Energialajit ja energian säilyminen* tätä energiaa kutsuttiin lämpöenergiaksi. Tarkempi nimi on sisäenergia. Lämpötila kuvaa hiukkasten lämpöliikkeen voimakkuutta. Kaasussa lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta. Kun aineen lämpötila nousee eikä olomuoto muutu, hiukkasten liike voimistuu ja sisäenergia kasvaa. Lämpötila ja sisäenergia eivät silti ole sama asia. Kun olomuoto muuttuu, sisäenergia muuttuu, vaikka lämpötila pysyy samana. Esimerkiksi puhdas jää sulaa normaalipaineessa. Silloin sisäenergia kasvaa, mutta lämpötila pysyy $0\,{}^\circ\text{C}$:ssa. Sisäenergia riippuu myös aineen määrästä. Iso järvi sisältää paljon enemmän sisäenergiaa kuin kuppi kuumaa teetä, vaikka järvi on kylmempi.

```pysahdy
Puhdas jää sulaa normaalipaineessa. Mitä sen sisäenergialle ja lämpötilalle tapahtuu?
---
Sisäenergia kasvaa. Lämpötila pysyy $0\,{}^\circ\text{C}$:ssa. Lämpötila ja sisäenergia eivät ole sama asia.
```

Systeemin sisäenergiaa voi muuttaa kahdella tavalla.

Ensimmäinen tapa on työ. Pumpun mäntä puristaa ilmaa. Silloin ympäristö tekee kaasuun työtä, ja kaasun sisäenergia kasvaa. Liikkuva mäntä osuu hiukkasiin kuin maila palloon, ja hiukkaset kimpoavat nopeampina. Simulaatiossa tämän näkee hiukkastasolla. Siksi pumppu kuumenee.

Toinen tapa on lämpö. Kaksi eri lämpötilassa olevaa kappaletta koskettaa toisiaan. Silloin energiaa siirtyy itsestään kuumemmasta kylmempään, kunnes lämpötilat ovat samat. Näin siirtynyttä energiaa sanotaan lämmöksi. Siirtyneen energian määrä on lämpömäärä $Q$. Lämpö on siis energian siirtymistä, ei aineen ominaisuus. Kappaleella on lämpötila ja sisäenergia, mutta sillä ei ole lämpöä.

<svg data-fig="two-ways" viewBox="0 0 600 316" role="img" aria-label="Kaksi tapaa muuttaa sisäenergiaa (kaaviokuva, ei mittakaavassa). Vasemmalla mäntä työntyy sylinteriin ja tekee ilmaan työn W. Ilman hiukkaset liikkuvat nopeammin. Oikealla kuuma ja kylmä kappale koskettavat toisiaan. Lämpömäärä Q siirtyy kuumasta kylmään." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-5-two-ways.webp" x="0" y="0" width="600" height="327.5" preserveAspectRatio="none"/>
  <foreignObject x="137.5" y="13.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{työ}$</div></foreignObject>
  <foreignObject x="415" y="13.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpö}$</div></foreignObject>
  <foreignObject x="50" y="113.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W$</div></foreignObject>
  <foreignObject x="96" y="261.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ilma kuumenee}$</div></foreignObject>
  <foreignObject x="347" y="159.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kuuma}$</div></foreignObject>
  <foreignObject x="467" y="159.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kylmä}$</div></foreignObject>
  <foreignObject x="432" y="43.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="344.5" y="261.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kuumasta kylmään}$</div></foreignObject>
</svg>

```pysahdy
Joku sanoo, että kuumassa teekupissa on paljon lämpöä. Onko väite fysiikan kannalta oikein?
---
Ei ole. Kupissa on sisäenergiaa. Lämpö on energian siirtymistä kuumemmasta kylmempään. Kappaleella ei ole lämpöä.
```

Energia säilyy. Oletetaan, että systeemin liike- ja potentiaalienergia eivät muutu. Kun systeemiin siirtyy energiaa lämpönä tai työnä, sen sisäenergia kasvaa täsmälleen siirtyneen energian verran. Kun energiaa siirtyy pois, sisäenergia pienenee yhtä paljon. Tämä on termodynamiikan ensimmäinen pääsääntö. Se on energian säilymisen laki kirjoitettuna lämmölle ja työlle.

Eristetty systeemi on suljettu systeemi. Siihen ei siirry energiaa lämpönä eikä työnä, eikä siitä siirry pois. Sen kokonaisenergia pysyy vakiona. Energia voi silti vaihtaa muotoa systeemin sisällä.

<figure class="unit-photo"><img src="pics/fy3/glowing-metal-furnace.webp" alt="Uunin aukosta näkyy oranssina hehkuva metallipala."><figcaption>Kuuma metalli hehkuu uunissa. Kun metallia kuumennetaan, sen sisäenergia kasvaa.</figcaption></figure>

## Kaava: Termodynamiikan ensimmäinen pääsääntö
Sisäenergian muutos on kahden asian summa: systeemiin tuotu lämpömäärä ja systeemiin tehty työ:
```kaavat
lämpöopin 1. pääsääntö :: \Delta U = Q + W
```
Tässä $\Delta U$ on sisäenergian muutos (J). $Q$ on systeemiin siirtynyt lämpömäärä (J). $W$ on ympäristön systeemiin tekemä työ (J). Merkit kertovat suunnan.

- $Q$ on positiivinen, kun lämpöä siirtyy systeemiin. Se on negatiivinen, kun lämpöä siirtyy pois.
- $W$ on positiivinen, kun ympäristö tekee työtä systeemiin. Esimerkiksi ympäristö puristaa kaasua. Se on negatiivinen, kun systeemi tekee työtä ympäristöön. Esimerkiksi kaasu laajenee ja työntää mäntää.

Kaikki termit ovat jouleja. Työn yksikkö oli sama luvussa *Työ ja energia*. Männän kaasuun tekemä työ lasketaan samoin kuin siellä: voima kertaa matka.

<svg data-fig="energy-balance" viewBox="0 0 600 300" role="img" aria-label="Energiakaavio: systeemiin tulee lämpömäärä Q ja työ W. Systeemin sisäenergia muuttuu niiden summan verran. Ulos siirtyvä energia on negatiivista." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-5-energy-balance.webp" x="9.9" y="9.9" width="591.1" height="307.9" preserveAspectRatio="none"/>
  <foreignObject x="246" y="103.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{systeemi}$</div></foreignObject>
  <foreignObject x="258.5" y="151.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta U = Q + W$</div></foreignObject>
  <foreignObject x="68.5" y="51.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpö}\ Q$</div></foreignObject>
  <foreignObject x="81" y="209.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{työ}\ W$</div></foreignObject>
  <foreignObject x="424" y="87.5" width="128" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q < 0\ \text{tai}\ W < 0$</div></foreignObject>
  <foreignObject x="459" y="163.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ulos}$</div></foreignObject>
  <foreignObject x="77.5" y="247.5" width="445" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sisään positiivinen, ulos negatiivinen}$</div></foreignObject>
</svg>

<svg data-fig="work-sign" viewBox="0 0 600 316" role="img" aria-label="Työn etumerkki (kaaviokuva, ei mittakaavassa). Vasemmalla mäntää työnnetään sisään ja kaasu puristuu. Ympäristö tekee kaasuun työn, joten W on positiivinen. Oikealla kaasu työntää mäntää ulos ja laajenee. Kaasu tekee työn ympäristöön, joten W on negatiivinen." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-5-work-sign.webp" x="1.2" y="2.5" width="597" height="322.1" preserveAspectRatio="none"/>
  <foreignObject x="121" y="13.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{puristus}$</div></foreignObject>
  <foreignObject x="376" y="13.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{laajeneminen}$</div></foreignObject>
  <foreignObject x="152.5" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W > 0$</div></foreignObject>
  <foreignObject x="432.5" y="231.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W < 0$</div></foreignObject>
  <foreignObject x="58.5" y="269.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ympäristö tekee työn}$</div></foreignObject>
  <foreignObject x="363.5" y="269.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kaasu tekee työn}$</div></foreignObject>
</svg>

```pysahdy
Kaasu laajenee ja työntää mäntää. Silloin se tekee ympäristöön työn $30\,\text{J}$. Kaasuun ei siirry lämpöä eikä siitä siirry pois. Kuinka paljon kaasun sisäenergia muuttuu?
---
Kaasu tekee työn ympäristöön, joten $W = -30\,\text{J}$. Lämpöä ei siirry, joten $Q = 0$. Siis $\Delta U = Q + W = -30\,\text{J}$. Sisäenergia pienenee $30\,\text{J}$.
```

## Esimerkki
Pumpun sylinterissä on ilmaa. Mäntää painetaan alas. Ympäristö tekee ilmaan työn $150\,\text{J}$. Samalla kuumenevasta ilmasta siirtyy sylinterin seinien kautta ympäristöön lämpömäärä $40\,\text{J}$. Kuinka paljon ilman sisäenergia muuttuu?

<!-- vaihe -->

**Tunnetut ja kysytty.** Ilma on systeemi. Ympäristö tekee työtä systeemiin, joten $W = +150\,\text{J}$. Lämpöä siirtyy systeemistä pois, joten $Q = -40\,\text{J}$.

Kysytty on sisäenergian muutos $\Delta U$.

<!-- vaihe -->

**Periaate.** Energia säilyy. Systeemin sisäenergia muuttuu täsmälleen sen verran kuin siihen siirtyy energiaa lämpönä ja työnä. Tämä on termodynamiikan ensimmäinen pääsääntö. Se pätee, koska ilma on selvästi rajattu systeemi. Sen rajan yli energia siirtyy vain työnä ja lämpönä.

<!-- vaihe -->

**Kaava ratkaistuna.** Kysytty $\Delta U$ on ensimmäisessä pääsäännössä jo yksin vasemmalla puolella. Yhtälöä ei siis tarvitse muokata:

```latex
\begin{aligned}
&\Delta U = Q + W
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita. Sekä $Q$ että $W$ on annettu jouleina, ja tulos halutaan jouleina. Etumerkit sen sijaan on päätettävä. Energia systeemiin on positiivista. Energia systeemistä pois on negatiivista.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan arvot etumerkkeineen:

```latex
\begin{aligned}
&\Delta U = Q + W \\
&= -40\,\text{J} + 150\,\text{J} \\
&= 110\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Ilman sisäenergia kasvaa $110\,\text{J}$. Tulos ilmoitetaan kokonaisina jouleina, koska sekä työ että lämpö on annettu kokonaisina jouleina.

<!-- vaihe -->

**Järkevyys.** Työ toi ilmaan $150\,\text{J}$. Lämpönä lähti vain $40\,\text{J}$. Siksi sisäenergian on kasvettava ja ilman lämpötilan on noustava. Tehdään nyt sama $150\,\text{J}$:n työ niin hitaasti, että kaikki työn tuoma energia ehtii siirtyä lämpönä pois. Silloin $Q = -150\,\text{J}$ ja $\Delta U = 0$, eikä lämpötila muutu. Esimerkissä lämpöä lähtee vähemmän. Tulos on siis tämän rajatapauksen ja pelkän työn $150\,\text{J}$ välissä.

## Yleinen virhekäsitys
Arkikielessä sanotaan, että kappaleessa ”on lämpöä” tai että lämpö ”varastoituu”. Fysiikassa lämpö on energian siirtymistä lämpötilaeron vuoksi. Kappaleeseen varastoituu sisäenergiaa.

Toinen virhe on pitää lämpötilaa ja sisäenergiaa samana asiana. Kuuman kipinän lämpötila on tuhansia asteita. Sen sisäenergia on silti pieni, koska kipinässä on vähän ainetta.

Kolmas virhe on ajatella, että sisäenergiaa voi muuttaa vain lämmittämällä. Pumpun ilma kuumenee ilman lämmönlähdettä, koska siihen tehdään työtä.

## Tiivistelmä
- Sisäenergia $U$ on systeemin hiukkasten liike-energian ja hiukkasten välisten vuorovaikutusten energian summa. Se kasvaa, kun lämpötila nousee eikä olomuoto muutu. Se riippuu myös aineen määrästä. Lämpötila ja sisäenergia eivät ole sama asia.
- Lämpö on energian siirtymistä kuumemmasta kylmempään lämpötilaeron vuoksi. Siirtynyt energia on lämpömäärä $Q$. Kappaleella ei ”ole lämpöä”.
- Sisäenergiaa muuttavat lämpö ja työ: $\Delta U = Q + W$. Sisään siirtyvä energia on positiivista. Ulos siirtyvä energia on negatiivista.
- Energia säilyy. Tämä on termodynamiikan ensimmäinen pääsääntö. Eristetyn systeemin kokonaisenergia pysyy vakiona.
