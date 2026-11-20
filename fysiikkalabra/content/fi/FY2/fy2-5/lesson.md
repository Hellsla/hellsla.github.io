# Polttoaineet ja lämpöarvo $E = Hm$

> **Miksi** kilogrammasta bensiiniä ja kilogrammasta ilmakuivaa polttopuuta vapautuu palaessa eri määrä energiaa, vaikka molemmat ovat vain palavaa ainetta?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: kaksi samanlaista vaakaa, joiden lukemat ovat samat. Vasemmalla vaa&#x27;alla bensiinikanisteri, oikealla halkoja. Kummankin vieressä palaa tulimaljassa sama aine: bensiinin liekki on selvästi suurempi kuin puun." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-5-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Tässä luvussa polttoaine tarkoittaa kemiallista polttoainetta: ainetta, jonka kemiallista energiaa vapautetaan polttamalla. Myös ydinvoimalan uraania sanotaan polttoaineeksi, mutta ydinpolttoaine ei pala: sen energia on ydinenergiaa (luku *Energialajit ja energian säilyminen*). Kemiallinen energia on energiaa, joka on varastoituna aineen atomien ja molekyylien väliseen rakenteeseen. Kun polttoaine palaa, rakenne muuttuu ja energiaa vapautuu lämpönä ja valona. Energiaa ei synny tyhjästä, vaan kemiallinen energia muuntuu toiseen muotoon. Sama pätee ruokaan: elimistö "polttaa" ravinnon hitaasti ja vapauttaa siitä energiaa.

<svg data-fig="energia" viewBox="0 0 600 330" role="img" aria-label="Vertailukuva, energiat mittakaavassa: kilogramma ilmakuivaa polttopuuta ja kilogramma bensiiniä. Kummankin vieressä on palamisessa vapautuva energia vaakapalkkina samalla asteikolla: polttopuusta 15 megajoulea, bensiinistä 43 megajoulea. Sama massa, eri energia: ero on polttoaineen lämpöarvossa. Vapautuva energia saadaan kertomalla polttoaineen massa lämpöarvolla." style="max-width:100%;font-size:24px">
  <foreignObject x="20" y="11.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{sama massa}$</div></foreignObject>
  <foreignObject x="264" y="11.5" width="330" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{palaessa vapautuva energia}$</div></foreignObject>
  <line x1="286" y1="50" x2="286" y2="262" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="266" y="263.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
  <line x1="350" y1="50" x2="350" y2="262" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="330" y="263.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10$</div></foreignObject>
  <line x1="414" y1="50" x2="414" y2="262" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="394" y="263.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$20$</div></foreignObject>
  <line x1="478" y1="50" x2="478" y2="262" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="458" y="263.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$30$</div></foreignObject>
  <line x1="542" y1="50" x2="542" y2="262" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="522" y="263.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$40$</div></foreignObject>
  <foreignObject x="471" y="291.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$E\ (\text{MJ})$</div></foreignObject>
  <ellipse cx="32" cy="118" rx="6" ry="14" fill="#e9c98a" stroke="#1f2933" stroke-width="1.75"/>
  <rect x="32" y="104" width="44" height="28" fill="#ffffff" stroke="#1f2933" stroke-width="1.75"/>
  <rect x="40" y="104" width="9" height="3" fill="#1f2933"/>
  <rect x="58" y="118" width="9" height="3" fill="#1f2933"/>
  <ellipse cx="76" cy="118" rx="6" ry="14" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.75"/>
  <ellipse cx="80" cy="118" rx="6" ry="14" fill="#e9c98a" stroke="#1f2933" stroke-width="1.75"/>
  <rect x="80" y="104" width="44" height="28" fill="#ffffff" stroke="#1f2933" stroke-width="1.75"/>
  <rect x="88" y="104" width="9" height="3" fill="#1f2933"/>
  <rect x="106" y="118" width="9" height="3" fill="#1f2933"/>
  <ellipse cx="124" cy="118" rx="6" ry="14" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.75"/>
  <ellipse cx="56" cy="88" rx="6" ry="14" fill="#e9c98a" stroke="#1f2933" stroke-width="1.75"/>
  <rect x="56" y="74" width="44" height="28" fill="#ffffff" stroke="#1f2933" stroke-width="1.75"/>
  <rect x="64" y="74" width="9" height="3" fill="#1f2933"/>
  <rect x="82" y="88" width="9" height="3" fill="#1f2933"/>
  <ellipse cx="100" cy="88" rx="6" ry="14" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.75"/>
  <foreignObject x="138" y="79.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{polttopuu}$</div></foreignObject>
  <foreignObject x="138" y="109.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 1\,\text{kg}$</div></foreignObject>
  <rect x="286" y="86" width="96" height="44" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="2"/>
  <foreignObject x="394" y="93.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$15\,\text{MJ}$</div></foreignObject>
  <path d="M44,238 V190 L58,176 H112 V238 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="1.75" stroke-linejoin="round"/>
  <rect x="74" y="179" width="28" height="8" rx="3" fill="#1f2933"/>
  <path d="M49,190 L37,168 L45,164 L56,184" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.75" stroke-linejoin="round"/>
  <path d="M56,200 L100,228 M100,200 L56,228" fill="none" stroke="#c92a2a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="138" y="179.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{bensiini}$</div></foreignObject>
  <foreignObject x="138" y="209.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$m = 1\,\text{kg}$</div></foreignObject>
  <rect x="286" y="186" width="275" height="44" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="2"/>
  <foreignObject x="449" y="193.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$43\,\text{MJ}$</div></foreignObject>
  <line x1="286" y1="48" x2="286" y2="264" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="41" y="291.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E = Hm$</div></foreignObject>
