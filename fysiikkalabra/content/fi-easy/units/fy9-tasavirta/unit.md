# Tasavirtapiirit ja sähköenergia

> **Miksi** mökin akku riittää pelkille LED-valoille yli viikon, mutta kylmälaukun kanssa vain vuorokauden?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: punainen kesämökki järven rannalla iltahämärässä. Taivas on ylhäällä tummansininen ja taivaanrannassa lämpimän oranssi. Taivaalla on kuunsirppi ja muutama tähti. Mökin ikkunoista loistaa lämmin keltainen valo. Pihalla on aurinkopaneeli telineen päällä. Sen johto kulkee harmaaseen akkulaatikkoon, joka on mökin seinällä. Kuistin portailla on sininen kylmälaukku. Rannassa on laituri ja soutuvene. Taustalla näkyy vastarannan kuusimetsä, ja mökin vieressä kasvaa koivu ja kuusia." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-tasavirta-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

Tasavirtapiirissä lähde pitää yllä **jännitettä**. Jännite ajaa piirin läpi **virran**. Virran suuruuden määrää koko piirin resistanssi. Siksi sama paristo antaa eri laitteille eri virrat. Virta ei kulu komponentissa eli piirin osassa. Komponentti muuttaa sähköenergiaa, jota varaukset kuljettavat, valoksi, liikkeeksi tai sisäenergiaksi. **Teho** kertoo, kuinka nopeasti energia muuttuu.

<svg data-fig="kartta" viewBox="0 0 380 866" role="img" aria-label="Tunnistuskaavio: mistä tunnistan, mitä lakia käytän? Piirrä ensin kytkentäkaavio ja katso, mikä tehtävän tunnusmerkki sopii. Varausta kulkee ajassa: virta on varaus jaettuna ajalla. Jännite ja virta tunnetaan: resistanssi saadaan Ohmin laista, jännite on resistanssi kertaa virta. Johtimen mitat ja aine: resistanssi on resistiivisyys kertaa pituus jaettuna poikkipinta-alalla. Sarjaan kytketyt: virta on sama ja kokonaisresistanssi on resistanssien summa. Rinnan kytketyt: jännite on sama ja kokonaisresistanssin käänteisluku on käänteislukujen summa. Virta haarautuu: haarapisteeseen tulevien virtojen summa on yhtä suuri kuin lähtevien. Suljettu silmukka: jännitteiden summa on nolla. Laitteen teho tai energia: teho on jännite kertaa virta. Paristolla on sisäinen vastus: napajännite johdetaan kiertämällä piiri. Jännitteiden summa on nolla." style="max-width:100%;font-size:21px">
  <line x1="14" y1="80" x2="14" y2="822" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="8" y="8" width="364" height="72" rx="12" fill="#f1dfb5" stroke="#d9b26a" stroke-width="2.5"/>
  <foreignObject x="25" y="21.5" width="330" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:21px">$\textbf{mistä tunnistan lain?}$</div></foreignObject>
  <foreignObject x="20" y="52" width="340" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px">$\text{piirrä kytkentä ensin, sitten tunnusmerkki}$</div></foreignObject>
  <line x1="14" y1="134" x2="30" y2="134" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="98" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="108.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{varausta kulkee ajassa}$</div></foreignObject>
  <line x1="40" y1="138" x2="362" y2="138" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="143" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{virta}$</div></foreignObject>
  <rect x="238" y="142" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="144" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$I = \Delta Q/\Delta t$</div></foreignObject>
  <line x1="14" y1="220" x2="30" y2="220" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="184" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="194.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{jännite ja virta tunnetaan}$</div></foreignObject>
  <line x1="40" y1="224" x2="362" y2="224" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="229" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{resistanssi}$</div></foreignObject>
  <rect x="238" y="228" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="230" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$U = RI$</div></foreignObject>
  <line x1="14" y1="306" x2="30" y2="306" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="270" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="280.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{johtimen mitat ja aine}$</div></foreignObject>
  <line x1="40" y1="310" x2="362" y2="310" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="315" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{resistanssi}$</div></foreignObject>
  <rect x="238" y="314" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="316" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$R = \rho\ell/A$</div></foreignObject>
  <line x1="14" y1="392" x2="30" y2="392" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="356" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="366.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{sarjaan kytketyt}$</div></foreignObject>
  <line x1="40" y1="396" x2="362" y2="396" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="401" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{sama virta}$</div></foreignObject>
  <rect x="238" y="400" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="402" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$R_\text{kok} = \Sigma R$</div></foreignObject>
  <line x1="14" y1="478" x2="30" y2="478" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="442" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="452.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{rinnan kytketyt}$</div></foreignObject>
  <line x1="40" y1="482" x2="362" y2="482" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="487" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{sama jännite}$</div></foreignObject>
  <rect x="238" y="486" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="488" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$1/R_\text{kok} = \Sigma 1/R$</div></foreignObject>
  <line x1="14" y1="564" x2="30" y2="564" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="528" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="538.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{virta haarautuu}$</div></foreignObject>
  <line x1="40" y1="568" x2="362" y2="568" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="573" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{haarapiste}$</div></foreignObject>
  <rect x="238" y="572" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="574" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma I_\text{t} = \Sigma I_\text{l}$</div></foreignObject>
  <line x1="14" y1="650" x2="30" y2="650" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="614" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="624.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{suljettu silmukka}$</div></foreignObject>
  <line x1="40" y1="654" x2="362" y2="654" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="659" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{jännitteet}$</div></foreignObject>
  <rect x="238" y="658" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="660" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma\Delta V = 0$</div></foreignObject>
  <line x1="14" y1="736" x2="30" y2="736" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="700" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="710.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{laitteen teho tai energia}$</div></foreignObject>
  <line x1="40" y1="740" x2="362" y2="740" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="745" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{teho}$</div></foreignObject>
  <rect x="238" y="744" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="746" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$P = UI$</div></foreignObject>
  <line x1="14" y1="822" x2="30" y2="822" stroke="#c9c2b2" stroke-width="3" stroke-linecap="butt"/>
  <rect x="30" y="786" width="342" height="72" rx="10" fill="#ffffff" stroke="#6b7480" stroke-width="2"/>
  <foreignObject x="44" y="796.5" width="314" height="23" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:19px">$\text{paristolla on sisäinen vastus}$</div></foreignObject>
  <line x1="40" y1="826" x2="362" y2="826" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="44" y="831" width="170" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:17px;color:#6b7480">$\to\ \text{johda silmukalla}$</div></foreignObject>
  <rect x="238" y="830" width="124" height="24" rx="8" fill="#1a4d2e" stroke="#1a4d2e" stroke-width="2"/>
  <foreignObject x="242" y="832" width="116" height="20" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:17px;color:#ffffff">$\Sigma\Delta V = 0$</div></foreignObject>
