# Momentti: voiman kiertävä vaikutus

> **Miksi** tiukkaan juuttunut pyöränmutteri aukeaa pitkällä avaimella, vaikka lyhyellä avaimella yhtä suuri voima ei saa sitä liikkumaan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: renkaiden vaihto syksyllä kotipihassa. Mies on polvillaan auton takapyörän vieressä. Hän painaa molemmin käsin alas pitkän vääntövarren päätä. Varren toinen pää on pyöränmutterissa vanteen keskellä. Varsi ulottuu pyörästä kauas vasemmalle. Miehen takana on pino talvirenkaita. Hänen edessään asfaltilla on lyhyt kiintoavain. Taustalla on punainen talo ja keltaisia koivuja." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-1-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Voima voi muuttaa kappaleen liikettä. Voima voi myös kiertää kappaletta. Joskus kappale on kiinni akselissa. Esimerkiksi ovi on kiinni saranoissaan, mutteri on pultissa ja keinulauta on tuessaan. Tällainen kappale ei pääse siirtymään pois. Se voi vain kiertyä akselin ympäri. Tätä akselia sanotaan **kiertoakseliksi**. Voiman kykyä kiertää kappaletta kiertoakselin ympäri sanotaan **vääntövaikutukseksi**. Vääntövaikutuksen suuruutta mitataan **momentilla** (voiman momentti). Vääntövaikutus ei riipu vain voiman suuruudesta. Siihen vaikuttavat myös voiman suunta ja se, mihin kohtaan kappaletta voima vaikuttaa.

### Ovi ja voiman vaikutuskohta
Ovi aukeaa helposti, kun työnnät kahvasta, joka on kaukana saranoista. Jos työnnät samalla voimalla läheltä saranaa, ovi kääntyy paljon huonommin. Jos työnnät oven päästä oven suuntaisesti kohti saranaa, ovi ei käänny lainkaan. Voima on silloinkin yhtä suuri. Kuvan kolme voimaa $\overline{F}_1$, $\overline{F}_2$ ja $\overline{F}_3$ ovat siis yhtä suuria. Niiden vääntövaikutukset saranan suhteen ovat kuitenkin aivan erilaiset.

<svg data-fig="ovi" viewBox="0 0 600 330" role="img" aria-label="Ovi ylhäältä katsottuna. Vasemmalla on seinä ja sarana. Ovi lähtee saranasta oikealle vaakasuorana lautana. Kuvassa on kolme yhtä pitkää punaista voimanuolta. Voima F1 vaikuttaa kahvassa kohtisuoraan ovea vastaan. Voima F2 vaikuttaa lähellä saranaa, myös kohtisuoraan. Voima F3 vaikuttaa oven päässä oven suuntaisesti kohti saranaa. Katkoviivainen kaari näyttää, mihin suuntaan ovi aukeaa. Kuva on kaavakuva, eikä se ole mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-1-ovi.webp" x="0" y="-1.2" width="600" height="341.2" preserveAspectRatio="none"/>
  <foreignObject x="9" y="167.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{seinä}$</div></foreignObject>
  <foreignObject x="68.5" y="275.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{sarana}$</div></foreignObject>
  <foreignObject x="430" y="275.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{kahva}$</div></foreignObject>
  <foreignObject x="403" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_1$</div></foreignObject>
  <foreignObject x="167" y="141.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_2$</div></foreignObject>
  <foreignObject x="547.5" y="207.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_3$</div></foreignObject>
  <foreignObject x="183.5" y="15.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{ylhäältä katsottuna}$</div></foreignObject>
</svg>

