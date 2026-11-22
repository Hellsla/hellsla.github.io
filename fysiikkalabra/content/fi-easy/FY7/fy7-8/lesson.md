# Muuntaja ja sähköenergian siirto

> **Miksi** sähkö kuljetetaan voimalaitokselta kaupunkiin $400\,\text{kV}$:n jännitteellä, vaikka kodin pistorasiassa jännite on vain $230\,\text{V}$?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: vasemmalla joen varrella on voimalaitos ja sen muuntaja. Muuntajasta lähtee pitkä voimajohto. Suuret ristikkopylväät kantavat johtimia peltojen ja metsän yli. Oikealla kaukana näkyy kaupunki, jonka ikkunoissa palaa valo." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-8-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Muuntaja muuttaa vaihtojännitettä
Muuntajassa on suljettu rautasydän. Sen ympärille on kierretty kaksi käämiä. Käämi on lankakela. **Ensiökäämiin** kytketään vaihtojännite. **Toisiokäämistä** saadaan jännite laitteelle. Käämit eivät kosketa toisiaan. Niiden välillä ei kulje virtaa johtimia pitkin.

Ensiökäämin vaihtovirta synnyttää rautasydämeen magneettikentän. Kentän suuruus ja suunta vaihtelevat virran tahdissa. Rautasydän ohjaa lähes koko magneettivuon kiertämään sydäntä pitkin. Vuo kulkee siis myös toisiokäämin läpi. Luvussa *Sähkömagneettinen induktio* nähtiin, että muuttuva magneettivuo indusoi käämiin jännitteen. Siksi toisiokäämiin syntyy vaihtojännite. Sen taajuus on sama kuin ensiöjännitteen.

<svg data-fig="transformer" viewBox="0 0 600 360" role="img" aria-label="Periaatekuva muuntajasta, ei mittakaavassa. Rautasydän on suljettu. Sen vasempaan haaraan on kierretty ensiökäämi, jossa on enemmän kierroksia. Oikeaan haaraan on kierretty toisiokäämi, jossa on vähemmän kierroksia. Ensiökäämi on kytketty vaihtojännitelähteeseen, jonka jännite on U1. Toisiokäämi on kytketty lamppuun, jonka jännite on U2. Vihreä katkoviiva nuolineen kiertää rautasydämen sisällä. Ensiövirta synnyttää muuttuvan magneettivuon. Vuo kulkee sydäntä pitkin myös toisiokäämin läpi." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-8-transformer.webp" x="1.2" y="1.2" width="597" height="368.2" preserveAspectRatio="none"/>
  <foreignObject x="290" y="19.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\Phi$</div></foreignObject>
  <foreignObject x="-6" y="165.5" width="46" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$U_1$</div></foreignObject>
  <foreignObject x="528.5" y="217.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U_2$</div></foreignObject>
  <foreignObject x="81.5" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1$</div></foreignObject>
  <foreignObject x="487.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_2$</div></foreignObject>
  <foreignObject x="222" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$N_1$</div></foreignObject>
  <foreignObject x="345" y="165.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$N_2$</div></foreignObject>
  <foreignObject x="83.5" y="317.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ensiökäämi}$</div></foreignObject>
  <foreignObject x="233.5" y="317.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rautasydän}$</div></foreignObject>
  <foreignObject x="377.5" y="317.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{toisiokäämi}$</div></foreignObject>
</svg>

### Kierrosten lukumäärä määrää jännitteen
Sama muuttuva magneettivuo kulkee kummankin käämin jokaisen kierroksen läpi. Siksi jokaiseen kierrokseen indusoituu yhtä suuri jännite. Käämin jännite on sen kierrosten jännitteiden summa. Jännite on siis verrannollinen kierrosten lukumäärään.

Ideaalisessa muuntajassa ensiöjännitteen ja toisiojännitteen suhde on sama kuin käämien kierrosten lukumäärien suhde. Tätä suhdetta sanotaan **muuntosuhteeksi**. Jos toisiokäämissä on enemmän kierroksia kuin ensiökäämissä, muuntaja nostaa jännitettä. Jos toisiokäämissä on vähemmän kierroksia, muuntaja laskee jännitettä.

