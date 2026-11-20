# Oma kokeellinen tutkimus: suunnittelu, toteutus ja raportointi

> **Miksi** kaksi ryhmää saa samalle leluautolle eri nopeuden, vaikka kumpikin mittaa huolellisesti?

<svg data-fig="hero" data-style="house" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: luokan lattialla on rata. Leluauto kulkee radalla mittanauhan vieressä. Radan kummallakin puolella on ryhmä. Kummallakin ryhmällä on oma sekuntikello. Kellojen viisarit ovat pysähtyneet eri kohtiin." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy1/fy1-8-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Fysiikka on kokeellinen tiede. Fysiikan väitteitä arvioidaan havaintojen ja mittausten avulla. Hyvässä tutkimuksessa menetelmät kerrotaan tarkasti. Silloin muut voivat tarkistaa tulokset ja usein myös toistaa mittaukset. **Tutkimus** on järjestelmällinen tapa vastata kysymykseen mittaamalla. Tutkimus alkaa kysymyksestä. Se päättyy johtopäätökseen, jonka mittaustulokset perustelevat. Hyvä tutkimus ei ole sellainen, jossa oletus osoittautuu oikeaksi. Hyvässä tutkimuksessa mittaus voisi näyttää oletuksen vääräksi.

<figure class="unit-photo"><img src="pics/fy1/ligo-scientists-laser-room.webp" alt="Kaksi suojapukuista tutkijaa katsoo laitetta valkoisessa huoneessa."><figcaption>Tutkijat tutkivat LIGO-laitoksen laserlaitetta puhtaassa huoneessa Yhdysvalloissa vuonna 2019.</figcaption></figure>

### Tutkimuskysymys ja hypoteesi
Tutkimuskysymys on kysymys, johon mittaus voi vastata. Esimerkki on "Miten leluauton kulkuaika riippuu ajomatkan pituudesta?" Kysymys "Mikä auto on paras?" ei kelpaa, koska sitä ei voi mitata.

**Hypoteesi** on perusteltu ja testattava ennuste, joka vastaa tutkimuskysymykseen. Esimerkiksi: "Auto liikkuu radalla vakionopeudella. Siksi sen kulkema matka on suoraan verrannollinen aikaan, $s = vt$." Hypoteesista pitää seurata jotain mitattavaa. Sen pitää myös voida osoittautua vääräksi. Ennuste "auto kulkee jotenkin" ei ole hypoteesi, koska mikään mittaus ei voi kumota sitä eli osoittaa sitä vääräksi.

```pysahdy
Ennuste on: "Jos matka kaksinkertaistuu, kulkuaika kaksinkertaistuu." Kelpaako se hypoteesiksi? Miksi?
---
Kelpaa. Siitä seuraa jotain mitattavaa. Mittaus voi myös näyttää sen vääräksi, jos aika ei kaksinkertaistu.
```

### Muuttujat
**Muuttuja** on suure tai muu asia, joka voi vaihdella tutkimuksessa. Kokeessa tehdään kolme asiaa. Yhtä muuttujaa muutetaan, toista mitataan ja kaikki muut pidetään samoina:

- **muutettava muuttuja**: kokeen tekijä valitsee sen arvot, tässä matka $s$
- **mitattava muuttuja**: sen arvo luetaan mittarista, tässä aika $t$
- **vakioitavat muuttujat**: ne pysyvät samoina koko kokeen ajan, tässä auto, paristot, alusta ja lähtötapa.

Joskus kaksi muuttujaa muuttuu yhtä aikaa, esimerkiksi matka ja paristot. Silloin ei voi päätellä, mikä muutti tulosta. Siksi koe on reilu vasta, kun vain muutettava muuttuja vaihtuu.

```pysahdy
Ryhmä vaihtaa matkaa. Samalla se vaihtaa leluautoon uudet paristot. Aika lyhenee. Voiko ryhmä päätellä, mikä sen aiheutti?
---
Ei voi. Kaksi muuttujaa muuttui yhtä aikaa. Silloin syytä ei voi päätellä. Vain muutettava muuttuja saa vaihtua.
```

