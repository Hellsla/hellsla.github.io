# Energialajit ja energian säilyminen

> **Miksi** pomppiva pallo pysähtyy lopulta lattialle?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: pallo pomppii liikuntasalin puulattialla vasemmalta oikealle. Katkoviivalla piirretyt kaaret ovat jokaisen pompun jälkeen matalampia. Lopussa pallo on paikallaan lattialla. Jokaisessa kohdassa, jossa pallo osuu lattiaan, on pieni lämpöväre." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-1-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
**Energia** on suure. Sen avulla kerrotaan, mitä systeemissä (tarkasteltavassa kokonaisuudessa) tapahtuu, kun jokin liikkuu, lämpenee, loistaa tai muuttaa muotoaan. Energian tunnus on $E$ ja yksikkö on **joule**, $\text{J}$. Joule on pieni yksikkö. Siksi energia ilmoitetaan usein myös kilojouleina. Etuliite kilo tarkoittaa tuhatta, joten $1\,\text{kJ} = 1000\,\text{J}$.

Energiaa on monessa muodossa. Jokaista muotoa sanotaan **energialajiksi**. Energialaji kertoo, mihin energia on sitoutunut eli varastoitunut tai miten se näkyy. Esimerkiksi liikkuvan pallon energia näkyy liikkeenä, ja pariston energia on varastoitunut sen aineisiin.

<figure class="unit-photo"><img src="pics/fy2/hydropower-plant-aerial.webp" alt="Vesivoimalaitoksen alue ylhäältä. Vasemmalla on joki ja alhaalla sähkölaitteita."><figcaption>Vesivoimalaitos ylhäältä. Veden potentiaalienergia muuttuu turbiinissa liike-energiaksi. Generaattori muuttaa sen sähköenergiaksi.</figcaption></figure>

### Seitsemän energialajia
| Energialaji | Mihin liittyy | Esimerkki |
|---|---|---|
| **Potentiaalienergia** $E_\text{p}$ | Kappaleen paikkaan. Tässä se on painovoiman potentiaalienergiaa. Mitä korkeammalla kappale on ja mitä suurempi sen massa on, sitä enemmän sillä on potentiaalienergiaa. | Hyllyn reunalla oleva pallo voi pudotessaan saada vauhtia. |
| **Liike-energia** $E_\text{k}$ | Kappaleen liikkeeseen. Mitä nopeammin kappale liikkuu ja mitä suurempi sen massa on, sitä enemmän sillä on liike-energiaa. Levossa olevalla kappaleella sitä ei ole. | Vierivä pallo |
| **Lämpöenergia** $E_\text{lämpö}$ | Aineen hiukkasten liikkeeseen ja siihen, miten hiukkaset vaikuttavat toisiinsa. Kun kappale lämpenee, sen hiukkaset liikkuvat enemmän. Silloin kappaleen lämpöenergia kasvaa. | Kuuma kahvikuppi |
| **Kemiallinen energia** | Aineiden kemiallisiin sidoksiin. Energia vapautuu esimerkiksi palamisessa ja aineenvaihdunnassa. | Ravinto, polttoaineet ja paristot |
| **Säteilyenergia** | Säteilyyn. Energia kulkee säteilyn mukana. Se kulkee myös tyhjiön läpi. | Auringonvalo |
| **Sähköenergia** | Sähkövirtaan. Energia siirtyy sähkövirran mukana. | Sähköverkko |
| **Ydinenergia** | Atomiytimiin. Energia vapautuu ydinreaktioissa. | Ydinvoimala ja Aurinko |

Lämpöenergia riippuu myös aineen määrästä. Siksi se ei ole sama asia kuin lämpötila. Sana **lämpö** tarkoittaa fysiikassa energiaa, joka *siirtyy* lämpötilaeron vuoksi. Energiaa siirtyy nettomääräisesti lämpimämmästä kappaleesta kylmempään. Kappaleella on lämpöenergiaa. Lämpönä energiaa siirtyy kappaleesta toiseen.

Potentiaalienergia ja liike-energia yhdessä ovat **mekaaninen energia**, $E_\text{mek} = E_\text{p} + E_\text{k}$.

```pysahdy
Kuuma kahvikuppi jäähtyy pöydällä. Mitä fysiikan sana lämpö tarkoittaa tässä tilanteessa?
---
Lämpö on energiaa, joka siirtyy kupista viileämpään ilmaan. Syynä on lämpötilaero eli se, että kuppi on lämpimämpi kuin ilma. Kupin lämpöenergia pienenee.
```

