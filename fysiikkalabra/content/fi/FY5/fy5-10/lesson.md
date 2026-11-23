# Aaltojen synty ja eteneminen

> **Miksi** tolpassa roikkuva kello kilahtaa, kun pitkän narun toista päätä heilautetaan kerran, vaikka kukaan ei koske kelloon?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: kesämökin piha järven rannalla. Vasemmalla tyttö pitelee pitkän narun päätä. Hän on juuri heilauttanut narua kerran. Narun toinen pää on sidottu puutolppaan, jonka varresta roikkuu messinkinen kello. Kireän narun keskivaiheilla on yksi kumpu matkalla kohti tolppaa. Taustalla ovat järvi, metsäinen ranta, punainen mökki, sauna ja koivuja." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-10-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Aalto on etenevä häiriö
Kun narun päätä heilautetaan ylös, käsi vetää mukanaan narun lähintä kohtaa. Jännittynyt naru vetää puolestaan seuraavaa kohtaa ja se taas seuraavaa, joten jokainen kohta lähtee liikkeelle hieman myöhemmin kuin edellinen. Näin poikkeama tasapainoasemasta eli häiriö etenee narussa kättä kauemmas. **Mekaaninen aaltoliike** on häiriön etenemistä väliaineessa. Väliaineen hiukkaset värähtelevät vain tasapainoasemansa ympärillä eivätkä kulje aallon mukana. Kaasussa molekyylit liikkuvat lisäksi satunnaisesti lämpöliikkeen vuoksi, mutta aalto ei kuljeta niitä mukanaan. Ideaalisessa aaltomallissa aalto kuljettaa siis energiaa lähteestä kauemmas, mutta ei ainetta. Siksi narun toisessa päässä oleva kello voi kilahtaa, vaikka mikään narun kohta ei kulje kädestä kelloon asti. Todellisissa aalloissa voi olla myös pientä nettokuljetusta: esimerkiksi veden pinta-aallossa vesihiukkaset kiertävät lähes suljettua rataa, mutta kelluva esine ajautuu hitaasti aallon suuntaan.

Mekaaninen aalto tarvitsee väliaineen, kuten narun, jousen, veden tai ilman. Yksi heilautus synnyttää **pulssin**, yksittäisen kummun, joka etenee narussa. Kun kättä heilutetaan tasaisesti ylös ja alas, syntyy jaksollinen aalto, jossa harjat ja pohjat toistuvat. Siinä narun jokainen kohta värähtelee samalla taajuudella $f$ kuin käsi. Jaksonaika $T$, taajuus $f$ ja amplitudi $A$ tarkoittavat samaa kuin luvussa *Värähtelyn suureet: jaksonaika, taajuus ja amplitudi*. Kun aalto saapuu narun päähän, se heijastuu takaisin; heijastumista tarkastellaan luvussa *Aalto kohtaa esteen tai raon*.

```pysahdy
Käsi heiluttaa narun päätä taajuudella $2{,}0\,\text{Hz}$. Millä taajuudella värähtelee narun kohta, joka on metrin päässä kädestä?
---
Se värähtelee samalla taajuudella $2{,}0\,\text{Hz}$. Jokainen narun kohta värähtelee samalla taajuudella kuin käsi, vaikka kohta liikahtaa myöhemmin.
```

### Poikittainen ja pitkittäinen aalto
Aallot jaetaan kahteen lajiin sen mukaan, mihin suuntaan väliaineen hiukkaset värähtelevät. **Poikittaisessa aallossa** hiukkaset värähtelevät kohtisuoraan aallon etenemissuuntaa vastaan: narun kohdat liikkuvat ylös ja alas, kun aalto etenee vaakasuoraan. **Pitkittäisessä aallossa** hiukkaset värähtelevät etenemissuunnan suuntaisesti. Kun pitkän kierrejousen päätä työnnetään edestakaisin, jouseen syntyy tihentymiä, joissa kierrokset ovat lähellä toisiaan, ja harvennuksia, joissa ne ovat kaukana toisistaan. Tihentymät ja harvennukset etenevät, mutta jokainen kierros vain heilahtelee paikkansa ympärillä. Esimerkiksi ääni ilmassa on pitkittäinen aalto.

