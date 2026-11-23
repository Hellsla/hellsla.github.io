# Energiantuotanto ja voimalaitosten hyötysuhde

> **Miksi** lämpövoimalaitokseen tarvitaan polttoaineen energiaa noin $2{,}5$ kertaa niin paljon kuin se tuottaa sähköenergiaa? Miten loppu energia voitaisiin hyödyntää?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvinen yhteistuotantovoimalaitos. Piipusta ja voimalasta nousee höyryä. Voimalinjat vievät sähköä pois. Kaukolämpöputket kulkevat kaupunkiin: punainen putki vie kuumaa vettä ja sininen putki tuo jäähtynyttä vettä takaisin. Kerrostalojen ikkunat loistavat lämpiminä." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-15-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Voimalaitos ei tuota energiaa vaan muuttaa sitä. Polttoaineen kemiallinen energia, ydinenergia, virtaavan veden tai tuulen liike-energia ja auringon säteily muuttuvat sähköksi vaihe vaiheelta. Vaiheiden jonoa sanotaan energiaketjuksi. Energia säilyy jokaisessa vaiheessa. Osa siitä siirtyy kuitenkin lämpönä ympäristöön, eikä se ole enää sähkönä käytettävissä. Hyötysuhde kertoo, kuinka suuri osa vaiheeseen tulevasta tehosta tulee ulos hyödyllisessä muodossa.

<figure class="unit-photo"><img src="pics/fy3/iru-turbine-generator.webp" alt="Voimalaitoksen konesalissa on sininen generaattori ja turbiini. Tasolla seisoo työntekijä."><figcaption>Irun voimalaitoksen turbiini ja generaattori Virossa. Turbiini muuttaa höyryn energiaa pyörimisen liike-energiaksi. Generaattori muuttaa sen sähköenergiaksi.</figcaption></figure>

Lauhdevoimalaitoksessa ketju on polttoaine, kattila, turbiini ja lauhdutin, generaattori ja muuntaja, sähköverkko. Kattilassa polttoaineen energia siirtyy höyryyn. Osa energiasta poistuu savukaasujen mukana. Turbiinissa höyry laajenee ja pyörittää generaattoria. Lauhduttimessa höyry tiivistyy takaisin vedeksi. Lauhduttimen kautta siirtyy mereen noin puolet polttoaineen energiasta. Kuva näyttää esimerkkilaitoksen. Kaistojen leveydet on piirretty mittakaavassa.

<svg data-fig="sankey" viewBox="0 0 600 400" role="img" aria-label="Virtauskaavio (Sankey) lauhdevoimalaitoksen energiaketjusta. Polttoaineen teho 500 MW kulkee vasemmalta oikealle kaistana. Kaista kapenee vaihe vaiheelta. Kattilassa savukaasujen mukana menee 40 MW. Turbiinissa ja lauhduttimessa lämpönä mereen menee 248 MW. Generaattorissa ja muuntajassa menee 12 MW. Sähköä saadaan 200 MW eli 40 prosenttia polttoaineen tehosta. Kaistojen ja nuolten leveydet ovat mittakaavassa: 100 MW on 40 pikseliä." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-15-sankey.webp" x="0" y="1.2" width="597" height="405.5" preserveAspectRatio="none"/>
  <foreignObject x="10" y="19.5" width="320" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{polttoaine } 500\,\text{MW}$</div></foreignObject>
  <foreignObject x="330" y="19.5" width="262" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{sähkö } 200\,\text{MW}$</div></foreignObject>
  <foreignObject x="4" y="281.5" width="148" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{savukaasut}$</div></foreignObject>
  <foreignObject x="4" y="321.5" width="148" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40\,\text{MW}$</div></foreignObject>
  <foreignObject x="372" y="295.5" width="224" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lauhdutin}$</div></foreignObject>
  <foreignObject x="372" y="333.5" width="224" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$248\,\text{MW}$</div></foreignObject>
  <foreignObject x="446" y="165.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{generaattori}$</div></foreignObject>
  <foreignObject x="446" y="201.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ja muuntaja}$</div></foreignObject>
  <foreignObject x="446" y="237.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$12\,\text{MW}$</div></foreignObject>
  <foreignObject x="70" y="373.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$=100\,\text{MW}$</div></foreignObject>