### Muuntaja tarvitsee muuttuvan magneettivuon
Toisiokäämiin syntyy jännite vain, kun sen läpi kulkeva magneettivuo muuttuu. Oletetaan, että ensiökäämi kytketään akkuun. Silloin käämissä kulkee vakiosuuruinen tasavirta, ja rautasydämen magneettikenttä on vakio. Vakiosuuruinen magneettivuo ei indusoi jännitettä. Toisiokäämin jännite on siis nolla. Jännitepulssi syntyy vain hetkellä, jolloin virta kytketään tai katkaistaan, koska silloin vuo muuttuu.

Tämän vuoksi sähköverkossa käytetään vaihtovirtaa. Luvussa *Generaattori ja vaihtovirta* generaattori tuottaa vaihtojännitettä. Muuntajilla jännite voidaan muuttaa aina sopivan suuruiseksi.

```pysahdy
Ensiökäämi on kytketty paristoon. Kytkin on ollut pitkään kiinni. Mikä on toisiokäämin jännite, kun ensiökäämin virta pysyy samana?
---
Toisiokäämin jännite on nolla. Tasainen virta antaa tasaisen magneettivuon. Tasainen vuo ei indusoi jännitettä.
```

### Teho säilyy, virta muuttuu
Ideaalinen muuntaja ei kuluta energiaa. Siksi ensiökäämiin tuleva teho on yhtä suuri kuin toisiokäämistä lähtevä teho. Kun kuorma on resistiivinen, teho on jännitteen ja virran tulo. Kun muuntaja nostaa jännitteen kymmenkertaiseksi, virta pienenee kymmenesosaan.

Muuntaja ei siis lisää energiaa eikä tehoa. Se vaihtaa suuren virran suureksi jännitteeksi tai päinvastoin. Todellisessa muuntajassa osa energiasta muuttuu sisäenergiaksi käämien resistanssissa ja rautasydämen pyörrevirroissa. Siksi sydän kootaan ohuista levyistä, jotka on eristetty toisistaan (luku *Lenzin laki ja pyörrevirrat*). Suurten voimalaitosmuuntajien hyötysuhde on yli $99\,\%$.

### Siirtohäviö ja suurjännite
Voimajohdolla on resistanssi. Johdossa kulkeva virta lämmittää johtoa. Osa siirrettävästä energiasta muuttuu johdon sisäenergiaksi. Se siirtyy lämpönä ympäristöön. Tämä häviöteho on verrannollinen virran neliöön. Siksi virta kannattaa pitää pienenä.

Saman tehon voi siirtää suurella jännitteellä ja pienellä virralla. Kun jännite nostetaan kymmenkertaiseksi, virta pienenee kymmenesosaan ja häviöteho sadasosaan. Siksi voimalaitoksen generaattorin jännite nostetaan muuntajalla **suurjännitteeksi**. Fingrid ylläpitää Suomen kantaverkkoa. Kantaverkon jännitteet ovat $400\,\text{kV}$, $220\,\text{kV}$ ja $110\,\text{kV}$. Kantaverkon häviöt vastaavat noin $2\,\%$:a Suomessa käytetystä sähköstä (Fingrid, *Yhteisillä linjoilla* 2026, vuoden 2025 tiedot).

