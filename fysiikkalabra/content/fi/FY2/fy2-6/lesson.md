# Energiantuotantotavat ja niiden vertailu

> **Miksi** Suomen sähköverkossa toimii yhtä aikaa ydinvoimaa, vesivoimaa, tuulivoimaa ja polttoainevoimaloita, vaikka yksi voimalatyyppi voisi periaatteessa tuottaa kaiken sähkön?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: suomalainen maisema, jossa on ydinvoimala meren rannalla, vesivoimala joen padolla, tuulivoimaloita ja savupiipullinen polttoainevoimala. Kaikista lähtevät voimalinjat samaan verkkoon, joka vie sähkön kaupunkiin." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-6-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Voimalaitos ei tuota energiaa tyhjästä, vaan muuttaa luonnonvaran energian sähköksi ja usein myös lämmöksi. Putoavan veden ja tuulen liike-energia, auringon säteilyenergia, uraanin ydinenergia ja polttoaineen kemiallinen energia kulkevat turbiinin ja generaattorin tai aurinkopaneelin kautta sähköverkkoon. Energia säilyy, mutta osa siitä päätyy aina lämpönä ympäristöön (luku *Hyötysuhde*).

<svg data-fig="plants" viewBox="0 0 600 366" role="img" aria-label="Kaavakuva: viisi tapaa tuottaa sähköä. Putoava vesi pyörittää vesiturbiinia, tuuli roottoria, ja kummankin akseli pyörittää generaattoria G. Auringonsäteily osuu aurinkopaneeliin, joka tuottaa sähköä suoraan ilman generaattoria. Uraanin ydinenergia lämmittää reaktorissa höyryn ja polttoaineen kemiallinen energia kattilassa höyryn, ja höyry pyörittää turbiinia ja generaattoria. Harmaat nuolet ovat luonnonvaran energiaa, tummat nuolet sähköä, ja jokaisesta laitoksesta lähtee alaspäin oranssi nuoli: osa energiasta päätyy lämpönä ympäristöön. Kuva on kaavamainen, nuolten pituus ei kuvaa tehoa." style="max-width:100%;font-size:24px">
  <rect x="496" y="14" width="88" height="308" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="500" y="153.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sähkö}$</div></foreignObject>
  <rect x="16" y="14" width="132" height="44" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="20" y="21.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{vesi}$</div></foreignObject>
  <path d="M150,42 L160,42 L160,48 L174,36 L160,24 L160,30 L150,30 Z" fill="#6b7480" stroke-linejoin="round"/>
  <rect x="176" y="14" width="236" height="44" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="180" y="21.5" width="228" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{vesiturbiini}$</div></foreignObject>
  <path d="M386,59 L386,67 L381,67 L390,77 L399,67 L394,67 L394,59 Z" fill="#e8590c" stroke-linejoin="round"/>
  <line x1="414" y1="36" x2="427" y2="36" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M438,36 L426,41.5 L426,30.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="456" cy="36" r="16" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="443" y="21.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$G$</div></foreignObject>
  <line x1="474" y1="36" x2="483" y2="36" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M494,36 L482,41.5 L482,30.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="16" y="80" width="132" height="44" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="20" y="87.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tuuli}$</div></foreignObject>
  <path d="M150,108 L160,108 L160,114 L174,102 L160,90 L160,96 L150,96 Z" fill="#6b7480" stroke-linejoin="round"/>
  <rect x="176" y="80" width="236" height="44" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="180" y="87.5" width="228" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{roottori}$</div></foreignObject>
  <path d="M386,125 L386,133 L381,133 L390,143 L399,133 L394,133 L394,125 Z" fill="#e8590c" stroke-linejoin="round"/>
  <line x1="414" y1="102" x2="427" y2="102" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M438,102 L426,107.5 L426,96.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="456" cy="102" r="16" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="443" y="87.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$G$</div></foreignObject>
  <line x1="474" y1="102" x2="483" y2="102" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M494,102 L482,107.5 L482,96.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="16" y="146" width="132" height="44" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="20" y="153.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{säteily}$</div></foreignObject>
  <path d="M150,174 L160,174 L160,180 L174,168 L160,156 L160,162 L150,162 Z" fill="#6b7480" stroke-linejoin="round"/>
  <rect x="176" y="146" width="236" height="44" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="180" y="153.5" width="228" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{aurinkopaneeli}$</div></foreignObject>
  <path d="M386,191 L386,199 L381,199 L390,209 L399,199 L394,199 L394,191 Z" fill="#e8590c" stroke-linejoin="round"/>
  <line x1="414" y1="168" x2="483" y2="168" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M494,168 L482,173.5 L482,162.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="16" y="212" width="132" height="44" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="20" y="219.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{uraani}$</div></foreignObject>
  <path d="M150,240 L160,240 L160,246 L174,234 L160,222 L160,228 L150,228 Z" fill="#6b7480" stroke-linejoin="round"/>
  <rect x="176" y="212" width="236" height="44" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="180" y="219.5" width="228" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{reaktori, turbiini}$</div></foreignObject>
  <path d="M386,257 L386,265 L381,265 L390,275 L399,265 L394,265 L394,257 Z" fill="#e8590c" stroke-linejoin="round"/>
  <line x1="414" y1="234" x2="427" y2="234" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M438,234 L426,239.5 L426,228.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="456" cy="234" r="16" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="443" y="219.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$G$</div></foreignObject>
  <line x1="474" y1="234" x2="483" y2="234" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M494,234 L482,239.5 L482,228.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <rect x="16" y="278" width="132" height="44" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="20" y="285.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{polttoaine}$</div></foreignObject>
  <path d="M150,306 L160,306 L160,312 L174,300 L160,288 L160,294 L150,294 Z" fill="#6b7480" stroke-linejoin="round"/>
  <rect x="176" y="278" width="236" height="44" rx="10" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="180" y="285.5" width="228" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kattila, turbiini}$</div></foreignObject>
  <path d="M386,323 L386,331 L381,331 L390,341 L399,331 L394,331 L394,323 Z" fill="#e8590c" stroke-linejoin="round"/>
  <line x1="414" y1="300" x2="427" y2="300" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M438,300 L426,305.5 L426,294.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="456" cy="300" r="16" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="443" y="285.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$G$</div></foreignObject>
  <line x1="474" y1="300" x2="483" y2="300" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M494,300 L482,305.5 L482,294.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="16" y="323.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$G\text{: generaattori}$</div></foreignObject>
  <foreignObject x="300" y="323.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{lämpö}$</div></foreignObject>