</svg>

Kun kokeessa on piiritehtävä, selvitä ensin kytkentä. Jos komponentit on kytketty sarjaan, niiden läpi kulkee sama virta. Jos komponentit on kytketty rinnan, niiden yli on sama jännite. Sen jälkeen Kirchhoffin lait ja Ohmin laki antavat virrat ja jännitteet. Teho ja energia lasketaan niiden avulla.

Nyt voimme vastata alun kysymykseen. Mökin laitteet on kytketty akkuun rinnan, joten kummankin laitteen yli on $12\,\text{V}$. LED-valot ottavat virran $\tfrac{6{,}0\,\text{W}}{12\,\text{V}} = 0{,}50\,\text{A}$ ja kylmälaukku $\tfrac{48\,\text{W}}{12\,\text{V}} = 4{,}0\,\text{A}$. Akusta lähtee näiden summa $4{,}5\,\text{A}$. Akun kapasiteetti on $100\,\text{Ah}$. Se riittää pelkille valoille $200\,\text{h}$ eli yli kahdeksan vuorokautta, mutta molemmille laitteille vain noin $22\,\text{h}$.

<svg data-fig="mokki" viewBox="0 0 600 356" role="img" aria-label="Kytkentäkaavio, ei mittakaavassa. Vasemmalla on 12 voltin akku. Akun plusnapa on ylhäällä. Akkuun on kytketty rinnan kaksi haaraa: LED-valot, joiden teho on 6,0 wattia, ja kylmälaukku, jonka teho on 48 wattia. Violetit nuolet näyttävät virran. Akun plusnavasta lähtee 4,5 ampeerin virta. Haarautumispisteessä se jakautuu kahteen osaan: 0,50 ampeeria menee LED-valoihin ja 4,0 ampeeria kylmälaukkuun. Haarojen virrat yhtyvät alajohtimessa ja palaavat akun miinusnapaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-tasavirta-mokki.webp" x="1.2" y="1.2" width="597" height="360.7" preserveAspectRatio="none"/>
  <foreignObject x="94" y="158.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="96" y="198.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$12\,\text{V}$</div></foreignObject>
  <foreignObject x="282" y="164.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{LED}$</div></foreignObject>
  <foreignObject x="282" y="198.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$6{,}0\,\text{W}$</div></foreignObject>
  <foreignObject x="436" y="164.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kylmälaukku}$</div></foreignObject>
  <foreignObject x="436" y="198.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$48\,\text{W}$</div></foreignObject>
  <foreignObject x="120" y="25.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$4{,}5\,\text{A}$</div></foreignObject>
  <foreignObject x="153" y="252.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$0{,}50\,\text{A}$</div></foreignObject>
  <foreignObject x="326" y="252.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$4{,}0\,\text{A}$</div></foreignObject>
  <foreignObject x="120" y="329.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$4{,}5\,\text{A}$</div></foreignObject>
