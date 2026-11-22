# Akut ja latauspiiri

> **Miksi** puhelimen akku latautuu alussa nopeasti, mutta viimeiset prosentit vievät pitkän ajan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: älypuhelin latautuu puisella pöydällä illalla. Puhelimesta kulkee johto seinän pistorasiassa olevaan valkoiseen laturiin. Puhelimen näytössä on akun kuva, joka on melkein kokonaan vihreä, ja sen vieressä salaman merkki. Pöydällä on kahvikuppi, ja seinällä lamppu valaisee." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-9-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Paristo ja akku
Paristossa ja akussa kemiallinen reaktio pitää napojen välillä jännitteen. Sitä sanotaan lähdejännitteeksi $E$ (luku *Lähdejännite ja sisäinen resistanssi*). Kun piiri suljetaan, kemiallista energiaa muuttuu sähköenergiaksi. **Paristo** on kertakäyttöinen. Kun sen aineet ovat reagoineet, reaktiota ei voi turvallisesti kääntää. **Akku** on ladattava. Ulkoinen jännitelähde voi ajaa sen reaktion takaisin, ja akkuun varastoituu taas kemiallista energiaa. Puhelimissa, kannettavissa tietokoneissa ja sähköautoissa on yleensä litiumioniakku. Auton käynnistysakku on lyijyakku.

Akku ei varastoi sähkövarausta. Se on sähköisesti neutraali sekä täynnä että tyhjänä. Kun akku purkautuu, se vain siirtää varauksia piirin ympäri. Jokainen varaus, joka lähtee plusnavasta, palaa miinusnapaan. Ulkoisessa piirissä virta kulkee plusnavasta miinusnapaan. Akun sisällä virta kulkee miinusnavalta plusnavalle.

```pysahdy
Mitä akussa muuttuu, kun se ladataan? Muuttuuko sen kokonaisvaraus?
---
Sähköenergiaa muuttuu akun kemialliseksi energiaksi. Kokonaisvaraus ei muutu: akku pysyy neutraalina.
```

### Lataaminen kääntää virran akun sisällä
Akku ladataan kytkemällä laturin plusnapa akun plusnapaan ja miinusnapa miinusnapaan. Kun laturin jännite on suurempi kuin akun lähdejännite, laturi pakottaa virran akun läpi toiseen suuntaan kuin purkautuessa. Akun sisällä virta kulkee silloin plusnavalta miinusnavalle. Sähköenergiaa muuttuu tällöin akun kemialliseksi energiaksi. Kuvassa ylempi piiri purkaa akkua lamppuun ja alempi lataa sitä. Kun virran suunta akun sisällä kääntyy, myös energia kulkee toiseen suuntaan.

<svg data-fig="purku-lataus" viewBox="0 0 600 384" role="img" aria-label="Kaksi kytkentäkaaviota päällekkäin, ei mittakaavassa. Ylempi: akku purkautuu. Akku on vasemmalla, plusnapa eli pitkä levy ylhäällä, ja lamppu oikealla. Violetti virta kulkee akun plusnavasta yläjohdinta pitkin lamppuun ja alajohdinta pitkin miinusnapaan. Akun sisällä virta kulkee miinusnavalta plusnavalle. Oranssi energianuoli osoittaa akusta lamppuun. Alempi: akkua ladataan. Laturi on vasemmalla ja akku oikealla, molempien plusnapa ylhäällä. Virta kulkee laturin plusnavasta akun plusnapaan. Siksi akun sisällä virta kulkee nyt plusnavalta miinusnavalle eli päinvastaiseen suuntaan. Energianuoli osoittaa laturista akkuun." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-9-purku-lataus.webp" x="0" y="0" width="600" height="392.5" preserveAspectRatio="none"/>
  <foreignObject x="12" y="7.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Purkautuminen}$</div></foreignObject>
  <foreignObject x="24" y="101.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{akku}$</div></foreignObject>
  <foreignObject x="460" y="101.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lamppu}$</div></foreignObject>
  <foreignObject x="268" y="23.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="205" y="135.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
  <foreignObject x="12" y="199.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Lataaminen}$</div></foreignObject>
  <foreignObject x="4" y="293.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{laturi}$</div></foreignObject>
  <foreignObject x="464" y="293.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{akku}$</div></foreignObject>
  <foreignObject x="268" y="215.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="205" y="327.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
