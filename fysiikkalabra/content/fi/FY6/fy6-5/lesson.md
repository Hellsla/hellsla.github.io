# Kirchhoffin lait ja potentiaali virtapiirissä

> **Miksi** lintu voi istua paljaalla suurjännitejohdolla vahingoittumatta, vaikka johdossa kulkee satojen ampeerien virta?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: suurjännitelinja peltomaiseman yllä kesäpäivänä. Kahden ristikkopylvään välissä riippuu johtimet, ja yhdellä johtimella istuu rivissä neljä pikkulintua. Taustalla on metsän reuna ja kumpuileva pelto." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-5-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Virta ei kulu: Kirchhoffin virtalaki
Sähkövirta on varausten liikettä. Varausta ei synny eikä häviä, eikä sitä kerry johtimiin, kun virrat pysyvät vakioina. Siksi kaikki varaus, joka tulee **haarautumispisteeseen** eli kohtaan, jossa johdin jakautuu haaroiksi, myös lähtee siitä. **Haarautumispisteeseen tulevien virtojen summa on yhtä suuri kuin siitä lähtevien virtojen summa.** Tämä on Kirchhoffin virtalaki. Samasta syystä virta on yhtä suuri vastuksen kummallakin puolella: vastuksessa sähköenergiaa muuttuu vastuksen sisäenergiaksi, joka siirtyy lämpönä ympäristöön, mutta virta ei kulu siinä.

Rinnakkaisten haarojen yli on sama jännite (luku *Vastusten sarja- ja rinnankytkennät*), joten Ohmin lain mukaan pienemmän resistanssin haaraan kulkee suurempi virta. Kuvassa $30\,\Omega$:n haaran virta on kaksinkertainen $60\,\Omega$:n haaraan verrattuna, ja haarojen virrat $0{,}20\,\text{A}$ ja $0{,}10\,\text{A}$ ovat yhteensä yhtä suuret kuin tuleva virta $0{,}30\,\text{A}$.

<svg data-fig="junction" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva haarautumispisteestä, ei mittakaavassa. Vasemmalta johdinta pitkin tulee virta I1 = 0,30 A haarautumispisteeseen. Siitä lähtee kaksi haaraa: ylähaarassa on 30 ohmin vastus ja alahaarassa 60 ohmin vastus, ja haarat yhtyvät oikealla uudelleen. Violettien virtanuolten leveys on verrannollinen virtaan: ylähaarassa I2 = 0,20 A, alahaarassa I3 = 0,10 A, ja yhteensä haaroista lähtee yhtä paljon virtaa kuin pisteeseen tulee, 0,30 A." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-5-junction.webp" x="0" y="-1.2" width="600" height="337.5" preserveAspectRatio="none"/>
  <foreignObject x="351" y="91.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30\,\Omega$</div></foreignObject>
  <foreignObject x="351" y="219.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60\,\Omega$</div></foreignObject>
  <foreignObject x="15" y="93.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1 = 0{,}30\,\text{A}$</div></foreignObject>
  <foreignObject x="334" y="27.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_2 = 0{,}20\,\text{A}$</div></foreignObject>
  <foreignObject x="334" y="283.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_3 = 0{,}10\,\text{A}$</div></foreignObject>
  <foreignObject x="216" y="155.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{haarautumispiste}$</div></foreignObject>
</svg>

```pysahdy
Haarautumispisteeseen tulee virta $0{,}80\,\text{A}$, ja se jakautuu kahteen haaraan. Voiko virta olla kummassakin haarassa $0{,}50\,\text{A}$? Miksi tai miksi ei?
---
Ei voi. Virtalain mukaan lähtevät virrat ovat yhteensä $0{,}80\,\text{A}$, mutta $0{,}50\,\text{A} + 0{,}50\,\text{A} = 1{,}00\,\text{A}$.
```

### Potentiaali: jokaisen kohdan sähköinen taso
Virtapiirin jokaisella kohdalla on **potentiaali** $V$: kohdan jännite valittuun nollakohtaan nähden. Nollakohdaksi valitaan usein jännitelähteen miinusnapa tai maadoitus, ja sen potentiaali on $0\,\text{V}$. Kahden kohdan välinen jännite on niiden potentiaalien erotus. Potentiaalia voi verrata korkeuteen: korkeus riippuu siitä, mistä se mitataan, mutta kahden kohdan korkeusero ei riipu. Samoin nollakohdan siirtäminen muuttaa kaikkia potentiaaleja yhtä paljon, mutta jännitteet pysyvät ennallaan.

