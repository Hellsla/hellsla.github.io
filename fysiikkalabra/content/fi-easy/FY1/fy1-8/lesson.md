# Oma kokeellinen tutkimus: suunnittelu, toteutus ja raportointi

> **Miksi** kaksi ryhmää saa samalle leluautolle eri nopeuden, vaikka kumpikin mittaa huolellisesti?

## Ydinajatus
Fysiikka on kokeellinen tiede. Väite pätee vasta, kun sitä on testattu mittauksilla. Kuka tahansa voi toistaa nämä mittaukset. **Tutkimus** on järjestelmällinen tapa vastata kysymykseen mittaamalla. Tutkimus alkaa kysymyksestä. Se päättyy johtopäätökseen, jonka mittaustulokset perustelevat. Hyvä tutkimus ei ole sellainen, jossa oletus osoittautuu oikeaksi. Hyvässä tutkimuksessa mittaus voisi näyttää oletuksen vääräksi.

### Tutkimuskysymys ja hypoteesi
Tutkimuskysymys on kysymys, johon mittaus voi vastata. Esimerkki on "Miten leluauton kulkema matka riippuu ajasta?" Kysymys "Mikä auto on paras?" ei kelpaa, koska sitä ei voi mitata.

**Hypoteesi** on perusteltu ja testattava ennuste kysymykseen. Esimerkiksi: "Jos auto liikkuu vakionopeudella, kulkema matka on suoraan verrannollinen aikaan, $s = vt$." Hypoteesista pitää seurata jotain mitattavaa. Sen pitää myös voida osoittautua vääräksi. Ennuste "auto kulkee jotenkin" ei ole hypoteesi, koska mikään mittaus ei kumoa sitä.

### Muuttujat
**Muuttuja** on suure, jonka arvo voi vaihdella tutkimuksessa. Kokeessa tehdään kolme asiaa. Yhtä muuttujaa muutetaan, toista mitataan ja kaikki muut pidetään samoina:
- **muutettava muuttuja**: kokeen tekijä valitsee sen arvot, tässä matka $s$
- **mitattava muuttuja**: sen arvo luetaan mittarista, tässä aika $t$
- **vakioitavat muuttujat**: ne pysyvät samoina koko kokeen ajan, tässä auto, paristot, alusta ja lähtötapa.

Joskus kaksi muuttujaa muuttuu yhtä aikaa, esimerkiksi matka ja paristot. Silloin ei voi päätellä, mikä muutti tulosta. Siksi koe on reilu vasta, kun vain muutettava muuttuja vaihtuu.

<svg data-fig="setup" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva kokeen asetelmasta. Leluauto ajaa pöydällä tasaisella radalla lähtöviivalta maaliviivalle. Radan vieressä on matka-asteikko metreinä. Lähtöviivan ja maaliviivan väli on muutettava muuttuja, matka s. Käsikello mittaa aikaa t. Aika on mitattava muuttuja. Vakioina pysyvät auto, alusta ja paristot. Asteikko on mittakaavassa: 150 yksikköä kuvassa vastaa metriä." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy18-wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <foreignObject x="24" y="13.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{muutettava: } s$</div></foreignObject>
  <foreignObject x="24" y="47.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{mitattava: } t$</div></foreignObject>
  <foreignObject x="24" y="81.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vakiona: auto, alusta, paristot}$</div></foreignObject>
  <rect x="514" y="20" width="12" height="12" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <circle cx="520" cy="66" r="30" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <line x1="520" y1="44" x2="520" y2="39" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="531" y1="47" x2="533.5" y2="42.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="539" y1="55" x2="543.5" y2="52.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="542" y1="66" x2="547" y2="66" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="539" y1="77" x2="543.5" y2="79.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="531" y1="85" x2="533.5" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="88" x2="520" y2="93" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="509" y1="85" x2="506.5" y2="89.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="501" y1="77" x2="496.5" y2="79.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="498" y1="66" x2="493" y2="66" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="501" y1="55" x2="496.5" y2="52.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="509" y1="47" x2="506.5" y2="42.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="66" x2="536" y2="52" stroke="#e8590c" stroke-width="3" stroke-linecap="round"/>
  <circle cx="520" cy="66" r="3.5" fill="#1f2933"/>
  <foreignObject x="510" y="103.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$t$</div></foreignObject>
  <rect x="40" y="200" width="520" height="16" fill="url(#fy18-wood)" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="72" y1="216" x2="72" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="62" y="227.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="147" y1="216" x2="147" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="124.5" y="227.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}5$</div></foreignObject>
  <line x1="222" y1="216" x2="222" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="212" y="227.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="297" y1="216" x2="297" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="274.5" y="227.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}5$</div></foreignObject>
  <line x1="372" y1="216" x2="372" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="362" y="227.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="447" y1="216" x2="447" y2="224" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="424.5" y="227.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}5$</div></foreignObject>
  <foreignObject x="475" y="227.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s\ (\text{m})$</div></foreignObject>
  <line x1="72" y1="140" x2="72" y2="200" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="37" y="111.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lähtö}$</div></foreignObject>
  <line x1="372" y1="140" x2="372" y2="200" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="337" y="111.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{maali}$</div></foreignObject>
  <rect x="92" y="166" width="68" height="22" rx="6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="108" y="148" width="36" height="18" rx="5" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="110" cy="191" r="9" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="144" cy="191" r="9" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="176" y1="160" x2="237" y2="160" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M250,160 L236,166.5 L236,153.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="264" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <line x1="72" y1="268" x2="372" y2="268" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="72" y1="258" x2="72" y2="278" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="372" y1="258" x2="372" y2="278" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="168" y="285.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$s = 2{,}00\,\text{m}$</div></foreignObject>