</svg>

### Akun kapasiteetti
**Akun kapasiteetti** kertoo, kuinka suuren varauksen täyteen ladattu akku pystyy siirtämään piirin läpi, ennen kuin se on tyhjä. Varaus on virta kertaa aika. Siksi kapasiteetti ilmoitetaan usein ampeeritunteina tai milliampeeritunteina. Yksi ampeeritunti on varaus, jonka virta $1\,\text{A}$ siirtää tunnissa: $1\,\text{Ah} = 1\,\text{A} \cdot 3600\,\text{s} = 3600\,\text{C}$. Kun virta on vakio, varaus on virran ja ajan kuvaajan alle jäävä pinta-ala. Kuvan akku antaa virtaa $0{,}50\,\text{A}$ neljän tunnin ajan, joten sen kapasiteetti on $2{,}0\,\text{Ah}$.

<svg data-fig="kapasiteetti" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa: purkuvirta I ampeereina ajan t funktiona tunteina. Virta on vakio 0,50 A ajan 0–4,0 h ja sen jälkeen nolla, kun akku on tyhjä. Kuvaajan ja aika-akselin väliin jäävä suorakulmio on sävytetty. Sen pinta-ala on varaus Q = It = 0,50 A · 4,0 h = 2,0 Ah." style="max-width:100%;font-size:24px">
  <line x1="169.5" y1="284" x2="169.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="247" y1="284" x2="247" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="325" y1="284" x2="325" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="402.5" y1="284" x2="402.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="284" x2="480" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="227" x2="480" y2="227" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="170" x2="480" y2="170" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="113" x2="480" y2="113" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="56" x2="480" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="284" x2="494" y2="284" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,284 L493,290 L493,278 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="285" x2="92" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,30 L98,43 L86,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="169.5" y1="284" x2="169.5" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="159.5" y="293.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="247" y1="284" x2="247" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="237" y="293.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="325" y1="284" x2="325" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="315" y="293.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="402.5" y1="284" x2="402.5" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="392.5" y="293.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="480" y1="284" x2="480" y2="291" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="470" y="293.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="85" y1="227" x2="92" y2="227" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="212.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}2$</div></foreignObject>
  <line x1="85" y1="170" x2="92" y2="170" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="155.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}4$</div></foreignObject>
  <line x1="85" y1="113" x2="92" y2="113" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="98.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}6$</div></foreignObject>
  <line x1="85" y1="56" x2="92" y2="56" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="41.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0{,}8$</div></foreignObject>
  <foreignObject x="62" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="269.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{h})$</div></foreignObject>
  <foreignObject x="82" y="-0.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{A})$</div></foreignObject>
  <polygon points="92,284 92,141.5 402.5,141.5 402.5,284" fill="#b2f2bb" fill-opacity="0.75"/>
  <polyline points="92,141.5 402.5,141.5 402.5,284 472,284" fill="none" stroke="#7048e8" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="187" y="182" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q = It$</div></foreignObject>
  <foreignObject x="172" y="216" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$= 2{,}0\,\text{Ah}$</div></foreignObject>
  <foreignObject x="197" y="105" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$0{,}50\,\text{A}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/ev-battery-cells.webp" alt="Rivissä suuria, litteitä akkukennoja. Kennon päissä on navat. Kyljessä lukee 60Ah."><figcaption>Sähköauton akun kennoja. Yhden kennon kapasiteetti on $60\,\text{Ah}$. Jännite on noin $3{,}7\,\text{V}$. Silloin yhdessä kennossa on energiaa noin $3{,}7\,\text{V} \cdot 60\,\text{Ah} \approx 220\,\text{Wh}$. Auton akussa on kymmeniä kennoja.</figcaption></figure>

### Varaus ei yksin kerro energiaa
Jännite kertoo, kuinka paljon energiaa yhtä varausyksikköä kohti muuttuu muodosta toiseen (luku *Virtapiiri, sähkövirta ja jännite*). Akun energia on siksi jännite kertaa varaus. Sen yksikkö on wattitunti: $1\,\text{V} \cdot 1\,\text{Ah} = 1\,\text{Wh} = 3600\,\text{J}$. Jännitteenä käytetään akkuun merkittyä **nimellisjännitettä**. Se on akun keskimääräinen jännite purkautumisen aikana. Tässä luvussa energiaa merkitään $W$:llä, koska $E$ on lähdejännite.

