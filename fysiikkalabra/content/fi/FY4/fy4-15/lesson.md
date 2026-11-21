# Vesi- ja tuulivoima energian muuntajina

> **Miksi** sama Vuoksen vesi antaa Imatralla kolme kertaa suuremman tehon kuin Tainionkoskella? Ja miksi tuulivoimalan teho kasvaa paljon enemmän kuin tuulen nopeus?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: jokilaakso kesäpäivänä. Keskellä joen poikki on rakennettu vesivoimalaitos: padon takana yläpuolinen vesi on korkealla, ja voimalan alapuolelta purkautuva vesi kuohuu valkoisena alempana. Taustalla harjanteella pyörii neljä tuulivoimalaa, ja taivaalla näkyy tuulen viivoja. Voimalasta lähtee sähkölinja pylväineen." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-15-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Voimala muuntaa energiaa
Vesi- ja tuulivoimala eivät tuota energiaa tyhjästä. Ne muuntavat veden tai ilman mekaanista energiaa sähköksi. Padon takana olevalla vedellä on potentiaalienergiaa $E_\text{p} = mgh$ alaveteen verrattuna. Kun vesi virtaa putkea alas, potentiaalienergia muuttuu liike-energiaksi, kuten luvussa *Mekaanisen energian säilyminen ja energiaperiaate*. Nopea vesivirta painaa turbiinin siipiä ja pyörittää turbiinia (monessa turbiinissa myös veden paine tekee työtä, mutta energiaketju on sama), ja turbiinin akseli pyörittää generaattoria, joka muuttaa pyörimisen energian sähköksi. Turbiinin jälkeen vesi virtaa hitaasti alaveteen. Ylä- ja alaveden pintojen korkeuseroa sanotaan **putouskorkeudeksi** $h$.

<svg data-fig="vesivoimala" viewBox="0 0 600 360" role="img" aria-label="Periaatekuva vesivoimalasta poikkileikkauksena, ei mittakaavassa. Vasemmalla padon takana on yläallas, jonka pinta on korkealla. Vesi virtaa padon läpi kulkevaa putkea alas turbiiniin, joka pyörittää akselin välityksellä generaattoria. Turbiinin jälkeen vesi purkautuu oikealle alaveteen. Ylä- ja alaveden pintojen korkeusero on putouskorkeus h. Veden potentiaalienergia muuttuu putkessa liike-energiaksi, turbiinissa pyörimisen energiaksi ja generaattorissa sähköksi, jota kuvaa oranssi nuoli." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-15-vesivoimala.webp" x="0" y="0" width="600" height="371.2" preserveAspectRatio="none"/>
  <foreignObject x="496" y="192.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{a}$</div></foreignObject>
  <foreignObject x="542" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="52" y="45.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{yläallas}$</div></foreignObject>
  <foreignObject x="64.5" y="145.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$E_\text{p} = mgh$</span></div></foreignObject>
  <foreignObject x="217.5" y="271.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E_\text{k}$</div></foreignObject>
  <foreignObject x="321" y="145.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{generaattori}$</div></foreignObject>
  <foreignObject x="246" y="315.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{turbiini}$</span></div></foreignObject>
  <foreignObject x="472.5" y="307.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{alavesi}$</span></div></foreignObject>
</svg>

### Teho kertoo energiaa sekunnissa
Voimalaa kuvataan teholla: kuinka paljon energiaa se muuntaa sekunnissa. Kun yksi kuutiometri vettä eli $1000\,\text{kg}$ putoaa Imatran putouskorkeuden $24\,\text{m}$, sen potentiaalienergiaa vapautuu $mgh \approx 235\,\text{kJ}$. Jos turbiinien läpi virtaa sekunnissa satoja kuutiometrejä, teho on satoja megawatteja. Teho kasvaa siis kahdesta syystä: kun sekunnissa putoavaa vettä on enemmän ja kun se putoaa korkeammalta. Vuoksen vesi virtaa ensin Tainionkosken ja sitten Imatran voimalaitoksen läpi, joten virtaama on molemmissa sama. Imatran putouskorkeus on noin kolme kertaa suurempi, ja niin on sen tehokin.