</svg>

Suurin häviö ei johdu pääosin kitkasta tai huonosta tekniikasta. Suurin osa siitä on höyrykierron hukkalämpöä. Lämpövoimakone ei voi välttää sitä kokonaan. Osa lämmöstä on luovutettava kylmempään ympäristöön, kuten luvussa Kaasun tekemä työ ja lämpövoimakone nähtiin. Vesivoimala, tuulivoimala ja aurinkopaneeli eivät ole lämpövoimakoneita. Niillä ei siis ole tätä pakollista häviötä. Vesivoimalan hyötysuhde on noin $90\,\%$, tuulivoimalan $40$–$45\,\%$ ja aurinkopaneelin noin $20\,\%$. Näiden lukujen nimittäjä on kuitenkin virtaavan veden, tuulen tai säteilyn teho. Se ei ole ostettu polttoaine. Luvut eivät siis ole suoraan verrattavissa polttolaitoksen hyötysuhteeseen.

```pysahdy
Tuulivoimalan hyötysuhde on $40\,\%$, yhtä suuri kuin kuvan lauhdevoimalaitoksen. Voiko lukuja verrata suoraan?
---
Ei voi. Tuulivoimalan hyötysuhteessa verrataan tuulen tehoon eikä ostettuun polttoaineeseen. Tuulivoimala ei myöskään ole lämpövoimakone.
```

Sähkön ja lämmön yhteistuotannossa lauhduttimen lämpö johdetaan kaukolämpöverkkoon. Veden pitää lämmetä riittävästi. Siksi höyry lauhdutetaan korkeammassa lämpötilassa, ja turbiinista saadaan vähemmän sähköä. Kuvaaja näyttää esimerkkilaitoksen, jonka polttoaineteho on $400\,\text{MW}$. Kun kaukolämpöteho kasvaa, sähköteho pienenee vähän. Hukkalämpö pienenee paljon enemmän. Kuvaajassa pystysuora matka kerrosten välillä on teho. Kolmen kerroksen yhteenlaskettu korkeus on aina $400\,\text{MW}$.

<svg viewBox="0 0 600 380" role="img" aria-label="Pinottu pinta-alakuvaaja yhteistuotantolaitoksesta, jonka polttoaineteho on 400 MW. Vaaka-akselilla on kaukolämpöteho 0–250 MW ja pystyakselilla teho. Kun kaukolämpöteho kasvaa nollasta 232 MW:iin, sähköteho pienenee 160 MW:sta 120 MW:iin. Kaukolämpö kasvaa. Hukkalämpö pienenee 240 MW:sta 48 MW:iin. Kolmen kerroksen yhteenlaskettu korkeus on aina 400 MW. Kuvaaja on mittakaavassa. Sähkön ja lämmön riippuvuus on likimain suora." style="max-width:100%;font-size:24px">
  <defs><pattern id="fy315-waste" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="10" height="10" fill="#ffffff"/><line x1="0" y1="0" x2="0" y2="10" stroke="#c9c2b2" stroke-width="3"/></pattern></defs>
  <line x1="100" y1="230" x2="560" y2="230" stroke="#e3dccb" stroke-width="2"/>
  <line x1="100" y1="170" x2="560" y2="170" stroke="#e3dccb" stroke-width="2"/>
  <line x1="100" y1="110" x2="560" y2="110" stroke="#e3dccb" stroke-width="2"/>
  <line x1="100" y1="50" x2="560" y2="50" stroke="#e3dccb" stroke-width="2"/>
  <polygon points="100,194 526.9,218 526.9,290 100,290" fill="#1f2933" fill-opacity="0.18"/>
  <polygon points="100,194 526.9,218 526.9,78.8 100,194" fill="#ffc078"/>
  <polygon points="100,194 526.9,78.8 526.9,50 100,50" fill="url(#fy315-waste)"/>
  <line x1="100" y1="194" x2="526.9" y2="218" stroke="#1f2933" stroke-width="4"/>
  <line x1="100" y1="194" x2="526.9" y2="78.8" stroke="#e8590c" stroke-width="4"/>
  <line x1="100" y1="50" x2="560" y2="50" stroke="#6b7480" stroke-width="2.5" stroke-dasharray="8 6"/>
  <line x1="526.9" y1="290" x2="526.9" y2="50" stroke="#6b7480" stroke-width="2" stroke-dasharray="5 5"/>
  <circle cx="100" cy="194" r="6" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="526.9" cy="218" r="6" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="526.9" cy="78.8" r="6" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="100" y1="290" x2="578" y2="290" stroke="#1f2933" stroke-width="3"/><polygon points="590,290 576,283 576,297" fill="#1f2933"/>
  <line x1="100" y1="290" x2="100" y2="44" stroke="#1f2933" stroke-width="3"/><polygon points="100,32 93,46 107,46" fill="#1f2933"/>
  <line x1="100" y1="290" x2="100" y2="298" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="70" y="296" width="60" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$0$</div></foreignObject>
  <line x1="284" y1="290" x2="284" y2="298" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="254" y="296" width="60" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$100$</div></foreignObject>
  <line x1="468" y1="290" x2="468" y2="298" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="438" y="296" width="60" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$200$</div></foreignObject>
  <line x1="92" y1="290" x2="100" y2="290" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="92" y1="230" x2="100" y2="230" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="30" y="212" width="62" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$100$</div></foreignObject>
  <line x1="92" y1="170" x2="100" y2="170" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="30" y="152" width="62" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$200$</div></foreignObject>
  <line x1="92" y1="110" x2="100" y2="110" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="30" y="92" width="62" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$300$</div></foreignObject>
  <line x1="92" y1="50" x2="100" y2="50" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="30" y="32" width="62" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$400$</div></foreignObject>
  <foreignObject x="380" y="332" width="214" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$P_\text{k}\ (\text{MW})$</div></foreignObject>
  <foreignObject x="104" y="2" width="200" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$P\ (\text{MW})$</div></foreignObject>
  <foreignObject x="250" y="214" width="200" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{sähkö } P_\text{s}$</div></foreignObject>
  <foreignObject x="238" y="148" width="230" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{kaukolämpö } P_\text{k}$</div></foreignObject>
  <foreignObject x="180" y="64" width="220" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{hukkalämpö}$</div></foreignObject>
  <foreignObject x="312" y="8" width="280" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:right">$P_\text{o} = 400\,\text{MW}$</div></foreignObject>