Potentiaali muuttuu vain lähteessä ja vastuksissa. Lähteessä se nousee miinusnavalta plusnavalle lähteen jännitteen verran; lähde on tässä luvussa ideaalinen, eli sen oman resistanssin vaikutus jätetään huomiotta. Vastuksessa se laskee virran suuntaan jännitteen $U = RI$ verran. Johtimen resistanssi on niin pieni, että sen jännite jätetään huomiotta, joten saman johtimen kaikissa kohdissa on sama potentiaali. Kuvan piirissä pisteet $B$ ja $C$ ovat samaa johdinta, joten molempien potentiaali on $6{,}0\,\text{V}$.

<svg data-fig="circuit" viewBox="0 0 600 368" role="img" aria-label="Kytkentäkaavio, ei mittakaavassa: jännitelähde 9,0 V, sen plusnavalta vastus R1 = 10 ohmia ja sen jälkeen kaksi rinnakkaista vastusta R2 = 30 ohmia ja R3 = 60 ohmia, jotka palaavat lähteen miinusnapaan. Johtimiin on merkitty pisteet A–F ja niiden potentiaalit, kun lähteen miinusnapa on nollakohta: A 9,0 V, B ja C 6,0 V sekä D, E ja F 0 V. Saman johtimen kaikissa kohdissa potentiaali on sama; se muuttuu vain lähteessä ja vastuksissa." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-5-circuit.webp" x="0" y="0" width="600" height="377.5" preserveAspectRatio="none"/>
  <foreignObject x="26" y="152.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="26" y="192.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="111" y="170.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U = 9{,}0\,\text{V}$</div></foreignObject>
  <foreignObject x="126" y="111.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1 = 10\,\Omega$</div></foreignObject>
  <foreignObject x="352" y="152.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <foreignObject x="352" y="188.5" width="64" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$30\,\Omega$</div></foreignObject>
  <foreignObject x="492" y="152.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_3$</div></foreignObject>
  <foreignObject x="492" y="188.5" width="64" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$60\,\Omega$</div></foreignObject>
  <foreignObject x="98" y="51.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="72" y="19.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$9{,}0\,\text{V}$</div></foreignObject>
  <foreignObject x="272" y="51.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B$</div></foreignObject>
  <foreignObject x="246" y="19.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$6{,}0\,\text{V}$</div></foreignObject>
  <foreignObject x="456" y="51.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$C$</div></foreignObject>
  <foreignObject x="430" y="19.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$6{,}0\,\text{V}$</div></foreignObject>
  <foreignObject x="456" y="289.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$D$</div></foreignObject>
  <foreignObject x="430" y="321.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$0\,\text{V}$</div></foreignObject>
  <foreignObject x="316" y="289.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="290" y="321.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$0\,\text{V}$</div></foreignObject>
  <foreignObject x="98" y="289.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F$</div></foreignObject>
  <foreignObject x="72" y="321.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$0\,\text{V}$</div></foreignObject>
</svg>

```pysahdy
Kaksi kohtaa on saman paljaan johtimen päissä, eikä niiden välissä ole vastusta. Kuinka suuri on niiden välinen jännite ja miksi?
---
Se on likimain nolla. Johtimen resistanssi on häviävän pieni, joten potentiaali ei muutu sen matkalla.
```

### Kierros silmukassa: Kirchhoffin jännitelaki
**Silmukka** on virtapiirin suljettu reitti, joka palaa lähtökohtaansa. Kun silmukka kierretään, potentiaali palaa samaan arvoon, josta lähdettiin. Siksi **potentiaalin nousujen ja laskujen summa silmukassa on nolla**. Tämä on Kirchhoffin jännitelaki. Yhden silmukan piirissä lähteen jännite on yhtä suuri kuin vastusten jännitteiden summa. Energian kannalta jännite kertoo, kuinka paljon energiaa yhtä varausyksikköä kohti muuttuu muodosta toiseen (luku *Virtapiiri, sähkövirta ja jännite*): varaus saa lähteessä energiaa ja luovuttaa saman määrän vastuksissa.

