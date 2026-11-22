# Vastusten sarja- ja rinnankytkennät

> **Miksi** vanhan jouluvalosarjan kaikki lamput sammuvat, kun yksi lamppu rikkoutuu, mutta kotona lattiavalaisin palaa edelleen, vaikka pöytävalaisin sammutetaan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: olohuone talvi-iltana. Ikkunan yläreunassa roikkuu vanha jouluvalosarja, jonka kaikki lamput ovat pimeinä, koska yksi lamppu on rikki ja roikkuu irti kannastaan. Saman jatkojohdon pistorasioihin kytketyt lattiavalaisin ja pöytävalaisin palavat kirkkaasti." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-4-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Virtapiirissä on usein useampi kuin yksi vastus tai lamppu. Kaksi vastusta voidaan kytkeä paristoon kahdella tavalla: peräkkäin samaan silmukkaan eli sarjaan tai eri haaroihin samojen kahden pisteen väliin eli rinnan. Kytkentätapa ratkaisee, miten virta ja jännite jakautuvat vastusten kesken ja kuinka suuri virta paristosta lähtee. Tässä luvussa paristo on ihanteellinen eli sen napojen välinen jännite ei riipu virrasta, ja johtimien resistanssi jätetään huomiotta.

### Sarjaankytkentä
Sarjaankytkennässä vastukset ovat peräkkäin, ja varauksilla on vain yksi kulkureitti. Siksi sama virta $I$ kulkee jokaisen vastuksen läpi. Virta ei kulu vastuksessa: varausta ei katoa eikä kasaannu mihinkään piirin kohtaan. Vastuksen jännite kertoo, kuinka paljon kunkin varauksen sähköistä energiaa muuttuu siinä vastuksen sisäenergiaksi, joka siirtyy lämpönä ympäristöön. Pariston jännite jakautuu vastusten kesken, $U = U_1 + U_2$. Ohmin lain mukaan $U_1 = R_1 I$ ja $U_2 = R_2 I$, joten suuremman resistanssin yli on suurempi jännite.

<svg data-fig="series" viewBox="0 0 600 344" role="img" aria-label="Kytkentäkaavio, ei mittakaavassa: paristo ja kaksi vastusta R1 ja R2 sarjassa samassa silmukassa. Violetit virtanuolet kulkevat pariston plusnavasta R1:n ja R2:n kautta takaisin miinusnapaan, ja jokaisen nuolen merkintä on sama I. Sinisillä hakasilla merkityt jännitteet U1 ja U2 ovat vastusten yli, ja pariston jännite on U." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-4-series.webp" x="0" y="0" width="600" height="355" preserveAspectRatio="none"/>
  <foreignObject x="30" y="143.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="30" y="187.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="126" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="229.5" y="39.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1$</div></foreignObject>
  <foreignObject x="229.5" y="137.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$U_1$</div></foreignObject>
  <foreignObject x="389.5" y="39.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <foreignObject x="389.5" y="137.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$U_2$</div></foreignObject>
  <foreignObject x="138" y="37.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="316" y="37.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="556" y="165.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="296" y="289.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="233.5" y="171.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\text{sama virta } I$</div></foreignObject>
</svg>

Jos sarjaan kytketty komponentti katkeaa, esimerkiksi lampun hehkulanka palaa poikki, ainoa kulkureitti aukeaa ja virta lakkaa kulkemasta koko piirissä. Siksi vanhanmallisen jouluvalosarjan kaikki lamput sammuvat, kun yksi niistä rikkoutuu.

```pysahdy
Sarjaankytketyistä vastuksista ensimmäisen läpi kulkee $0{,}20\,\text{A}$. Kuinka suuri virta kulkee toisen vastuksen läpi ja miksi?
---
Yhtä suuri, $0{,}20\,\text{A}$. Kulkureittejä on vain yksi, eikä varausta katoa tai kasaannu mihinkään.
```

### Rinnankytkentä
Rinnankytkennässä vastukset ovat eri haaroissa samojen kahden haarautumispisteen välissä. Kummankin haaran päät on yhdistetty johtimilla pariston napoihin, joten kummankin vastuksen yli on sama jännite $U$. Haarautumispisteessä virta jakautuu, ja toisessa haarautumispisteessä haaravirrat yhdistyvät taas: paristosta lähtevä virta on haaravirtojen summa, $I = I_1 + I_2$. Ohmin lain mukaan haaravirta on $I_1 = U : R_1$, joten pienemmän resistanssin haarassa kulkee suurempi virta.

