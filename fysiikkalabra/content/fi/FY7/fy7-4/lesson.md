# Voima virtajohtimeen: sähkömoottori ja kaiutin

> **Miksi** kaiuttimen kartio värähtelee ja tuulettimen siivet pyörivät, vaikka kumpaakaan ei työnnä mikään näkyvä?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: työpöydällä on puinen kaiutin, jonka kartiosta lähtee ääniaaltoja, ja sen vieressä pöytätuuletin, jonka siivet pyörivät. Kumpaakaan ei kosketa, mutta kartio värähtelee ja siivet pyörivät, kun laitteisiin kytketään sähkövirta." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-4-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Magneettikenttä työntää virtajohdinta
Luvussa *Varatun hiukkasen liike sähkö- ja magneettikentässä* magneettikenttä kohdisti liikkuvaan varattuun hiukkaseen voiman, joka oli kohtisuorassa sekä hiukkasen nopeutta että kenttää vastaan. Sähkövirta johtimessa on varausten liikettä: metallin johtavuuselektronit kulkevat johdinta pitkin. Magneettikenttä kohdistaa voiman jokaiseen liikkuvaan elektroniin, ja elektronit välittävät sen johtimen metalliin, joten voima kohdistuu koko johtimeen. Kun kevyt kuparijohdin ripustetaan hevosenkenkämagneetin napojen väliin ja virta kytketään, johdin heilahtaa sivulle. Kupari ei ole ferromagneettinen aine, eikä magneetti vedä sitä puoleensa: voima syntyy vasta, kun johtimessa kulkee virta.

<svg data-fig="swing" viewBox="0 0 600 360" role="img" aria-label="Kaksi periaatekuvaa, ei mittakaavassa. Vasemmalla johdin nähdään päästä päin kahden magneetin navan välissä: N-napa on ylhäällä ja S-napa alhaalla, joten magneettikenttä osoittaa alaspäin. Virta kulkee johtimessa paperiin päin, ja magneettikentän voima työntää johdinta vasemmalle, kohtisuoraan sekä virtaa että kenttää vastaan. Oikealla oikean käden sääntö: peukalo osoittaa virran suuntaan, muut sormet kentän suuntaan (vinosti piirretty nuoli tulee kohti katsojaa), ja voima osoittaa kämmenestä ulos, tässä alaspäin. Kolme nuolta ovat keskenään kohtisuorassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-4-swing.webp" x="1.2" y="1.2" width="597" height="366.9" preserveAspectRatio="none"/>
  <foreignObject x="150" y="53.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="150" y="281.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="246" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="103.5" y="137.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="150" y="207.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="540" y="81.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="465" y="131.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{peukalo}$</div></foreignObject>
  <foreignObject x="287" y="171.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="286" y="209.5" width="96" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sormet}$</div></foreignObject>
  <foreignObject x="416" y="265.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="416" y="303.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kämmen}$</div></foreignObject>
  <foreignObject x="310" y="13.5" width="280" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{oikean käden sääntö}$</div></foreignObject>
</svg>

### Voiman suunta
Voima on aina kohtisuorassa sekä virran suuntaa että magneettikenttää vastaan. Suunnan saa **oikean käden säännöllä**: kun ojennetun oikean käden peukalo osoittaa virran suuntaan ja muut sormet magneettikentän suuntaan, voima osoittaa kämmenestä ulos. Se on sama sääntö kuin positiiviselle varatulle hiukkaselle, sillä virran suunta on positiivisen varauksen liikkeen suunta. Kun virran tai kentän suunta käännetään, voiman suunta kääntyy. Jos johdin on kentän suuntainen, voimaa ei synny lainkaan.

```pysahdy
Johtimessa kulkee virta kohtisuoraan magneettikenttää vastaan, ja voima työntää johdinta ylöspäin. Mihin suuntaan voima osoittaa, jos virran suunta käännetään mutta kenttä pidetään ennallaan?
---
Voima osoittaa alaspäin. Kun virran tai kentän suunta kääntyy, voiman suunta kääntyy, mutta voiman suuruus pysyy samana.
```