</svg>

Kokonaishyötysuhde nousee yhteistuotannossa jopa 85–$90\,\%$:iin. Sähkö ja lämpö eivät kuitenkaan ole yhtä arvokkaita. Sähköä voi käyttää mihin tahansa, ja sitä voi siirtää satojen kilometrien päähän. Kaukolämpöä käytetään pääasiassa rakennusten ja käyttöveden lämmittämiseen. Sitä voidaan hyödyntää myös esimerkiksi jäähdytyksen tuottamisessa ja teollisuuden lämpöprosesseissa. Sen verkko ulottuu vain kaupunkiin. Kesällä kaukolämmön tarve on yleensä pienempi kuin talvella. Laitoksen sähkö- ja lämpötehon suhde sekä käyttö riippuvat laitostyypistä ja energiantarpeesta.

```pysahdy
Yhteistuotantolaitoksen kokonaishyötysuhde on $85\,\%$. Onko sen tuotto yhtä arvokasta kuin $85\,\%$ sähkönä?
---
Ei ole. Sähköä voi käyttää mihin tahansa ja siirtää kauas. Kaukolämpö on lähinnä rakennusten lämmitykseen, ja sen verkko ulottuu vain kaupunkiin.
```

<figure class="unit-photo"><img src="pics/fy3/nesjavellir.webp" alt="Valkoisia rakennuksia vihreässä laaksossa. Yhdestä nousee valkoinen pilvi."><figcaption>Nesjavellirin voimalaitos Islannissa tekee sähköä ja kaukolämpöä maan lämmöstä. Valkoinen pilvi on tiivistynyttä vesihöyryä. Se vie hukkalämpöä ympäristöön.</figcaption></figure>