<svg data-fig="grid" viewBox="0 0 640 372" role="img" aria-label="Kaavakuva sähköverkosta yksiviivaesityksenä, ei mittakaavassa. Todellisissa kolmivaiheisissa johdoissa on kolme vaihejohdinta. Ylärivillä voimalaitoksen generaattorin jännite 20 kV nostetaan muuntajalla 400 kilovoltiksi. Kantaverkon suuret pylväät vievät sähkön sähköasemalle. Sähköasemalla muuntaja laskee jännitteen. Alarivillä jakeluverkon pienet pylväät vievät 20 kV:n jännitteen muuntamolle. Muuntamo laskee jännitteen pienjänniteverkon jännitteeksi. Kotien pistorasioissa on 230 volttia." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-8-grid.webp" x="0" y="0" width="640" height="382.7" preserveAspectRatio="none"/>
  <foreignObject x="89" y="103.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20\,\text{kV}$</div></foreignObject>
  <foreignObject x="275" y="29.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400\,\text{kV}$</div></foreignObject>
  <foreignObject x="252.5" y="181.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kantaverkko}$</div></foreignObject>
  <foreignObject x="496" y="183.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{sähköasema}$</div></foreignObject>
  <foreignObject x="307" y="239.5" width="86" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20\,\text{kV}$</div></foreignObject>
  <foreignObject x="271" y="335.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{jakeluverkko}$</div></foreignObject>
  <foreignObject x="160" y="233.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{muuntamo}$</div></foreignObject>
  <foreignObject x="51" y="197.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$230\,\text{V}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/transformer-750kv.webp" alt="Iso vaalea muuntaja nurmella. Taustalla on sähköaseman rakenteita ja johtoja."><figcaption>Muuntaja, jonka suurempi jännite on $750\,\text{kV}$. Johdoissa häviää tehoa $P = RI^2$. Kun jännite on suuri, johdoissa kulkee pieni virta. Silloin johdoissa häviää vähän tehoa.</figcaption></figure>

### Jännite lasketaan vaiheittain
Sähköasemilla muuntajat laskevat jännitteen alueverkon $110\,\text{kV}$:iin ja jakeluverkon $20\,\text{kV}$:iin. Asuinalueen muuntamossa on jakelumuuntaja. Se laskee esimerkiksi $20\,\text{kV}$:n jännitteen pienjänniteverkon jännitteeksi. Pienjänniteverkossa vaihejohtimien välillä on noin $400\,\text{V}$. Vaihejohtimen ja nollajohtimen välillä on noin $230\,\text{V}$. Se on kodin pistorasian jännite. Suurjännitettä ei tuoda koteihin. Sen eristäminen vaatii pitkiä eristimiä ja suuria etäisyyksiä, ja kosketus olisi hengenvaarallinen (luku *Sähköturvallisuus kotona ja työssä*).

Puhelimen laturi laskee jännitteen vielä noin $5\,\text{V}$:iin. Nykyaikainen laturi muuttaa verkkojännitteen ensin hyvin suuritaajuiseksi. Silloin muuntaja voi olla pieni. Lopuksi laturi tasasuuntaa jännitteen. Laturin muuntajan käämit eivät kosketa toisiaan. Puhelin ei siis ole johtavassa yhteydessä sähköverkkoon.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: pieni puhelimen laturi on kytketty seinäpistorasiaan. Laturin johto vie pöydällä olevaan puhelimeen, joka latautuu." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-8-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>

## Kaava: Muuntaja ja siirtohäviö
Ideaalisen muuntajan jännitteet ja virrat riippuvat käämien kierrosten lukumääristä:
```kaavat
muuntaja :: \frac{U_1}{U_2} = \frac{N_1}{N_2} = \frac{I_2}{I_1}
```
Tässä $U_1$ on ensiöjännite (V) ja $U_2$ on toisiojännite (V). Kirjaimet $N_1$ ja $N_2$ ovat ensiökäämin ja toisiokäämin kierrosten lukumäärät. Kirjaimet $I_1$ ja $I_2$ ovat ensiövirta ja toisiovirta (A). Suhde $N_1 : N_2$ on muuntosuhde. Viimeinen yhtäsuuruus seuraa tehon säilymisestä: $U_1 I_1 = U_2 I_2$. Jännitteet ja virrat ovat tehollisia arvoja (luku *Generaattori ja vaihtovirta*). Kun jännite kasvaa, virta pienenee samassa suhteessa.

```pysahdy
Muuntajan ensiökäämissä on $460$ kierrosta, ja sen jännite on $230\,\text{V}$. Toisiokäämissä on $40$ kierrosta. Mikä on toisiojännite, kun muuntaja on ideaalinen?
---
Jännitteet ovat samassa suhteessa kuin kierrosluvut. Siis $U_2 = U_1 \cdot \tfrac{N_2}{N_1} = 230\,\text{V} \cdot \tfrac{40}{460} = 20{,}0\,\text{V}$.
```

