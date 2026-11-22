# Virtajohtimen ja käämin magneettikenttä

> **Miksi** romuttamon nosturin magneetti nostaa tonnin painoisen autonromun ilmaan ja päästää sen irti napin painalluksella, vaikka jääkaappimagneetti ei päästä irti koskaan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: romuttamon nosturi. Nosturin puomin päästä riippuu ketjuissa pyöreä harmaa sähkömagneetti. Se pitää ruosteista autonromua kiinni pohjassaan ja nostaa sen irti romukasan päältä. Taustalla on romukasoja ja taivas." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-3-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Sähkövirta synnyttää magneettikentän
Vuonna 1820 tanskalainen Hans Christian Ørsted piti luennon. Hän huomasi, että kompassin neula kääntyi, kun viereiseen johtimeen kytkettiin virta. Kun virta katkaistiin, neula palasi osoittamaan pohjoiseen. Havainto yhdisti sähkön ja magnetismin: **jokaisen virtajohtimen ympärillä on magneettikenttä**. Virtajohdin on johdin, jossa kulkee sähkövirta.

Kenttä syntyy liikkuvista varauksista. Siksi johtimen ei tarvitse olla magneettista ainetta. Kuparijohdinkin synnyttää kentän. Kun virta kasvaa, kenttä voimistuu. Kun virran suunta vaihtuu, myös kentän suunta vaihtuu.

Suoran johtimen kenttäviivat ovat johtimen ympärillä samankeskisiä ympyröitä. Ympyrät ovat kohtisuorassa johdinta vastaan. Kenttä ei siis osoita johtimesta poispäin eikä johdinta kohti. Se kiertää johdinta. Johtimen ympärille asetetut kompassit kääntyvät ympyrän tangentin suuntaan. Tangentti on suora, joka koskettaa ympyrää yhdessä pisteessä. Näin käy, kun johtimen kenttä on paljon Maan magneettikenttää voimakkaampi. Mitä kauempana johtimesta ollaan, sitä heikompi kenttä on.

<svg data-fig="wire-field" viewBox="0 0 600 372" role="img" aria-label="Kaavakuva, ei mittakaavassa. Kuvassa on kaksi osaa. Vasemmalla on pystysuora virtajohdin pöytälevyn läpi sivulta katsottuna. Violetti nuoli osoittaa virran ylöspäin. Johtimen ympärillä on kolme vihreää ympyränmuotoista kenttäviivaa. Niiden nuolet kiertävät ylhäältä katsottuna vastapäivään. Oikealla on sama tilanne ylhäältä. Johdin on piste ympyrän sisällä, koska virta tulee kohti katsojaa. Sen ympärillä on kolme samankeskistä kenttäviivaa vastapäivään. Kenttäviivoilla on neljä kompassia. Jokaisen neulan pohjoispää on vaaleanpunainen ja osoittaa kenttäviivan suuntaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-3-wire-field.webp" x="0" y="1.2" width="600" height="380" preserveAspectRatio="none"/>
  <foreignObject x="102.5" y="9.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sivulta}$</div></foreignObject>
  <foreignObject x="396" y="9.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ylhäältä}$</div></foreignObject>
  <foreignObject x="186" y="303.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="250" y="145.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="470" y="209.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="554" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/compass-needles-wire.webp" alt="Sininen johdin menee levyn läpi. Sen ympärillä on neljä riviä pieniä kompassineuloja."><figcaption>Pieniä kompassineuloja johtimen ympärillä. Johtimessa kulkee sähkövirta. Lähellä johdinta neulat kääntyvät kenttäviivojen suuntaan. Kenttäviivat kiertävät johdinta.</figcaption></figure>

