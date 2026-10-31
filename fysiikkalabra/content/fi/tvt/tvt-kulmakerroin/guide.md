Sovitetun suoran kulmakerroin ja vakiotermi ovat lukuja, joilla on yksikkö ja fysikaalinen merkitys. Kun vertaat suoran yhtälöä tutkimuksen malliin, saat niistä tutkittavan suureen ja tietoa mittauksen onnistumisesta.

## Mihin tarvitset tätä

Kulmakertoimesta saat tutkittavan suureen esimerkiksi tutkimuksissa *Jousivakion määrittäminen* ja *Putoamiskiihtyvyyden määrittäminen heilurin avulla*. Vakiotermi kertoo esimerkiksi tutkimuksessa *Valaistusvoimakkuuden riippuvuus etäisyydestä*, jäikö mittaukseen taustavaloa. Ennen tätä tarvitset [[ohje:tvt-suoran-sovitus|mittauspisteisiin sovitetun suoran]].

## Työvaiheet

1. **Valitse suoralta kaksi kaukana toisistaan olevaa pistettä.** Lue pisteiden $(x_1, y_1)$ ja $(x_2, y_2)$ koordinaatit sovitetulta suoralta, ei mittauspisteistä. Valitse pisteet lähelle mittausalueen päitä: mitä kauempana ne ovat toisistaan, sitä vähemmän lukemisen epätarkkuus vaikuttaa tulokseen. Graphical Analysis Pro laskee kulmakertoimen sovituksesta puolestasi, mutta kahden pisteen laskulla tarkistat sen ja ymmärrät, mistä luku tulee.

2. **Laske kulmakerroin.** Kulmakerroin on

    $$k = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$

    missä $\Delta y$ on pystyakselin suureen muutos ja $\Delta x$ vaaka-akselin suureen muutos pisteiden välillä. Tässä $\Delta$ tarkoittaa muutosta, ei epävarmuutta. Lue muutokset akselien asteikoilta suureiden arvoina, älä ruutuina tai senttimetreinä paperilla.

    <svg data-fig="slope" viewBox="0 0 600 340" role="img" aria-label="Kaaviokuva ilman lukuarvoja: mittauspisteet ja niihin sovitettu suora. Suoralta on valittu kaksi kaukana toisistaan olevaa pistettä, joiden koordinaatit x yksi, y yksi ja x kaksi, y kaksi on merkitty akseleille. Pisteiden välissä on suorakulmainen kolmio: vaakasivu on delta x ja pystysivu delta y. Kulmakerroin k on delta y jaettuna delta x:llä. Suoran ja pystyakselin leikkauskohta on merkitty vakiotermiksi b." style="max-width:100%;font-size:24px">
  <line x1="89" y1="290" x2="474" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M486,290 L473,296 L473,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="291" x2="90" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,44 L96,57 L84,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="492" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <foreignObject x="80" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$y$</div></foreignObject>
  <line x1="172" y1="229" x2="172" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="90" y1="229" x2="172" y2="229" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="419" y1="105" x2="419" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="90" y1="105" x2="419" y2="105" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <polyline points="90,270 460,84" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="131" cy="255" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="213.5" cy="196" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="262.5" cy="189" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="316" cy="164" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="365.5" cy="120" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="443.5" cy="97.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="172" y1="229" x2="419" y2="229" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="419" y1="229" x2="419" y2="105" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="172" cy="229" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="419" cy="105" r="7" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="90" cy="270" r="6" fill="#1f2933"/>
  <foreignObject x="155.5" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_1$</div></foreignObject>
  <foreignObject x="402.5" y="299.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$x_2$</div></foreignObject>
  <foreignObject x="45" y="214.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$y_1$</div></foreignObject>
  <foreignObject x="45" y="90.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$y_2$</div></foreignObject>
  <foreignObject x="58" y="255.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$b$</div></foreignObject>
  <foreignObject x="279" y="234.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\Delta x$</div></foreignObject>
  <foreignObject x="429" y="152.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\Delta y$</div></foreignObject>
  <foreignObject x="168" y="114.5" width="58" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$k = \dfrac{\Delta y}{\Delta x}$</div></foreignObject>
</svg>

3. **Lue kertoimet sovituksen tulosruudusta.** Kun olet sovittanut suoran valinnoilla **Käyrän sovitus** ja **Lineaarinen** ([[ohje:tvt-suoran-sovitus|Suoran sovittaminen mittauspisteisiin]]), tulosruudussa ovat kulmakerroin ja vakiotermi. Graphical Analysis kirjoittaa suoran muotoon y = mx + b: ohjelman m on kulmakerroin $k$ ja b vakiotermi $b$. Ohjelma käyttää desimaalipistettä. Kuvan esimerkkiarvoista m: 1.671 g/cm3 kirjoitetaan raporttiin $k = 1{,}671\,\text{g/cm}^3$. Kertoimet näkyvät yksiköineen, kun sarakkeille on annettu yksiköt; jos yksiköitä ei näy, asetus voi olla tulosruudun rattaan kuvakkeen takana (englanninkielisessä versiossa **Show units in linear fit parameters**). Tarkista silti itse, että kulmakertoimen yksikkö on pystyakselin yksikkö jaettuna vaaka-akselin yksiköllä.

    <figure class="shot"><img src="pics/tvt/ga-tulosruutu.png" alt="Suoran sovituksen tulosruutu, jonka otsikko on LINEAARINEN. Siinä lukee x alue 0 - 50 cm3, y = mx + b, m: 1.671 g/cm3, b: -1.619 g, r: 0.9961 ja RMSE: 3.078. Oikeassa alakulmassa on rattaan kuvake." width="288" height="280" loading="lazy"><figcaption>Kuvakaappaus: Graphical Analysis (suomenkielinen käyttöliittymä); esimerkkiarvoja.</figcaption></figure>

