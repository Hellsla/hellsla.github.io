Kuvaaja näyttää yhdellä silmäyksellä, miten kaksi mitattua suuretta riippuvat toisistaan. Hyvästä kuvaajasta näkee, sopivatko mittaukset malliin, ja siitä voi määrittää tutkittavan suureen.

## Mihin tarvitset tätä

Lähes jokaisessa tutkimuksessa tulokset esitetään kuvaajana. Tutkimuksessa *Jousivakion määrittäminen* piirrät jousivoiman venymän funktiona ja tutkimuksessa *Kuuman veden jäähtyminen* lämpötilan ajan funktiona. Kuvaaja on myös lähtökohta seuraaville vaiheille: [[ohje:tvt-suoran-sovitus|suoran sovittamiselle]] ja [[ohje:tvt-kulmakerroin|kulmakertoimen tulkinnalle]].

## Työvaiheet

Ohje on kirjoitettu Graphical Analysis Prolle, mutta samat periaatteet pätevät käsin piirrettyyn kuvaajaan.

1. **Valitse akselit.** Vaaka-akselille tulee yleensä suure, jonka arvot valitset itse tai joka etenee tasaisesti, kuten aika. Pystyakselille tulee suure, joka määräytyy sen mukaan. Jos tutkimuksen malli kertoo, millä akseleilla kuvaajasta tulee suora, käytä niitä. Tutkimuksessa *Putoamiskiihtyvyyden määrittäminen heilurin avulla* pystyakselille tulee jaksonajan neliö $T^2$ ja vaaka-akselille heilurin pituus $l$. Napsauta ohjelmassa pystyakselin otsikkoa ja valitse piirrettävä sarake, ja napsauta vaaka-akselin otsikkoa ja valitse vaaka-akselin sarake.

2. **Anna akseleille suureet ja yksiköt.** Akselin otsikko tulee sarakkeen nimestä ja yksiköstä, jotka annat valinnassa **Column Options** ([[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]]). Otsikossa on suureen tunnus ja yksikkö, esimerkiksi $l\ (\text{m})$ tai $F\ (\text{N})$. Laskettu suure saa lasketun yksikön: $T^2\ (\text{s}^2)$.

3. **Valitse asteikot.** Asteikon jaot ovat tasavälisiä: yhtä pitkä väli akselilla tarkoittaa aina yhtä suurta muutosta suureessa. Pisteiden pitää täyttää suurin osa kuvaajasta. Avaa **Graph Tools** ja valitse **Edit Graph Options**. Asteikoksi voit valita **Automatic**, **Always Show 0** tai **Manual**, jolloin kirjoitat akselin rajat itse. Näytä nollakohta, kun se on tärkeä, esimerkiksi kun haluat nähdä, kulkeeko suora origon kautta. Jos kaikki lukemat ovat kaukana nollasta, kuten lämpötilat $60\,{}^\circ\text{C}$:n ja $80\,{}^\circ\text{C}$:n välillä, nollasta alkava akseli litistäisi pisteet kapeaksi nauhaksi. Kun haluat taas nähdä kaikki pisteet, valitse **Zoom to all Data**.

4. **Näytä mittauspisteet, älä murtoviivaa.** Jokainen mittaus on yksi piste. Valitse samasta asetusikkunasta näyttötavaksi **Points**, jolloin pisteitä ei yhdistetä. Murtoviiva seuraisi myös mittausten satunnaisia virheitä, eikä se ole malli. Anturin tiheässä aikasarjassa, kuten jäähtymiskäyrässä, ohjelma käyttää yleensä näyttötapaa **Lines**, ja se sopii, kun lukemia on satoja. Näyttötapa **Both** näyttää sekä pisteet että viivan.