</svg>

## Kaava: Tasavirtapiirit ja sähköenergia

### Virta, jännite ja resistanssi

```kaavat
sähkövirta :: I = \frac{\Delta Q}{\Delta t}
jännitehäviö johtimessa :: U = RI
johtimen resistanssi :: R = \rho\,\frac{\ell}{A}
```

missä $I$ on virta ($\text{A}$), $\Delta Q$ varaus, joka on kulkenut poikkileikkauksen läpi ($\text{C}$), $\Delta t$ aika ($\text{s}$), $U$ komponentin jännite ($\text{V}$), $R$ resistanssi ($\Omega$), $\rho$ resistiivisyys ($\Omega\cdot\text{m}$), $\ell$ johtimen pituus ($\text{m}$) ja $A$ poikkipinta-ala ($\text{m}^2$). Ohmin lain mukaan metallijohtimen resistanssi on vakio eli se ei muutu, kun lämpötila pysyy samana. Hehkulampun resistanssi kasvaa, kun lanka kuumenee. Virtamittari kytketään sarjaan ja jännitemittari rinnan.

### Kytkennät ja Kirchhoffin lait

```kaavat
sarjaan kytkettyjen vastusten kokonaisresistanssi :: R_\text{kok} = \Sigma R
rinnan kytkettyjen vastusten kokonaisresistanssi :: \frac{1}{R_\text{kok}} = \Sigma\frac{1}{R}
Kirchhoffin 1. laki :: \Sigma I_\text{t} = \Sigma I_\text{l}
Kirchhoffin 2. laki :: \Sigma \Delta V = 0
```

Ensimmäinen kaava antaa sarjaan kytkettyjen vastusten kokonaisresistanssin $R_\text{kok}$. Toinen kaava antaa rinnan kytkettyjen vastusten kokonaisresistanssin. Merkki $\Sigma$ tarkoittaa summaa. Virtalaissa $I_\text{t}$ ovat haarautumispisteeseen tulevat virrat ja $I_\text{l}$ siitä lähtevät virrat. Virtalaki pätee haarautumispisteessä eli kohdassa, jossa johto jakautuu. Se pätee, koska varaus säilyy. Jännitelaki pätee, kun silmukka eli suljettu reitti kierretään kerran. Potentiaali $V$ nousee lähteessä miinusnavalta plusnavalle. Vastuksessa potentiaali laskee virran suuntaan $RI$:n verran. Siksi rinnakkaisten haarojen yli on sama jännite.

### Teho ja energia

```kaavat
tehonkulutus johtimessa :: P = UI
teho :: P = \frac{W}{\Delta t}
```

missä $P$ on teho ($\text{W}$) ja $W$ sähköenergia, joka on muuttunut ajassa $\Delta t$ ($\text{J}$ tai $\text{kWh}$). Kaava $P = UI$ pätee kaikille komponenteille. Vastuksen tehon voi laskea myös pelkästä virrasta tai pelkästä jännitteestä. Silloin tehon kaavaan sijoitetaan Ohmin laki (Johda itse alla). Sarjaankytkennässä suurempi resistanssi saa suuremman tehon. Rinnankytkennässä pienempi resistanssi saa suuremman tehon. Energian yksiköt muunnetaan sijoittamalla: $1\,\text{kWh} = 1000\,\text{W} \cdot 3600\,\text{s} = 3{,}6\,\text{MJ}$. Energialle käytetään kirjainta $W$, koska $E$ tarkoittaa lähdejännitettä.