</svg>

### Uusiutuva ja uusiutumaton energia
Vesi, tuuli ja auringonsäteily ovat uusiutuvia: ne eivät lopu käytettäessä. Bioperäiset polttoaineet, kuten puu, ovat uusiutuvia, kun uusi metsä kasvaa tilalle. Kivihiili, öljy ja maakaasu ovat fossiilisia, ja uraanikin on uusiutumaton luonnonvara. Turve kasvaa suolla niin hitaasti, tuhansien vuosien aikana, että se rinnastetaan päästöjen laskennassa fossiilisiin polttoaineisiin; tilastoissa se on usein omana ryhmänään. Voimaloiden päästöt ja ilmastovaikutukset käsitellään luvussa *Energiantuotanto, ympäristö ja ilmastonmuutos*.

<figure class="unit-photo"><img src="pics/fy2/summa-wind-turbines.webp" alt="Valkoisia tuulivoimaloita meren rannalla sinistä taivasta vasten."><figcaption>Summan tuulivoimapuiston voimaloita Haminassa. Tuulivoimala muuttaa tuulen liike-energiaa sähköksi.</figcaption></figure>

### Kolme ominaisuutta: miten voimala toimii verkossa
Sähköä ei voi varastoida suuria määriä suoraan verkkoon, joten tuotannon on vastattava kulutusta joka hetki. Siksi voimaloita kuvataan sen mukaan, kuinka niiden tehoon voi vaikuttaa. Ryhmät ovat hyödyllisiä ominaisuuksia, eivät toisensa poissulkevia luokkia: vesivoima on hyvin säädettävää mutta riippuu myös sateista.