<svg data-fig="energialajit" viewBox="0 0 600 396" role="img" aria-label="Kaavakuva: energialajit ja esimerkki jokaisesta. Mekaaninen energia on potentiaalienergiaa ja liike-energiaa. Potentiaalienergian esimerkki on pallo kallion reunalla. Liike-energian esimerkki on vierivä pallo. Kuvassa ovat myös lämpöenergia (kuuma kahvikuppi), kemiallinen energia (paristo), säteilyenergia (Aurinko), sähköenergia (salama) ja ydinenergia (atomiydin). Kuva on kaavamainen. Se ei ole mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-1-energialajit.webp" x="0" y="-1.2" width="600" height="401.2" preserveAspectRatio="none"/>
  <foreignObject x="40" y="5.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{mekaaninen energia}$</div></foreignObject>
  <foreignObject x="99" y="67.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h$</div></foreignObject>
  <foreignObject x="243" y="47.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$v$</div></foreignObject>
  <foreignObject x="-4" y="155.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{potentiaali-}$</div></foreignObject>
  <foreignObject x="27.5" y="185.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
  <foreignObject x="183.5" y="155.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{liike-}$</div></foreignObject>
  <foreignObject x="177.5" y="185.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
  <foreignObject x="333.5" y="155.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpö-}$</div></foreignObject>
  <foreignObject x="327.5" y="185.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
  <foreignObject x="452.5" y="155.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kemiallinen}$</div></foreignObject>
  <foreignObject x="477.5" y="185.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
  <foreignObject x="96" y="327.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{säteily-}$</div></foreignObject>
  <foreignObject x="102.5" y="357.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
  <foreignObject x="258.5" y="327.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sähkö-}$</div></foreignObject>
  <foreignObject x="252.5" y="357.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
  <foreignObject x="415" y="327.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ydin-}$</div></foreignObject>
  <foreignObject x="402.5" y="357.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
</svg>

### Energia muuttaa muotoa
Energia ei pysy samassa muodossa. Taskulampussa pariston kemiallinen energia muuttuu sähköenergiaksi. Lamppu muuttaa sähköenergian valoksi ja lämpöenergiaksi. Hehkulampussa suurin osa energiasta muuttuu lämpöenergiaksi. Vain pieni osa muuttuu valoksi.

<svg data-fig="energian-muuttuminen" viewBox="0 0 600 250" role="img" aria-label="Kaavakuva: energian muuttuminen taskulampussa. Paristossa on kemiallista energiaa. Se muuttuu sähköenergiaksi. Lamppu muuttaa sähköenergian valoksi ja lämpöenergiaksi. Suurin osa muuttuu lämpöenergiaksi, joten lämpöenergian nuoli on leveämpi. Kuva on kaavamainen. Nuolten leveys ei ole mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-1-energian-muuttuminen.webp" x="0" y="0" width="600" height="258.8" preserveAspectRatio="none"/>
  <foreignObject x="7.5" y="11.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kemiallinen}$</div></foreignObject>
  <foreignObject x="32.5" y="41.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
  <foreignObject x="32.5" y="183.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{paristo}$</div></foreignObject>
  <foreignObject x="163.5" y="11.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sähkö-}$</div></foreignObject>
  <foreignObject x="157.5" y="41.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
  <foreignObject x="280.5" y="183.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lamppu}$</div></foreignObject>
  <foreignObject x="444" y="62.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{valo}$</div></foreignObject>
  <foreignObject x="444" y="139.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lämpö-}$</div></foreignObject>
  <foreignObject x="444" y="169.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
</svg>

Samanlaisia muutoksia on kaikkialla. Kasvi muuttaa auringon säteilyenergiaa kemialliseksi energiaksi. Lihas muuttaa kemiallista energiaa liike-energiaksi ja lämpöenergiaksi. Ydinvoimalassa ydinenergia muuttuu lopulta sähköenergiaksi.

## Kaava: Energian säilymislaki
Kaikissa näissä muutoksissa energian kokonaismäärä pysyy samana. Energiaa ei synny eikä katoa. Se muuttaa muotoa tai siirtyy paikasta toiseen. Tämä on fysiikan yleinen periaate, **energian säilymislaki**. Tarkastellaan **eristettyä systeemiä**. Siihen ei tule energiaa ulkopuolelta, eikä siitä lähde energiaa pois. Silloin systeemin kokonaisenergia on sama alussa ja lopussa:

```latex
E_\text{alussa} = E_\text{lopussa}
```

