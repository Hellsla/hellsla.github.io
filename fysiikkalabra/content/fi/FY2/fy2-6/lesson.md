# Energiantuotantotavat ja niiden vertailu

> **Miksi** Suomen sähköverkossa toimii yhtä aikaa ydinvoimaa, vesivoimaa, tuulivoimaa ja polttoainevoimaloita, vaikka yksi voimalatyyppi voisi periaatteessa tuottaa kaiken sähkön?

## Ydinajatus
Voimalaitos ei tuota energiaa tyhjästä, vaan muuttaa luonnonvaran energian sähköksi ja usein myös lämmöksi. Putoavan veden ja tuulen liike-energia, auringon säteilyenergia, uraanin ydinenergia ja polttoaineen kemiallinen energia kulkevat turbiinin ja generaattorin tai aurinkopaneelin kautta sähköverkkoon. Energia säilyy, mutta osa siitä päätyy aina lämpönä ympäristöön (luku *Hyötysuhde*).

<svg data-fig="plants" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva: viisi tapaa tuottaa sähköä. Putoava vesi pyörittää turbiinia, tuuli roottoria, auringonsäteily osuu aurinkopaneeliin, ydinpolttoaineen energia lämmittää höyryn höyryturbiinille ja polttoaineen kemiallinen energia lämmittää höyryn höyryturbiinille. Jokaisesta laitoksesta lähtee nuoli sähköverkkoon. Kuva on kaavamainen, nuolten pituus ei kuvaa tehoa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy26-heat" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <rect x="468" y="18" width="116" height="294" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="472" y="150.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sähkö}$</div></foreignObject>
  <rect x="16" y="18" width="196" height="54" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="20" y="30.5" width="188" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{putoava vesi}$</div></foreignObject>
  <path d="M214,51 L232,51 L232,58 L250,45 L232,32 L232,39 L214,39 Z" fill="url(#fy26-heat)" stroke-linejoin="round"/>
  <rect x="252" y="18" width="176" height="54" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="256" y="30.5" width="168" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{turbiini}$</div></foreignObject>
  <path d="M430,51 L448,51 L448,58 L466,45 L448,32 L448,39 L430,39 Z" fill="url(#fy26-heat)" stroke-linejoin="round"/>
  <rect x="16" y="78" width="196" height="54" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="20" y="90.5" width="188" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tuuli}$</div></foreignObject>
  <path d="M214,111 L232,111 L232,118 L250,105 L232,92 L232,99 L214,99 Z" fill="url(#fy26-heat)" stroke-linejoin="round"/>
  <rect x="252" y="78" width="176" height="54" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="256" y="90.5" width="168" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{roottori}$</div></foreignObject>
  <path d="M430,111 L448,111 L448,118 L466,105 L448,92 L448,99 L430,99 Z" fill="url(#fy26-heat)" stroke-linejoin="round"/>
  <rect x="16" y="138" width="196" height="54" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="20" y="150.5" width="188" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{säteily}$</div></foreignObject>
  <path d="M214,171 L232,171 L232,178 L250,165 L232,152 L232,159 L214,159 Z" fill="url(#fy26-heat)" stroke-linejoin="round"/>
  <rect x="252" y="138" width="176" height="54" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="256" y="150.5" width="168" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{paneeli}$</div></foreignObject>
  <path d="M430,171 L448,171 L448,178 L466,165 L448,152 L448,159 L430,159 Z" fill="url(#fy26-heat)" stroke-linejoin="round"/>
  <rect x="16" y="198" width="196" height="54" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="20" y="210.5" width="188" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ydinpolttoaine}$</div></foreignObject>
  <path d="M214,231 L232,231 L232,238 L250,225 L232,212 L232,219 L214,219 Z" fill="url(#fy26-heat)" stroke-linejoin="round"/>
  <rect x="252" y="198" width="176" height="54" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="256" y="210.5" width="168" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{höyryturbiini}$</div></foreignObject>
  <path d="M430,231 L448,231 L448,238 L466,225 L448,212 L448,219 L430,219 Z" fill="url(#fy26-heat)" stroke-linejoin="round"/>
  <rect x="16" y="258" width="196" height="54" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="20" y="270.5" width="188" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{polttoaine}$</div></foreignObject>
  <path d="M214,291 L232,291 L232,298 L250,285 L232,272 L232,279 L214,279 Z" fill="url(#fy26-heat)" stroke-linejoin="round"/>
  <rect x="252" y="258" width="176" height="54" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="256" y="270.5" width="168" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{höyryturbiini}$</div></foreignObject>
  <path d="M430,291 L448,291 L448,298 L466,285 L448,272 L448,279 L430,279 Z" fill="url(#fy26-heat)" stroke-linejoin="round"/>