<svg data-fig="types" viewBox="0 0 600 412" role="img" aria-label="Kaavakuva, ei mittakaavassa. Ylhäällä poikittainen aalto: naru on siniaallon muotoinen, ja sininen nuoli osoittaa aallon etenemissuunnan oikealle. Kolmessa narun kohdassa pystysuora kaksipäinen nuoli näyttää, että kohta liikkuu ylös ja alas eli kohtisuoraan etenemissuuntaa vastaan. Alhaalla pitkittäinen aalto: pitkän kierrejousen kierrokset ovat paikoin tiheässä (tihentymä) ja paikoin harvassa (harvennus). Yhden kierroksen yllä vaakasuora kaksipäinen nuoli näyttää, että kierros liikkuu edestakaisin jousen suuntaisesti. Sininen nuoli osoittaa tämänkin aallon etenemissuunnan oikealle." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-10-types.webp" x="0" y="0" width="600" height="420" preserveAspectRatio="none"/>
  <foreignObject x="24" y="9.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{poikittainen aalto}$</div></foreignObject>
  <foreignObject x="412" y="9.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="37.5" y="169.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kohdan liike}$</div></foreignObject>
  <foreignObject x="24" y="211.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{pitkittäinen aalto}$</div></foreignObject>
  <foreignObject x="412" y="211.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="165" y="247.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kierroksen liike}$</div></foreignObject>
  <foreignObject x="100" y="339.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tihentymä}$</div></foreignObject>
  <foreignObject x="300" y="339.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tihentymä}$</div></foreignObject>
  <foreignObject x="200" y="369.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{harvennus}$</div></foreignObject>
  <foreignObject x="400" y="369.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{harvennus}$</div></foreignObject>
</svg>

```pysahdy
Kierrejousen päätä työnnetään edestakaisin. Mihin suuntaan jousen kierrokset värähtelevät aallon etenemissuuntaan nähden?
---
Etenemissuunnan suuntaisesti. Aalto on siis pitkittäinen: tihentymät etenevät, mutta jokainen kierros heilahtelee vain paikallaan.
```

## Kaava: Aaltoliikkeen perusyhtälö
**Aallonpituus** $\lambda$ on kahden peräkkäisen harjan tai kahden peräkkäisen tihentymän välinen etäisyys. Se on lyhin etäisyys kahden sellaisen kohdan välillä, jotka liikkuvat täsmälleen samalla tavalla. Kun lähde tekee yhden täyden värähdyksen eli yhden jaksonajan $T$ aikana, aalto etenee tasan yhden aallonpituuden. Kuvan neljä hetkeä näyttävät, miten jokainen jaksonajan neljännes vie aaltoa neljäsosan aallonpituudesta eteenpäin.

<svg data-fig="birth" viewBox="0 0 600 420" role="img" aria-label="Kaavakuva: narun pää alkaa heilua ylös ja alas, ja narusta on piirretty neljä kuvaa allekkain hetkillä neljäsosa jaksonajasta, puolet, kolme neljäsosaa ja koko jaksonaika. Katkoviiva näyttää, mihin asti aalto on kunakin hetkenä edennyt: neljäsosan aallonpituudesta, puolet, kolme neljäsosaa ja koko aallonpituuden. Alimman kuvan alla mittajana näyttää, että yhden jaksonajan aikana aalto on edennyt yhden aallonpituuden. Rintaman takana naru on levossa." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-10-birth.webp" x="0" y="0" width="600" height="425" preserveAspectRatio="none"/>
  <foreignObject x="40" y="43.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t = \tfrac{1}{4}T$</div></foreignObject>
  <foreignObject x="40" y="125.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t = \tfrac{1}{2}T$</div></foreignObject>
  <foreignObject x="40" y="207.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t = \tfrac{3}{4}T$</div></foreignObject>
  <foreignObject x="53" y="289.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$t = T$</div></foreignObject>
  <foreignObject x="442" y="331.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="270" y="371.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
</svg>