Puhelimen akun kapasiteetti on $5000\,\text{mAh}$ ja nimellisjännite $3{,}85\,\text{V}$. Se varastoi energiaa $3{,}85\,\text{V} \cdot 5{,}0\,\text{Ah} \approx 19{,}3\,\text{Wh}$. Eri jännitteisiä akkuja voi verrata vain energian avulla. Samalla ampeerituntimäärällä $12\,\text{V}$:n akkuun mahtuu yli kolme kertaa niin paljon energiaa kuin $3{,}7\,\text{V}$:n akkuun.

### Miksi lataus hidastuu lopussa
Akun lähdejännite ei ole vakio. Se kasvaa, kun akku latautuu. Latausvirtaa ajaa laturin jännitteen ja akun lähdejännitteen erotus. Kun lähdejännite kasvaa, virta pienenee. Tämä on luvun yksinkertaistettu virtapiirin malli. Todellisen litiumioniakun latausta ohjaa elektroniikka. Latauksen alussa virta voidaan pitää likimain vakiona. Akun jännitteellä on sallittu yläraja eli suurin sallittu arvo. Kun jännite saavuttaa ylärajan, ohjaus pitää jännitteen vakiona, ja latausvirta pienenee vähitellen. Siksi viimeisten prosenttien lataaminen vie enemmän aikaa. Lopuksi ohjauspiiri katkaisee virran. Akku myös lämpenee latauksessa, koska virta kulkee sen sisäisen resistanssin läpi.

## Kaava: Akun kapasiteetti ja latausvirta
Akun kapasiteetti eli varaus, jonka vakiovirta siirtää ajassa $t$:
```latex
Q = I t
```
missä $Q$ on varaus (Ah tai C), $I$ virta (A) ja $t$ aika (h tai s).

Akkuun varastoitunut energia:
```kaavat
sähkökentän tekemä työ :: W = U Q
```
missä $W$ on energia (Wh tai J), $U$ akun nimellisjännite (V) ja $Q$ akun kapasiteetti (Ah tai C).

```pysahdy
Akun kapasiteetti on $4{,}0\,\text{Ah}$ ja nimellisjännite $3{,}6\,\text{V}$. Kuinka paljon energiaa akku varastoi?
---
Energia on $W = UQ$. Lukuarvoilla $W = 3{,}6\,\text{V} \cdot 4{,}0\,\text{Ah} \approx 14\,\text{Wh}$.
```

### Latauspiiri
Kuvan yksinkertaistetussa latauspiirissä on kolme osaa. Siinä on laturi, jonka jännite on $U_\text{lat}$. Siinä on laturin ja johtojen resistanssi $R$. Siinä on myös akku, jonka lähdejännite on $E$ ja sisäinen resistanssi $R_\text{s}$. Kierretään silmukka virran suuntaan laturin miinusnavalta (luku *Kirchhoffin lait ja potentiaali virtapiirissä*). Potentiaali nousee laturissa $U_\text{lat}$:n verran. Se laskee vastuksessa $RI$ ja akun sisäisessä resistanssissa $R_\text{s} I$. Lisäksi se laskee akun lähdejännitteen $E$ verran, koska virta kulkee akun läpi plusnavalta miinusnavalle. Jännitelain mukaan $U_\text{lat} - RI - R_\text{s} I - E = 0$.