| Ominaisuus | Tyypillisiä voimaloita | Teho |
|---|---|---|
| Sää&shy;riippuvainen | tuuli, aurinko | vaihtelee sään mukaan |
| Säädettävä | vesi, poltto&shy;aine | voidaan säätää |
| Perusvoima | ydinvoima | lähes vakio |

Vesivoimalaitoksessa virtausta lisätään tai vähennetään nopeasti, mutta tuulta ja aurinkoa ei voi käskeä. Ydinvoimalaa ajetaan yleensä tasaisesti lähes täydellä teholla, mutta sen tehoa voi tarvittaessa myös laskea: esimerkiksi Olkiluodon yksiköt ovat vähentäneet tehoaan, kun sähkön hinta on ollut hyvin matala.

```pysahdy
Illalla sähkön kulutus nousee äkkiä. Kumpi voimala pystyy vastaamaan siihen luotettavammin, vesivoimala vai tuulivoimala?
---
Vesivoimala, koska sen virtausta voi säätää nopeasti. Tuulta ei voi käskeä, joten tuulivoimalan teho riippuu säästä.
```

### Vertailun kriteerit
Eri tuotantotapoja vertaillaan samoilla kysymyksillä:

- **Hinta:** kuinka paljon sähkö maksaa tuottaa.
- **Teho:** kuinka suuri yksi voimala on.
- **Kuljetettavuus:** voiko energialähteen tuoda voimalaan, kuten polttoaineen, vai pitääkö voimala rakentaa sinne, missä tuuli tai virtaava vesi on.
- **Varastoitavuus:** polttoaineen ja vesialtaan voi varastoida, tuulta ja auringonsäteilyä ei.
- **Turvallisuus:** onnettomuuden vaikutus ja riski.
- **Ympäristö:** päästöt, maankäyttö, luonto ja jätteet.

### Suomen sähköntuotanto
Suomessa tuotettiin vuonna 2024 sähköä yhteensä noin $80\,\text{TWh}$ (Tilastokeskus). Ydinvoima tuotti eniten ja tuulivoima noin neljänneksen, ja fossiilisten polttoaineiden osuus oli vain muutama prosentti. Pylväät on piirretty mittakaavassa.

<svg data-fig="fi-bars" viewBox="0 0 600 330" role="img" aria-label="Vaakapylväskaavio Suomen sähköntuotannosta vuonna 2024 energialähteittäin teravattitunteina (Tilastokeskus), mittakaavassa: ydinvoima 31, tuulivoima 20,2, vesivoima 14,1, bioperäiset polttoaineet 9,5, fossiiliset polttoaineet ja turve 3,4 ja aurinkosähkö 0,9. Ydinvoiman pylväs on noin kaksi viidesosaa kokonaistuotannosta 79,9." style="max-width:100%;font-size:24px">
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

<figure class="unit-photo"><img src="pics/fy2/olkiluoto.webp" alt="Punavalkoisia voimalaitosrakennuksia ja korkeita piippuja meren takana kesäpäivänä. Vasemmalla on kupolikattoinen rakennus."><figcaption>Olkiluodon ydinvoimalaitos Eurajoella vuonna 2015. Vasemmalla oleva kolmas yksikkö aloitti säännöllisen sähköntuotannon vuonna 2023.</figcaption></figure>

## Kaava: Voimalan energia
Teho kertoo, kuinka nopeasti voimala tuottaa energiaa. Kun teho on vakio, tuotettu energia on teho kerrottuna ajalla:

```latex
E = P \cdot t
```
missä $E$ on tuotettu energia, $P$ voimalan teho ja $t$ aika. Kun teho on kilowatteina ja aika tunteina, energia on kilowattitunteina. Tavallisessa $365$ vuorokauden vuodessa on $t = 8760\,\text{h}$. Karkausvuodessa on $8784\,\text{h}$. Tämän luvun esimerkkilaskuissa käytetään tavallisen vuoden pituutta, ellei muuta ilmoiteta. Suuret energiat ilmoitetaan usein gigawatti- ja teravattitunteina: $1\,\text{GWh} = 10^{6}\,\text{kWh}$ ja $1\,\text{TWh} = 10^{9}\,\text{kWh}$.

```pysahdy
Voimala tuottaa vakioteholla $2{,}0\,\text{MW}$ ajan $3\,\text{h}$. Kuinka paljon energiaa se tuottaa?
---
Energia on teho kertaa aika: $E = P \cdot t$.
Siis $E = 2{,}0\,\text{MW} \cdot 3\,\text{h} = 6{,}0\,\text{MWh}$.
```

### Nimellisteho ja keskiteho
Voimalan nimellisteho on suurin teho, jolla se voi toimia. Tuulivoimala ei tuota nimellisteholla koko vuotta, koska tuuli vaihtelee. Keskiteho on vuoden aikana tuotettu energia jaettuna vuoden tuntimäärällä. Keskiteho jaettuna nimellisteholla kertoo, kuinka suuri osa nimellistehosta on keskimäärin käytössä.

```pysahdy
Tuulivoimalan nimellisteho on $5\,\text{MW}$ ja vuoden keskiteho $1{,}5\,\text{MW}$. Miksi keskiteho on pienempi, ja kuinka suuri osa nimellistehosta se on?
---
Tuuli vaihtelee, joten voimala ei tuota nimellisteholla koko ajan. Osuus on $1{,}5\,\text{MW} : 5\,\text{MW} = 0{,}30$.
```

### Suuruusluokat
Yhden voimalan teho voi olla tuhatta kertaa suurempi kuin toisen. Siksi suuruusluokkia vertaillaan kymmenen potensseilla. Kuvan vaaka-akselilla jokainen askel pystyviivalta seuraavalle on kymmenkertainen, joten pisteiden välimatka kertoo, montako kertaa kymmenen teho kasvaa.