### Sähkömoottori
Tasavirtamoottorissa magneetin napojen välissä on akselin ympäri kääntyvä **virtasilmukka**. Silmukan kahdessa kentän poikki kulkevassa sivussa virta kulkee vastakkaisiin suuntiin, joten niihin kohdistuu vastakkaissuuntaiset voimat. Voimat eivät ole samalla suoralla, joten niillä on vääntövaikutus: ne kääntävät silmukkaa. Kun silmukka on kääntynyt kohtisuoraan kenttää vastaan, voimat osoittavat poispäin akselista eivätkä enää käännä sitä, ja silmukka jatkaa liikettä hitautensa vuoksi. Juuri silloin **kommutaattori**, halkaistu rengas ja sitä koskettavat hiiliharjat, kääntää silmukan virran suunnan. Näin voimat kääntävät silmukkaa joka puolikierroksella samaan suuntaan. Oikeassa moottorissa on monta kelaa ja rautasydän, joten se pyörii tasaisesti ja voimakkaasti.

<svg data-fig="motor" viewBox="0 0 600 380" role="img" aria-label="Kaksi periaatekuvaa tasavirtamoottorista, ei mittakaavassa. Vasemmalla virtasilmukka nähdään akselin suunnasta N- ja S-navan välissä; magneettikenttä osoittaa vasemmalta oikealle. Silmukan toisessa sivussa virta kulkee paperiin päin, toisessa paperista ulos. Sivuihin kohdistuvat voimat ovat vastakkaissuuntaiset, toinen alaspäin ja toinen ylöspäin, ja ne kääntävät silmukkaa vastapäivään. Oikealla kommutaattori: akselin ympärillä on kahteen osaan halkaistu rengas, jota kaksi hiiliharjaa koskettaa. Harjat on kytketty virtalähteen plus- ja miinusnapaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-4-motor.webp" x="0" y="-1.2" width="600" height="387.5" preserveAspectRatio="none"/>
  <foreignObject x="36" y="180.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="304" y="180.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="243" y="269.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="130.5" y="276" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="196.5" y="85" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="95" y="345.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{virtasilmukka}$</div></foreignObject>
  <foreignObject x="380" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="564" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="392" y="77.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kommutaattori}$</div></foreignObject>
  <foreignObject x="407" y="275.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hiiliharjat}$</div></foreignObject>
</svg>

```pysahdy
Mitä tasavirtamoottorille tapahtuisi, jos kommutaattori ei kääntäisi silmukan virran suuntaa?
---
Kun silmukka on kääntynyt kohtisuoraan kenttää vastaan, voimat alkaisivat kääntää sitä takaisin. Silmukka ei pyörisi jatkuvasti vaan värähtelisi tämän asennon ympärillä ja pysähtyisi lopulta siihen.
```

### Kaiutin
Kaiuttimen magneetti on rakennettu niin, että rengasmaisessa raossa kenttä osoittaa säteittäin ulospäin. Raossa on kevyt puhekela, jonka jokainen kohta on kohtisuorassa kenttää vastaan, joten jokaiseen kohtaan kohdistuu yhtä suuri voima kelan akselin suuntaan. Säteittäinen kenttä on välttämätön: homogeenisessa kentässä suljetun kelan vastakkaisiin puoliin kohdistuvat voimat olisivat vastakkaissuuntaiset ja kumoaisivat toisensa, joten kelaa ei työntäisi mikään. Kela on kiinni kartiossa. Vahvistimen vaihtovirta muuttaa suuntaansa samassa tahdissa kuin äänisignaali, joten voima työntää kartiota vuorotellen eteen ja taakse. Kartio värähtelee signaalin taajuudella, puristaa ja harventaa ilmaa ja synnyttää ääniaallon. Mitä suurempi virta, sitä suurempi voima ja sitä voimakkaampi ääni. Suurin osa kaiuttimeen tuodusta sähköenergiasta muuttuu kuitenkin kelan ja magneetin sisäenergiaksi.

