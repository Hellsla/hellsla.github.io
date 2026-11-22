# Intensiteetti ja desibeliasteikko

> **Miksi** äänen voimakkuus ilmoitetaan desibeleinä eikä watteina neliömetriä kohti? Mitä desibelilukema oikeastaan kertoo?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: ulkoilmakonsertti iltapäivällä. Lavan molemmin puolin on kaiutintornit, ja niiden edessä seisoo yleisöä. Kaiuttimista leviää yhä laajempia kaaria. Kaukana oikealla rinteellä istuu kaksi kuulijaa. Kaaret ulottuvat heihin vaaleina." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-15-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Intensiteetti: teho pinta-alaa kohti
Ääni on ilmassa etenevä aalto. Se kuljettaa energiaa lähteestä kuulijaan. Äänen voimakkuus riippuu siitä, kuinka paljon energiaa sekunnissa osuu pinnalle. Pinta voi olla esimerkiksi tärykalvo tai mikrofoni. Siksi äänen voimakkuutta kuvataan **intensiteetillä** $I$. Intensiteetti on pinnan läpi kulkeva ääniteho $P$ jaettuna pinnan pinta-alalla $A$. Pinnan pitää olla kohtisuorassa äänen etenemissuuntaan nähden. Intensiteetin yksikkö on watti neliömetriä kohti, $\text{W/m}^2$. Jos sama teho keskittyy pienelle alalle, intensiteetti on suuri. Jos teho leviää laajalle alalle, intensiteetti on pieni.

### Pistemäinen lähde ja etäisyys
Pieni äänilähde, joka säteilee tasaisesti joka suuntaan, on pistemäinen lähde. Oletetaan, että ääni ei heijastu eikä ilma vaimenna sitä. Silloin lähteen koko teho $P$ kulkee jokaisen lähdettä ympäröivän pallopinnan läpi. Pallon pinta-ala $4\pi r^2$ kasvaa etäisyyden $r$ neliönä. Kaksinkertaisella etäisyydellä sama teho jakautuu nelinkertaiselle alalle. Kolminkertaisella etäisyydellä ala on yhdeksänkertainen. Intensiteetti on siis kääntäen verrannollinen etäisyyden neliöön. Tätä sanotaan **etäisyyden neliön käänteislaiksi**. Todellisuudessa seinät ja maa heijastavat ääntä. Sisätiloissa intensiteetti pienenee siksi hitaammin.

<svg data-fig="kartio" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva, ei mittakaavassa: pistemäinen äänilähde on vasemmalla. Siitä lähtevät säteet rajaavat kartion, joka leikkaa kolme neliötä etäisyyksillä r, 2r ja 3r. Lähin neliö on yksi ruutu, jonka pinta-ala on A. Etäisyydellä 2r kartio peittää neljä samankokoista ruutua eli pinta-alan 4A. Etäisyydellä 3r se peittää yhdeksän ruutua eli 9A. Sama teho jakautuu yhä suuremmalle alalle, joten intensiteetti on I, I/4 ja I/9. Ruutujen väri vaalenee samassa suhteessa." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-15-kartio.webp" x="1.2" y="1.2" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="42" y="197.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P$</div></foreignObject>
  <foreignObject x="176.5" y="115.5" width="49" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A,\ I$</div></foreignObject>
  <foreignObject x="316" y="86" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4A,\ I/4$</div></foreignObject>
  <foreignObject x="475" y="56" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$9A,\ I/9$</div></foreignObject>
  <foreignObject x="192" y="311.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="335.5" y="311.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2r$</div></foreignObject>
  <foreignObject x="485.5" y="311.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3r$</div></foreignObject>
  <foreignObject x="42" y="311.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy5/sound-level-meter-park.webp" alt="Ihmisiä istuu puistossa. Tolpassa on punainen näyttö, jossa lukee 62 dB."><figcaption>Melunäyttö puistossa Kiinassa. Näyttö kertoo äänitason desibeleinä. Tällaiset mittarit näyttävät yleensä A-painotettua äänenpainetasoa. Ulkona painottamaton äänenpainetaso on lukuarvoltaan suunnilleen sama kuin intensiteettitaso. A-painotettu lukema voi olla erilainen, varsinkin matalilla äänillä. $62\,\text{dB}$ on noin tavallisen puheen voimakkuus.</figcaption></figure>