<svg data-fig="unit-power" viewBox="0 0 600 368" role="img" aria-label="Yksittäisten voimalaitosten tehot yhdellä vaakasuoralla logaritmisella akselilla, jossa jokainen väli on kymmenkertainen edelliseen: omakotitalon aurinkopaneelit noin 5 kW, tuulivoimala noin 5 MW, suuri vesivoimalaitos noin 100 MW ja Olkiluoto 3 noin 1600 MW. Jokaisen laitoksen nimi on viiteviivan päässä oman pisteensä yläpuolella. Pisteen paikka kertoo tehon kymmenen potenssin, joten Olkiluoto 3 on noin 320 kertaa tuulivoimalaa suurempi, vaikka sen piste on vain kaksi ja puoli väliä oikeammalla." style="max-width:100%;font-size:24px">
  <line x1="44" y1="24" x2="44" y2="292" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="122" y1="24" x2="122" y2="292" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="24" x2="200" y2="292" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="278" y1="24" x2="278" y2="292" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="356" y1="24" x2="356" y2="292" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="434" y1="24" x2="434" y2="292" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="512" y1="24" x2="512" y2="292" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="528" y1="292" x2="528" y2="62" stroke="#6b7480" stroke-width="1.25" stroke-linecap="butt"/>
  <path d="M505.92135864716215,58 V42 Q517.9213586471622,22 529.9213586471622,42 V58 Z" fill="#ffffff" stroke="#1f2933" stroke-width="1.75" stroke-linejoin="round"/>
  <rect x="530" y="44" width="20" height="14" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.75"/>
  <foreignObject x="196" y="20.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{Olkiluoto 3}$</div></foreignObject>
  <foreignObject x="376" y="50.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$1600\,\text{MW}$</div></foreignObject>
  <circle cx="528" cy="292" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="98.5" y1="292" x2="98.5" y2="122" stroke="#6b7480" stroke-width="1.25" stroke-linecap="butt"/>
  <path d="M78.51966033820946,106 L88.51966033820946,88 H118.51966033820946 L108.51966033820946,106 Z" fill="#2f74b5" stroke="#1f2933" stroke-width="1.75" stroke-linejoin="round"/>
  <line x1="88.5" y1="106" x2="98.5" y2="88" stroke="#ffffff" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="98.5" y1="106" x2="108.5" y2="88" stroke="#ffffff" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="83.5" y1="97" x2="113.5" y2="97" stroke="#ffffff" stroke-width="1.2" stroke-linecap="butt"/>
  <foreignObject x="126.5" y="80.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{omakotitalon aurinkopaneelit}$</div></foreignObject>
  <foreignObject x="126.5" y="110.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$5\,\text{kW}$</div></foreignObject>
  <circle cx="98.5" cy="292" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="434" y1="292" x2="434" y2="182" stroke="#6b7480" stroke-width="1.25" stroke-linecap="butt"/>
  <rect x="410" y="156" width="18" height="20" fill="#a9d1f0"/>
  <path d="M410.0,156 H428.0" fill="none" stroke="#2f74b5" stroke-width="2" stroke-linejoin="round"/>
  <path d="M428.0,150 H436.0 L446.0,176 H428.0 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="1.75" stroke-linejoin="round"/>
  <path d="M446.0,173 q6,3 12,0" fill="none" stroke="#2f74b5" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="102" y="140.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{suuri vesivoimalaitos}$</div></foreignObject>
  <foreignObject x="282" y="170.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$100\,\text{MW}$</div></foreignObject>
  <circle cx="434" cy="292" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="332.5" y1="292" x2="332.5" y2="242" stroke="#6b7480" stroke-width="1.25" stroke-linecap="butt"/>
  <path d="M329.51966033820946,238 L331.51966033820946,216 H333.51966033820946 L335.51966033820946,238 Z" fill="#ffffff" stroke="#1f2933" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="332.5" y1="216" x2="332.5" y2="201" stroke="#1f2933" stroke-width="2.2" stroke-linecap="round"/>
  <line x1="332.5" y1="216" x2="319.5" y2="223.5" stroke="#1f2933" stroke-width="2.2" stroke-linecap="round"/>
  <line x1="332.5" y1="216" x2="345.5" y2="223.5" stroke="#1f2933" stroke-width="2.2" stroke-linecap="round"/>
  <circle cx="332.5" cy="216" r="2.4" fill="#1f2933"/>
  <foreignObject x="9.5" y="200.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{tuulivoimala}$</div></foreignObject>
  <foreignObject x="189.5" y="230.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$5\,\text{MW}$</div></foreignObject>
  <circle cx="332.5" cy="292" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="44" y1="292" x2="546" y2="292" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M558,292 L545,298 L545,286 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="44" y1="292" x2="44" y2="299" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="14" y="303.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{3}$</div></foreignObject>
  <line x1="122" y1="292" x2="122" y2="299" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="92" y="303.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{4}$</div></foreignObject>
  <line x1="200" y1="292" x2="200" y2="299" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="170" y="303.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{5}$</div></foreignObject>
  <line x1="278" y1="292" x2="278" y2="299" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="248" y="303.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{6}$</div></foreignObject>
  <line x1="356" y1="292" x2="356" y2="299" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="326" y="303.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{7}$</div></foreignObject>
  <line x1="434" y1="292" x2="434" y2="299" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="404" y="303.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{8}$</div></foreignObject>
  <line x1="512" y1="292" x2="512" y2="299" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="482" y="303.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$10^{9}$</div></foreignObject>
  <foreignObject x="478" y="335.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P\ (\text{W})$</div></foreignObject>
  <foreignObject x="44" y="335.5" width="330" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{jokainen väli on 10-kertainen}$</div></foreignObject>