### Siirtojohdon tehohäviö
Sähkönsiirtoa kuvataan ensin yksinkertaistetulla kaksijohtimisella virtapiirillä. Siinä virta kulkee perille yhtä johdinta pitkin ja palaa toista pitkin. Voimalaitos lähettää tehon $P$ jännitteellä $U$. Johdon virta ja johdossa sisäenergiaksi muuttuva teho ovat
```latex
\begin{aligned}
&P = U I \\
&P_\text{h} = R I^2 = \frac{R P^2}{U^2}
\end{aligned}
```
Tässä $P$ on siirrettävä teho (W), $U$ on siirtojännite (V) ja $I$ on johdon virta (A). Kirjain $R$ on kummankin johtimen yhteenlaskettu resistanssi (Ω) ja $P_\text{h}$ on häviöteho (W). Kun sama teho siirretään kaksinkertaisella jännitteellä, virta puolittuu ja häviöteho pienenee neljäsosaan.

Siirtojännite $U$ ei ole sama kuin jännite johdon resistanssin yli. Johdon päiden välinen jännitehäviö on vain $R I$. Siksi häviötehoa ei saa laskea lausekkeella $U^2 : R$.

<svg data-fig="loss-graph" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa: siirtojohdossa sisäenergiaksi muuttuvan tehon osuus siirretystä tehosta prosentteina. Osuus on siirtojännitteen funktio, ja jännite on kilovoltteina. Siirretty teho on 200 MW ja johdon resistanssi 6,0 ohmia yksinkertaistetussa kaksijohtimisessa mallissa. Käyrä laskee jyrkästi. Jännitteellä 100 kV osuus on 12 %, jännitteellä 200 kV 3,0 % ja jännitteellä 400 kV 0,75 %. Kun jännite kaksinkertaistuu, osuus pienenee neljäsosaan." style="max-width:100%;font-size:24px">
  <line x1="143" y1="290" x2="143" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="189.5" y1="290" x2="189.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="236" y1="290" x2="236" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="283" y1="290" x2="283" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330" y1="290" x2="330" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="376.5" y1="290" x2="376.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="423" y1="290" x2="423" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="244" x2="470" y2="244" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="198" x2="470" y2="198" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="152" x2="470" y2="152" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="106" x2="470" y2="106" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="60" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="143" y1="290" x2="143" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="189.5" y1="290" x2="189.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="167" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="236" y1="290" x2="236" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="283" y1="290" x2="283" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="260.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$200$</div></foreignObject>
  <line x1="330" y1="290" x2="330" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="376.5" y1="290" x2="376.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="354" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$300$</div></foreignObject>
  <line x1="423" y1="290" x2="423" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$400$</div></foreignObject>
  <line x1="89" y1="244" x2="96" y2="244" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="229.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="89" y1="198" x2="96" y2="198" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="183.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="89" y1="152" x2="96" y2="152" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="137.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="89" y1="106" x2="96" y2="106" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="91.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="89" y1="60" x2="96" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$25$</div></foreignObject>
  <foreignObject x="66" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U\ (\text{kV})$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$P_\text{h} : P\ (\%)$</div></foreignObject>
  <polyline points="161.5,64.5 164,81.5 166.5,96.5 169,109.5 171.5,121.5 174.5,132.5 177,142.5 179.5,151.5 182,159.5 184.5,167 187,174 189.5,180 192.5,186 195,191.5 197.5,196 200,201 202.5,205 205,209 207.5,212.5 210.5,216 213,219.5 215.5,222.5 218,225 220.5,228 223,230.5 225.5,232.5 228.5,235 231,237 233.5,239 236,241 238.5,242.5 241,244 243.5,246 246.5,247.5 249,248.5 251.5,250 254,251.5 256.5,252.5 259,253.5 261.5,255 264.5,256 267,257 269.5,258 272,259 274.5,259.5 277,260.5 279.5,261.5 282.5,262 285,263 287.5,263.5 290,264.5 292.5,265 295,265.5 297.5,266.5 300.5,267 303,267.5 305.5,268 308,268.5 310.5,269 313,269.5 315.5,270 318.5,270.5 321,271 323.5,271.5 326,272 328.5,272 331,272.5 333.5,273 336.5,273.5 339,273.5 341.5,274 344,274.5 346.5,274.5 349,275 351.5,275 354.5,275.5 357,276 359.5,276 362,276.5 364.5,276.5 367,277 369.5,277 372.5,277.5 375,277.5 377.5,278 380,278 382.5,278 385,278.5 387.5,278.5 390.5,279 393,279 395.5,279 398,279.5 400.5,279.5 403,280 405.5,280 408.5,280 411,280.5 413.5,280.5 416,280.5 418.5,280.5 421,281 423.5,281 426.5,281 429,281.5 431.5,281.5 434,281.5 436.5,281.5 439,282 441.5,282 444.5,282 447,282 449.5,282.5 452,282.5 454.5,282.5 457,282.5 459.5,282.5 462.5,283 465,283 467.5,283 470,283" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="189.5" y1="179.5" x2="189.5" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="179.5" x2="189.5" y2="179.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="189.5" cy="179.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="283" y1="262.5" x2="283" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="262.5" x2="283" y2="262.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="283" cy="262.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <line x1="470" y1="283" x2="470" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="283" x2="470" y2="283" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="470" cy="283" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="203.5" y="165" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$12\,\%$</span></div></foreignObject>
  <foreignObject x="289" y="222" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$3{,}0\,\%$</span></div></foreignObject>
  <foreignObject x="383" y="242.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$0{,}75\,\%$</span></div></foreignObject>
  <foreignObject x="300" y="77.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$P = 200\,\text{MW}$</div></foreignObject>
  <foreignObject x="320" y="115.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R = 6{,}0\,\Omega$</div></foreignObject>