</svg>

### Suunnittelu ennen mittausta
Suunnitelma vastaa ennen mittausta näihin kysymyksiin:
- Mitä mitataan ja millä välineellä?
- Mitkä arvot muutettavalle muuttujalle valitaan, ja kuinka monta?
- Montako toistoa kustakin arvosta tehdään?
- Mitä pidetään vakiona?

Kokeile ensin esikokeella. Esikoe kertoo, onko mittaus ylipäätään mahdollinen. Se antaa myös karkean arvion tuloksesta.

Valitse mittausalue niin, että mitattava suure on selvästi suurempi kuin mittauksen epävarmuus (ks. kohta *Suhteellinen epävarmuus ja mittausalueen valinta*). Valitse useita arvoja ja pidä niiden välit yhtä suurina. Yksi tai kaksi pistettä ei näytä, onko riippuvuus suora.

### Mittauspöytäkirja
**Mittauspöytäkirja** on kirjaus, joka tehdään kokeen aikana. Sitä ei tehdä muistista jälkikäteen. Siihen kirjataan nämä asiat:
- tutkimuskysymys ja päivämäärä
- välineet ja niiden tarkkuus
- vakioidut asiat
- mittaukset taulukkona yksiköineen
- havainnot, esimerkiksi "auto kääntyi sivuun".

Kirjaa lukemat sellaisenaan. Älä poista tai korjaa hiljaa mittausta, joka näyttää oudolta. Merkitse se ja kirjaa, mitä silloin tapahtui. Lyhyt esimerkki:

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

Johtopäätös on vain niin vahva kuin aineisto. Jos mittaukset osuvat epävarmuuden sisällä ennusteeseen, hypoteesi on saanut tukea. Sitä ei silti ole todistettu.

## Kaava: Suhteellinen epävarmuus ja mittausalueen valinta
Käsin mitatun ajan epävarmuus $\Delta t$ johtuu pääosin reaktioajasta. Se on lähes sama lyhyessä ja pitkässä mittauksessa. Siksi mittauksen laatua kuvaa **suhteellinen epävarmuus**. Se tarkoittaa epävarmuutta suhteessa mitattuun arvoon. Suhteellinen epävarmuus saa olla enintään $\varepsilon_\text{max}$. Silloin mitattavan ajan pitää olla vähintään
```latex
\begin{aligned}
\varepsilon &= \frac{\Delta t}{t} \\
t &\ge \frac{\Delta t}{\varepsilon_\text{max}}
\end{aligned}
```
missä $\varepsilon$ on suhteellinen epävarmuus (ilmoitetaan usein prosentteina), $\Delta t$ ajan epävarmuus (s) ja $t$ mitattu aika (s). Esimerkki: epävarmuus on $\Delta t = 0{,}2\,\text{s}$ ja raja on $5\,\%$. Silloin aikaa pitää olla vähintään $4\,\text{s}$.