```pysahdy
Kaksi voimalaa saa saman virtaaman, mutta toisen putouskorkeus on kaksinkertainen. Kumman teho on suurempi ja kuinka paljon?
---
Kaksinkertaisen putouskorkeuden voimalan teho on kaksinkertainen, koska jokaisen sekunnissa putoavan kuutiometrin potentiaalienergia $mgh$ on kaksinkertainen.
```

### Hyötysuhde
Kaikki veden menettämä energia ei muutu sähköksi. Vesi hankaa putken seiniä, turbiini ja generaattori lämpenevät, ja alaveteen purkautuvalla vedellä on vielä vähän liike-energiaa. Voimalan **hyötysuhde** on sen antotyön $W_\text{a}$ ja ottotyön $W_\text{o}$ suhde, ja yhtä hyvin antotehon $P_\text{a}$ ja ottotehon $P_\text{o}$ suhde. Voimalassa antoteho on sen antama sähköteho:
```kaavat
hyötysuhde :: \eta = \frac{W_\text{a}}{W_\text{o}} = \frac{P_\text{a}}{P_\text{o}}
```
missä $\eta$ (eta) on hyötysuhde, joka ilmoitetaan desimaalilukuna tai prosentteina. Hyötysuhde on enintään $100\,\%$. Todellisissa laitteissa se jää usein alle $100\,\%$, koska osa otetusta energiasta ei päädy määriteltyyn hyödylliseen käyttötarkoitukseen, tässä sähköksi. Suuren vesivoimalan hyötysuhde on noin $90\,\%$.

```pysahdy
Voimala ottaa vedestä tehon $100\,\text{MW}$ ja antaa sähkötehon $90\,\text{MW}$. Mihin loput $10\,\text{MW}$ menevät?
---
Energiaa ei katoa. Pääosa muuttuu sisäenergiaksi, joka siirtyy lämpönä ympäristöön, kun vesi hankaa ja laitteet lämpenevät, ja osa jää alaveteen purkautuvan veden liike-energiaksi.
```

### Tuulen liike-energia
Tuulivoimalassa energian lähde on liikkuvan ilman liike-energia $E_\text{k} = \tfrac{1}{2}mv^2$. Tuuli painaa roottorin lapoja ja pyörittää roottoria, ja ilma hidastuu ohittaessaan roottorin. Roottori ei voi pysäyttää ilmaa kokonaan, koska ilman on päästävä virtaamaan pois roottorin takaa. Siksi edes ihanteellinen roottori ei saa talteen kuin noin $59\,\%$ siitä tehosta, jonka häiriötön tuuli kuljettaa roottorin pyyhkäisypinta-alan läpi, ja todellisen tuulivoimalan osuus on alle puolet. Ilma on kevyttä: kuutiometrin massa on vain noin $1{,}25\,\text{kg}$. Siksi tuulivoimalan roottorin on oltava suuri, jotta sen läpi virtaisi sekunnissa paljon ilmaa.

```pysahdy
Ilmassa on paljon energiaa. Miksi tuulivoimalan roottori silti tehdään kooltaan valtavaksi?
---
Ilma on kevyttä, joten sen massa on pieni. Suuri roottori saa sekunnissa läpi paljon ilmaa, ja vasta silloin liike-energiaa saadaan talteen riittävästi.
```

<figure class="unit-photo"><img src="pics/fy4/middelgrunden-wind-farm.webp" alt="Valkoisia tuulivoimaloita aallonmurtajan takana sinistä taivasta vasten. Edustalla on avointa merta ja muutama vene."><figcaption>Middelgrundenin merituulipuisto Kööpenhaminan edustalla Tanskassa veneestä kuvattuna.</figcaption></figure>

## Kaava: Vesi- ja tuulivoimalan teho