## Kaava: Voimalaitoksen hyötysuhde
Yhden vaiheen tai koko laitoksen hyötysuhde kertoo, kuinka suuri osa sisään tuodusta energiasta saadaan hyödyksi. Hyödyksi saatu energia on antotyö, ja sisään tuotu energia on ottotyö. Sama suhde saadaan tehoista: antoteho jaetaan ottoteholla. Hukkalämmön teho on se osa ottotehosta, joka ei tule hyödyksi:
```kaavat
hyötysuhde :: \eta = \frac{W_\text{a}}{W_\text{o}} = \frac{P_\text{a}}{P_\text{o}}
```
```latex
P_\text{h} = P_\text{o} - P_\text{a}
```
Tässä $\eta$ on hyötysuhde (usein prosentteina). $W_\text{a}$ on antotyö eli hyödyksi saatu energia (J), ja $W_\text{o}$ on ottotyö eli sisään tuotu energia (J). $P_\text{a}$ on antoteho eli hyödyksi saatu teho (W). $P_\text{o}$ on ottoteho eli sisään tuotu teho, esimerkiksi polttoaineteho (W). Alaindeksi a tulee sanasta anto ja o sanasta otto. Huomaa, että $P_\text{o}$:n alaindeksi on o-kirjain, ei nolla. Lisäksi $P_\text{h}$ on hukkalämmön teho (W). Voimalaitoksessa vaiheet ovat peräkkäin, ja ketju alkaa ottotehosta $P_\text{o}$. Kunkin vaiheen ulostuleva teho on sen hyötysuhteen ja sisään tulevan tehon tulo:
```latex
\begin{aligned}
P_1 &= \eta_1 P_\text{o} \\
P_2 &= \eta_2 P_1 \\
P_3 &= \eta_3 P_2
\end{aligned}
```
Sijoita ylempi yhtälö alempaan. Näin saat koko ketjun hyötysuhteen:
```latex
\eta = \frac{P_3}{P_\text{o}} = \eta_1\,\eta_2\,\eta_3
```
Tässä $\eta_1$, $\eta_2$ ja $\eta_3$ ovat vaiheiden hyötysuhteet (kattila, höyrykierto, generaattori ja muuntaja). $P_3$ on sähköteho eli laitoksen antoteho $P_\text{a}$. Hyötysuhteet kerrotaan keskenään. Niitä ei lasketa yhteen. Todellisessa voimalaitoksessa jokainen tekijä on pienempi kuin 1. Siksi ketjun hyötysuhde on pienempi kuin heikoimman vaiheen. Kuvassa pylväät $P_1$, $P_2$ ja $P_3$ saadaan edellisestä pylväästä kertomalla se vaiheen hyötysuhteella $\eta_1$, $\eta_2$ tai $\eta_3$.

<svg viewBox="0 0 600 480" role="img" aria-label="Pylväskuvaaja siitä, miten teho pienenee energiaketjussa. Polttoaineteho P_o on 500 MW. Kattilan jälkeen P1 on 460 MW. Höyrykierron jälkeen P2 on 212 MW. Generaattorin ja muuntajan jälkeen P3 on 200 MW. Jokainen pylväs on edellistä matalampi. Pylvään päällä oleva vaalea, katkoviivalla rajattu osa on edellisessä vaiheessa hukkaan mennyt teho. Häviöt ovat kattilassa 40 MW, höyrykierrossa 248 MW ja generaattorissa ja muuntajassa 12 MW. Vaiheiden hyötysuhteet ovat 0,92, 0,46 ja 0,945. Niiden tulo on 0,40. Pylväät ovat mittakaavassa." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy315-bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></linearGradient></defs>
  <line x1="30" y1="380" x2="590" y2="380" stroke="#1f2933" stroke-width="3"/>
  <rect x="50" y="130" width="100" height="250" fill="url(#fy315-bar)"/>
  <rect x="190" y="130" width="100" height="20" fill="#ffc078" fill-opacity="0.35" stroke="#e8590c" stroke-width="2" stroke-dasharray="6 4"/>
  <rect x="190" y="150" width="100" height="230" fill="url(#fy315-bar)"/>
  <rect x="330" y="150" width="100" height="124.2" fill="#ffc078" fill-opacity="0.35" stroke="#e8590c" stroke-width="2" stroke-dasharray="6 4"/>
  <rect x="330" y="274.2" width="100" height="105.8" fill="#1f2933"/>
  <rect x="470" y="274.2" width="100" height="5.8" fill="#ffc078" fill-opacity="0.35" stroke="#e8590c" stroke-width="2" stroke-dasharray="6 4"/>
  <rect x="470" y="280" width="100" height="100" fill="#1f2933"/>
  <foreignObject x="170" y="8" width="140" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\eta_1 = 0{,}92$</div></foreignObject>
  <foreignObject x="310" y="8" width="140" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\eta_2 = 0{,}46$</div></foreignObject>
  <foreignObject x="450" y="8" width="140" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\eta_3 = 0{,}945$</div></foreignObject>
  <foreignObject x="40" y="388" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$P_\text{o}$</div></foreignObject>
  <foreignObject x="40" y="426" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$500\,\text{MW}$</div></foreignObject>
  <foreignObject x="180" y="388" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$P_1$</div></foreignObject>
  <foreignObject x="180" y="426" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$460\,\text{MW}$</div></foreignObject>
  <foreignObject x="320" y="388" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$P_2$</div></foreignObject>
  <foreignObject x="320" y="426" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$212\,\text{MW}$</div></foreignObject>
  <foreignObject x="460" y="388" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$P_3$</div></foreignObject>
  <foreignObject x="460" y="426" width="120" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$200\,\text{MW}$</div></foreignObject>
  <foreignObject x="180" y="54" width="120" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{häviö}$</div></foreignObject>
  <foreignObject x="180" y="92" width="120" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$40\,\text{MW}$</div></foreignObject>
  <foreignObject x="320" y="172" width="120" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{häviö}$</div></foreignObject>
  <foreignObject x="320" y="210" width="120" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$248\,\text{MW}$</div></foreignObject>
  <foreignObject x="460" y="196" width="120" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$\text{häviö}$</div></foreignObject>
  <foreignObject x="460" y="234" width="120" height="38"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="text-align:center">$12\,\text{MW}$</div></foreignObject>
