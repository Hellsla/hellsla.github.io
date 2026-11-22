# Lenzin laki ja pyörrevirrat

> **Miksi** voimakas magneetti putoaa kupariputken läpi monta sekuntia, vaikka kupari ei ole magneettista ja tavallinen kappale putoaa saman matkan alle sekunnissa?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion pöydällä seisoo telineessä pystysuora kupariputki ja sen vieressä läpinäkyvä muoviputki. Kupariputken alapäästä on juuri tulossa ulos pieni magneetti pehmeän alustan yläpuolella. Pöydällä on sekuntikello, joka näyttää kuluneen useita sekunteja." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-6-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Induktiovirta vastustaa muutosta
Luvussa *Sähkömagneettinen induktio* suljettuun johdinsilmukkaan syntyi induktiovirta aina, kun silmukan läpi kulkeva magneettivuo muuttui. Virran suunta noudattaa yhtä sääntöä, **Lenzin lakia**: *induktiovirran suunta on aina sellainen, että sen oma magneettikenttä vastustaa sitä muutosta, joka induktiovirran synnyttää.* Kun magneetin N-napa työnnetään kohti kuparirengasta, renkaan läpi kulkeva vuo kasvaa. Renkaan induktiovirta tekee renkaasta pienen magneetin, jonka magneetin puoleinen sivu on N-napa, joten rengas hylkii lähestyvää magneettia. Kun magneetti vedetään pois, vuo pienenee. Nyt virta kiertää toiseen suuntaan, renkaan magneetin puoleinen sivu on S-napa, ja rengas vetää magneettia takaisin. Kummassakin tapauksessa renkaan voima vastustaa magneetin liikettä.

<svg data-fig="ring" viewBox="0 0 600 360" role="img" aria-label="Kaksi periaatekuvaa, ei mittakaavassa. Kuparirengas on leikattu paperin tasossa, joten siitä näkyvät ylä- ja alareunan poikkileikkaukset. Vasemmalla magneetti liikkuu N-napa edellä kohti rengasta. Renkaan induktiovirta kulkee yläreunassa paperiin päin ja alareunassa paperista ulos, ja sen magneettikenttä osoittaa renkaan keskellä vasemmalle, kohti magneettia: renkaan magneetin puoleinen sivu on N-napa, ja rengas hylkii magneettia. Voima magneettiin osoittaa vasemmalle, liikettä vastaan. Oikealla magneetti loittonee renkaasta. Virta on vastakkaissuuntainen, renkaan kenttä osoittaa oikealle, magneetin puoleinen sivu on S-napa, ja rengas vetää magneettia takaisin. Voima osoittaa oikealle, taas liikettä vastaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-6-ring.webp" x="0" y="0" width="600" height="368.8" preserveAspectRatio="none"/>
  <foreignObject x="30" y="13.5" width="240" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{magneetti lähestyy}$</div></foreignObject>
  <foreignObject x="330" y="13.5" width="240" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{magneetti loittonee}$</div></foreignObject>
  <foreignObject x="44" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="100" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="240" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="145" y="197.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_\text{ind}$</div></foreignObject>
  <foreignObject x="172" y="137.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="124" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="82" y="227.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="65" y="315.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rengas hylkii}$</div></foreignObject>
  <foreignObject x="344" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="400" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="540" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="445" y="197.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_\text{ind}$</div></foreignObject>
  <foreignObject x="472" y="137.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="414" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="343" y="227.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="365" y="315.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rengas vetää}$</div></foreignObject>
</svg>

```pysahdy
Magneetin S-napaa työnnetään kohti kuparirengasta. Millainen on renkaan magneetin puoleinen sivu, ja miksi?
---
Renkaan magneetin puoleinen sivu on S-napa. Renkaan läpi kulkeva vuo kasvaa, ja induktiovirran kenttä vastustaa kasvua, joten rengas hylkii magneettia.
```

### Lenzin laki on energian säilymistä
Miksi induktiovirta ei voisi auttaa muutosta? Jos lähestyvä magneetti vetäisi rengasta puoleensa, magneetti kiihtyisi kohti rengasta, vuo muuttuisi yhä nopeammin, induktiovirta kasvaisi ja veto voimistuisi. Magneetin liike-energia ja renkaan sähköenergia kasvaisivat ilman, että kukaan tekisi työtä: syntyisi ikiliikkuja, joka tuottaa energiaa tyhjästä. Energian säilyminen estää tämän. Siksi magneettia on liikutettava voimalla, joka tekee työtä renkaan vastustavaa voimaa vastaan, ja juuri tämä työ muuttuu induktiovirran sähköenergiaksi. Virta lämmittää johdinta, joten energia päätyy lopulta johtimen sisäenergiaksi.