### Vesivoimala
Virtaama $Q$ kertoo, montako kuutiometriä vettä virtaa sekunnissa turbiinien läpi. Ajassa $t$ turbiinien läpi virtaa tilavuus $V = Qt$, jonka massa on $m = \rho V = \rho Q t$. Sen potentiaalienergia putouskorkeudella $h$ on $mgh = \rho Q t g h$, joten veden tuoma teho on $P_\text{o} = \rho Q g h$. Hyötysuhteen mukaan sähköteho on $\eta$ kertaa tämä:
```latex
P = \eta \rho Q g h
```
missä $P$ on voimalan sähköteho ($\text{W}$), $\eta$ hyötysuhde, $\rho$ veden tiheys ($1000\,\text{kg/m}^3$), $Q$ virtaama ($\text{m}^3\text{/s}$), $g$ putoamiskiihtyvyys ($9{,}81\,\text{m/s}^2$) ja $h$ putouskorkeus ($\text{m}$). Kaavassa oletetaan, että veden liike-energia on ylä- ja alavedessä pieni, joten muuntuva energia on potentiaalienergian muutos.

### Tuulivoimala
Tarkastellaan ensin häiriötöntä tuulta eli tuulta, jota roottori ei ole vielä hidastanut. Ajassa $t$ häiriötön tuuli, jonka nopeus on $v$, kuljettaisi roottorin pyyhkäisypinta-alan $A = \pi r^2$ läpi ilman, joka täyttää lieriön, jonka pituus on $vt$. Tämän ilman massa on $m = \rho A v t$, ja sen liike-energia on $\tfrac{1}{2}mv^2 = \tfrac{1}{2}\rho A v^3 t$. Häiriöttömän tuulen tehovirta pyyhkäisypinta-alan läpi on siis $P_\text{tuuli} = \tfrac{1}{2}\rho A v^3$.

Todellisuudessa roottori hidastaa ilmaa jo ennen lapoja, joten roottorin kohdalla ilma virtaa hitaammin kuin $v$, eikä sen massavirta ole $\rho A v$. Siksi $P_\text{tuuli}$ on vertailuteho: se kertoo, kuinka paljon energiaa sekunnissa samankokoisen alueen läpi kulkisi ilman voimalaa. Voimalan hyötysuhde $\eta$ määritellään osuudeksi tästä vertailutehosta, $\eta = P : P_\text{tuuli}$.

<svg data-fig="ilmalierio" viewBox="0 0 600 360" role="img" aria-label="Periaatekuva, ei mittakaavassa: tuuli puhaltaa vasemmalta tuulivoimalan roottoria kohti. Ajassa t häiriötön tuuli kuljettaisi roottorin pyyhkäisypinta-alan läpi ilman, joka täyttäisi lieriön. Lieriön poikkipinta-ala on roottorin pyyhkäisemä pinta-ala A = πr² ja pituus s = vt, joten ilman massa olisi m = ρAvt. Sininen nuoli on tuulen nopeus v." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-15-ilmalierio.webp" x="0" y="0" width="600" height="367.5" preserveAspectRatio="none"/>
  <foreignObject x="53.5" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="256" y="303.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s = vt$</div></foreignObject>
  <foreignObject x="243.5" y="155.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$m = \rho A v t$</div></foreignObject>
  <foreignObject x="372" y="107.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="488" y="93.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$A = \pi r^2$</div></foreignObject>
</svg>

Sähköteho on siis:
```latex
P = \frac{1}{2}\eta \rho A v^3
```
missä $P$ on sähköteho ($\text{W}$), $\eta$ voimalan hyötysuhde eli sähkötehon osuus häiriöttömän tuulen vertailutehosta, $\rho$ ilman tiheys (noin $1{,}25\,\text{kg/m}^3$), $A$ roottorin pyyhkäisemä pinta-ala ($\text{m}^2$) ja $v$ häiriöttömän tuulen nopeus ($\text{m/s}$).

### Miksi nopeus on kolmannessa potenssissa?
Kun tuulen nopeus kaksinkertaistuu, pyyhkäisypinta-alan läpi kulkee sekunnissa kaksi kertaa enemmän ilmaa, ja jokaisella ilmakilogrammalla on neljä kertaa enemmän liike-energiaa. Vertailuteho kasvaa siis $2 \cdot 4 = 2^3 = 8$ -kertaiseksi. Sähköteho kasvaa samassa suhteessa vain mallissa, jossa hyötysuhde pysyy likimain vakiona. Todellisen voimalan tehokäyrässä teho kasvaa tuulen nopeudesta $5\,\text{m/s}$ nopeuteen $10\,\text{m/s}$ noin $8{,}9$-kertaiseksi, koska hyötysuhde on suuremmalla nopeudella vähän parempi.

