# Generaattori ja vaihtovirta

> **Miksi** tuulivoimalan pyörivä roottori tuottaa sähköverkkoon jännitteen, joka vaihtaa suuntaansa sata kertaa sekunnissa?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: tuulivoimapuisto suomalaisella pellolla meren rannalla. Keskellä on suuri tuulivoimala, jonka siivet pyörivät, ja sen takana pienempiä voimaloita. Oikealla voimalinja kulkee pylväiden varassa punaisten talojen luo. Taivaalla on pilviä, ja tuuli taivuttaa koivujen latvoja." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-7-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Pyörivä käämi magneettikentässä
Luvussa *Sähkömagneettinen induktio* käämiin syntyi induktiojännite, kun sen läpi kulkeva magneettivuo muuttui. **Generaattori** tuottaa vuon muutoksen pyörimisliikkeellä: käämiä pyöritetään magneetin napojen välissä. Kun käämin taso on kohtisuorassa kenttää vastaan, kenttäviivoja kulkee käämin läpi eniten ja vuo on suurin, $\Phi = BA$. Neljänneskierroksen jälkeen käämin taso on kentän suuntainen, eikä yksikään kenttäviiva kulje sen läpi: vuo on nolla. Seuraavan neljänneksen jälkeen kenttä kulkee käämin läpi taas kohtisuoraan, mutta käämin toiselta puolelta, joten vuo on $-BA$. Vuo vaihtelee siis tasaisesti pyörivässä käämissä jatkuvasti arvojen $BA$ ja $-BA$ välillä.

<svg data-fig="generator" viewBox="0 0 600 360" role="img" aria-label="Periaatekuva vaihtovirtageneraattorista, ei mittakaavassa. Ylhäällä on magneetin N-napa ja alhaalla S-napa, joten magneettikenttä osoittaa alaspäin. Napojen välissä on kuparinen käämi, jota pyöritetään vaakasuoran akselin ympäri. Käämin johtimen päät on kytketty akselilla oleviin kahteen liukurenkaaseen. Renkaita koskettavat hiiliharjat, ja harjoista johdot kulkevat lamppuun." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-7-generator.webp" x="0" y="0" width="600" height="370" preserveAspectRatio="none"/>
  <foreignObject x="200" y="36.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="200" y="304.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="348" y="135.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="165" y="171.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{käämi}$</div></foreignObject>
  <foreignObject x="365" y="81.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{hiiliharjat}$</div></foreignObject>
  <foreignObject x="372" y="267.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{liukurenkaat}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/bicycle-dynamo.webp" alt="Polkupyörän etupyörä ja pyöreä etuvalo; rengasta vasten on painettu pieni hopeanvärinen pullodynamo."><figcaption>Polkupyörän dynamo on pieni generaattori. Renkaan pyörittämä akseli pyörittää kestomagneettia käämin sisällä. Käämi pysyy paikallaan, mutta sen läpi kulkeva magneettivuo muuttuu, joten siihen indusoituu vaihtojännite.</figcaption></figure>

```pysahdy
Käämin pinta-ala on $0{,}010\,\text{m}^2$ ja magneettivuon tiheys $0{,}20\,\text{T}$. Kuinka suuri on käämin läpi kulkeva vuo, kun käämin taso on kohtisuorassa kenttää vastaan, ja kuinka suuri neljänneskierroksen jälkeen?
---
Aluksi $\Phi = BA = 0{,}20\,\text{T} \cdot 0{,}010\,\text{m}^2 = 0{,}0020\,\text{Wb}$. Neljänneskierroksen jälkeen käämin taso on kentän suuntainen, eikä yksikään kenttäviiva kulje sen läpi, joten vuo on nolla.
```

### Liukurenkaat ja harjat
Käämin johtimen päät on kytketty akselilla oleviin kahteen **liukurenkaaseen**. Renkaita koskettavat hiiliharjat, joiden kautta jännite johdetaan ulkoiseen virtapiiriin, kuten kuvan lamppuun. Toisin kuin tasavirtamoottorin kommutaattori luvussa *Voima virtajohtimeen: sähkömoottori ja kaiutin*, liukurenkaat eivät käännä virran suuntaa, joten ulkoiseen piiriin tulee käämiin syntyvä jännite sellaisenaan.