### Pyörrevirrat
Induktiovirta ei tarvitse erillistä johdinsilmukkaa. Kun magneettivuo muuttuu umpinaisessa metallikappaleessa, kuten levyssä tai putken seinässä, metalliin syntyy suljettuja virtasilmukoita, **pyörrevirtoja**. Kupariputkessa putoavan magneetin alapuolella putken seinän läpi kulkeva vuo kasvaa ja yläpuolella pienenee. Lenzin lain mukaan alapuolinen pyörrevirta hylkii magneettia ja yläpuolinen vetää sitä, joten molemmat jarruttavat putoamista. Pyörrevirrat ovat sitä suurempia, mitä nopeammin magneetti liikkuu, joten myös jarruttava voima kasvaa vauhdin mukana. Kun jarruttava voima on kasvanut yhtä suureksi kuin magneetin paino, kokonaisvoima on nolla, ja magneetti putoaa tasaisella vauhdilla. Muoviputkessa ei synny virtoja, koska muovi ei johda sähköä, eikä kupariputki jarruta magnetoimatonta teräskappaletta, koska sen liike ei muuta putken läpi kulkevaa vuota.

<svg data-fig="tube" viewBox="0 0 600 380" role="img" aria-label="Periaatekuva, ei mittakaavassa. Vasemmalla pystysuora kupariputki pituussuunnassa leikattuna, ja sen sisällä putoava magneetti, jonka N-napa on alaspäin. Magneetin alapuolella putken seinässä kiertää pyörrevirta, joka kulkee oikeassa seinässä paperiin päin ja vasemmassa paperista ulos; sen kenttä osoittaa ylöspäin, kohti magneettia. Magneetin yläpuolella pyörrevirta kiertää vastakkaiseen suuntaan, ja sen kenttä osoittaa alaspäin. Magneettiin vaikuttavat alaspäin paino ja ylöspäin yhtä pitkä jarruttava voima, ja sen nopeus osoittaa alaspäin. Oikealla alempi pyörrevirtarengas ylhäältä katsottuna: virta kiertää vastapäivään, ja kenttä osoittaa renkaan keskellä kohti katsojaa eli ylöspäin." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-6-tube.webp" x="0" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="140" y="156.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="140" y="194.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="70" y="257.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="70" y="93.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="12" y="287.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_\text{ind}$</div></foreignObject>
  <foreignObject x="232" y="241.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="232" y="109.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{j}$</div></foreignObject>
  <foreignObject x="296" y="197.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="544" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="436" y="217.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_\text{ind}$</div></foreignObject>
  <foreignObject x="341" y="31.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{alempi rengas ylhäältä}$</div></foreignObject>
</svg>


<figure class="unit-photo"><img src="pics/fy7/eddy-current-brake.webp" alt="Harmaa akseli ja sen ympärillä suuri pyöreä metallilevy; levyn vieressä on laatikkomainen jarruyksikkö, jossa on johtoja ja liittimiä."><figcaption>Junan pyörrevirtajarru. Akselin mukana pyörivän metallilevyn vieressä on sähkömagneetteja. Kun jarrutetaan, magneettikenttä indusoi levyyn pyörrevirtoja, jotka Lenzin lain mukaan vastustavat levyn pyörimistä. Liike-energia muuttuu levyn sisäenergiaksi ilman kuluvia jarrupaloja.</figcaption></figure>

```pysahdy
Kupariputkessa putoavan magneetin vauhti kasvaa. Mitä tapahtuu jarruttavalle voimalle ja miksi?
---
Jarruttava voima kasvaa. Mitä suurempi vauhti on, sitä suuremmat pyörrevirrat ovat, ja sitä voimakkaammin ne jarruttavat.
```