</svg>

Eri polttoaineet sisältävät massaansa nähden eri määrän kemiallista energiaa. Suure, joka kertoo tämän, on lämpöarvo $H$. Se on polttoaineen palaessa vapautuva energia yhtä kilogrammaa kohti, ja sen yksikkö on esimerkiksi $\text{MJ/kg}$. Bensiinin lämpöarvo on noin $43\,\text{MJ/kg}$ eli yhdestä kilogrammasta vapautuu noin $43\,\text{MJ}$ (noin $43 \cdot 10^{6}\,\text{J}$). Ilmakuivan polttopuun (kosteus $20\text{–}25\,\%$) lämpöarvo on vain noin $15\,\text{MJ/kg}$, joten saman energian saamiseksi puuta tarvitaan lähes kolminkertainen massa.

<figure class="unit-photo"><img src="pics/fy2/fireplace-wood-burning.webp" alt="Takassa palaa halkoja kirkkain liekein, ja niiden alla hehkuu hiillos."><figcaption>Puun palaessa sen kemiallinen energia vapautuu lämpönä ja valona.</figcaption></figure>

```pysahdy
Takassa tarvitaan puusta $43\,\text{MJ}$ energiaa. Puun lämpöarvo on $15\,\text{MJ/kg}$. Onko puuta poltettava enemmän vai vähemmän kuin $1{,}0\,\text{kg}$?
---
Enemmän: yhdestä kilogrammasta vapautuu vain $15\,\text{MJ}$, joten tarvitaan noin $2{,}9\,\text{kg}$.
```

Koska lämpöarvo on energia massayksikköä kohti, vapautuva energia on suoraan verrannollinen palaneen polttoaineen massaan: kaksi kertaa enemmän polttoainetta vapauttaa kaksi kertaa enemmän energiaa. Tästä saadaan laki, jolla vapautuva energia lasketaan.

<figure class="unit-photo"><img src="pics/fy2/garzweiler-excavator.webp" alt="Valtava teräsristikkoinen kaivinkone laajalla, hiekanvärisellä avolouhoksella pilvisenä päivänä."><figcaption>Kauhapyöräkaivinkone Garzweilerin avolouhoksella Saksassa. Kaivoksesta louhitaan ruskohiiltä, joka on kosteaa ja jonka lämpöarvo on pieni.</figcaption></figure>

## Kaava: Lämpöarvo ja vapautuva energia
Polttoaineesta palaessaan vapautuva energia on
```kaavat
palamisessa vapautuva lämpö :: E = Hm
```
missä $E$ on vapautuva energia ($\text{J}$ tai $\text{MJ}$), $H$ polttoaineen lämpöarvo ($\text{MJ/kg}$) ja $m$ palaneen polttoaineen massa ($\text{kg}$). Massa on laskettava kilogrammoina, koska lämpöarvo on energia kilogrammaa kohti. Esimerkiksi $3{,}0\,\text{kg}$ bensiiniä vapauttaa $43\,\tfrac{\text{MJ}}{\text{kg}} \cdot 3{,}0\,\text{kg} = 129\,\text{MJ} \approx 130\,\text{MJ}$, koska massa tunnetaan kahden numeron tarkkuudella.

Taulukossa on yleisten polttoaineiden lämpöarvoja. Ne ovat tehollisia lämpöarvoja eli lämpöarvoja, joissa savukaasun vesihöyryn tiivistymislämpöä ei lasketa mukaan, ja energiatilastot käyttävät niitä. Arvot on pyöristetty: todellinen arvo vaihtelee polttoaine-erän mukaan.