<svg data-fig="parallel" viewBox="0 0 600 404" role="img" aria-label="Kytkentäkaavio, ei mittakaavassa: paristo ja kaksi vastusta R1 ja R2 rinnan. Pariston plusnavasta lähtevä virta I jakautuu haarautumispisteessä kahteen haaraan, joissa kulkevat virrat I1 ja I2, ja virrat yhdistyvät taas toisessa haarautumispisteessä. Kummankin vastuksen yli on sama jännite U kuin pariston napojen välillä." style="max-width:100%;font-size:24px">
  <path d="M86,182 L86,86 L476,86 L476,306 L86,306 L86,210" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M236,86 L236,196 L476,196" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="56" y="182" width="60" height="28" fill="#ffffff"/>
  <line x1="58" y1="188" x2="114" y2="188" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="73" y1="204" x2="99" y2="204" stroke="#1f2933" stroke-width="8" stroke-linecap="butt"/>
  <foreignObject x="30" y="159.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="30" y="203.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="126" y="181.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <circle cx="236" cy="86" r="5.5" fill="#1f2933"/>
  <circle cx="476" cy="196" r="5.5" fill="#1f2933"/>
  <rect x="318" y="72" width="76" height="28" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="339.5" y="33.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1$</div></foreignObject>
  <rect x="318" y="182" width="76" height="28" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="339.5" y="145.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <line x1="132" y1="70" x2="167" y2="70" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M180,70 L166,76.5 L166,63.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="146" y="31.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <line x1="408" y1="70" x2="439" y2="70" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M452,70 L438,76.5 L438,63.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="413.5" y="31.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1$</div></foreignObject>
  <line x1="408" y1="180" x2="439" y2="180" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M452,180 L438,186.5 L438,173.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="413.5" y="141.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_2$</div></foreignObject>
  <line x1="330" y1="324" x2="295" y2="324" stroke="#7048e8" stroke-width="3" stroke-linecap="butt"/>
  <path d="M282,324 L296,317.5 L296,330.5 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="296" y="333.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="308.5" y="241.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I = I_1 + I_2$</div></foreignObject>
  <foreignObject x="65" y="369.5" width="470" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\text{sama jännite } U \text{ kummankin vastuksen yli}$</div></foreignObject>
</svg>

Uusi rinnakkainen haara ei muuta muiden haarojen virtoja, koska niiden jännite pysyy samana. Se tuo piiriin lisää kulkureittejä, joten paristosta lähtevä virta kasvaa. Kotien valaisimet ja pistorasiat on kytketty rinnan: jokainen laite saa saman verkkojännitteen, ja yhden laitteen sammuttaminen katkaisee vain sen oman haaran.

<figure class="unit-photo"><img src="pics/fy6/christmas-lights.webp" alt="Omakotitalo illalla. Räystäällä, puussa ja pihalla palaa satoja pieniä valoja."><figcaption>Jouluvaloja omakotitalon pihalla. Pitkässä valosarjassa on kymmeniä lamppuja, ja kytkentätapa ratkaisee, mitä tapahtuu, kun yksi niistä rikkoutuu.</figcaption></figure>

### Kokonaisresistanssi
Vastusten kytkentä voidaan korvata yhdellä vastuksella, josta paristo antaa saman virran. Tämän vastuksen resistanssi on kytkennän kokonaisresistanssi $R$: sille pätee $U = RI$, missä $I$ on paristosta lähtevä virta. Sarjaankytkennässä varaukset kulkevat jokaisen vastuksen läpi, joten kokonaisresistanssi on suurempi kuin yksikään vastuksista. Rinnankytkennässä jokainen haara on uusi kulkureitti, joten kokonaisresistanssi on pienempi kuin pienin haarojen resistansseista.

```pysahdy
Vastukset $10\,\Omega$ ja $1000\,\Omega$ kytketään rinnan. Onko kokonaisresistanssi suurempi vai pienempi kuin $10\,\Omega$?
---
Pienempi, koska jokainen haara on uusi kulkureitti. Rinnankytkennän kokonaisresistanssi on aina pienempi kuin pienin haarojen resistansseista.
```