<svg data-fig="latauspiiri" viewBox="0 0 600 360" role="img" aria-label="Latauspiirin kytkentäkaavio, ei mittakaavassa. Vasemmalla on laturi, jonka jännite on U_lat ja plusnapa ylhäällä. Yläjohtimessa ovat laturin ja johtojen resistanssi R ja virtamittari A. Oikealla on akku katkoviivalla rajattuna. Sen sisällä ovat sisäinen resistanssi R_s ja lähdejännite E, jonka plusnapa on ylhäällä. Akun navat ovat katkoviivan reunalla, ja niiden väliin on kytketty jännitemittari V. Se näyttää napajännitteen U. Violetit virtanuolet kulkevat laturin plusnavasta yläjohdinta pitkin akun plusnapaan, akun läpi alaspäin ja alajohdinta pitkin takaisin laturin miinusnapaan." style="max-width:100%;font-size:24px">
  <polyline points="86,183 86,82 430,82 430,108" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="86,199 86,300 430,300 430,274" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="430,108 430,228" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="430,244 430,274" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="48" y="145" width="76" height="92" rx="8" fill="#f1dfb5" stroke="#1f2933" stroke-width="2.5"/>
  <polyline points="86,145 86,183" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="86,199 86,237" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="58" y="180" width="56" height="22" fill="#ffffff"/>
  <line x1="60" y1="183" x2="112" y2="183" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="73" y1="199" x2="99" y2="199" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="132" y="174.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U_\text{lat}$</div></foreignObject>
  <rect x="184" y="71" width="60" height="22" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="199" y="37.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <circle cx="316" cy="82" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="301" y="67.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <rect x="390" y="108" width="80" height="166" rx="6" fill="none" stroke="#6b7480" stroke-width="2" stroke-dasharray="7 6"/>
  <rect x="420" y="131" width="20" height="50" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="402" y="225" width="56" height="22" fill="#ffffff"/>
  <line x1="404" y1="228" x2="456" y2="228" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="417" y1="244" x2="443" y2="244" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <foreignObject x="332" y="141.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <foreignObject x="352" y="221.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$E$</div></foreignObject>
  <circle cx="430" cy="108" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="430" cy="274" r="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="390" y="317.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{akku}$</div></foreignObject>
  <polyline points="430,108 532,108 532,171" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="532,211 532,274 430,274" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="430" cy="108" r="4" fill="#1f2933"/>
  <circle cx="430" cy="274" r="4" fill="#1f2933"/>
  <circle cx="532" cy="191" r="20" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="517" y="176.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="558" y="142.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <path d="M160,82 L140,74 L140,90 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M390,82 L370,74 L370,90 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M250,300 L270,292 L270,308 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M430,206 L422,186 L438,186 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="138" y="41.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
</svg>

Latausvirta on siis
```latex
I = \frac{U_\text{lat} - E}{R + R_\text{s}}
```
missä $I$ on latausvirta (A), $U_\text{lat}$ laturin jännite (V), $E$ akun lähdejännite (V), $R$ laturin ja johtojen resistanssi ($\Omega$) ja $R_\text{s}$ akun sisäinen resistanssi ($\Omega$). Akku latautuu vain, kun $U_\text{lat} > E$. Jos $U_\text{lat} < E$, virta kääntyy ja akku purkautuu laturiin. Näin ei käy, jos laturissa on diodi, joka päästää virran vain yhteen suuntaan.

```pysahdy
Laturin jännite $U_\text{lat}$ on pienempi kuin akun lähdejännite $E$. Latautuuko akku?
---
Ei lataudu. Silloin $U_\text{lat} - E < 0$, joten laturi ei pysty ajamaan virtaa akun läpi latauksen suuntaan.
```

Akun napajännite on jännite akun napojen välillä. Latauksen aikana se on
```latex
U = E + R_\text{s} I
```
missä $U$ on akun napojen välinen jännite (V). Latauksessa napajännite on suurempi kuin lähdejännite. Purkautuessa se on pienempi, $U = E - R_\text{s} I$.

Kuvaajassa latauspiirin silmukka on kierretty, kun $U_\text{lat} = 4{,}5\,\text{V}$, $R = 0{,}40\,\Omega$, $E = 3{,}40\,\text{V}$ ja $R_\text{s} = 0{,}10\,\Omega$. Silloin latausvirta on $2{,}2\,\text{A}$. Laturin nousu $4{,}5\,\text{V}$ on yhtä suuri kuin laskujen $0{,}88\,\text{V}$, $0{,}22\,\text{V}$ ja $3{,}40\,\text{V}$ summa. Akun plusnavan potentiaali $3{,}62\,\text{V}$ on napajännite.