### Miksi jännite on sinimuotoinen
Induktiolain mukaan jännite ei riipu siitä, kuinka suuri vuo on, vaan siitä, kuinka nopeasti se muuttuu. Kuvaajassa $\Phi(t)$ muutosnopeus on kuvaajan jyrkkyys. Kun vuo on suurimmillaan, käämin sivut liikkuvat kenttäviivojen suuntaisesti, vuo ei hetkeen juuri muutu ja jännite on nolla. Kun käämin taso on kentän suuntainen, vuo on nolla, mutta sivut liikkuvat kohtisuoraan kenttäviivojen poikki ja vuo muuttuu nopeimmin: jännite on suurimmillaan. Vuo vaihtelee kosinin tavoin, ja sen jyrkkyys vaihtelee sinin tavoin. Jokaisella puolikierroksella vuon muutoksen suunta kääntyy, joten myös jännitteen merkki kääntyy. Syntyy **vaihtojännite**, ja suljetussa piirissä kulkee **vaihtovirta**, jonka suunta vaihtuu kahdesti jokaisen kierroksen aikana.

<svg data-fig="phi-e" viewBox="0 0 600 440" role="img" aria-label="Kaksi kuvaajaa samalla aika-akselilla yhden jaksonajan T ajalta. Ylemmässä vihreä magneettivuo Phi alkaa suurimmasta arvostaan BA, laskee nollaan neljäsosajakson kohdalla, on pienimmillään miinus BA puolen jakson kohdalla ja palaa arvoon BA. Alemmassa violetti jännite e alkaa nollasta, on suurin e0 neljäsosajakson kohdalla, nolla puolen jakson kohdalla ja pienin miinus e0 kolmen neljäsosajakson kohdalla. Katkoviiva neljäsosajakson kohdalla näyttää, että jännite on suurin, kun vuo on nolla. Alimpana pienet kuvat käämistä päästä katsottuna: kenttä osoittaa oikealle, ja käämin taso on hetkellä nolla kohtisuorassa kenttää vastaan, neljäsosajakson kohdalla kentän suuntainen ja niin edelleen." style="max-width:100%;font-size:24px">
  <line x1="208" y1="170" x2="208" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="296" y1="170" x2="296" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384" y1="170" x2="384" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="472" y1="170" x2="472" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="159" x2="500" y2="159" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="115" x2="500" y2="115" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="71" x2="500" y2="71" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="119" y1="170" x2="514" y2="170" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,170 L513,176 L513,164 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="120" y1="171" x2="120" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M120,34 L126,47 L114,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="208" y1="170" x2="208" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="166.5" y="179.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}25\,T$</div></foreignObject>
  <line x1="296" y1="170" x2="296" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="261" y="179.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}5\,T$</div></foreignObject>
  <line x1="384" y1="170" x2="384" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="342.5" y="179.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}75\,T$</div></foreignObject>
  <line x1="472" y1="170" x2="472" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="462" y="179.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="113" y1="159" x2="120" y2="159" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="63" y="144.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-BA$</div></foreignObject>
  <line x1="113" y1="115" x2="120" y2="115" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="88" y="100.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="113" y1="71" x2="120" y2="71" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="75" y="56.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$BA$</div></foreignObject>
  <foreignObject x="532" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="110" y="3.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\Phi$</div></foreignObject>
  <polyline points="120,71 123,71 126,71 129,71.5 131.5,72 134.5,72.5 137.5,73 140.5,74 143.5,75 146.5,76 149.5,77 152.5,78 155,79.5 158,81 161,82.5 164,84 167,85.5 170,87.5 173,89 175.5,91 178.5,93 181.5,95 184.5,97 187.5,99 190.5,101.5 193.5,103.5 196,106 199,108 202,110.5 205,112.5 208,115 211,117.5 214,119.5 217,122 219.5,124 222.5,126.5 225.5,128.5 228.5,131 231.5,133 234.5,135 237.5,137 240,139 243,141 246,142.5 249,144.5 252,146 255,147.5 258,149 260.5,150.5 263.5,152 266.5,153 269.5,154 272.5,155 275.5,156 278.5,157 281.5,157.5 284,158 287,158.5 290,159 293,159 296,159 299,159 302,159 304.5,158.5 307.5,158 310.5,157.5 313.5,157 316.5,156 319.5,155 322.5,154 325,153 328,152 331,150.5 334,149 337,147.5 340,146 343,144.5 346,142.5 348.5,141 351.5,139 354.5,137 357.5,135 360.5,133 363.5,131 366.5,128.5 369,126.5 372,124 375,122 378,119.5 381,117.5 384,115 387,112.5 390,110.5 392.5,108 395.5,106 398.5,103.5 401.5,101.5 404.5,99 407.5,97 410.5,95 413,93 416,91 419,89 422,87.5 425,85.5 428,84 431,82.5 433.5,81 436.5,79.5 439.5,78 442.5,77 445.5,76 448.5,75 451.5,74 454.5,73 457,72.5 460,72 463,71.5 466,71 469,71 472,71" fill="none" stroke="#2b8a3e" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="482" y="56.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\Phi$</div></foreignObject>
  <line x1="208" y1="330" x2="208" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="296" y1="330" x2="296" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384" y1="330" x2="384" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="472" y1="330" x2="472" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="320" x2="500" y2="320" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="280" x2="500" y2="280" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="240" x2="500" y2="240" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="119" y1="330" x2="514" y2="330" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,330 L513,336 L513,324 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="120" y1="331" x2="120" y2="216" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M120,204 L126,217 L114,217 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="208" y1="330" x2="208" y2="337" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="166.5" y="339.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}25\,T$</div></foreignObject>
  <line x1="296" y1="330" x2="296" y2="337" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="261" y="339.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}5\,T$</div></foreignObject>
  <line x1="384" y1="330" x2="384" y2="337" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="342.5" y="339.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}75\,T$</div></foreignObject>
  <line x1="472" y1="330" x2="472" y2="337" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="462" y="339.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="113" y1="320" x2="120" y2="320" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="63" y="305.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-e_0$</div></foreignObject>
  <line x1="113" y1="280" x2="120" y2="280" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="88" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="113" y1="240" x2="120" y2="240" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="75" y="225.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$e_0$</div></foreignObject>
  <foreignObject x="532" y="315.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="110" y="173.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$e$</div></foreignObject>
  <polyline points="120,280 123,278 126,276 129,273.5 131.5,271.5 134.5,269.5 137.5,267.5 140.5,265.5 143.5,263.5 146.5,262 149.5,260 152.5,258 155,256.5 158,255 161,253 164,251.5 167,250.5 170,249 173,247.5 175.5,246.5 178.5,245.5 181.5,244.5 184.5,243.5 187.5,242.5 190.5,242 193.5,241.5 196,241 199,240.5 202,240 205,240 208,240 211,240 214,240 217,240.5 219.5,241 222.5,241.5 225.5,242 228.5,242.5 231.5,243.5 234.5,244.5 237.5,245.5 240,246.5 243,247.5 246,249 249,250.5 252,251.5 255,253 258,255 260.5,256.5 263.5,258 266.5,260 269.5,262 272.5,263.5 275.5,265.5 278.5,267.5 281.5,269.5 284,271.5 287,273.5 290,276 293,278 296,280 299,282 302,284 304.5,286.5 307.5,288.5 310.5,290.5 313.5,292.5 316.5,294.5 319.5,296.5 322.5,298 325,300 328,302 331,303.5 334,305 337,307 340,308.5 343,309.5 346,311 348.5,312.5 351.5,313.5 354.5,314.5 357.5,315.5 360.5,316.5 363.5,317.5 366.5,318 369,318.5 372,319 375,319.5 378,320 381,320 384,320 387,320 390,320 392.5,319.5 395.5,319 398.5,318.5 401.5,318 404.5,317.5 407.5,316.5 410.5,315.5 413,314.5 416,313.5 419,312.5 422,311 425,309.5 428,308.5 431,307 433.5,305 436.5,303.5 439.5,302 442.5,300 445.5,298 448.5,296.5 451.5,294.5 454.5,292.5 457,290.5 460,288.5 463,286.5 466,284 469,282 472,280" fill="none" stroke="#7048e8" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="482" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$e$</div></foreignObject>
  <line x1="208" y1="60" x2="208" y2="170" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="208" y1="230" x2="208" y2="330" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="49.5" y="399.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <line x1="94" y1="418" x2="138" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M146,418 L137,422 L137,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="120" y1="375" x2="120" y2="409" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="120" cy="375" r="4" fill="#1f2933"/>
  <circle cx="120" cy="409" r="4" fill="#1f2933"/>
  <line x1="182" y1="418" x2="226" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M234,418 L225,422 L225,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="191" y1="392" x2="225" y2="392" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="191" cy="392" r="4" fill="#1f2933"/>
  <circle cx="225" cy="392" r="4" fill="#1f2933"/>
  <line x1="270" y1="418" x2="314" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M322,418 L313,422 L313,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="296" y1="409" x2="296" y2="375" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="296" cy="409" r="4" fill="#1f2933"/>
  <circle cx="296" cy="375" r="4" fill="#1f2933"/>
  <line x1="358" y1="418" x2="402" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M410,418 L401,422 L401,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="401" y1="392" x2="367" y2="392" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="401" cy="392" r="4" fill="#1f2933"/>
  <circle cx="367" cy="392" r="4" fill="#1f2933"/>
  <line x1="446" y1="418" x2="490" y2="418" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt"/>
  <path d="M498,418 L489,422 L489,414 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="472" y1="375" x2="472" y2="409" stroke="#b8622d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="472" cy="375" r="4" fill="#1f2933"/>
  <circle cx="472" cy="409" r="4" fill="#1f2933"/>