</svg>

### Uusiutuva ja uusiutumaton energia
Vesi, tuuli ja auringonsäteily ovat uusiutuvia: ne eivät lopu käytettäessä. Bioperäiset polttoaineet, kuten puu, ovat uusiutuvia, koska uusi metsä kasvaa tilalle. Kivihiili, öljy, maakaasu ja turve ovat fossiilisia, ja uraanikin on uusiutumaton luonnonvara. Voimaloiden päästöt ja ilmastovaikutukset käsitellään luvussa *Energiantuotanto, ympäristö ja ilmastonmuutos*.

### Kolme ryhmää: miten voimala toimii verkossa
Sähköä ei voi varastoida suuria määriä suoraan verkkoon, joten tuotannon on vastattava kulutusta joka hetki. Siksi voimalat ryhmitellään sen mukaan, kuinka niiden tehoon voi vaikuttaa.

| Ryhmä | Voimalat | Teho |
|---|---|---|
| Sääriippuvainen | tuuli, aurinko | vaihtelee sään mukaan |
| Säädettävä | vesi, polttoaine | säädettävissä |
| Perusvoima | ydinvoima | lähes vakio |

Vesivoimalaitoksessa virtausta lisätään tai vähennetään nopeasti, mutta tuulta ja aurinkoa ei voi käskeä. Ydinvoimala käy mieluiten tasaisesti, koska sen tehon muuttaminen on hidasta.

### Vertailun kriteerit
Eri tuotantotapoja vertaillaan samoilla kysymyksillä:
- **Hinta:** kuinka paljon sähkö maksaa tuottaa.
- **Teho:** kuinka suuri yksi voimala on.
- **Kuljetettavuus:** voiko polttoaineen kuljettaa voimalaan (kyllä) vai pitääkö voimala rakentaa sinne, missä tuuli tai vesi on.
- **Varastoitavuus:** polttoaineen ja vesialtaan voi varastoida, tuulta ja auringonsäteilyä ei.
- **Turvallisuus:** onnettomuuden vaikutus ja riski.
- **Ympäristö:** päästöt, maankäyttö, luonto ja jätteet.

### Suomen sähköntuotanto
Suomessa tuotettiin vuonna 2024 sähköä yhteensä noin 80 TWh (Tilastokeskus). Ydinvoima tuotti eniten, noin neljänneksen tuotti tuulivoima, ja fossiilisten polttoaineiden osuus oli vain muutama prosentti. Pylväät on piirretty mittakaavassa.

<svg data-fig="fi-bars" viewBox="0 0 600 330" role="img" aria-label="Vaakapylväskaavio Suomen sähköntuotannosta vuonna 2024 energialähteittäin teravattitunteina (Tilastokeskus), mittakaavassa: ydinvoima 31, tuulivoima 20,2, vesivoima 14,1, bioperäiset polttoaineet 9,5, fossiiliset polttoaineet ja turve 3,4 ja aurinkosähkö 0,9. Ydinvoiman pylväs on noin kolmannes kokonaistuotannosta 79,9." style="max-width:100%;font-size:24px">
  <foreignObject x="168" y="5.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E\ (\text{TWh})$</div></foreignObject>
  <line x1="275" y1="42" x2="275" y2="262" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="42" x2="380" y2="262" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="485" y1="42" x2="485" y2="262" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="170" y="46" width="325.5" height="26" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="10" y="44.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{ydinvoima}$</div></foreignObject>
  <foreignObject x="503.5" y="44.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$31$</div></foreignObject>
  <rect x="170" y="82" width="212" height="26" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="10" y="80.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{tuulivoima}$</div></foreignObject>
  <foreignObject x="390" y="80.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$20{,}2$</div></foreignObject>
  <rect x="170" y="118" width="148" height="26" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="10" y="116.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{vesivoima}$</div></foreignObject>
  <foreignObject x="326" y="116.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$14{,}1$</div></foreignObject>
  <rect x="170" y="154" width="100" height="26" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="10" y="152.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{bioperäiset}$</div></foreignObject>
  <foreignObject x="278" y="152.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$9{,}5$</div></foreignObject>
  <rect x="170" y="190" width="35.5" height="26" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="10" y="188.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{fossiiliset}$</div></foreignObject>
  <foreignObject x="213.5" y="188.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$3{,}4$</div></foreignObject>
  <rect x="170" y="226" width="9.5" height="26" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="10" y="224.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{aurinko}$</div></foreignObject>
  <foreignObject x="187.5" y="224.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0{,}9$</div></foreignObject>
  <line x1="170" y1="262" x2="533" y2="262" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M545,262 L532,268 L532,256 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="170" y1="40" x2="170" y2="264" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="275" y1="262" x2="275" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="258.5" y="273.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10$</div></foreignObject>
  <line x1="380" y1="262" x2="380" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="363.5" y="273.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$20$</div></foreignObject>
  <line x1="485" y1="262" x2="485" y2="269" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="468.5" y="273.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$30$</div></foreignObject>
  <foreignObject x="140" y="273.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