<svg data-fig="setup" data-style="house" viewBox="0 0 600 414" role="img" aria-label="Kaavakuva kokeen asetelmasta. Leluauto toimii paristoilla. Se ajaa pöydällä lähtöviivalta maaliviivalle. Maalissa on ruutulippu. Pöydän reunassa on mittanauha, jonka asteikko on metreinä. Lähtöviivan ja maaliviivan väli on muutettava muuttuja, matka s. Sekuntikello mittaa aikaa t. Aika on mitattava muuttuja. Vakioina pysyvät auto, alusta ja paristot. Asteikko on mittakaavassa: 150 yksikköä kuvassa vastaa metriä." style="max-width:100%;font-size:24px">
  <image href="pics/fy1/fy1-8-setup.webp" x="0" y="-1.2" width="600" height="420" preserveAspectRatio="none"/>
  <foreignObject x="24" y="13.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{muutettava: } s$</div></foreignObject>
  <foreignObject x="24" y="47.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{mitattava: } t$</div></foreignObject>
  <foreignObject x="24" y="81.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vakiona: auto, alusta, paristot}$</div></foreignObject>
  <foreignObject x="526" y="117.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="62" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="124.5" y="277.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}5$</div></foreignObject>
  <foreignObject x="212" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="274.5" y="277.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}5$</div></foreignObject>
  <foreignObject x="362" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="424.5" y="277.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}5$</div></foreignObject>
  <foreignObject x="475" y="277.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s\ (\text{m})$</div></foreignObject>
  <foreignObject x="41" y="123.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lähtö}$</div></foreignObject>
  <foreignObject x="341" y="145.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{maali}$</div></foreignObject>
  <foreignObject x="284" y="179.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="168" y="337.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$s = 2{,}00\,\text{m}$</div></foreignObject>
</svg>

### Suunnittelu ennen mittausta
Ennen suunnittelua hankitaan taustatietoa ilmiöstä ja menetelmistä. Lähdettä arvioidaan lähdekriittisesti: kuka tiedon on tuottanut ja miksi, miten se perustellaan, onko se ajantasaista ja tukevatko muut lähteet sitä.

Suunnitelma vastaa ennen mittausta näihin kysymyksiin:

- Mitä mitataan ja millä välineellä?
- Mitkä arvot muutettavalle muuttujalle valitaan, ja kuinka monta?
- Montako toistoa kustakin arvosta tehdään?
- Mitä pidetään vakiona?

Kokeile suunnitelmaa ensin esikokeella. Esikoe kertoo, onko mittaus ylipäätään mahdollinen. Se antaa myös karkean arvion tuloksesta.

Valitse mittausalue niin, että mitattava suure on selvästi suurempi kuin mittauksen epävarmuus (ks. kohta *Suhteellinen epävarmuus ja mittausalueen valinta*). Valitse useita arvoja ja pidä niiden välit yhtä suurina. Yksi tai kaksi pistettä ei näytä, onko riippuvuus suora.

### Mittauspöytäkirja
**Mittauspöytäkirja** on kirjaus, joka tehdään kokeen aikana. Sitä ei tehdä muistista jälkikäteen. Siihen kirjataan nämä asiat:

- tutkimuskysymys ja päivämäärä
- välineet ja niiden tarkkuus
- vakioidut asiat
- mittaukset taulukkona yksiköineen
- havainnot, esimerkiksi "auto kääntyi sivuun".

Kirjaa lukemat sellaisenaan. Silloin kirjaus pysyy objektiivisena eli ei muutu omien odotusten mukaiseksi. Älä poista tai korjaa hiljaa mittausta, joka näyttää oudolta. Merkitse se ja kirjaa, mitä silloin tapahtui. Lyhyt esimerkki:

| $s\ (\text{m})$ | $t_1\ (\text{s})$ | $t_2\ (\text{s})$ | $t_3\ (\text{s})$ | huomio |
|---|---|---|---|---|
| 0,50 | 1,3 | 1,1 | 1,4 | vaikea ajoittaa |
| 1,00 | 2,5 | 2,3 | 2,6 | |
| 1,50 | 3,7 | 3,5 | 3,6 | |