</svg>

```pysahdy
Voimalaitos siirtää saman tehon johtoa pitkin. Siirtojännite nostetaan kolminkertaiseksi. Miten johdon häviöteho muuttuu?
---
Virta pienenee kolmasosaan, koska $I = P : U$. Häviöteho $P_\text{h} = R I^2$ pienenee yhdeksäsosaan, koska virran neliö pienenee yhdeksäsosaan.
```

### Todellinen kantaverkko on kolmivaiheinen
Suomen todellinen kantaverkko on kolmivaiheinen. Johdolla on kolme vaihejohdinta. Esimerkiksi $400\,\text{kV}$ on vaihejohtimien välinen jännite. Sitä sanotaan pääjännitteeksi. Kun kolmivaiheverkko on tasaisesti kuormitettu, sen pätöteho on
```latex
P = \sqrt{3}\,U I \cos\varphi
```
Tässä $P$ on siirrettävä pätöteho (W), $U$ on pääjännite (V) ja $I$ on vaihejohtimen virta (A). Merkintä $\cos\varphi$ on tehokerroin. Tehokerroin on yksi, kun virta ja jännite ovat samassa vaiheessa.

Samalla jännitteellä, virralla ja tehokertoimella kolmivaihejohto siirtää noin $1{,}73$-kertaisen tehon kaksijohtimiseen malliin verrattuna. Periaate on silti sama: suuri siirtojännite pienentää virtaa ja häviöitä. Tämän luvun laskutehtävissä käytetään tarkoituksella yksinkertaistettua kaksijohtimista mallia $P = UI$, ellei tehtävässä sanota muuta.

## Esimerkki
Sähköaseman muuntaja laskee alueverkon jännitteen $110\,\text{kV}$ jakeluverkon jännitteeksi $20\,\text{kV}$. Toisiokäämissä on $360$ kierrosta, ja jakeluverkkoon lähtevä virta on $450\,\text{A}$. Kuinka monta kierrosta ensiökäämissä on? Kuinka suuri virta ensiökäämissä kulkee? Muuntaja oletetaan ideaaliseksi.

<!-- vaihe -->

**Tunnetut ja kysytty.** Ensiöjännite on $U_1 = 110\,\text{kV}$ ja toisiojännite $U_2 = 20\,\text{kV}$. Toisiokäämin kierrosten lukumäärä on $N_2 = 360$ ja toisiovirta $I_2 = 450\,\text{A}$.

Kysytään ensiökäämin kierrosten lukumäärää $N_1$ ja ensiövirtaa $I_1$.

<!-- vaihe -->