</svg>

<figure class="unit-photo"><img src="pics/fy7/generator-stator.webp" alt="Suuri pyöreä kuilu ylhäältä kuvattuna; kuilun seinämillä kiertää käämien rivi, reunoilla on keltaiset kaiteet ja pohjalla työkaluja."><figcaption>Vesivoimalan generaattorin staattori, josta roottori on nostettu pois. Käämit ovat paikallaan kehän ympärillä, ja niissä indusoituu jännite, kun magneettinapoja kantava roottori pyörii sisällä.</figcaption></figure>

<figure class="unit-photo"><img src="pics/fy7/generator-rotor.webp" alt="Suuri punaruskea lieriö seisoo valaistun hallin lattialla; lieriön kehällä on pystysuoria raitoja, ja sen ympärillä on laitteita ja ihmisiä pieninä."><figcaption>Pumppuvoimalan generaattorin roottori huollossa Coo-Trois-Pontsissa Belgiassa. Roottorin kehällä on sähkömagneettien napoja. Kun roottori pyörii staattorin sisällä, käämien läpi kulkeva magneettivuo muuttuu jatkuvasti.</figcaption></figure>

### Voimalaitoksen generaattori ja tuulivoimala
Voimalaitosten suurissa generaattoreissa pyörii sähkömagneetti, ja käämit ovat paikallaan ympärillä. Paikallaan olevan käämin läpi kulkeva vuo muuttuu samalla tavalla kuin pyörivässä käämissä, joten syntyy samanlainen vaihtojännite, ja suuri virta saadaan käämeistä ilman liukukoskettimia. Tuulivoimalassa tuuli pyörittää roottoria, jonka akseli pyörittää generaattoria. Roottori pyörii hitaasti, noin $10$–$15$ kierrosta minuutissa, joten generaattorissa on joko vaihteisto, joka nostaa pyörimisnopeuden, tai paljon magneettinapoja. Tuulen nopeus vaihtelee, joten taajuusmuuttaja muuntaa generaattorin jännitteen verkon taajuuteen $50\,\text{Hz}$. Suomessa oli vuoden 2024 lopussa $1835$ tuulivoimalaa, joiden yhteenlaskettu nimellisteho oli $8358\,\text{MW}$. Ne tuottivat vuonna 2024 $19{,}8\,\text{TWh}$ sähköä, noin $24\,\%$ Suomen sähkönkulutuksesta (Suomen Uusiutuvat ry, tuulivoimatilastot 2024).