<svg data-fig="potentiaali" viewBox="0 0 600 372" role="img" aria-label="Potentiaalikuvaaja, pystyakseli mittakaavassa, vaaka-akseli kaavamainen. Latauspiirin silmukka kierretään laturin miinusnavasta A laturin, vastuksen R ja akun kautta takaisin A:han. Laturin jännite on 4,5 V, R = 0,40 ohmia, akun lähdejännite 3,40 V ja sisäinen resistanssi 0,10 ohmia, joten virta on 2,2 A. Laturissa potentiaali nousee 4,5 volttia. Vastuksessa R se laskee 0,88 V, ja akun plusnavassa B se on 3,62 V, mikä on napajännite. Akun sisäisessä resistanssissa se laskee 0,22 V arvoon 3,40 V kohdassa C. Akun lähdejännitteen kohdalla se laskee 3,40 V nollaan. Virta kulkee akun läpi plusnavalta miinusnavalle, joten potentiaali laskee akussa." style="max-width:100%;font-size:24px">
  <line x1="96" y1="245.5" x2="500" y2="245.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="204.5" x2="500" y2="204.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="164" x2="500" y2="164" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="123" x2="500" y2="123" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="82.5" x2="500" y2="82.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="286" x2="514" y2="286" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,286 L513,292 L513,280 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="287" x2="96" y2="48" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,36 L102,49 L90,49 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="89" y1="245.5" x2="96" y2="245.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="231" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="204.5" x2="96" y2="204.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="190" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="164" x2="96" y2="164" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="149.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="123" x2="96" y2="123" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="108.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="89" y1="82.5" x2="96" y2="82.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="68" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <foreignObject x="532" y="271.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kohta}$</div></foreignObject>
  <foreignObject x="86" y="5.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{V})$</div></foreignObject>
  <rect x="131.5" y="62" width="30.5" height="224" fill="#eef5f9"/>
  <foreignObject x="116.5" y="63.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U_\text{lat}$</div></foreignObject>
  <rect x="227.5" y="62" width="50.5" height="224" fill="#eef5f9"/>
  <foreignObject x="222.5" y="63.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <rect x="348.5" y="62" width="50.5" height="224" fill="#eef5f9"/>
  <foreignObject x="344" y="63.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <rect x="424" y="62" width="30.5" height="224" fill="#eef5f9"/>
  <foreignObject x="409.5" y="63.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E$</div></foreignObject>
  <line x1="97" y1="245.5" x2="500" y2="245.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="204.5" x2="500" y2="204.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="164" x2="500" y2="164" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="123" x2="500" y2="123" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="82.5" x2="500" y2="82.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="64" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="96,286 146.5,286 146.5,102.5 227.5,102.5 278,138.5 348.5,138.5 399,147.5 439.5,147.5 439.5,286 500,286" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="96" y1="286" x2="96" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="82" y="299.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <circle cx="96" cy="286" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="313" y1="286" x2="313" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="299" y="299.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B$</div></foreignObject>
  <circle cx="313" cy="138.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="419" y1="286" x2="419" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="405" y="299.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$C$</div></foreignObject>
  <circle cx="419" cy="147.5" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <line x1="500" y1="286" x2="500" y2="293" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="486" y="299.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <circle cx="500" cy="286" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="156.5" y="210.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+4{,}5\,\text{V}$</div></foreignObject>
  <foreignObject x="202.5" y="169.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-0{,}88\,\text{V}$</div></foreignObject>
  <foreignObject x="268" y="100.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$3{,}62\,\text{V}$</div></foreignObject>
  <foreignObject x="324" y="169.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-0{,}22\,\text{V}$</div></foreignObject>
  <foreignObject x="329.5" y="210.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$-3{,}40\,\text{V}$</span></div></foreignObject>
</svg>

### Energia latauksessa
Laturin teho on $P = U_\text{lat} I$ (luku *Sähköteho ja vastuksen lämpeneminen*). Vakiojännitteinen laturi antaa siis energian $W_\text{lat} = U_\text{lat} Q$, kun akun läpi kulkee varaus $Q$. Akkuun varastoituu kemiallisena energiana vain lähdejännitteen osuus. Loput muuttuvat resistanssien $R$ ja $R_\text{s}$ sisäenergiaksi, joka siirtyy lämpönä ympäristöön. Latauksen hyötysuhde on
```kaavat
hyötysuhde :: \eta = \frac{W_\text{akku}}{W_\text{lat}}
```
missä $W_\text{akku}$ on akkuun kemiallisena energiana varastoitunut energia (Wh) ja $W_\text{lat}$ laturin antama energia (Wh).