Aallon nopeus on siis aallonpituus jaettuna jaksonajalla. Koska taajuus on $f = \tfrac{1}{T}$, saadaan **aaltoliikkeen perusyhtälö**
```kaavat
aaltoliikkeen perusyhtälö :: v = \frac{\lambda}{T} = f\lambda
```
missä $v$ on aallon etenemisnopeus ($\text{m/s}$), $\lambda$ aallonpituus ($\text{m}$), $T$ jaksonaika ($\text{s}$) ja $f$ taajuus ($\text{Hz}$). Yksiköt sopivat yhteen, koska $1\,\text{Hz} = 1\,\text{s}^{-1}$, joten $1\,\text{Hz} \cdot 1\,\text{m} = 1\,\text{m/s}$. Pulssin nopeuden voi mitata myös suoraan: pulssi etenee samassa väliaineessa tasaisella nopeudella, joten $v = \tfrac{s}{t}$, missä $s$ on matka ja $t$ siihen kulunut aika.

```pysahdy
Aallon aallonpituus on $0{,}50\,\text{m}$ ja jaksonaika $0{,}25\,\text{s}$. Mikä on aallon nopeus?
---
Nopeus on $v = \tfrac{\lambda}{T}$, eli $\tfrac{0{,}50\,\text{m}}{0{,}25\,\text{s}} = 2{,}0\,\text{m/s}$.
```

### Nopeus riippuu väliaineesta, taajuus lähteestä
Aallon nopeus määräytyy väliaineen ominaisuuksista. Kireässä narussa aalto etenee nopeammin kuin löysässä, ja ääni etenee $20\,{}^\circ\text{C}$:n ilmassa noin $343\,\text{m/s}$:n mutta vedessä noin $1500\,\text{m/s}$:n nopeudella. Taajuus määräytyy lähteestä: se on käden, jousen pään tai kaiuttimen värähtelyn taajuus. Ideaalisessa narussa aallon nopeus määräytyy narun jännityksestä ja massasta pituusyksikköä kohti, joten se ei riipu taajuudesta eikä pienestä amplitudista; samoin ilmassa äänen nopeus ei käytännössä riipu taajuudesta. Tämä ei ole kaikkien aaltojen yleinen laki: esimerkiksi veden pinta-aaltojen nopeus voi riippua aallonpituudesta, jolloin aaltoa sanotaan dispersiiviseksi. Tsunamin hyvin pitkä aalto taas etenee sitä nopeammin, mitä syvempää meri on. Kun samaa narua heilutetaan tiheämmin, nopeus pysyy samana ja aallonpituus lyhenee: kaksinkertainen taajuus puolittaa aallonpituuden. Kun aalto siirtyy väliaineesta toiseen, taajuus säilyy, mutta nopeus ja aallonpituus muuttuvat.

### Valokuva ja yhden kohdan kuvaaja
Aaltoa voi kuvata kahdella kuvaajalla, jotka näyttävät samanlaisilta siniaalloilta. **Valokuva** eli $(x, y)$-kuvaaja näyttää koko narun muodon yhdellä hetkellä: vaaka-akselilla on paikka $x$, ja kahden harjan väli on aallonpituus $\lambda$. **Yhden kohdan kuvaaja** eli $(t, y)$-kuvaaja näyttää yhden narun kohdan poikkeaman $y$ ajan funktiona: vaaka-akselilla on aika $t$, ja kahden huipun väli on jaksonaika $T$. Kummastakin kuvaajasta voi lukea amplitudin $A$. Lue siis aina ensin, mikä suure on vaaka-akselilla.