Tässä $E_\text{alussa}$ on systeemin kaikkien energialajien energioiden summa alussa. Lopussa vastaava summa on $E_\text{lopussa}$. Molemmat ilmoitetaan jouleina ($\text{J}$).

Summaan kuuluvat kaikki energialajit, myös lämpöenergia. Skeittari liukuu half-pipen reunalta pohjalle, ja kitka vaikuttaa. Silloin mekaaninen energia $E_\text{p} + E_\text{k}$ pienenee. Lämpöenergia $E_\text{lämpö}$ kasvaa saman verran. Summa $E_\text{p} + E_\text{k} + E_\text{lämpö}$ ei muutu. Kitka ei siis luo energiaa. Se muuttaa mekaanista energiaa lämpöenergiaksi. Renkaat, ramppi ja ilma lämpenevät hieman.

```pysahdy
Skeittarin mekaaninen energia pienenee kitkan takia $50\,\text{J}$. Mitä tapahtuu lämpöenergialle, jos systeemi on eristetty? Eristetty tarkoittaa, että energiaa ei tule ulkopuolelta eikä lähde pois.
---
Lämpöenergia kasvaa $50\,\text{J}$. Kokonaisenergia pysyy samana, koska energiaa ei synny eikä katoa.
```

<svg data-fig="sailyminen" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva: skeittari half-pipessä kolmella hetkellä. Jokaisen hetken energiat näkyvät pylväinä. Alussa skeittari on levossa reunalla. Silloin koko energia 800 J on potentiaalienergiaa. Välillä potentiaalienergiaa on 300 J, liike-energiaa 450 J ja lämpöenergiaa 50 J. Pohjalla potentiaalienergiaa ei ole. Liike-energiaa on 700 J ja lämpöenergiaa 100 J. Pylväiden korkeus on mittakaavassa. Jokaisen pylvään kokonaiskorkeus vastaa 800 joulea. Kaikilla hetkillä energiaa on siis yhtä paljon." style="max-width:100%;font-size:24px">
  <defs><pattern id="fy21-hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="#c92a2a"/><line x1="0" y1="0" x2="0" y2="8" stroke="#f2a69c" stroke-width="3"/></pattern></defs>
  <path d="M10,38 L20,38 Q100,146 180,38 L190,38 L190,106 L10,106 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <path d="M10,38 L20,38 Q100,146 180,38 L190,38" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M210,38 L220,38 Q300,146 380,38 L390,38 L390,106 L210,106 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <path d="M210,38 L220,38 Q300,146 380,38 L390,38" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M410,38 L420,38 Q500,146 580,38 L590,38 L590,106 L410,106 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <path d="M410,38 L420,38 Q500,146 580,38 L590,38" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <g transform="translate(20,37) rotate(53.5) scale(0.66)" stroke-linecap="round" stroke-linejoin="round"><rect x="-17" y="-9" width="34" height="4.2" rx="2.1" fill="#d9b26a" stroke="#a97a35" stroke-width="1.5"/><circle cx="-10" cy="-3.4" r="3.4" fill="#1f2933"/><circle cx="10" cy="-3.4" r="3.4" fill="#1f2933"/><path d="M-8,-9.5 L-4,-19 L1,-28 M9,-9.5 L7,-19 L1,-28" fill="none" stroke="#6c757d" stroke-width="4.4"/><path d="M1,-28 L4,-44" fill="none" stroke="#1971c2" stroke-width="7"/><path d="M4,-41 L-6,-34 M4,-41 L14,-36" fill="none" stroke="#e9c98a" stroke-width="3.2"/><circle cx="6" cy="-51" r="6.4" fill="#e9c98a"/><path d="M-0.4,-52 A6.4,6.4 0 0 1 12.4,-52 Z" fill="#1f2933"/></g>
  <rect x="45" y="164" width="44" height="128" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="99" y="213.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$800\,\text{J}$</div></foreignObject>
  <g transform="translate(251,71) rotate(39.6) scale(0.66)" stroke-linecap="round" stroke-linejoin="round"><rect x="-17" y="-9" width="34" height="4.2" rx="2.1" fill="#d9b26a" stroke="#a97a35" stroke-width="1.5"/><circle cx="-10" cy="-3.4" r="3.4" fill="#1f2933"/><circle cx="10" cy="-3.4" r="3.4" fill="#1f2933"/><path d="M-8,-9.5 L-4,-19 L1,-28 M9,-9.5 L7,-19 L1,-28" fill="none" stroke="#6c757d" stroke-width="4.4"/><path d="M1,-28 L4,-44" fill="none" stroke="#1971c2" stroke-width="7"/><path d="M4,-41 L-6,-34 M4,-41 L14,-36" fill="none" stroke="#e9c98a" stroke-width="3.2"/><circle cx="6" cy="-51" r="6.4" fill="#e9c98a"/><path d="M-0.4,-52 A6.4,6.4 0 0 1 12.4,-52 Z" fill="#1f2933"/></g>
  <rect x="245" y="284" width="44" height="8" fill="url(#fy21-hatch)" stroke="#1f2933" stroke-width="2"/>
  <rect x="245" y="212" width="44" height="72" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="245" y="164" width="44" height="48" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="299" y="262.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$50\,\text{J}$</div></foreignObject>
  <foreignObject x="299" y="233.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$450\,\text{J}$</div></foreignObject>
  <foreignObject x="299" y="173.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$300\,\text{J}$</div></foreignObject>
  <g transform="translate(500,91) rotate(0.0) scale(0.66)" stroke-linecap="round" stroke-linejoin="round"><rect x="-17" y="-9" width="34" height="4.2" rx="2.1" fill="#d9b26a" stroke="#a97a35" stroke-width="1.5"/><circle cx="-10" cy="-3.4" r="3.4" fill="#1f2933"/><circle cx="10" cy="-3.4" r="3.4" fill="#1f2933"/><path d="M-8,-9.5 L-4,-19 L1,-28 M9,-9.5 L7,-19 L1,-28" fill="none" stroke="#6c757d" stroke-width="4.4"/><path d="M1,-28 L4,-44" fill="none" stroke="#1971c2" stroke-width="7"/><path d="M4,-41 L-6,-34 M4,-41 L14,-36" fill="none" stroke="#e9c98a" stroke-width="3.2"/><circle cx="6" cy="-51" r="6.4" fill="#e9c98a"/><path d="M-0.4,-52 A6.4,6.4 0 0 1 12.4,-52 Z" fill="#1f2933"/></g>
  <rect x="445" y="276" width="44" height="16" fill="url(#fy21-hatch)" stroke="#1f2933" stroke-width="2"/>
  <rect x="445" y="164" width="44" height="112" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="499" y="262.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$100\,\text{J}$</div></foreignObject>
  <foreignObject x="499" y="205.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$700\,\text{J}$</div></foreignObject>
  <foreignObject x="58.5" y="303.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{alussa}$</div></foreignObject>
  <foreignObject x="252.5" y="303.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{välillä}$</div></foreignObject>
  <foreignObject x="452.5" y="303.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lopussa}$</div></foreignObject>
  <line x1="24" y1="164" x2="576" y2="164" stroke="#1f2933" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <foreignObject x="158.5" y="129.5" width="283" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kokonaisenergia } E = 800\,\text{J}$</div></foreignObject>
  <line x1="30" y1="292" x2="570" y2="292" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="120" y="348" width="20" height="20" fill="#1971c2" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="150" y="343.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{p}$</div></foreignObject>
  <rect x="270" y="348" width="20" height="20" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="300" y="343.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{k}$</div></foreignObject>
  <rect x="420" y="348" width="20" height="20" fill="url(#fy21-hatch)" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="450" y="343.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E_\text{lämpö}$</div></foreignObject>