<svg data-fig="epavarmuus" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja näyttää suhteellisen epävarmuuden ajan funktiona. Ajan epävarmuus on 0,2 s. Kun aika on 1 s, epävarmuus on 20 %. Kun aika on 4 s, epävarmuus on 5,0 %. Kun aika on 10 s, epävarmuus on 2,0 %. Vihreä alue näyttää mittaukset, joiden epävarmuus on enintään 5,0 %. Ne vaativat vähintään 4 s:n ajan. Kuvaaja on mittakaavassa." style="max-width:100%;font-size:24px">
  <line x1="176" y1="286" x2="176" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="256" y1="286" x2="256" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="336" y1="286" x2="336" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="416" y1="286" x2="416" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="496" y1="286" x2="496" y2="54" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="237.5" x2="496" y2="237.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="189.5" x2="496" y2="189.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="141" x2="496" y2="141" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="92.5" x2="496" y2="92.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="286" x2="510" y2="286" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M522,286 L509,292 L509,280 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="287" x2="96" y2="40" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,28 L102,41 L90,41 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="176" y1="286" x2="176" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="166" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="256" y1="286" x2="256" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="246" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="336" y1="286" x2="336" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="326" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="416" y1="286" x2="416" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="406" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$8$</div></foreignObject>
  <line x1="496" y1="286" x2="496" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="479.5" y="295.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="237.5" x2="96" y2="237.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="223" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="89" y1="189.5" x2="96" y2="189.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="175" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="141" x2="96" y2="141" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="126.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="89" y1="92.5" x2="96" y2="92.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="78" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <foreignObject x="66" y="291.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="528" y="271.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="86" y="-2.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\varepsilon\ (\%)$</div></foreignObject>
  <polygon points="256,286 496,286 496,237.5 256,237.5" fill="#b2f2bb" fill-opacity="0.7"/>
  <line x1="96" y1="237.5" x2="496" y2="237.5" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <polyline points="136,92.5 139,106 142,118 145,128 148,137.5 151,145.5 154,152.5 157,159 160,165 163,170.5 166,175.5 169,180 172,184 175,188 178,191.5 181,195 184,198 187,201 190,203.5 193,206.5 196,208.5 199,211 202,213 205,215 208,217 211,219 214,220.5 217,222 220,223.5 223,225 226,226.5 229,228 232,229 235,230.5 238,231.5 241,232.5 244,233.5 247,235 250,236 253,236.5 256,237.5 259,238.5 262,239.5 265,240 268,241 271,242 274,242.5 277,243.5 280,244 283,244.5 286,245.5 289,246 292,246.5 295,247 298,247.5 301,248.5 304,249 307,249.5 310,250 313,250.5 316,251 319,251.5 322,252 325,252 328,252.5 331,253 334,253.5 337,254 340,254.5 343,254.5 346,255 349,255.5 352,256 355,256 358,256.5 361,257 364,257 367,257.5 370,258 373,258 376,258.5 379,258.5 382,259 385,259 388,259.5 391,260 394,260 397,260.5 400,260.5 403,261 406,261 409,261.5 412,261.5 415,262 418,262 421,262 424,262.5 427,262.5 430,263 433,263 436,263.5 439,263.5 442,263.5 445,264 448,264 451,264 454,264.5 457,264.5 460,265 463,265 466,265 469,265.5 472,265.5 475,265.5 478,266 481,266 484,266 487,266 490,266.5 493,266.5 496,266.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="256" y1="237.5" x2="256" y2="286" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="237.5" x2="256" y2="237.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="256" cy="237.5" r="6.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="304" y="188.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$\varepsilon \le 5\,\%$</div></foreignObject>
  <foreignObject x="184" y="73.5" width="180" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\varepsilon = \dfrac{0{,}2\,\text{s}}{t}$</div></foreignObject>
</svg>

Tarvittava matka saadaan tasaisen liikkeen mallista $s = vt$. Jos mittaus tehdään usealla matkalla, mittauspisteisiin sovitetaan suora (luku *Graafinen esitys ja suoran sovittaminen*). Aika $t$ on vaaka-akselilla ja matka $s$ pystyakselilla. Silloin suoran kulmakerroin on nopeus $v$. Lyhin kelvollinen matka on se, jolla suhteellinen epävarmuus vielä pysyy valitussa rajassa $\varepsilon_\text{max}$. Lyhyemmällä matkalla suhteellinen epävarmuus ylittää tämän rajan. Silloin tulos on liian epätarkka.

## Esimerkki
Oppilaat tutkivat leluauton liikettä. Esikokeessa auton nopeus on noin $0{,}42\,\text{m/s}$. Aika mitataan käsikellolla. Ajanoton epävarmuus on $\Delta t = 0{,}2\,\text{s}$. Mittauksen suhteellinen epävarmuus saa olla enintään $5{,}0\,\%$. Kuinka pitkä matka auton pitää vähintään kulkea?

<!-- vaihe -->

**Tunnetut ja kysytty.** Nopeus $v = 0{,}42\,\text{m/s}$, ajan epävarmuus $\Delta t = 0{,}2\,\text{s}$ ja suurin sallittu suhteellinen epävarmuus $\varepsilon_\text{max} = 5{,}0\,\% = 0{,}050$. Kysytään lyhintä matkaa $s_\text{min}$.

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

**Tulos.** Matkan pitää olla vähintään $1{,}7\,\text{m}$. Tulos pyöristetään kahteen merkitsevään numeroon, kuten nopeus $0{,}42\,\text{m/s}$. Epävarmuus $0{,}2\,\text{s}$ on annettu yhdellä numerolla. Siksi se antaa vain arvion lyhimmästä ajasta.

<!-- vaihe -->

**Järkevyys.** Matkalla $1{,}7\,\text{m}$ auton kulkuaika on noin $1{,}7\,\text{m} : 0{,}42\,\text{m/s} \approx 4{,}05\,\text{s}$. Silloin $\varepsilon = 0{,}2\,\text{s} : 4{,}05\,\text{s} \approx 4{,}9\,\%$ eli tasan rajan sisällä. Matkalla $0{,}50\,\text{m}$ aika olisi vain $1{,}2\,\text{s}$ ja epävarmuus noin $17\,\%$. Siksi lyhyt matka oli huono valinta.

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