5. **Merkitse epävarmuus.** Jos tiedät mittauksen epävarmuuden, näytä jokaisen pisteen kohdalla epävarmuusjana. Pystysuora jana ulottuu arvosta $y - \Delta y$ arvoon $y + \Delta y$, ja vaakasuoran janan saat samalla tavalla epävarmuudesta $\Delta x$. Janat näyttävät, kuinka tarkasti pisteen paikka tiedetään, ja niitä tarvitaan, kun arvioit [[ohje:tvt-epavarmuus|kulmakertoimen epävarmuutta]]. Graphical Analysis Prossa epävarmuusjanat ovat Pro-ominaisuus; kysy opettajalta, jos et löydä asetusta.

    Vertaa kuvan kahta kuvaajaa. Ylemmästä ei näe, mitä akseleilla on, pisteet on yhdistetty murtoviivalla, ja pystyakselin asteikko on niin suuri, että pisteet ovat litistyneet alareunaan. Alemmassa on suureet ja yksiköt, pisteiden täyttämät asteikot ja epävarmuusjanat.

    <svg data-fig="good-bad" viewBox="0 0 600 640" role="img" aria-label="Kaksi kuvaajaa samasta keksitystä esimerkkiaineistosta, heilurin jaksonajan neliöstä pituuden funktiona. Ylempi kuvaaja on puutteellinen: akseleilla ei ole suureita eikä yksiköitä, vaan kysymysmerkit, pystyakselin asteikko ulottuu kahteenkymmeneen, joten pisteet ovat litistyneet kuvaajan alareunaan, ja pisteet on yhdistetty murtoviivalla. Alempi kuvaaja on hyvä: vaaka-akselilla on l metreinä ja pystyakselilla T toiseen sekunnin neliöinä, asteikot on valittu niin, että pisteet täyttävät kuvaajan, ja jokaisessa pisteessä on pystysuora epävarmuusjana. Pisteitä ei ole yhdistetty." style="max-width:100%;font-size:24px">
  <line x1="185" y1="270" x2="185" y2="80" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="280" y1="270" x2="280" y2="80" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="375" y1="270" x2="375" y2="80" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="270" x2="470" y2="80" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="222.5" x2="470" y2="222.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="175" x2="470" y2="175" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="127.5" x2="470" y2="127.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="80" x2="470" y2="80" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="89" y1="270" x2="484" y2="270" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,270 L483,276 L483,264 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="271" x2="90" y2="66" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,54 L96,67 L84,67 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="185" y1="270" x2="185" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="162.5" y="279.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}2$</div></foreignObject>
  <line x1="280" y1="270" x2="280" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="257.5" y="279.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}4$</div></foreignObject>
  <line x1="375" y1="270" x2="375" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="352.5" y="279.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}6$</div></foreignObject>
  <line x1="470" y1="270" x2="470" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="279.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}8$</div></foreignObject>
  <line x1="83" y1="222.5" x2="90" y2="222.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="58" y="208" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="83" y1="175" x2="90" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="160.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="83" y1="127.5" x2="90" y2="127.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="113" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$15$</div></foreignObject>
  <line x1="83" y1="80" x2="90" y2="80" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="45" y="65.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <foreignObject x="60" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="255.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{?}$</div></foreignObject>
  <foreignObject x="80" y="23.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{?}$</div></foreignObject>
  <polyline points="185,262 232.5,259 280,254 327.5,251.5 375,246 422.5,244" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="185" cy="262" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="232.5" cy="259" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="280" cy="254" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="327.5" cy="251.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="375" cy="246" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="422.5" cy="244" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="233.5" y="190.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{murtoviiva}$</span></div></foreignObject>
  <foreignObject x="418" y="25.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{puutteellinen}$</div></foreignObject>
  <line x1="30" y1="322" x2="570" y2="322" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="192.5" y1="590" x2="192.5" y2="400" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="285" y1="590" x2="285" y2="400" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="377.5" y1="590" x2="377.5" y2="400" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="590" x2="470" y2="400" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="558.5" x2="470" y2="558.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="526.5" x2="470" y2="526.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="495" x2="470" y2="495" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="463.5" x2="470" y2="463.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="431.5" x2="470" y2="431.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="400" x2="470" y2="400" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="590" x2="484" y2="590" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,590 L483,596 L483,584 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="591" x2="100" y2="386" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,374 L106,387 L94,387 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="192.5" y1="590" x2="192.5" y2="597" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="170" y="599.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}2$</div></foreignObject>
  <line x1="285" y1="590" x2="285" y2="597" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="262.5" y="599.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}4$</div></foreignObject>
  <line x1="377.5" y1="590" x2="377.5" y2="597" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="355" y="599.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}6$</div></foreignObject>
  <line x1="470" y1="590" x2="470" y2="597" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="599.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}8$</div></foreignObject>
  <line x1="93" y1="558.5" x2="100" y2="558.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="526.5" x2="100" y2="526.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="68" y="512" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="93" y1="495" x2="100" y2="495" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="463.5" x2="100" y2="463.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="68" y="449" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="93" y1="431.5" x2="100" y2="431.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="93" y1="400" x2="100" y2="400" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="68" y="385.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <foreignObject x="70" y="595.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="575.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$l\ (\text{m})$</div></foreignObject>
  <foreignObject x="90" y="343.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T^2\ (\text{s}^2)$</div></foreignObject>
  <line x1="192.5" y1="545" x2="192.5" y2="526" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="185.5" y1="545" x2="199.5" y2="545" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="185.5" y1="526" x2="199.5" y2="526" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="192.5" cy="535.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="238.5" y1="527.5" x2="238.5" y2="508.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="231.5" y1="527.5" x2="245.5" y2="527.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="231.5" y1="508.5" x2="245.5" y2="508.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="238.5" cy="518" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="285" y1="494.5" x2="285" y2="475.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="278" y1="494.5" x2="292" y2="494.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="278" y1="475.5" x2="292" y2="475.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="285" cy="485" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="331" y1="474.5" x2="331" y2="455.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="324" y1="474.5" x2="338" y2="474.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="324" y1="455.5" x2="338" y2="455.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="331" cy="465" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="377.5" y1="441" x2="377.5" y2="422" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="370.5" y1="441" x2="384.5" y2="441" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="370.5" y1="422" x2="384.5" y2="422" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="377.5" cy="431.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="423.5" y1="424.5" x2="423.5" y2="405.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="416.5" y1="424.5" x2="430.5" y2="424.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="416.5" y1="405.5" x2="430.5" y2="405.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <circle cx="423.5" cy="415" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="530" y="345.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{hyvä}$</div></foreignObject>
  <foreignObject x="258" y="545.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{esimerkkiaineisto}$</span></div></foreignObject>