Kuvan piirissä on kaksi silmukkaa, joista toinen kulkee vastuksen $R_2$ ja toinen vastuksen $R_3$ kautta. Kummassakin lähteen $9{,}0\,\text{V}$ jakautuu vastuksen $R_1$ jännitteeseen $3{,}0\,\text{V}$ ja haaran jännitteeseen $6{,}0\,\text{V}$. Siksi rinnakkaisten haarojen yli on sama jännite.

### Lintu johdolla
Linnun jalat ovat saman johtimen kahdessa kohdassa vain muutaman senttimetrin päässä toisistaan. Lintu on rinnakkainen haara jalkojen välissä olevalle johtimen pätkälle, jonka resistanssi on häviävän pieni. Siksi jalkojen välinen jännite on vain millivoltteja, ja Ohmin lain mukaan linnun kautta kulkee häviävän pieni virta. Virtalain mukaan lähes koko virta jatkaa siis johdinta pitkin. Linnun potentiaali maahan nähden on suuri, mutta vaara syntyisi vasta, jos se koskettaisi samalla toista johdinta tai pylvästä, joiden potentiaali on eri. Ihmiselle tilanne ei ole vertailukelpoinen: suurjännitejohtoa ei saa lähestyä, koska valokaari voi syntyä jo ilman kosketusta.

<figure class="unit-photo"><img src="pics/fy6/swallows-power-line.webp" alt="Kaksi haarapääskyä istuu ilmajohdolla sinistä taivasta vasten."><figcaption>Haarapääskyt ilmajohdolla. Kuvan johto on eristetty kaapeli, mutta linnut istuvat samoin myös paljailla johdoilla: molemmat jalat ovat saman johtimen kahdessa lähekkäisessä kohdassa.</figcaption></figure>

## Kaava: Kirchhoffin lait
Kirchhoffin virtalaki haarautumispisteelle:
```kaavat
Kirchhoffin 1. laki :: \sum I_\text{tulevat} = \sum I_\text{lähtevät}
```
missä $I_\text{tulevat}$ ovat haarautumispisteeseen tulevat virrat (A) ja $I_\text{lähtevät}$ siitä lähtevät virrat (A). Kahteen haaraan jakautuvalle virralle $I_1 = I_2 + I_3$.

Kohtien $A$ ja $B$ välinen jännite on potentiaalien erotus:
```kaavat
kahden pisteen välinen jännite :: U_{AB} = V_A - V_B
```
missä $U_{AB}$ on jännite (V) ja $V_A$ ja $V_B$ ovat kohtien potentiaalit (V) samaan nollakohtaan nähden. Jännite on positiivinen, kun $A$ on korkeammassa potentiaalissa.

Kirchhoffin jännitelaki silmukalle:
```kaavat
Kirchhoffin 2. laki :: \sum \Delta V = 0
```
missä $\Delta V$ (V) on potentiaalin muutos silmukan kussakin osassa, kun silmukka kierretään kerran. Lähteessä miinusnavalta plusnavalle $\Delta V = +U$, vastuksessa virran suuntaan $\Delta V = -RI$ ja johtimessa $\Delta V = 0$. Yhden silmukan piirissä, jossa on kaksi vastusta, laki antaa $U - R_1 I - R_2 I = 0$ eli $U = R_1 I + R_2 I$.

```pysahdy
Yhden silmukan piirissä vastukset ovat $R_1 = 20\,\Omega$ ja $R_2 = 10\,\Omega$. Kuinka monta kertaa suurempi on vastuksen $R_1$ jännite kuin vastuksen $R_2$ jännite ja miksi?
---
Kaksi kertaa suurempi. Molempien läpi kulkee sama virta $I$, joten kaavan $U = RI$ mukaan jännite on verrannollinen resistanssiin. Jännitteet muodostavat yhdessä lähteen jännitteen, $U = R_1 I + R_2 I$.
```

**Potentiaalikuvaaja** näyttää potentiaalin silmukan eri kohdissa. Kuvaajassa kierretään pisteillä $A$–$F$ merkityn piirin silmukka miinusnavasta $F$ vastusten $R_1$ ja $R_2$ kautta takaisin pisteeseen $F$. Lähteen nousu $+9{,}0\,\text{V}$ on yhtä suuri kuin vastusten laskujen $-3{,}0\,\text{V}$ ja $-6{,}0\,\text{V}$ yhteismäärä, ja johtimissa kuvaaja on vaakasuora.