## Kaava: Vastusten kokonaisresistanssi
Sarjaankytkennässä jännitteet summautuvat, $U = U_1 + U_2$, ja jokaisessa vastuksessa kulkee sama virta $I$. Kun jännitteet kirjoitetaan Ohmin lain avulla, saadaan $RI = R_1 I + R_2 I$, ja virta $I$ supistuu pois. Sarjaan kytkettyjen vastusten kokonaisresistanssi on siis
```kaavat
sarjaan kytkettyjen vastusten kokonaisresistanssi :: R = R_1 + R_2 + R_3 + \dots
```
missä $R$ on kokonaisresistanssi ($\Omega$) ja $R_1$, $R_2$, $R_3$, … ovat vastusten resistanssit ($\Omega$).

Rinnankytkennässä virrat summautuvat, $I = I_1 + I_2$, ja jokaisen vastuksen yli on sama jännite $U$. Kun virrat kirjoitetaan Ohmin lain avulla, saadaan $\tfrac{U}{R} = \tfrac{U}{R_1} + \tfrac{U}{R_2}$, ja jännite $U$ supistuu pois. Rinnan kytkettyjen vastusten kokonaisresistanssille pätee
```kaavat
rinnan kytkettyjen vastusten kokonaisresistanssi :: \frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots
```
missä $R$ on kokonaisresistanssi ja $R_1$, $R_2$, $R_3$, … ovat haarojen resistanssit. Yhtälöstä saadaan ensin luku $\tfrac{1}{R}$, jonka yksikkö on $\tfrac{1}{\Omega}$. Kokonaisresistanssi on sen käänteisluku, joten laskun lopuksi on muistettava kääntää. Kahdelle rinnakkaiselle vastukselle yhtälön voi ratkaista valmiiksi:
```latex
R = \frac{R_1 R_2}{R_1 + R_2}
```
Kun kaksi yhtä suurta vastusta kytketään rinnan, kokonaisresistanssi on puolet yhden vastuksen resistanssista.

Kuvaajassa vastus $R_1 = 100\,\Omega$ pysyy samana ja $R_2$ muuttuu. Sarjaankytkennän kokonaisresistanssi kasvaa yhtä paljon kuin $R_2$ ja on aina yli $100\,\Omega$. Rinnankytkennän kokonaisresistanssi jää aina pienemmäksi kuin kumpikaan vastuksista; kun $R_2 = 100\,\Omega$, se on $50\,\Omega$.

<svg data-fig="graph" viewBox="0 0 600 352" role="img" aria-label="Kuvaaja mittakaavassa: kokonaisresistanssi R ohmeina vastuksen R2 funktiona, kun toinen vastus R1 on 100 ohmia. Sarjaankytkennän suora nousee 100 ohmista 300 ohmiin, kun R2 kasvaa nollasta 200 ohmiin. Rinnankytkennän käyrä nousee nollasta noin 67 ohmiin ja pysyy aina 100 ohmin katkoviivan alapuolella; kohdassa R2 = 100 ohmia se on 50 ohmia." style="max-width:100%;font-size:24px">
  <line x1="192" y1="300" x2="192" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="288" y1="300" x2="288" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384" y1="300" x2="384" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="300" x2="480" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="260.5" x2="480" y2="260.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="221.5" x2="480" y2="221.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="182" x2="480" y2="182" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="142.5" x2="480" y2="142.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="103.5" x2="480" y2="103.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="64" x2="480" y2="64" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="300" x2="494" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M506,300 L493,306 L493,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="301" x2="96" y2="50" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,38 L102,51 L90,51 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="192" y1="300" x2="192" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="175.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="288" y1="300" x2="288" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="265.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="384" y1="300" x2="384" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="361.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="480" y1="300" x2="480" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="457.5" y="309.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="89" y1="260.5" x2="96" y2="260.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="246" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="89" y1="221.5" x2="96" y2="221.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="207" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="89" y1="182" x2="96" y2="182" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="167.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="89" y1="142.5" x2="96" y2="142.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="128" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="89" y1="103.5" x2="96" y2="103.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="89" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$250$</div></foreignObject>
  <line x1="89" y1="64" x2="96" y2="64" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="49.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$300$</div></foreignObject>
  <foreignObject x="66" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="512" y="285.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_2\ (\Omega)$</div></foreignObject>
  <foreignObject x="86" y="7.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R\ (\Omega)$</div></foreignObject>
  <line x1="96" y1="221.5" x2="480" y2="221.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="96,221.5 480,64" fill="none" stroke="#2f74b5" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,300 99,298.5 102.5,297.5 105.5,296.5 109,295 112,294 115,293 118.5,292 121.5,290.5 125,289.5 128,289 131,288 134.5,287 137.5,286 141,285 144,284.5 147,283.5 150.5,282.5 153.5,282 157,281 160,280.5 163,279.5 166.5,279 169.5,278 173,277.5 176,277 179,276 182.5,275.5 185.5,275 189,274.5 192,274 195,273 198.5,272.5 201.5,272 205,271.5 208,271 211,270.5 214.5,270 217.5,269.5 221,269 224,268.5 227,268 230.5,267.5 233.5,267 237,266.5 240,266.5 243,266 246.5,265.5 249.5,265 253,264.5 256,264 259,264 262.5,263.5 265.5,263 269,262.5 272,262.5 275,262 278.5,261.5 281.5,261.5 285,261 288,260.5 291,260.5 294.5,260 297.5,259.5 301,259.5 304,259 307,259 310.5,258.5 313.5,258 317,258 320,257.5 323,257.5 326.5,257 329.5,257 333,256.5 336,256.5 339,256 342.5,256 345.5,255.5 349,255.5 352,255 355,255 358.5,254.5 361.5,254.5 365,254 368,254 371,253.5 374.5,253.5 377.5,253 381,253 384,253 387,252.5 390.5,252.5 393.5,252 397,252 400,252 403,251.5 406.5,251.5 409.5,251 413,251 416,251 419,250.5 422.5,250.5 425.5,250.5 429,250 432,250 435,250 438.5,249.5 441.5,249.5 445,249.5 448,249 451,249 454.5,249 457.5,248.5 461,248.5 464,248.5 467,248 470.5,248 473.5,248 477,247.5 480,247.5" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="288" cy="142.5" r="6.5" fill="#2f74b5" stroke="#ffffff" stroke-width="2"/>
  <circle cx="288" cy="260.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="308" y="56" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2f74b5">$\text{sarjaan}$</div></foreignObject>
  <foreignObject x="490" y="233" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$\text{rinnan}$</div></foreignObject>
  <foreignObject x="406" y="207" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$R_1$</span></div></foreignObject>