### Oikean käden sääntö
Kentän kiertosuunnan saat **oikean käden säännöllä**. Osoita oikean käden peukalolla virran suuntaan. Silloin koukistetut sormet kiertävät kenttäviivojen suuntaan. Kuvassa virta kulkee ylöspäin, joten ylhäältä katsottuna kenttä kiertää vastapäivään. Kuvissa virta kohti katsojaa merkitään pisteellä $\odot$ ja virta poispäin katsojasta ristillä $\otimes$. Merkit muistuttavat nuolen kärkeä ja sulkia.

```pysahdy
Pystysuorassa johtimessa virta kulkee alaspäin. Mihin suuntaan johtimen kenttä kiertää, kun katsot johdinta ylhäältä?
---
Peukalo osoittaa virran suuntaan eli alas. Silloin sormet kiertävät ylhäältä katsottuna myötäpäivään. Kenttä kiertää siis myötäpäivään.
```

### Käämin kenttä
Kun johdin kierretään kierukaksi, syntyy **käämi**. Jokaisen kierroksen kenttä osoittaa käämin sisällä samaan suuntaan, ja kentät vahvistavat toisiaan. Pitkän käämin sisällä kenttäviivat ovat lähes suoria ja tasavälisiä. Kenttä on silloin lähes homogeeninen, eli se on samanlainen joka kohdassa käämin sisällä. Se on käämin akselin suuntainen.

Käämin päissä kenttäviivat levenevät. Käämin ulkopuolella kenttä on samanlainen kuin sauvamagneetin kenttä luvussa *Magneetit, magneettinen dipoli ja magneettikenttä*. Pää, josta kenttäviivat tulevat ulos, on pohjoisnapa N.

Oikean käden sääntö toimii myös käämille. Kierrä sormet kierroksia pitkin virran suuntaan. Silloin peukalo osoittaa käämin sisällä kentän suuntaan eli kohti pohjoisnapaa.

<svg data-fig="coil-field" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei mittakaavassa. Kuvassa on pitkä käämi pituussuunnassa leikattuna. Ylärivin johdinpoikkileikkauksissa on piste, eli virta tulee kohti katsojaa. Alarivin poikkileikkauksissa on risti, eli virta menee poispäin katsojasta. Käämin sisällä vihreät kenttäviivat ovat suoria, tasavälisiä ja oikealle osoittavia. Kenttä on siis lähes homogeeninen. Ulkona kenttäviivat kaartuvat oikeasta päästä takaisin vasempaan. Oikea pää on pohjoisnapa N ja vasen pää eteläpää S, kuten sauvamagneetissa." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-3-coil-field.webp" x="0" y="0" width="600" height="370" preserveAspectRatio="none"/>
  <foreignObject x="492" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="89" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="372" y="147.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\overline{B}$</span></div></foreignObject>
  <foreignObject x="90" y="9.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{virta: } \odot \text{ kohti katsojaa, } \otimes \text{ poispäin}$</div></foreignObject>
  <foreignObject x="100" y="321.5" width="400" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sisällä lähes homogeeninen kenttä}$</div></foreignObject>
</svg>

```pysahdy
Pitkässä käämissä virta kiertää myötäpäivään, kun katsot käämiä päästä $P$. Onko pää $P$ käämin pohjoisnapa vai eteläpää?
---
Kun oikean käden sormet kiertävät kierroksia pitkin virran suuntaan, peukalo osoittaa kentän suuntaan. Se osoittaa nyt pois päästä $P$. Kenttäviivat tulevat ulos käämin toisesta päästä, joten se pää on pohjoisnapa. Pää $P$ on eteläpää.
```

### Sähkömagneetti
Kun käämin sisään työnnetään rautasydän, kenttä voimistuu moninkertaiseksi. Käämin kenttä kääntää raudan alkeisalueet samansuuntaisiksi. Alkeisalue on raudan pieni osa, joka toimii kuin pieni magneetti. Kun alkeisalueet osoittavat samaan suuntaan, rauta magnetoituu. Magnetoitunut rauta lisää oman kenttänsä käämin kenttään. Tällainen käämi on **sähkömagneetti**.