```pysahdy
Miksi intensiteetti pienenee, kun mennään kauemmas pistemäisestä lähteestä? Lähteen teho pysyy samana.
---
Sama teho levittäytyy isommalle pallopinnalle. Pinta-ala on isompi, joten intensiteetti eli teho pinta-alaa kohti on pienempi.
```

### Kuulokynnys ja kipukynnys
Ihmisen korva on hämmästyttävän herkkä. Nuori normaalikuuloinen ihminen erottaa noin $1000\,\text{Hz}$:n taajuudella äänen, jonka intensiteetti on noin $I_0 = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2$. Se on heikoin ääni, jonka hän kuulee. Tätä sanotaan **kuulokynnykseksi**. Kuulokynnys ei ole hiljaisuus. Se on heikoin kuultavissa oleva ääni. Se on myös eri suuri eri taajuuksilla. Kovimmat äänet alkavat tuntua kivulta, kun intensiteetti on noin $1\,\text{W/m}^2$. Tämä kipukynnys on biljoona eli $10^{12}$ kertaa kuulokynnyksen suuruinen. Näin laajaa vaihteluväliä on hankala esittää tavallisella asteikolla. Molemmat kynnykset ovat eri ihmisillä erilaisia, ja ne riippuvat taajuudesta. Siksi nämä arvot ovat sovittuja likiarvoja. Ne eivät ole luonnonvakioita.

### Desibeliasteikko
Intensiteetin vaihteluväli on siis hyvin laaja. Siksi äänen voimakkuutta kuvataan **intensiteettitasolla** $L$. Se vertaa intensiteettiä kuulokynnykseen logaritmin avulla. Tason yksikkö on **desibeli** ($\text{dB}$). Kuulokynnyksellä taso on noin $0\,\text{dB}$ ja kipukynnyksellä noin $120\,\text{dB}$. Asteikko on logaritminen. Aina kun intensiteetti kymmenkertaistuu, tasoon lisätään $10\,\text{dB}$. Keskustelun taso on noin $60\,\text{dB}$. Se ei siis ole puolet kipukynnyksestä. Sen intensiteetti on miljoonasosa kipukynnyksen intensiteetistä. Myös korva aistii voimakkuuden suunnilleen logaritmisesti. Noin $10\,\text{dB}$:n lisäys kuulostaa suunnilleen kaksi kertaa niin voimakkaalta, vaikka intensiteetti kymmenkertaistuu.