### Pyörrevirtajarru, induktioliesi ja metallinilmaisin
**Induktiojarrussa** eli pyörrevirtajarrussa metallilevy tai kisko liikkuu magneettikentässä, ja pyörrevirrat jarruttavat liikettä. Vuoristoradan vaunun alle kiinnitetyt kupari- tai alumiinilevyt kulkevat radan vahvojen magneettien välistä, ja junissa jarrun sähkömagneetit ovat lähellä kiskoa. Jarru ei kulu, koska mikään ei hankaa, ja se jarruttaa sitä voimakkaammin, mitä suurempi vauhti on. Pysähtymisen lähellä jarrutus heikkenee, joten lopullinen pysäytys tarvitsee tavallisen jarrun. Induktioliedessä lasin alla olevan kelan vaihtovirta muuttaa magneettikenttää kymmeniätuhansia kertoja sekunnissa, ja pyörrevirrat lämmittävät kattilan pohjaa. Lasi ei johda sähköä, joten se lämpenee vain kuuman kattilan vaikutuksesta. Metallinilmaisimen kela synnyttää vaihtuvan kentän, ja maassa olevan metallin pyörrevirtojen oma kenttä havaitaan ilmaisimen kelassa.

### Kun pyörrevirroista on haittaa
Pyörrevirrat muuttavat sähköenergiaa aina sisäenergiaksi. Muuntajan ja sähkömoottorin rautasydämessä magneettikenttä vaihtelee jatkuvasti, ja umpinaisessa sydämessä kiertäisivät suuret pyörrevirrat, jotka kuumentaisivat sydäntä ja hukkaisivat energiaa. Siksi sydän kootaan ohuista levyistä, joiden välissä on sähköä johtamaton eristekerros. Pyörrevirrat voivat kiertää vain kunkin kapean levyn sisällä, joten ne jäävät pieniksi. Muuntajasta kerrotaan lisää luvussa *Muuntaja ja sähköenergian siirto*. Sama ajatus näkyy kupariputkessa, johon on sahattu pitkittäinen rako: rako katkaisee putken ympäri kiertävät virrat, ja magneetti putoaa paljon nopeammin. Pienemmät pyörrevirrat kiertävät yhä raon välisessä seinässä, joten jarrutus ei katoa kokonaan.

<svg data-fig="core" viewBox="0 0 600 340" role="img" aria-label="Kaksi periaatekuvaa muuntajan rautasydämen poikkileikkauksesta, ei mittakaavassa. Vaihtuva magneettikenttä osoittaa sydämen pituussuunnassa paperiin päin, mitä kuvaavat vihreät ristit. Vasemmalla umpinainen rautasydän: siinä kiertää yksi suuri pyörrevirtasilmukka koko poikkileikkauksen ympäri. Oikealla sydän on koottu ohuista levyistä, joiden välissä on eristekerros: pyörrevirrat kiertävät vain kunkin kapean levyn sisällä pieninä ja heikkoina silmukoina." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-6-core.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="40" y="13.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{umpinainen sydän}$</div></foreignObject>
  <foreignObject x="325" y="13.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{levyistä koottu sydän}$</div></foreignObject>
  <foreignObject x="50" y="295.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{suuri pyörrevirta}$</div></foreignObject>
  <foreignObject x="355" y="295.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{eristetyt levyt}$</div></foreignObject>
  <foreignObject x="365" y="49.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}\ \text{paperiin}$</div></foreignObject>
</svg>

## Kaava: Lenzin laki ja energia
Luvun *Sähkömagneettinen induktio* induktiolain miinusmerkki on Lenzin laki:
```kaavat
käämiin indusoituva jännite :: e_\text{ka} = -N \frac{\Delta \Phi}{\Delta t}
```
missä $e_\text{ka}$ on keskimääräinen induktiojännite (V) aikavälillä $\Delta t$, $N$ silmukan kierrosten lukumäärä, $\Delta\Phi$ magneettivuon muutos (Wb) ja $\Delta t$ muutokseen kulunut aika (s). Kun vuo muuttuu tasaisesti, jännite on vakio, ja merkitään lyhyesti $e$. Miinusmerkki kertoo, että induktiovirran kenttä vastustaa vuon muutosta. Suuruus lasketaan ilman merkkiä, ja suunta päätellään Lenzin laista.