</svg>

## Kaava: Voimalan energia
Teho kertoo, kuinka nopeasti voimala tuottaa energiaa. Kun teho on vakio, tuotettu energia on teho kerrottuna ajalla:

```latex
E = P \cdot t
```
missä $E$ on tuotettu energia, $P$ voimalan teho ja $t$ aika. Kun teho on kilowatteina ja aika tunteina, energia on kilowattitunteina. Vuodessa on $t = 8760\,\text{h}$. Suuret energiat ilmoitetaan usein gigawatti- ja teravattitunteina: $1\,\text{GWh} = 10^{6}\,\text{kWh}$ ja $1\,\text{TWh} = 10^{9}\,\text{kWh}$.

### Nimellisteho ja keskiteho
Voimalan nimellisteho on suurin teho, jolla se voi toimia. Tuulivoimala ei tuota nimellisteholla koko vuotta, koska tuuli vaihtelee. Keskiteho on vuoden aikana tuotettu energia jaettuna vuoden tuntimäärällä. Keskiteho jaettuna nimellisteholla kertoo, kuinka suuri osa nimellistehosta on käytössä (kapasiteettikerroin).

### Suuruusluokat
Yhden voimalan teho voi olla tuhatta kertaa suurempi kuin toisen. Siksi suuruusluokkia vertaillaan kymmenen potensseilla: jokainen ruutu kuvassa on kymmenkertainen edellisestä.

<svg data-fig="unit-power" viewBox="0 0 600 372" role="img" aria-label="Vaakapylväskaavio yksittäisten voimalaitosten tehoista logaritmisella asteikolla, jossa jokainen ruutu on kymmenkertainen: omakotitalon aurinkopaneelit noin 5 kW, tuulivoimala noin 5 MW, suuri vesivoimalaitos noin 100 MW ja Olkiluoto 3 noin 1600 MW. Pylväiden pituudet ovat tehon logaritmin mukaiset, joten Olkiluoto 3 on noin 320 kertaa tuulivoimalaa suurempi, vaikka pylväs on vain vähän pidempi." style="max-width:100%;font-size:24px">
  <foreignObject x="40" y="3.5" width="330" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P\ (\text{W})$</div></foreignObject>
  <line x1="40" y1="44" x2="40" y2="300" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="44" x2="110" y2="300" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="44" x2="180" y2="300" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="250" y1="44" x2="250" y2="300" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="44" x2="320" y2="300" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="390" y1="44" x2="390" y2="300" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="460" y1="44" x2="460" y2="300" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="41.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{omakotitalon aurinkopaneelit}$</div></foreignObject>
  <rect x="40" y="72" width="49" height="24" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="97" y="69.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$5\,\text{kW}$</div></foreignObject>
  <foreignObject x="44" y="105.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{tuulivoimala}$</div></foreignObject>
  <rect x="40" y="136" width="259" height="24" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="307" y="133.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$5\,\text{MW}$</div></foreignObject>
  <foreignObject x="44" y="169.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{suuri vesivoimalaitos}$</div></foreignObject>
  <rect x="40" y="200" width="350" height="24" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="398" y="197.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$100\,\text{MW}$</div></foreignObject>
  <foreignObject x="44" y="233.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Olkiluoto 3}$</div></foreignObject>
  <rect x="40" y="264" width="434.5" height="24" rx="3" fill="#ffc078" stroke="#e8590c" stroke-width="1.5"/>
  <foreignObject x="482.5" y="261.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1600\,\text{MW}$</div></foreignObject>
  <line x1="40" y1="300" x2="488" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M500,300 L487,306 L487,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="40" y1="42" x2="40" y2="302" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="10" y="313.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{3}$</div></foreignObject>
  <line x1="110" y1="300" x2="110" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="80" y="313.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{4}$</div></foreignObject>
  <line x1="180" y1="300" x2="180" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="150" y="313.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{5}$</div></foreignObject>
  <line x1="250" y1="300" x2="250" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="220" y="313.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{6}$</div></foreignObject>
  <line x1="320" y1="300" x2="320" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="290" y="313.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{7}$</div></foreignObject>
  <line x1="390" y1="300" x2="390" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="360" y="313.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{8}$</div></foreignObject>
  <line x1="460" y1="300" x2="460" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="430" y="313.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{9}$</div></foreignObject>