<svg data-fig="asteikko" viewBox="0 0 600 396" role="img" aria-label="Kaavakuva: intensiteettitason asteikko on pystysuora palkki, joka tummuu alhaalta ylös. Alhaalla on 0 dB eli intensiteetti 10 potenssiin miinus 12 wattia neliömetrille. Se on kuulokynnys. Joka 20 desibelin välein intensiteetti on sata kertaa suurempi: 20 dB kuiskaus, 40 dB hiljainen huone, 60 dB keskustelu, 80 dB vilkas katu ja 100 dB moottorisaha. Ylhäällä on 120 dB eli 1 watti neliömetrille. Se on kipukynnys. Esimerkkiäänet ovat tyypillisiä suuruusluokkia." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy515-bar" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ffc078" stop-opacity="0.35"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <foreignObject x="284" y="7.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$L\ (\text{dB})$</div></foreignObject>
  <foreignObject x="400" y="7.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{W/m}^2)$</div></foreignObject>
  <rect x="236" y="68" width="32" height="300" rx="4" fill="url(#fy515-bar)" stroke="#1f2933" stroke-width="2"/>
  <line x1="230" y1="368" x2="236" y2="368" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="368" x2="274" y2="368" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="77" y="353.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{kuulokynnys}$</div></foreignObject>
  <foreignObject x="284" y="353.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="400" y="353.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10^{-12}$</div></foreignObject>
  <line x1="230" y1="318" x2="236" y2="318" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="318" x2="274" y2="318" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="114" y="303.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{kuiskaus}$</div></foreignObject>
  <foreignObject x="284" y="303.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$20$</div></foreignObject>
  <foreignObject x="400" y="303.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10^{-10}$</div></foreignObject>
  <line x1="230" y1="268" x2="236" y2="268" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="268" x2="274" y2="268" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="253.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{hiljainen huone}$</div></foreignObject>
  <foreignObject x="284" y="253.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$40$</div></foreignObject>
  <foreignObject x="400" y="253.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10^{-8}$</div></foreignObject>
  <line x1="230" y1="218" x2="236" y2="218" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="218" x2="274" y2="218" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="89" y="203.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{keskustelu}$</div></foreignObject>
  <foreignObject x="284" y="203.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="400" y="203.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10^{-6}$</div></foreignObject>
  <line x1="230" y1="168" x2="236" y2="168" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="168" x2="274" y2="168" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="89" y="153.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{vilkas katu}$</div></foreignObject>
  <foreignObject x="284" y="153.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$80$</div></foreignObject>
  <foreignObject x="400" y="153.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10^{-4}$</div></foreignObject>
  <line x1="230" y1="118" x2="236" y2="118" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="118" x2="274" y2="118" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="103.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{moottorisaha}$</div></foreignObject>
  <foreignObject x="284" y="103.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$100$</div></foreignObject>
  <foreignObject x="400" y="103.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10^{-2}$</div></foreignObject>
  <line x1="230" y1="68" x2="236" y2="68" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="268" y1="68" x2="274" y2="68" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="89" y="53.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{kipukynnys}$</div></foreignObject>
  <foreignObject x="284" y="53.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$120$</div></foreignObject>
  <foreignObject x="400" y="53.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1$</div></foreignObject>
</svg>

```pysahdy
Äänen intensiteetti tulee tuhatkertaiseksi. Kuinka monta desibeliä taso kasvaa?
---
Tuhatkertainen on kolme kymmenkertaista peräkkäin. Taso kasvaa $3 \cdot 10\,\text{dB} = 30\,\text{dB}$.
```

Korva ei ole yhtä herkkä kaikille taajuuksille. Matalat ja hyvin korkeat äänet kuulostavat samalla intensiteetillä hiljaisemmilta kuin äänet, joiden taajuus on noin $1000$–$4000\,\text{Hz}$. Siksi melumittarit painottavat taajuuksia korvan herkkyyden mukaan. Tällainen painotettu lukema merkitään $\text{dB(A)}$. Tavalliset melumittarit näyttävät usein A-painotettua äänenpainetasoa. Tässä luvussa lasketaan painottamattomia intensiteettitasoja.

### Mitä mittari mittaa
Mittarin mikrofoni ei mittaa intensiteettiä. Se mittaa äänenpainetta eli ilmanpaineen vaihtelua. Siitä lasketaan **äänenpainetaso**. Äänenpainetaso vertaa äänenpainetta vertailupaineeseen $p_0 = 20\,\mu\text{Pa}$. Intensiteettitaso taas vertaa intensiteettiä vertailuintensiteettiin $I_0$. Tasot liittyvät toisiinsa, mutta ne eivät ole sama suure. Kun ääni etenee vapaasti, esimerkiksi ulkona kaukana seinistä, painottamattoman äänenpainetason ja intensiteettitason lukuarvot ovat suunnilleen samat. Kaikuvassa huoneessa heijastuneet aallot kulkevat moneen suuntaan. Ne kasvattavat äänenpainetta, mutta niiden energiavirrat kumoavat osittain toisiaan. Siksi tasot voivat erota. Tämän luvun laskuissa oletetaan, että ääni etenee vapaasti ilman heijastuksia. Silloin mittarin lukemaa käsitellään intensiteettitasona. Melun vaikutuksista ja kuulon suojaamisesta kerrotaan luvussa *Melu, akustiikka ja äänentoisto*.