Todellisella voimalalla on lisäksi kolme tuulen nopeuden aluetta, joita kuutiollinen malli ei kuvaa. Käynnistysnopeutta heikommassa tuulessa, tällä voimalalla noin $3\text{–}4\,\text{m/s}$, voimala ei tuota sähköä. Noin $13\,\text{m/s}$:n tuulesta alkaen teho pysyy $1650\,\text{kW}$:ssa. Se on voimalan nimellisteho, jota generaattori ei voi ylittää, joten lapoja käännetään päästämään osa tuulesta ohi. Silloin kaava vakiohyötysuhteella ei enää kuvaa voimalaa. Pysäytysnopeutta voimakkaammassa myrskytuulessa voimala pysäytetään rakenteiden suojaamiseksi, ja sen teho putoaa nollaan.

<svg data-fig="tehokayra" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa, valmistajan ilmoittama tehokäyrä: tuulivoimalan sähköteho P kilowatteina tuulen nopeuden v funktiona, kun roottorin halkaisija on 82 m. Pisteet: 3 m/s 0 kW, 4 m/s 28 kW, 5 m/s 144 kW, 6 m/s 309 kW, 7 m/s 511 kW, 8 m/s 758 kW, 9 m/s 1017 kW, 10 m/s 1285 kW, 11 m/s 1504 kW, 12 m/s 1637 kW ja 13–20 m/s 1650 kW. Katkoviivana mallin käyrä ½ηρAv³, kun η = 0,45: se nousee kuten pisteet mutta jatkaa nousuaan, kun pisteet tasaantuvat 1650 kilowattiin." style="max-width:100%;font-size:24px">
  <line x1="133.5" y1="296" x2="133.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="171" y1="296" x2="171" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="208" y1="296" x2="208" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="245.5" y1="296" x2="245.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="283" y1="296" x2="283" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320.5" y1="296" x2="320.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="358" y1="296" x2="358" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="395" y1="296" x2="395" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="432.5" y1="296" x2="432.5" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="296" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="268.5" x2="470" y2="268.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="241.5" x2="470" y2="241.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="214" x2="470" y2="214" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="186.5" x2="470" y2="186.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="159.5" x2="470" y2="159.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="132" x2="470" y2="132" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="104.5" x2="470" y2="104.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="77.5" x2="470" y2="77.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="50" x2="470" y2="50" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="296" x2="484" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,296 L483,302 L483,290 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="297" x2="96" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,24 L102,37 L90,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="133.5" y1="296" x2="133.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="171" y1="296" x2="171" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="161" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="208" y1="296" x2="208" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="245.5" y1="296" x2="245.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="235.5" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="283" y1="296" x2="283" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="320.5" y1="296" x2="320.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="304" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$12$</div></foreignObject>
  <line x1="358" y1="296" x2="358" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="395" y1="296" x2="395" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="378.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$16$</div></foreignObject>
  <line x1="432.5" y1="296" x2="432.5" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="296" x2="470" y2="303" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="453.5" y="305.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="268.5" x2="96" y2="268.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="241.5" x2="96" y2="241.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="227" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="89" y1="214" x2="96" y2="214" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="186.5" x2="96" y2="186.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="172" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$800$</div></foreignObject>
  <line x1="89" y1="159.5" x2="96" y2="159.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="132" x2="96" y2="132" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="26" y="117.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1200$</div></foreignObject>
  <line x1="89" y1="104.5" x2="96" y2="104.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="77.5" x2="96" y2="77.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="26" y="63" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1600$</div></foreignObject>
  <line x1="89" y1="50" x2="96" y2="50" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="66" y="301.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="281.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\text{m/s})$</div></foreignObject>
  <foreignObject x="110" y="15.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$P\ (\text{kW})$</span></div></foreignObject>
  <polyline points="96,296 97.5,296 99.5,296 101,296 102.5,296 104.5,296 106,296 107.5,296 109.5,296 111,296 112.5,296 114.5,296 116,296 117.5,295.5 119.5,295.5 121,295.5 122.5,295.5 124,295.5 126,295 127.5,295 129,295 131,294.5 132.5,294.5 134,294.5 136,294 137.5,294 139,293.5 141,293 142.5,293 144,292.5 146,292 147.5,292 149,291.5 151,291 152.5,290.5 154,290 156,289.5 157.5,289 159,288 161,287.5 162.5,287 164,286 166,285.5 167.5,284.5 169,284 171,283 172.5,282 174,281 175.5,280.5 177.5,279.5 179,278 180.5,277 182.5,276 184,275 185.5,273.5 187.5,272.5 189,271 190.5,269.5 192.5,268 194,267 195.5,265 197.5,263.5 199,262 200.5,260.5 202.5,258.5 204,257 205.5,255 207.5,253 209,251 210.5,249 212.5,247 214,245 215.5,243 217.5,240.5 219,238.5 220.5,236 222.5,233.5 224,231 225.5,228.5 227.5,226 229,223 230.5,220.5 232,217.5 234,214.5 235.5,211.5 237,208.5 239,205.5 240.5,202.5 242,199 244,195.5 245.5,192 247,188.5 249,185 250.5,181.5 252,178 254,174 255.5,170 257,166 259,162 260.5,158 262,153.5 264,149.5 265.5,145 267,140.5 269,136 270.5,131 272,126.5 274,121.5 275.5,116.5 277,111.5 279,106.5 280.5,101.5 282,96 283.5,90.5 285.5,85 287,79.5 288.5,74 290.5,68 292,62 293.5,56 295.5,50" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 6"/>
  <foreignObject x="200.5" y="39.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\tfrac{1}{2}\eta\rho A v^3$</span></div></foreignObject>
  <circle cx="152" cy="296" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="171" cy="292" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="189.5" cy="276.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="208" cy="254" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="227" cy="226" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="245.5" cy="192.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="264.5" cy="157" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="283" cy="120.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="301.5" cy="90.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="320.5" cy="72.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="339" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="358" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="376.5" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="395" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="414" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="432.5" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="451.5" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="470" cy="70.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="344.5" y="86" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{tehokäyrä}$</span></div></foreignObject>