**Periaate.** Ideaalisessa muuntajassa sama muuttuva magneettivuo kulkee kummankin käämin läpi. Siksi jännitteet suhtautuvat kuten kierrosten lukumäärät. Muuntaja ei kuluta energiaa, joten teho säilyy, $U_1 I_1 = U_2 I_2$. Virrat suhtautuvat siis kääntäen kuten jännitteet.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&\frac{U_1}{U_2} = \frac{N_1}{N_2} \;\Rightarrow\; N_1 = \frac{N_2 U_1}{U_2} \\[6pt]
&\frac{U_1}{U_2} = \frac{I_2}{I_1} \;\Rightarrow\; I_1 = \frac{I_2 U_2}{U_1}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Niitä ei tarvita. Jännitteet ovat kummassakin kaavassa osamääränä, joten kilovoltit supistuvat. Kumpikin jännite on samassa yksikössä, $\text{kV}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&N_1 = \frac{N_2 U_1}{U_2} \\
&= \frac{360 \cdot 110\,\text{kV}}{20\,\text{kV}} \\
&= 1980 \\[6pt]
&I_1 = \frac{I_2 U_2}{U_1} \\
&= \frac{450\,\text{A} \cdot 20\,\text{kV}}{110\,\text{kV}} \\
&= 81{,}82\,\text{A}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Ensiökäämissä on $1980$ kierrosta. Ensiövirta on $I_1 \approx 82\,\text{A}$. Virta ilmoitetaan kahdella merkitsevällä numerolla, kuten jännite $20\,\text{kV}$.

<!-- vaihe -->

**Järkevyys.** Muuntaja laskee jännitettä. Siksi ensiökäämissä on oltava enemmän kierroksia ja pienempi virta kuin toisiokäämissä. Tulos on tällainen. Teho säilyy: $110\,\text{kV} \cdot 81{,}82\,\text{A} = 9{,}0\,\text{MW}$ ja $20\,\text{kV} \cdot 450\,\text{A} = 9{,}0\,\text{MW}$.

## Yleinen virhekäsitys
Moni laskee voimajohdon häviötehon lausekkeella $P = U^2 : R$. Sen jälkeen hän päättelee, että suurempi jännite lisää häviöitä. Lausekkeessa $U$ on kuitenkin vastuksen yli oleva jännite. Siirtojännite on johtimien ja maan tai johtimien keskinäinen jännite. Johdon resistanssin yli on vain pieni jännitehäviö $R I$.

Oikea tapa on laskea ensin virta $I = P : U$ ja sitten häviöteho $P_\text{h} = R I^2$. Suurempi jännite pienentää virtaa ja häviöitä.

Toinen virhe on ajatella, että jännitettä nostava muuntaja lisää tehoa. Ideaalisessa muuntajassa teho säilyy. Kun jännite kasvaa, virta pienenee. Kolmas virhe on olettaa, että muuntaja toimii myös akulla. Muuntaja tarvitsee muuttuvan magneettivuon, eli vaihtovirran.

## Tiivistelmä
- Muuntajassa ensiökäämin vaihtovirta synnyttää rautasydämeen muuttuvan magneettivuon. Vuo indusoi toisiokäämiin vaihtojännitteen. Tasavirralla vuo ei muutu, eikä muuntaja toimi.
- Ideaalisessa muuntajassa $U_1 : U_2 = N_1 : N_2 = I_2 : I_1$. Teho säilyy, joten jännitteen kasvaessa virta pienenee.
- Siirtojohdon häviöteho on $P_\text{h} = R I^2$, missä $I = P : U$. Kaksinkertainen siirtojännite pienentää häviöt neljäsosaan.
- Sähkö siirretään pitkiä matkoja suurjännitteellä. Suomen kantaverkon jännitteet ovat $400\,\text{kV}$, $220\,\text{kV}$ ja $110\,\text{kV}$. Muuntajat laskevat jännitteen vaiheittain pienjänniteverkon $400\,\text{V}$:iin ja $230\,\text{V}$:iin.
- Laskuissa käytetään yksinkertaistettua kaksijohtimista mallia $P = UI$. Todellinen kantaverkko on kolmivaiheinen: $400\,\text{kV}$ on pääjännite, ja pätöteho on $P = \sqrt{3}\,U I \cos\varphi$.