Energian säilyminen kertoo, mihin putoavan magneetin energia menee. Kun magneetti putoaa korkeuden $h$, sen potentiaalienergia pienenee määrän $mgh$. Osa muuttuu liike-energiaksi ja loput pyörrevirtojen kautta putken sisäenergiaksi $Q$:
```latex
\begin{aligned}
&mgh = \tfrac{1}{2} m v^2 + Q \\
&Q = mgh - \tfrac{1}{2} m v^2
\end{aligned}
```
missä $m$ on magneetin massa (kg), $g = 9{,}81\,\text{m/s}^2$, $h$ pudotuskorkeus (m), $v$ vauhti lopussa (m/s) ja $Q$ sisäenergiaksi muuttunut energia (J). Kun magneetti putoaa tasaisella vauhdilla, jarruttava voima $F$ on yhtä suuri kuin paino $mg$. Ajassa $\Delta t$ voima vaikuttaa matkalla $v \Delta t$ ja tekee työn $F v \Delta t$, joten sisäenergia kasvaa teholla
```kaavat
hetkellinen teho :: P = F v
```
missä $P$ on teho (W), $F$ jarruttava voima (N) ja $v$ vauhti (m/s). Sama kaava pätee jokaiseen pyörrevirtajarruun: jarruttava voima kertaa vauhti on teho, jolla liike-energia muuttuu sisäenergiaksi.

<svg data-fig="energy" viewBox="0 0 600 360" role="img" aria-label="Pylväskuvaaja mittakaavassa: energiat, kun 20 gramman magneetti on pudonnut metrin pituisen putken läpi. Muoviputkessa potentiaalienergian väheneminen 196 millijoulea on kokonaan muuttunut liike-energiaksi, eikä sisäenergiaa synny. Kupariputkessa potentiaalienergia vähenee yhtä paljon, mutta liike-energiaa on vain 0,2 millijoulea, niin vähän ettei pylväs näy, ja lähes kaikki, 196 millijoulea, on muuttunut putken sisäenergiaksi." style="max-width:100%;font-size:24px">
  <line x1="100" y1="227.5" x2="560" y2="227.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="175" x2="560" y2="175" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="122.5" x2="560" y2="122.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="70" x2="560" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="280" x2="574" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M586,280 L573,286 L573,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="281" x2="100" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,44 L106,57 L94,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="93" y1="227.5" x2="100" y2="227.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="213" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="93" y1="175" x2="100" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="160.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="93" y1="122.5" x2="100" y2="122.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="108" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="93" y1="70" x2="100" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="55.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <foreignObject x="70" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="90" y="13.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E\ (\text{mJ})$</div></foreignObject>
  <rect x="139.5" y="74" width="46" height="206" fill="#6b7480"/>
  <foreignObject x="140" y="287.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta E_\text{p}$</div></foreignObject>
  <rect x="198.5" y="74" width="46" height="206" fill="#1971c2"/>
  <foreignObject x="205" y="287.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$E_\text{k}$</div></foreignObject>
  <foreignObject x="270.5" y="287.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$Q$</div></foreignObject>
  <foreignObject x="146.5" y="327.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{muoviputki}$</div></foreignObject>
  <rect x="363" y="74" width="46" height="206" fill="#6b7480"/>
  <foreignObject x="363.5" y="287.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta E_\text{p}$</div></foreignObject>
  <foreignObject x="428.5" y="287.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$E_\text{k}$</div></foreignObject>
  <rect x="481" y="74" width="46" height="206" fill="#e8590c"/>
  <foreignObject x="494" y="287.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$Q$</div></foreignObject>
  <foreignObject x="370" y="327.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kupariputki}$</div></foreignObject>
  <line x1="445" y1="276" x2="445" y2="217" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <foreignObject x="403.5" y="192" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$0{,}2\,\text{mJ}$</span></div></foreignObject>
</svg>

```pysahdy
Magneetin massa on $20\,\text{g}$, ja se putoaa kupariputkessa tasaisella vauhdilla $0{,}30\,\text{m/s}$. Millä teholla putken sisäenergia kasvaa?
---
Jarruttava voima on yhtä suuri kuin paino: $F = mg = 0{,}020\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 \approx 0{,}196\,\text{N}$. Teho on $P = Fv \approx 0{,}196\,\text{N}\cdot 0{,}30\,\text{m/s} \approx 0{,}059\,\text{W}$.
```

## Esimerkki
Opiskelija pudottaa $25\,\text{g}$:n neodyymimagneetin $1{,}20\,\text{m}$:n pituiseen pystysuoraan kupariputkeen ja mittaa, että magneetti tulee putken alapäästä ulos $8{,}0\,\text{s}$:n kuluttua. Magneetti putoaa lähes koko matkan tasaisella vauhdilla. Kuinka paljon putken sisäenergia kasvaa putoamisen aikana?

<!-- vaihe -->

**Tunnetut ja kysytty.** Magneetin massa $m = 25\,\text{g}$, putken pituus eli pudotuskorkeus $h = 1{,}20\,\text{m}$, putoamisaika $t = 8{,}0\,\text{s}$ ja $g = 9{,}81\,\text{m/s}^2$.