<svg data-fig="potential-graph" viewBox="0 0 600 360" role="img" aria-label="Potentiaalikuvaaja, pystyakseli mittakaavassa, vaaka-akseli kaavamainen: potentiaali V volteissa, kun kierretään kuvan virtapiirin silmukka lähteen miinusnavasta F lähteen ja vastusten R1 ja R2 kautta takaisin F:ään. Lähteessä potentiaali nousee 0 voltista 9,0 volttiin. Johdinta pitkin pisteeseen A se pysyy 9,0 voltissa, vastuksessa R1 se laskee 3,0 V arvoon 6,0 V pisteessä B ja vastuksessa R2 6,0 V nollaan pisteessä E. Pisteestä E pisteeseen F potentiaali pysyy nollassa. Nousujen ja laskujen summa on nolla." style="max-width:100%;font-size:24px">
  <line x1="96" y1="230" x2="500" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="170" x2="500" y2="170" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="110" x2="500" y2="110" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="514" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,290 L513,296 L513,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,44 L102,57 L90,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="89" y1="230" x2="96" y2="230" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="215.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="170" x2="96" y2="170" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="89" y1="110" x2="96" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="95.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$9$</div></foreignObject>
  <foreignObject x="532" y="275.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kohta}$</div></foreignObject>
  <foreignObject x="86" y="13.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{V})$</div></foreignObject>
  <rect x="127.5" y="70" width="27" height="220" fill="#eef5f9"/>
  <foreignObject x="119" y="71.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U$</div></foreignObject>
  <rect x="230.5" y="70" width="45" height="220" fill="#eef5f9"/>
  <foreignObject x="231" y="71.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1$</div></foreignObject>
  <rect x="365.5" y="70" width="45" height="220" fill="#eef5f9"/>
  <foreignObject x="366" y="71.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <line x1="97" y1="230" x2="500" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="170" x2="500" y2="170" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="110" x2="500" y2="110" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="64" y="269.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="96,290 141,290 141,110 186,110 230.5,110 275.5,170 320.5,170 365.5,170 410,290 455,290 500,290" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="96" y1="290" x2="96" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="82" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F$</div></foreignObject>
  <line x1="186" y1="290" x2="186" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="172" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <line x1="320.5" y1="290" x2="320.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="306.5" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B$</div></foreignObject>
  <line x1="455" y1="290" x2="455" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="441" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E$</div></foreignObject>
  <line x1="500" y1="290" x2="500" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="486" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F$</div></foreignObject>
  <circle cx="96" cy="290" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="186" cy="110" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="320.5" cy="170" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="455" cy="290" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="500" cy="290" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="149" y="185.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+9{,}0\,\text{V}$</div></foreignObject>
  <foreignObject x="283.5" y="125.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-3{,}0\,\text{V}$</div></foreignObject>
  <foreignObject x="418" y="215.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-6{,}0\,\text{V}$</div></foreignObject>
</svg>

## Esimerkki
Jännitelähteen jännite on $12\,\text{V}$. Lähteen plusnavasta virta kulkee vastuksen $R_1 = 20\,\Omega$ kautta haarautumispisteeseen $B$, josta lähtee kaksi rinnakkaista haaraa: vastus $R_2 = 60\,\Omega$ ja vastus $R_3 = 30\,\Omega$. Haarat palaavat lähteen miinusnapaan, joka on nollakohta. Mikä on pisteen $B$ potentiaali, ja kuinka suuri virta kulkee vastuksen $R_3$ kautta?

<!-- vaihe -->

**Tunnetut ja kysytty.** $U = 12\,\text{V}$, $R_1 = 20\,\Omega$, $R_2 = 60\,\Omega$, $R_3 = 30\,\Omega$ ja miinusnavan potentiaali $0\,\text{V}$.

Kysytään pisteen $B$ potentiaalia $V_B$ ja virtaa $I_3$.

<!-- vaihe -->