<svg data-fig="graphs" viewBox="0 0 600 556" role="img" aria-label="Kaksi kuvaajaa samasta aallosta allekkain, amplitudi 4 cm. Ylempi on valokuva koko narusta yhdellä hetkellä: vaaka-akselilla paikka x metreinä nollasta 2,5 metriin ja pystyakselilla poikkeama y senttimetreinä. Kahden peräkkäisen harjan väli, 1,0 m, on merkitty aallonpituudeksi lambda ja harjan korkeus amplitudiksi A. Alempi on yhden narun kohdan poikkeama ajan funktiona: vaaka-akselilla aika t sekunteina nollasta 1,25 sekuntiin. Kahden peräkkäisen huipun väli, 0,50 s, on merkitty jaksonajaksi T. Kuvaajat näyttävät samanmuotoisilta, mutta niiden vaaka-akselien suureet ovat eri." style="max-width:100%;font-size:24px">
  <foreignObject x="24" y="7.5" width="407" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{valokuva: koko naru yhdellä hetkellä}$</div></foreignObject>
  <foreignObject x="24" y="295.5" width="407" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{yksi kohta: poikkeama ajan funktiona}$</div></foreignObject>
  <line x1="12" y1="282" x2="588" y2="282" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="172" y1="236" x2="172" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248" y1="236" x2="248" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="324" y1="236" x2="324" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="400" y1="236" x2="400" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="236" x2="476" y2="104" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="214" x2="476" y2="214" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="126" x2="476" y2="126" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="236" x2="96" y2="170" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="95" y1="170" x2="490" y2="170" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,170 L489,176 L489,164 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="171" x2="96" y2="90" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,78 L102,91 L90,91 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="172" y1="170" x2="172" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="248" y1="170" x2="248" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="324" y1="170" x2="324" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="170" x2="400" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="476" y1="170" x2="476" y2="177" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="214" x2="96" y2="214" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="199.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-4$</div></foreignObject>
  <line x1="89" y1="170" x2="96" y2="170" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="89" y1="126" x2="96" y2="126" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="111.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="508" y="155.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <foreignObject x="86" y="47.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$y\ (\text{cm})$</div></foreignObject>
  <foreignObject x="149.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0{,}5$</div></foreignObject>
  <foreignObject x="238" y="241.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1$</div></foreignObject>
  <foreignObject x="301.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1{,}5$</div></foreignObject>
  <foreignObject x="390" y="241.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$2$</div></foreignObject>
  <foreignObject x="453.5" y="241.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$2{,}5$</div></foreignObject>
  <polyline points="96,170 99,164.5 102.5,158.5 105.5,153 108.5,148 112,143 115,139 118,135 121.5,132 124.5,129.5 127.5,127.5 131,126.5 134,126 137,126.5 140.5,127.5 143.5,129.5 146.5,132 150,135 153,139 156,143 159.5,148 162.5,153 165.5,158.5 169,164.5 172,170 175,175.5 178.5,181.5 181.5,187 184.5,192 188,197 191,201 194,205 197.5,208 200.5,210.5 203.5,212.5 207,213.5 210,214 213,213.5 216.5,212.5 219.5,210.5 222.5,208 226,205 229,201 232,197 235.5,192 238.5,187 241.5,181.5 245,175.5 248,170 251,164.5 254.5,158.5 257.5,153 260.5,148 264,143 267,139 270,135 273.5,132 276.5,129.5 279.5,127.5 283,126.5 286,126 289,126.5 292.5,127.5 295.5,129.5 298.5,132 302,135 305,139 308,143 311.5,148 314.5,153 317.5,158.5 321,164.5 324,170 327,175.5 330.5,181.5 333.5,187 336.5,192 340,197 343,201 346,205 349.5,208 352.5,210.5 355.5,212.5 359,213.5 362,214 365,213.5 368.5,212.5 371.5,210.5 374.5,208 378,205 381,201 384,197 387.5,192 390.5,187 393.5,181.5 397,175.5 400,170 403,164.5 406.5,158.5 409.5,153 412.5,148 416,143 419,139 422,135 425.5,132 428.5,129.5 431.5,127.5 435,126.5 438,126 441,126.5 444.5,127.5 447.5,129.5 450.5,132 454,135 457,139 460,143 463.5,148 466.5,153 469.5,158.5 473,164.5 476,170" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="134" y1="113" x2="286" y2="113" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="134" y1="105" x2="134" y2="121" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="286" y1="105" x2="286" y2="121" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="200" y="78.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <line x1="134" y1="126" x2="134" y2="121" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="286" y1="126" x2="286" y2="121" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="134" y1="170" x2="134" y2="135" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M134,126 L138.5,136 L129.5,136 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="141" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$A$</div></foreignObject>
  <line x1="172" y1="522" x2="172" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248" y1="522" x2="248" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="324" y1="522" x2="324" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="400" y1="522" x2="400" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="522" x2="476" y2="390" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="500" x2="476" y2="500" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="412" x2="476" y2="412" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="522" x2="96" y2="456" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="95" y1="456" x2="490" y2="456" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,456 L489,462 L489,450 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="457" x2="96" y2="376" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,364 L102,377 L90,377 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="172" y1="456" x2="172" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="248" y1="456" x2="248" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="324" y1="456" x2="324" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="400" y1="456" x2="400" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="476" y1="456" x2="476" y2="463" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="500" x2="96" y2="500" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="485.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-4$</div></foreignObject>
  <line x1="89" y1="456" x2="96" y2="456" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="441.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="89" y1="412" x2="96" y2="412" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="397.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="508" y="441.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="333.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$y\ (\text{cm})$</div></foreignObject>
  <foreignObject x="143" y="527.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0{,}25$</div></foreignObject>
  <foreignObject x="225.5" y="527.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0{,}5$</div></foreignObject>
  <foreignObject x="295" y="527.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0{,}75$</div></foreignObject>
  <foreignObject x="390" y="527.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1$</div></foreignObject>
  <foreignObject x="447" y="527.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$1{,}25$</div></foreignObject>
  <polyline points="96,456 99,450.5 102.5,444.5 105.5,439 108.5,434 112,429 115,425 118,421 121.5,418 124.5,415.5 127.5,413.5 131,412.5 134,412 137,412.5 140.5,413.5 143.5,415.5 146.5,418 150,421 153,425 156,429 159.5,434 162.5,439 165.5,444.5 169,450.5 172,456 175,461.5 178.5,467.5 181.5,473 184.5,478 188,483 191,487 194,491 197.5,494 200.5,496.5 203.5,498.5 207,499.5 210,500 213,499.5 216.5,498.5 219.5,496.5 222.5,494 226,491 229,487 232,483 235.5,478 238.5,473 241.5,467.5 245,461.5 248,456 251,450.5 254.5,444.5 257.5,439 260.5,434 264,429 267,425 270,421 273.5,418 276.5,415.5 279.5,413.5 283,412.5 286,412 289,412.5 292.5,413.5 295.5,415.5 298.5,418 302,421 305,425 308,429 311.5,434 314.5,439 317.5,444.5 321,450.5 324,456 327,461.5 330.5,467.5 333.5,473 336.5,478 340,483 343,487 346,491 349.5,494 352.5,496.5 355.5,498.5 359,499.5 362,500 365,499.5 368.5,498.5 371.5,496.5 374.5,494 378,491 381,487 384,483 387.5,478 390.5,473 393.5,467.5 397,461.5 400,456 403,450.5 406.5,444.5 409.5,439 412.5,434 416,429 419,425 422,421 425.5,418 428.5,415.5 431.5,413.5 435,412.5 438,412 441,412.5 444.5,413.5 447.5,415.5 450.5,418 454,421 457,425 460,429 463.5,434 466.5,439 469.5,444.5 473,450.5 476,456" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="134" y1="399" x2="286" y2="399" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="134" y1="391" x2="134" y2="407" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="286" y1="391" x2="286" y2="407" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="200" y="364.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="134" y1="412" x2="134" y2="407" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="286" y1="412" x2="286" y2="407" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="134" y1="456" x2="134" y2="421" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M134,412 L138.5,422 L129.5,422 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="141" y="431.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$A$</div></foreignObject>