Kun virta katkaistaan, käämin kenttä häviää. Pehmeän raudan alkeisalueet palaavat lähes epäjärjestykseen, joten sydän menettää magnetoitumansa lähes kokonaan. Siksi romuttamon nosturi pitää romua vain niin kauan kuin virta kulkee. Kestomagneetti on toisenlainen. Sen alkeisalueet pysyvät järjestyksessä, joten sitä ei voi kytkeä pois.

<svg data-fig="electromagnet" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei mittakaavassa. Kuvassa on sähkömagneetti. Pystysuoran harmaan rautasydämen ympärille on kierretty kuparinen käämi. Käämin johtimet menevät paristoon ja kytkimeen. Vasemmalla kytkin on kiinni ja virta kulkee. Rautasydämen alapää vetää puoleensa rautanauloja, jotka roikkuvat siinä ketjuna. Oikealla sama sähkömagneetti on kytkin auki, eli kytkin on avattu. Kytkimen terä on nostettu irti kärjestä, virtapiiri on katkennut ja naulat ovat pudonneet pöydälle." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-3-electromagnet.webp" x="1.2" y="1.2" width="597" height="366.9" preserveAspectRatio="none"/>
  <foreignObject x="77.5" y="9.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{virta kulkee}$</div></foreignObject>
  <foreignObject x="358.5" y="9.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{virta katkaistu}$</div></foreignObject>
  <foreignObject x="191" y="221.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="44" y="145.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{rauta}$</div></foreignObject>
  <foreignObject x="330" y="145.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{rauta}$</div></foreignObject>
</svg>

## Kaava: Suoran johtimen ja käämin magneettikenttä
Pitkän suoran johtimen magneettivuon tiheys etäisyydellä $r$ johtimesta on
```kaavat
suoran virtajohtimen magneettivuon tiheys :: B = \frac{\mu_0 I}{2\pi r}
```
Kaavassa $B$ on magneettivuon tiheys (T) ja $I$ on johtimen virta (A). Symboli $r$ on etäisyys johtimesta (m). Vakio $\mu_0 \approx 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}}$ on tyhjiön permeabiliteetti. Se on luonnonvakio. Ilmassa käytetään samaa arvoa.

Kenttä on suoraan verrannollinen virtaan ja kääntäen verrannollinen etäisyyteen. Kun etäisyys kaksinkertaistuu, kenttä puolittuu. Kaava pätee, kun johdin on paljon pidempi kuin etäisyys $r$ ja muut johtimet ovat kaukana. Esimerkiksi $10\,\text{A}$:n johtimen kenttä on $1\,\text{cm}$:n etäisyydellä $200\,\mu\text{T}$. Se on noin nelinkertainen Maan magneettikenttään noin $50\,\mu\text{T}$ verrattuna.