## Kaava: Generaattorin jännite
Kun käämi, jossa on $N$ kierrosta ja jonka pinta-ala on $A$, pyörii tasaisesti homogeenisessa magneettikentässä $B$ pyörimistaajuudella $f$ ja hetkellä $t = 0$ käämin taso on kohtisuorassa kenttää vastaan, käämin läpi kulkeva vuo ja käämiin syntyvä jännite ovat
```kaavat
\Phi = BA\cos(2\pi f t)
sinimuotoinen vaihtojännite ajan funktiona :: e = e_0 \sin(2\pi f t)
e_0 = NBA \cdot 2\pi f
```
missä $\Phi$ on magneettivuo yhden kierroksen läpi (Wb), $e$ jännitteen hetkellinen arvo (V), $e_0$ jännitteen huippuarvo (V), $N$ kierrosten lukumäärä, $B$ magneettivuon tiheys (T), $A$ käämin pinta-ala (m²) ja $f$ pyörimistaajuus (Hz). Jännitteen taajuus on sama kuin pyörimistaajuus, ja jaksonaika on $T = 1 : f$. Vuo muuttuu pyöriessä epätasaisesti, joten $e$ on hetkellinen jännite: se on suurin, kun vuo on nolla ja muuttuu nopeimmin, ja nolla, kun vuo on suurimmillaan.