Hyötysuhde on enintään $100\,\%$. Todellisissa laitteissa se jää usein alle $100\,\%$, koska osa otetusta energiasta ei päädy hyötykäyttöön. Latauksessa näin käy aina, koska virta lämmittää resistansseja $R$ ja $R_\text{s}$. Kuvassa akku, jonka kapasiteetti on $2{,}0\,\text{Ah}$, ladataan tyhjästä täyteen $4{,}5\,\text{V}$:n laturilla. Laturi antaa $9{,}0\,\text{Wh}$, ja akkuun varastoituu $7{,}6\,\text{Wh}$. Hyötysuhde on siis noin $84\,\%$. Mitä suurempi laturin jännite on akun lähdejännitteeseen verrattuna, sitä suurempi on virta ja sitä nopeampi lataus. Silloin myös suurempi osa energiasta muuttuu sisäenergiaksi.

<svg data-fig="energia" viewBox="0 0 600 340" role="img" aria-label="Energiavirtakaavio mittakaavassa: nuolten leveys on verrannollinen energiaan. Laturi antaa täydessä latauksessa tyhjästä täyteen 9,0 Wh energiaa, kun laturin jännite on 4,5 V ja akun kapasiteetti 2,0 Ah. Siitä 7,6 Wh varastoituu akkuun kemialliseksi energiaksi ja jatkaa nuolena oikealle. Alaspäin erkanee kaksi kapeaa nuolta. Laturin ja johtojen sisäenergiaksi muuttuu 1,1 Wh ja akun sisäenergiaksi 0,3 Wh. Ne siirtyvät lämpönä ympäristöön." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-9-energia.webp" x="1.2" y="2.5" width="597" height="349.5" preserveAspectRatio="none"/>
  <foreignObject x="40" y="55.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$W_\text{lat} = 9{,}0\,\text{Wh}$</div></foreignObject>
  <foreignObject x="40" y="23.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{laturista}$</div></foreignObject>
  <foreignObject x="306" y="23.5" width="260" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\text{akkuun kemiallisena}$</div></foreignObject>
  <foreignObject x="466" y="55.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$7{,}6\,\text{Wh}$</div></foreignObject>
  <foreignObject x="133.5" y="299.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1{,}1\,\text{Wh}$</div></foreignObject>
  <foreignObject x="33.5" y="267.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{laturi ja johdot}$</div></foreignObject>
  <foreignObject x="393.5" y="299.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0{,}3\,\text{Wh}$</div></foreignObject>
  <foreignObject x="393.5" y="267.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{akku}$</div></foreignObject>
  <foreignObject x="40" y="207.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{sisäenergiaksi:}$</div></foreignObject>
</svg>

## Esimerkki
Akkukennon lähdejännite on $3{,}70\,\text{V}$ ja sisäinen resistanssi $0{,}10\,\Omega$. Kennoa ladataan laturilla, jonka jännite on $4{,}20\,\text{V}$. Laturin ja johtojen resistanssi on yhteensä $0{,}15\,\Omega$. Kuinka suuri on latausvirta, ja mikä on kennon napajännite latauksen aikana?

<!-- vaihe -->

**Tunnetut ja kysytty.** $E = 3{,}70\,\text{V}$, $R_\text{s} = 0{,}10\,\Omega$, $U_\text{lat} = 4{,}20\,\text{V}$ ja $R = 0{,}15\,\Omega$.

Kysytään latausvirtaa $I$ ja napajännitettä $U$.

<!-- vaihe -->