<svg data-fig="wire-graph" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa. Se näyttää suoran johtimen magneettivuon tiheyden B mikrotesloina etäisyyden r funktiona senttimetreinä, kun virta on 10 A. Käyrä laskee etäisyyden kasvaessa. Etäisyydellä 1 cm on B 200 µT, etäisyydellä 2 cm 100 µT ja etäisyydellä 4 cm 50 µT. Kun etäisyys kaksinkertaistuu, kenttä puolittuu." style="max-width:100%;font-size:24px">
  <line x1="171" y1="290" x2="171" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="245.5" y1="290" x2="245.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320.5" y1="290" x2="320.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="395" y1="290" x2="395" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="243" x2="470" y2="243" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="196.5" x2="470" y2="196.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="149.5" x2="470" y2="149.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="103" x2="470" y2="103" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="56" x2="470" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,30 L102,43 L90,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="171" y1="290" x2="171" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="161" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="245.5" y1="290" x2="245.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="235.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="320.5" y1="290" x2="320.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="310.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="395" y1="290" x2="395" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="385" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="460" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="89" y1="243" x2="96" y2="243" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="228.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="196.5" x2="96" y2="196.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="182" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="149.5" x2="96" y2="149.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="135" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="89" y1="103" x2="96" y2="103" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="88.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="89" y1="56" x2="96" y2="56" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="41.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r\ (\text{cm})$</div></foreignObject>
  <foreignObject x="86" y="-0.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$B\ (\mu\text{T})$</div></foreignObject>
  <polyline points="156,56 158.5,66 161,75 163.5,83 166.5,91 169,98 171.5,104.5 174,111 177,116.5 179.5,122 182,127 184.5,132 187.5,136.5 190,141 192.5,145 195,148.5 197.5,152.5 200.5,156 203,159 205.5,162 208,165 211,168 213.5,171 216,173.5 218.5,176 221.5,178 224,180.5 226.5,182.5 229,185 232,187 234.5,189 237,190.5 239.5,192.5 242,194 245,196 247.5,197.5 250,199 252.5,200.5 255.5,202 258,203.5 260.5,205 263,206 266,207.5 268.5,209 271,210 273.5,211 276.5,212.5 279,213.5 281.5,214.5 284,215.5 286.5,216.5 289.5,217.5 292,218.5 294.5,219.5 297,220.5 300,221.5 302.5,222 305,223 307.5,224 310.5,224.5 313,225.5 315.5,226 318,227 321,227.5 323.5,228.5 326,229 328.5,230 331,230.5 334,231 336.5,232 339,232.5 341.5,233 344.5,233.5 347,234 349.5,235 352,235.5 355,236 357.5,236.5 360,237 362.5,237.5 365.5,238 368,238.5 370.5,239 373,239.5 376,240 378.5,240.5 381,241 383.5,241.5 386,242 389,242 391.5,242.5 394,243 396.5,243.5 399.5,244 402,244 404.5,244.5 407,245 410,245.5 412.5,245.5 415,246 417.5,246.5 420.5,247 423,247 425.5,247.5 428,248 430.5,248 433.5,248.5 436,249 438.5,249 441,249.5 444,249.5 446.5,250 449,250.5 451.5,250.5 454.5,251 457,251 459.5,251.5 462,252 465,252 467.5,252.5 470,252.5" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="171" y1="103" x2="171" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="103" x2="171" y2="103" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="171" cy="103" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <line x1="245.5" y1="196.5" x2="245.5" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="196.5" x2="245.5" y2="196.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="245.5" cy="196.5" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <line x1="395" y1="243" x2="395" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="243" x2="395" y2="243" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="395" cy="243" r="6.5" fill="#2b8a3e" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="268" y="83.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$I = 10\,\text{A}$</div></foreignObject>
</svg>

Pitkän käämin sisällä, kaukana sen päistä, magneettivuon tiheys on
```kaavat
pitkän käämin magneettivuon tiheys :: B = \mu_0 \frac{N I}{l}
```
Kaavassa $N$ on käämin kierrosten lukumäärä ja $I$ on virta (A). Symboli $l$ on käämin pituus (m).

Kenttä riippuu kierrostiheydestä $N : l$. Se kertoo, kuinka monta kierrosta on yhdellä metrillä. Kenttä ei riipu käämin paksuudesta. Kaava pätee, kun käämi on paljon pidempi kuin paksu ja sen sisällä on vain ilmaa. Käämin päissä kenttä on noin puolet keskikohdan arvosta. Rautasydän voimistaa kenttää moninkertaiseksi.

<svg data-fig="coil-dims" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva, ei mittakaavassa. Kuvassa on käämi sivulta. Käämissä on N kierrosta kuparijohdinta pituudella l. Johtimen päistä kulkee virta I, joka on merkitty violetilla nuolella. Käämin sisällä vihreä nuoli osoittaa akselin suuntaan. Nuolen merkintä B on käämin vasemmalla puolella, samalla korkeudella kuin nuoli." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-3-coil-dims.webp" x="0" y="1.2" width="597" height="338.3" preserveAspectRatio="none"/>
  <foreignObject x="73" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="60" y="253.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="255" y="15.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$l$</div></foreignObject>
  <foreignObject x="426" y="135.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N\ \text{kierrosta}$</div></foreignObject>