</svg>

Kuvaajan pisteet ovat Vestas V82 -tuulivoimalan valmistajan tehokäyrä (roottorin halkaisija $82\,\text{m}$, nimellisteho $1650\,\text{kW}$). Valmistajan tehokäyrä ilmoitetaan vakio-olosuhteissa, tavallisesti ilman tiheydelle $1{,}225\,\text{kg/m}^3$ ja kymmenen minuutin keskituulille napakorkeudella. Mallin katkoviiva on laskettu tiheydellä $1{,}25\,\text{kg/m}^3$, joten vertailu on likimääräinen. Liian voimakkaassa tuulessa voimala pysäytetään, jolloin sen teho putoaa nollaan; kuvaaja ei näytä tätä aluetta. Lähde: Vestas Wind Systems, V82-voimalan tekniset tiedot; lukuarvot NREL:n tuulivoimala-arkistosta (turbine-models, Vestas V82).

## Esimerkki
Tuulivoimalan roottorin halkaisija on $120\,\text{m}$. Tuulen nopeus on $9{,}0\,\text{m/s}$ ja ilman tiheys $1{,}25\,\text{kg/m}^3$. Voimala muuttaa sähköksi $45\,\%$ siitä tehosta, jonka häiriötön tuuli kuljettaa roottorin pyyhkäisypinta-alan läpi. Kuinka suuri on voimalan sähköteho?

<!-- vaihe -->

**Tunnetut ja kysytty.** Roottorin halkaisija $d = 120\,\text{m}$, tuulen nopeus $v = 9{,}0\,\text{m/s}$, ilman tiheys $\rho = 1{,}25\,\text{kg/m}^3$ ja hyötysuhde $\eta = 45\,\%$.

Kysytään sähkötehoa $P$.

<!-- vaihe -->

**Periaate.** Häiriötön tuuli kuljettaa roottorin pyyhkäisypinta-alan läpi tehon $\tfrac{1}{2}\rho A v^3$. Voimala muuttaa tästä vertailutehosta sähköksi osuuden $\eta$, joten sähköteho saadaan tuulivoimalan tehon kaavasta. Pinta-ala $A$ on roottorin pyyhkäisemä ympyrä.

<!-- vaihe -->