**Periaate.** Piirissä on yksi silmukka. Jännitelain mukaan laturin jännite on yhtä suuri kuin potentiaalin laskujen summa. Laskut ovat resistanssien jännitteet ja akun lähdejännite, koska virta kulkee akun läpi plusnavalta miinusnavalle. Napajännite on akun lähdejännite ja sen sisäisen resistanssin jännite yhteensä.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&U_\text{lat} - RI - R_\text{s} I - E = 0 \\
&I = \frac{U_\text{lat} - E}{R + R_\text{s}} \\
&U = E + R_\text{s} I
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: kaikki suureet ovat perusyksiköissä, ja $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&I = \frac{U_\text{lat} - E}{R + R_\text{s}} \\
&\phantom{I} = \frac{4{,}20\,\text{V} - 3{,}70\,\text{V}}{0{,}15\,\Omega + 0{,}10\,\Omega} \\
&\phantom{I} = \frac{0{,}50\,\text{V}}{0{,}25\,\Omega} = 2{,}0\,\text{A} \\
&U = 3{,}70\,\text{V} + 0{,}10\,\Omega \cdot 2{,}0\,\text{A} \\
&\phantom{U} = 3{,}90\,\text{V}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Latausvirta on $2{,}0\,\text{A}$. Siinä on kaksi merkitsevää numeroa, kuten jännite-erotuksessa $0{,}50\,\text{V}$ ja resistansseissa. Napajännite on $3{,}90\,\text{V}$, sadasosavoltin tarkkuudella kuten annetut jännitteet.

<!-- vaihe -->

**Järkevyys.** Laturin puolelta laskettuna napajännite on $4{,}20\,\text{V} - 0{,}15\,\Omega \cdot 2{,}0\,\text{A} = 3{,}90\,\text{V}$. Tulos on sama. Napajännite on lähdejännitteen ja laturin jännitteen välissä, kuten latauksessa pitääkin. Jos lähdejännite jätettäisiin pois, virraksi tulisi $16{,}8\,\text{A}$. Se on yli kahdeksan kertaa liikaa.

## Yleinen virhekäsitys
Moni ajattelee, että akkuun ladataan sähkövarausta ja että tyhjästä akusta varaus on loppunut. Akku on kuitenkin sähköisesti neutraali koko ajan. Ladattaessa siihen varastoituu kemiallista energiaa. Kapasiteetti kertoo, kuinka suuri varaus akun läpi voi kulkea, kun se purkautuu.

Toinen virhe on verrata akkuja pelkkien milliampeerituntien perusteella. Ampeeritunti on varauksen yksikkö, ei energian. Varavirtalähde, jossa on $10\,000\,\text{mAh}$ jännitteellä $3{,}7\,\text{V}$, sisältää vähemmän energiaa kuin kannettavan tietokoneen akku, jossa on $4000\,\text{mAh}$ jännitteellä $11{,}4\,\text{V}$: $37\,\text{Wh}$ ja $45{,}6\,\text{Wh}$. Kolmas virhe on laskea latausvirta pelkästä laturin jännitteestä. Virtaa ajaa laturin jännitteen ja akun lähdejännitteen erotus.

## Tiivistelmä
- Paristo on kertakäyttöinen ja akku ladattava. Kumpikin muuttaa kemiallista energiaa sähköenergiaksi. Akku ei varastoi varausta vaan kemiallista energiaa.
- Akun kapasiteetti on varaus $Q = It$, yleensä ampeeritunteina: $1\,\text{Ah} = 3600\,\text{C}$. Akun energia on $W = UQ$ wattitunteina, $1\,\text{Wh} = 3600\,\text{J}$. Akkuja verrataan energian perusteella.
- Ladattaessa virta kulkee akun läpi plusnavalta miinusnavalle. Latausvirta on $I = \tfrac{U_\text{lat} - E}{R + R_\text{s}}$. Akku latautuu siis vain, kun laturin jännite on suurempi kuin akun lähdejännite. Napajännite latauksessa on $U = E + R_\text{s} I$.
- Lähdejännite kasvaa, kun akku latautuu. Siksi yksinkertaistetussa mallissa vakiojännitteisellä laturilla virta pienenee ja lataus hidastuu loppua kohti. Todellisen litiumioniakun latausta ohjaa elektroniikka. Ensin virta on likimain vakio. Kun jännite on ylärajalla, virta pienenee vähitellen.
- Osa laturin energiasta muuttuu resistanssien sisäenergiaksi. Siksi latauksen hyötysuhde on alle $100\,\%$.