```johda
Johda vastuksen teho $P$ kahdella tavalla: virran $I$ avulla ja jännitteen $U$ avulla.
---
Teho on $P = UI$. Ohmin lain mukaan vastuksen jännite on $U = RI$. Sijoitetaan jännite tehon kaavaan:

$$P = UI = RI \cdot I = RI^2$$

Ohmin laista saadaan myös virta $I = \tfrac{U}{R}$. Sijoitetaan virta tehon kaavaan:

$$P = UI = U \cdot \frac{U}{R} = \frac{U^2}{R}$$

Nämä muodot pätevät vain vastukselle, koska niissä käytetään Ohmin lakia.
```

### Paristo ja akku

Paristoa kuvataan mallilla. Mallissa lähdejännite $E$ ($\text{V}$) ja sisäinen resistanssi $R_\text{s}$ ($\Omega$) ovat sarjassa. Napajännite $U$ ($\text{V}$) on pariston napojen välinen jännite. Kun paristosta kulkee virta $I$, osa lähdejännitteestä kuluu pariston sisällä. Siksi napajännite on pienempi kuin lähdejännite. Ulkoisen piirin resistanssi on $R$ ($\Omega$).

<svg data-fig="piiri" viewBox="0 0 600 330" role="img" aria-label="Kytkentäkaavio ilman lukuarvoja. Vasemmalla on katkoviivalaatikko. Se on paristo. Laatikon sisällä on sarjassa lähdejännite E ja sisäinen resistanssi R s. Lähdejännite on piirretty jännitelähteen merkillä ja sisäinen resistanssi vastuksena. Laatikon oikeassa reunassa ovat pariston navat. Plusnapa on ylhäällä ja miinusnapa alhaalla. Napojen välissä on napajännite U. Napoihin on kytketty ulkoinen vastus R. Violetti virta I kulkee plusnavasta vastuksen R kautta takaisin miinusnapaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy9/fy9-tasavirta-piiri.webp" x="9.7" y="1.2" width="582.5" height="327.7" preserveAspectRatio="none"/>
  <foreignObject x="64" y="251" width="74" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:18px;color:#6b7480">$\text{paristo}$</div></foreignObject>
  <foreignObject x="184" y="121" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$+$</div></foreignObject>
  <foreignObject x="96" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="91" y="190.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <foreignObject x="324" y="71" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$+$</div></foreignObject>
  <foreignObject x="324" y="223" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:22px">$-$</div></foreignObject>
  <foreignObject x="248" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$U$</div></foreignObject>
  <foreignObject x="494" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R$</div></foreignObject>
  <foreignObject x="380" y="19.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
</svg>

```johda
Pariston napoihin kytketään vastus $R$. Johda piirissä kulkeva virta $I$ ja pariston napajännite $U$.
---
Kierretään piiri kerran virran suuntaan. Käytetään Kirchhoffin 2. lakia. Lähteessä potentiaali nousee lähdejännitteen $E$ verran. Sisäisessä resistanssissa potentiaali laskee $R_\text{s}I$ ja ulkoisessa vastuksessa $RI$:

$$E - R_\text{s}I - RI = 0$$

Ratkaistaan virta:

$$I = \frac{E}{R + R_\text{s}}$$

Napajännite on ulkoisen vastuksen jännite. Se on lähdejännite, josta on vähennetty sisäisen resistanssin jännitehäviö:

$$U = RI = E - R_\text{s}I$$
```

```kaavat
sähkövirta :: I = \frac{\Delta Q}{\Delta t}
```

missä $Q$ on akun kapasiteetti ($\text{Ah}$ tai $\text{C}$) eli varaus $\Delta Q$, jonka akku antaa ajassa $\Delta t$. Malli olettaa, että $E$ ja $R_\text{s}$ pysyvät vakioina. Akun energia on $W = UQ$, missä $U$ on nimellisjännite eli akkuun merkitty jännite. Latauksen aikana virta kulkee akun läpi toiseen suuntaan. Silloin napajännite on suurempi kuin lähdejännite.