```pysahdy
Generaattorin käämi pyörii tasaisesti $20$ kierrosta sekunnissa. Mikä on syntyvän jännitteen taajuus ja jaksonaika?
---
Jännitteen taajuus on sama kuin pyörimistaajuus eli $20\,\text{Hz}$. Jaksonaika on $T = \tfrac{1}{f} = \tfrac{1}{20\,\text{Hz}} = 0{,}050\,\text{s}$.
```

### Mistä huippuarvo tulee
Huippuarvo saadaan liikkuvan johtimen jännitteestä $e = vBl$ (luku *Sähkömagneettinen induktio*). Suorakulmaisen käämin kaksi sivua, joiden pituus on $l$, kiertävät akselia säteellä $b : 2$, missä $b$ on käämin leveys. Sivujen nopeus on $v = 2\pi f \cdot b : 2 = \pi f b$. Jännitteeseen vaikuttaa vain nopeuden kenttää vastaan kohtisuora komponentti $v \sin\theta$, missä $\theta$ on nopeuden ja kentän välinen kulma. Kumpaankin sivuun syntyy jännite $B l v \sin\theta$, ja sivujen jännitteet summautuvat kierroksessa. Yhdessä kierroksessa jännite on siis $2 B l \cdot \pi f b \sin\theta = BA \cdot 2\pi f \sin\theta$, koska $lb = A$, ja $N$ kierroksessa $N$-kertainen. Kun $\theta = 90^\circ$, käämin taso on kentän suuntainen ja jännite on huippuarvossaan $e_0 = NBA \cdot 2\pi f$. Kaksinkertainen pyörimistaajuus kaksinkertaistaa sekä jännitteen taajuuden että huippuarvon, koska sivut liikkuvat kaksi kertaa nopeammin.

<svg data-fig="derive" viewBox="0 0 600 360" role="img" aria-label="Periaatekuva, ei mittakaavassa: käämi nähdään akselin suunnasta. Vaakasuorat vihreät kenttäviivat osoittavat oikealle. Käämin taso on vinossa, ja sen kaksi sivua, joiden pituus l on kohtisuoraan paperia vastaan, ovat ympyröinä: oikean alemman sivun virta kulkee paperiin päin ja vasemman ylemmän paperista ulos. Sivujen nopeudet, siniset nuolet, ovat kohtisuorassa käämin tasoa vastaan ja vastakkaissuuntaiset. Oikean sivun nopeuden ja kentän välinen kulma on theeta, ja nopeuden kenttää vastaan kohtisuora komponentti v sin theeta on piirretty katkoviivalla. Käämin leveys on b." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-7-derive.webp" x="-1.3" y="-1.3" width="603" height="370.6" preserveAspectRatio="none"/>
  <foreignObject x="527" y="3.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}$</div></foreignObject>
  <foreignObject x="180" y="173.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$b$</span></div></foreignObject>
  <foreignObject x="404" y="119.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="23" y="209.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="350.5" y="197" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <foreignObject x="406" y="185.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v\sin\theta$</div></foreignObject>
  <foreignObject x="264.5" y="250" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$I$</span></div></foreignObject>
</svg>