## Kaava: Intensiteettitaso

### Intensiteetti
Äänen intensiteetti on
```kaavat
intensiteetti :: I = \frac{P}{A}
```
missä $I$ on intensiteetti ($\text{W/m}^2$), $P$ pinnan läpi kulkeva ääniteho ($\text{W}$) ja $A$ pinnan pinta-ala ($\text{m}^2$). Pistemäinen lähde säteilee tasaisesti joka suuntaan, eikä ääni heijastu. Silloin $A$ on pallon pinta-ala $4\pi r^2$:
```latex
I = \frac{P}{4\pi r^2}
```
missä $P$ on lähteen ääniteho ($\text{W}$) ja $r$ etäisyys lähteestä ($\text{m}$).

### Intensiteettitaso
Intensiteettitaso desibeleinä on
```kaavat
äänen intensiteettitaso :: L = 10\lg\left(\frac{I}{I_0}\right)\,\text{dB}
```
missä $L$ on intensiteettitaso ($\text{dB}$), $I$ intensiteetti ja $I_0 = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2$ sovittu vertailuintensiteetti. Se on suunnilleen kuulokynnyksen suuruinen. Merkintä $\lg$ on kymmenkantainen logaritmi. Luku $\lg x$ kertoo, mihin potenssiin luku $10$ pitää korottaa, jotta saadaan $x$. Esimerkiksi $\lg 1000 = 3$, koska $10^3 = 1000$. Lisäksi $\lg 1 = 0$, joten $I = I_0$ antaa tason $0\,\text{dB}$.

### Intensiteetti tunnetusta tasosta
Jos taso tunnetaan, intensiteetti lasketaan kahdessa vaiheessa. Ensin yhtälö jaetaan puolittain $10\,\text{dB}$:llä. Sitten käytetään logaritmin määritelmää: jos $\lg x = y$, niin $x = 10^y$. Lopuksi kerrotaan $I_0$:lla:
```latex
\begin{aligned}
&\lg \frac{I}{I_0} = \frac{L}{10\,\text{dB}} \\
&\frac{I}{I_0} = 10^{\,L/(10\,\text{dB})} \\
&I = I_0 \cdot 10^{\,L/(10\,\text{dB})}
\end{aligned}
```
Esimerkiksi keskustelun $60\,\text{dB}$ antaa $\tfrac{L}{10\,\text{dB}} = 6$, joten $I = 10^{6} \cdot I_0 = 1{,}0 \cdot 10^{-6}\,\text{W/m}^2$. Laskimessa logaritmin näppäin on $\lg$ (tai $\log$). Potenssi $10^x$ on yleensä saman näppäimen toinen toiminto. Kokeile, että $\lg 3 \approx 0{,}477$ ja $10^{0{,}477} \approx 3$.

### Tasojen erotus
Kahden äänen tasojen erotus riippuu vain intensiteettien suhteesta, koska $I_0$ supistuu pois:
```latex
L_2 - L_1 = 10\,\text{dB} \cdot \lg \frac{I_2}{I_1}
```
Kun intensiteetti kaksinkertaistuu, taso kasvaa $10\,\text{dB} \cdot \lg 2 \approx 3{,}0\,\text{dB}$. Kun intensiteetti kymmenkertaistuu, taso kasvaa $10\,\text{dB}$. Kun etäisyys pistemäisestä lähteestä kaksinkertaistuu, intensiteetti putoaa neljäsosaan. Silloin taso pienenee $10\,\text{dB} \cdot \lg 4 \approx 6{,}0\,\text{dB}$.