| Polttoaine | $H\ (\text{MJ/kg})$ |
| --- | --- |
| maakaasu | 48 |
| bensiini | 43 |
| diesel | 43 |
| kivihiili | 26 |
| puupelletti | 17 |
| polttopuu (ilmakuiva) | 15 |
| turve (jyrsinturve) | 10 |

Lähteet: polttopuu ($13\text{–}15\,\text{GJ/t}$, kosteus $20\text{–}25\,\%$) ja jyrsinturve ($9\text{–}11\,\text{GJ/t}$, kosteus $40\text{–}50\,\%$): Tilastokeskus, *Polttoaineluokitus, määritelmät* (2017). Maakaasu $48{,}0\,\text{MJ/kg}$: IPCC, *2006 Guidelines for National Greenhouse Gas Inventories*, osa 2, oletuslämpöarvojen taulukko (2006). Tyypillisiä arvoja: kivihiili (IPCC 2006: $25{,}8\,\text{MJ/kg}$), diesel (IPCC 2006: $43{,}0\,\text{MJ/kg}$), bensiini ($43\,\text{MJ/kg}$; puhtaan bensiinin IPCC 2006 -arvo on $44{,}3\,\text{MJ/kg}$, mutta suomalaisessa bensiinissä on etanolia, jonka lämpöarvo on pienempi) ja puupelletti (julkaistu tyypillinen arvo). Arvot on pyöristetty.

<svg data-fig="lampoarvot" viewBox="0 0 600 372" role="img" aria-label="Vaakapylväskaavio polttoaineiden lämpöarvoista yksikössä MJ/kg, pyöristettyjä arvoja: maakaasu 48, bensiini 43, diesel 43, kivihiili 26, puupelletti 17, polttopuu (ilmakuiva) 15 ja turve 10. Pylväiden pituudet ovat mittakaavassa: maakaasun pylväs on noin viisi kertaa turpeen pylvään pituinen." style="max-width:100%;font-size:24px">
  <foreignObject x="150" y="9.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$H\ \left(\text{MJ/kg}\right)$</div></foreignObject>
  <line x1="224" y1="48" x2="224" y2="320" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="292" y1="48" x2="292" y2="320" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="48" x2="360" y2="320" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="428" y1="48" x2="428" y2="320" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="496" y1="48" x2="496" y2="320" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="156" y="52" width="326.5" height="26" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="4" y="50.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{maakaasu}$</div></foreignObject>
  <foreignObject x="492.5" y="50.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$48$</div></foreignObject>
  <rect x="156" y="90" width="292.5" height="26" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="4" y="88.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{bensiini}$</div></foreignObject>
  <foreignObject x="458.5" y="88.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$43$</div></foreignObject>
  <rect x="156" y="128" width="292.5" height="26" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="4" y="126.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{diesel}$</div></foreignObject>
  <foreignObject x="458.5" y="126.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$43$</div></foreignObject>
  <rect x="156" y="166" width="177" height="26" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="4" y="164.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{kivihiili}$</div></foreignObject>
  <foreignObject x="343" y="164.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$26$</div></foreignObject>
  <rect x="156" y="204" width="115.5" height="26" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="4" y="202.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{puupelletti}$</div></foreignObject>
  <foreignObject x="281.5" y="202.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$17$</div></foreignObject>
  <rect x="156" y="242" width="102" height="26" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="4" y="240.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{polttopuu}$</div></foreignObject>
  <foreignObject x="268" y="240.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$15$</div></foreignObject>
  <rect x="156" y="280" width="68" height="26" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="4" y="278.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{turve}$</div></foreignObject>
  <foreignObject x="234" y="278.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="156" y1="320" x2="514" y2="320" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,320 L513,326 L513,314 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="156" y1="44" x2="156" y2="322" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="224" y1="320" x2="224" y2="327" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="204" y="331.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10$</div></foreignObject>
  <line x1="292" y1="320" x2="292" y2="327" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="272" y="331.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$20$</div></foreignObject>
  <line x1="360" y1="320" x2="360" y2="327" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="340" y="331.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$30$</div></foreignObject>
  <line x1="428" y1="320" x2="428" y2="327" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="408" y="331.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$40$</div></foreignObject>
  <line x1="496" y1="320" x2="496" y2="327" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="476" y="331.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$50$</div></foreignObject>
  <foreignObject x="116" y="327.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
</svg>