### Tehollinen arvo
Vaihtojännitteen keskiarvo yhden jakson aikana on nolla, mutta lamppu tai vastus lämpenee silti, koska teho $p = ui$ on positiivinen kummallakin virran suunnalla. Vastuksen teho vaihtelee nollan ja huippuarvon $P_0 = U_0 I_0$ välillä, ja sen keskiarvo on puolet huippuarvosta. **Tehollinen arvo** on se tasajännite tai tasavirta, joka tuottaisi vastukseen saman keskimääräisen tehon:
```kaavat
sinimuotoisen vaihtojännitteen tehollinen arvo :: U = \frac{U_0}{\sqrt{2}}
sinimuotoisen vaihtovirran tehollinen arvo :: I = \frac{I_0}{\sqrt{2}}
```
missä $U_0$ ja $I_0$ ovat jännitteen ja virran **huippuarvot** ja $U$ ja $I$ tehollisarvot. Kun vaihtovirta kulkee puhtaan resistiivisen kuorman, kuten ideaalisen vastuksen, läpi, virta ja jännite ovat samanvaiheiset. Tällöin keskimääräinen teho voidaan laskea tehollisarvoista kaavalla $P = UI$, kuten tasavirralla. Yleisessä vaihtovirtapiirissä virran ja jännitteen välillä voi olla vaihe-ero, jolloin keskimääräinen teho riippuu myös tehokertoimesta. Pistorasian $230\,\text{V}$ on tehollinen arvo: jännitteen huippuarvo on $230\,\text{V} \cdot \sqrt{2} \approx 325\,\text{V}$, ja taajuus on $50\,\text{Hz}$, joten jännite vaihtaa suuntaansa sata kertaa sekunnissa. Fingrid pitää kantaverkon taajuuden normaalisti välillä $49{,}9$–$50{,}1\,\text{Hz}$. Mittarit näyttävät vaihtojännitteen ja -virran tehollisarvoina.

<svg data-fig="power" viewBox="0 0 600 320" role="img" aria-label="Kuvaaja: vastuksen teho p ajan t funktiona yhden jaksonajan T ajalta, kun vastukseen on kytketty sinimuotoinen vaihtojännite. Oranssi käyrä vaihtelee nollan ja huippuarvon P0 välillä ja on nolla hetkillä 0, puoli jaksoa ja T, ja huipussaan neljäsosa- ja kolmen neljäsosan jakson kohdalla. Katkoviiva korkeudella puolet P0:sta on tehon keskiarvo: käyrän huiput sen yläpuolella ovat yhtä suuret kuin kuopat sen alapuolella." style="max-width:100%;font-size:24px">
  <line x1="202.5" y1="262" x2="202.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="285" y1="262" x2="285" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="367" y1="262" x2="367" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="449.5" y1="262" x2="449.5" y2="52" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="168" x2="476" y2="168" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="74.5" x2="476" y2="74.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="119" y1="262" x2="490" y2="262" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,262 L489,268 L489,256 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="120" y1="263" x2="120" y2="38" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M120,26 L126,39 L114,39 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="202.5" y1="262" x2="202.5" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="161" y="271.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}25\,T$</div></foreignObject>
  <line x1="285" y1="262" x2="285" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="250" y="271.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}5\,T$</div></foreignObject>
  <line x1="367" y1="262" x2="367" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="325.5" y="271.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}75\,T$</div></foreignObject>
  <line x1="449.5" y1="262" x2="449.5" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="439.5" y="271.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="113" y1="168" x2="120" y2="168" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="63" y="154" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\tfrac{1}{2}P_0$</div></foreignObject>
  <line x1="113" y1="74.5" x2="120" y2="74.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="75" y="60" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P_0$</div></foreignObject>
  <foreignObject x="90" y="267.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="508" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="134" y="17.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$p$</span></div></foreignObject>
  <polygon points="120,168 120,262 122.5,261.5 125.5,260 128,257.5 131,254 133.5,249.5 136.5,244 139,238 142,231 144.5,223.5 147.5,215 150,206.5 153,197 155.5,187.5 158.5,178 161,168.5 164,158.5 166.5,149 169.5,139.5 172,130 175,121.5 177.5,113 180.5,105.5 183,98.5 186,92.5 188.5,87 191.5,82.5 194,79 197,76.5 199.5,75 202.5,74.5 205,75 208,76.5 210.5,79 213.5,82.5 216,87 219,92.5 221.5,98.5 224.5,105.5 227,113 230,121.5 232.5,130 235.5,139.5 238,149 241,158.5 243.5,168 246.5,178 249,187.5 252,197 254.5,206.5 257.5,215 260,223.5 263,231 265.5,238 268.5,244 271,249.5 274,254 276.5,257.5 279.5,260 282,261.5 285,262 287.5,261.5 290.5,260 293,257.5 296,254 298.5,249.5 301.5,244 304,238 307,231 309.5,223.5 312.5,215 315,206.5 318,197 320.5,187.5 323.5,178 326,168.5 329,158.5 331.5,149 334.5,139.5 337,130 340,121.5 342.5,113 345,105.5 348,98.5 350.5,92.5 353.5,87 356,82.5 359,79 361.5,76.5 364.5,75 367,74.5 370,75 372.5,76.5 375.5,79 378,82.5 381,87 383.5,92.5 386.5,98.5 389,105.5 392,113 394.5,121.5 397.5,130 400,139.5 403,149 405.5,158.5 408.5,168 411,178 414,187.5 416.5,197 419.5,206.5 422,215 425,223.5 427.5,231 430.5,238 433,244 436,249.5 438.5,254 441.5,257.5 444,260 447,261.5 449.5,262 449.5,168" fill="#ffc078" fill-opacity="0.3"/>
  <polyline points="120,262 122.5,261.5 125.5,260 128,257.5 131,254 133.5,249.5 136.5,244 139,238 142,231 144.5,223.5 147.5,215 150,206.5 153,197 155.5,187.5 158.5,178 161,168.5 164,158.5 166.5,149 169.5,139.5 172,130 175,121.5 177.5,113 180.5,105.5 183,98.5 186,92.5 188.5,87 191.5,82.5 194,79 197,76.5 199.5,75 202.5,74.5 205,75 208,76.5 210.5,79 213.5,82.5 216,87 219,92.5 221.5,98.5 224.5,105.5 227,113 230,121.5 232.5,130 235.5,139.5 238,149 241,158.5 243.5,168 246.5,178 249,187.5 252,197 254.5,206.5 257.5,215 260,223.5 263,231 265.5,238 268.5,244 271,249.5 274,254 276.5,257.5 279.5,260 282,261.5 285,262 287.5,261.5 290.5,260 293,257.5 296,254 298.5,249.5 301.5,244 304,238 307,231 309.5,223.5 312.5,215 315,206.5 318,197 320.5,187.5 323.5,178 326,168.5 329,158.5 331.5,149 334.5,139.5 337,130 340,121.5 342.5,113 345,105.5 348,98.5 350.5,92.5 353.5,87 356,82.5 359,79 361.5,76.5 364.5,75 367,74.5 370,75 372.5,76.5 375.5,79 378,82.5 381,87 383.5,92.5 386.5,98.5 389,105.5 392,113 394.5,121.5 397.5,130 400,139.5 403,149 405.5,158.5 408.5,168 411,178 414,187.5 416.5,197 419.5,206.5 422,215 425,223.5 427.5,231 430.5,238 433,244 436,249.5 438.5,254 441.5,257.5 444,260 447,261.5 449.5,262" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="120" y1="168" x2="449.5" y2="168" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="459.5" y="154" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{keskiarvo}$</div></foreignObject>