</svg>

### Energian kuluttaminen on energian muuttumista
Arkikielessä energiaa "kuluu". Fysiikassa energia ei kuitenkaan lopu. Kun laite kuluttaa energiaa, se muuttaa energiaa muodosta toiseen. Useimmiten suurin osa muuttuu lämpöenergiaksi. Lämpöenergia siirtyy lämpönä ympäristöön, ja sitä on vaikea käyttää enää hyödyksi. Lyhyesti sanotaan usein, että energia "muuttuu lämmöksi". Siksi energiaa kannattaa säästää, vaikka sitä ei voi hävittää.

```pysahdy
Puhelimen akku "tyhjenee", kun käytät puhelinta. Mihin akun energia on mennyt?
---
Se ei ole kadonnut. Energia on muuttunut toiseen muotoon, esimerkiksi valoksi ja lämpöenergiaksi. Suurin osa siirtyy lämpönä ympäristöön.
```

## Esimerkki
Skeittari lähtee levosta half-pipen reunalta. Reunalla hänen potentiaalienergiansa on $840\,\text{J}$, kun nollataso on half-pipen pohja. Pohjalla hänen liike-energiansa on $0{,}72\,\text{kJ}$. Skeittari, half-pipe ja ympäristö muodostavat eristetyn systeemin. Kuinka paljon kitka on muuttanut energiaa lämpöenergiaksi laskun aikana?