<svg data-fig="kuvaaja" viewBox="0 0 600 420" role="img" aria-label="Kuvaaja mittakaavassa: pistemäisen äänilähteen intensiteettitaso L desibeleinä etäisyyden r funktiona nollasta kymmeneen metriin. Lähteen teho on 12,6 milliwattia. Käyrä laskee ensin jyrkästi ja sitten loivasti. Pisteet etäisyyksillä 1, 2, 4 ja 8 metriä ovat 90,0, 84,0, 78,0 ja 71,9 dB. Joka kerta, kun etäisyys kaksinkertaistuu, taso pienenee noin 6 dB." style="max-width:100%;font-size:24px">
  <line x1="149" y1="376" x2="149" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="188" y1="376" x2="188" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="227" y1="376" x2="227" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="266" y1="376" x2="266" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="305" y1="376" x2="305" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="344" y1="376" x2="344" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="383" y1="376" x2="383" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="422" y1="376" x2="422" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="461" y1="376" x2="461" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="376" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="345.5" x2="500" y2="345.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="315" x2="500" y2="315" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="284" x2="500" y2="284" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="253.5" x2="500" y2="253.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="223" x2="500" y2="223" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="192.5" x2="500" y2="192.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="162" x2="500" y2="162" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="131" x2="500" y2="131" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="100.5" x2="500" y2="100.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="70" x2="500" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="109" y1="376" x2="514" y2="376" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,376 L513,382 L513,370 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="377" x2="110" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,44 L116,57 L104,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="149" y1="376" x2="149" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="188" y1="376" x2="188" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="178" y="385.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="227" y1="376" x2="227" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="266" y1="376" x2="266" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="256" y="385.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="305" y1="376" x2="305" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="344" y1="376" x2="344" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="334" y="385.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="383" y1="376" x2="383" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="422" y1="376" x2="422" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="412" y="385.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="461" y1="376" x2="461" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="500" y1="376" x2="500" y2="383" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="483.5" y="385.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="103" y1="345.5" x2="110" y2="345.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="331" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="103" y1="315" x2="110" y2="315" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="300.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="103" y1="284" x2="110" y2="284" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="269.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="103" y1="253.5" x2="110" y2="253.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="239" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="103" y1="223" x2="110" y2="223" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="208.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="103" y1="192.5" x2="110" y2="192.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="178" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="103" y1="162" x2="110" y2="162" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="147.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$70$</div></foreignObject>
  <line x1="103" y1="131" x2="110" y2="131" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="116.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="103" y1="100.5" x2="110" y2="100.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="65" y="86" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$90$</div></foreignObject>
  <line x1="103" y1="70" x2="110" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="53" y="55.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <foreignObject x="80" y="381.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="532" y="361.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r\ (\text{m})$</div></foreignObject>
  <foreignObject x="100" y="13.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$L\ (\text{dB})$</div></foreignObject>
  <polyline points="149,100.5 152,102.5 155,104.5 158,106 160.5,107.5 163.5,109 166.5,110.5 169.5,112 172.5,113 175.5,114.5 178,115.5 181,116.5 184,117.5 187,118.5 190,119.5 193,120.5 196,121.5 198.5,122.5 201.5,123.5 204.5,124 207.5,125 210.5,125.5 213.5,126.5 216.5,127 219,128 222,128.5 225,129.5 228,130 231,130.5 234,131.5 237,132 239.5,132.5 242.5,133 245.5,133.5 248.5,134.5 251.5,135 254.5,135.5 257,136 260,136.5 263,137 266,137.5 269,138 272,138.5 275,139 277.5,139.5 280.5,140 283.5,140.5 286.5,140.5 289.5,141 292.5,141.5 295,142 298,142.5 301,143 304,143 307,143.5 310,144 313,144.5 315.5,145 318.5,145 321.5,145.5 324.5,146 327.5,146.5 330.5,146.5 333.5,147 336,147.5 339,147.5 342,148 345,148.5 348,148.5 351,149 354,149.5 356.5,149.5 359.5,150 362.5,150 365.5,150.5 368.5,151 371.5,151 374,151.5 377,151.5 380,152 383,152.5 386,152.5 389,153 392,153 394.5,153.5 397.5,153.5 400.5,154 403.5,154 406.5,154.5 409.5,155 412,155 415,155.5 418,155.5 421,156 424,156 427,156.5 430,156.5 432.5,157 435.5,157 438.5,157 441.5,157.5 444.5,157.5 447.5,158 450.5,158 453,158.5 456,158.5 459,159 462,159 465,159.5 468,159.5 471,159.5 473.5,160 476.5,160 479.5,160.5 482.5,160.5 485.5,161 488.5,161 491,161 494,161.5 497,161.5 500,162" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="149" y1="100.5" x2="149" y2="376" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="110" y1="100.5" x2="149" y2="100.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="149" cy="100.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="157" y="46" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$90{,}0$</span></div></foreignObject>
  <line x1="188" y1="119" x2="188" y2="376" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="110" y1="119" x2="188" y2="119" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="188" cy="119" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="196" y="82.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$84{,}0$</span></div></foreignObject>
  <line x1="266" y1="137.5" x2="266" y2="376" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="110" y1="137.5" x2="266" y2="137.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="266" cy="137.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="274" y="101" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$78{,}0$</span></div></foreignObject>
  <line x1="422" y1="156" x2="422" y2="376" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="110" y1="156" x2="422" y2="156" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="422" cy="156" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="430" y="119.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$71{,}9$</span></div></foreignObject>