</svg>

```pysahdy
Vastuksen läpi kulkevan sinimuotoisen vaihtovirran huippuarvo on $2{,}0\,\text{A}$. Mikä on virran tehollinen arvo?
---
Tehollinen arvo on huippuarvo jaettuna luvulla $\sqrt{2}$: $I = \tfrac{I_0}{\sqrt{2}} = \tfrac{2{,}0\,\text{A}}{\sqrt{2}} \approx 1{,}4\,\text{A}$.
```

## Esimerkki
Opetuskäytössä olevan generaattorin käämissä on $250$ kierrosta, ja suorakulmaisen käämin sivujen pituudet ovat $4{,}0\,\text{cm}$ ja $5{,}0\,\text{cm}$. Käämi pyörii homogeenisessa magneettikentässä, jonka magneettivuon tiheys on $0{,}18\,\text{T}$, ja tekee $12$ kierrosta sekunnissa. Kuinka suuri on käämiin syntyvän vaihtojännitteen tehollinen arvo?

<!-- vaihe -->

**Tunnetut ja kysytty.** Kierrosten lukumäärä $N = 250$, käämin sivut $4{,}0\,\text{cm}$ ja $5{,}0\,\text{cm}$, magneettivuon tiheys $B = 0{,}18\,\text{T}$ ja pyörimistaajuus $f = 12\,\text{Hz}$.

Kysytään jännitteen tehollista arvoa $U$.

<!-- vaihe -->

**Periaate.** Käämi pyörii tasaisesti homogeenisessa kentässä, joten siihen syntyy sinimuotoinen vaihtojännite, jonka huippuarvo on $e_0 = NBA \cdot 2\pi f$. Sinimuotoisen jännitteen tehollinen arvo on huippuarvo jaettuna luvulla $\sqrt{2}$.

<!-- vaihe -->