### Voiman varsi
Vääntövaikutuksen ratkaisee voiman **vaikutussuora**. Vaikutussuora on suora, joka kulkee voiman vaikutuskohdan kautta voiman suuntaan. Avaimessa vaikutuskohta on kohta, josta käsi pitää avaimesta kiinni. Sitä sanotaan myös otekohdaksi. **Voiman varsi** $r$ on kiertoakselin lyhin etäisyys voiman vaikutussuorasta. Lyhin etäisyys mitataan kohtisuoraan vaikutussuoraa vastaan. Jos voima on kohtisuorassa avaimen vartta vastaan, varsi on yhtä pitkä kuin vaikutuskohdan etäisyys $d$ akselista. Jos voima on vinossa, varsi on lyhyempi kuin $d$. Jos vaikutussuora kulkee kiertoakselin kautta, varsi on nolla. Silloin voima ei kierrä kappaletta lainkaan. Siksi oven suuntainen voima $\overline{F}_3$ ei avaa ovea.

<svg data-fig="varsi" viewBox="0 0 600 340" role="img" aria-label="Kiintoavain mutterin ympärillä. Mutterin keskellä on kiertoakseli O. Avaimen varsi osoittaa vaakasuoraan oikealle. Käsi vetää vartta kohdasta, joka on etäisyyden d päässä akselista. Voima F osoittaa vinosti ylös oikealle. Se on 60 asteen kulmassa varren jatkeeseen nähden. Voiman vaikutussuora on piirretty katkoviivalla molempiin suuntiin. Akselista vaikutussuoralle piirretty kohtisuora jana on voiman varsi r. Se on lyhyempi kuin d. Kuva on kaavakuva." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-1-varsi.webp" x="1.2" y="0" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="191" y="192" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="248" y="47.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$d$</div></foreignObject>
  <foreignObject x="461.5" y="20.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="442" y="87" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="68" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <foreignObject x="313" y="264.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{vaikutussuora}$</div></foreignObject>
</svg>

```pysahdy
Avainta vedetään vinosti varteen nähden. Onko voiman varsi silloin yhtä pitkä kuin käden etäisyys akselista?
---
Ei ole. Varsi mitataan kohtisuoraan vaikutussuoraa vastaan. Vinossa vedossa varsi on lyhyempi kuin käden etäisyys akselista.
```

## Kaava: Voiman momentti
Voiman momentti kiertoakselin suhteen on voiman suuruuden ja voiman varren tulo:
```kaavat
voiman momentti :: M = F r
```
Kaavassa $M$ on voiman momentti ($\text{Nm}$), $F$ on voiman suuruus ($\text{N}$) ja $r$ on voiman varsi ($\text{m}$). Voiman varsi on kiertoakselin kohtisuora etäisyys voiman vaikutussuorasta. Momentin yksikkö on newtonmetri $\text{Nm}$. Se ei ole sama asia kuin energian yksikkö joule. Molemmat ovat newtonin ja metrin tuloja, mutta niiden etäisyydet ovat erilaisia. Momentissa etäisyys on kohtisuorassa voimaa vastaan. Työssä etäisyys on voiman suuntainen siirtymä.

```pysahdy
Avaimen vartta vedetään kohtisuoraan $30\,\text{N}$:n voimalla. Veto on $0{,}40\,\text{m}$:n päässä mutterin keskeltä. Mikä on voiman momentti?
---
Voima on kohtisuorassa, joten varsi on $0{,}40\,\text{m}$. Momentti on $30\,\text{N}\cdot 0{,}40\,\text{m} = 12\,\text{Nm}$.
```

### Kiertosuunta ja etumerkki
Momentilla on suuruuden lisäksi kiertosuunta. Tässä kirjassa vastapäivään kiertävä momentti on positiivinen. Myötäpäivään kiertävä momentti on negatiivinen. Joskus kappaleeseen vaikuttaa monta voimaa. Silloin lasketaan voimien momentit yhteen etumerkkeineen. Tulosta sanotaan **kokonaismomentiksi**:
```latex
\Sigma M = M_1 + M_2 + M_3 + \ldots
```
Kaavassa $\Sigma M$ on kokonaismomentti ($\text{Nm}$). Luvut $M_1$, $M_2$, … ovat yksittäisten voimien momentit saman kiertoakselin suhteen ($\text{Nm}$). Oletetaan, että kappale on levossa ja se voi kiertyä kiinteän akselin ympäri. Jos kokonaismomentti ei ole nolla, kappale alkaa kiertyä kokonaismomentin suuntaan. Milloin kappale pysyy paikallaan, tutkitaan tarkemmin luvussa *Kappaleen tasapaino: voimat ja momentit*.