</svg>

### Usean lähteen yhteistaso
Joskus samaan paikkaan kuuluu kaksi toisistaan riippumatonta äänilähdettä, esimerkiksi kaksi konetta tai kaksi soittajaa. Silloin niiden tehot lasketaan yhteen, ja siksi myös intensiteetit lasketaan yhteen: $I = I_1 + I_2$. Desibelejä ei lasketa yhteen. Yhteistaso lasketaan summaintensiteetistä. Kaksi yhtä voimakasta lähdettä kaksinkertaistaa intensiteetin, joten $80\,\text{dB}$ ja $80\,\text{dB}$ antavat yhdessä noin $83\,\text{dB}$. Jos toinen lähde on paljon heikompi, se ei juuri muuta tasoa. Tasot $70\,\text{dB}$ ja $60\,\text{dB}$ antavat intensiteetin $1{,}1 \cdot 10^{-5}\,\text{W/m}^2$ eli noin $70{,}4\,\text{dB}$. Sääntö ei päde kahteen kaiuttimeen, jotka toistavat samaa sävelaaltoa samassa vaiheessa. Niiden aallot interferoivat, kuten luvussa *Aaltojen yhteisvaikutus: superpositio ja interferenssi*. Siksi aallot vahvistavat toisiaan joissakin kohdissa ja heikentävät toisissa.

<svg data-fig="summa" viewBox="0 0 600 360" role="img" aria-label="Kaksi pylväskaaviota mittakaavassa. Vasemmalla ovat intensiteetit yksikössä 10 potenssiin miinus 4 wattia neliömetrille: kumpikin kaiutin yksin 1,0 ja yhdessä 2,0. Yhteinen pylväs on siis kaksi kertaa niin korkea. Oikealla ovat samat tilanteet intensiteettitasoina: kumpikin yksin 80 dB ja yhdessä 83 dB. Yhteinen pylväs on vain vähän korkeampi." style="max-width:100%;font-size:24px">
  <line x1="300" y1="14" x2="300" y2="346" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="40" y="11.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (10^{-4}\,\text{W/m}^2)$</div></foreignObject>
  <line x1="32" y1="300" x2="284" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="52" y="200" width="52" height="100" rx="3" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="55.5" y="167.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}0$</div></foreignObject>
  <foreignObject x="61.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I_1$</div></foreignObject>
  <rect x="122" y="200" width="52" height="100" rx="3" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="125.5" y="167.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}0$</div></foreignObject>
  <foreignObject x="131.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I_2$</div></foreignObject>
  <rect x="196" y="100" width="52" height="200" rx="3" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="199.5" y="67.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}0$</div></foreignObject>
  <foreignObject x="187" y="309.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I_1 + I_2$</div></foreignObject>
  <foreignObject x="330" y="11.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$L\ (\text{dB})$</div></foreignObject>
  <line x1="318" y1="300" x2="584" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="340" y="140" width="52" height="160" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="349.5" y="107.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$80$</div></foreignObject>
  <foreignObject x="349.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$L_1$</div></foreignObject>
  <rect x="410" y="140" width="52" height="160" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="419.5" y="107.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$80$</div></foreignObject>
  <foreignObject x="419.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$L_2$</div></foreignObject>
  <rect x="486" y="134" width="52" height="166" rx="3" fill="#8a96a3" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="495.5" y="101.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$83$</div></foreignObject>
  <foreignObject x="502" y="309.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$L$</div></foreignObject>