<svg data-fig="speaker" viewBox="0 0 600 360" role="img" aria-label="Kaiuttimen poikkileikkaus, periaatekuva, ei mittakaavassa. Vasemmalla on rautainen keskinapa ja sen ympärillä rengasmagneetti ja etulevy. Keskinapa on N-napa ja etulevy S-napa, joten kapeassa raossa magneettikenttä osoittaa säteittäin ulospäin, yläraossa ylös ja alaraossa alas. Raossa on puhekela: sen kierrosten poikkileikkauksessa virta kulkee yläpuolella paperiin päin ja alapuolella paperista ulos. Kummallakin puolella voima osoittaa oikealle, kohti kartiota, joka on kiinnitetty kelaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-4-speaker.webp" x="0" y="0" width="600" height="368.8" preserveAspectRatio="none"/>
  <foreignObject x="198" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{N}$</div></foreignObject>
  <foreignObject x="138" y="72.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="138" y="258.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="92" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="92" y="215.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="186" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="252" y="97.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="252" y="233.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="446" y="25.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kartio}$</div></foreignObject>
  <foreignObject x="40" y="315.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{rengasmagneetti}$</div></foreignObject>
  <foreignObject x="365" y="165.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I \text{ vaihtelee}$</div></foreignObject>
  <foreignObject x="325" y="207.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Rightarrow F \text{ vaihtelee}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/electric-motor-cutaway.webp" alt="Sininen teollisuuden sähkömoottori, josta on leikattu osa kuoresta pois. Näkyvissä ovat akseli, roottori, kuparikäämit ja tuuletin."><figcaption>Leikattu teollisuuden sähkömoottori. Virta kulkee kuparikäämeissä, ja magneettikenttä kohdistaa voiman roottorin johtimiin, jolloin akseli pyörii. Tämä vaihtovirtamoottori on rakenteeltaan erilainen kuin tunnin tasavirtamoottori, mutta perusilmiö on sama: magneettikenttä työntää virtajohdinta.</figcaption></figure>

## Kaava: Voima virtajohtimeen
Kun suorassa johtimessa kulkee virta $I$ ja johdin on homogeenisessa magneettikentässä, kenttä kohdistaa johtimeen voiman, jonka suuruus on
```kaavat
suoraan johtimeen kohdistuva magneettinen voima :: F = I l B \sin\alpha
```
missä $F$ on voima (N), $I$ virta (A), $l$ kentässä olevan johtimen osan pituus (m), $B$ magneettivuon tiheys (T) ja $\alpha$ johtimen ja kentän välinen kulma. Voimaa synnyttää vain kentän johtimeen kohtisuora komponentti $B \sin\alpha$. Voima on suurin, kun johdin on kohtisuorassa kenttää vastaan ($\sin 90^\circ = 1$), ja nolla, kun johdin on kentän suuntainen ($\sin 0^\circ = 0$). Kulmassa $30^\circ$ voima on puolet suurimmasta arvosta, koska $\sin 30^\circ = 0{,}5$. Kaavasta saadaan teslan yksikkö: $1\,\text{T} = 1\,\tfrac{\text{N}}{\text{A}\cdot\text{m}}$.

<svg data-fig="angle" viewBox="0 0 600 340" role="img" aria-label="Periaatekuva ylhäältä, ei mittakaavassa. Vaakasuorat vihreät kenttäviivat osoittavat oikealle. Johdin on kulmassa alfa kenttään nähden, ja virta kulkee johdinta pitkin yläoikealle. Kentän johtimeen kohtisuora komponentti B sin alfa on piirretty katkoviivalla. Voima osoittaa paperiin päin, mitä kuvaa risti ympyrän sisällä johtimen keskellä." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-4-angle.webp" x="1.2" y="0" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="527" y="19.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="230" y="156" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="376.5" y="134" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="470" y="140" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$B \sin\alpha$</div></foreignObject>
  <foreignObject x="320" y="201.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
</svg>

```pysahdy
Johtimen pituus kentässä on $0{,}50\,\text{m}$ ja virta $4{,}0\,\text{A}$. Magneettivuon tiheys on $0{,}25\,\text{T}$, ja johdin on kentän kanssa kulmassa $30^\circ$. Kuinka suuri voima johtimeen kohdistuu?
---
Voima on $F = I l B \sin\alpha = 4{,}0\,\text{A} \cdot 0{,}50\,\text{m} \cdot 0{,}25\,\text{T} \cdot \sin 30^\circ = 0{,}25\,\text{N}$.
```