</svg>

```pysahdy
Kolmen vaiheen hyötysuhteet ovat $0{,}90$, $0{,}40$ ja $0{,}95$. Mikä on koko ketjun hyötysuhde?
---
Hyötysuhteet kerrotaan: $\eta \approx 0{,}34$ ($0{,}90 \cdot 0{,}40 \cdot 0{,}95$) eli $34\,\%$. Se on pienempi kuin heikoimman vaiheen hyötysuhde $0{,}40$.
```

Yhteistuotantolaitoksessa hyödyksi saadaan sekä sähkö että kaukolämpö. Kokonaishyötysuhde on siis
```latex
\eta_\text{kok} = \frac{P_\text{s} + P_\text{k}}{P_\text{o}}
```
Tässä $P_\text{s}$ on sähköteho (W) ja $P_\text{k}$ on kaukolämpöteho (W). Lauhduttimen lämpö lämmittää jäähdytysvettä. Vettä virtaa massa $m$ ajassa $t$, ja sen lämpötila nousee $\Delta T$. Lämpömäärä on $Q = cm\,\Delta T$. Sen avulla lauhduttimen lämpöteho on
```latex
P_\text{L} = c\,q_m\,\Delta T
```
Tässä $P_\text{L}$ on lauhduttimesta veteen siirtyvä lämpöteho (W), $c$ on veden ominaislämpökapasiteetti ($4190\,\text{J/(kg}\cdot\text{K)}$), $q_m = m/t$ on vesivirta (kg/s) ja $\Delta T$ on veden lämpötilan nousu (K). Lauhduttimen lämpöteho on hukkalämmön suurin osa, mutta ei koko hukkalämpö $P_\text{h}$. Osa hukkalämmöstä lähtee savukaasujen mukana. Osa on generaattorin ja muuntajan häviöitä.

<svg data-fig="condenser" viewBox="0 0 600 310" role="img" aria-label="Lauhduttimen kaaviokuva. Merivesi virtaa putkessa vasemmalta oikealle lauhduttimen läpi. Veden lämpötila nousee arvosta T1 arvoon T2. Putken väri vaihtuu sinisestä punaiseen. Lauhduttimen yläosassa oleva höyry luovuttaa lämpöä veteen teholla P_L. Sitä kuvaa oranssi nuoli. Höyry tiivistyy alaosaan vedeksi. Vesivirta q_m on molemmissa päissä sama. Kaaviokuva, ei mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-15-condenser.webp" x="4.9" y="7.4" width="591.1" height="316.5" preserveAspectRatio="none"/>
  <foreignObject x="200" y="87.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{höyry}$</div></foreignObject>
  <foreignObject x="328" y="93.5" width="76" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$P_\text{L}$</div></foreignObject>
  <foreignObject x="246" y="203.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lauhde}$</div></foreignObject>
  <foreignObject x="6" y="105.5" width="184" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{merivesi sisään}$</div></foreignObject>
  <foreignObject x="30" y="189.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_1$</div></foreignObject>
  <foreignObject x="414" y="105.5" width="184" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{merivesi ulos}$</div></foreignObject>
  <foreignObject x="414" y="189.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T_2 = T_1 + \Delta T$</div></foreignObject>
  <foreignObject x="140" y="252" width="320" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$q_m = \dfrac{m}{t}$</div></foreignObject>