</svg>

```pysahdy
Kaksi samanlaista konetta toimii yhtä aikaa. Toinen sammutetaan. Putoaako taso puoleen?
---
Ei putoa. Intensiteetti puolittuu. Taso laskee vain noin $3\,\text{dB}$.
```

## Esimerkki
Ulkoilmakonsertissa desibelimittari näyttää $96\,\text{dB}$, kun se on $10\,\text{m}$:n päässä kaiutintornista. Kuinka suuri on äänen intensiteetti mittarin kohdalla? Kuinka suuri on kaiutintornin ääniteho? Oleta, että torni säteilee kuin pistemäinen lähde tasaisesti joka suuntaan. Oleta myös, että ääni ei heijastu eikä vaimene. Silloin mittarin lukemaa voi käsitellä intensiteettitasona.

<!-- vaihe -->

**Tunnetut ja kysytty.** Mittarin lukema eli intensiteettitaso on $L = 96\,\text{dB}$, etäisyys $r = 10\,\text{m}$ ja kuulokynnys $I_0 = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2$.

Kysytään intensiteettiä $I$ ja lähteen äänitehoa $P$.

<!-- vaihe -->

**Periaate.** Intensiteettitaso vertaa intensiteettiä kuulokynnykseen. Intensiteetti saadaan siis ratkaisemalla se tasoyhtälöstä. Ensin jaetaan $10\,\text{dB}$:llä ja sitten käytetään logaritmin määritelmää. Torni säteilee tasaisesti joka suuntaan. Siksi koko teho kulkee $10\,\text{m}$:n säteisen pallopinnan läpi, ja $I = \tfrac{P}{4\pi r^2}$.

<!-- vaihe -->