<!-- vaihe -->

**Tunnetut ja kysytty.** Alussa potentiaalienergia on $E_\text{p} = 840\,\text{J}$.

Liike-energia on nolla, koska skeittari on levossa.

Pohjalla potentiaalienergia on nolla ja liike-energia on $E_\text{k} = 0{,}72\,\text{kJ}$.

Kysytään sitä mekaanista energiaa $E_\text{lämpö}$, jonka kitka muuttaa laskun aikana lämpöenergiaksi.

<!-- vaihe -->

**Periaate.** Systeemi on eristetty, joten energia säilyy: $E_\text{alussa} = E_\text{lopussa}$. Alussa kaikki energia on potentiaalienergiaa. Pohjalla energia on jakautunut kahtia. Osa on liike-energiaa ja osa on lämpöenergiaa. Kitka on muuttanut osan energiasta lämpöenergiaksi.

<!-- vaihe -->

**Kaava ratkaistuna.** Alussa on vain $E_\text{p}$. Lopussa on $E_\text{k}$ ja $E_\text{lämpö}$:
```latex
\begin{aligned}
E_\text{alussa} &= E_\text{lopussa} \\
E_\text{p} &= E_\text{k} + E_\text{lämpö} \\
E_\text{lämpö} &= E_\text{p} - E_\text{k}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Liike-energia on annettu kilojouleina ja potentiaalienergia jouleina. Etuliite kilo tarkoittaa tuhatta, joten se sijoitetaan yksikön paikalle: $E_\text{k} = 0{,}72\,\text{kJ} = 0{,}72 \cdot 1000\,\text{J} = 720\,\text{J}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
E_\text{lämpö} &= E_\text{p} - E_\text{k} \\
&= 840\,\text{J} - 720\,\text{J} \\
&= 120\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kitka muutti lämpöenergiaksi $E_\text{lämpö} = 120\,\text{J}$. Tulos pyöristetään kymmeniin jouleihin. Liike-energia $0{,}72\,\text{kJ}$ on annettu kymmenen joulen tarkkuudella, ja se rajoittaa erotuksen tarkkuutta.

<!-- vaihe -->

**Järkevyys.** Lämpöenergia on positiivinen ja pienempi kuin alkuenergia $840\,\text{J}$, kuten kitkan kohdalla pitääkin. Energia on tallessa: $720\,\text{J} + 120\,\text{J} = 840\,\text{J} = E_\text{alussa}$. Lämpöenergiaksi muuttui alle viidesosa alkuenergiasta. Se on uskottava määrä sileässä half-pipessä.

## Yleinen virhekäsitys
Energia ei katoa eikä kulu loppuun. Pallo pysähtyy tai laite kuluttaa energiaa. Silloin energia on muuttunut toiseen muotoon, yleensä lämpöenergiaksi, joka on siirtynyt lämpönä ympäristöön. Toinen virhe on laskea vain mekaaninen energia. Kitkallisessa liikkeessä $E_\text{p} + E_\text{k}$ pienenee. Kokonaisenergia pysyy silti samana, kun lämpöenergia otetaan mukaan. Kitka ei luo energiaa. Se muuttaa energiaa muodosta toiseen.

## Tiivistelmä
- Energian tunnus on $E$ ja yksikkö joule $\text{J}$; $1\,\text{kJ} = 1000\,\text{J}$.
- Energialajeja ovat potentiaalienergia, liike-energia (yhdessä mekaaninen energia), lämpöenergia, kemiallinen energia, säteilyenergia, sähköenergia ja ydinenergia.
- Energia muuttaa muotoa ja siirtyy, mutta se ei synny eikä katoa: eristetyssä systeemissä $E_\text{alussa} = E_\text{lopussa}$.
- Kitka ei luo energiaa vaan muuttaa mekaanista energiaa lämpöenergiaksi: $E_\text{p} + E_\text{k}$ pienenee, mutta kokonaisenergia ei muutu.
- Kappaleella on lämpöenergiaa. Lämpö on energiaa, joka siirtyy lämpötilaeron vuoksi, nettomääräisesti lämpimämmästä kylmempään.
- Energian kuluttaminen tarkoittaa sen muuttumista muotoon, jota on vaikea hyödyntää. Yleensä se on lämpöenergiaa.