### Kahden virtajohtimen välinen voima
Kahden rinnakkaisen virtajohtimen välillä on voima, koska kumpikin on toisen magneettikentässä. Luvussa *Virtajohtimen ja käämin magneettikenttä* johtimen $1$ kenttä kiertää sitä ympyröinä, ja etäisyydellä $r$ sen suuruus on $B_1$. Johtimen $2$ kohdalla kenttä on kohtisuorassa johdinta $2$ vastaan, joten johtimen $2$ osaan, jonka pituus on $l$, kohdistuu voima $F$:
```latex
\begin{aligned}
&B_1 = \frac{\mu_0 I_1}{2\pi r} \\[6pt]
&F = I_2 l B_1 \\
&\quad = \frac{\mu_0 I_1 I_2 l}{2\pi r}
\end{aligned}
```
missä $I_1$ ja $I_2$ ovat johtimien virrat (A), $r$ johtimien välinen etäisyys (m), $l$ rinnakkain kulkevan osan pituus (m) ja $\mu_0 \approx 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}}$ tyhjiön permeabiliteetti. Newtonin kolmannen lain mukaan johtimeen $1$ kohdistuu yhtä suuri ja vastakkaissuuntainen voima. Oikean käden säännöstä seuraa, että **samansuuntaiset virrat vetävät toisiaan puoleensa ja vastakkaissuuntaiset hylkivät**. Vuoteen 2019 asti ampeeri määriteltiin tämän voiman avulla: virta on $1\,\text{A}$, kun $1\,\text{m}$:n päässä toisistaan olevien johtimien välinen voima on $2 \cdot 10^{-7}\,\text{N}$ jokaista johtimen metriä kohti.

<svg data-fig="wires" viewBox="0 0 600 360" role="img" aria-label="Kaksi periaatekuvaa rinnakkaisista johtimista päästä päin, ei mittakaavassa. Vasemmalla kummassakin johtimessa virta kulkee paperista ulos. Vasemman johtimen magneettikenttä kiertää sitä vastapäivään, ja oikean johtimen kohdalla kenttä osoittaa ylöspäin. Voimat osoittavat johtimesta toiseen: johtimet vetävät toisiaan puoleensa. Oikealla virrat ovat vastakkaissuuntaiset, oikean johtimen virta kulkee paperiin päin, ja voimat osoittavat poispäin toisistaan: johtimet hylkivät toisiaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-4-wires.webp" x="0" y="0" width="600" height="370" preserveAspectRatio="none"/>
  <foreignObject x="15" y="13.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{samansuuntaiset virrat}$</div></foreignObject>
  <foreignObject x="325" y="13.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{vastakkaiset virrat}$</div></foreignObject>
  <foreignObject x="207" y="121.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_1$</div></foreignObject>
  <foreignObject x="88.5" y="213.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1$</div></foreignObject>
  <foreignObject x="209" y="217.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_2$</div></foreignObject>
  <foreignObject x="133.5" y="149.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="90" y="321.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{vetävät}$</div></foreignObject>
  <foreignObject x="507" y="121.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_1$</div></foreignObject>
  <foreignObject x="388.5" y="213.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1$</div></foreignObject>
  <foreignObject x="509" y="217.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_2$</div></foreignObject>
  <foreignObject x="354.5" y="149.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="390" y="321.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hylkivät}$</div></foreignObject>
</svg>

## Esimerkki
Kaiuttimen puhekelassa on $60$ kierrosta ohutta johdinta, ja kelan säde on $1{,}3\,\text{cm}$. Kela on magneetin raossa, jossa säteittäisen magneettikentän magneettivuon tiheys on $0{,}95\,\text{T}$, ja kenttä on joka kohdassa kohtisuorassa johdinta vastaan. Kuinka suuri voima kelaan kohdistuu, kun virta on huippuarvossaan $1{,}5\,\text{A}$?

<!-- vaihe -->

**Tunnetut ja kysytty.** Kierrosten lukumäärä $N = 60$, kelan säde $r = 1{,}3\,\text{cm}$, magneettivuon tiheys $B = 0{,}95\,\text{T}$, virta $I = 1{,}5\,\text{A}$ ja johtimen ja kentän välinen kulma $\alpha = 90^\circ$.

Kysytään kelaan kohdistuvaa voimaa $F$.

<!-- vaihe -->