</svg>

6. **Tee yksi kuvaaja kutakin kysymystä kohti.** Jokainen tutkittava riippuvuus saa oman kuvaajansa. Jos vertaat kahta mittaussarjaa, esimerkiksi kahta eri jousta, voit näyttää ne samassa kuvaajassa, kun akseleilla on samat suureet. Anna sarjoille eri merkit valinnalla **Point Symbols** (pystyakselin otsikon kautta avautuvassa **Plot Manager** -näkymässä) ja lisää selite valinnalla **Graph Legend**.

7. **Anna otsikko ja vie kuvaaja.** Kirjoita kuvaajalle otsikko valinnassa **Edit Graph Options** ja vie kuvaaja kuvatiedostoksi valinnalla **Export graph as png**. Numeroi kuvaaja työselostuksessa ja kirjoita sen alle kuvateksti, esimerkiksi "Kuva 1. Heilurin jaksonajan neliö pituuden funktiona." Lisää neuvoja on ohjeessa [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]].

## Tavallisimmat virheet

- **Akseleilta puuttuu suure tai yksikkö.** Huomaat sen, kun et pysty sanomaan, mitä akselin luku $2$ tarkoittaa. Anna sarakkeille nimet ja yksiköt valinnassa **Column Options**.
- **Pisteet on yhdistetty murtoviivalla.** Kuvaaja näyttää sahalaidalta, vaikka riippuvuus on tasainen. Valitse näyttötavaksi **Points** ja [[ohje:tvt-suoran-sovitus|sovita pisteisiin malli]].
- **Akselilla on väärä sarake.** Kuvaajan muoto on odottamaton, tai pystyakselilla on esimerkiksi $T$, vaikka piti olla $T^2$. Napsauta akselin otsikkoa ja valitse oikea sarake.
- **Akselit ovat mallin kannalta väärin päin.** Kulmakerroin ei silloin ole etsimäsi suure vaan esimerkiksi sen käänteisluku. Tarkista mallista, kumpi suure kuuluu pystyakselille.
- **Asteikko on liian suuri tai liian pieni.** Pisteet ovat pienessä kasassa tai osa niistä jää kuvaajan ulkopuolelle. Valitse **Zoom to all Data** tai muuta akselien rajoja.

## Tarkista ennen kuin jatkat

- Kummallakin akselilla on suureen tunnus ja yksikkö.
- Pisteet täyttävät suurimman osan kuvaajasta, eikä niitä ole yhdistetty murtoviivalla.
- Epävarmuusjanat on näytetty, jos epävarmuus tunnetaan.
- Kuvaajalla on otsikko, ja työselostuksessa sillä on numero ja kuvateksti.