**Kaava ratkaistuna.**
```kaavat
generaattorissa käämiin indusoituvan sinimuotoisen vaihtojännitteen huippuarvo :: e_0 = NBA \cdot 2\pi f
U = \frac{e_0}{\sqrt{2}} = \frac{NBA \cdot 2\pi f}{\sqrt{2}}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Pinta-ala neliömetreinä: $A = 4{,}0 \cdot 0{,}01\,\text{m} \cdot 5{,}0 \cdot 0{,}01\,\text{m} = 0{,}0020\,\text{m}^2$. Pyörimistaajuus on $12$ kierrosta sekunnissa eli $f = 12\,\text{Hz}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin huippuarvo ja sitten tehollinen arvo:
```latex
\begin{aligned}
&e_0 = NBA \cdot 2\pi f \\
&= 250 \cdot 0{,}18\,\text{T} \cdot 0{,}0020\,\text{m}^2 \\
&\quad \cdot 2\pi \cdot 12\,\tfrac{1}{\text{s}} \\
&= 6{,}786\,\text{V} \\[6pt]
&U = \frac{6{,}786\,\text{V}}{\sqrt{2}} \\
&= 4{,}798\,\text{V}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Jännitteen tehollinen arvo on $U \approx 4{,}8\,\text{V}$ ja huippuarvo noin $6{,}8\,\text{V}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla, kuten käämin mitat ja magneettivuon tiheys.

<!-- vaihe -->

**Järkevyys.** Yksiköt sopivat: $\text{T} \cdot \text{m}^2 \cdot \tfrac{1}{\text{s}} = \tfrac{\text{Wb}}{\text{s}} = \text{V}$. Pyöreillä luvuilla $250 \cdot 0{,}2\,\text{T} \cdot 0{,}002\,\text{m}^2 \cdot 6 \cdot 10\,\tfrac{1}{\text{s}} \approx 6\,\text{V}$, mikä sopii huippuarvoon. Tehollinen arvo on pienempi kuin huippuarvo, kuten pitääkin. Muutaman voltin jännite on samaa suuruusluokkaa kuin polkupyörän dynamon jännite.

## Yleinen virhekäsitys
Moni ajattelee, että jännite on suurin silloin, kun käämin läpi kulkee eniten kenttäviivoja eli käämin taso on kohtisuorassa kenttää vastaan. Silloin jännite on kuitenkin **nolla**, koska vuo ei sillä hetkellä muutu. Jännite on suurin, kun käämin taso on kentän suuntainen ja vuo on nolla, koska silloin vuo muuttuu nopeimmin. Toinen yleinen virhe on pitää pistorasian $230\,\text{V}$:a jännitteen suurimpana arvona. Se on tehollinen arvo, ja jännite käy välillä $-325\,\text{V}$ ja $325\,\text{V}$. Kolmas virhe on päätellä, että vaihtovirta ei siirrä energiaa, koska sen keskiarvo on nolla. Teho on positiivinen kummallakin virran suunnalla.

## Tiivistelmä
- Generaattorissa käämi pyörii magneettikentässä (tai magneetti käämin sisällä), ja käämin läpi kulkeva vuo $\Phi = BA\cos(2\pi f t)$ vaihtelee jatkuvasti.
- Induktiojännite riippuu vuon muutosnopeudesta: se on nolla, kun vuo on suurin, ja suurin, kun käämin taso on kentän suuntainen ja vuo on nolla.
- Syntyy sinimuotoinen vaihtojännite $e = e_0 \sin(2\pi f t)$, jonka huippuarvo on $e_0 = NBA \cdot 2\pi f$ ja taajuus sama kuin pyörimistaajuus.
- Sinimuotoisen vaihtojännitteen tehollinen arvo on $U = U_0 : \sqrt{2}$ ja $I = I_0 : \sqrt{2}$, ja resistiivisen kuorman keskimääräinen teho on $P = UI$. Verkkojännitteen $230\,\text{V}$ huippuarvo on noin $325\,\text{V}$ ja taajuus $50\,\text{Hz}$.
- Tuulivoimalan roottori pyörittää generaattoria, ja taajuusmuuttaja sovittaa jännitteen verkon taajuuteen.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: pyöräilijä ajaa iltahämärässä. Etupyörän navassa on dynamo, joka tuottaa lampulle vaihtojännitteen, ja lampun valokeila valaisee tietä pyörän edessä." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-7-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