**Periaate.** Kenttä on säteittäinen, joten jokainen kelan johtimen kohta on kohtisuorassa kenttää vastaan, ja jokaiseen kohtaan kohdistuva voima osoittaa samaan suuntaan, kelan akselin suuntaan. Siksi voimat summautuvat, ja kaavassa $F = I l B \sin\alpha$ pituus $l$ on koko kelan johtimen pituus: $N$ kierrosta, joista kunkin pituus on ympyrän kehä $2\pi r$.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&l = N \cdot 2\pi r \\
&F = I l B \sin 90^\circ = I l B
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Säde metreinä: $r = 1{,}3\,\text{cm} = 1{,}3 \cdot 0{,}01\,\text{m} = 0{,}013\,\text{m}$. Muut suureet ovat SI-yksiköissä.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin johtimen pituus ja sitten voima:
```latex
\begin{aligned}
&l = N \cdot 2\pi r \\
&= 60 \cdot 2\pi \cdot 0{,}013\,\text{m} \\
&= 4{,}9009\,\text{m} \\[6pt]
&F = I l B \\
&= 1{,}5\,\text{A} \cdot 4{,}9009\,\text{m} \cdot 0{,}95\,\text{T} \\
&= 6{,}984\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kelaan kohdistuu voima $F \approx 7{,}0\,\text{N}$ kelan akselin suuntaan. Tulos ilmoitetaan kahdella merkitsevällä numerolla, kuten säde $1{,}3\,\text{cm}$ ja virta $1{,}5\,\text{A}$.

<!-- vaihe -->

**Järkevyys.** Yksiköt sopivat: $\text{A} \cdot \text{m} \cdot \text{T} = \text{A} \cdot \text{m} \cdot \tfrac{\text{N}}{\text{A}\cdot\text{m}} = \text{N}$. Jos kartion ja kelan massa on noin $10\,\text{g}$, niiden paino on vain noin $0{,}1\,\text{N}$, joten voima on noin $70$-kertainen painoon verrattuna. Se on uskottavaa, koska kartion täytyy kiihtyä edestakaisin satoja kertoja sekunnissa.

## Yleinen virhekäsitys
Moni ajattelee, että magneetti vetää johdinta puoleensa ja johdin liikkuu kenttäviivojen suuntaan kohti toista napaa. Voima on kuitenkin **kohtisuorassa** kenttää vastaan, ja kupari- tai alumiinijohtimeen kohdistuu voima vain silloin, kun siinä kulkee virta. Kun virran suunta käännetään, johdin liikkuu vastakkaiseen suuntaan, vaikka magneetti on sama. Toinen yleinen virhe on päätellä varauksista, että samansuuntaiset virrat hylkivät toisiaan. Johtimien välinen voima on magneettinen, ja samansuuntaiset virrat vetävät toisiaan puoleensa. Kolmas virhe on käyttää kaavassa kosinia: kulma $\alpha$ on johtimen ja kentän välinen, ja voima on nolla, kun johdin on kentän suuntainen.

## Tiivistelmä
- Magneettikenttä kohdistaa virtajohtimeen voiman $F = I l B \sin\alpha$, missä $\alpha$ on johtimen ja kentän välinen kulma. Voima on suurin, kun johdin on kohtisuorassa kenttää vastaan, ja nolla, kun johdin on kentän suuntainen.
- Voima on kohtisuorassa sekä virtaa että kenttää vastaan; suunta saadaan oikean käden säännöllä, ja se kääntyy, kun virran tai kentän suunta kääntyy.
- Samansuuntaiset virrat vetävät toisiaan puoleensa, vastakkaissuuntaiset hylkivät. Voima on $F = I_2 l B_1$, missä $B_1 = \mu_0 I_1 : (2\pi r)$.
- Tasavirtamoottorissa voimat kääntävät virtasilmukkaa, ja kommutaattori vaihtaa virran suunnan joka puolikierroksella.
- Kaiuttimessa vaihtovirta säteittäisessä kentässä työntää puhekelaa ja kartiota edestakaisin signaalin tahdissa.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: kuulokkeet ja älypuhelin pöydällä. Kuulokkeiden kummassakin kuvussa on pieni kaiutin, ja kuvuista lähtee ääniaaltoja." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-4-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