</svg>

## Esimerkki
Esimerkkinä oleva tuulivoimala on nimellisteholtaan $5{,}0\,\text{MW}$ ja tuottaa vuoden aikana sähköä $14\,\text{GWh}$. Mikä on sen keskiteho ja kuinka suuri osa nimellistehosta se on?

<!-- vaihe -->

**Tunnetut ja kysytty.** Energia $E = 14\,\text{GWh}$, aika $t = 8760\,\text{h}$ ja nimellisteho $P_\text{nim} = 5{,}0\,\text{MW}$. Kysytään keskiteho $P_\text{ka}$ ja sen osuus nimellistehosta.

<!-- vaihe -->

**Periaate.** Energia on teho kerrottuna ajalla, $E = P t$. Tuulivoimalan teho vaihtelee, joten vuosienergiasta saadaan keskiteho, jolla voimala olisi tuottanut saman energian tasaisesti.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&E = P_\text{ka}\, t \\
&P_\text{ka} = \frac{E}{t}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** $14\,\text{GWh} = 14 \cdot 10^{6}\,\text{kWh}$ ja $5{,}0\,\text{MW} = 5{,}0 \cdot 1000\,\text{kW} = 5000\,\text{kW}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
P_\text{ka} &= E : t \\
&= 14 \cdot 10^{6}\,\text{kWh} : 8760\,\text{h} \\
&= 1598\,\text{kW} \\
\text{osuus} &= 1598\,\text{kW} : 5000\,\text{kW} = 0{,}32
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Keskiteho on $1{,}6\,\text{MW}$ eli $32\,\%$ nimellistehosta, kaksi merkitsevää numeroa kuten energiassa $14\,\text{GWh}$.

<!-- vaihe -->

**Järkevyys.** Jos voimala toimisi koko vuoden nimellisteholla, se tuottaisi $5000\,\text{kW} \cdot 8760\,\text{h} = 43{,}8\,\text{GWh}$, ja $14 : 43{,}8 = 0{,}32$. Osuus on alle yksi, koska tuuli ei puhalla aina.

## Yleinen virhekäsitys
Nimellisteho ei kerro, kuinka paljon sähköä voimala todella tuottaa. Tuulivoimala, jonka nimellisteho on 5 MW, tuottaa vuodessa vain noin kolmanneksen siitä, mitä tuottaisi, jos tuuli puhaltaisi aina oikealla nopeudella. Uusiutuva ei myöskään tarkoita jatkuvasti saatavaa: tuuli ja aurinko ovat uusiutuvia mutta sääriippuvaisia.

## Tiivistelmä
- Voimalaitos muuttaa luonnonvaran energian sähköksi; energia säilyy, mutta osa muuttuu hukkalämmöksi.
- Voimalat ovat sääriippuvaisia (tuuli, aurinko), hyvin säädettäviä (vesi, polttoaine) tai tasaista perusvoimaa (ydinvoima).
- Tuotettu energia on $E = P \cdot t$; keskiteho on vuosienergia jaettuna vuoden tuntimäärällä $8760\,\text{h}$.
- Voimaloita vertaillaan hinnan, tehon, kuljetettavuuden, varastoitavuuden, turvallisuuden ja ympäristövaikutusten mukaan.
- Suuruusluokat vertaillaan kymmenen potensseilla: Olkiluoto 3:n nimellisteho on yli kolmesataa tuulivoimalan nimellistehoa.