**Periaate.** Koko virta $I_1$ kulkee lähteen ja vastuksen $R_1$ kautta. Rinnakkaiset vastukset korvataan yhdellä vastuksella $R_{23}$, jolloin Ohmin laki antaa $I_1$. Jännitelain mukaan potentiaali laskee plusnavan arvosta $U$ vastuksessa $R_1$ jännitteen $R_1 I_1$ verran. Vastus $R_3$ on pisteen $B$ ja nollakohdan välissä, joten sen jännite on $V_B$.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&\frac{1}{R_{23}} = \frac{1}{R_2} + \frac{1}{R_3} \\
&I_1 = \frac{U}{R_1 + R_{23}} \\
&V_B = U - R_1 I_1 \\
&I_3 = \frac{V_B}{R_3}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: kaikki suureet ovat perusyksiköissä, ja $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&\frac{1}{R_{23}} = \frac{1}{60\,\Omega} + \frac{1}{30\,\Omega} \\
&R_{23} = 20\,\Omega \\
&I_1 = \frac{12\,\text{V}}{20\,\Omega + 20\,\Omega} = 0{,}30\,\text{A} \\
&V_B = 12\,\text{V} - 20\,\Omega \cdot 0{,}30\,\text{A} \\
&\phantom{V_B} = 6{,}0\,\text{V} \\
&I_3 = \frac{6{,}0\,\text{V}}{30\,\Omega} = 0{,}20\,\text{A}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Pisteen $B$ potentiaali on $6{,}0\,\text{V}$, ja vastuksen $R_3$ kautta kulkee virta $0{,}20\,\text{A}$. Tulokset ilmoitetaan kahdella merkitsevällä numerolla kuten resistanssit.

<!-- vaihe -->

**Järkevyys.** Vastuksen $R_2$ kautta kulkee $6{,}0\,\text{V} : 60\,\Omega = 0{,}10\,\text{A}$, ja haarojen virrat ovat yhteensä $0{,}30\,\text{A}$ kuten virtalaki vaatii. Silmukassa $12\,\text{V} - 6{,}0\,\text{V} - 6{,}0\,\text{V} = 0$, kuten jännitelaki vaatii. Pienemmän resistanssin haaraan kulkee suurempi virta, kuten pitääkin.

## Yleinen virhekäsitys
Moni ajattelee, että vastus kuluttaa virtaa, joten virta olisi vastuksen jälkeen pienempi kuin ennen sitä. Vastus muuttaa sähköenergiaa sisäenergiaksi, mutta varauksia ei katoa: virtamittari näyttää vastuksen kummallakin puolella saman lukeman. Vastuksessa pienenee potentiaali, ei virta.

Toinen yleinen virhe on käyttää haaran virran laskemisessa koko lähteen jännitettä. Jos $30\,\Omega$:n haaran virta laskettaisiin virheellisesti jännitteestä $9{,}0\,\text{V}$, saataisiin $0{,}30\,\text{A}$. Haaran todellinen jännite on kuitenkin $6{,}0\,\text{V}$, joten $I_2 = 0{,}20\,\text{A}$. Toisessa haarassa $I_3 = 6{,}0\,\text{V} : 60\,\Omega = 0{,}10\,\text{A}$. Kirchhoffin virtalaki toteutuu: $0{,}20\,\text{A} + 0{,}10\,\text{A} = 0{,}30\,\text{A}$. Kolmas virhe on ajatella, että jännite on jonkin kohdan ominaisuus: jännite on aina kahden kohdan välinen potentiaaliero.

## Tiivistelmä
- Kirchhoffin virtalaki: haarautumispisteeseen tulevien virtojen summa on yhtä suuri kuin siitä lähtevien virtojen summa, koska varaus säilyy. Virta ei kulu vastuksessa.
- Potentiaali $V$ on kohdan jännite nollakohtaan nähden. Jännite on potentiaaliero $U_{AB} = V_A - V_B$, eikä se riipu nollakohdan valinnasta.
- Potentiaali nousee lähteessä miinusnavalta plusnavalle, laskee vastuksessa virran suuntaan $RI$:n verran ja pysyy johtimessa samana.
- Kirchhoffin jännitelaki: silmukan potentiaalin muutosten summa on nolla, $\sum \Delta V = 0$. Siksi lähteen jännite jakautuu silmukan vastuksille, ja rinnakkaisten haarojen yli on sama jännite.