</svg>

```pysahdy
Vastukset $12\,\Omega$ ja $4{,}0\,\Omega$ kytketään rinnan. Kuinka suuri on kokonaisresistanssi?
---
Kaavan $R = \tfrac{R_1 R_2}{R_1 + R_2}$ mukaan $R = \tfrac{12\,\Omega \cdot 4{,}0\,\Omega}{16\,\Omega}$, joten $R = 3{,}0\,\Omega$. Tulos on pienempi kuin $4{,}0\,\Omega$, kuten pitääkin.
```

### Sekakytkentä
Monessa piirissä on sekä sarjaan että rinnan kytkettyjä vastuksia. Ratkaisu etenee vaiheittain, sisältä ulospäin:

1. Korvaa rinnakkaiset vastukset $R_2$ ja $R_3$ yhdellä vastuksella $R_{23}$ rinnankytkennän kaavalla.
2. Vastus $R_1$ on sarjassa sen kanssa, joten kokonaisresistanssi on $R = R_1 + R_{23}$.
3. Paristosta lähtevä virta on $I = U : R$. Se kulkee sekä $R_1$:n että rinnakkaisosan läpi.
4. Sarjaosien jännitteet saadaan Ohmin laista: $U_1 = R_1 I$ ja $U_{23} = R_{23} I$. Ne summautuvat pariston jännitteeksi.
5. Jännite $U_{23}$ on sama kummankin rinnakkaisen vastuksen yli, joten haaravirrat ovat $I_2 = U_{23} : R_2$ ja $I_3 = U_{23} : R_3$. Ne summautuvat virraksi $I$.

<svg data-fig="mixed" viewBox="0 0 600 340" role="img" aria-label="Kaksi kytkentäkaaviota vierekkäin, ei mittakaavassa. Vasemmalla paristoon on kytketty vastus R1 ja sen kanssa sarjaan kahden rinnakkaisen vastuksen R2 ja R3 ryhmä. Oikealla sama kytkentä, jossa rinnakkaiset vastukset on korvattu yhdellä vastuksella R23, joka on sarjassa R1:n kanssa." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-4-mixed.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="16" y="148.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="16" y="192.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="114" y="170.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="96.5" y="35.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1$</div></foreignObject>
  <foreignObject x="199.5" y="35.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <foreignObject x="199.5" y="211.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_3$</div></foreignObject>
  <foreignObject x="312" y="148.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="312" y="192.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="402" y="170.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="392.5" y="35.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1$</div></foreignObject>
  <foreignObject x="497" y="170.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R_{23}$</div></foreignObject>
  <foreignObject x="40" y="303.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_2 \text{ ja } R_3 \text{ rinnan}$</div></foreignObject>
  <foreignObject x="340" y="303.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R = R_1 + R_{23}$</div></foreignObject>