</svg>

## Esimerkki
Lauhdevoimalaitoksen polttoaineteho on $600\,\text{MW}$. Kattilan hyötysuhde on 0,910, höyrykierron 0,440 ja generaattorin ja muuntajan 0,950. Mikä on laitoksen sähköteho? Mikä on koko laitoksen hyötysuhde? Kuinka suuri teho siirtyy ympäristöön hukkalämpönä?

<!-- vaihe -->

**Tunnetut ja kysytty.** Polttoaineteho on $P_\text{o} = 600\,\text{MW}$. Vaiheiden hyötysuhteet ovat $\eta_1 = 0{,}910$ (kattila), $\eta_2 = 0{,}440$ (höyrykierto) ja $\eta_3 = 0{,}950$ (generaattori ja muuntaja).

Kysytään sähkötehoa $P_3$, koko ketjun hyötysuhdetta $\eta$ ja hukkalämmön tehoa $P_\text{h}$.

<!-- vaihe -->

**Periaate.** Vaiheet ovat peräkkäin. Kunkin vaiheen ulostuloteho on seuraavan vaiheen sisäänmenoteho. Kukin vaihe päästää läpi vain hyötysuhteensa verran siihen tulevasta tehosta. Laitos toimii tasaisesti ja energia säilyy. Polttoaineteho on siis joko sähköä tai lämpönä ympäristöön siirtyvää hukkaa: $P_\text{o} = P_3 + P_\text{h}$.

<!-- vaihe -->