```pysahdy
Poltetaan $250\,\text{g}$ puupellettiä. Kuinka paljon energiaa vapautuu? Käytä taulukon arvoa.
---
Massa kilogrammoina on $0{,}250\,\text{kg}$, koska lämpöarvo on energiaa kilogrammaa kohti. Silloin $E = Hm = 17\,\text{MJ/kg}\cdot0{,}250\,\text{kg}$ eli noin $4{,}3\,\text{MJ}$.
```

### Kosteus ja polttoaineen laatu
Märkä puu antaa kilogrammaa kohti vähemmän energiaa kuin kuiva, koska osa sen massasta on vettä, joka ei pala, ja lisäksi osa vapautuvasta energiasta kuluu tämän veden höyrystämiseen. Siksi taulukon polttopuu on ilmakuivaa (kosteus $20\text{–}25\,\%$) ja turve jyrsinturvetta, jonka kosteus on $40\text{–}50\,\%$. Kuivemmasta puusta saa enemmän: MAFY-taulukossa kuivan puun lämpöarvo on $16{,}2\,\text{MJ/kg}$.

```pysahdy
Kaksi polttopuukiloa on yhtä suuria, mutta toinen on kuivaa ja toinen märkää. Kummasta vapautuu enemmän energiaa ja miksi?
---
Kuivasta. Märässä puussa osa massasta on vettä, joka ei pala, ja osa energiasta kuluu veden höyrystämiseen.
```

### Ruoan energiasisältö ja lämpöarvo
Ravintoarvomerkinnässä energia ilmoitetaan sadalle grammalle, esimerkiksi $2200\,\text{kJ}$ per $100\,\text{g}$. Kun energia muutetaan megajouleiksi ja massa kilogrammoiksi, saadaan ruoan energiasisältö massayksikköä kohti, tässä $e = 22\,\text{MJ/kg}$. Sekä ruoan energiasisältö että polttoaineen lämpöarvo voidaan ilmoittaa yksikössä $\text{MJ/kg}$. Ruoan ravintoarvomerkintä kuvaa elimistön hyödynnettävissä olevaa energiaa, kun taas polttoaineen lämpöarvo kuvaa palamisessa vapautuvaa energiaa. Ne eivät siis ole sama suure: elimistö ei saa ruoasta kaikkea energiaa, joka vapautuisi sen palaessa, koska esimerkiksi osa ruoasta ei imeydy suolistosta. Laskutapa on silti sama kuin lämpöarvolla: ruoan energia on $E = em$.

<svg data-fig="etiketti" viewBox="0 0 600 300" role="img" aria-label="Periaatekuva ravintoarvomerkinnästä, esimerkki eikä todellinen tuote: pakkauksessa lukee energia 2200 kJ sadassa grammassa. Kun energia muutetaan megajouleiksi ja massa kilogrammoiksi, saadaan ruoan energiasisältö 22 MJ/kg." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy25-heat" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient><linearGradient id="fy25-heatv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <rect x="30" y="30" width="230" height="220" rx="8" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="45" y="51.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{Ravintoarvo}$</div></foreignObject>
  <line x1="46" y1="92" x2="244" y2="92" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="40" y="109.5" width="210" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{sadassa grammassa}$</div></foreignObject>
  <line x1="46" y1="152" x2="244" y2="152" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="46" y="173.5" width="96" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
  <foreignObject x="150" y="173.5" width="94" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2200\,\text{kJ}$</div></foreignObject>
  <line x1="46" y1="214" x2="244" y2="214" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="80" y="217.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{esimerkki}$</div></foreignObject>
  <path d="M280,147 L318,147 L318,155 L340,140 L318,125 L318,133 L280,133 Z" fill="url(#fy25-heat)" stroke-linejoin="round"/>
  <foreignObject x="350" y="81.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2200\,\text{kJ} = 2{,}2\,\text{MJ}$</div></foreignObject>
  <foreignObject x="350" y="125.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$100\,\text{g} = 0{,}100\,\text{kg}$</div></foreignObject>
  <foreignObject x="350" y="175" width="200" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$e = 22\,\dfrac{\text{MJ}}{\text{kg}}$</div></foreignObject>
</svg>

| Ruoka | $\text{kJ}$ / $100\,\text{g}$ | $e$ ($\text{MJ/kg}$) |
| --- | --- | --- |
| peruna, keitetty | 300 | 3 |
| ruisleipä | 1000 | 10 |
| maitosuklaa | 2200 | 22 |
| voi | 3000 | 30 |

Tyypillisiä ravintoarvoja (vertailukohta Fineli, THL), pyöristetty ja vaihtelee tuotteittain.