</svg>

## Esimerkki
Kaksi vastusta, $R_1 = 120\,\Omega$ ja $R_2 = 60\,\Omega$, kytketään rinnan $9{,}0\,\text{V}$:n paristoon. Kuinka suuri virta paristosta lähtee? Paristoa pidetään ihanteellisena, ja johtimien resistanssi jätetään huomiotta.

<!-- vaihe -->

**Tunnetut ja kysytty.** $R_1 = 120\,\Omega$, $R_2 = 60\,\Omega$ ja $U = 9{,}0\,\text{V}$.

Kysytään paristosta lähtevää virtaa $I$.

<!-- vaihe -->

**Periaate.** Vastukset ovat rinnan, joten kummankin yli on pariston jännite. Kytkentä voidaan korvata kokonaisresistanssilla $R$, jolloin Ohmin laki antaa paristosta lähtevän virran $I = U : R$.

<!-- vaihe -->

**Kaava ratkaistuna.** Ratkaistaan rinnankytkennän yhtälöstä $R$ ja sen avulla virta $I$:
```latex
\begin{aligned}
&\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2} \\[4pt]
&R = \frac{R_1 R_2}{R_1 + R_2} \\[4pt]
&I = \frac{U}{R}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: resistanssit ovat ohmeina ja jännite voltteina, ja $\tfrac{\text{V}}{\Omega} = \text{A}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
R &= \frac{120\,\Omega \cdot 60\,\Omega}{120\,\Omega + 60\,\Omega} \\
&= 40\,\Omega \\[6pt]
I &= \frac{9{,}0\,\text{V}}{40\,\Omega} \\
&= 0{,}225\,\text{A}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Paristosta lähtee virta $0{,}23\,\text{A}$ eli noin $230\,\text{mA}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla kuten jännite $9{,}0\,\text{V}$.

<!-- vaihe -->

**Järkevyys.** Haaravirroista saadaan sama tulos: $9{,}0\,\text{V} : 120\,\Omega = 0{,}075\,\text{A}$ ja $9{,}0\,\text{V} : 60\,\Omega = 0{,}15\,\text{A}$, yhteensä $0{,}225\,\text{A}$. Kokonaisresistanssi $40\,\Omega$ on pienempi kuin pienempi vastuksista, $60\,\Omega$, kuten rinnankytkennässä pitääkin.

## Yleinen virhekäsitys
Moni ajattelee, että virta kuluu vastuksessa, jolloin sarjaankytkennän ensimmäinen vastus saisi eniten virtaa ja seuraaville jäisi vähemmän. Kun $10\,\Omega$:n ja $20\,\Omega$:n vastukset kytketään sarjaan $6{,}0\,\text{V}$:n paristoon, kummankin läpi kulkee kuitenkin sama virta $0{,}20\,\text{A}$. Vastuksessa ei häviä varausta, vaan varausten sähköistä energiaa muuttuu sisäenergiaksi, ja lampussa myös valoksi.

Toinen yleinen virhe on ajatella, että jokainen lisätty vastus suurentaa kokonaisresistanssia. Se pitää paikkansa vain sarjaankytkennässä. Rinnan lisätty vastus avaa uuden kulkureitin, joten kokonaisresistanssi pienenee ja paristosta lähtevä virta kasvaa.

## Tiivistelmä
- Sarjaankytkennässä sama virta kulkee jokaisen vastuksen läpi, jännitteet summautuvat, $U = U_1 + U_2$, ja kokonaisresistanssi on $R = R_1 + R_2 + \dots$
- Rinnankytkennässä jokaisen haaran yli on sama jännite, virrat summautuvat, $I = I_1 + I_2$, ja $\tfrac{1}{R} = \tfrac{1}{R_1} + \tfrac{1}{R_2} + \dots$. Kokonaisresistanssi on pienempi kuin pienin haarojen resistansseista.
- Sarjaan kytketyn komponentin katkeaminen katkaisee virran koko piiristä, rinnakkaisen haaran katkeaminen vain siitä haarasta.
- Sekakytkennän kokonaisresistanssi lasketaan vaiheittain: ensin rinnakkaiset osat, sitten sarjaan kytketyt.