</svg>

## Esimerkki
Pitkä naru on vedetty kireälle pihan poikki. Kun narun päätä heilautetaan kerran, syntyvä pulssi kulkee $6{,}0\,\text{m}$:n matkan $2{,}5\,\text{s}$:ssa. Sitten samaa narua heilutetaan tasaisesti taajuudella $3{,}0\,\text{Hz}$, eikä narun jännitys muutu. Kuinka pitkä on syntyvän aallon aallonpituus?

<!-- vaihe -->

**Tunnetut ja kysytty.** Pulssin kulkema matka $s = 6{,}0\,\text{m}$ ja siihen kulunut aika $t = 2{,}5\,\text{s}$, jaksollisen aallon taajuus $f = 3{,}0\,\text{Hz}$.

Kysytään aallonpituutta $\lambda$.

<!-- vaihe -->

**Periaate.** Aallon nopeus riippuu väliaineen ominaisuuksista, tässä narun jännityksestä ja massasta pituusyksikköä kohti, ei siitä, tehdäänkö narussa pulssi vai jaksollinen aalto. Siksi jaksollinen aalto etenee samalla nopeudella $v$ kuin pulssi, ja pulssi etenee tasaisesti, joten $v = \tfrac{s}{t}$. Aallonpituus saadaan sitten perusyhtälöstä $v = f\lambda$.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&v = \frac{s}{t} \quad\text{ja}\quad v = f\lambda \\
&\lambda = \frac{v}{f} = \frac{s}{f\,t}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: matka on metreinä ja aika sekunteina, ja $1\,\text{Hz} = 1\,\text{s}^{-1}$, joten $\tfrac{\text{m/s}}{\text{Hz}} = \text{m}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin nopeus ja sitten aallonpituus:
```latex
\begin{aligned}
&v = \frac{s}{t} \\
&= \frac{6{,}0\,\text{m}}{2{,}5\,\text{s}} = 2{,}4\,\text{m/s} \\[6pt]
&\lambda = \frac{v}{f} \\
&= \frac{2{,}4\,\text{m/s}}{3{,}0\,\text{Hz}} = 0{,}80\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Aallonpituus on $0{,}80\,\text{m}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla kuten lähtötiedot $6{,}0\,\text{m}$, $2{,}5\,\text{s}$ ja $3{,}0\,\text{Hz}$.

<!-- vaihe -->

**Järkevyys.** Jaksonaika on $T = \tfrac{1}{f} = 0{,}333\,\text{s}$, ja siinä ajassa aalto etenee $2{,}4\,\text{m/s} \cdot 0{,}333\,\text{s} = 0{,}80\,\text{m}$ eli juuri yhden aallonpituuden, kuten pitääkin.

## Yleinen virhekäsitys
Moni ajattelee, että aalto etenee sitä nopeammin, mitä tiheämmin kättä heilutetaan. Samassa narussa nopeus pysyy kuitenkin samana. Kun taajuus kasvaa $1{,}0\,\text{Hz}$:stä $2{,}0\,\text{Hz}$:iin, aallonpituus lyhenee $2{,}0\,\text{m}$:stä $1{,}0\,\text{m}$:iin, ja tulo $f\lambda$ on edelleen $2{,}0\,\text{m/s}$. Nopeuden voi muuttaa vain muuttamalla narua tai sen jännitystä, esimerkiksi kiristämällä narua.

Toinen yleinen virhe on lukea aallonpituus yhden kohdan $(t, y)$-kuvaajasta. Siinä huippujen väli on jaksonaika $T$ sekunteina, ei aallonpituus. Kolmas virhe on ajatella, että aalto kuljettaa narun ainetta mukanaan: narun kohdat vain värähtelevät paikallaan, ja eteenpäin siirtyy energia.

## Tiivistelmä
- Mekaaninen aaltoliike on häiriön etenemistä väliaineessa. Väliaineen hiukkaset värähtelevät tasapainoasemansa ympärillä, ja ideaalinen aalto kuljettaa energiaa mutta ei ainetta.
- Poikittaisessa aallossa hiukkaset värähtelevät kohtisuoraan etenemissuuntaa vastaan (naru), pitkittäisessä aallossa etenemissuunnan suuntaisesti (kierrejousi, ääni ilmassa).
- Yksi heilautus tekee pulssin, tasainen heilutus jaksollisen aallon. Aallonpituus $\lambda$ on kahden peräkkäisen harjan väli.
- Aaltoliikkeen perusyhtälö on $v = \tfrac{\lambda}{T} = f\lambda$. Nopeus riippuu väliaineesta, taajuus lähteestä.
- Valokuvasta eli $(x, y)$-kuvaajasta luetaan aallonpituus, yhden kohdan $(t, y)$-kuvaajasta jaksonaika.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: stadionin katsomo. Kolmessa rivissä istuu katsojia, ja keskellä joukko katsojia on noussut seisomaan kädet ylhäällä. Seisovien vieressä katsojat ovat puoliksi nousseet tai istuutumassa. Katsojat eivät vaihda paikkaa, mutta nousemisen kohta kiertää katsomossa." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-10-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