**Kaava ratkaistuna.** Kaava antaa kysytyn tehon suoraan, kun pinta-ala lasketaan säteestä $r = \tfrac{d}{2}$:
```latex
\begin{aligned}
&P = \tfrac{1}{2}\eta\rho A v^3 \\
&A = \pi r^2
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Säde on $r = 120\,\text{m} : 2 = 60\,\text{m}$, ja hyötysuhde desimaalilukuna on $\eta = 0{,}45$. Muut suureet ovat SI-yksiköissä, ja $\tfrac{\text{kg}}{\text{m}^3}\cdot\text{m}^2\cdot\tfrac{\text{m}^3}{\text{s}^3} = \tfrac{\text{kg}\cdot\text{m}^2}{\text{s}^3} = \text{W}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin pinta-ala ja sitten teho:
```latex
\begin{aligned}
A &= \pi r^2 \\
&= \pi\cdot(60\,\text{m})^2 \\
&= 11\,309{,}7\,\text{m}^2 \\
P &= \tfrac{1}{2}\eta\rho A v^3 \\
&= 0{,}5\cdot 0{,}45\cdot 1{,}25\,\tfrac{\text{kg}}{\text{m}^3} \\
&\quad\cdot 11\,309{,}7\,\text{m}^2\cdot\left(9{,}0\,\tfrac{\text{m}}{\text{s}}\right)^3 \\
&= 2\,318\,849\,\text{W}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Sähköteho on noin $2{,}3\,\text{MW}$, kahden merkitsevän numeron tarkkuudella kuten tuulen nopeudessa $9{,}0\,\text{m/s}$ ja hyötysuhteessa $0{,}45$.

<!-- vaihe -->

**Järkevyys.** Tehokäyrän voimala, jonka roottorin halkaisija on $82\,\text{m}$, antaa tuulen nopeudella $9\,\text{m/s}$ tehon $1017\,\text{kW}$. Tämän roottorin pinta-ala on $(120 : 82)^2 \approx 2{,}14$ kertaa suurempi, joten tehon pitäisi olla noin $2{,}14 \cdot 1{,}02\,\text{MW} \approx 2{,}2\,\text{MW}$. Tulos $2{,}3\,\text{MW}$ on samaa suuruusluokkaa. Häiriöttömän tuulen vertailuteho on $5{,}2\,\text{MW}$, ja sähköksi saadaan alle puolet, kuten pitääkin.

## Yleinen virhekäsitys
Usein ajatellaan, että voimala tuottaa energiaa. Voimala muuntaa energiaa: vesivoimalan sähkö on peräisin veden potentiaalienergiasta ja tuulivoimalan sähkö tuulen liike-energiasta, ja osa energiasta muuttuu aina muuksi kuin sähköksi. Toinen virhe on olettaa, että kaksinkertainen tuuli antaa kaksinkertaisen tehon. Teho kasvaa nopeuden kolmannessa potenssissa, kunnes voimala saavuttaa nimellistehonsa. Kolmas virhe on sekoittaa teho ja energia: teho ilmoitetaan watteina, ja energia saadaan, kun teho kerrotaan ajalla. Voimala, jonka teho on $3\,\text{MW}$, tuottaa tunnissa $3\,\text{MWh}$ energiaa.

## Tiivistelmä
- Vesi- ja tuulivoimala muuntavat mekaanista energiaa sähköksi: vesivoimala veden potentiaalienergiaa, tuulivoimala ilman liike-energiaa.
- Hyötysuhde $\eta = \tfrac{P_\text{a}}{P_\text{o}}$ on enintään $100\,\%$; suuren vesivoimalan hyötysuhde on noin $90\,\%$ ja tuulivoimalan alle $50\,\%$.
- Vesivoimalan teho on $P = \eta\rho Q g h$: se on verrannollinen virtaamaan ja putouskorkeuteen.
- Tuulivoimalan teho on $P = \tfrac{1}{2}\eta\rho A v^3$: kun hyötysuhde pysyy likimain vakiona, kaksinkertainen tuulen nopeus antaa noin kahdeksankertaisen tehon, kunnes voimala saavuttaa nimellistehonsa. Hyvin voimakkaassa tuulessa voimala pysäytetään.
- Energia on teho kertaa aika, $E = Pt$.