<svg data-fig="suunta" viewBox="0 0 600 320" role="img" aria-label="Kaksi tilannetta vierekkäin. Kummassakin vaakasuora sauva on kiinni akselissa O vasemmasta päästään. Vasemmalla voima F vaikuttaa sauvan oikeaan päähän ylöspäin. Kaarinuoli akselin ympärillä kiertää vastapäivään, joten momentti on positiivinen. Oikealla voima vaikuttaa sauvan päähän alaspäin. Kaarinuoli kiertää myötäpäivään, joten momentti on negatiivinen." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-1-suunta.webp" x="1.2" y="1.2" width="597" height="330.8" preserveAspectRatio="none"/>
  <foreignObject x="263.5" y="67.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="66" y="19.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vastapäivään}$</div></foreignObject>
  <foreignObject x="66" y="275.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M > 0$</div></foreignObject>
  <foreignObject x="34" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <foreignObject x="563.5" y="235.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="366" y="19.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{myötäpäivään}$</div></foreignObject>
  <foreignObject x="366" y="275.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$M < 0$</div></foreignObject>
  <foreignObject x="334" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
</svg>

```pysahdy
Levy on levossa ja voi kiertyä akselin ympäri. Siihen vaikuttavat momentit $+8\,\text{Nm}$ ja $-5\,\text{Nm}$. Mihin suuntaan levy alkaa kiertyä? Miksi?
---
Kokonaismomentti on $+3\,\text{Nm}$. Se on positiivinen, joten levy alkaa kiertyä vastapäivään.
```

### Vinon voiman varsi
Usein tiedetään kaksi asiaa. Ensimmäinen on vaikutuskohdan etäisyys $d$ kiertoakselista. Toinen on kulma $\alpha$. Se on kulma voiman ja sen suoran välillä, joka kulkee akselista vaikutuskohtaan. Esimerkiksi avaimen varren jatke on tällainen suora. Akseli, vaikutuskohta ja varren kantapiste muodostavat suorakulmaisen kolmion. Kolmion pisin sivu eli hypotenuusa on $d$. Varsi on kulman $\alpha$ vastainen kateetti:
```latex
r = d\sin\alpha
```
Kaavassa $r$ on voiman varsi ($\text{m}$), $d$ on vaikutuskohdan etäisyys kiertoakselista ($\text{m}$) ja $\alpha$ on voiman ja varren jatkeen välinen kulma. Kun $\alpha = 90^\circ$, niin $r = d$ ja momentti on suurin. Kun $\alpha = 0^\circ$ tai $\alpha = 180^\circ$, niin $r = 0$.

<svg data-fig="kulma" viewBox="0 0 600 340" role="img" aria-label="Suorakulmainen kolmio. Sen kärjet ovat kiertoakseli O, voiman otekohta ja akselista vaikutussuoralle piirretyn kohtisuoran kantapiste. Hypotenuusa on akselin ja otekohdan välinen etäisyys d. Kateetti akselista kantapisteeseen on voiman varsi r. Otekohdan kulma on alfa. Se on sama kulma kuin voiman ja varren jatkeen välinen kulma. Siksi r on d kertaa sini alfa." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-1-kulma.webp" x="0" y="0" width="600" height="347.5" preserveAspectRatio="none"/>
  <foreignObject x="508" y="41" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="56" y="93.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <foreignObject x="247" y="67.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$d$</div></foreignObject>
  <foreignObject x="128" y="186.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="352" y="111.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="466.5" y="69.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="385" y="271.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r = d\sin\alpha$</div></foreignObject>
</svg>

## Esimerkki
Juuttunutta mutteria avataan kiintoavaimella. Käsi tarttuu varteen $0{,}35\,\text{m}$:n etäisyydellä mutterin keskeltä. Mutterin keskikohta on kiertoakseli. Käsi vetää vartta $240\,\text{N}$:n voimalla. Voima on $65^\circ$:n kulmassa varren jatkeeseen nähden, ja se kiertää mutteria aukeamissuuntaan. Mutteri aukeaa vasta, kun momentti on vähintään $80\,\text{Nm}$. Kuinka suuri on käden voiman momentti mutterin akselin suhteen? Aukeaako mutteri?