**Kaava ratkaistuna.** Tasoyhtälöstä saadaan $\lg \tfrac{I}{I_0} = \tfrac{L}{10\,\text{dB}}$. Logaritmin määritelmä antaa intensiteetin. Teho saadaan kertomalla intensiteetti pallon pinta-alalla:
```latex
\begin{aligned}
&I = I_0 \cdot 10^{\,L/(10\,\text{dB})} \\[6pt]
&P = I \cdot 4\pi r^2
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Niitä ei tarvita. Etäisyys on metreinä ja kuulokynnys yksikössä $\text{W/m}^2$. Desibelit supistuvat osamäärässä:
```latex
\begin{aligned}
&\dfrac{L}{10\,\text{dB}} \\
&= \dfrac{96\,\text{dB}}{10\,\text{dB}} \\
&= 9{,}6
\end{aligned}
```

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&I = I_0 \cdot 10^{\,L/(10\,\text{dB})} \\
&= 1{,}0 \cdot 10^{-12}\,\tfrac{\text{W}}{\text{m}^2} \cdot 10^{9{,}6} \\
&= 3{,}98 \cdot 10^{-3}\,\tfrac{\text{W}}{\text{m}^2} \\[6pt]
&P = I \cdot 4\pi r^2 \\
&= 3{,}98 \cdot 10^{-3}\,\tfrac{\text{W}}{\text{m}^2} \cdot 4\pi \cdot (10\,\text{m})^2 \\
&= 5{,}00\,\text{W}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Intensiteetti on noin $4{,}0 \cdot 10^{-3}\,\text{W/m}^2$. Kaiutintornin ääniteho on noin $5{,}0\,\text{W}$. Tulokset ilmoitetaan kahdella merkitsevällä numerolla, koska taso $96\,\text{dB}$ on annettu kokonaisina desibeleinä. Jo $1\,\text{dB}$:n ero tasossa muuttaisi intensiteettiä ja tehoa noin neljänneksellä. Tarkkuutta rajoittaa siis taso. Esimerkissä etäisyyttä $10\,\text{m}$ pidetään tarkkana arvona.

<!-- vaihe -->

**Järkevyys.** Taso $96\,\text{dB}$ on tasojen $90\,\text{dB}$ ja $100\,\text{dB}$ välissä. Intensiteetin pitää siis olla välillä $10^{-3}$–$10^{-2}\,\text{W/m}^2$, ja $4{,}0 \cdot 10^{-3}\,\text{W/m}^2$ on. Ääniteho $5\,\text{W}$ tuntuu pieneltä. Kaiutin kuitenkin muuttaa ääneksi tyypillisesti vain noin $1\,\%$ sähkötehostaan. Tornin vahvistimien teho on siis satoja watteja.

## Yleinen virhekäsitys
Moni laskee desibelit yhteen kuten tavalliset luvut. Kaksi konetta tuottaa kumpikin yksinään $80\,\text{dB}$. Ne eivät tuota yhdessä $160\,\text{dB}$, joka olisi suihkukonetta kovempi ääni. Yhteen lasketaan intensiteetit. Intensiteetti kaksinkertaistuu, ja taso kasvaa vain noin $3\,\text{dB}$:llä arvoon $83\,\text{dB}$.

Toinen virhe on ajatella, että kaksinkertainen desibelilukema tarkoittaa kaksinkertaista ääntä. Taso $120\,\text{dB}$ on $60\,\text{dB}$ suurempi kuin $60\,\text{dB}$. Siksi intensiteetti on $10^6$ eli miljoona kertaa suurempi. Kolmas virhe on luulla, että $0\,\text{dB}$ tarkoittaa, ettei ääntä ole. Se tarkoittaa kuulokynnyksen intensiteettiä $I_0$. Vielä heikommilla äänillä taso on negatiivinen.

## Tiivistelmä
- Intensiteetti on teho pinta-alaa kohti: $I = \tfrac{P}{A}$, yksikkö $\text{W/m}^2$. Pistemäiselle lähteelle ilman heijastuksia $I = \tfrac{P}{4\pi r^2}$. Kaksinkertainen etäisyys antaa neljäsosan intensiteetistä.
- Vertailuintensiteetti $I_0 = 1{,}0 \cdot 10^{-12}\,\text{W/m}^2$ on suunnilleen kuulokynnys eli heikoin kuultava ääni. Kipukynnys on noin $1\,\text{W/m}^2$. Kynnykset ovat sovittuja likiarvoja. Ne vaihtelevat ihmisen ja taajuuden mukaan.
- Melumittari mittaa äänenpainetasoa (usein A-painotettuna, $\text{dB(A)}$). Kun ääni etenee vapaasti, painottamaton äänenpainetaso on lukuarvoltaan suunnilleen sama kuin intensiteettitaso. Kaikuvassa huoneessa se voi olla erilainen.
- Intensiteettitaso on $L = 10\lg\left(\tfrac{I}{I_0}\right)\,\text{dB}$. Kaksinkertainen intensiteetti lisää tasoa noin $3\,\text{dB}$ ja kymmenkertainen $10\,\text{dB}$.
- Intensiteetti tasosta: $I = I_0 \cdot 10^{\,L/(10\,\text{dB})}$.
- Riippumattomien lähteiden intensiteetit lasketaan yhteen. Desibelejä ei lasketa yhteen.