### Raportti
**Raportti** kertoo tutkimuksen niin, että toinen voi toistaa sen. Toinen voi myös arvioida johtopäätöksen. Raportin osat ovat:

1. tutkimuskysymys ja hypoteesi
2. menetelmä: välineet, muuttujat ja toteutus
3. tulokset: taulukko, kuvaaja ja suureen arvo epävarmuuksineen
4. pohdinta: virhelähteet ja se, mitä seuraavalla kerralla tehtäisiin toisin
5. johtopäätös: vastaus tutkimuskysymykseen ja se, tukevatko tulokset hypoteesia.

Johtopäätös on vain niin vahva kuin aineisto. Jos mittaukset vastaavat ennustetta epävarmuuden rajoissa, hypoteesi on saanut tukea. Sitä ei silti ole todistettu.

## Kaava: Suhteellinen epävarmuus ja mittausalueen valinta
Käsin mitatun ajan epävarmuus $\Delta t$ johtuu pääosin reaktioajasta. Se on lähes sama lyhyessä ja pitkässä mittauksessa. Siksi mittauksen laatua kuvaa **suhteellinen epävarmuus**. Se tarkoittaa epävarmuutta suhteessa mitattuun arvoon. Suhteellinen epävarmuus saa olla enintään $\varepsilon_\text{max}$. Silloin mitattavan ajan pitää olla vähintään
```latex
\begin{aligned}
\varepsilon &= \frac{\Delta t}{t} \\
t &\ge \frac{\Delta t}{\varepsilon_\text{max}}
\end{aligned}
```
missä $\varepsilon$ on suhteellinen epävarmuus (ilmoitetaan usein prosentteina), $\Delta t$ ajan epävarmuus (s) ja $t$ mitattu aika (s). Esimerkki: epävarmuus on $\Delta t = 0{,}2\,\text{s}$ ja raja on $5\,\%$. Silloin aikaa pitää olla vähintään $4\,\text{s}$.

<svg data-fig="epavarmuus" data-style="house" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja näyttää suhteellisen epävarmuuden ajan funktiona. Ajan epävarmuus on 0,2 s. Kun aika on 1 s, epävarmuus on 20 %. Kun aika on 4 s, epävarmuus on 5,0 %. Kun aika on 10 s, epävarmuus on 2,0 %. Vihreä alue näyttää mittaukset, joiden epävarmuus on enintään 5,0 %. Ne vaativat vähintään 4 s:n ajan. Kuvaaja on mittakaavassa." style="max-width:100%;font-size:24px">
  <line x1="176" y1="286" x2="176" y2="54" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="256" y1="286" x2="256" y2="54" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="336" y1="286" x2="336" y2="54" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="416" y1="286" x2="416" y2="54" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="496" y1="286" x2="496" y2="54" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="96" y1="237.5" x2="496" y2="237.5" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="96" y1="189.5" x2="496" y2="189.5" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="96" y1="141" x2="496" y2="141" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="96" y1="92.5" x2="496" y2="92.5" stroke="#e7e2d7" stroke-width="1" stroke-linecap="butt"/>
  <line x1="95" y1="286" x2="514" y2="286" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M522,286 L510.5,291 L514,286 L510.5,281 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="287" x2="96" y2="36" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <path d="M96,28 L101,39.5 L96,36 L91,39.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="176" y1="286" x2="176" y2="293" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="166" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="256" y1="286" x2="256" y2="293" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="246" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="336" y1="286" x2="336" y2="293" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="326" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="416" y1="286" x2="416" y2="293" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="406" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="496" y1="286" x2="496" y2="293" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="479.5" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="237.5" x2="96" y2="237.5" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="64" y="223" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="89" y1="189.5" x2="96" y2="189.5" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="51" y="175" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="141" x2="96" y2="141" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="51" y="126.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="89" y1="92.5" x2="96" y2="92.5" stroke="#1f2933" stroke-width="1.75" stroke-linecap="butt"/>
  <foreignObject x="51" y="78" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <foreignObject x="66" y="291.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="528" y="271.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="-2.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\varepsilon\ (\%)$</div></foreignObject>
  <polygon points="256,286 496,286 496,237.5 256,237.5" fill="#b2f2bb" fill-opacity="0.7"/>
  <line x1="96" y1="237.5" x2="496" y2="237.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <polyline points="136,92.5 139,106 142,118 145,128 148,137.5 151,145.5 154,152.5 157,159 160,165 163,170.5 166,175.5 169,180 172,184 175,188 178,191.5 181,195 184,198 187,201 190,203.5 193,206.5 196,208.5 199,211 202,213 205,215 208,217 211,219 214,220.5 217,222 220,223.5 223,225 226,226.5 229,228 232,229 235,230.5 238,231.5 241,232.5 244,233.5 247,235 250,236 253,236.5 256,237.5 259,238.5 262,239.5 265,240 268,241 271,242 274,242.5 277,243.5 280,244 283,244.5 286,245.5 289,246 292,246.5 295,247 298,247.5 301,248.5 304,249 307,249.5 310,250 313,250.5 316,251 319,251.5 322,252 325,252 328,252.5 331,253 334,253.5 337,254 340,254.5 343,254.5 346,255 349,255.5 352,256 355,256 358,256.5 361,257 364,257 367,257.5 370,258 373,258 376,258.5 379,258.5 382,259 385,259 388,259.5 391,260 394,260 397,260.5 400,260.5 403,261 406,261 409,261.5 412,261.5 415,262 418,262 421,262 424,262.5 427,262.5 430,263 433,263 436,263.5 439,263.5 442,263.5 445,264 448,264 451,264 454,264.5 457,264.5 460,265 463,265 466,265 469,265.5 472,265.5 475,265.5 478,266 481,266 484,266 487,266 490,266.5 493,266.5 496,266.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="256" y1="237.5" x2="256" y2="286" stroke="#6b7480" stroke-width="1.25" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="96" y1="237.5" x2="256" y2="237.5" stroke="#6b7480" stroke-width="1.25" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <circle cx="256" cy="237.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="304" y="188.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\varepsilon \le 5\,\%$</div></foreignObject>
  <foreignObject x="184" y="73.5" width="180" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\varepsilon = \dfrac{0{,}2\,\text{s}}{t}$</div></foreignObject>