<!-- vaihe -->

**Tunnetut ja kysytty.** Tunnetut arvot ovat $F = 240\,\text{N}$, $d = 0{,}35\,\text{m}$ ja $\alpha = 65^\circ$. Mutterin vaatima momentti on $80\,\text{Nm}$.

Kysytään voiman momenttia $M$ ja sitä, riittääkö se.

<!-- vaihe -->

**Periaate.** Mutteri voi vain kiertyä akselinsa ympäri. Siksi voiman vääntövaikutuksen kertoo sen momentti $M = Fr$. Voima on vinossa varteen nähden, joten varsi $r$ on lyhyempi kuin etäisyys $d$. Varsi saadaan suorakulmaisesta kolmiosta: $r = d\sin\alpha$.

<!-- vaihe -->

**Kaava ratkaistuna.** Sijoitetaan varren lauseke momentin kaavaan:
```latex
\begin{aligned}
&M = F r \\
&M = F d\sin\alpha
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Muunnoksia ei tarvita. Voima on newtoneina ja etäisyys metreinä, joten momentti tulee newtonmetreinä.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen:
```latex
\begin{aligned}
M &= F d\sin\alpha \\
&= 240\,\text{N}\cdot 0{,}35\,\text{m}\cdot\sin 65^\circ \\
&\approx 76{,}1\,\text{Nm}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Voiman momentti on $M \approx 76\,\text{Nm}$. Tuloksessa on kaksi merkitsevää numeroa, koska etäisyydessä $0{,}35\,\text{m}$ on kaksi. Momentti on pienempi kuin mutterin vaatima $80\,\text{Nm}$, joten mutteri ei aukea.

<!-- vaihe -->

**Järkevyys.** Oletetaan, että sama voima vaikuttaisi kohtisuoraan vartta vastaan. Silloin varsi olisi koko $0{,}35\,\text{m}$ ja momentti olisi $240\,\text{N}\cdot 0{,}35\,\text{m} = 84\,\text{Nm}$. Vino veto antaa vähemmän, koska $\sin 65^\circ \approx 0{,}91 < 1$. Mutteri aukeaisi siis samalla voimalla, jos vedettäisiin kohtisuoraan vartta vastaan.

## Yleinen virhekäsitys
Momenttia ei saada kertomalla voima etäisyydellä vaikutuskohtaan. Se saadaan kertomalla voima etäisyydellä vaikutussuoraan. Etäisyys $d$ ja varsi $r$ ovat yhtä suuret vain silloin, kun voima on kohtisuorassa akselista vaikutuskohtaan kulkevaa suoraa vastaan. Toinen virhe on ajatella, että pitkä avain lisää voimaa. Käden voima on sama. Pitkällä avaimella voiman varsi on kuitenkin pidempi, joten momentti on suurempi. Mutterin aukeaminen ei vaadi tiettyä voimaa vaan tietyn momentin.

## Tiivistelmä
- Voiman vääntövaikutusta kiertoakselin suhteen mitataan momentilla $M = Fr$. Sen yksikkö on newtonmetri $\text{Nm}$.
- Voiman varsi $r$ on kiertoakselin kohtisuora etäisyys voiman vaikutussuorasta. Se ei ole etäisyys vaikutuskohtaan.
- Vinon voiman varsi on $r = d\sin\alpha$. Voima, jonka vaikutussuora kulkee akselin kautta, ei kierrä kappaletta.
- Vastapäivään kiertävä momentti on positiivinen ja myötäpäivään kiertävä negatiivinen. Kokonaismomentti on momenttien summa etumerkkeineen.
- Oletetaan, että kappale on levossa ja se voi kiertyä akselin ympäri. Jos kokonaismomentti ei ole nolla, kappale alkaa kiertyä.