Kysytään putken sisäenergian kasvua $Q$.

<!-- vaihe -->

**Periaate.** Energia säilyy: pyörrevirrat muuttavat sen osan potentiaalienergian vähenemisestä, joka ei jää magneetin liike-energiaksi, putken sisäenergiaksi. Ilmanvastus on näin pienellä vauhdilla merkityksetön. Vauhti on lähes koko matkan sama, joten se saadaan matkasta ja ajasta.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&v = \frac{h}{t} \\
&Q = mgh - \tfrac{1}{2} m v^2
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Massa kilogrammoina: $m = 25\,\text{g} = 25 \cdot 0{,}001\,\text{kg} = 0{,}025\,\text{kg}$. Muut suureet ovat SI-yksiköissä.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin vauhti ja sitten energia:
```latex
\begin{aligned}
&v = \frac{h}{t} \\
&= \frac{1{,}20\,\text{m}}{8{,}0\,\text{s}} \\
&= 0{,}15\,\text{m/s} \\[6pt]
&Q = mgh - \tfrac{1}{2} m v^2 \\
&= 0{,}025\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \cdot 1{,}20\,\text{m} \\
&\quad - \tfrac{1}{2} \cdot 0{,}025\,\text{kg} \cdot (0{,}15\,\text{m/s})^2 \\
&= 0{,}29430\,\text{J} - 0{,}00028\,\text{J} \\
&= 0{,}29402\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Putken sisäenergia kasvaa noin $0{,}29\,\text{J}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla, kuten massa $25\,\text{g}$ ja aika $8{,}0\,\text{s}$.

<!-- vaihe -->

**Järkevyys.** Liike-energiaksi jää vain noin $0{,}1\,\%$ potentiaalienergian vähenemisestä, joten lähes kaikki energia lämmittää putkea, kuten tasaisessa putoamisessa pitääkin. Jos putken massa on $0{,}30\,\text{kg}$, kuparin ominaislämpökapasiteetti $385\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$ antaa lämpötilan nousuksi vain noin $0{,}003\,\text{K}$: siksi putki ei tunnu lämpenevän.

## Yleinen virhekäsitys
Moni ajattelee, että kupariputki hidastaa magneettia, koska magneetti tarttuu kupariin. Kupari ei kuitenkaan ole ferromagneettinen aine: levossa oleva magneetti ei tartu kupariputken seinään, eikä putki jarruta samanmuotoista magnetoimatonta teräskappaletta lainkaan. Jarrutus syntyy vain liikkeestä, koska vain liikkuva magneetti muuttaa putken läpi kulkevaa vuota. Toinen yleinen virhe on sanoa, että induktiovirran kenttä on aina magneetin kenttää vastaan. Lenzin laki ei vastusta kenttää vaan sen **muutosta**. Kun magneetti loittonee renkaasta, renkaan läpi kulkeva vuo pienenee, ja induktiovirran kenttä osoittaa renkaan keskellä samaan suuntaan kuin magneetin kenttä, jolloin rengas vetää magneettia puoleensa.

## Tiivistelmä
- Lenzin laki: induktiovirran oma magneettikenttä vastustaa sitä muutosta, joka induktiovirran synnyttää. Lähestyvää magneettia rengas hylkii, loittonevaa se vetää.
- Lenzin laki seuraa energian säilymisestä. Työ, joka tehdään magneettia liikutettaessa, muuttuu induktiovirran sähköenergiaksi ja edelleen johtimen sisäenergiaksi: $Q = mgh - \tfrac{1}{2} m v^2$.
- Metallikappaleeseen syntyy muuttuvassa magneettikentässä pyörrevirtoja. Ne jarruttavat liikettä sitä voimakkaammin, mitä suurempi vauhti on, ja jarrutuksen teho on $P = F v$.
- Pyörrevirtoja hyödynnetään induktiojarrussa, induktioliedessä ja metallinilmaisimessa. Muuntajan ja moottorin rautasydän kootaan eristetyistä levyistä, jotta pyörrevirrat ja niiden energiahäviö jäävät pieniksi.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: induktioliesi, jonka lasipinnalla on teräskattila. Kattilassa vesi kiehuu ja siitä nousee höyryä. Lasipinnan alla näkyy leikkauskuvana kuparinen kela. Liekkiä tai hehkuvaa levyä ei ole." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-6-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