</svg>

```pysahdy
Ajan epävarmuus on $0{,}2\,\text{s}$. Suhteellinen epävarmuus saa olla enintään $2{,}0\,\%$. Kuinka pitkä aika pitää vähintään mitata?
---
Aika pitää olla vähintään $t = \Delta t/\varepsilon_\text{max}$, joten $t = 0{,}2\,\text{s}/0{,}020 = 10\,\text{s}$.
```

Tarvittava matka saadaan tasaisen liikkeen mallista $s = vt$. Jos mittaus tehdään usealla matkalla, mittauspisteisiin sovitetaan suora (luku *Graafinen esitys ja suoran sovittaminen*). Aika $t$ on vaaka-akselilla ja matka $s$ pystyakselilla. Silloin suoran kulmakerroin on nopeus $v$. Lyhin kelvollinen matka on se, jolla suhteellinen epävarmuus vielä pysyy valitussa rajassa $\varepsilon_\text{max}$. Lyhyemmällä matkalla suhteellinen epävarmuus ylittää tämän rajan. Silloin tulos on liian epätarkka.

## Esimerkki
Oppilaat tutkivat leluauton liikettä. Esikokeessa auton nopeus on noin $0{,}42\,\text{m/s}$. Aika mitataan käsikellolla. Ajanoton epävarmuus on $\Delta t = 0{,}2\,\text{s}$. Ajanmittauksen suhteellinen epävarmuus saa olla enintään $5{,}0\,\%$. Kuinka pitkä matka auton pitää vähintään kulkea?

<!-- vaihe -->

**Tunnetut ja kysytty.** Nopeus $v = 0{,}42\,\text{m/s}$, ajan epävarmuus $\Delta t = 0{,}2\,\text{s}$ ja suurin sallittu suhteellinen epävarmuus $\varepsilon_\text{max} = 5{,}0\,\% = 0{,}050$.

Kysytään lyhintä matkaa $s_\text{min}$.

<!-- vaihe -->