## Esimerkki
Takassa poltetaan $6{,}0\,\text{kg}$ ilmakuivaa polttopuuta, jonka lämpöarvo on $15\,\tfrac{\text{MJ}}{\text{kg}}$. Kuinka paljon energiaa puusta vapautuu? Anna vastaus megajouleina ja kilowattitunteina.

<!-- vaihe -->

**Tunnetut ja kysytty.** Polttopuun massa $m = 6{,}0\,\text{kg}$ ja taulukosta lämpöarvo $H = 15\,\tfrac{\text{MJ}}{\text{kg}}$.

Kysytään vapautuvaa energiaa $E$.

<!-- vaihe -->

**Periaate.** Puu palaa, joten sen kemiallinen energia muuntuu lämmöksi. Lämpöarvo kertoo energian yhtä kilogrammaa kohti, joten vapautuva energia saadaan kertomalla lämpöarvo massalla.

<!-- vaihe -->

**Kaava ratkaistuna.** Kysytty suure $E$ on jo yhtälön vasemmalla puolella:
```latex
E = Hm
```

<!-- vaihe -->

**Yksikkömuunnokset.** Massa on jo kilogrammoina, joten megajoulet voi laskea suoraan. Kilowattitunteja varten käytetään yhteyttä $1\,\text{kWh} = 3{,}6\,\text{MJ}$, josta $1\,\text{MJ} = 1\,\text{kWh} : 3{,}6$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
E &= Hm \\
&= 15\,\tfrac{\text{MJ}}{\text{kg}} \cdot 6{,}0\,\text{kg} \\
&= 90\,\text{MJ}
\end{aligned}
```
Kilowattitunteina $E = 90\,\text{MJ} = 90 \cdot (1\,\text{kWh} : 3{,}6) = 25\,\text{kWh}$.

<!-- vaihe -->

**Tulos.** Puusta vapautuu energiaa $90\,\text{MJ}$ eli $25\,\text{kWh}$.

Vastaus on annettu kahdella merkitsevällä numerolla, koska sekä massa $6{,}0\,\text{kg}$ että lämpöarvo $15\,\tfrac{\text{MJ}}{\text{kg}}$ tunnetaan kahden numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Yksi kilogramma puuta antaa $15\,\text{MJ}$ eli noin $4\,\text{kWh}$, joten kuusi kilogrammaa antaa noin kuusi kertaa niin paljon: $6 \cdot 4\,\text{kWh} = 24\,\text{kWh}$, mikä sopii tulokseen.

Energia vastaa yhden kilowatin ($1\,\text{kW}$) lämmitintä, joka on päällä $25\,\text{h}$.

Takasta ei kuitenkaan saada koko määrää huoneen lämmöksi, koska osa lämmöstä poistuu savukaasujen mukana (luku *Hyötysuhde*).

## Yleinen virhekäsitys
- **Lämpöarvo ei ole lämpötila.** Moni luulee, että lämpöarvo kertoo, kuinka kuumana polttoaine palaa. Se on kuitenkin energia massayksikköä kohti.
- **Palaessa ei synny energiaa.** Polttoaineen kemiallinen energia muuntuu lämmöksi ja valoksi, mutta energiaa ei synny tyhjästä.
- **Vapautunut energia ei ole hyötyenergia.** Kattilassa, takassa ja moottorissa osa energiasta menee hukkaan, ja hyödyn osuus lasketaan hyötysuhteella (luku *Hyötysuhde*).

Hiiltä sisältävien polttoaineiden, kuten puun, turpeen ja fossiilisten polttoaineiden, palamisessa syntyy myös hiilidioksidia, jota käsitellään luvussa *Energiantuotanto, ympäristö ja ilmastonmuutos*.

## Tiivistelmä
- Polttoaineen kemiallinen energia vapautuu palaessa lämpönä ja valona. Energia ei synny vaan muuntuu.
- Lämpöarvo $H$ on vapautuva energia yhtä kilogrammaa polttoainetta kohti, yksikkö $\text{MJ/kg}$.
- Vapautuva energia on $E = Hm$, kun massa $m$ on kilogrammoina.
- Bensiinin ja dieselin lämpöarvo on noin $43\,\text{MJ/kg}$, kivihiilen $26$, ilmakuivan puun $15$ ja turpeen $10\,\text{MJ/kg}$.
- Ruoan pakkausmerkinnän $\text{kJ}$ per $100\,\text{g}$ voidaan muuttaa yksikköön $\text{MJ/kg}$ kuten lämpöarvo, mutta se kuvaa elimistön hyödynnettävissä olevaa energiaa, ei palamisessa vapautuvaa energiaa.
- Vapautunut energia ei ole sama kuin hyöty: hyötyenergia saadaan hyötysuhteella.