</svg>

```pysahdy
Pitkässä käämissä on $500$ kierrosta, ja sen pituus on $0{,}250\,\text{m}$. Käämissä kulkee virta $1{,}00\,\text{A}$. Kuinka suuri on magneettivuon tiheys käämin keskellä?
---
Kaavan mukaan $B = \mu_0 \tfrac{N I}{l} = 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}} \cdot \tfrac{500 \cdot 1{,}00\,\text{A}}{0{,}250\,\text{m}} \approx 2{,}51\,\text{mT}$.
```

### Magneettivuon tiheyden määrittäminen käämin sisällä
Kenttää mitataan magneettikenttäanturilla. Anturin kärki asetetaan käämin keskelle akselin suuntaiseksi. Virtaa muutetaan virtalähteellä. Jokaisella virralla kirjataan virta ja anturin lukema $B$.

Piirrä mittauspisteet $(I, B)$-koordinaatistoon esimerkiksi Vernier Graphical Analysis -ohjelmalla. Sovita pisteisiin suora $B = A I + B_0$. Kaavan mukaan kulmakerroin on $A = \mu_0 \tfrac{N}{l}$. Siksi mittauksesta saat tyhjiön permeabiliteetille arvion $\mu_0 = A l : N$.

Tuloksen epävarmuus arvioidaan näin. Kulmakertoimen epävarmuus on $\Delta A$ ja pituuden epävarmuus $\Delta l$. Laske tekijöiden suhteelliset epävarmuudet yhteen: $\Delta \mu_0 : \mu_0 = \Delta A : A + \Delta l : l$. Vakiotermi $B_0$ on yleensä pieni. Siihen vaikuttavat anturin nollakohta ja Maan magneettikenttä.

## Esimerkki
Koulun käämissä on $600$ kierrosta, ja sen pituus on $15{,}0\,\text{cm}$. Käämissä kulkee virta $2{,}50\,\text{A}$. Käämi on pitkä paksuuteensa verrattuna, ja sen sisällä on ilmaa. Kuinka suuri on magneettivuon tiheys käämin keskellä? Kuinka moninkertainen se on Maan magneettikenttään $50\,\mu\text{T}$ verrattuna?

<!-- vaihe -->

**Tunnetut ja kysytty.** Kierrosten lukumäärä on $N = 600$. Käämin pituus on $l = 15{,}0\,\text{cm}$ ja virta $I = 2{,}50\,\text{A}$. Vakio on $\mu_0 \approx 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}}$.

Kysytään magneettivuon tiheyttä $B$ käämin keskellä. Lisäksi kysytään sen suhdetta Maan kenttään $B_\text{Maa} = 50\,\mu\text{T}$.

<!-- vaihe -->

**Periaate.** Käämi on pitkä, ja sen sisällä on ilmaa. Kenttä halutaan keskeltä, kaukaa päistä. Siksi pitkän käämin kaava pätee. Kenttä riippuu vain kierrostiheydestä ja virrasta.

<!-- vaihe -->