</svg>

## Esimerkki
Esimerkkinä oleva tuulivoimala on nimellisteholtaan $5{,}0\,\text{MW}$ ja tuottaa vuoden aikana sähköä $14\,\text{GWh}$. Mikä on sen keskiteho ja kuinka suuri osa nimellistehosta se on?

<!-- vaihe -->

**Tunnetut ja kysytty.** Energia $E = 14\,\text{GWh}$, aika $t = 8760\,\text{h}$ ja nimellisteho $P_\text{nim} = 5{,}0\,\text{MW}$.

Kysytään keskiteho $P_\text{ka}$ ja sen osuus nimellistehosta.

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

**Yksikkömuunnokset.** $14\,\text{GWh} = {14 \cdot 10^{6}}\,\text{kWh}$ ja $5{,}0\,\text{MW} = 5{,}0 \cdot 1000\,\text{kW} = 5000\,\text{kW}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
P_\text{ka} &= E : t \\
&= 14 \cdot 10^{6}\,\text{kWh} : 8760\,\text{h} \\
&= 1598\,\text{kW} \\
\text{osuus} &= P_\text{ka} : P_\text{nim} \\
&= 1598\,\text{kW} : 5000\,\text{kW} \\
&= 0{,}32
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Keskiteho on $1598\,\text{kW} = 1{,}598\,\text{MW} \approx 1{,}6\,\text{MW}$ eli $32\,\%$ nimellistehosta, kaksi merkitsevää numeroa kuten energiassa $14\,\text{GWh}$.

<!-- vaihe -->

**Järkevyys.** Jos voimala toimisi koko vuoden nimellisteholla, se tuottaisi $5000\,\text{kW} \cdot 8760\,\text{h} = 43\,800\,000\,\text{kWh} = 43{,}8 \cdot 10^{6}\,\text{kWh} = 43{,}8\,\text{GWh}$, ja $14 : 43{,}8 = 0{,}32$.

Osuus on alle yksi, koska tuuli ei puhalla aina.

## Yleinen virhekäsitys
Nimellisteho ei kerro, kuinka paljon sähköä voimala todella tuottaa. Tuulivoimala, jonka nimellisteho on $5\,\text{MW}$, tuottaa vuodessa vain noin kolmanneksen siitä, mitä tuottaisi, jos tuuli puhaltaisi aina oikealla nopeudella. Uusiutuva ei myöskään tarkoita jatkuvasti saatavaa: tuuli ja aurinko ovat uusiutuvia mutta sääriippuvaisia.

## Tiivistelmä
- Voimalaitos muuttaa luonnonvaran energian sähköksi; energia säilyy, mutta osa muuttuu hukkalämmöksi.
- Voimaloita kuvataan ominaisuuksilla, jotka eivät sulje toisiaan pois: sääriippuvainen (tuuli, aurinko), hyvin säädettävä (vesi, polttoaine) ja yleensä tasaisesti ajettava perusvoima (ydinvoima).
- Tuotettu energia on $E = P \cdot t$; keskiteho on vuosienergia jaettuna vuoden tuntimäärällä $8760\,\text{h}$.
- Voimaloita vertaillaan hinnan, tehon, kuljetettavuuden, varastoitavuuden, turvallisuuden ja ympäristövaikutusten mukaan.
- Suuruusluokat vertaillaan kymmenen potensseilla: Olkiluoto 3:n nimellisteho on yli kolmesataa tuulivoimalan nimellistehoa.