Pariston $(I, U)$-kuvaaja on laskeva suora. Suora leikkaa pystyakselin kohdassa, jossa jännite on lähdejännite $E$. Vaaka-akselin se leikkaa oikosulkuvirran $I_\text{k} = \tfrac{E}{R_\text{s}}$ kohdalla. Suoran kulmakerroin on $-R_\text{s}$.

<svg data-fig="napa" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva ilman lukuarvoja: pariston napajännite U virran I funktiona. Laskeva suora alkaa pystyakselilta lähdejännitteen E kohdalta. Se leikkaa vaaka-akselin oikosulkuvirran I k kohdalla. Suoralle on piirretty kulmakertoimen kolmio. Kolmion vaakasivu on delta I ja pystysivu delta U. Kulmakerroin on miinus R s. Suoran yläpäässä virrat ovat pieniä, ja napajännite on melkein E." style="max-width:100%;font-size:24px">
  <line x1="79" y1="320" x2="484" y2="320" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,320 L483,326 L483,314 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="321" x2="80" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,34 L86,47 L74,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="50" y="325.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I$</div></foreignObject>
  <foreignObject x="70" y="3.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <polyline points="80,103.5 431,320" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="80" cy="103.5" r="6" fill="#1971c2"/>
  <foreignObject x="48" y="89" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$E$</div></foreignObject>
  <circle cx="431" cy="320" r="6" fill="#c92a2a"/>
  <foreignObject x="414.5" y="331.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$I_\text{k}$</div></foreignObject>
  <line x1="177.5" y1="163.5" x2="314" y2="163.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="314" y1="163.5" x2="314" y2="248" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="229" y="129" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\Delta I$</div></foreignObject>
  <foreignObject x="326" y="191" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\Delta U$</div></foreignObject>
  <foreignObject x="298.5" y="106" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kulmakerroin } {-R_\text{s}}$</div></foreignObject>
</svg>

## Yleisiä virheitä {Virheet}

- **Virta kuluu.** Komponenttiin tulee sama virta kuin siitä lähtee. Komponentissa muuttuu energia, ei virta.
- **Lähteen jännite sarjavastukselle.** Sarjaan kytketyn vastuksen yli on vain osa lähteen jännitteestä. Laske ensin virta ja sitten $U_1 = R_1 I$.
- **Käänteisluku unohtuu.** Kun lasket rinnankytkennän, saat ensin $\tfrac{1}{R}$. Se pitää lopuksi kääntää. Kokonaisresistanssi on pienempi kuin pienin haaran resistanssi.
- **Hehkulamppu Ohmin lain mukaan.** Kuuman langan resistanssi on suurempi. Siksi lampun resistanssi lasketaan suhteena $U : I$ jokaisessa kohdassa erikseen.
- **Napajännite on aina merkitty jännite.** Kun paristosta otetaan virtaa, napajännite on $R_\text{s} I$:n verran pienempi kuin lähdejännite.
- **Kilowattitunti tehona.** $\text{kWh}$ on energian yksikkö. Kilowatit kerrotaan tunneilla, ja minuutit muutetaan ensin tunneiksi.
- **Milliampeeritunnit energiana.** $\text{mAh}$ on varauksen yksikkö. Siksi akkuja verrataan energian $W = UQ$ avulla.

## Kertaa tarvittaessa {Kertaa}

- Piirin suureet: [*Virtapiiri, sähkövirta ja jännite*](fy6-1.html), [*Mittaukset virtapiirissä*](fy6-2.html) ja [*Resistanssi ja Ohmin laki*](fy6-3.html).
- Kytkennät: [*Vastusten sarja- ja rinnankytkennät*](fy6-4.html) ja [*Kirchhoffin lait ja potentiaali virtapiirissä*](fy6-5.html).
- Teho ja energia: [*Sähköteho ja vastuksen lämpeneminen*](fy6-6.html) ja [*Sähköenergia kotona*](fy6-7.html).
- Lähteet: [*Lähdejännite ja sisäinen resistanssi*](fy6-8.html) ja [*Akut ja latauspiiri*](fy6-9.html).