**Kaava ratkaistuna.** Kaava antaa kysytyn suureen suoraan. Suhde saadaan jakamalla:
```latex
\begin{aligned}
&B = \mu_0 \frac{N I}{l} \\
&k = \frac{B}{B_\text{Maa}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Pituus metreinä: $l = 15{,}0 \cdot 0{,}01\,\text{m} = 0{,}150\,\text{m}$. Maan kenttä tesloina: $50\,\mu\text{T} = 50 \cdot 10^{-6}\,\text{T}$. Yksiköistä saadaan $\tfrac{\text{Vs}}{\text{Am}} \cdot \tfrac{\text{A}}{\text{m}} = \tfrac{\text{Vs}}{\text{m}^2} = \text{T}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&B = \mu_0 \frac{N I}{l} \\
&= 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}} \\
&\quad \cdot \frac{600 \cdot 2{,}50\,\text{A}}{0{,}150\,\text{m}} \\
&= 0{,}012566\,\text{T} \\[6pt]
&k = \frac{0{,}012566\,\text{T}}{50 \cdot 10^{-6}\,\text{T}} \\
&= 251{,}3
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Magneettivuon tiheys käämin keskellä on $12{,}6\,\text{mT}$. Vastauksessa on kolme merkitsevää numeroa, koska pituudessa $15{,}0\,\text{cm}$ ja virrassa $2{,}50\,\text{A}$ on kolme. Kenttä on noin $250$-kertainen Maan kenttään verrattuna. Suhteessa on vain kaksi numeroa, koska Maan kenttä $50\,\mu\text{T}$ tunnetaan vain kahden numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Kierrostiheys on $600 : 0{,}150\,\text{m} = 4000$ kierrosta metrillä. Yksi ampeeri ja tuhat kierrosta metrillä antavat noin $1{,}3\,\text{mT}$. Nyt virta on $2{,}5\,\text{A}$ ja tiheys nelinkertainen, joten kenttä on noin $1{,}3\,\text{mT} \cdot 2{,}5 \cdot 4 = 13\,\text{mT}$.

Tulos on noin $250$-kertainen Maan kenttään verrattuna, joten käämin kenttä on helppo mitata. Se on kuitenkin selvästi pienempi kuin magneettikuvauslaitteen noin $1{,}5\,\text{T}$. Sellainen kenttä vaatii suprajohtavan käämin ja satojen ampeerien virran.

## Yleinen virhekäsitys
Moni ajattelee, että virtajohtimen magneettikenttä osoittaa johtimesta poispäin. Näin on varatun johtimen sähkökentässä. Magneettikentän kenttäviivat kuitenkin kiertävät johdinta suljettuina ympyröinä, eikä niillä ole alku- eikä loppupistettä. Kompassi johtimen vieressä kääntyy siksi poikittain johtimeen nähden, ei johdinta kohti.

Toinen virhe on luulla, että käämin kenttä riippuu kierrosten kokonaismäärästä. Otetaan esimerkki: sama $200$ kierroksen käämi venytetään kaksinkertaiseen pituuteen. Kierrostiheys $N : l$ puolittuu, ja kenttä käämin keskellä noin puolittuu. Kierroksia on silti yhtä monta.

Kolmas virhe on unohtaa, että pitkän käämin kaava ei päde käämin päissä. Siellä kenttä on vain noin puolet keskikohdan arvosta.

## Tiivistelmä
- Sähkövirta synnyttää ympärilleen magneettikentän (Ørsted 1820). Suoran johtimen kenttäviivat ovat johdinta kiertäviä ympyröitä. Suunnan saat oikean käden säännöllä: peukalo virran suuntaan, sormet kentän suuntaan.
- Pitkän suoran johtimen kenttä on $B = \tfrac{\mu_0 I}{2\pi r}$. Se kasvaa virran mukana ja heikkenee etäisyyden kasvaessa.
- Pitkän käämin sisällä kenttä on lähes homogeeninen, $B = \mu_0 \tfrac{N I}{l}$. Se riippuu kierrostiheydestä $N : l$ ja virrasta. Käämin ulkopuolella kenttä on kuin sauvamagneetin kenttä.
- Rautasydän tekee käämistä sähkömagneetin. Sen kenttä on moninkertainen, ja sen voi kytkeä päälle ja pois.
- Mittaa $B$ virran funktiona ja sovita pisteisiin suora. Kulmakertoimesta saat $\mu_0 = A l : N$.