**Kaava ratkaistuna.** Hyötysuhteet kerrotaan. Hukkalämpö on se osa, joka ei muutu sähköksi:
```latex
\begin{aligned}
P_3 &= \eta_1\,\eta_2\,\eta_3\,P_\text{o} \\
\eta &= \frac{P_3}{P_\text{o}} \\
P_\text{h} &= P_\text{o} - P_3
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Hyötysuhteet ovat dimensiottomia lukuja ja kaikki tehot ovat megawatteina. Muunnoksia ei siis tarvita. Vain hyötysuhde $\eta$ ilmoitetaan lopuksi myös prosentteina. Kerro se sadalla.

<!-- vaihe -->

**Sijoitus.** Hyötysuhteiden tulo on $0{,}910 \cdot 0{,}440 \cdot 0{,}950 = 0{,}38038$. Sähköteho on
```latex
\begin{aligned}
P_3 &= \eta_1\,\eta_2\,\eta_3\,P_\text{o} \\
&= 0{,}38038 \cdot 600\,\text{MW} \\
&= 228{,}228\,\text{MW}
\end{aligned}
```
Tästä hyötysuhde on $\eta = \tfrac{228{,}228\,\text{MW}}{600\,\text{MW}} = 0{,}38038$. Hukkalämpö on $P_\text{h} = 600\,\text{MW} - 228{,}228\,\text{MW} = 371{,}772\,\text{MW}$.

<!-- vaihe -->

**Tulos.** Sähköteho on $P_3 \approx 228\,\text{MW}$, hyötysuhde $\eta \approx 0{,}380 = 38{,}0\,\%$ ja hukkalämmön teho $P_\text{h} \approx 372\,\text{MW}$. Tulokset ilmoitetaan kolmella merkitsevällä numerolla. Hyötysuhteet $0{,}910$, $0{,}440$ ja $0{,}950$ on annettu kolmella numerolla. Polttoaineteho $600\,\text{MW}$ on annettu megawatin tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Arvio: $$\begin{aligned} &0{,}9 \cdot 0{,}45 \cdot 0{,}95 \cdot 600\,\text{MW} \\ &\approx 231\,\text{MW} \end{aligned}$$. Se vastaa tulosta. Hyötysuhde on pienempi kuin heikoimman vaiheen 0,440, kuten tulon pitääkin. Se sopii lauhdevoimalaitoksen tavalliseen noin $40\,\%$:n hyötysuhteeseen (tyypillisesti $38$–$42\,\%$). Tase täsmää: sähkö $228\,\text{MW}$ ja hukka $372\,\text{MW}$ ovat yhteensä $600\,\text{MW}$. Lauhduttimeen siirtyy teho $P_1 - P_2 = 546\,\text{MW} - 240{,}24\,\text{MW} \approx 306\,\text{MW}$. Se on yli puolet polttoaineen energiasta.

Kattilan häviö on vain $54\,\text{MW}$ ja generaattorin ja muuntajan $12\,\text{MW}$. Parannukset kannattaa siis kohdistaa höyrykiertoon ja sen jälkeen lauhduttimen lämmön käyttöön.

## Yleinen virhekäsitys
Moni ajattelee, että hukkalämpö on energiaa, joka on kadonnut. Energia ei kuitenkaan katoa. Se siirtyy esimerkiksi jäähdytysveteen tai ympäröivään ilmaan.

Lämpö voi siirtyä ympäristöön lämpötilassa, joka on vain vähän ympäristön lämpötilaa korkeampi. Silloin siitä on vaikea saada paljon mekaanista työtä tai sähköä. Mitä pienempi lämpötilaero on, sitä pienempi on lämpövoimakoneen suurin mahdollinen hyötysuhde.

Sähkön ja lämmön yhteistuotannossa osa energiasta voidaan käyttää kaukolämpönä. Muuten tämä energia siirtyisi hukkalämpönä ympäristöön.

Toinen virhe on laskea vaiheiden hyötysuhteet yhteen tai ottaa niiden keskiarvo. Kolmen vaiheen hyötysuhteet ovat 0,92, 0,46 ja 0,945. Ketjun hyötysuhde on niiden tulo 0,40, ei keskiarvo 0,78. Kolmas virhe on pitää yhteistuotannon $88\,\%$:n kokonaishyötysuhdetta merkkinä siitä, että kaikki energia olisi yhtä arvokasta. Sähköä voi käyttää kaikkeen, kaukolämpöä pääasiassa lämmitykseen.

## Tiivistelmä
- Voimalaitos muuttaa energiaa vaihe vaiheelta energiaketjussa. Jokaisessa vaiheessa osa energiasta siirtyy lämpönä ympäristöön.
- Hyötysuhde on $\eta = P_\text{a}/P_\text{o}$. Hukkalämmön teho on $P_\text{h} = P_\text{o} - P_\text{a}$.
- Ketjun hyötysuhde on vaiheiden hyötysuhteiden tulo, $\eta = \eta_1\,\eta_2\,\eta_3$. Se on pienempi kuin heikoimman vaiheen hyötysuhde.
- Lauhdevoimalaitoksen suurin häviö on höyrykierron lauhduttimeen siirtyvä lämpö. Lämpövoimakone ei voi välttää sitä kokonaan. Sähköntuotannon hyötysuhde on noin $40\,\%$ (tyypillisesti $38$–$42\,\%$).
- Yhteistuotannossa lauhduttimen lämpö johdetaan kaukolämpöverkkoon. Kokonaishyötysuhde on $\eta_\text{kok} = (P_\text{s} + P_\text{k})/P_\text{o}$, noin 85–$90\,\%$. Sähköä saadaan silloin vähemmän.
- Vesivoimala, tuulivoimala ja aurinkopaneeli eivät ole lämpövoimakoneita. Niiden hyötysuhteiden nimittäjä on virtaavan veden, tuulen tai säteilyn teho, ei ostettu polttoaine.
- Lauhduttimen jäähdytysvesi saa lämpötehon $P_\text{L} = c\,q_m\,\Delta T$. Se on hukkalämmön suurin osa.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: talvi-ilta kotona. Ikkunan alla oleva kaukolämpöpatteri lämmittää huonetta. Lämmin ilma nousee patterin yltä. Ulkona sataa lunta." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-15-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