4. **Lue vakiotermi.** Vakiotermi $b$ on suoran ja pystyakselin leikkauskohta eli pystyakselin suureen arvo, kun vaaka-akselin suure on nolla. Jos luet suoraa käsin ja vaaka-akseli ei ala nollasta, laske vakiotermi yhdestä suoran pisteestä: $b = y_1 - kx_1$.

5. **Merkitse yksiköt.** Kulmakertoimen yksikkö on pystyakselin yksikkö jaettuna vaaka-akselin yksiköllä. Jos pystyakselilla on $F\ (\text{N})$ ja vaaka-akselilla $x\ (\text{m})$, kulmakertoimen yksikkö on $\text{N/m}$. Kun pystyakselilla on $T^2\ (\text{s}^2)$ ja vaaka-akselilla $l\ (\text{m})$, yksikkö on $\text{s}^2/\text{m}$. Vakiotermin yksikkö on sama kuin pystyakselin suureen.

6. **Vertaa suoran yhtälöä malliin.** Kirjoita malli suoran yhtälön $y = kx + b$ muotoon ja katso, mikä mallin osa on kulmakertoimen paikalla.

    - Jousivoiman laki $F = kx$: kulmakerroin on suoraan jousivakio.
    - Heilurin malli $T^2 = \tfrac{4\pi^2}{g} \cdot l$: kulmakerroin on $k = \tfrac{4\pi^2}{g}$, joten putoamiskiihtyvyys on $g = \tfrac{4\pi^2}{k}$.

    Esimerkiksi jos keksityn esimerkkiaineiston suoran kulmakerroin on $k = 4{,}05\,\text{s}^2/\text{m}$, putoamiskiihtyvyys on $g = 4\pi^2 : 4{,}05\,\text{s}^2/\text{m} \approx 9{,}75\,\text{m/s}^2$. Yksikkö tarkistaa laskun: $1 : (\text{s}^2/\text{m}) = \text{m/s}^2$.

7. **Tulkitse vakiotermi.** Mieti mallin avulla, mikä pystyakselin suureen arvon pitäisi olla, kun vaaka-akselin suure on nolla. Nollasta selvästi poikkeavalla vakiotermillä on yleensä jokin näistä syistä:

    - **Nollakohdan virhe eli systemaattinen siirtymä.** Jos heilurin pituus mitataan kuulan yläpintaan eikä keskipisteeseen, jokainen pituus on säteen verran liian lyhyt. Suora siirtyy, ja vakiotermi on positiivinen, mutta kulmakerroin ei muutu.
    - **Epäjohdonmukainen mittaustapa.** Tutkimuksessa *Jousivakion määrittäminen* suoraan tulee vakiotermi, jos jousen pituus ilman kuormaa mitataan ilman punnustelinettä mutta telineen massaa ei lasketa venyttävään voimaan.
    - **Todellinen fysikaalinen termi.** Joskus mallissa kuuluu olla vakiotermi. Jousen värähdysajan neliö massan funktiona ei kulje tarkasti origon kautta, koska jousen oma massa värähtelee osittain mukana.

    Jos vakiotermi on epävarmuuksien rajoissa nolla, mittaukset ovat sopusoinnussa origon kautta kulkevan mallin kanssa.

## Tavallisimmat virheet

- **Kulmakerroin on laskettu kahdesta mittauspisteestä.** Tulos riippuu siitä, mitkä pisteet valitsit, ja sisältää niiden satunnaiset virheet. Käytä sovituksen kulmakerrointa tai lue pisteet sovitetulta suoralta.
- **Valitut pisteet ovat lähellä toisiaan.** Pieni lukemisvirhe muuttaa kulmakerrointa paljon. Valitse pisteet mittausalueen päistä.
- **Kulmakertoimen yksikkö puuttuu tai on väärä.** Huomaat sen, kun lopputuloksen yksikkö ei täsmää, esimerkiksi putoamiskiihtyvyydelle tulee yksiköksi $\text{s}^2/\text{m}$. Muodosta yksikkö akselien yksiköistä tai näytä yksiköt sovituksen tulosruudussa, ja kuljeta yksikkö laskun läpi.
- **Kulmakerroin on sekoitettu tutkittavaan suureeseen.** Heilurin kuvaajan kulmakerroin ei ole $g$ vaan $\tfrac{4\pi^2}{g}$. Vertaa aina suoran yhtälöä malliin.
- **Vakiotermi on jätetty huomiotta.** Selvästi nollasta poikkeava vakiotermi kertoo jotakin mittauksesta. Kerro raportissa, mistä se voi johtua.

## Tarkista ennen kuin jatkat

- Kulmakerroin on luettu suoralta kaukana toisistaan olevista pisteistä tai saatu sovituksesta.
- Kulmakertoimella ja vakiotermillä on yksiköt.
- Tiedät mallin avulla, mitä kulmakerroin ja vakiotermi tarkoittavat.