**Periaate.** Mitattava aika kasvaa, ja silloin suhteellinen epävarmuus pienenee, koska $\Delta t$ pysyy samana. Lasketaan ensin lyhin sallittu aika epävarmuuden rajasta. Auto liikkuu vakionopeudella. Siksi tasaisen liikkeen malli $s = vt$ antaa ajasta matkan.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&t_\text{min} = \frac{\Delta t}{\varepsilon_\text{max}} \\
&s_\text{min} = v\, t_\text{min} = \frac{v\,\Delta t}{\varepsilon_\text{max}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Niitä ei tarvita. Nopeus on yksikössä $\text{m/s}$ ja aika sekunteina, joten matka tulee metreinä. Prosentti on muunnettu desimaaliluvuksi: $5{,}0\,\% = 0{,}050$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
t_\text{min} &= \frac{\Delta t}{\varepsilon_\text{max}} \\
&= \frac{0{,}2\,\text{s}}{0{,}050} = 4\,\text{s} \\
s_\text{min} &= v\, t_\text{min} \\
&= 0{,}42\,\tfrac{\text{m}}{\text{s}} \cdot 4\,\text{s} \\
&= 1{,}68\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Matkan pitää olla vähintään $1{,}7\,\text{m}$. Tämä on suunnitteluarvio. Sen tarkkuutta rajoittaa epävarmuus $0{,}2\,\text{s}$, joka on annettu yhdellä numerolla. Siksi vähimmäismatka ilmoitetaan käytännön tarkkuudella, tässä kahdella numerolla kuten nopeus $0{,}42\,\text{m/s}$. Matka pyöristetään ylöspäin, jotta raja varmasti täyttyy.

<!-- vaihe -->

**Järkevyys.** Matkalla $1{,}7\,\text{m}$ auton kulkuaika on noin $1{,}7\,\text{m} : 0{,}42\,\text{m/s} \approx 4{,}05\,\text{s}$. Silloin $\varepsilon = 0{,}2\,\text{s} : 4{,}05\,\text{s} \approx 4{,}9\,\%$ eli juuri ja juuri rajan sisällä. Matkalla $0{,}50\,\text{m}$ aika olisi vain $1{,}2\,\text{s}$ ja epävarmuus noin $17\,\%$. Siksi lyhyt matka olisi huono valinta.

## Yleinen virhekäsitys
Moni ajattelee, että tutkimus on epäonnistunut, jos mittaus ei tue hypoteesia. Näin ei ole. Jos mittaus kumoaa hypoteesin, tutkija tietää jotakin, mitä hän ei aiemmin tiennyt. Epäonnistunut tutkimus on sellainen, josta ei voi päätellä mitään. Silloin muuttujia ei ole hallittu tai mittaukset ovat liian epävarmoja.

Toinen yleinen virhe on pitää yhtä mittausta riittävänä. Yksi lukema ei kerro, kuinka paljon tulos vaihtelee. Siksi satunnaisvirheen aiheuttamaa hajontaa ei voi arvioida. Kolmas virhe on valita tulokseen sopivat mittaukset ja jättää muut pois. Kaikki mittaukset kirjataan, ja poikkeava mittaus selitetään tai merkitään.

## Tiivistelmä
- Tutkimus alkaa kysymyksestä, jonka voi mitata. Siinä on myös hypoteesi, jonka voi testata ja joka voi osoittautua vääräksi.
- Reilussa kokeessa muutetaan yhtä muuttujaa, mitataan toista ja pidetään muut vakioina.
- Mittaus suunnitellaan etukäteen: mittausalue, pisteiden määrä, toistot ja vakioidut asiat. Esikoe tarkistaa suunnitelman.
- Pöytäkirjaan kirjataan lukemat, yksiköt, välineet ja havainnot kokeen aikana. Mitään mittausta ei poisteta hiljaa.
- Suhteellinen epävarmuus $\varepsilon = \Delta t : t$ pienenee, kun mitattava aika kasvaa. Siksi aikaa on oltava vähintään $\Delta t : \varepsilon_\text{max}$.
- Raportti kertoo kysymyksen, menetelmän, tulokset, pohdinnan ja johtopäätöksen. Näin toinen voi toistaa tutkimuksen.
